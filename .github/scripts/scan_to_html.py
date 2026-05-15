#!/usr/bin/env python3
"""Convert a scan-*.md Trivy report to styled HTML matching github.com/rancher/dashboard."""

import sys
import os
import re
import html as html_lib
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
# HTML rendering helpers
# ---------------------------------------------------------------------------

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


def _severity_badge(severity):
    s = severity.strip().upper()
    css = s if s in ("CRITICAL", "HIGH", "MEDIUM", "LOW") else "UNKNOWN"
    return f'<span class="sev sev-{css}">{esc(severity.strip())}</span>'


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
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Markdown pipe-table helpers
# ---------------------------------------------------------------------------

def _is_pipe_table_row(line):
    """True if line looks like a markdown pipe-table row."""
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|")


def _is_pipe_separator(line):
    """True if line is a markdown pipe-table separator row (| --- | ---: | etc.)."""
    if not _is_pipe_table_row(line):
        return False
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.match(r"^:?-+:?$", c) for c in cells if c)


def _parse_pipe_table(lines):
    """
    Parse a list of pipe-table markdown lines (header row, separator, data rows…).
    Returns (headers: list[str], rows: list[dict[str,str]]).
    """
    headers = [c.strip() for c in lines[0].strip().strip("|").split("|")]
    rows = []
    for line in lines[2:]:  # skip separator row at index 1
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        while len(cells) < len(headers):
            cells.append("")
        cells = cells[: len(headers)]
        rows.append(dict(zip(headers, cells)))
    return headers, rows


def render_pipe_table(headers, rows):
    """Render (headers, rows) from a markdown pipe-table as a styled HTML table."""
    if not headers or not rows:
        return ""
    out = ['<table class="report-table">']
    out.append("<thead><tr>")
    for h in headers:
        out.append(f"<th>{render_inline(h)}</th>")
    out.append("</tr></thead><tbody>")
    for row in rows:
        out.append("<tr>")
        for h in headers:
            val = row.get(h, "")
            out.append(f"<td>{render_inline(val)}</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Code-block processor
# ---------------------------------------------------------------------------

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
    """Convert the structured scan markdown to an HTML body string."""
    lines = md.split("\n")
    out = []
    i = 0
    in_ul = False
    in_images_list = False  # the "## Images Scanned" bullet list
    in_code = False
    code_lang = ""
    code_lines = []

    def close_ul():
        nonlocal in_ul, in_images_list
        if in_ul:
            if in_images_list:
                out.append("</ul>")
                in_images_list = False
            else:
                out.append("</ul>")
            in_ul = False

    while i < len(lines):
        line = lines[i]

        # ---- fenced code block ----
        if line.startswith("```"):
            if not in_code:
                close_ul()
                in_code = True
                code_lang = line[3:].strip()
                code_lines = []
            else:
                in_code = False
                block_content = "\n".join(code_lines)
                processed = _process_trivy_block(block_content)
                if processed.strip():
                    out.append(f'<div class="scan-card">{processed}</div>')
                code_lines = []
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        # ---- headings ----
        if line.startswith("# "):
            close_ul()
            out.append(f"<h1>{render_inline(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            close_ul()
            title = line[3:].strip()
            out.append(f"<h2>{render_inline(title)}</h2>")
            in_images_list = title.lower().startswith("images scanned")
        elif line.startswith("### "):
            close_ul()
            out.append(f"<h3>{render_inline(line[4:].strip())}</h3>")

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

        # ---- markdown pipe table ----
        elif _is_pipe_table_row(line):
            close_ul()
            table_lines = [line]
            while i + 1 < len(lines) and _is_pipe_table_row(lines[i + 1]):
                i += 1
                table_lines.append(lines[i])
            if len(table_lines) >= 2 and _is_pipe_separator(table_lines[1]):
                headers, rows = _parse_pipe_table(table_lines)
                if headers and rows:
                    out.append(render_pipe_table(headers, rows))
                else:
                    for tl in table_lines:
                        out.append(f"<p>{render_inline(tl.strip())}</p>")
            else:
                for tl in table_lines:
                    out.append(f"<p>{render_inline(tl.strip())}</p>")

        # ---- paragraph ----
        else:
            close_ul()
            stripped = line.strip()
            if stripped:
                out.append(f"<p>{render_inline(stripped)}</p>")

        i += 1

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


def build_html(title, body_html, source_filename):
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
    <span class="subtitle">— Trivy Scan Report</span>
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

    # Detect format: markdown if first non-blank line starts with #
    first_line = next((l for l in content.splitlines() if l.strip()), "")
    is_markdown = first_line.startswith("#")

    if is_markdown:
        content = _move_summary_to_top(content)
        body_html = _convert_markdown(content)
        title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else "Scan Report"
    else:
        body_html = _convert_raw(content)
        title = os.path.splitext(os.path.basename(input_path))[0]

    full_html = build_html(title, body_html, os.path.basename(input_path))

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
    write a styled index.html listing them all, most-recent first.

    Returns the path of the written index file.
    """
    html_dir = os.path.abspath(html_dir)
    entries = sorted(
        [
            f
            for f in os.listdir(html_dir)
            if f.endswith(".html") and f != "index.html"
        ],
        key=lambda f: (_parse_date_from_filename(f), f),
        reverse=True,
    )

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    if entries:
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

        grid_html = '<div class="reports-grid">\n' + "\n".join(cards) + "\n</div>"
    else:
        grid_html = '<p class="empty-state">No scan reports found yet.</p>'

    count = len(entries)
    subtitle = f"{count} report{'s' if count != 1 else ''} available"

    body_html = f"""
<h1>Trivy Scan Reports</h1>
<p class="index-intro">{esc(subtitle)}</p>
{grid_html}
<div class="page-footer">
  Index generated &nbsp;·&nbsp; {esc(now)}
</div>
"""

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RKE2 Toolbox — Scan Reports</title>
  <style>{CSS}{_INDEX_CSS_EXTRA}</style>
</head>
<body>
  <header class="page-header">
    <div class="brand">
      {_RANCHER_LOGO_SVG}
      RKE2 Toolbox
    </div>
    <span class="subtitle">— Trivy Scan Reports</span>
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
