#!/usr/bin/env python3
"""
Sweep the entire digitised UA records collection (the Herald back file and more)
through the archive's OAI harvesting interface, and pull every article-index
line that mentions student government.

Writes data/herald-index.json: one entry per matching archive item, with the
item's date, its title (issue label), its TopSCHOLAR URL, and every line of its
article index that matches the keyword set. These lines become the complete
timeline. Paced politely; resumable by rerunning (skips known URLs).

    python3 scripts/harvest_herald_index.py --all

keeps EVERYTHING instead, into data/herald-index-full.json: every dated item and
every line of its article index, whether or not student government is named.
The filtered file is what the timeline renders, but the filter is a real blind
spot for research: a president named in a headline that does not contain "SGA",
"ASG" or "student government" cannot be found in it, and several of this
archive's hardest questions turned on exactly that. Harvest the full index when
you need to search the Herald rather than render it.
"""
import json, re, sys, time, urllib.request
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
KEEP_ALL = "--all" in sys.argv
OUT = ROOT / "data" / ("herald-index-full.json" if KEEP_ALL else "herald-index.json")
BASE = "https://digitalcommons.wku.edu/do/oai/"
NS = {"oai": "http://www.openarchives.org/OAI/2.0/",
      "dc": "http://purl.org/dc/elements/1.1/"}
KW = re.compile(r"\b(sga|asg|associated student|student government|"
                r"student body president|student regent)\b", re.I)
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = urllib.request.urlopen(req, timeout=90).read()
    time.sleep(2.5)
    return data


def main():
    existing = {}
    if OUT.exists():
        existing = {e["url"]: e for e in json.loads(OUT.read_text())["entries"]}
    url = BASE + "?verb=ListRecords&metadataPrefix=document-export&set=publication:dlsc_ua_records"
    entries = dict(existing)
    pages = 0
    while url:
        try:
            xml = fetch(url)
        except Exception as e:
            print(f"stopped at page {pages}: {e}", file=sys.stderr)
            break
        root = ET.fromstring(xml)
        for rec in root.iter("{http://www.openarchives.org/OAI/2.0/}record"):
            item_url = next((el.text.strip() for el in rec.iter()
                             if el.tag.endswith("coverpage-url") and el.text), "") or \
                       next((el.text.strip() for el in rec.iter()
                             if el.tag.endswith("identifier") and el.text
                             and "/dlsc_ua_records/" in el.text), "")
            pdf = next((el.text.strip() for el in rec.iter()
                        if el.tag.endswith("fulltext-url") and el.text), "")
            pdf = pdf.replace("&amp;", "&").replace("&unstamped=1", "")
            if not item_url or item_url in entries:
                continue
            title = next((el.text for el in rec.iter() if el.tag.endswith("title") and el.text), "")
            desc = " \n ".join(el.text for el in rec.iter()
                               if el.text and ("description" in el.tag or el.tag.endswith("abstract")))
            # The document-export schema calls this publication-date. It has been
            # through other names, so the older ones are still tried after it;
            # miss it and every record fails the dating law and nothing is kept.
            date = ""
            for want in ("publication-date", "date.created", "created", "date"):
                date = next((el.text for el in rec.iter()
                             if el.tag.split("}")[-1] == want and el.text), "")
                if date:
                    break
            date = (date or "")[:10]
            if not KEEP_ALL and not (KW.search(title) or KW.search(desc)):
                continue
            lines = [ln.strip() for ln in re.split(r"[\n\r]+|(?<=[.?!])\s{2,}", desc)]
            if KEEP_ALL:
                hits = [ln[:300] for ln in lines if ln]
            else:
                hits = [ln[:300] for ln in lines if ln and KW.search(ln)]
                if not hits and KW.search(title):
                    hits = [title[:300]]
            if not re.match(r"\d{4}", date):
                continue  # the dating law: no year, no timeline
            entries[item_url] = {"date": date, "issue": title[:160],
                                 "url": item_url, "pdf": pdf,
                                 "lines": hits if KEEP_ALL else hits[:12]}
        pages += 1
        if pages % 10 == 0:
            print(f"page {pages}: {len(entries)} matching items", flush=True)
        tok = root.findtext(".//oai:resumptionToken", "", NS)
        url = BASE + f"?verb=ListRecords&resumptionToken={tok}" if tok else None
    OUT.write_text(json.dumps(
        {"entries": sorted(entries.values(), key=lambda e: e["date"])},
        ensure_ascii=False, indent=1) + "\n")
    total_lines = sum(len(e["lines"]) for e in entries.values())
    print(f"done: {len(entries)} matching items, {total_lines} article lines")


if __name__ == "__main__":
    main()
