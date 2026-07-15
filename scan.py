#!/usr/bin/env python3
"""Generate a Trivy CVE scan report for RKE2 images.

This is a Python port of the original ``scan.sh``. It keeps the exact same CLI
and produces the same artifacts:

* ``trivy_scan_report.txt`` -- a markdown report whose structure is consumed by
  ``.github/scripts/scan_to_html.py``.
* ``images.txt`` / ``images-optional.txt`` -- the default and optional add-on
  image lists that were scanned.
* ``reports/scan_metrics.db`` -- an SQLite database of per-run and per-CVE
  metrics (with best-effort EPSS enrichment).

The script resolves the set of images to scan from one of three sources -- a
published release tarball, a pull request head, or a branch tip -- runs the
upstream ``scripts/build-images`` in a sandbox to reproduce the image lists,
then scans every image with Trivy under Rancher's OpenVEX suppression.

Usage:
    scan.py [branch] [--pr <pr-number|pr-url>] [--release <version>]
            [--gist <title>] [--prime] [--no-prime]
"""

import argparse
import glob as globmod
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

OUTPUT_FILE = "trivy_scan_report.txt"
DB_FILE = os.environ.get("SCAN_STATS_DB_PATH", "reports/scan_metrics.db")

# Registry used to reproduce PRIME builds. build-images emits the PRIME/hardened
# image variants (ingress-nginx prime tags, hardened vsphere images, etc.) only
# when REGISTRY != docker.io, and the final scan targets registry.rancher.com.
PRIME_REGISTRY = "registry.rancher.com"

UPSTREAM_REPO = "rancher/rke2"
VEX_URL = "https://github.com/rancher/vexhub/raw/refs/heads/main/reports/rancher.openvex.json"
VEX_FILE = "rancher.openvex.json"

# Optional (non-default) image groups. These add-on images are NOT shipped in
# the default RKE2 airgap tarball (images-core + images-canal), but we still want
# to scan them; they are reported in a separate, clearly delineated section.
OPTIONAL_GROUPS = ["cilium", "calico", "vsphere", "multus", "harvester"]

HIGH_CRIT = {"HIGH", "CRITICAL"}


def log(msg=""):
    print(msg, flush=True)


def warn(msg):
    print(msg, file=sys.stderr, flush=True)


def die(msg, code=1):
    warn(msg)
    sys.exit(code)


def run(cmd, **kwargs):
    """Thin wrapper around subprocess.run with text mode defaulted on."""
    kwargs.setdefault("text", True)
    return subprocess.run(cmd, **kwargs)


def capture(cmd, **kwargs):
    """Run a command and return its stdout (empty string on failure)."""
    res = run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, **kwargs)
    if res.returncode != 0:
        return ""
    return res.stdout


# --------------------------------------------------------------------------- #
# CLI / source resolution
# --------------------------------------------------------------------------- #

def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="scan.py",
        add_help=True,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=(
            "Scan RKE2 images with Trivy and produce a markdown report + metrics DB.\n\n"
            "Examples:\n"
            "  scan.py\n"
            "  scan.py release-1.32\n"
            "  scan.py --pr 9994\n"
            "  scan.py --pr https://github.com/rancher/rke2/pull/9994\n"
            "  scan.py --release v1.36.1-rc1-rke2r1\n"
            "  scan.py --release v1.36.1+rke2r1\n"
            "  scan.py --prime\n"
            "  scan.py --gist 'My Scan Results'\n\n"
            "Note: --pr scans default to --prime; pass --no-prime to disable."
        ),
    )
    parser.add_argument("branch", nargs="?", default="master",
                        help="Branch to scan (default: master).")
    parser.add_argument("-p", "--pr", dest="pr", metavar="PR",
                        help="PR number or Rancher rke2 PR URL to scan.")
    parser.add_argument("-r", "--release", dest="release", metavar="VERSION",
                        help="Published RKE2 release version to scan.")
    parser.add_argument("-g", "--gist", dest="gist", metavar="TITLE",
                        help="Upload the report to a public gist with this title.")
    parser.add_argument("--prime", dest="prime", action="store_true", default=None,
                        help="Scan the PRIME (registry.rancher.com) image variants.")
    parser.add_argument("--no-prime", dest="prime", action="store_false",
                        help="Do not use the PRIME image variants.")

    args = parser.parse_args(argv)

    if args.release and args.pr:
        parser.error("--release and --pr cannot be used together")

    # PR scans default to the prime ingress registry unless the caller explicitly
    # opted in/out via --prime/--no-prime.
    prime_explicit = args.prime is not None
    use_prime = bool(args.prime)
    if args.pr and not prime_explicit:
        use_prime = True
    args.use_prime = use_prime
    return args


class Source:
    """Resolved description of what to scan."""

    def __init__(self):
        self.mode = "branch"          # branch | pr | release
        self.branch = "master"
        self.ref_path = ""            # refs/heads/... or refs/pull/N/head
        self.release_tag = ""
        self.release_tag_url = ""
        self.pr_number = ""
        self.pr_head_sha = ""
        self.pr_head_ref = ""
        self.source_desc = ""
        self.source_ref = ""          # canonical reference recorded with the scan


def resolve_source(args):
    src = Source()
    src.branch = args.branch

    if args.release:
        src.mode = "release"
        # Normalize "-rke2rN" suffix to "+rke2rN" so the tag matches GitHub's
        # release naming, then URL-encode the '+' as '%2B'.
        tag = args.release
        m = re.match(r"^(.*)-rke2r([0-9]+)$", tag)
        if m:
            tag = f"{m.group(1)}+rke2r{m.group(2)}"
        src.release_tag = tag
        src.release_tag_url = tag.replace("+", "%2B")
        src.source_desc = f"release {tag}"
    elif args.pr:
        src.mode = "pr"
        pr = args.pr
        if re.fullmatch(r"[0-9]+", pr):
            src.pr_number = pr
        else:
            m = re.search(r"github\.com/rancher/rke2/pull/([0-9]+)", pr)
            if not m:
                die("Error: --pr value must be a PR number or Rancher rke2 PR URL")
            src.pr_number = m.group(1)

        src.ref_path = f"refs/pull/{src.pr_number}/head"
        src.source_desc = f"PR #{src.pr_number}"

        # Fetch PR head SHA and head branch for artifact lookup.
        info = capture(["gh", "pr", "view", src.pr_number, "-R", UPSTREAM_REPO,
                        "--json", "headRefOid,headRefName,headRepositoryOwner"])
        if info:
            try:
                data = json.loads(info)
                src.pr_head_sha = data.get("headRefOid", "") or ""
                src.pr_head_ref = data.get("headRefName", "") or ""
                log(f"PR head SHA: {src.pr_head_sha}")
                log(f"PR head ref: {src.pr_head_ref}")
            except json.JSONDecodeError:
                warn("Error parsing PR info JSON")
        else:
            warn("Error fetching PR info")
    else:
        src.mode = "branch"
        src.ref_path = f"refs/heads/{src.branch}"
        src.source_desc = f"branch '{src.branch}'"

    src.source_ref = src.ref_path if src.ref_path else f"release:{src.release_tag}"
    return src


# --------------------------------------------------------------------------- #
# Image list preparation
# --------------------------------------------------------------------------- #

def read_image_list(path):
    """Return non-empty, non-comment, stripped lines from an image list file."""
    if not os.path.exists(path):
        return []
    images = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            images.append(s)
    return images


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line + "\n")


def dedupe(lines):
    """De-duplicate while preserving first-seen order, dropping blanks."""
    seen = set()
    out = []
    for line in lines:
        if not line or line in seen:
            continue
        seen.add(line)
        out.append(line)
    return out


def download_release_images(src):
    url = (f"https://github.com/{UPSTREAM_REPO}/releases/download/"
           f"{src.release_tag_url}/rke2-images.linux-amd64.txt")
    log(f"Downloading release images list from: {url}")
    res = run(["curl", "-fsSL", url, "-o", "images.txt"])
    if res.returncode != 0:
        die(f"Error: Failed to download release images list from {url}\n"
            f"       Verify that the release tag '{src.release_tag}' exists at "
            f"https://github.com/{UPSTREAM_REPO}/releases")
    if not os.path.getsize("images.txt"):
        die("Error: Downloaded release images list is empty")
    count = len(read_image_list("images.txt"))
    log(f"Downloaded {count} images from release {src.release_tag}")


def download_build_scripts(work_dir, repo, ref):
    """Fetch version.sh + build-images for repo@ref into work_dir/scripts."""
    base = f"https://raw.githubusercontent.com/{repo}/{ref}/scripts"
    ok = True
    for name in ("version.sh", "build-images"):
        res = run(["curl", "-fsSL", f"{base}/{name}",
                   "-o", os.path.join(work_dir, "scripts", name)],
                  stderr=subprocess.DEVNULL)
        ok = ok and res.returncode == 0
    return ok


def write_git_shim(work_dir):
    """Write a fake ``git`` that satisfies build-images without a real checkout."""
    shim = os.path.join(work_dir, "bin", "git")
    with open(shim, "w", encoding="utf-8") as fh:
        fh.write(
            "#!/bin/sh\n"
            "case \"$1\" in\n"
            "    rev-parse)\n"
            "        echo deadbeefdeadbeefdeadbeefdeadbeefdeadbeef\n"
            "        ;;\n"
            "    diff|status|tag)\n"
            "        exit 0\n"
            "        ;;\n"
            "    log)\n"
            "        echo deadbeefdeadbeefdeadbeefdeadbeefdeadbeef someone@example.com\n"
            "        ;;\n"
            "    *)\n"
            "        exit 0\n"
            "        ;;\n"
            "esac\n"
        )
    os.chmod(shim, 0o755)


def run_build_images(work_dir, out_dir, registry_override, log_path):
    """Run scripts/build-images with scan-specific stubs.

    Uses ``echo`` in place of a real pull, a stubbed git, and skips the runtime
    build. ``registry_override``, when set, sets REGISTRY so the PRIME/hardened
    image variants are emitted. Returns True on success.
    """
    env = dict(os.environ)
    env["PATH"] = os.path.join(work_dir, "bin") + os.pathsep + env.get("PATH", "")
    env["GOARCH"] = env.get("GOARCH") or capture(["go", "env", "GOARCH"]).strip()
    env["GOOS"] = env.get("GOOS") or capture(["go", "env", "GOOS"]).strip()
    env["BUILD_DIR"] = out_dir
    env["SKIP_BUILD_IMAGE_RUNTIME"] = "1"
    env["PULL_CMD"] = "echo"
    env["PULL_CMD_CORE"] = "echo"
    if registry_override:
        env["REGISTRY"] = registry_override

    with open(log_path, "w", encoding="utf-8") as errlog:
        res = run(["bash", os.path.join(work_dir, "scripts", "build-images")],
                  stdout=subprocess.DEVNULL, stderr=errlog, env=env)
    return res.returncode == 0


def extract_var(path, name):
    """Return the first ``NAME=value`` assignment value in a shell file."""
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(rf"^{re.escape(name)}=(.*)$", line)
            if m:
                return m.group(1).strip()
    return ""


def build_image_lists(src, use_prime, work_dir):
    """Reproduce the image lists by running build-images in a sandbox.

    Writes images.txt (default install set) and images-optional.txt (add-ons).
    """
    for sub in ("scripts", "bin", "build"):
        os.makedirs(os.path.join(work_dir, sub), exist_ok=True)

    repo, ref = UPSTREAM_REPO, src.ref_path

    if not download_build_scripts(work_dir, repo, ref):
        if src.mode == "pr":
            log(f"Unable to fetch scripts via {repo}/{ref}; "
                "resolving PR head via GitHub API...")
            pr_json = capture(["gh", "api",
                               f"repos/{UPSTREAM_REPO}/pulls/{src.pr_number}"])
            head_repo = head_sha = ""
            if pr_json:
                try:
                    head = json.loads(pr_json).get("head", {}) or {}
                    head_repo = (head.get("repo") or {}).get("full_name", "") or ""
                    head_sha = head.get("sha", "") or ""
                except json.JSONDecodeError:
                    pass
            if not head_repo or not head_sha:
                die(f"Error: could not resolve head repo/SHA for PR #{src.pr_number}")
            repo, ref = head_repo, head_sha
            src.source_desc = f"PR #{src.pr_number} ({repo}@{ref})"
            log(f"Retrying with {src.source_desc}")
            if not download_build_scripts(work_dir, repo, ref):
                die(f"Error: failed to fetch scripts for PR #{src.pr_number} "
                    f"from {repo}@{ref}")
        else:
            die(f"Error: failed to fetch scripts for {src.source_desc} ({src.ref_path})")

    build_images = os.path.join(work_dir, "scripts", "build-images")
    os.chmod(build_images, 0o755)

    hardened_tag = prime_tag = ""
    if use_prime:
        hardened_tag = extract_var(build_images, "INGRESS_NGINX_HARDENED_TAG")
        prime_tag = extract_var(build_images, "INGRESS_NGINX_PRIME_TAG")
        if not hardened_tag or not prime_tag:
            die("Error: failed to determine ingress-nginx hardened/prime tags "
                "from build-images")

    write_git_shim(work_dir)

    build_dir = os.path.join(work_dir, "build")
    if not run_build_images(work_dir, build_dir, "",
                            os.path.join(work_dir, "build-images.log")):
        with open(os.path.join(work_dir, "build-images.log"), encoding="utf-8") as fh:
            warn(fh.read())
        sys.exit(1)

    if use_prime:
        _apply_prime_variants(work_dir, build_dir, hardened_tag, prime_tag)

    _assemble_lists(build_dir)


def _apply_prime_variants(work_dir, build_dir, hardened_tag, prime_tag):
    """Rewrite ingress-nginx to the prime tag and swap in hardened vsphere images."""
    ingress_file = os.path.join(build_dir, "images-ingress-nginx.txt")
    if not os.path.isfile(ingress_file):
        die("Error: expected ingress-nginx image list was not generated")

    lines = read_image_list(ingress_file)
    lines = [re.sub(rf":{re.escape(hardened_tag)}$", f":{prime_tag}", ln)
             for ln in lines]
    write_lines(ingress_file, lines)

    # PR rancher/rke2#10696 introduced PRIME-only hardened vsphere images that
    # build-images emits only when REGISTRY != docker.io. The default run used
    # docker.io and produced the non-hardened vsphere list. Regenerate just the
    # vsphere list against the prime registry and swap it in. On branches
    # predating #10696 the lists are identical, so this is a no-op there.
    prime_build_dir = os.path.join(work_dir, "build-prime")
    os.makedirs(prime_build_dir, exist_ok=True)
    if not run_build_images(work_dir, prime_build_dir, PRIME_REGISTRY,
                            os.path.join(work_dir, "build-images-prime.log")):
        with open(os.path.join(work_dir, "build-images-prime.log"), encoding="utf-8") as fh:
            warn(fh.read())
        sys.exit(1)
    prime_vsphere = os.path.join(prime_build_dir, "images-vsphere.txt")
    if os.path.isfile(prime_vsphere):
        shutil.copyfile(prime_vsphere, os.path.join(build_dir, "images-vsphere.txt"))


def _assemble_lists(build_dir):
    """Split the generated images-*.txt files into default + optional lists."""
    optional_group_files = {
        os.path.join(build_dir, f"images-{grp}.txt") for grp in OPTIONAL_GROUPS
    }

    # Default list: every generated images-*.txt EXCEPT the optional group files.
    # The historical "mirrored-" passthrough exclusion keeps the default report
    # reflecting the default install set.
    default_lines = []
    for path in sorted(globmod.glob(os.path.join(build_dir, "images-*.txt"))):
        if path in optional_group_files:
            continue
        for line in read_image_list(path):
            if "mirrored" not in line:
                default_lines.append(line)
    default = dedupe(default_lines)
    write_lines("images.txt", default)

    # Optional list: the union of the optional group files, de-duplicated and
    # with anything already in the default list removed so nothing is scanned
    # twice.
    optional_lines = []
    for path in sorted(optional_group_files):
        optional_lines.extend(read_image_list(path))
    default_set = set(default)
    optional = [ln for ln in dedupe(optional_lines) if ln not in default_set]
    write_lines("images-optional.txt", optional)


def rewrite_registry_prime(path):
    """Rewrite image refs to registry.rancher.com for --prime scans.

    docker.io/ prefixes become registry.rancher.com/, and refs with no registry
    (no '.'/':' in the first path segment, i.e. implicit docker.io) are prefixed.
    """
    if not os.path.exists(path) or not os.path.getsize(path):
        return
    out = []
    for line in read_image_list(path):
        line = re.sub(r"^docker\.io/", "registry.rancher.com/", line)
        first = line.split("/", 1)[0]
        if "." not in first and ":" not in first:
            line = "registry.rancher.com/" + line
        out.append(line)
    write_lines(path, out)


# --------------------------------------------------------------------------- #
# Runtime image tarball (CI artifact)
# --------------------------------------------------------------------------- #

def fetch_runtime_tarball(src):
    """Locate and download the rke2-runtime image tarball from a CI artifact.

    The rke2-runtime image is only published during a real CI run; for an
    unreleased build (branch tip or PR head) it never exists in a registry, so a
    plain ``trivy image rancher/rke2-runtime:<dev-version>`` cannot pull it. We
    fetch the prebuilt tarball from the source's latest CI run and scan it
    directly. Release scans skip this (the runtime image is published alongside
    the release). Returns (tarball_path or None, artifact_dir or None).
    """
    lookup_sha = lookup_ref = lookup_desc = ""
    if src.pr_number:
        lookup_sha, lookup_ref, lookup_desc = src.pr_head_sha, src.pr_head_ref, f"PR #{src.pr_number}"
    elif src.mode != "release":
        lookup_ref, lookup_desc = src.branch, f"branch '{src.branch}'"

    if not lookup_sha and not lookup_ref:
        return None, None

    log(f"Fetching workflow runs for {lookup_desc}...")

    candidates = []
    if lookup_sha:
        out = capture(["gh", "run", "list", "-R", UPSTREAM_REPO, "-s", "completed",
                       "--limit", "100", "--json", "databaseId,headSha,name",
                       "--jq", f'.[] | select(.headSha=="{lookup_sha}") | .databaseId'])
        candidates += out.split()
    if lookup_ref:
        out = capture(["gh", "run", "list", "-R", UPSTREAM_REPO, "-s", "completed",
                       "-b", lookup_ref, "--limit", "50",
                       "--json", "databaseId", "--jq", ".[].databaseId"])
        candidates += out.split()
    if src.pr_number:
        out = capture(["gh", "api",
                       f"repos/{UPSTREAM_REPO}/actions/runs?event=pull_request&per_page=100",
                       "--jq",
                       f".workflow_runs[] | select(.pull_requests[]?.number == {src.pr_number}) | .id"])
        candidates += out.split()

    candidates = sorted(set(c for c in candidates if c))
    if not candidates:
        warn(f"Warning: No completed workflow runs found for {lookup_desc}")
        return None, None

    run_id = artifact_name = ""
    for cand in candidates:
        names = capture(["gh", "api",
                         f"repos/{UPSTREAM_REPO}/actions/runs/{cand}/artifacts",
                         "--paginate", "--jq", ".artifacts[].name"]).splitlines()
        match = next((n for n in names
                      if re.search(r"rke2-runtime|rke2-test-artifacts|rke2-images", n)), "")
        if match:
            run_id, artifact_name = cand, match
            log(f"Found workflow run ID {run_id} with artifact: {artifact_name}")
            break

    if not run_id:
        warn(f"Warning: None of the workflow runs for {lookup_desc} contain a matching rke2 artifact")
        return None, None

    artifact_dir = tempfile.mkdtemp()
    log(f"Downloading {artifact_name} from workflow run...")
    res = run(["gh", "run", "download", run_id, "-R", UPSTREAM_REPO,
               "-n", artifact_name, "-D", artifact_dir],
              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if res.returncode != 0:
        warn(f"Warning: Failed to download artifact from workflow run: {res.stdout}")
        shutil.rmtree(artifact_dir, ignore_errors=True)
        return None, None

    # Prefer the rke2-runtime tarball; fall back to the linux-amd64 images archive.
    archive = _find_first(artifact_dir, (r"rke2-runtime.*\.tar\.zst$", r"rke2-runtime.*\.tar$"))
    if not archive:
        archive = _find_first(artifact_dir, (r"rke2-images\.linux-amd64\.tar\.zst$",))
    if not archive:
        warn("Warning: No suitable runtime/image archive found in artifact")
        shutil.rmtree(artifact_dir, ignore_errors=True)
        return None, None

    log(f"Found archive: {archive}")
    if archive.endswith(".zst"):
        tarball = archive[:-len(".zst")]
        log("Decompressing archive...")
        if run(["zstd", "-d", archive, "-o", tarball],
               stderr=subprocess.DEVNULL).returncode != 0:
            warn("Warning: Failed to decompress archive")
            shutil.rmtree(artifact_dir, ignore_errors=True)
            return None, None
    else:
        tarball = archive

    log(f"Will scan runtime tarball: {tarball}")

    # The runtime image reference generated by build-images is never pushed to a
    # registry for an unreleased build, so drop it from the lists; the tarball
    # scan covers it (otherwise it is reported as an empty "scanned" image).
    for img_list in ("images.txt", "images-optional.txt"):
        if os.path.exists(img_list):
            kept = [ln for ln in read_image_list(img_list) if "/rke2-runtime:" not in ln]
            write_lines(img_list, kept)

    return tarball, artifact_dir


def _find_first(root, patterns):
    """Return the first file under root whose name matches any regex pattern."""
    for pattern in patterns:
        rx = re.compile(pattern)
        for dirpath, _, files in os.walk(root):
            for name in sorted(files):
                if rx.search(name):
                    return os.path.join(dirpath, name)
    return None


# --------------------------------------------------------------------------- #
# VEX
# --------------------------------------------------------------------------- #

def download_vex():
    """Download the Rancher OpenVEX report, aborting if it cannot be retrieved.

    This file is large (~85MB) and the GitHub raw endpoint frequently flakes with
    HTTP/2 stream errors mid-transfer, so force HTTP/1.1 and retry aggressively.
    VEX suppression is essential: without it, previously-vexed CVEs reappear and
    massively inflate the report, so a failure aborts rather than publishing
    misleading counts.
    """
    for attempt in range(1, 6):
        res = run(["curl", "-fSL", "--http1.1",
                   "--retry", "5", "--retry-all-errors", "--retry-delay", "5",
                   "--connect-timeout", "30", "--max-time", "600",
                   VEX_URL, "-o", VEX_FILE])
        if (res.returncode == 0 and os.path.exists(VEX_FILE)
                and os.path.getsize(VEX_FILE) > 0):
            with open(VEX_FILE, encoding="utf-8", errors="replace") as fh:
                if fh.read(1) == "{":
                    return True
        warn(f"Warning: attempt {attempt}/5 to download Rancher OpenVEX report failed; retrying...")
        if os.path.exists(VEX_FILE):
            os.remove(VEX_FILE)
        if attempt < 5:
            time.sleep(10)

    if os.path.exists(VEX_FILE):
        os.remove(VEX_FILE)
    die("Error: Failed to download a valid Rancher OpenVEX report after 5 attempts.\n"
        "Aborting: scanning without VEX suppression would produce misleading CVE counts.")


# --------------------------------------------------------------------------- #
# Trivy scanning + parsing
# --------------------------------------------------------------------------- #

def trivy_scan(ref, vex_flag, is_tarball=False):
    """Scan an image (or tarball) and return (table_text, parsed_json_or_None)."""
    json_tmp = tempfile.mktemp()
    try:
        cmd = ["trivy", "image"]
        if is_tarball:
            cmd += ["--input", ref]
        else:
            cmd += [ref]
        cmd += vex_flag + ["--severity", "CRITICAL,HIGH", "--format", "json"]
        with open(json_tmp, "w", encoding="utf-8") as out:
            run(cmd, stdout=out, stderr=subprocess.DEVNULL)

        table = capture(["trivy", "convert", "--format", "table", json_tmp])

        data = None
        try:
            with open(json_tmp, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError):
            data = None
        return table, data
    finally:
        if os.path.exists(json_tmp):
            os.remove(json_tmp)


def iter_vulns(data):
    """Yield every vulnerability dict across all Results in a Trivy JSON doc."""
    if not data:
        return
    for result in data.get("Results", []) or []:
        for vuln in result.get("Vulnerabilities") or []:
            yield result, vuln


def count_severities(data):
    """Return (critical, high) counts of HIGH/CRITICAL vulnerabilities.

    Counting the JSON vulnerabilities directly matches the summed totals of
    Trivy's per-target "Total: N (HIGH: x, CRITICAL: y)" table lines.
    """
    crit = high = 0
    for _, vuln in iter_vulns(data):
        sev = vuln.get("Severity")
        if sev == "CRITICAL":
            crit += 1
        elif sev == "HIGH":
            high += 1
    return crit, high


def classify_sources(data):
    """Return (go_stdlib, go_module, base_image) HIGH/CRITICAL CVE counts."""
    go_stdlib = go_module = base_image = 0
    for result, vuln in iter_vulns(data):
        if vuln.get("Severity") not in HIGH_CRIT:
            continue
        result_class = (result.get("Class") or "").lower()
        result_type = (result.get("Type") or "").lower()
        pkg = (vuln.get("PkgName") or "").lower()
        if result_class == "os-pkgs":
            base_image += 1
        elif pkg in {"stdlib", "go"}:
            go_stdlib += 1
        elif result_type in {"gomod", "gobinary"}:
            go_module += 1
    return go_stdlib, go_module, base_image


def collect_cve_rows(data, image, scope):
    """Return one row per unique HIGH/CRITICAL CVE for the given image.

    Rows: (scope, image, cve_id, severity, package, installed, fixed). Duplicate
    findings (same CVE/package/version) are collapsed to match the scan_cves
    unique-identity index.
    """
    def clean(value):
        return str(value or "").replace("\t", " ").replace("\n", " ").replace("\r", " ")

    rows = []
    seen = set()
    for _, vuln in iter_vulns(data):
        sev = vuln.get("Severity")
        if sev not in HIGH_CRIT:
            continue
        cve_id = clean(vuln.get("VulnerabilityID"))
        if not cve_id:
            continue
        pkg = clean(vuln.get("PkgName"))
        installed = clean(vuln.get("InstalledVersion"))
        key = (cve_id, pkg, installed)
        if key in seen:
            continue
        seen.add(key)
        rows.append((clean(scope), clean(image), cve_id, clean(sev),
                     pkg, installed, clean(vuln.get("FixedVersion"))))
    return rows


# --------------------------------------------------------------------------- #
# Report building
# --------------------------------------------------------------------------- #

class Report:
    """Accumulates markdown lines and per-scan metrics."""

    def __init__(self):
        self.lines = []

        # Default-images summary (report Summary section). These totals INCLUDE
        # the runtime tarball scan, matching scan.sh.
        self.total_critical = 0
        self.total_high = 0
        self.images_with_cves = []   # "name|crit|high"
        self.images_clean = []

        # Optional add-on summary.
        self.opt_total_critical = 0
        self.opt_total_high = 0
        self.opt_images_with_cves = []
        self.opt_images_clean = []

        # Bundle metrics persisted to sqlite (default images loop ONLY).
        self.bundle_total_critical = 0
        self.bundle_total_high = 0
        self.bundle_images_with_cves = 0
        self.bundle_go_stdlib = 0
        self.bundle_go_module = 0
        self.bundle_base_image = 0

        # Per-CVE rows for scan_cves.
        self.cve_rows = []

    def emit(self, line=""):
        self.lines.append(line)

    def emit_table(self, table_text):
        if not table_text:
            return
        body = table_text[:-1] if table_text.endswith("\n") else table_text
        for line in body.split("\n"):
            self.emit(line)

    def tally(self, name, crit, high, optional=False):
        if optional:
            self.opt_total_critical += crit
            self.opt_total_high += high
            if crit + high > 0:
                self.opt_images_with_cves.append(f"{name}|{crit}|{high}")
            else:
                self.opt_images_clean.append(name)
        else:
            self.total_critical += crit
            self.total_high += high
            if crit + high > 0:
                self.images_with_cves.append(f"{name}|{crit}|{high}")
            else:
                self.images_clean.append(name)

    def write(self, path):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("".join(line + "\n" for line in self.lines))


def scan_one(report, display_name, ref, vex_flag, target_lines, scope,
             is_tarball=False, count_bundle=False):
    """Scan a single image/tarball, append its report block, update metrics.

    target_lines is the list the report block is appended to (main report or the
    buffered optional block). count_bundle=True feeds the sqlite bundle metrics.
    """
    table, data = trivy_scan(ref, vex_flag, is_tarball=is_tarball)
    crit, high = count_severities(data)

    heading = display_name if is_tarball else f"`{display_name}`"
    target_lines.append(f"## Scan Results: {heading}")
    target_lines.append("")
    target_lines.append("```text")
    if table:
        body = table[:-1] if table.endswith("\n") else table
        target_lines.extend(body.split("\n"))
    target_lines.append("```")
    target_lines.append("")

    report.tally(display_name, crit, high, optional=(scope == "optional"))
    report.cve_rows.extend(collect_cve_rows(data, display_name, scope))

    if count_bundle:
        go_stdlib, go_module, base_image = classify_sources(data)
        report.bundle_go_stdlib += go_stdlib
        report.bundle_go_module += go_module
        report.bundle_base_image += base_image
        report.bundle_total_critical += crit
        report.bundle_total_high += high
        if crit + high > 0:
            report.bundle_images_with_cves += 1


def build_report(report, src, images, optional_images, runtime_tarball,
                 runtime_artifact_dir, vex_flag):
    # Header + list of images being scanned.
    report.emit("# Trivy Scan Report")
    report.emit("")
    report.emit(f"<!-- scan-source-ref: {src.source_ref} -->")
    report.emit(f"<!-- scan-source-desc: {src.source_desc} -->")
    report.emit("## Images Scanned")
    report.emit("")
    for image in images:
        report.emit(f"- `{image}`")
    if runtime_tarball:
        report.emit("")
        report.emit("## Runtime Image Tarball")
        report.emit("")
        report.emit(f"- `{runtime_tarball}`")
    report.emit("")

    # Default images.
    for image in images:
        log(f"Scanning image: {image}")
        scan_one(report, image, image, vex_flag, report.lines, "default",
                 count_bundle=True)

    # Runtime tarball (counted into the global totals but NOT the bundle metrics,
    # matching scan.sh).
    if runtime_tarball:
        log(f"Scanning runtime tarball: {runtime_tarball}")
        label = f"Runtime Image Tarball: {os.path.basename(runtime_tarball)}"
        scan_one(report, label, runtime_tarball, vex_flag, report.lines, "default",
                 is_tarball=True)
        if runtime_artifact_dir:
            shutil.rmtree(runtime_artifact_dir, ignore_errors=True)

    # Optional add-on images, buffered so they can be wrapped in the toggle
    # markers the HTML converter understands.
    optional_block = []
    optional_count = 0
    for image in optional_images:
        log(f"Scanning optional add-on image: {image}")
        optional_count += 1
        scan_one(report, image, image, vex_flag, optional_block, "optional")

    if optional_count > 0:
        _emit_optional_section(report, optional_images, optional_block)

    _emit_summary(report)


def _emit_optional_section(report, optional_images, optional_block):
    e = report.emit
    e("<!--OPTIONAL-START-->")
    e("")
    e("## Optional Add-on Images (Not in Default Tarball)")
    e("")
    e("> \u26a0\ufe0f The images in this section are **not** part of the default RKE2 "
      "airgap tarball (`images-core` + `images-canal`). They ship with optional "
      "add-ons \u2014 Cilium, Calico, vSphere, Multus, and Harvester. Use the toggle "
      "above to show or hide them.")
    e("")
    e("### Optional CVEs by Severity")
    e("")
    e("| Severity | Count |")
    e("| --- | ---: |")
    e(f"| CRITICAL | {report.opt_total_critical} |")
    e(f"| HIGH | {report.opt_total_high} |")
    e(f"| **Total** | **{report.opt_total_critical + report.opt_total_high}** |")
    e("")
    e(f"### Optional Images with CVEs ({len(report.opt_images_with_cves)})")
    e("")
    _emit_cve_table(report, report.opt_images_with_cves)
    e("")
    e("### Images Scanned (Optional)")
    e("")
    for image in optional_images:
        e(f"- `{image}`")
    e("")
    report.lines.extend(optional_block)
    e("<!--OPTIONAL-END-->")
    e("")


def _emit_summary(report):
    e = report.emit
    e("## Summary")
    e("")
    e("### CVEs by Severity")
    e("")
    e("| Severity | Count |")
    e("| --- | ---: |")
    e(f"| CRITICAL | {report.total_critical} |")
    e(f"| HIGH | {report.total_high} |")
    e(f"| **Total** | **{report.total_critical + report.total_high}** |")
    e("")
    e(f"### Images with CVEs ({len(report.images_with_cves)})")
    e("")
    _emit_cve_table(report, report.images_with_cves)
    e("")
    e(f"### CVE-free Images ({len(report.images_clean)})")
    e("")
    if not report.images_clean:
        e("_None_")
    else:
        for name in report.images_clean:
            e(f"- `{name}`")
    e("")


def _emit_cve_table(report, entries):
    e = report.emit
    if not entries:
        e("_None_")
        return
    e("| Image | CRITICAL | HIGH |")
    e("| --- | ---: | ---: |")
    for entry in entries:
        name, crit, high = entry.split("|", 2)
        e(f"| `{name}` | {crit} | {high} |")


# --------------------------------------------------------------------------- #
# Metrics database
# --------------------------------------------------------------------------- #

_SCHEMA = """
CREATE TABLE IF NOT EXISTS scan_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scanned_at TEXT NOT NULL,
    source_desc TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    total_images INTEGER NOT NULL,
    images_with_cves INTEGER NOT NULL,
    critical_cves INTEGER NOT NULL,
    high_cves INTEGER NOT NULL,
    go_stdlib_cves INTEGER NOT NULL,
    go_module_cves INTEGER NOT NULL,
    base_image_cves INTEGER NOT NULL,
    channel TEXT NOT NULL DEFAULT 'prime',
    optional_total_images INTEGER NOT NULL DEFAULT 0,
    optional_images_with_cves INTEGER NOT NULL DEFAULT 0,
    optional_critical_cves INTEGER NOT NULL DEFAULT 0,
    optional_high_cves INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE INDEX IF NOT EXISTS idx_scan_metrics_scanned_at ON scan_metrics(scanned_at);
CREATE INDEX IF NOT EXISTS idx_scan_metrics_source_ref_scanned_at
    ON scan_metrics(source_ref, scanned_at);

CREATE TABLE IF NOT EXISTS scan_cves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER NOT NULL REFERENCES scan_metrics(id),
    scanned_at TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    scope TEXT NOT NULL DEFAULT 'default',
    image TEXT NOT NULL,
    cve_id TEXT NOT NULL,
    severity TEXT NOT NULL,
    package TEXT NOT NULL DEFAULT '',
    installed_version TEXT NOT NULL DEFAULT '',
    fixed_version TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE INDEX IF NOT EXISTS idx_scan_cves_scan_id ON scan_cves(scan_id);
CREATE INDEX IF NOT EXISTS idx_scan_cves_cve_id ON scan_cves(cve_id);
CREATE INDEX IF NOT EXISTS idx_scan_cves_source_ref_scanned_at
    ON scan_cves(source_ref, scanned_at);
CREATE UNIQUE INDEX IF NOT EXISTS uq_scan_cves_identity
    ON scan_cves(scan_id, image, cve_id, package, installed_version);
"""

_RUN_SIGNATURE_INDEX = """
DROP INDEX IF EXISTS uq_scan_metrics_run_signature;
CREATE UNIQUE INDEX IF NOT EXISTS uq_scan_metrics_run_signature
    ON scan_metrics(
        scanned_at, source_ref, channel, total_images, images_with_cves,
        critical_cves, high_cves, go_stdlib_cves, go_module_cves, base_image_cves
    );
"""


def init_metrics_db(conn):
    """Create the schema and apply idempotent migrations for older databases."""
    conn.executescript(_SCHEMA)

    metrics_cols = {r[1] for r in conn.execute("PRAGMA table_info(scan_metrics)")}
    for col in ("optional_total_images", "optional_images_with_cves",
                "optional_critical_cves", "optional_high_cves"):
        if col not in metrics_cols:
            conn.execute(f"ALTER TABLE scan_metrics ADD COLUMN {col} INTEGER NOT NULL DEFAULT 0")

    cve_cols = {r[1] for r in conn.execute("PRAGMA table_info(scan_cves)")}
    for col in ("epss_score", "epss_percentile"):
        if col not in cve_cols:
            conn.execute(f"ALTER TABLE scan_cves ADD COLUMN {col} REAL")

    if "channel" not in metrics_cols:
        conn.execute("ALTER TABLE scan_metrics ADD COLUMN channel TEXT NOT NULL DEFAULT 'prime'")
        conn.execute("UPDATE scan_metrics SET channel='community' WHERE source_ref LIKE 'release:%'")

    conn.executescript(_RUN_SIGNATURE_INDEX)
    conn.commit()


def persist_metrics(report, src, use_prime, total_images):
    """Write the run's aggregate + per-CVE rows, then run EPSS enrichment."""
    db_dir = os.path.dirname(DB_FILE)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    scanned_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    channel = "prime" if use_prime else "community"

    conn = sqlite3.connect(DB_FILE)
    try:
        init_metrics_db(conn)

        cur = conn.execute(
            """
            INSERT OR IGNORE INTO scan_metrics (
                scanned_at, source_desc, source_ref, channel,
                total_images, images_with_cves, critical_cves, high_cves,
                go_stdlib_cves, go_module_cves, base_image_cves,
                optional_total_images, optional_images_with_cves,
                optional_critical_cves, optional_high_cves
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (scanned_at, src.source_desc, src.source_ref, channel,
             total_images, report.bundle_images_with_cves,
             report.total_critical, report.total_high,
             report.bundle_go_stdlib, report.bundle_go_module, report.bundle_base_image,
             len(report.opt_images_with_cves) + len(report.opt_images_clean),
             len(report.opt_images_with_cves),
             report.opt_total_critical, report.opt_total_high),
        )
        conn.commit()

        if cur.rowcount > 0:
            log(f"Scan metrics written to {DB_FILE}")
        else:
            log("Scan metrics already recorded for this run signature; skipped duplicate insert")

        row = conn.execute(
            "SELECT id FROM scan_metrics WHERE scanned_at=? AND source_ref=? AND channel=? "
            "ORDER BY id DESC LIMIT 1",
            (scanned_at, src.source_ref, channel),
        ).fetchone()
        scan_id = row[0] if row else None

        if scan_id is not None and report.cve_rows:
            conn.executemany(
                """
                INSERT OR IGNORE INTO scan_cves (
                    scan_id, scanned_at, source_ref, scope, image, cve_id,
                    severity, package, installed_version, fixed_version
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [(scan_id, scanned_at, src.source_ref, scope, image, cve_id,
                  severity, package, installed, fixed)
                 for (scope, image, cve_id, severity, package, installed, fixed)
                 in report.cve_rows],
            )
            conn.commit()
            count = conn.execute(
                "SELECT count(*) FROM scan_cves WHERE scan_id=?", (scan_id,)
            ).fetchone()[0]
            log(f"Recorded {count} per-CVE rows for scan {scan_id} in {DB_FILE}")
    finally:
        conn.close()

    _run_epss_enrichment(scan_id)


def _run_epss_enrichment(scan_id):
    """Best-effort EPSS enrichment of the scan's CVEs."""
    if scan_id is None:
        return
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          ".github", "scripts", "epss_enrich.py")
    if not os.path.isfile(script):
        return
    log(f"Enriching scan {scan_id} CVEs with EPSS scores...")
    res = run([sys.executable, script, "--db", DB_FILE, "--scan-id", str(scan_id)])
    if res.returncode != 0:
        warn("Warning: EPSS enrichment step failed; continuing")


# --------------------------------------------------------------------------- #
# Gist upload
# --------------------------------------------------------------------------- #

def upload_gist(title, pr_number):
    log("Uploading results to GitHub Gist...")
    res = run(["gh", "gist", "create", "--public", "--desc", title,
               "--filename", OUTPUT_FILE, OUTPUT_FILE],
              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if res.returncode != 0:
        die(f"Error creating gist: {res.stdout}")

    gist_url = res.stdout.strip().splitlines()[-1] if res.stdout.strip() else ""
    log(f"Gist created: {gist_url}")

    if pr_number:
        log(f"Adding comment to PR #{pr_number} with gist link...")
        comment = run(["gh", "pr", "comment", pr_number, "-R", UPSTREAM_REPO,
                       "--body", f"Trivy scan results: {gist_url}"])
        if comment.returncode == 0:
            log(f"Comment added to PR #{pr_number}")
        else:
            warn(f"Warning: Failed to add comment to PR #{pr_number}")


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    src = resolve_source(args)

    for stale in (OUTPUT_FILE, "images.txt", "images-optional.txt"):
        if os.path.exists(stale):
            os.remove(stale)

    log(f"Scanning using {src.source_desc} "
        f"({src.ref_path or 'release tag ' + src.release_tag})")

    work_dir = tempfile.mkdtemp()
    try:
        if src.mode == "release":
            download_release_images(src)
        else:
            build_image_lists(src, args.use_prime, work_dir)

        # Ensure the optional list exists even in release mode (no per-group
        # breakdown is available for a published release tarball).
        if not os.path.exists("images-optional.txt"):
            write_lines("images-optional.txt", [])

        if args.use_prime:
            rewrite_registry_prime("images.txt")
            rewrite_registry_prime("images-optional.txt")

        if not shutil.which("trivy"):
            die("Error: trivy CLI not found in PATH. Install Trivy and re-run scan.py.")

        runtime_tarball, runtime_artifact_dir = fetch_runtime_tarball(src)

        download_vex()
        vex_flag = ["--vex", VEX_FILE]

        images = read_image_list("images.txt")
        optional_images = read_image_list("images-optional.txt")

        report = Report()
        build_report(report, src, images, optional_images,
                     runtime_tarball, runtime_artifact_dir, vex_flag)
        report.write(OUTPUT_FILE)
        log(f"Trivy scan completed. Reports are saved in {OUTPUT_FILE}.")

        persist_metrics(report, src, args.use_prime, len(images))

        if args.gist:
            upload_gist(args.gist, src.pr_number)
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)
        if os.path.exists(VEX_FILE):
            os.remove(VEX_FILE)

    return 0


if __name__ == "__main__":
    sys.exit(main())
