#!/usr/bin/env python3
"""
Report events whose date sits outside the academic year that holds them, and
one election reported under two academic years at once.

Two blind spots made this necessary, both found on 13 October 2026.

`check_data.py` checks that an event's *year* falls inside `start .. start + 2`
and never looks at the month. So an event dated April 1981 passes inside
1981-82, although April 1981 belongs to 1980-81. A whole academic year of
slippage is invisible to it.

`check_duplicates.py` compares events only *within* one year. An election
written up once in the year it was held and again in the year its winner went
on to serve is therefore invisible to it as well, however closely the two
titles match.

Neither is a defect list. The archive files most spring elections in the year
the vote happened and a minority forward, with the administration the vote
produced, and that split is long-standing and deliberate in places: the
founding of the organisation in spring 1966 sits in 1966-67, a president who
resigned in July sits in the year he was elected to, and a schedule published
in June for the coming year sits in the year it covers. Those are editorial
calls, not faults.

What the report is for is the case the two gaps hide between them: the same
vote, reported twice, in two consecutive years, where a reader of either page
sees an election the other page also claims. Read both entries and the sources
before moving anything, and record the move - CLAUDE.md's rule is that a year
is never silently changed.

It changes nothing and always exits 0, so it can never gate a build.

Usage: python3 scripts/check_year_filing.py
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
# a title reporting a result, not a campaign, a preview or a filing deadline
RESULT = re.compile(
    r"\b(wins?|won|elected|defeats?|defeated|re-elected|sworn in|seated)\b", re.I
)


def span(start, year, month):
    """Is `year`-`month` inside the academic year beginning in `start`?"""
    if year == start:
        return month >= 8
    if year == start + 1:
        return month <= 7
    return False


def main(argv):
    ys = json.loads((ROOT / "data" / "years.json").read_text())
    if isinstance(ys, dict):
        ys = ys.get("years", ys)

    outside = []
    results = defaultdict(list)
    for y in ys:
        start, yid = y["start"], y["id"]
        for e in y.get("events", []):
            m = DATE.match(str(e.get("date", "")))
            if not m:
                continue
            year, month = int(m.group(1)), int(m.group(2))
            title = e.get("title", "")
            if not span(start, year, month):
                # a bare YYYY-01-01 is the file's way of dating to the year
                # alone, so it is reported apart from a real out-of-span date
                vague = str(e.get("date", "")).endswith("-01-01")
                outside.append((yid, str(e.get("date")), vague, title))
            if month in (3, 4, 5) and RESULT.search(title):
                results[(year, month)].append((yid, str(e.get("date")), title))

    split = {k: v for k, v in results.items() if len({r[0] for r in v}) > 1}

    if outside:
        print("events dated outside the academic year that holds them:\n")
        for yid, d, vague, title in sorted(outside, key=lambda r: (r[2], r[0])):
            tag = "  year only?" if vague else ""
            print(f"  [{yid}] {d}  {title[:66]}{tag}")
        real = sum(1 for r in outside if not r[2])
        print(
            f"\n{real} dated outside their year, and {len(outside) - real} dated "
            f"YYYY-01-01, which is how this file dates an event to the year "
            f"alone. Most of the first group are deliberate: read the entry "
            f"before you move it."
        )

    if split:
        print(
            "\none election, results reported under two academic years - a "
            "reader of either page sees a vote the other page also claims:\n"
        )
        for (year, month), rows in sorted(split.items()):
            print(f"{year}-{month:02d}, filed under {sorted({r[0] for r in rows})}")
            for yid, d, title in sorted(rows):
                print(f"   [{yid}] {d}  {title[:62]}")
            print()
        print(
            f"{len(split)} election month(s) to judge. A primary and a general "
            f"are two votes and belong apart; one vote in two years does not."
        )

    if not outside and not split:
        print("every event sits inside the year that holds it")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
