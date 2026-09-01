#!/usr/bin/env python3
"""Build a local index of every captioned Herald photograph of student government.

    python3 scripts/herald_photo_index.py            # build it
    python3 scripts/herald_photo_index.py Stephens   # search what was built

Writes data/herald-photos.json.

Why this exists, and it is worth reading before searching the Herald by hand.
The media endpoint returns newest first and caps a page at a hundred. A search
for SGA matches five hundred and thirty-two photographs going back to 2011, so
the first page is a solid wall of the current year and everything older sits
behind five more pages nobody thinks to ask for. Search a person's name and you
get nothing, conclude the Herald has no picture of them, and move on. It does.
Passing order=asc turns the same query into 2011 immediately.

So this pulls the whole thing once, oldest first, and leaves it on disk to grep.
One local search then beats a dozen paginated round trips, and it cannot lie to
you by running out of page.
"""

import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "herald-photos.json"
API = "https://wkuherald.com/wp-json/wp/v2/media"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# The vocabulary student government has been written about under, across sixty
# years of style changes. ASG and Associated Students are the older names.
TERMS = ["SGA", "Student Government", "student body president", "senate",
         "senator", "Associated Students", "ASG", "student regent",
         "election", "campaign", "inauguration", "administrative vice"]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for wait in (0, 5, 20):
        if wait:
            time.sleep(wait)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read()), r.headers
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            continue
    return None, None


def clean(s):
    return " ".join(re.sub(r"<[^>]+>", " ", unescape(str(s or ""))).split())


def fold(s):
    s = unicodedata.normalize("NFKD", str(s or ""))
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def harvest(first=2008, last=2027):
    """Every captioned photograph in the library, walked year by year.

    Searching by subject was the original approach and it was badly wrong. The
    terms matched about eleven hundred photographs; the library holds forty-three
    thousand. Researchers were told a zero in the index meant the Herald had no
    picture of their person, and for most of them the index had simply never
    looked. A caption saying "Bowling Green junior Jane Smith" contains none of
    the words a subject search would use.

    So nothing is filtered on the way in except the presence of a caption. The
    walk is year by year because the endpoint will not page arbitrarily deep.
    """
    seen = {}
    for year in range(first, last + 1):
        page, pages, got = 1, 1, 0
        while page <= pages:
            q = urllib.parse.urlencode({
                "after": f"{year}-01-01T00:00:00",
                "before": f"{year}-12-31T23:59:59",
                "order": "asc", "orderby": "date",
                "per_page": 100, "page": page,
                "_fields": "id,date,source_url,caption"})
            rows, hdr = get(f"{API}?{q}")
            if rows is None:
                print(f"  {year}: page {page} failed, moving on")
                break
            if page == 1:
                pages = int(hdr.get("X-WP-TotalPages", 1) or 1)
            for m in rows:
                cap = clean(m.get("caption", {}).get("rendered"))
                if not cap:
                    continue
                got += 1
                seen[m["id"]] = {"id": m["id"], "date": m["date"][:10],
                                 "url": m["source_url"], "caption": cap,
                                 "x": fold(cap)}
            page += 1
            time.sleep(float(__import__("os").environ.get("PACE", "0.4")))
        if got:
            print(f"  {year}: {got} captioned of "
                  f"{hdr.get('X-WP-Total', '?') if hdr else '?'}")
    return sorted(seen.values(), key=lambda r: r["date"])


def main():
    if len(sys.argv) > 1:
        if not OUT.is_file():
            sys.exit(f"{OUT} does not exist yet. Run this with no arguments.")
        needle = fold(" ".join(sys.argv[1:]))
        rows = json.loads(OUT.read_text())
        hits = [r for r in rows if needle in r["x"]]
        print(f"{len(hits)} of {len(rows)} captions mention {needle!r}\n")
        for r in hits:
            print(f"{r['date']}  {r['url']}")
            print(f"   {r['caption'][:200]}\n")
        return

    import os
    first = int(os.environ.get("FROM_YEAR", 2008))
    last = int(os.environ.get("TO_YEAR", 2027))
    print(f"harvesting {first} to {last}, oldest first")
    rows = harvest(first, last)
    # Merge, never replace. Cloudflare cuts the walk off partway through, and
    # a partial run that overwrote the file once cost every year it had not
    # reached yet.
    have = {r["id"]: r for r in (json.loads(OUT.read_text())
                                 if OUT.is_file() else [])}
    before = len(have)
    have.update({r["id"]: r for r in rows})
    rows = sorted(have.values(), key=lambda r: r["date"])
    OUT.write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(f"{before} already indexed, {len(rows)} now")
    years = sorted({r["date"][:4] for r in rows})
    print(f"\nwrote {OUT}: {len(rows)} captioned photographs, "
          f"{years[0]} to {years[-1]}")
    named = sum(1 for r in rows
                if re.search(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", r["caption"]))
    print(f"{named} of them name somebody")


if __name__ == "__main__":
    main()
