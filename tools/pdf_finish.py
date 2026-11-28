#!/usr/bin/env python3
"""Finish a digital PDF exported from TPL-E01-06 (E05 §5.9.2, C01 §5.6.1).

Browsers differ in what "Save as PDF" writes. This tool makes every digital
export carry the same document properties:
  * Title  = the document title from the cover (not the browser tab title);
  * Author = the Owner from the cover;
  * Lang   = en-US;
  * Bookmarks for Headings 1-3 and appendices. Chromium writes these itself and
    they are kept. When a browser writes none, they are rebuilt from the
    Contents page, whose entries carry the printed page numbers.

Usage (from the repository root):
    python3 tools/pdf_finish.py "REF-001 Document Master Element Reference v1.0.0.pdf"
    python3 tools/pdf_finish.py in.pdf --out out.pdf --title "..." --author "..."

The press route does the same through tools/press_export.py.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

LABELS = ("IDENTIFIER", "VERSION", "STATUS", "ISSUE DATE", "OWNER", "APPROVER", "SUPERSEDED BY", "WAIVER ID", "WAIVER EXPIRY")


class FinishError(Exception):
    pass


def cover_fields(reader: PdfReader) -> dict:
    """Read the labelled metadata block and the title from the cover page text."""
    lines = [ln.strip() for ln in (reader.pages[0].extract_text() or "").splitlines() if ln.strip()]
    out = {}
    for i, ln in enumerate(lines[:-1]):
        if ln in LABELS and lines[i + 1] not in LABELS:
            out[ln.lower()] = lines[i + 1]
    browser_title = str((reader.metadata or {}).get("/Title") or "")
    ident, ver = out.get("identifier", ""), out.get("version", "")
    m = re.match(rf"^{re.escape(ident)}\s+(.+?)\s+{re.escape(ver)}$", browser_title) if ident and ver else None
    if m:
        out["title"] = m.group(1)
    return out


def contents_outline(reader: PdfReader) -> list[tuple[int, str, int]]:
    """(level, text, page index) from the Contents page entries (number, title, printed page)."""
    import unicodedata
    entries = []
    for page in reader.pages[1:8]:
        lines = [unicodedata.normalize("NFKC", ln).strip() for ln in (page.extract_text() or "").splitlines()]
        if "Contents" not in lines:
            continue
        for ln in lines[lines.index("Contents") + 1:]:
            # Text order differs by extractor: "1.2 6Title" (page first) or "1.2 Title 6" (page last).
            m = (re.match(r"^(?:((?:\d+|[A-Z])(?:\.\d+)*)\s+)?(\d+)\s*([^\d\s].*)$", ln)
                 or re.match(r"^(?:((?:\d+|[A-Z])(?:\.\d+)*)\s+)?()(.+?)\s+(\d+)$", ln))
            if not m:
                continue
            num = m.group(1)
            pg, title = (int(m.group(2)), m.group(3)) if m.group(2) else (int(m.group(4)), m.group(3))
            if not 1 <= pg <= len(reader.pages):
                continue
            level = num.count(".") + 1 if num else 1
            entries.append((level, f"{num} {title.strip()}" if num else title.strip(), pg - 1))
    return entries


def tidy_outline(reader: PdfReader, writer: PdfWriter) -> int:
    """Trim browser bookmark titles and restore heading numbers that a browser dropped, using the Contents entries."""
    numbered = {}
    for _level, text, _idx in contents_outline(reader):
        m = re.match(r"^((?:\d+|[A-Z])(?:\.\d+)*) (.+)$", text)
        if m:
            numbered.setdefault(m.group(2), text)
    fixed = 0
    root = writer._root_object.get("/Outlines")
    stack = [root.get_object().get("/First")] if root is not None else []
    while stack:
        node = stack.pop()
        while node is not None:
            item = node.get_object()
            title = str(item.get("/Title", ""))
            new = numbered.get(title.strip(), title.strip())
            if new != title:
                item[NameObject("/Title")] = TextStringObject(new)
                fixed += 1
            if "/First" in item:
                stack.append(item["/First"])
            node = item.get("/Next")
    return fixed


def finish(src: Path, out: Path, title: str | None, author: str | None) -> dict:
    reader = PdfReader(str(src))
    fields = cover_fields(reader)
    title = title or fields.get("title")
    author = author or fields.get("owner")
    if not title or not author:
        raise FinishError("could not read the title and Owner from the cover; pass --title and --author")
    writer = PdfWriter(clone_from=reader)
    built = fixed = 0
    if not reader.outline:
        parents: dict[int, object] = {}
        for level, text, idx in contents_outline(reader):
            parent = parents.get(level - 1) if level > 1 else None
            parents[level] = writer.add_outline_item(text, idx, parent=parent)
            built += 1
        if not built:
            raise FinishError("the PDF has no bookmarks and no Contents page to build them from (E05 §5.9.2)")
    else:
        fixed = tidy_outline(reader, writer)
    writer._root_object[NameObject("/Lang")] = TextStringObject("en-US")
    writer.add_metadata({"/Title": title, "/Author": author})
    if hasattr(writer, "_root_object"):
        prefs = writer._root_object.get("/ViewerPreferences")
        if prefs is None:
            from pypdf.generic import DictionaryObject, BooleanObject
            writer._root_object[NameObject("/ViewerPreferences")] = DictionaryObject({NameObject("/DisplayDocTitle"): BooleanObject(True)})
    with open(out, "wb") as fh:
        writer.write(fh)
    check = PdfReader(str(out))
    return {"title": title, "author": author, "bookmarks": len(check.outline), "rebuilt": built, "retitled": fixed, "pages": len(check.pages)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path, help="PDF saved from the \"Export A4 PDF\" button")
    ap.add_argument("--out", type=Path, help="output path (default: overwrite the input)")
    ap.add_argument("--title", help="document title (default: read from the cover)")
    ap.add_argument("--author", help="document Owner (default: read from the cover)")
    args = ap.parse_args()
    out = args.out or args.pdf
    try:
        r = finish(args.pdf, out, args.title, args.author)
    except FinishError as e:
        print(f"PDF finish stopped: {e}", file=sys.stderr)
        return 1
    notes = []
    if r["rebuilt"]:
        notes.append("rebuilt from Contents")
    if r["retitled"]:
        notes.append(f"{r['retitled']} titles tidied")
    extra = f" ({', '.join(notes)})" if notes else ""
    print(f"Wrote {out}: {r['pages']} pages, title \"{r['title']}\", author \"{r['author']}\", "
          f"{r['bookmarks']} top-level bookmarks{extra}, language en-US")
    return 0


if __name__ == "__main__":
    sys.exit(main())
