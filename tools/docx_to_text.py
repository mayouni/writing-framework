#!/usr/bin/env python3
"""docx_to_text — Word files to Markdown-ish text, for a study of a manuscript (as for the Ring book archive).

    python docx_to_text.py <file.docx|folder>... --out <folder>

Headings become `#` lines (from Word's Heading styles), code paragraphs (a Code/Source style, or a single monospace font) are indented
four spaces, list paragraphs get `- `, notes/tips/quotes get `> `, captions are italic, tables become pipe rows. Images are dropped
(a Word file whose code was pasted as images keeps only its prose; say so in the study). A `_stats.json` is written beside the texts:
words, sentences, mean sentence, paragraphs, headings, code lines, questions, exclamations, I / we / you counts, prose only.
Needs python-docx.
"""
import json, re, sys
from pathlib import Path
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn


def iter_blocks(d):
    for child in d.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, d)
        elif child.tag == qn("w:tbl"):
            yield Table(child, d)


def para_md(p):
    style = (p.style.name if p.style is not None else "") or ""
    text = p.text.rstrip()
    if not text:
        return None
    m = re.match(r"Heading (\d)", style)
    if m:
        return "#" * int(m.group(1)) + " " + text
    if style.lower().startswith("title"):
        return "# " + text
    fonts = {r.font.name for r in p.runs if r.font is not None and r.font.name}
    mono = len(fonts) == 1 and any(("Courier" in f or "Consolas" in f or "Mono" in f) for f in fonts)
    s = style.lower()
    if "code" in s or "source" in s or mono:
        return "    " + text
    if "list" in s or "bullet" in s:
        return "- " + text
    if any(w in s for w in ("quote", "note", "tip", "caution", "sidebar")):
        return "> " + text
    if "caption" in s:
        return "*" + text + "*"
    return text


def extract(path):
    d = docx.Document(str(path))
    lines = []
    for b in iter_blocks(d):
        if isinstance(b, Paragraph):
            md = para_md(b)
            if md is not None:
                lines.append(md)
        else:
            rows = ["| " + " | ".join(c.text.replace("\n", " ").strip() for c in r.cells) + " |" for r in b.rows]
            if rows:
                lines += [rows[0], "|" + "---|" * (rows[0].count("|") - 1)] + rows[1:] + [""]
    return "\n\n".join(lines)


def stats(text):
    prose = "\n".join(l for l in text.split("\n") if not l.startswith(("    ", "|", "#", "*")))
    words = re.findall(r"[A-Za-zÀ-ÿ'’\-]+", prose)
    sents = [s for s in re.split(r"(?<=[.!?])\s+", prose) if len(s.split()) > 1]
    paras = [p for p in prose.split("\n\n") if p.strip()]
    return dict(words=len(words), sentences=len(sents), avg_sentence=round(len(words) / max(1, len(sents)), 1), paragraphs=len(paras),
                headings=sum(1 for l in text.split("\n") if l.startswith("#")), code_lines=sum(1 for l in text.split("\n") if l.startswith("    ")),
                questions=sum(1 for s in sents if s.strip().endswith("?")), exclamations=sum(1 for s in sents if s.strip().endswith("!")),
                I=sum(1 for w in words if w == "I"), we=sum(1 for w in words if w.lower() in ("we", "our", "us", "let's")),
                you=sum(1 for w in words if w.lower() in ("you", "your")))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else Path("text")
    out.mkdir(parents=True, exist_ok=True)
    files = []
    for a in args:
        p = Path(a)
        files += sorted(x for x in p.rglob("*.docx") if not x.name.startswith("~$")) if p.is_dir() else [p]
    summary = {}
    for f in files:
        try:
            text = extract(f)
        except Exception as e:
            print("FAILED", f.name, e); continue
        (out / (f.stem + ".md")).write_text(text, encoding="utf-8")
        summary[f.stem] = stats(text)
        s = summary[f.stem]
        print(f"{f.stem[:40]:40s} words {s['words']:6d} sents {s['sentences']:5d} avg {s['avg_sentence']:5} code {s['code_lines']:5d}")
    (out / "_stats.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
