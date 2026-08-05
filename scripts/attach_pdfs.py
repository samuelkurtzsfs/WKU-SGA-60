#!/usr/bin/env python3
"""
Give every citation a download link where the archive already knows one.

The OAI harvest behind data/herald-index.json records the direct fulltext URL
for each digitised issue. Any event citing one of those issue pages can carry
that URL as src.pdf, and the build then offers the file next to the citation,
so a reader can check a claim against the page it came from without leaving
the site. Safe to rerun; it only ever adds.

Usage: python3 scripts/attach_pdfs.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    hx = json.loads((ROOT / "data" / "herald-index.json").read_text())["entries"]
    pdf = {e["url"].rstrip("/"): e["pdf"] for e in hx if e.get("pdf")}

    path = ROOT / "data" / "years.json"
    data = json.loads(path.read_text())
    added = 0

    def attach(src):
        nonlocal added
        if not src or src.get("pdf") or not src.get("url"):
            return
        u = pdf.get(src["url"].rstrip("/"))
        if u:
            src["pdf"] = u
            added += 1

    for y in data["years"]:
        for e in y["events"]:
            attach(e.get("src"))
        for l in y["leaders"]:
            for s in l.get("sources") or []:
                attach(s)
        for d in y.get("documents") or []:
            attach(d.get("src"))

    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    print(f"attached {added} download links from the Herald index")


if __name__ == "__main__":
    main()
