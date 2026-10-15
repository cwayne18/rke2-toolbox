#!/usr/bin/env python3
"""Generate manual-VEX candidates using vexscan instead of the in-tree analysis.

This is a drop-in replacement for ``vex_candidates.py``'s *analysis core*. It
reuses that module's report parser and renderers verbatim so the downstream
contract is byte-for-byte identical:

* ``vex-candidates.text-vex``  - CSV block consumed by rancher/image-scanning
* ``vex-candidates-issue.md``  - GitHub issue body
* ``vex-candidates.json``      - row-level detail
* GITHUB_OUTPUT keys           - candidate_count, report_name, issue_body_file

The only thing that changes is *how* a Go-binary CVE is judged present. Instead
of skopeo-extracting the image, hunting the binary, running strings/pclntab and
govulncheck by hand, and mapping CVEs to packages via OSV, we shell out to
``vexscan`` (github.com/cwayne18/vexscan), which does exactly that analysis --
the same pclntab + govulncheck technique this script pioneered as ``gomod-vex``
-- but reads the image directly and resolves versions from build info.

vexscan JSON (schema_version 2) findings carry: cve, module/package, version,
location (binary path), packages[] (the vulnerable import paths), granularity,
stripped, and status in {linked, not_present, not_in_execute_path,
undetermined}. We bucket those into the same candidate/present/undetermined
shape the renderers expect.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# Reuse the parser + renderers from the existing script so output is identical.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vex_candidates as legacy  # noqa: E402

DEFAULT_MODULES = legacy.DEFAULT_MODULES

# vexscan status -> (justification, method) used by the renderers.
STATUS_MAP = {
    "not_present": "vulnerable_code_not_present",
    "not_in_execute_path": "vulnerable_code_not_in_execute_path",
}


def run_vexscan(image: str, modules: list[str], cves: list[str], vexscan_bin: str) -> dict | None:
    """Run vexscan for one image scoped to the given Go modules + CVE ids.

    Returns the parsed JSON document, or None if vexscan could not analyze the
    image (extract failure, tool error). Findings for modules the binary does
    not link come back as undetermined/no_component_matched and are handled by
    the caller.
    """
    cmd = [
        vexscan_bin,
        "--image", image,
        "--package", "golang:" + ",".join(modules),
        "--format", "json",
    ]
    if cves:
        cmd += ["--cves", ",".join(sorted(set(cves)))]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"  ! vexscan invocation failed for {image}: {exc}", file=sys.stderr)
        return None
    if not out.stdout.strip():
        print(f"  ! vexscan produced no JSON for {image} (exit {out.returncode}): "
              f"{out.stderr.strip().splitlines()[-1] if out.stderr.strip() else ''}",
              file=sys.stderr)
        return None
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError as exc:
        print(f"  ! vexscan JSON parse failed for {image}: {exc}", file=sys.stderr)
        return None


def analyze(images: list[str], findings: list[dict], modules: list[str],
            vexscan_bin: str) -> dict:
    """Judge Go-binary CVEs via vexscan, bucketed for the legacy renderers."""
    findings = [f for f in findings if f["module"] in modules and f["installed"]]

    # Which CVE ids to focus vexscan on, per image (from the Trivy report).
    cves_by_image: dict[str, set[str]] = defaultdict(set)
    for f in findings:
        cves_by_image[f["image"]].add(f["cve"])

    # Report-declared rows keyed for cross-referencing vexscan output back to a
    # Trivy target (so an undetermined vexscan result still lists the finding).
    # Group by the image the finding was reported under -- the "Scan Results"
    # header -- which is authoritative and may include images not repeated in
    # the "Images Scanned" bullet list.
    report_rows: dict[str, list[dict]] = defaultdict(list)
    for f in findings:
        report_rows[f["image"]].append(f)

    candidates: list[dict] = []
    present: list[dict] = []
    undetermined: list[dict] = []
    image_status: dict[str, str] = {}

    for image, rows in report_rows.items():
        print(f"==> {image} ({len(rows)} candidate findings)", file=sys.stderr)
        doc = run_vexscan(image, modules, sorted(cves_by_image[image]), vexscan_bin)
        if doc is None:
            image_status[image] = "vexscan_failed"
            for f in rows:
                undetermined.append({**f, "reason": "vexscan_failed"})
            continue
        image_status[image] = "ok"

        # A report row supplies only fallback fields (vexscan's own binary,
        # version and vulnerable-package list are authoritative). Index one row
        # per (cve, module) for that fallback, and track which keys vexscan
        # actually resolved so unresolved report rows can be flagged.
        row_by_key: dict[tuple[str, str], dict] = {}
        for f in rows:
            row_by_key.setdefault((f["cve"], f["module"]), f)
        report_keys = set(row_by_key)

        # Catch-all "no_component_matched" rows carry an empty module; keep their
        # reason keyed by CVE so an unresolved report row can report it verbatim.
        catchall_reason: dict[str, str] = {}
        resolved_keys: set[tuple[str, str]] = set()

        # Iterate vexscan findings as the source of truth: one record per
        # (finding = binary x advisory), which is exactly how the legacy
        # renderer emits per-binary rows. No fan-out against report rows.
        #
        # We pass vexscan the union of in-scope modules and CVEs, so it also
        # checks each CVE against modules the Trivy report never paired it with
        # (e.g. an x/net CVE against x/crypto), yielding spurious
        # "no_osv_package_mapping" undetermined rows. Trivy is the authority on
        # what is flagged, so results are scoped back to the (cve, module) pairs
        # the report actually contains -- which drops that cross-product noise
        # while keeping genuine findings vexscan resolved better than the legacy
        # binary hunt did.
        for vf in doc.get("findings", []):
            cve = vf.get("cve") or vf.get("id", "")
            module = vf.get("module") or vf.get("package", "")
            status = vf.get("status", "undetermined")
            if not module:
                if status == "undetermined" and cve:
                    catchall_reason[cve] = vf.get("reason", "no_component_matched")
                continue
            if (cve, module) not in report_keys:
                continue  # vexscan explored a module the report did not flag
            resolved_keys.add((cve, module))
            fallback = row_by_key.get((cve, module), {})
            rec = _to_record(image, fallback, vf)
            if status in STATUS_MAP:
                rec["justification"] = STATUS_MAP[status]
                rec["method"] = _method_for(status, rec["granularity"])
                candidates.append(rec)
            elif status == "linked":
                present.append(rec)
            else:
                rec["reason"] = vf.get("reason", status)
                undetermined.append(rec)

        # Any report row vexscan never produced a finding for stays visible as
        # undetermined, carrying vexscan's own reason when it offered one.
        for f in rows:
            if (f["cve"], f["module"]) not in resolved_keys:
                undetermined.append({**f, "reason": catchall_reason.get(f["cve"], "vexscan_no_finding")})

    return {
        "candidates": candidates,
        "present": present,
        "undetermined": undetermined,
        "image_status": image_status,
    }


def _method_for(status: str, granularity: str) -> str:
    if status == "not_present":
        return "pclntab-module" if granularity == "module" else "pclntab"
    return "govulncheck"


def _to_record(image: str, report_row: dict, vf: dict) -> dict:
    """Build a candidate/present record with the keys the renderers expect.

    ``report_row`` supplies only fallback values and may be empty when vexscan
    surfaced a finding the Trivy report did not enumerate.
    """
    pkgs = vf.get("packages") or [vf.get("module") or vf.get("package", "")]
    return {
        "image": image,
        "target": vf.get("location") or vf.get("binary") or report_row.get("target", ""),
        "module": vf.get("module") or vf.get("package") or report_row.get("module", ""),
        # Prefer the version vexscan read from build info; fall back to Trivy's.
        "installed": vf.get("version") or report_row.get("installed", ""),
        "fixed": vf.get("fixed_version") or report_row.get("fixed"),
        "cve": vf.get("cve") or vf.get("id") or report_row.get("cve", ""),
        "pkgs": sorted(pkgs),
        "granularity": vf.get("granularity", "package"),
        "stripped": vf.get("stripped", False),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report", help="Path to a scan-*.md report (default: latest in reports/).")
    ap.add_argument("--reports-dir", default="reports", help="Directory holding scan-*.md reports.")
    ap.add_argument("--modules", default=",".join(DEFAULT_MODULES),
                    help="Comma-separated Go modules to evaluate.")
    ap.add_argument("--vexscan-bin", default=os.getenv("VEXSCAN_BIN", "vexscan"),
                    help="Path to the vexscan binary.")
    ap.add_argument("--out-json", default="vex-candidates.json")
    ap.add_argument("--out-vex", default="vex-candidates.text-vex")
    ap.add_argument("--out-issue", default="vex-candidates-issue.md")
    ap.add_argument("--github-output", help="Append key=value outputs here (GITHUB_OUTPUT).")
    args = ap.parse_args()

    vexscan_bin = shutil.which(args.vexscan_bin) or args.vexscan_bin
    if not shutil.which(vexscan_bin) and not Path(vexscan_bin).exists():
        print(f"vexscan binary not found: {args.vexscan_bin}", file=sys.stderr)
        return 1

    report = args.report
    if not report:
        latest = legacy.find_latest_report(Path(args.reports_dir))
        if not latest:
            print("No scan-*.md report found.", file=sys.stderr)
            return 1
        report = str(latest)
    report_name = Path(report).stem
    modules = [m.strip() for m in args.modules.split(",") if m.strip()]

    print(f"Report: {report}", file=sys.stderr)
    print(f"vexscan: {vexscan_bin}", file=sys.stderr)
    images, findings = legacy.parse_report(report)
    print(f"Parsed {len(images)} images, {len(findings)} gobinary CVE rows.", file=sys.stderr)

    result = analyze(images, findings, modules, vexscan_bin)
    result["report"] = report_name
    result["modules"] = modules

    Path(args.out_json).write_text(json.dumps(result, indent=2, default=list))
    Path(args.out_vex).write_text(legacy.render_textvex(result["candidates"]) + "\n")
    Path(args.out_issue).write_text(legacy.render_issue(report_name, result, modules))

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
