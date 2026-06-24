#!/usr/bin/env python3
"""Generate manual-VEX candidates from the latest Trivy scan report.

For every Go-binary CVE in a committed ``reports/scan-*.md`` report this script
determines whether the *vulnerable package* (not just the module) is actually
linked into the shipped binary. It uses two complementary, stripping-tolerant
techniques:

1. pclntab presence test (primary). Go keeps its function-name table (pclntab)
   even when the binary is fully stripped (``-ldflags=-s -w``; ``go tool nm``
   returns nothing). If none of a CVE's vulnerable packages appear in that table
   the linker dead-code-eliminated them => ``vulnerable_code_not_present``.

2. govulncheck binary mode (secondary, non-stripped binaries only). When a
   binary still carries symbols, govulncheck's reachability analysis can show a
   linked-but-unreachable package => ``vulnerable_code_not_in_execute_path``.
   It is deliberately skipped on stripped binaries, where binary mode
   over-reports by echoing the OSV's declared symbols.

The vulnerable package for each CVE is resolved authoritatively from the OSV Go
vulnerability database (``api.osv.dev``) keyed by module + installed version, so
genuinely-linked packages (e.g. ``x/net/http2``/``idna``) are never VEXed.

Output: a JSON detail file, an image-scanning-compatible ``text-vex`` CSV block
and a ready-to-file GitHub issue body.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

OSV_QUERY_URL = "https://api.osv.dev/v1/query"

# Modules whose CVEs we evaluate. The technique is general, but we focus on the
# x/net and x/crypto storm by default. Override with --modules.
DEFAULT_MODULES = ["golang.org/x/net", "golang.org/x/crypto"]

# Registry hosts stripped from image refs so they match image-scanning targets
# (e.g. registry.rancher.com/rancher/foo -> rancher/foo).
KNOWN_REGISTRY_HOSTS = ("registry.rancher.com", "docker.io", "index.docker.io")


# --------------------------------------------------------------------------- #
# Report parsing
# --------------------------------------------------------------------------- #
def find_latest_report(reports_dir: Path) -> Path | None:
    """Return the newest dated scan report (scan-YYYYMMDD-N.md)."""
    best = None
    best_key = None
    pat = re.compile(r"scan-(\d{8})-(\d+)\.md$")
    for p in reports_dir.glob("scan-*.md"):
        m = pat.search(p.name)
        if not m:
            continue
        key = (m.group(1), int(m.group(2)))
        if best_key is None or key > best_key:
            best_key, best = key, p
    return best


def _split_row(line: str) -> list[str] | None:
    """Split a Trivy box-table data row into trimmed cells, else None."""
    if "│" not in line:
        return None
    # Strip leading/trailing border, then split on the inner separators.
    inner = line.strip().strip("│")
    return [c.strip() for c in inner.split("│")]


def parse_report(path: str) -> tuple[list[str], list[dict]]:
    """Parse a scan report into (images, findings).

    findings: list of dicts {image, target, module, installed, fixed, cve}
    limited to gobinary targets.
    """
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    images: list[str] = []
    findings: list[dict] = []

    cur_image = None
    cur_target = None
    in_gobinary = False
    # Carried-forward (rowspan) cells.
    last_lib = last_installed = last_fixed = None

    header_re = re.compile(r"^##\s+Scan Results:\s+`([^`]+)`")
    img_bullet_re = re.compile(r"^[-*]\s+`([^`]+)`")
    target_re = re.compile(r"^(\S.*?)\s+\((\w[\w-]*)\)\s*$")
    cve_re = re.compile(r"^CVE-\d{4}-\d+$")
    section = None  # None | "images"

    for line in lines:
        if line.startswith("## Images Scanned"):
            section = "images"
            continue
        hm = header_re.match(line)
        if hm:
            cur_image = hm.group(1)
            cur_target = None
            in_gobinary = False
            section = None
            continue
        if section == "images":
            bm = img_bullet_re.match(line)
            if bm:
                images.append(bm.group(1))
                continue
            if line.startswith("## "):
                section = None

        if cur_image is None:
            continue

        tm = target_re.match(line)
        if tm and not line.startswith("│") and not line.startswith("#"):
            cur_target = tm.group(1).strip()
            in_gobinary = tm.group(2) == "gobinary"
            last_lib = last_installed = last_fixed = None
            continue

        if not in_gobinary or cur_target is None:
            continue

        cells = _split_row(line)
        if not cells or len(cells) < 6:
            continue
        # Expected columns: Library, Vulnerability, Severity, Status,
        # Installed Version, Fixed Version, Title
        lib, vuln, _sev, _status, installed, fixed = cells[0], cells[1], cells[2], cells[3], cells[4], cells[5]
        if lib in ("Library", ""):
            if lib == "Library":
                continue
        if lib:
            last_lib = lib
        if installed:
            last_installed = installed
        if fixed:
            last_fixed = fixed
        if cve_re.match(vuln):
            findings.append({
                "image": cur_image,
                "target": cur_target,
                "module": last_lib,
                "installed": last_installed,
                "fixed": last_fixed,
                "cve": vuln,
            })

    # De-dupe images preserving order.
    seen = set()
    uniq_images = [i for i in images if not (i in seen or seen.add(i))]
    return uniq_images, findings


# --------------------------------------------------------------------------- #
# OSV: CVE -> vulnerable package paths
# --------------------------------------------------------------------------- #
def osv_query(module: str, version: str) -> dict:
    version = version.lstrip("v")
    body = json.dumps({"package": {"ecosystem": "Go", "name": module}, "version": version}).encode()
    req = urllib.request.Request(OSV_QUERY_URL, data=body, headers={"Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
    return {}


def build_osv_map(module: str, version: str) -> dict[str, dict]:
    """Return {CVE: {"pkgs": set(import paths), "goid": GO-id}} for module@version."""
    out: dict[str, dict] = {}
    data = osv_query(module, version)
    for v in data.get("vulns", []):
        goid = v.get("id", "")
        pkgs: set[str] = set()
        for aff in v.get("affected", []):
            if aff.get("package", {}).get("name") != module:
                continue
            for imp in aff.get("ecosystem_specific", {}).get("imports", []):
                if imp.get("path"):
                    pkgs.add(imp["path"])
        cves = [a for a in v.get("aliases", []) if a.startswith("CVE-")]
        if goid.startswith("CVE-"):
            cves.append(goid)
        for cve in cves:
            out[cve] = {"pkgs": pkgs, "goid": goid}
    return out


# --------------------------------------------------------------------------- #
# Image extraction + binary inspection
# --------------------------------------------------------------------------- #
def extract_image(image: str, dest: Path) -> bool:
    """Copy + flatten an image's layers into dest. Returns success."""
    raw = tempfile.mkdtemp(prefix="oci-")
    try:
        cmd = ["skopeo", "copy", "-q", "--override-os", "linux", "--override-arch", "amd64",
               f"docker://{image}", f"dir:{raw}"]
        if subprocess.run(cmd, capture_output=True).returncode != 0:
            return False
        manifest = json.loads(Path(raw, "manifest.json").read_text())
        for layer in manifest.get("layers", []):
            digest = layer["digest"].split(":", 1)[1]
            blob = Path(raw, digest)
            if not blob.exists():
                continue
            # Extract each layer in order; later layers overwrite earlier ones
            # so we end up with the final image state. tar auto-detects gzip.
            subprocess.run(["tar", "-xf", str(blob), "-C", str(dest)], capture_output=True)
        return True
    except Exception:
        return False
    finally:
        shutil.rmtree(raw, ignore_errors=True)


def is_stripped(binary: Path) -> bool:
    try:
        out = subprocess.run(["go", "tool", "nm", str(binary)], capture_output=True, text=True)
        if out.returncode != 0:
            return True
        return len([l for l in out.stdout.splitlines() if l.strip()]) == 0
    except Exception:
        return True


def linked_symbol_blob(binary: Path) -> str:
    """All pclntab-ish strings from the binary (one big lowercase-safe blob)."""
    out = subprocess.run(["strings", "-n", "8", str(binary)], capture_output=True, text=True)
    return out.stdout


def package_present(blob: str, pkg: str) -> bool:
    """True if package `pkg`'s own functions appear in the symbol blob.

    Matches ``pkg.<ident>`` exactly so that a parent package match does not
    leak from a child (e.g. ``.../ssh`` vs ``.../ssh/agent``).
    """
    esc = re.escape(pkg)
    return re.search(esc + r"\.[A-Za-z(]", blob) is not None


def govulncheck_not_affected(binary: Path) -> set[str]:
    """Return GO-ids govulncheck binary mode marks not_affected (best effort)."""
    exe = shutil.which("govulncheck")
    if not exe:
        return set()
    try:
        out = subprocess.run([exe, "-mode", "binary", "-format", "openvex", str(binary)],
                             capture_output=True, text=True, timeout=300)
        if out.returncode != 0 or not out.stdout.strip():
            return set()
        doc = json.loads(out.stdout)
        ids = set()
        for st in doc.get("statements", []):
            if st.get("status") == "not_affected":
                name = st.get("vulnerability", {}).get("name") or st.get("vulnerability", {}).get("@id", "")
                if name:
                    ids.add(name)
        return ids
    except Exception:
        return set()


def find_binary(root: Path, target: str) -> Path | None:
    cand = root / target.lstrip("/")
    if cand.is_file():
        return cand
    # Fall back to basename search (handles symlinks / path drift).
    base = os.path.basename(target.rstrip("/"))
    for p in root.rglob(base):
        if p.is_file() and not p.is_symlink():
            return p
    return None


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def short_image(image: str) -> str:
    first = image.split("/", 1)[0]
    if first in KNOWN_REGISTRY_HOSTS or ("." in first or ":" in first) and "/" in image:
        return image.split("/", 1)[1]
    return image


def vex_note(target: str, pkgs: list[str], module: str, installed: str, justification: str) -> str:
    pkg_list = ", ".join(pkgs)
    if justification == "vulnerable_code_not_present":
        return (f"`{target}` does not link {pkg_list}; the Go function-name table (pclntab, retained "
                f"despite -s -w stripping) contains no matching symbols at {module} {installed}. "
                f"Vulnerable code not present.")
    return (f"`{target}`: govulncheck (binary mode) reports the vulnerable symbols in {pkg_list} are not "
            f"reachable at {module} {installed}. Vulnerable code not in execute path.")


# --------------------------------------------------------------------------- #
# Main analysis
# --------------------------------------------------------------------------- #
def analyze(images: list[str], findings: list[dict], modules: list[str]) -> dict:
    findings = [f for f in findings if f["module"] in modules and f["installed"]]

    # OSV map cache keyed by (module, installed).
    osv_cache: dict[tuple[str, str], dict] = {}

    def osv_for(module: str, installed: str) -> dict:
        key = (module, installed)
        if key not in osv_cache:
            try:
                osv_cache[key] = build_osv_map(module, installed)
            except Exception as exc:  # noqa: BLE001
                print(f"  ! OSV query failed for {module}@{installed}: {exc}", file=sys.stderr)
                osv_cache[key] = {}
        return osv_cache[key]

    # Group findings by image.
    by_image: dict[str, list[dict]] = defaultdict(list)
    for f in findings:
        by_image[f["image"]].append(f)

    candidates: list[dict] = []
    present: list[dict] = []      # genuinely linked -> not VEXed
    undetermined: list[dict] = [] # couldn't resolve package / binary
    image_status: dict[str, str] = {}

    for image, fs in by_image.items():
        print(f"==> {image} ({len(fs)} candidate findings)", file=sys.stderr)
        with tempfile.TemporaryDirectory(prefix="fs-") as td:
            root = Path(td)
            if not extract_image(image, root):
                image_status[image] = "extract_failed"
                for f in fs:
                    undetermined.append({**f, "reason": "image_extract_failed"})
                continue
            image_status[image] = "ok"

            # Cache per-binary inspection.
            blob_cache: dict[str, str] = {}
            stripped_cache: dict[str, bool] = {}
            gv_cache: dict[str, set[str]] = {}

            # Group by target binary.
            by_target: dict[str, list[dict]] = defaultdict(list)
            for f in fs:
                by_target[f["target"]].append(f)

            for target, tfs in by_target.items():
                binary = find_binary(root, target)
                if binary is None:
                    for f in tfs:
                        undetermined.append({**f, "reason": "binary_not_found"})
                    continue
                bkey = str(binary)
                if bkey not in blob_cache:
                    blob_cache[bkey] = linked_symbol_blob(binary)
                    stripped_cache[bkey] = is_stripped(binary)
                blob = blob_cache[bkey]
                stripped = stripped_cache[bkey]
                if not stripped and bkey not in gv_cache:
                    gv_cache[bkey] = govulncheck_not_affected(binary)
                gv_ids = gv_cache.get(bkey, set())

                for f in tfs:
                    omap = osv_for(f["module"], f["installed"])
                    entry = omap.get(f["cve"])
                    if not entry or not entry["pkgs"]:
                        undetermined.append({**f, "reason": "no_osv_package_mapping"})
                        continue
                    pkgs = sorted(entry["pkgs"])
                    linked = any(package_present(blob, p) for p in pkgs)
                    rec = {**f, "pkgs": pkgs, "stripped": stripped}
                    if not linked:
                        rec["justification"] = "vulnerable_code_not_present"
                        rec["method"] = "pclntab"
                        candidates.append(rec)
                    elif not stripped and (f["cve"] in gv_ids or entry["goid"] in gv_ids):
                        rec["justification"] = "vulnerable_code_not_in_execute_path"
                        rec["method"] = "govulncheck"
                        candidates.append(rec)
                    else:
                        present.append(rec)

    return {
        "candidates": candidates,
        "present": present,
        "undetermined": undetermined,
        "image_status": image_status,
    }


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def render_textvex(candidates: list[dict]) -> str:
    rows = []
    for c in sorted(candidates, key=lambda x: (x["image"], x["target"], x["cve"])):
        img = short_image(c["image"])
        target = c["target"].lstrip("/")
        ver = c["installed"]
        if not ver.startswith("v"):
            ver = "v" + ver
        note = vex_note(target, c["pkgs"], c["module"], ver, c["justification"])
        rows.append(f'{img},{c["cve"]},{c["module"]},{ver},{target},not_affected,{c["justification"]},"{note}"')
    return "\n".join(rows)


def render_issue(report_name: str, result: dict, modules: list[str]) -> str:
    cands = result["candidates"]
    present = result["present"]
    undet = result["undetermined"]

    # Per-image / per-justification counts.
    by_img = defaultdict(lambda: defaultdict(int))
    for c in cands:
        by_img[short_image(c["image"])][c["justification"]] += 1

    lines = []
    lines.append(f"## Manual VEX candidates — `{report_name}`")
    lines.append("")
    lines.append(
        "Automated triage of the Go-binary CVEs in the latest Trivy scan, scoped to "
        f"`{'`, `'.join(modules)}`. Each candidate below was checked for **package-level "
        "presence in the actual shipped binary**, which the upstream govulncheck-based "
        "auto-VEX pipeline cannot determine for stripped binaries scanned at module granularity."
    )
    lines.append("")
    lines.append("### Method")
    lines.append(
        "- **pclntab presence test** (primary): a binary's Go function-name table survives "
        "`-s -w` stripping (`go tool nm` returns 0 symbols). If none of a CVE's vulnerable "
        "packages — resolved from the OSV Go database by module+version — appear in that table, "
        "the linker eliminated them ⇒ `vulnerable_code_not_present`.\n"
        "- **govulncheck binary mode** (secondary, non-stripped binaries only): a linked-but-"
        "unreachable package ⇒ `vulnerable_code_not_in_execute_path`. Skipped on stripped "
        "binaries where it over-reports.\n"
        "- Genuinely-linked packages (e.g. `x/net/http2`, `x/net/idna`) are intentionally left "
        "as real findings."
    )
    lines.append("")
    if not cands:
        lines.append("> No VEX candidates found in this scan — every flagged vulnerable package is "
                     "linked into its binary, or no mapping/binary was resolvable.")
    else:
        lines.append(f"### Candidates ({len(cands)})")
        lines.append("")
        lines.append("| image | not_present | not_in_execute_path |")
        lines.append("|---|---|---|")
        for img in sorted(by_img):
            d = by_img[img]
            lines.append(f"| `{img}` | {d.get('vulnerable_code_not_present', 0)} | "
                         f"{d.get('vulnerable_code_not_in_execute_path', 0)} |")
        lines.append("")
        lines.append("Paste the block below into a `rancher/image-scanning` VEX issue after validating:")
        lines.append("")
        lines.append("```text-vex")
        lines.append(render_textvex(cands))
        lines.append("```")

    if present:
        genuine = sorted({(short_image(c["image"]), c["target"], "/".join(c["pkgs"])) for c in present})
        lines.append("")
        lines.append("<details><summary>Left as genuine findings (vulnerable package IS linked) — "
                     f"{len(present)} rows</summary>")
        lines.append("")
        for img, tgt, pk in genuine[:200]:
            lines.append(f"- `{img}` `{tgt}` — {pk}")
        lines.append("")
        lines.append("</details>")

    if undet:
        reasons = defaultdict(int)
        for u in undet:
            reasons[u.get("reason", "unknown")] += 1
        lines.append("")
        lines.append("<details><summary>Undetermined (needs manual review) — "
                     f"{len(undet)} rows</summary>")
        lines.append("")
        for r, n in sorted(reasons.items()):
            lines.append(f"- {r}: {n}")
        lines.append("")
        lines.append("</details>")

    lines.append("")
    lines.append("<sub>Generated by `.github/scripts/vex_candidates.py`. Validate before transferring "
                 "to `rancher/image-scanning`.</sub>")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report", help="Path to a scan-*.md report (default: latest in reports/).")
    ap.add_argument("--reports-dir", default="reports", help="Directory holding scan-*.md reports.")
    ap.add_argument("--modules", default=",".join(DEFAULT_MODULES),
                    help="Comma-separated Go modules to evaluate.")
    ap.add_argument("--out-json", default="vex-candidates.json")
    ap.add_argument("--out-vex", default="vex-candidates.text-vex")
    ap.add_argument("--out-issue", default="vex-candidates-issue.md")
    ap.add_argument("--github-output", help="Append key=value outputs here (GITHUB_OUTPUT).")
    args = ap.parse_args()

    report = args.report
    if not report:
        latest = find_latest_report(Path(args.reports_dir))
        if not latest:
            print("No scan-*.md report found.", file=sys.stderr)
            return 1
        report = str(latest)
    report_name = Path(report).stem
    modules = [m.strip() for m in args.modules.split(",") if m.strip()]

    print(f"Report: {report}", file=sys.stderr)
    images, findings = parse_report(report)
    print(f"Parsed {len(images)} images, {len(findings)} gobinary CVE rows.", file=sys.stderr)

    result = analyze(images, findings, modules)
    result["report"] = report_name
    result["modules"] = modules

    Path(args.out_json).write_text(json.dumps(result, indent=2, default=list))
    Path(args.out_vex).write_text(render_textvex(result["candidates"]) + "\n")
    Path(args.out_issue).write_text(render_issue(report_name, result, modules))

    n = len(result["candidates"])
    print(f"\nCandidates: {n}  |  genuine: {len(result['present'])}  |  "
          f"undetermined: {len(result['undetermined'])}", file=sys.stderr)

    if args.github_output:
        with open(args.github_output, "a") as fh:
            fh.write(f"candidate_count={n}\n")
            fh.write(f"report_name={report_name}\n")
            fh.write(f"issue_body_file={args.out_issue}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
