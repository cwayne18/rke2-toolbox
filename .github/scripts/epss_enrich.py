#!/usr/bin/env python3
"""Enrich the scan metrics database with EPSS scores.

EPSS (Exploit Prediction Scoring System, https://www.first.org/epss/) estimates
the probability that a CVE will be exploited in the wild within the next 30 days.
Each CVE gets an ``epss_score`` (probability in ``[0, 1]``) and an
``epss_percentile`` (its ranking relative to all scored CVEs).

This script downloads FIRST's canonical daily score file and writes the values
onto the ``scan_cves`` rows in ``reports/scan_metrics.db``.

Design goals (mirrors rancher/image-scanning#1621):

* **Non-destructive.** The ``epss_score`` / ``epss_percentile`` columns are added
  with ``ALTER TABLE ADD COLUMN`` (nullable) and only ever ``UPDATE``-d. No rows
  or existing columns are ever dropped or rewritten.
* **Best-effort.** Any network or parse failure is logged and the script exits
  ``0`` without modifying the database, so a transient outage never blocks a scan
  or clears previously recorded scores.

Usage::

    python3 epss_enrich.py [--db PATH] [--scan-id N] [--only-missing]
                           [--max-lookback-days N]
"""

import argparse
import csv
import gzip
import io
import os
import sqlite3
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

# Canonical FIRST.org daily EPSS score file. A fresh gzipped CSV is published
# each day; the URL 301-redirects, so the opener must follow redirects.
_EPSS_URL_TEMPLATE = "https://epss.cyentia.com/epss_scores-{date}.csv.gz"
_USER_AGENT = "rke2-toolbox-epss-enrich/1.0"
_DEFAULT_MAX_LOOKBACK_DAYS = 7


def _log(msg):
    print(f"[epss] {msg}", file=sys.stderr)


def _default_db_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(
        os.path.join(script_dir, "..", "..", "reports", "scan_metrics.db")
    )


def _fetch_epss_csv(max_lookback_days):
    """Return the decoded text of the most recent available EPSS file.

    Walks back one day at a time (today first) to tolerate publishing gaps,
    returning ``None`` if nothing is retrievable within the window.
    """
    today = datetime.now(timezone.utc).date()
    for delta in range(max_lookback_days + 1):
        day = today - timedelta(days=delta)
        url = _EPSS_URL_TEMPLATE.format(date=day.isoformat())
        req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            _log(f"fetch {day.isoformat()} failed ({exc}); trying previous day")
            continue
        try:
            text = gzip.decompress(raw).decode("utf-8", "replace")
        except (OSError, EOFError) as exc:
            _log(f"decompress {day.isoformat()} failed ({exc}); trying previous day")
            continue
        _log(f"using EPSS scores published {day.isoformat()}")
        return text
    return None


def _parse_epss(text):
    """Parse EPSS CSV text into ``{CVE_ID: (score, percentile)}``.

    The file starts with a ``#model_version,score_date`` comment line followed by
    a ``cve,epss,percentile`` header, both of which are skipped.
    """
    scores = {}
    reader = csv.reader(io.StringIO(text))
    for row in reader:
        if not row or row[0].startswith("#"):
            continue
        if row[0].strip().lower() == "cve":
            continue
        if len(row) < 3:
            continue
        cve = row[0].strip().upper()
        if not cve.startswith("CVE-"):
            continue
        try:
            score = float(row[1])
            percentile = float(row[2])
        except ValueError:
            continue
        scores[cve] = (score, percentile)
    return scores


def _ensure_columns(conn):
    """Add the nullable EPSS columns to scan_cves if they are missing."""
    existing = {r[1] for r in conn.execute("PRAGMA table_info(scan_cves)").fetchall()}
    for col in ("epss_score", "epss_percentile"):
        if col not in existing:
            conn.execute(f"ALTER TABLE scan_cves ADD COLUMN {col} REAL")
            _log(f"added column scan_cves.{col}")


def enrich(db_path, scores, scan_id=None, only_missing=False):
    """Write EPSS values onto scan_cves rows. Returns the number of rows updated.

    Only CVEs that actually appear in ``scan_cves`` are updated (the daily EPSS
    file lists hundreds of thousands of CVEs; the scan tables hold a few
    hundred), so enrichment is driven off the distinct CVE IDs already stored.
    """
    with sqlite3.connect(db_path) as conn:
        _ensure_columns(conn)

        base_where = []
        base_params = []
        if scan_id is not None:
            base_where.append("scan_id = ?")
            base_params.append(scan_id)
        if only_missing:
            base_where.append("epss_score IS NULL")

        # Restrict work to CVE IDs present in the table and covered by EPSS.
        distinct_sql = "SELECT DISTINCT UPPER(cve_id) FROM scan_cves"
        if base_where:
            distinct_sql += " WHERE " + " AND ".join(base_where)
        present = {r[0] for r in conn.execute(distinct_sql, base_params).fetchall() if r[0]}
        targets = present & set(scores)

        row_where = ["UPPER(cve_id) = ?"] + base_where
        where_sql = " AND ".join(row_where)

        updated = 0
        for cve in targets:
            score, percentile = scores[cve]
            cur = conn.execute(
                f"UPDATE scan_cves SET epss_score = ?, epss_percentile = ? WHERE {where_sql}",
                [score, percentile, cve, *base_params],
            )
            updated += cur.rowcount
        conn.commit()
    return updated


def main():
    parser = argparse.ArgumentParser(description="Enrich scan_cves with EPSS scores.")
    parser.add_argument("--db", default=_default_db_path(), help="Path to scan_metrics.db")
    parser.add_argument(
        "--scan-id", type=int, default=None,
        help="Only enrich rows for this scan_id (default: all rows).",
    )
    parser.add_argument(
        "--only-missing", action="store_true",
        help="Only fill rows that have no EPSS score yet (preserve historical values).",
    )
    parser.add_argument(
        "--max-lookback-days", type=int, default=_DEFAULT_MAX_LOOKBACK_DAYS,
        help="How many days to walk back for a published EPSS file.",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.db):
        _log(f"database not found at {args.db}; nothing to enrich")
        return 0

    text = _fetch_epss_csv(max(0, args.max_lookback_days))
    if text is None:
        _log("no EPSS file available; leaving database unchanged")
        return 0

    scores = _parse_epss(text)
    if not scores:
        _log("parsed zero EPSS scores; leaving database unchanged")
        return 0
    _log(f"parsed {len(scores)} EPSS scores")

    try:
        updated = enrich(args.db, scores, scan_id=args.scan_id, only_missing=args.only_missing)
    except sqlite3.Error as exc:
        _log(f"database error ({exc}); leaving database unchanged")
        return 0

    _log(f"updated {updated} scan_cves row(s) with EPSS data")
    return 0


if __name__ == "__main__":
    sys.exit(main())
