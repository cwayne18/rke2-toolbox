#!/usr/bin/env python3
"""Convert scan-*.md Trivy reports and check-*.md image-update reports to styled HTML
matching github.com/rancher/dashboard."""

import sys
import os
import re
import json
import sqlite3
import html as html_lib
import urllib.request
import urllib.error
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Rancher Dashboard colour palette (Modern Light theme)
# Source: shell/assets/styles/themes/_modern.scss
# ---------------------------------------------------------------------------
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Lato:ital,wght@0,400;0,700;1,400&family=Roboto+Mono:wght@400;500&display=swap');

:root {
  --body-bg:          #FFFFFF;
  --body-text:        #141419;
  --muted:            #6C6C76;
  --border:           #DCDEE7;
  --box-bg:           #F4F5FA;
  --header-bg:        #FFFFFF;
  --header-border:    #DCDEE7;
  --link:             #1F67DB;
  --code-bg:          #F4F5FA;
  --table-header-bg:  #F4F5FA;
  --table-hover-bg:   #F4F5FA;

  /* Severity */
  --sev-critical-bg:     #B13333;
  --sev-critical-text:   #FFFFFF;
  --sev-critical-border: #7C0015;
  --sev-high-bg:         #E45C1E;
  --sev-high-text:       #FFFFFF;
  --sev-high-border:     #B03A0A;
  --sev-medium-bg:       #FFE47A;
  --sev-medium-text:     #473900;
  --sev-medium-border:   #E5A200;
  --sev-low-bg:          #DFE6F2;
  --sev-low-text:        #1F67DB;
  --sev-low-border:      #2673A6;
  --sev-unknown-bg:      #EDEFF3;
  --sev-unknown-text:    #6C6C76;
  --sev-unknown-border:  #DCDEE7;

  /* Check-images status */
  --status-needs-bg:     #E45C1E;
  --status-needs-text:   #FFFFFF;
  --status-needs-border: #B03A0A;
  --status-ok-bg:        #27AE60;
  --status-ok-text:      #FFFFFF;
  --status-ok-border:    #1A7A41;
}

*, *::before, *::after { box-sizing: border-box; }

html, body {
  margin: 0; padding: 0;
  background: var(--body-bg);
  color: var(--body-text);
  font-family: 'Lato', arial, helvetica, sans-serif;
  font-size: 14px;
  line-height: 1.6;
}

/* ---- Header ---- */
.page-header {
  background: var(--header-bg);
  border-bottom: 1px solid var(--header-border);
  padding: 0 32px;
  height: 55px;
  display: flex;
  align-items: center;
  gap: 12px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
}
.page-header .brand {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 17px;
  color: var(--body-text);
  display: flex;
  align-items: center;
  gap: 10px;
}
.page-header .brand svg { width: 28px; height: 28px; flex-shrink: 0; }
.page-header .subtitle {
  font-size: 13px;
  color: var(--muted);
  margin-left: 4px;
}

/* ---- Layout ---- */
.page-content {
  max-width: 1280px;
  margin: 0 auto;
  padding: 32px 24px 64px;
}

/* ---- Headings ---- */
h1, h2, h3, h4 {
  font-family: 'Poppins', sans-serif;
  color: var(--body-text);
  margin-top: 0;
}
h1 {
  font-size: 24px; font-weight: 600;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--border);
}
h2 {
  font-size: 17px; font-weight: 600;
  margin-top: 36px; margin-bottom: 10px;
}
.anchored-heading {
  display: flex;
  align-items: center;
  gap: 8px;
}
.heading-anchor {
  color: var(--muted);
  text-decoration: none;
  font-size: 12px;
  opacity: 0;
  transition: opacity .15s ease;
}
.anchored-heading:hover .heading-anchor,
.anchored-heading:focus-within .heading-anchor {
  opacity: 1;
}
.heading-anchor:hover {
  color: var(--link);
}
h2 code {
  font-family: 'Roboto Mono', monospace;
  font-size: 13px;
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 2px 7px;
  font-weight: 400;
}
h3 {
  font-size: 15px; font-weight: 600;
  margin-top: 24px; margin-bottom: 8px;
}

/* ---- Images list ---- */
ul.images-list {
  list-style: none;
  padding: 0; margin: 0 0 24px;
  display: flex; flex-wrap: wrap; gap: 6px;
}
ul.images-list li code {
  font-family: 'Roboto Mono', monospace;
  font-size: 12px;
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 3px 8px;
  display: inline-block;
}

/* Generic list */
ul.generic-list { margin: 8px 0 16px; padding-left: 20px; }
ul.generic-list li { margin-bottom: 3px; }
ul.generic-list li code {
  font-family: 'Roboto Mono', monospace;
  font-size: 12px;
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 5px;
}

/* ---- Scan result card ---- */
.scan-card {
  border: 1px solid var(--border);
  border-radius: 6px;
  overflow: hidden;
  margin-bottom: 8px;
}

/* ---- Tables ---- */
.report-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  background: var(--body-bg);
}
.report-table thead tr { background: var(--table-header-bg); }
.report-table th {
  padding: 10px 14px;
  text-align: left;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 11px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .05em;
  border-bottom: 1px solid var(--border);
  white-space: nowrap;
}
.report-table td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
  word-break: break-word;
}
.report-table tbody tr:last-child td { border-bottom: none; }
.report-table tbody tr:hover { background: var(--table-hover-bg); }
.report-table a {
  color: var(--link);
  text-decoration: none;
}
.report-table a:hover { text-decoration: underline; }
.report-table .num { text-align: center; font-variant-numeric: tabular-nums; }
.table-wrap { margin: 8px 0 14px; }
.table-collapsible {
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--body-bg);
  overflow: hidden;
}
.table-collapsible summary {
  cursor: pointer;
  list-style: none;
  font-family: 'Poppins', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
  background: var(--table-header-bg);
  border-bottom: 1px solid var(--border);
  padding: 10px 14px;
}
.table-collapsible summary::-webkit-details-marker { display: none; }
.table-collapsible .toggle-label::before {
  content: "▾";
  display: inline-block;
  margin-right: 8px;
  transition: transform .15s ease;
}
.table-collapsible:not([open]) .toggle-label::before {
  transform: rotate(-90deg);
}

/* vuln count colouring */
.vuln-count { font-weight: 700; }
.vuln-count.has-vulns { color: #B13333; }

/* ---- Severity badges ---- */
.sev {
  display: inline-flex;
  align-items: center;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .04em;
  white-space: nowrap;
  border-width: 1px;
  border-style: solid;
}
.sev-CRITICAL { background: var(--sev-critical-bg); color: var(--sev-critical-text); border-color: var(--sev-critical-border); }
.sev-HIGH     { background: var(--sev-high-bg);     color: var(--sev-high-text);     border-color: var(--sev-high-border);     }
.sev-MEDIUM   { background: var(--sev-medium-bg);   color: var(--sev-medium-text);   border-color: var(--sev-medium-border);   }
.sev-LOW      { background: var(--sev-low-bg);      color: var(--sev-low-text);      border-color: var(--sev-low-border);      }
.sev-UNKNOWN  { background: var(--sev-unknown-bg);  color: var(--sev-unknown-text);  border-color: var(--sev-unknown-border);  }

/* ---- Status badges (check-images) ---- */
.status {
  display: inline-flex;
  align-items: center;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .04em;
  white-space: nowrap;
  border-width: 1px;
  border-style: solid;
}
.status-NEEDS_UPDATE { background: var(--status-needs-bg); color: var(--status-needs-text); border-color: var(--status-needs-border); }
.status-UP_TO_DATE   { background: var(--status-ok-bg);    color: var(--status-ok-text);    border-color: var(--status-ok-border);    }
.status-UNKNOWN      { background: var(--sev-unknown-bg);  color: var(--sev-unknown-text);  border-color: var(--sev-unknown-border);  }

/* ---- All-clean banner ---- */
.all-clean-banner {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 18px;
  background: #EAF7EF;
  border: 1px solid var(--status-ok-border);
  border-radius: 6px;
  color: #1A7A41;
  font-weight: 600;
  font-size: 13px;
  margin-bottom: 8px;
}
.all-clean-banner .all-clean-icon {
  font-size: 18px;
  line-height: 1;
}

/* ---- Pre / fallback ---- */
pre.raw-output {
  background: var(--box-bg);
  margin: 0;
  padding: 14px 16px;
  font-family: 'Roboto Mono', monospace;
  font-size: 12px;
  color: var(--muted);
  white-space: pre-wrap;
  word-break: break-all;
  overflow-x: auto;
}

/* ---- Code inline ---- */
code {
  font-family: 'Roboto Mono', monospace;
  font-size: 12px;
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 5px;
}

/* ---- Footer ---- */
.page-footer {
  margin-top: 48px;
  padding-top: 16px;
  border-top: 1px solid var(--border);
  text-align: center;
  color: var(--muted);
  font-size: 12px;
}
.page-footer code {
  font-family: 'Roboto Mono', monospace;
  font-size: 11px;
}

/* ---- Legend ---- */
.legend {
  font-size: 12px;
  color: var(--muted);
  padding: 8px 14px;
  background: var(--box-bg);
  border-top: 1px solid var(--border);
}

/* ---- Suggested actions ---- */
.suggested-actions {
  border: 1px solid var(--border);
  border-radius: 8px;
  background: #F8FAFF;
  padding: 18px 20px 8px;
  margin-bottom: 22px;
}
.suggested-actions h2 {
  margin: 0 0 10px;
}
.suggested-actions ul {
  margin: 0;
  padding-left: 20px;
}
.suggested-actions li {
  margin-bottom: 8px;
}

/* ---- VEX candidates ---- */
.vex-candidates {
  border: 1px solid var(--border);
  border-radius: 8px;
  background: #F5FFF8;
  padding: 18px 20px 12px;
  margin-bottom: 22px;
}
.vex-candidates h2 {
  margin: 0 0 4px;
}
.vex-candidates .vex-intro {
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 12px;
}
.vex-candidates .vex-intro a {
  color: var(--link);
}
.vex-candidates table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}
.vex-candidates th {
  background: var(--table-header-bg);
  text-align: left;
  padding: 6px 10px;
  border: 1px solid var(--border);
  font-family: 'Poppins', sans-serif;
  font-size: 12px;
}
.vex-candidates td {
  padding: 6px 10px;
  border: 1px solid var(--border);
  vertical-align: top;
}
.vex-candidates tr:nth-child(even) td {
  background: var(--box-bg);
}
.vex-status {
  display: inline-block;
  padding: 2px 7px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  background: #D4EDDA;
  color: #155724;
  border: 1px solid #C3E6CB;
}
"""

# ---------------------------------------------------------------------------
# ASCII table parser
# ---------------------------------------------------------------------------

def _split_row(line):
    """Split a │-delimited table row into stripped cell strings."""
    parts = line.split("│")
    # parts[0] is before first │, parts[-1] is after last │
    return [p.strip() for p in parts[1:-1]]


def _is_full_separator(line):
    """True for lines like ├────┼────┤ or └────┴────┘ or ┌────┬────┐."""
    s = line.strip()
    return s and s[0] in ("├", "└", "┌") and all(
        c in "├─┤└┘┌┐┼┴┬" for c in s
    )


def _is_partial_separator(line):
    """True for lines like │   ├────┤   │ — an intra-row CVE separator."""
    return line.startswith("│") and ("├" in line or "┤" in line)


def parse_ascii_table(lines):
    """
    Parse a Trivy ASCII box-drawing table.

    Returns (headers: list[str], rows: list[dict[str,str]]) or (None, None).
    Multi-line cells are joined with a newline.  Rows sharing a library
    (inner ├──┤ separators) inherit empty columns from the previous row.
    """
    headers = None
    rows = []
    current = None          # dict of {header: value}
    prev_complete = None    # last fully-saved row (for inheritance)

    def save_current():
        nonlocal current, prev_complete
        if current is not None:
            rows.append(current)
            prev_complete = current
            current = None

    for line in lines:
        if not line:
            continue

        if _is_full_separator(line):
            # ┌ top border — nothing saved yet; ├ header/row sep; └ end
            if line.strip()[0] == "└":
                save_current()
            elif headers is not None:
                save_current()
            continue

        if not line.startswith("│"):
            # Non-table text (e.g. legend lines)
            save_current()
            continue

        if _is_partial_separator(line):
            # Inner CVE separator: save current row, next row inherits
            save_current()
            continue

        cells = _split_row(line)
        if not cells:
            continue

        if headers is None:
            headers = cells
            continue

        # Pad or trim to match header count
        while len(cells) < len(headers):
            cells.append("")
        cells = cells[: len(headers)]

        if current is None:
            # Start a new row; inherit empty cells from previous row
            current = {}
            for h, c in zip(headers, cells):
                if c:
                    current[h] = c
                elif prev_complete and h in prev_complete:
                    current[h] = prev_complete[h]
                else:
                    current[h] = ""
        else:
            # Continuation line: append non-empty cells
            for h, c in zip(headers, cells):
                if c:
                    sep = "\n" if current.get(h) else ""
                    current[h] = current.get(h, "") + sep + c

    save_current()
    return headers, rows if headers else (None, None)


# ---------------------------------------------------------------------------
# Markdown pipe-table parser  (used for check-*.md reports)
# ---------------------------------------------------------------------------

def parse_md_table(lines):
    """
    Parse a standard GitHub-flavoured markdown pipe table.

    *lines* is a list of raw strings (or a single string that will be split).
    Returns (headers: list[str], rows: list[dict]) or (None, None).
    Separator rows (|---|---|) are skipped.
    """
    if isinstance(lines, str):
        lines = lines.split("\n")

    table_lines = [l for l in lines if l.strip().startswith("|")]
    if not table_lines:
        return None, None

    def split_row(line):
        parts = line.strip().split("|")
        # strip leading/trailing empty strings from outer pipes
        if parts and parts[0].strip() == "":
            parts = parts[1:]
        if parts and parts[-1].strip() == "":
            parts = parts[:-1]
        return [p.strip() for p in parts]

    import re as _re

    headers = None
    rows = []
    for line in table_lines:
        cells = split_row(line)
        if headers is None:
            headers = cells
            continue
        # Skip separator row (cells like ---, :--:, etc.)
        if all(_re.match(r"^:?-+:?$", c) for c in cells if c):
            continue
        while len(cells) < len(headers):
            cells.append("")
        rows.append(dict(zip(headers, cells[: len(headers)])))

    if not headers or not rows:
        return None, None
    return headers, rows

def esc(text):
    return html_lib.escape(str(text))


def render_inline(text):
    """Escape text and convert inline markdown spans to HTML."""
    escaped = esc(text)
    # Bold: **text** → <strong>text</strong>
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    # Backtick code: `code` → <code>code</code>
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return escaped


def _slugify_heading(text):
    clean = re.sub(r"`([^`]+)`", r"\1", text)
    slug = re.sub(r"[^a-z0-9]+", "-", clean.lower()).strip("-")
    return slug or "section"


def _render_heading(level, title, heading_ids):
    base = _slugify_heading(title)
    count = heading_ids.get(base, 0) + 1
    heading_ids[base] = count
    hid = base if count == 1 else f"{base}-{count}"
    return (
        f'<h{level} id="{esc(hid)}" class="anchored-heading">'
        f"{render_inline(title)}"
        f'<a class="heading-anchor" href="#{esc(hid)}" aria-label="Link to section">#</a>'
        f"</h{level}>"
    )


def _render_collapsible_table(table_html, label, row_count):
    return (
        '<div class="table-wrap">'
        '<details class="table-collapsible" open>'
        f'<summary><span class="toggle-label">{esc(label)} ({row_count} rows)</span></summary>'
        f"{table_html}"
        "</details>"
        "</div>"
    )


def _severity_badge(severity):
    s = severity.strip().upper()
    css = s if s in ("CRITICAL", "HIGH", "MEDIUM", "LOW") else "UNKNOWN"
    return f'<span class="sev sev-{css}">{esc(severity.strip())}</span>'


def _status_badge(status):
    """Render a check-images Status cell (NEEDS_UPDATE / UP_TO_DATE / UNKNOWN)."""
    s = status.strip().upper()
    css = s if s in ("NEEDS_UPDATE", "UP_TO_DATE", "UNKNOWN") else "UNKNOWN"
    return f'<span class="status status-{css}">{esc(status.strip())}</span>'


def _vuln_count_cell(val):
    stripped = val.strip()
    try:
        n = int(stripped)
        cls = "vuln-count has-vulns" if n > 0 else "vuln-count"
    except ValueError:
        cls = "vuln-count"
    return f'<span class="{cls}">{esc(stripped)}</span>'


def _render_title_cell(text):
    """Render the Title column: turn https:// lines into links."""
    parts = text.split("\n")
    rendered = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if p.startswith("https://"):
            rendered.append(
                f'<a href="{esc(p)}" target="_blank" rel="noopener noreferrer">{esc(p)}</a>'
            )
        else:
            rendered.append(esc(p))
    return "<br>".join(rendered)


def render_table(headers, rows):
    """Render (headers, rows) as an HTML table."""
    if not headers or not rows:
        return ""

    # Detect column roles by normalised header name
    hlo = [h.lower().replace(" ", "") for h in headers]

    def col_html(h, h_norm, val):
        if h_norm == "severity":
            return _severity_badge(val) if val.strip() else ""
        if h_norm in ("vulnerabilities", "secrets"):
            return _vuln_count_cell(val)
        if h_norm == "vulnerability":
            v = val.strip()
            if re.match(r"CVE-\d{4}-\d+", v, re.I):
                url = f"https://avd.aquasec.com/nvd/{v.lower()}"
                return f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(v)}</a>'
            return esc(v)
        if h_norm == "title":
            return _render_title_cell(val)
        return esc(val)

    out = ['<table class="report-table">']
    out.append("<thead><tr>")
    for h in headers:
        out.append(f"<th>{esc(h)}</th>")
    out.append("</tr></thead><tbody>")

    for row in rows:
        out.append("<tr>")
        for h, h_norm in zip(headers, hlo):
            val = row.get(h, "")
            td_class = ' class="num"' if h_norm in ("vulnerabilities", "secrets") else ""
            out.append(f"<td{td_class}>{col_html(h, h_norm, val)}</td>")
        out.append("</tr>")

    out.append("</tbody></table>")
    return _render_collapsible_table("\n".join(out), "Scan Findings", len(rows))


def render_md_table(headers, rows):
    """Render a parsed markdown pipe table as HTML with check-images aware styling."""
    if not headers or not rows:
        return ""

    hlo = [h.lower().replace(" ", "").replace("(", "").replace(")", "") for h in headers]

    def col_html(h_norm, val):
        if h_norm == "status":
            return _status_badge(val) if val.strip() else ""
        if h_norm == "image":
            # Strip surrounding backticks if the cell value is a markdown code span
            clean = val.strip()
            if clean.startswith("`") and clean.endswith("`") and len(clean) > 1:
                clean = clean[1:-1]
            return f'<code style="font-size:11px;word-break:break-all">{esc(clean)}</code>'
        if h_norm in ("buildrepo",):
            repo = val.strip()
            if repo and repo != "N/A":
                repo_path = repo if "/" in repo else f"rancher/{repo}"
                url = f"https://github.com/{repo_path}"
                return (
                    f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">'
                    f"{esc(val)}</a>"
                )
        return render_inline(val)

    out = ['<table class="report-table">']
    out.append("<thead><tr>")
    for h in headers:
        out.append(f"<th>{render_inline(h)}</th>")
    out.append("</tr></thead><tbody>")

    for row in rows:
        out.append("<tr>")
        for h, h_norm in zip(headers, hlo):
            val = row.get(h, "")
            out.append(f"<td>{col_html(h_norm, val)}</td>")
        out.append("</tr>")

    out.append("</tbody></table>")
    return _render_collapsible_table("\n".join(out), "Table", len(rows))

def _process_trivy_block(content):
    """
    Process the raw text inside a ```text ... ``` fence.

    Finds every ASCII table and converts it to HTML; surrounding text is
    emitted as <pre class="raw-output">.  Legend lines are styled separately.
    """
    lines = content.split("\n")
    html_parts = []
    non_table_buf = []
    table_buf = []
    in_table = False
    legend_lines = []

    def flush_non_table():
        text = "\n".join(non_table_buf).strip()
        non_table_buf.clear()
        if text:
            html_parts.append(f'<pre class="raw-output">{esc(text)}</pre>')

    for line in lines:
        # Legend lines (outside tables)
        if not in_table and re.match(r"^[-•]\s+'?[-0]'?:", line):
            legend_lines.append(line)
            continue

        if not in_table:
            if line.startswith("┌"):
                flush_non_table()
                in_table = True
                table_buf = [line]
            else:
                non_table_buf.append(line)
        else:
            table_buf.append(line)
            if line.startswith("└"):
                in_table = False
                headers, rows = parse_ascii_table(table_buf)
                table_buf = []
                if headers:
                    html_parts.append(render_table(headers, rows))
                else:
                    flush_non_table()

    if table_buf:
        non_table_buf.extend(table_buf)
    flush_non_table()

    if legend_lines:
        legend_text = esc("\n".join(legend_lines))
        html_parts.append(f'<div class="legend">{legend_text}</div>')

    return "\n".join(html_parts)


# ---------------------------------------------------------------------------
# Markdown-format converter
# ---------------------------------------------------------------------------

def _convert_markdown(md):
    """Convert the structured scan/check-images markdown to an HTML body string."""
    lines = md.split("\n")
    out = []
    i = 0
    in_ul = False
    in_images_list = False  # the "## Images Scanned" bullet list
    in_code = False
    code_lang = ""
    code_lines = []
    in_pipe_table = False
    pipe_table_lines = []
    in_scan_result = False  # True while inside a "## Scan Results: `…`" section
    heading_ids = {}

    def close_ul():
        nonlocal in_ul, in_images_list
        if in_ul:
            out.append("</ul>")
            in_images_list = False
            in_ul = False

    def close_pipe_table():
        nonlocal in_pipe_table, pipe_table_lines
        if in_pipe_table:
            headers, rows = parse_md_table(pipe_table_lines)
            if headers and rows:
                out.append('<div class="scan-card">')
                out.append(render_md_table(headers, rows))
                out.append("</div>")
            in_pipe_table = False
            pipe_table_lines = []

    while i < len(lines):
        line = lines[i]

        # ---- fenced code block ----
        if line.startswith("```"):
            if not in_code:
                close_ul()
                close_pipe_table()
                in_code = True
                code_lang = line[3:].strip()
                code_lines = []
            else:
                in_code = False
                block_content = "\n".join(code_lines)
                processed = _process_trivy_block(block_content)
                if processed.strip():
                    out.append(f'<div class="scan-card">{processed}</div>')
                    if in_scan_result and "<table" not in processed:
                        out.append(
                            '<div class="all-clean-banner">'
                            '<span class="all-clean-icon">✓</span>'
                            "No vulnerabilities found — this image is clean"
                            "</div>"
                        )
                elif in_scan_result:
                    out.append(
                        '<div class="all-clean-banner">'
                        '<span class="all-clean-icon">✓</span>'
                        "No vulnerabilities found — this image is clean"
                        "</div>"
                    )
                in_scan_result = False
                code_lines = []
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        # ---- markdown pipe table ----
        if line.strip().startswith("|"):
            close_ul()
            in_pipe_table = True
            pipe_table_lines.append(line)
            i += 1
            continue

        # Any non-pipe line closes an open pipe table
        close_pipe_table()

        # ---- headings ----
        if line.startswith("# "):
            close_ul()
            in_scan_result = False
            out.append(_render_heading(1, line[2:].strip(), heading_ids))
        elif line.startswith("## "):
            close_ul()
            title = line[3:].strip()
            out.append(_render_heading(2, title, heading_ids))
            in_images_list = title.lower().startswith("images scanned")
            in_scan_result = bool(re.match(r"Scan Results:\s*`[^`]+`", title))
        elif line.startswith("### "):
            close_ul()
            in_scan_result = False
            out.append(_render_heading(3, line[4:].strip(), heading_ids))

        # ---- bullet list ----
        elif re.match(r"^[-*] ", line):
            item = line[2:].strip()
            if not in_ul:
                ul_cls = "images-list" if in_images_list else "generic-list"
                out.append(f'<ul class="{ul_cls}">')
                in_ul = True
            out.append(f"<li><code>{esc(item)}</code></li>" if in_images_list
                       else f"<li>{render_inline(item)}</li>")

        # ---- blank line ----
        elif not line.strip():
            close_ul()

        # ---- paragraph ----
        else:
            close_ul()
            stripped = line.strip()
            if stripped:
                out.append(f"<p>{render_inline(stripped)}</p>")

        i += 1

    close_pipe_table()
    close_ul()
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Raw-text converter (no markdown structure)
# ---------------------------------------------------------------------------

def _convert_raw(text):
    """
    Fallback converter for raw Trivy text files (no markdown headers).
    Finds ASCII tables and renders them; everything else is <pre>.
    """
    processed = _process_trivy_block(text)
    return f'<div class="scan-card">{processed}</div>' if processed.strip() else f'<pre class="raw-output">{esc(text)}</pre>'


# ---------------------------------------------------------------------------
# Markdown pre-processing helpers
# ---------------------------------------------------------------------------

def _move_summary_to_top(md):
    """
    Move the ``## Summary`` section from the bottom of the markdown to just
    after the opening ``# …`` title heading, so it appears at the top of the
    rendered page.
    """
    lines = md.split("\n")

    # Locate the ## Summary section
    summary_start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Summary":
            summary_start = i
            break

    if summary_start is None:
        return md  # nothing to move

    # Determine where the Summary section ends (next ## heading or EOF)
    summary_end = len(lines)
    for i in range(summary_start + 1, len(lines)):
        if lines[i].startswith("## "):
            summary_end = i
            break

    summary_lines = lines[summary_start:summary_end]
    # Remove the summary block from its original location
    remaining = lines[:summary_start] + lines[summary_end:]

    # Find insertion point: right after the first # heading line
    insert_at = 1  # fallback: just after line 0
    for i, line in enumerate(remaining):
        if line.startswith("# "):
            insert_at = i + 1
            break

    # Skip any blank lines immediately following the heading
    while insert_at < len(remaining) and not remaining[insert_at].strip():
        insert_at += 1

    new_lines = remaining[:insert_at] + [""] + summary_lines + [""] + remaining[insert_at:]
    return "\n".join(new_lines)


def _extract_summary_total_cves(md):
    """Extract total CVEs from the markdown summary table."""
    m = re.search(r"^\|\s*\*\*Total\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|", md, re.MULTILINE)
    if m:
        return int(m.group(1))

    critical = re.search(r"^\|\s*CRITICAL\s*\|\s*(\d+)\s*\|", md, re.MULTILINE)
    high = re.search(r"^\|\s*HIGH\s*\|\s*(\d+)\s*\|", md, re.MULTILINE)
    if critical and high:
        return int(critical.group(1)) + int(high.group(1))
    return None


def _count_images_scanned(md):
    """Count entries in the '## Images Scanned' section."""
    lines = md.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Images Scanned":
            start = i + 1
            break
    if start is None:
        return 0

    count = 0
    for i in range(start, len(lines)):
        line = lines[i]
        if line.startswith("## "):
            break
        if re.match(r"^\s*[-*]\s+`[^`]+`\s*$", line):
            count += 1
    return count


def _count_scanned_binaries(md):
    """Count gobinary/binary targets reported by Trivy scan output."""
    return len(re.findall(r"(?im)^\s*.+\((?:go)?binary\)\s*$", md))


def _metrics_db_path(input_path):
    """Resolve the metrics DB location."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root_db = os.path.abspath(os.path.join(script_dir, "..", "..", "reports", "scan_metrics.db"))
    if os.path.isfile(repo_root_db):
        return repo_root_db

    sibling_db = os.path.join(os.path.dirname(os.path.abspath(input_path)), "scan_metrics.db")
    if os.path.isfile(sibling_db):
        return sibling_db
    return None


def _recent_cve_totals_from_db(input_path):
    """Return most recent CVE totals from metrics DB (latest first)."""
    db_path = _metrics_db_path(input_path)
    if not db_path:
        return []
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT (critical_cves + high_cves) AS total_cves
                FROM scan_metrics
                ORDER BY scanned_at DESC, id DESC
                LIMIT 2
                """
            )
            rows = [int(r[0]) for r in cur.fetchall() if r and r[0] is not None]
            return rows
    except sqlite3.Error:
        return []


def _augment_scan_summary(md, input_path):
    """Add extra scan metrics sections into the markdown Summary section."""
    lines = md.split("\n")
    summary_start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Summary":
            summary_start = i
            break
    if summary_start is None:
        return md

    summary_end = len(lines)
    for i in range(summary_start + 1, len(lines)):
        if lines[i].startswith("## "):
            summary_end = i
            break

    summary_lines = lines[summary_start:summary_end]
    summary_text = "\n".join(summary_lines)
    add_lines = []

    if "### CVE Delta vs Previous Scan" not in summary_text:
        current_total = _extract_summary_total_cves(md)
        recent_totals = _recent_cve_totals_from_db(input_path)

        previous_total = None
        delta_value = None
        if recent_totals:
            if current_total is None:
                current_total = recent_totals[0]
            if len(recent_totals) >= 2:
                previous_total = recent_totals[1] if current_total == recent_totals[0] else recent_totals[0]
                delta_value = current_total - previous_total if current_total is not None else None

        delta_display = f"{delta_value:+d}" if delta_value is not None else "N/A"
        add_lines.extend(
            [
                "",
                "### CVE Delta vs Previous Scan",
                "",
                "| Metric | Count |",
                "| --- | ---: |",
                f"| Previous scan CVEs | {previous_total if previous_total is not None else 'N/A'} |",
                f"| Current scan CVEs | {current_total if current_total is not None else 'N/A'} |",
                f"| **Delta** | **{delta_display}** |",
                "",
            ]
        )

    if "### Scan Coverage" not in summary_text:
        image_count = _count_images_scanned(md)
        binary_count = _count_scanned_binaries(md)
        add_lines.extend(
            [
                "### Scan Coverage",
                "",
                "| Metric | Count |",
                "| --- | ---: |",
                f"| Images scanned | {image_count} |",
                f"| Binaries scanned | {binary_count} |",
                f"| **Total scanned targets** | **{image_count + binary_count}** |",
                "",
            ]
        )

    if not add_lines:
        return md

    updated_summary = summary_lines + add_lines
    new_lines = lines[:summary_start] + updated_summary + lines[summary_end:]
    return "\n".join(new_lines)


def _extract_ascii_tables_from_text(text):
    """Return all parsed ASCII tables found in *text*."""
    tables = []
    lines = text.split("\n")
    table_buf = []
    in_table = False
    for line in lines:
        if not in_table and line.startswith("┌"):
            in_table = True
            table_buf = [line]
            continue
        if in_table:
            table_buf.append(line)
            if line.startswith("└"):
                headers, rows = parse_ascii_table(table_buf)
                if headers and rows:
                    tables.append((headers, rows))
                table_buf = []
                in_table = False
    return tables


def _extract_scan_findings(md):
    """Extract scan findings grouped by image from a scan markdown report."""
    findings_by_image = {}
    lines = md.split("\n")
    current_image = None
    in_code = False
    code_lines = []

    for line in lines:
        m = re.match(r"^##\s+Scan Results:\s+`([^`]+)`", line.strip())
        if m:
            current_image = m.group(1).strip()
            findings_by_image.setdefault(current_image, [])
            continue

        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                in_code = False
                if current_image:
                    for headers, rows in _extract_ascii_tables_from_text("\n".join(code_lines)):
                        hmap = {h.lower().replace(" ", ""): h for h in headers}
                        lib_key = hmap.get("library")
                        vuln_key = hmap.get("vulnerability")
                        sev_key = hmap.get("severity")
                        status_key = hmap.get("status")
                        inst_key = hmap.get("installedversion")
                        fix_key = hmap.get("fixedversion")
                        title_key = hmap.get("title")
                        for row in rows:
                            vuln = row.get(vuln_key, "").strip() if vuln_key else ""
                            if not re.match(r"^CVE-\d{4}-\d+", vuln, re.I):
                                continue
                            findings_by_image[current_image].append(
                                {
                                    "library": row.get(lib_key, "").strip() if lib_key else "",
                                    "vulnerability": vuln,
                                    "severity": row.get(sev_key, "").strip() if sev_key else "",
                                    "status": row.get(status_key, "").strip() if status_key else "",
                                    "installed_version": row.get(inst_key, "").strip() if inst_key else "",
                                    "fixed_version": row.get(fix_key, "").strip() if fix_key else "",
                                    "title": row.get(title_key, "").strip() if title_key else "",
                                }
                            )
                code_lines = []
            continue

        if in_code:
            code_lines.append(line)

    return findings_by_image


def _fallback_suggested_actions(findings_by_image):
    """Generate deterministic suggested actions from parsed findings."""
    actions = []
    for image, findings in findings_by_image.items():
        if not findings:
            continue

        stdlib_high = [
            f for f in findings
            if f.get("library", "").lower() == "stdlib"
            and f.get("severity", "").upper() in ("CRITICAL", "HIGH")
        ]
        if stdlib_high:
            actions.append(
                f"For `{image}`, Go stdlib CVEs were detected; bump Go/toolchain to a fixed release and rebuild/publish the image."
            )

        fixed_versions = sorted(
            {
                f["fixed_version"]
                for f in findings
                if f.get("fixed_version")
            }
        )
        if fixed_versions:
            actions.append(
                f"For `{image}`, update vulnerable components to available fixed versions ({', '.join(fixed_versions[:3])}) and regenerate the image SBOM/scan."
            )

    if not actions:
        return ["No actionable CVEs were found in this report."]
    return actions[:6]


def _parse_actions_from_copilot_text(text):
    text = text.strip()
    if not text:
        return []

    try:
        payload = json.loads(text)
        if isinstance(payload, list):
            parsed = [str(x).strip() for x in payload if str(x).strip()]
            if parsed:
                return parsed
    except json.JSONDecodeError:
        pass

    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"^\d+\.\s+", "", line)
        if line:
            out.append(line)
    return out


def _copilot_suggested_actions(title, findings_by_image):
    """Ask Copilot/GitHub Models for suggested actions; fallback on local rules."""
    fallback_actions = _fallback_suggested_actions(findings_by_image)
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return fallback_actions

    findings_summary = []
    for image, findings in findings_by_image.items():
        if not findings:
            continue
        cves = sorted({f["vulnerability"] for f in findings if f.get("vulnerability")})
        libs = sorted({f["library"] for f in findings if f.get("library")})
        severities = sorted({f["severity"].upper() for f in findings if f.get("severity")})
        fixed_versions = sorted({f["fixed_version"] for f in findings if f.get("fixed_version")})
        findings_summary.append(
            {
                "image": image,
                "cves": cves[:20],
                "libraries": libs[:10],
                "severities": severities[:10],
                "fixed_versions": fixed_versions[:10],
            }
        )

    if not findings_summary:
        return fallback_actions

    model = os.getenv("COPILOT_MODEL", "openai/gpt-4.1-mini")
    user_prompt = (
        "Suggest concise remediation actions for this Trivy scan report.\n"
        "Return JSON only: an array of plain strings, 2-6 items, no markdown.\n"
        "Prefer image-specific rebuild/update actions.\n"
        f"Report title: {title}\n"
        f"Findings summary: {json.dumps(findings_summary, ensure_ascii=False)}"
    )
    payload = {
        "model": model,
        "temperature": 0.2,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are GitHub Copilot helping with container vulnerability remediation. "
                    "Prioritize concrete actions such as dependency bumps and image rebuilds."
                ),
            },
            {"role": "user", "content": user_prompt},
        ],
    }

    req = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8")
        decoded = json.loads(raw)
        content = (
            decoded.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )
        actions = _parse_actions_from_copilot_text(content)
        return actions[:6] if actions else fallback_actions
    except (
        urllib.error.URLError,
        json.JSONDecodeError,
        KeyError,
        IndexError,
        AttributeError,
        TimeoutError,
        ConnectionResetError,
    ):
        return fallback_actions


def _render_suggested_actions(actions):
    if not actions:
        return ""
    items = "\n".join(f"<li>{esc(a)}</li>" for a in actions)
    return (
        '<section class="suggested-actions">'
        "<h2>Suggested Actions</h2>"
        f"<ul>{items}</ul>"
        "</section>"
    )


# ---------------------------------------------------------------------------
# VEX candidate helpers
# ---------------------------------------------------------------------------

# Libraries associated with interpreted/scripting runtimes that are typically
# absent from the execution path in statically compiled (Go/Rust/C) workloads.
_INTERP_RUNTIME_LIBS = re.compile(
    r"(python|libpython|ruby|libruby|perl|libperl|nodejs|node\.js|npm|php|libphp"
    r"|lua|liblua|tcl|libtcl|openjdk|java|jre|jdk)",
    re.IGNORECASE,
)

# Libraries that indicate the image contains a Go binary.
_GO_BINARY_INDICATORS = {"stdlib", "k8s.io", "github.com", "golang.org", "google.golang.org"}


def _image_has_go_binaries(findings):
    """Return True if the findings suggest this image contains Go binaries."""
    for f in findings:
        lib = f.get("library", "")
        if lib.lower() == "stdlib":
            return True
        for indicator in _GO_BINARY_INDICATORS:
            if lib.lower().startswith(indicator):
                return True
    return False


def _fallback_vex_candidates(findings_by_image):
    """Generate deterministic VEX candidate suggestions from parsed findings.

    Applies simple heuristics:
    - Interpreter/scripting-runtime libraries (libpython, libruby, …) in images
      whose findings include Go-binary packages (stdlib, k8s.io/…) are likely
      not in the execution path of the workload.
    """
    candidates = []
    for image, findings in findings_by_image.items():
        if not findings:
            continue
        is_go = _image_has_go_binaries(findings)
        if not is_go:
            continue
        for f in findings:
            lib = f.get("library", "")
            if _INTERP_RUNTIME_LIBS.search(lib):
                candidates.append(
                    {
                        "cve": f.get("vulnerability", ""),
                        "image": image,
                        "library": lib,
                        "status": "not_affected",
                        "justification": "vulnerable_code_not_in_execute_path",
                        "note": (
                            f"Library `{lib}` is an interpreted-runtime component "
                            f"not present in the execution path of this statically "
                            f"compiled Go workload."
                        ),
                    }
                )
    return candidates


def _parse_vex_candidates_from_copilot_text(text):
    """Parse the LLM response for VEX candidates.

    Expects a JSON array of objects with keys: cve, image, library, status,
    justification, note.  Returns an empty list on parse failure.
    """
    text = text.strip()
    if not text:
        return []
    # Strip markdown code fences if present
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"```\s*$", "", text, flags=re.MULTILINE)
    text = text.strip()
    try:
        payload = json.loads(text)
        if not isinstance(payload, list):
            return []
        out = []
        for item in payload:
            if not isinstance(item, dict):
                continue
            cve = str(item.get("cve", "")).strip()
            if not cve:
                continue
            out.append(
                {
                    "cve": cve,
                    "image": str(item.get("image", "")).strip(),
                    "library": str(item.get("library", "")).strip(),
                    "status": str(item.get("status", "not_affected")).strip(),
                    "justification": str(item.get("justification", "")).strip(),
                    "note": str(item.get("note", "")).strip(),
                }
            )
        return out
    except json.JSONDecodeError:
        return []


def _copilot_vex_candidates(title, findings_by_image):
    """Ask the LLM to identify likely VEX candidates; fall back to local rules."""
    fallback = _fallback_vex_candidates(findings_by_image)
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return fallback

    findings_summary = []
    for image, findings in findings_by_image.items():
        if not findings:
            continue
        entries = [
            {
                "cve": f["vulnerability"],
                "library": f["library"],
                "severity": f["severity"],
                "title": f.get("title", ""),
            }
            for f in findings
            if f.get("vulnerability")
        ]
        if entries:
            findings_summary.append({"image": image, "findings": entries[:30]})

    if not findings_summary:
        return fallback

    model = os.getenv("COPILOT_MODEL", "openai/gpt-4.1-mini")
    user_prompt = (
        "Analyze the following Trivy scan findings from an RKE2 Kubernetes distribution "
        "and identify CVEs that are likely NOT exploitable in a typical RKE2 installation.\n\n"
        "Focus on:\n"
        "- Base-image OS packages (e.g. libpython, libruby, libperl, liblua, openjdk) present "
        "in images whose workloads are statically compiled Go, Rust, or C binaries — these "
        "libraries are not in the application execution path.\n"
        "- Libraries included in the image layer but never loaded by the container's primary "
        "process (e.g. scripting-language runtimes in a pure-Go service).\n"
        "- CVEs that require an interpreted language runtime to be reachable when no such "
        "runtime is invoked by the workload.\n\n"
        "For each candidate, propose an OpenVEX-compliant statement. "
        "Valid OpenVEX status values: not_affected, affected, fixed, under_investigation. "
        "Valid justification values (from the OpenVEX spec): "
        "component_not_present, vulnerable_code_not_present, "
        "vulnerable_code_not_in_execute_path, "
        "vulnerable_code_cannot_be_controlled_by_adversary, "
        "inline_mitigations_already_exist.\n\n"
        "Return ONLY a JSON array (no markdown, no extra text). Each element must have these "
        "keys: cve, image, library, status, justification, note.\n"
        "Limit your response to the 10 most confident candidates.\n\n"
        f"Report title: {title}\n"
        f"Findings: {json.dumps(findings_summary, ensure_ascii=False)}"
    )
    payload = {
        "model": model,
        "temperature": 0.1,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a container security analyst specialising in OpenVEX and "
                    "RKE2/Kubernetes workload analysis. You help teams identify CVEs that "
                    "are not exploitable due to the workload's runtime characteristics, "
                    "following the automation patterns used in rancher/image-scanning. "
                    "Respond only with valid JSON."
                ),
            },
            {"role": "user", "content": user_prompt},
        ],
    }

    req = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
        decoded = json.loads(raw)
        content = (
            decoded.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )
        candidates = _parse_vex_candidates_from_copilot_text(content)
        return candidates if candidates else fallback
    except (
        urllib.error.URLError,
        json.JSONDecodeError,
        KeyError,
        IndexError,
        AttributeError,
        TimeoutError,
        ConnectionResetError,
    ):
        return fallback


def _render_vex_candidates(candidates):
    """Render the Potential VEX Candidates section as an HTML string."""
    if not candidates:
        return ""
    rows = []
    for c in candidates:
        cve = c.get("cve", "")
        cve_link = (
            f'<a href="https://avd.aquasec.com/nvd/{cve.lower()}" '
            f'target="_blank" rel="noopener noreferrer">{esc(cve)}</a>'
            if re.match(r"^CVE-\d{4}-\d+$", cve, re.I)
            else esc(cve)
        )
        image = esc(c.get("image", ""))
        library = esc(c.get("library", ""))
        status = esc(c.get("status", "not_affected"))
        justification = esc(c.get("justification", ""))
        note = esc(c.get("note", ""))
        rows.append(
            f"<tr>"
            f"<td>{cve_link}</td>"
            f'<td><code style="font-size:11px;word-break:break-all">{image}</code></td>'
            f"<td><code>{library}</code></td>"
            f'<td><span class="vex-status">{status}</span></td>'
            f"<td>{justification}</td>"
            f"<td>{note}</td>"
            f"</tr>"
        )
    rows_html = "\n".join(rows)
    return (
        '<section class="vex-candidates">'
        '<h2 id="potential-vex-candidates-automated-recommendations" class="anchored-heading">'
        "Potential VEX Candidates (Automated Recommendations)"
        '<a class="heading-anchor" href="#potential-vex-candidates-automated-recommendations" aria-label="Link to section">#</a>'
        "</h2>"
        '<p class="vex-intro">'
        "The following CVEs may be suitable for "
        '<a href="https://openvex.dev/" target="_blank" rel="noopener noreferrer">OpenVEX</a> '
        "<code>not_affected</code> statements based on workload characteristics. "
        "Review each entry before submitting a formal VEX statement. "
        "Inspired by the <em>auto-vex-*</em> workflows in "
        '<a href="https://github.com/rancher/image-scanning" target="_blank" rel="noopener noreferrer">'
        "rancher/image-scanning</a>."
        "</p>"
        '<div class="table-wrap"><details class="table-collapsible" open>'
        f'<summary><span class="toggle-label">Potential VEX Candidates ({len(candidates)} rows)</span></summary>'
        '<table class="report-table">'
        "<thead><tr>"
        "<th>CVE</th>"
        "<th>Image</th>"
        "<th>Library</th>"
        "<th>Proposed Status</th>"
        "<th>Justification</th>"
        "<th>Note</th>"
        "</tr></thead>"
        f"<tbody>{rows_html}</tbody>"
        "</table>"
        "</details></div>"
        "</section>"
    )


# ---------------------------------------------------------------------------
# Full HTML document builder
# ---------------------------------------------------------------------------

_RANCHER_LOGO_SVG = (
    '<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">'
    '<circle cx="16" cy="16" r="14" fill="#2F68DF"/>'
    '<path d="M9 16.5l4.5 4.5 9.5-9.5" stroke="white" '
    'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
    '</svg>'
)


def build_html(title, body_html, source_filename, subtitle="— Report"):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <style>{CSS}</style>
</head>
<body>
  <header class="page-header">
    <div class="brand">
      {_RANCHER_LOGO_SVG}
      RKE2 Toolbox
    </div>
    <span class="subtitle">{esc(subtitle)}</span>
  </header>
  <main class="page-content">
    {body_html}
    <div class="page-footer">
      Generated from <code>{esc(source_filename)}</code> &nbsp;·&nbsp; {esc(now)}
    </div>
  </main>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def convert(input_path, output_path=None):
    with open(input_path, encoding="utf-8") as fh:
        content = fh.read()

    basename = os.path.basename(input_path)

    # Detect report type from filename prefix
    if basename.startswith("check-"):
        subtitle = "— Check Images Report"
    else:
        subtitle = "— Trivy Scan Report"

    # Detect format: markdown if first non-blank line starts with #
    first_line = next((l for l in content.splitlines() if l.strip()), "")
    is_markdown = first_line.startswith("#")

    if is_markdown:
        if basename.startswith("scan-"):
            content = _augment_scan_summary(content, input_path)
        if not basename.startswith("check-"):
            content = _move_summary_to_top(content)
        body_html = _convert_markdown(content)
        title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Report"
        if basename.startswith("scan-"):
            findings_by_image = _extract_scan_findings(content)
            suggested_actions = _copilot_suggested_actions(title, findings_by_image)
            vex_candidates = _copilot_vex_candidates(title, findings_by_image)
            body_html = (
                _render_suggested_actions(suggested_actions)
                + _render_vex_candidates(vex_candidates)
                + body_html
            )
    else:
        body_html = _convert_raw(content)
        title = os.path.splitext(basename)[0]

    full_html = build_html(title, body_html, basename, subtitle)

    if output_path is None:
        base = os.path.splitext(input_path)[0]
        output_path = base + ".html"

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(full_html)

    return output_path


# ---------------------------------------------------------------------------
# Index page generator
# ---------------------------------------------------------------------------

_INDEX_CSS_EXTRA = """
/* ---- Index card grid ---- */
.index-intro {
  color: var(--muted);
  margin-bottom: 32px;
  font-size: 14px;
}
.reports-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
  margin-top: 16px;
}
.report-card {
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--body-bg);
  padding: 20px 22px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: box-shadow .15s, border-color .15s;
  text-decoration: none;
  color: inherit;
}
.report-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,.10);
  border-color: var(--link);
}
.report-card .rc-name {
  font-family: 'Roboto Mono', monospace;
  font-size: 13px;
  font-weight: 500;
  color: var(--link);
  word-break: break-all;
}
.report-card .rc-date {
  font-size: 12px;
  color: var(--muted);
}
.report-card .rc-arrow {
  margin-left: auto;
  color: var(--muted);
  font-size: 16px;
  align-self: flex-start;
}
.rc-header {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}
.empty-state {
  color: var(--muted);
  font-size: 14px;
  padding: 48px 0;
  text-align: center;
}
"""


def _parse_date_from_filename(name):
    """
    Try to parse a date from filenames like scan-20260515-1.html.
    Returns a datetime or datetime.min so sorting always works.
    """
    m = re.search(r"(\d{8})", name)
    if m:
        try:
            return datetime.strptime(m.group(1), "%Y%m%d")
        except ValueError:
            pass
    return datetime.min


def generate_index(html_dir):
    """
    Scan *html_dir* for *.html files (excluding index.html itself) and
    write a styled index.html with two sections: Trivy Scan Reports and
    Check Images Reports, each showing cards sorted most-recent first.

    Returns the path of the written index file.
    """
    html_dir = os.path.abspath(html_dir)
    all_entries = sorted(
        [
            f
            for f in os.listdir(html_dir)
            if f.endswith(".html") and f != "index.html"
        ],
        key=lambda f: (_parse_date_from_filename(f), f),
        reverse=True,
    )

    scan_entries = [f for f in all_entries if f.startswith("scan-")]
    check_entries = [f for f in all_entries if f.startswith("check-")]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    def _make_cards(entries):
        cards = []
        for fname in entries:
            m = re.search(r"(\d{8})", fname)
            date_str = ""
            if m:
                try:
                    date_str = datetime.strptime(m.group(1), "%Y%m%d").strftime(
                        "%B %d, %Y"
                    )
                except ValueError:
                    pass

            stem = os.path.splitext(fname)[0]
            card = (
                f'<a class="report-card" href="{esc(fname)}">'
                f'  <div class="rc-header">'
                f'    <div>'
                f'      <div class="rc-name">{esc(stem)}</div>'
                + (f'      <div class="rc-date">{esc(date_str)}</div>' if date_str else "")
                + f"    </div>"
                f'    <span class="rc-arrow">&#8594;</span>'
                f"  </div>"
                f"</a>"
            )
            cards.append(card)
        return cards

    def _section(title, entries, empty_msg):
        if entries:
            cards = _make_cards(entries)
            grid = '<div class="reports-grid">\n' + "\n".join(cards) + "\n</div>"
        else:
            grid = f'<p class="empty-state">{esc(empty_msg)}</p>'
        count = len(entries)
        subtitle_text = f"{count} report{'s' if count != 1 else ''} available"
        return (
            f'<h2>{esc(title)}</h2>'
            f'<p class="index-intro">{esc(subtitle_text)}</p>'
            f"{grid}"
        )

    body_html = (
        "<h1>RKE2 Toolbox Reports</h1>\n"
        + _section("Trivy Scan Reports", scan_entries, "No scan reports found yet.")
        + "\n"
        + _section("Check Images Reports", check_entries, "No check-images reports found yet.")
        + f'\n<div class="page-footer">Index generated &nbsp;·&nbsp; {esc(now)}</div>'
    )

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RKE2 Toolbox — Reports</title>
  <style>{CSS}{_INDEX_CSS_EXTRA}</style>
</head>
<body>
  <header class="page-header">
    <div class="brand">
      {_RANCHER_LOGO_SVG}
      RKE2 Toolbox
    </div>
    <span class="subtitle">— Reports</span>
  </header>
  <main class="page-content">
    {body_html}
  </main>
</body>
</html>"""

    index_path = os.path.join(html_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as fh:
        fh.write(full_html)

    return index_path


def main():
    if len(sys.argv) < 2:
        print(
            f"Usage: {sys.argv[0]} <scan-file.md> [output.html]\n"
            f"       {sys.argv[0]} --index <html-dir>",
            file=sys.stderr,
        )
        sys.exit(1)

    if sys.argv[1] == "--index":
        if len(sys.argv) < 3:
            print(f"Usage: {sys.argv[0]} --index <html-dir>", file=sys.stderr)
            sys.exit(1)
        html_dir = sys.argv[2]
        if not os.path.isdir(html_dir):
            print(f"Error: directory not found: {html_dir}", file=sys.stderr)
            sys.exit(1)
        out = generate_index(html_dir)
        print(f"Index written to: {out}")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.isfile(input_file):
        print(f"Error: file not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    out = convert(input_file, output_file)
    print(f"HTML report written to: {out}")


if __name__ == "__main__":
    main()
