#!/usr/bin/env python3
"""
Read the authors and sponsors off the legislation itself.

data/legislation/ holds 390 bills and resolutions as PDFs and 373 of them print
an AUTHOR line. That is primary evidence, in the document's own words, of who
wrote what: the single richest unworked source in this repository for the people
who were not presidents.

The text layer needs a real parser. pdftotext is not installed here and a naive
scrape of PostScript strings returns embedded font tables that look enough like
prose to fool a word search, which is how this was first missed.

Writes .research/legislation-authors.json for review, and prints what it found.

Usage: python3 scripts/extract_authors.py
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("needs PyMuPDF: python3 -m pip install pymupdf")

ROOT = Path(__file__).resolve().parent.parent
LEG = ROOT / "data" / "legislation"
OUT = ROOT / ".research" / "legislation-authors.json"

# a name, allowing an initial, a hyphen or an apostrophe
# Greedy on the middle, so "Jay Todd Richey" is not clipped to "Jay Todd" and
# filed as a different person from the one on the plaque.
NAME = re.compile(r"\b[A-Z][a-z]+(?:['’-][A-Za-z]+)?"
                  r"(?:\s+(?:[A-Z]\.|[A-Z][a-z]+))*"
                  r"\s+[A-Z][a-z]+(?:['’-][A-Za-z]+)?\b")
# committees, bodies and boilerplate that sit in the same field as people
# Committees, offices and constituencies sit in the same field as people and
# read exactly like names: "Legislative Operations", "Sophomore Senator",
# "Senator At-Large". Anything carrying one of these words is not a person.
ROLE_WORD = re.compile(
    r"\b(senator|senate|committee|chair|chairman|chairwoman|vice|president|"
    r"speaker|justice|council|operations|sustainability|wellbeing|experience|"
    r"affairs|relations|research|improvement|enrollment|outreach|opportunity|"
    r"communications|treasurer|secretary|director|officer|freshman|sophomore|"
    r"junior|senior|graduate|college|heights|academy|association|government|"
    r"university|board|regents|large|staff|cabinet|branch|body|caucus|"
    r"organization|organisation|foundation|fraternity|sorority|panhellenic|"
    r"interfraternity|hall|campus|student)\b", re.I)
NOT_A_PERSON = re.compile(
    r"western kentucky|bowling green|big red|spirit makes|the master|"
    r"be it|whereas|therefore|first reading|second reading|purpose|"
    r"adobe|microsoft|linux|normal drive|new york|united states|"
    r"organizational aid|mental health|associate chief|chief justice|"
    r"black history|greek life|dining dollars|study abroad", re.I)
STOP = re.compile(r"(?i)\b(sponsor|purpose|whereas|therefore|be it|first reading|"
                  r"second reading|pass\b|fail\b)")


def read(p):
    try:
        with fitz.open(p) as doc:
            return re.sub(r"\s+", " ", " ".join(pg.get_text() for pg in doc))
    except Exception:
        return ""


def names_in(blob):
    blob = STOP.split(blob)[0]
    out = []
    for m in NAME.finditer(blob):
        n = " ".join(m.group(0).split())
        if NOT_A_PERSON.search(n) or ROLE_WORD.search(n) or len(n) < 6:
            continue
        out.append(n)
    return out


def main():
    meta = {}
    idx = ROOT / "data" / "legislation.json"
    if idx.exists():
        meta = {e["file"]: e for e in json.loads(idx.read_text())["entries"]}

    rows, no_text, no_author = [], 0, 0
    files = sorted(LEG.rglob("*.pdf"))
    for p in files:
        t = read(p)
        if len(t) < 200:
            no_text += 1
            continue
        rel = str(p.relative_to(LEG))
        m = meta.get(rel, {})
        found = False
        for label in ("author", "sponsor"):
            for hit in re.finditer(rf"(?i)\b{label}(?:s|ed by)?\s*[:\-]\s*(.{{0,200}})", t):
                for n in names_in(hit.group(1)):
                    rows.append({"file": rel, "session": m.get("session") or p.parent.name,
                                 "type": m.get("type"), "title": m.get("title"),
                                 "role": label, "name": n})
                    found = True
        if not found:
            no_author += 1

    # a name that appears once may be an OCR artefact; one that recurs is a person
    counts = Counter(r["name"] for r in rows)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n")

    print(f"{len(files)} bills and resolutions read")
    print(f"  {no_text} had no usable text layer, {no_author} named nobody")
    print(f"{len(rows)} attributions, {len(counts)} distinct names")
    print(f"  {sum(1 for c in counts.values() if c > 1)} names appear on more than one document")
    by_session = Counter(r["session"] for r in rows)
    print(f"  across {len(by_session)} sessions")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    print("\nmost prolific:")
    for n, c in counts.most_common(15):
        print(f"   {c:3}  {n}")


if __name__ == "__main__":
    main()
