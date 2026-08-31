#!/usr/bin/env python3
"""Search a Talisman on archive.org and pull page images out of it.

    python3 scripts/talisman.py --years
    python3 scripts/talisman.py 1975 "LaCivita"
    python3 scripts/talisman.py 1975 --page 112 --out /tmp/p112.jpg

Why this exists. The yearbooks are the best source of portraits the archive
has, and TopSCHOLAR refuses everything after a burst, so a dozen researchers
hunting there at once get nothing. The same volumes sit on archive.org, which
does not rate limit, at 3116 by 4146 a page.

Searching them takes one trick. The OCR text is a single stream with no page
breaks in it, and the file that maps a position in that stream back to a page
is undocumented: the first two numbers of each row in the page index are the
character range of that leaf. Everything here rests on that.

Downloads are cached under the scratch directory, so the first search of a
volume takes a moment and the rest are instant.
"""

import argparse
import bisect
import gzip
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

CACHE = Path.home() / ".cache" / "sga60-talisman"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# The volumes archive.org holds. Everything else has to come off TopSCHOLAR,
# where the pacing rule in CLAUDE.md applies.
YEARS = [1943, 1946, 1947, 1963, 1964, 1965, 1971, 1972, 1973, 1974, 1975,
         1976, 1977, 1978, 1979, 1980, 1981, 1986, 1987]


def item(year):
    return f"talisman{year}west"


def fetch(url, path, binary=True):
    if path.exists() and path.stat().st_size:
        return path.read_bytes() if binary else path.read_text()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = r.read()
    except (urllib.error.URLError, TimeoutError) as e:
        sys.exit(f"could not fetch {url}: {e}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def load(year):
    """The OCR text of a volume, and the leaf each character sits on."""
    it = item(year)
    base = f"https://archive.org/download/{it}"
    d = CACHE / it
    txt = gzip.decompress(
        fetch(f"{base}/{it}_hocr_searchtext.txt.gz", d / "search.txt.gz")
    ).decode("utf-8", "replace")
    idx = json.loads(gzip.decompress(
        fetch(f"{base}/{it}_hocr_pageindex.json.gz", d / "index.json.gz")))
    return txt, [e[0] for e in idx]


def search(year, term, window=110):
    txt, starts = load(year)
    hits = []
    for m in re.finditer(re.escape(term), txt, re.I):
        leaf = bisect.bisect_right(starts, m.start()) - 1
        a = max(0, m.start() - window)
        ctx = " ".join(txt[a:m.end() + window].split())
        hits.append((leaf, ctx))
    return hits


def page_url(year, leaf, width=2400):
    return f"https://archive.org/download/{item(year)}/page/n{leaf}_w{width}.jpg"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("year", nargs="?", type=int)
    ap.add_argument("term", nargs="?")
    ap.add_argument("--page", type=int, help="download this leaf instead")
    ap.add_argument("--width", type=int, default=2400)
    ap.add_argument("--out")
    ap.add_argument("--years", action="store_true",
                    help="list the volumes archive.org has")
    args = ap.parse_args()

    if args.years:
        print("on archive.org, no rate limit:")
        print("  " + ", ".join(str(y) for y in YEARS))
        print("every other year has to come off TopSCHOLAR, paced.")
        return
    if not args.year:
        ap.error("give a year, or --years")
    if args.year not in YEARS:
        sys.exit(f"{args.year} is not on archive.org. Have: "
                 + ", ".join(str(y) for y in YEARS))

    if args.page is not None:
        url = page_url(args.year, args.page, args.width)
        out = Path(args.out or f"talisman{args.year}-n{args.page}.jpg")
        data = fetch(url, out)
        if data[:2] != b"\xff\xd8":
            sys.exit(f"{out} came back as {data[:16]!r}, not a JPEG")
        print(f"{out}  {len(data) // 1024} KB")
        return

    if not args.term:
        ap.error("give a term to search for, or --page")
    hits = search(args.year, args.term)
    if not hits:
        print(f"{args.term!r} is not in the {args.year} Talisman")
        print("OCR misreads names, so try a surname alone before believing it")
        return
    seen = set()
    for leaf, ctx in hits:
        print(f"leaf n{leaf}")
        print(f"   {ctx}")
        if leaf not in seen:
            seen.add(leaf)
    print()
    print(f"{len(hits)} hits on {len(seen)} leaves. To look at one:")
    y = args.year
    print(f"   python3 scripts/talisman.py {y} --page "
          f"{sorted(seen)[0]} --out /tmp/p.jpg")


if __name__ == "__main__":
    main()
