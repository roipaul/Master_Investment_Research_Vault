#!/usr/bin/env python3
"""Assemble the four primer parts + sources into a numbered .docx and .pdf.

Usage:
  python3 build_primer.py --ticker POOL --company "Pool Corporation" \
      --out ./primer_out [--parts-dir .] [--no-pdf]

Expects in --parts-dir:
  part1_company.md, part2_logistics.md, part3_industry.md, part4_financial.md, sources.md

Numbering: top-level '# ' headings become "1. ", "2. " ...; second-level
'## ' headings become "1.1 ", "1.2 " ... . A table of contents is built from
those and placed at the top. The source list is appended as a final
"Sources" section. Pandoc writes the docx; LibreOffice converts to PDF.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

PARTS = [
    "part1_company.md",
    "part2_logistics.md",
    "part3_industry.md",
    "part4_financial.md",
]



def widen_first_column(md: str) -> str:
    """Give the label column of wide pipe tables more width (pandoc derives
    relative column widths from the dash counts in the separator row)."""
    out = []
    for line in md.splitlines():
        if re.match(r"^\|(\s*:?-+:?\s*\|)+\s*$", line):
            cells = line.strip().strip("|").split("|")
            if len(cells) >= 5:
                cells[0] = "-" * 9
                cells[1:] = ["-" * 5 for _ in cells[1:]]
                line = "|" + "|".join(cells) + "|"
        out.append(line)
    return "\n".join(out) + "\n"


def shrink_wide_tables(docx_path):
    """Reduce font size in wide tables so numeric columns do not wrap."""
    try:
        from docx import Document
        from docx.shared import Pt
    except ImportError:
        print("python-docx not installed; wide tables left at default size", file=sys.stderr)
        return
    doc = Document(str(docx_path))
    for t in doc.tables:
        n = len(t.columns)
        if n < 6:
            continue
        size = Pt(8) if n < 8 else Pt(7.5)
        for row in t.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.font.size = size
    doc.save(str(docx_path))

def number_headings(md: str, part_no: int):
    """Return (numbered markdown, list of (level, text) toc entries)."""
    out, toc = [], []
    sub = 0
    for line in md.splitlines():
        m1 = re.match(r"^#\s+(.*)$", line)
        m2 = re.match(r"^##\s+(.*)$", line)
        if m1:
            text = m1.group(1).strip()
            text = re.sub(r"^\d+\.\s*", "", text)
            line = f"# {part_no}. {text}"
            toc.append((1, f"{part_no}. {text}"))
        elif m2:
            sub += 1
            text = m2.group(1).strip()
            text = re.sub(r"^\d+\.\d+\s*", "", text)
            line = f"## {part_no}.{sub} {text}"
            toc.append((2, f"{part_no}.{sub} {text}"))
        out.append(line)
    return "\n".join(out), toc


def build(parts_dir: Path, ticker: str, company: str, out_dir: Path, pdf: bool):
    out_dir.mkdir(parents=True, exist_ok=True)
    body, toc = [], []
    for i, name in enumerate(PARTS, start=1):
        p = parts_dir / name
        if not p.exists():
            sys.exit(f"missing {p}")
        md, t = number_headings(widen_first_column(p.read_text(encoding="utf-8")), i)
        body.append(md)
        toc.extend(t)

    sources = parts_dir / "sources.md"
    src_md = sources.read_text(encoding="utf-8") if sources.exists() else "(no sources file)"
    body.append("# Sources\n\n" + src_md)
    toc.append((1, "Sources"))

    toc_lines = ["# Table of Contents", ""]
    for lvl, text in toc:
        toc_lines.append(("" if lvl == 1 else "    ") + f"- {text}")
    title = f"% {company} ({ticker}) — Company Primer\n\n"
    full = title + "\n".join(toc_lines) + "\n\n" + "\n\n".join(body) + "\n"

    safe = re.sub(r"[^A-Za-z0-9]+", "_", company).strip("_")
    stem = f"{safe}_{ticker}_Primer_Full"
    md_path = out_dir / f"{stem}.md"
    docx_path = out_dir / f"{stem}.docx"
    md_path.write_text(full, encoding="utf-8")

    subprocess.run(
        ["pandoc", str(md_path), "-o", str(docx_path), "--from", "markdown+pipe_tables-tex_math_dollars-raw_tex",
         "--wrap=none"],
        check=True,
    )
    shrink_wide_tables(docx_path)
    print(f"wrote {docx_path}")

    if pdf and shutil.which("soffice"):
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(out_dir), str(docx_path)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        print(f"wrote {out_dir / (stem + '.pdf')}")
    elif pdf:
        print("soffice not found; skipped PDF", file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--company", required=True)
    ap.add_argument("--out", default="primer_out")
    ap.add_argument("--parts-dir", default=".")
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()
    build(Path(a.parts_dir), a.ticker, a.company, Path(a.out), not a.no_pdf)
