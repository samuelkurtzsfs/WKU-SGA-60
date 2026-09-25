#!/usr/bin/env python3
"""
Report events in the same year that look like the same event written twice.

Successive research passes have described one event in two sets of words, and a
deduplicator that matches whole titles never sees it. This compares the words in
the titles instead, and flags close pairs for an editor to judge. It changes
nothing: same-day legislative business is genuinely several events, so the call
has to be made by someone reading both.

Titles are not enough on their own. Two passes can describe one meeting in two
sets of words that share nothing at all - "Three senators removed for excessive
absences" against "Three senators removed from the Senate after second censure"
is the near miss; "DEI Week funded" against "Four bills fund a month of events"
shares no word whatever. Nine such pairs were live on the site in September 2026
and this report saw none of them. So there is a second pass that ignores the
wording completely and looks at the citation: two events drawn from the same
single article and dated within three days of each other, carrying the same bill
number, sum of money or vote tally between them. That is the signature of one
meeting written up twice, once under the date it was held and once under the
date it was reported.

Run it after any merge. Exit status is 1 when anything is flagged, so it can
gate a build.

Usage: python3 scripts/check_duplicates.py [--json OUT]
"""
import itertools
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# a citation that points at one article, not at a whole issue's landing page
ARTICLE = re.compile(r"(wkuherald\.com/\d+/|wku\.edu/news/|web\.archive\.org/.*wkuherald)")
# tokens distinctive enough that sharing one means the same piece of business
BILL = re.compile(r"\b\d+[-\u2013]\d+[-\u2013][A-Z]\b")
MONEY = re.compile(r"\$[\d,]+")
TALLY = re.compile(r"\b\d+-\d+\b")
NAME = re.compile(r"\b[A-Z][a-z]{3,}\s[A-Z][a-z]{3,}\b")
STOP = {"the", "a", "an", "of", "for", "and", "to", "in", "on", "at", "is",
        "its", "with", "as", "by", "after", "over"}


def words(t):
    return set(re.sub(r"[^a-z0-9 ]", " ", str(t).lower()).split()) - STOP


def strong(e):
    """Bill numbers, sums and vote tallies: sharing one is hard to do by accident."""
    t = f"{e.get('title', '')} {e.get('body', '')}"
    return set(BILL.findall(t)) | set(MONEY.findall(t)) | set(TALLY.findall(t))


def named(e):
    t = f"{e.get('title', '')} {e.get('body', '')}"
    return set(NAME.findall(t))


def days_apart(a, b):
    try:
        return abs((date.fromisoformat(a["date"]) - date.fromisoformat(b["date"])).days)
    except (ValueError, KeyError, TypeError):
        return None


def same_source(years):
    """One article, dates a day or three apart, the same business in both."""
    out = []
    for y in years:
        by = {}
        for e in y["events"]:
            u = (e.get("src") or {}).get("url") or ""
            if u and ARTICLE.search(u):
                by.setdefault(u, []).append(e)
        for url, evs in by.items():
            for a, b in itertools.combinations(evs, 2):
                gap = days_apart(a, b)
                # same day is normal: several bills at one meeting are several events
                if gap is None or not 1 <= gap <= 3:
                    continue
                shared = strong(a) & strong(b)
                names = named(a) & named(b)
                if shared or len(names) >= 2:
                    out.append({"year": y["id"], "gap": gap, "url": url,
                                "shared": sorted(shared | names), "a": a, "b": b})
    return sorted(out, key=lambda p: -len(p["shared"]))


def candidates(years):
    out = []
    for y in years:
        for a, b in itertools.combinations(y["events"], 2):
            wa, wb = words(a["title"]), words(b["title"])
            if not wa or not wb:
                continue
            j = len(wa & wb) / len(wa | wb)
            if j >= 0.45 or (a["date"] == b["date"] and j >= 0.3):
                out.append({"year": y["id"], "similarity": round(j, 2),
                            "a": a, "b": b})
    return sorted(out, key=lambda p: -p["similarity"])


def main(argv):
    data = json.loads((ROOT / "data" / "years.json").read_text())
    pairs = candidates(data["years"])
    sourced = same_source(data["years"])
    if "--json" in argv:
        dest = Path(argv[argv.index("--json") + 1])
        dest.write_text(json.dumps({"by_title": pairs, "by_source": sourced},
                                   ensure_ascii=False, indent=1) + "\n")
        print(f"wrote {len(pairs)} title pairs and {len(sourced)} "
              f"same-source pairs to {dest}")
    else:
        for p in pairs:
            print(f'{p["year"]}  similarity {p["similarity"]}')
            print(f'   {p["a"]["date"]}  {p["a"]["title"]}')
            print(f'   {p["b"]["date"]}  {p["b"]["title"]}')
        print(f"\n{len(pairs)} pairs to judge. Same-day bills and votes are "
              f"usually separate events; read both before merging.")
        if sourced:
            print("\none article, two entries, dated within three days - the "
                  "signature of a meeting written up twice:")
            for p in sourced:
                print(f'\n{p["year"]}  {p["gap"]} day(s) apart, '
                      f'sharing {", ".join(p["shared"])}')
                print(f'   {p["a"]["date"]}  {p["a"]["title"]}')
                print(f'   {p["b"]["date"]}  {p["b"]["title"]}')
                print(f'   {p["url"]}')
            print(f"\n{len(sourced)} same-source pairs to judge. Two entries can "
                  f"honestly share one article when they report different "
                  f"business; read both.")
    return 1 if (pairs or sourced) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
