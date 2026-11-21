#!/usr/bin/env python3
"""One-off tool to backfill reports/scan_metrics.db from committed scan-*.md /
pr-*.md reports that never made it into the metrics database.

Background: scan_metrics.db grew past GitHub's 100MB push limit around
2026-11-13, which silently stranded every DB commit from then on (see
scan.sh's prune_metrics_db() for the permanent fix). The daily scan reports
kept being generated and committed as markdown throughout the outage, so the
aggregate CVE counts and per-CVE identities for that gap are reconstructable
from those files -- they were never lost, just never ingested.

This script re-derives what scan.sh would have written for each report and
inserts it with the same INSERT OR IGNORE semantics/unique indexes scan.sh
uses, so it is safe to re-run (a report whose signature is already present is
a no-op).

Usage:
    python3 .github/scripts/backfill_scan_metrics.py [--db PATH] [--dry-run] \\
        reports/scan-20261114-1.md reports/scan-release-1.34-54.md ...

Known limitation: go_stdlib_cves/go_module_cves/base_image_cves are written as
0 for backfilled rows. Deriving them requires the raw Trivy JSON (to tell a Go
stdlib CVE from an OS package CVE), which was never committed -- only the
rendered markdown was. Nothing in scan_to_html.py's rendering or the CVE
Trends chart reads those three columns, so this has no visible effect.
Likewise, community/DockerHub comparison scans are never committed as their
own report (scan-report.yml discards that scan's output deliberately), so
only 'prime' rows can be backfilled this way.
"""

import argparse
import os
import re
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_to_html import _extract_ascii_tables_from_text  # noqa: E402

SOURCE_REF_RE = re.compile(r"<!--\s*scan-source-ref:\s*(.+?)\s*-->")
SOURCE_DESC_RE = re.compile(r"<!--\s*scan-source-desc:\s*(.+?)\s*-->")
HEADING_RE = re.compile(r"^##\s+(.*?)\s*$", re.MULTILINE)
IMAGE_HEADING_RE = re.compile(r"^Scan Results:\s*`([^`]+)`$")
TARBALL_HEADING_RE = re.compile(r"^Scan Results:\s*(Runtime Image Tarball:.+)$")
SEVERITY_ROW_RE = re.compile(r"^\|\s*(CRITICAL|HIGH)\s*\|\s*(\d+)\s*\|", re.MULTILINE)


def _git_commit_timestamp(path):
    """Return the UTC 'scanned_at' timestamp (scan.sh's format) for the single
    commit that added *path*, used as a proxy for when the scan actually ran."""
    out = subprocess.run(
        ["git", "log", "--format=%aI", "--", path],
        capture_output=True, text=True, check=True,
    ).stdout.strip().splitlines()
    if not out:
        raise ValueError(f"no commit history found for {path}")
    if len(out) != 1:
        raise ValueError(
            f"expected exactly one commit for {path}, found {len(out)}; "
            "refusing to guess which timestamp to use"
        )
    # NOTE: do not pass --follow here. These report filenames collide in
    # shape across weeks (e.g. scan-YYYYMMDD-N.md), and git's rename
    # detection will happily "follow" into an unrelated older file with a
    # similar diff, producing a wildly wrong timestamp.
    dt = datetime.fromisoformat(out[0])
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _severity_totals(section_text):
    crit = high = 0
    for sev, count in SEVERITY_ROW_RE.findall(section_text):
        if sev == "CRITICAL":
            crit = int(count)
        else:
            high = int(count)
    return crit, high


def _heading_count(text, label):
    pattern = re.compile(r"^###\s+" + re.escape(label) + r"\s*\((\d+)\)\s*$", re.MULTILINE)
    m = pattern.search(text)
    return int(m.group(1)) if m else 0


def _bullet_list_count(text, heading):
    """Count '- `...`' bullet lines under a '### <heading>' section."""
    m = re.search(r"^###\s+" + re.escape(heading) + r"\s*$", text, re.MULTILINE)
    if not m:
        return 0
    rest = text[m.end():]
    stop = re.search(r"^##\s+", rest, re.MULTILINE)
    body = rest[: stop.start()] if stop else rest
    return len(re.findall(r"^-\s+`", body, re.MULTILINE))


def parse_report(md):
    """Parse a scan-*.md / pr-*.md report into the fields scan.sh records."""
    source_ref_m = SOURCE_REF_RE.search(md)
    source_desc_m = SOURCE_DESC_RE.search(md)
    if not source_ref_m:
        raise ValueError("missing <!-- scan-source-ref: ... --> marker")
    source_ref = source_ref_m.group(1)
    source_desc = source_desc_m.group(1) if source_desc_m else source_ref

    optional_m = re.search(r"^##\s+Optional Add-on Images.*$", md, re.MULTILINE)

    default_images_m = re.search(r"^##\s+Images Scanned\s*$", md, re.MULTILINE)
    default_images_text = ""
    if default_images_m:
        stop = re.search(r"^##\s+", md[default_images_m.end():], re.MULTILINE)
        default_images_text = (
            md[default_images_m.end():][: stop.start()] if stop else md[default_images_m.end():]
        )
    channel = "prime" if "registry.rancher.com/" in default_images_text else "community"

    summary_m = re.search(r"^##\s+Summary\s*$", md, re.MULTILINE)
    if not summary_m:
        raise ValueError("missing final '## Summary' section")
    summary_text = md[summary_m.end():]

    cves_m = re.search(r"^###\s+CVEs by Severity\s*$", summary_text, re.MULTILINE)
    if not cves_m:
        raise ValueError("missing '### CVEs by Severity' in Summary section")
    stop = re.search(r"^###\s+", summary_text[cves_m.end():], re.MULTILINE)
    cves_section = (
        summary_text[cves_m.end():][: stop.start()] if stop else summary_text[cves_m.end():]
    )
    critical_cves, high_cves = _severity_totals(cves_section)
    images_with_cves = _heading_count(summary_text, "Images with CVEs")

    optional_critical_cves = optional_high_cves = 0
    optional_images_with_cves = optional_total_images = 0
    if optional_m:
        optional_text = md[optional_m.start():summary_m.start()]
        opt_cves_m = re.search(r"^###\s+Optional CVEs by Severity\s*$", optional_text, re.MULTILINE)
        if opt_cves_m:
            stop = re.search(r"^###\s+", optional_text[opt_cves_m.end():], re.MULTILINE)
            opt_section = (
                optional_text[opt_cves_m.end():][: stop.start()]
                if stop else optional_text[opt_cves_m.end():]
            )
            optional_critical_cves, optional_high_cves = _severity_totals(opt_section)
        optional_images_with_cves = _heading_count(optional_text, "Optional Images with CVEs")
        optional_total_images = _bullet_list_count(optional_text, "Images Scanned (Optional)")

    total_images = len(md.splitlines())

    return {
        "source_ref": source_ref,
        "source_desc": source_desc,
        "channel": channel,
        "total_images": total_images,
        "images_with_cves": images_with_cves,
        "critical_cves": critical_cves,
        "high_cves": high_cves,
        "optional_total_images": optional_total_images,
        "optional_images_with_cves": optional_images_with_cves,
        "optional_critical_cves": optional_critical_cves,
        "optional_high_cves": optional_high_cves,
    }


def extract_cve_rows(md):
    """Yield (scope, image, cve_id, severity, package, installed, fixed) tuples
    for every HIGH/CRITICAL finding in the report's per-image ASCII tables."""
    optional_m = re.search(r"^##\s+Optional Add-on Images.*$", md, re.MULTILINE)
    summary_m = re.search(r"^##\s+Summary\s*$", md, re.MULTILINE)
    optional_start = optional_m.start() if optional_m else None
    summary_start = summary_m.start() if summary_m else len(md)

    headings = list(HEADING_RE.finditer(md))
    for idx, h in enumerate(headings):
        title = h.group(1).strip()
        img_m = IMAGE_HEADING_RE.match(title)
        tarball_m = None if img_m else TARBALL_HEADING_RE.match(title)
        if not img_m and not tarball_m:
            continue
        image = img_m.group(1) if img_m else tarball_m.group(1)

        block_start = h.end()
        block_end = headings[idx + 1].start() if idx + 1 < len(headings) else len(md)
        block_end = min(block_end, summary_start)
        if block_start >= block_end:
            continue
        block_text = md[block_start:block_end]

        scope = "optional" if optional_start is not None and h.start() > optional_start else "default"

        for headers, rows in _extract_ascii_tables_from_text(block_text):
            hmap = {hh.lower().replace(" ", ""): hh for hh in headers}
            lib_key = hmap.get("library")
            vuln_key = hmap.get("vulnerability")
            sev_key = hmap.get("severity")
            inst_key = hmap.get("installedversion")
            fix_key = hmap.get("fixedversion")
            for row in rows:
                cve_id = row.get(vuln_key, "").strip() if vuln_key else ""
                if not re.match(r"^CVE-\d{4}-\d+", cve_id, re.I):
                    continue
                yield (
                    scope,
                    image,
                    cve_id,
                    row.get(sev_key, "").strip() if sev_key else "",
                    row.get(lib_key, "").strip() if lib_key else "",
                    row.get(inst_key, "").strip() if inst_key else "",
                    row.get(fix_key, "").strip() if fix_key else "",
                )


def backfill(db_path, paths, dry_run=False):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    inserted_metrics = inserted_cves = skipped = 0

    for path in paths:
        with open(path, "r", encoding="utf-8") as fh:
            md = fh.read()

        try:
            fields = parse_report(md)
        except ValueError as exc:
            print(f"SKIP {path}: {exc}", file=sys.stderr)
            skipped += 1
            continue

        scanned_at = _git_commit_timestamp(path)

        cur = conn.cursor()
        cur.execute(
            """
            INSERT OR IGNORE INTO scan_metrics (
                scanned_at, source_desc, source_ref, channel,
                total_images, images_with_cves, critical_cves, high_cves,
                go_stdlib_cves, go_module_cves, base_image_cves,
                optional_total_images, optional_images_with_cves,
                optional_critical_cves, optional_high_cves
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, 0, 0, ?, ?, ?, ?)
            """,
            (
                scanned_at, fields["source_desc"], fields["source_ref"], fields["channel"],
                fields["total_images"], fields["images_with_cves"],
                fields["critical_cves"], fields["high_cves"],
                fields["optional_total_images"], fields["optional_images_with_cves"],
                fields["optional_critical_cves"], fields["optional_high_cves"],
            ),
        )
        is_new = cur.rowcount > 0
        if is_new:
            inserted_metrics += 1
        cur.execute(
            "SELECT id FROM scan_metrics WHERE scanned_at=? AND source_ref=? AND channel=?"
            " ORDER BY id DESC LIMIT 1",
            (scanned_at, fields["source_ref"], fields["channel"]),
        )
        scan_id = cur.fetchone()[0]

        row_count = 0
        for scope, image, cve_id, severity, package, installed, fixed in extract_cve_rows(md):
            cur.execute(
                """
                INSERT OR IGNORE INTO scan_cves (
                    scan_id, scanned_at, source_ref, scope, image, cve_id,
                    severity, package, installed_version, fixed_version
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (scan_id, scanned_at, fields["source_ref"], scope, image, cve_id,
                 severity, package, installed, fixed),
            )
            if cur.rowcount > 0:
                row_count += 1
        inserted_cves += row_count

        print(
            f"{'[dry-run] ' if dry_run else ''}{path}: scanned_at={scanned_at} "
            f"source_ref={fields['source_ref']} channel={fields['channel']} "
            f"critical={fields['critical_cves']} high={fields['high_cves']} "
            f"{'(new scan_metrics row, ' if is_new else '(already present, '}"
            f"{row_count} scan_cves rows)"
        )

    if dry_run:
        conn.rollback()
    else:
        conn.commit()
        conn.execute("VACUUM;")
    conn.close()

    print(
        f"\nDone. {inserted_metrics} scan_metrics row(s) and {inserted_cves} "
        f"scan_cves row(s) inserted; {skipped} report(s) skipped."
        + (" (dry run, nothing written)" if dry_run else "")
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--db", default="reports/scan_metrics.db", help="Path to scan_metrics.db")
    parser.add_argument("--dry-run", action="store_true", help="Parse and print without writing")
    parser.add_argument("reports", nargs="+", help="scan-*.md / pr-*.md report paths to backfill")
    args = parser.parse_args()

    backfill(args.db, args.reports, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
