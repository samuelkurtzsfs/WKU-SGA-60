#!/usr/bin/env python3
"""
Report how many officers still have no portrait, and say on what rule.

This figure has been quoted from one research report to the next as though it
were a stable fact. It is not: it moves whenever a portrait lands, and it moves
again whenever someone guesses at the counting rule. Two consecutive passes
carried 166 and 165 without either stating a basis, which cost a later pass the
work of reconciling them. The rule lives here now, in one place, so the number
can be re-derived instead of remembered.

The rule:

  A slot is one named person holding one office in one year, taken from
  `organization.executive` and `organization.senate.officers`. Committee chairs
  are NOT slots - a committee chair is not an officer, which is trap 2 - though
  --committees will add them for comparison.

  Ordinary senate seats are excluded, because the gap is meant to measure
  cabinet and Senate leadership, not the whole Senate. "Senator" and "Senator At
  Large" are matched on their words, not their punctuation: the archive spells
  the at-large seat four ways and an exact-string exclusion list silently counted
  twelve of them as leadership offices.

  A slot is in the gap when `data/photos.json` carries no portrait for that
  person in that year. A portrait of the same person in another year does not
  fill it; --any-year reports that stricter count beside it.

It changes nothing and always exits 0. It reports; you judge.

Usage: python3 scripts/portrait_gap.py [--committees] [--any-year] [--list]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAIN_SEATS = (["senator"], ["senator", "at", "large"])


def is_plain_seat(office):
    """True for an ordinary senate seat, whatever the punctuation."""
    return re.sub(r"[^a-z]", " ", office.lower()).split() in PLAIN_SEATS


def slots(years, committees=False):
    for y in years:
        org = y.get("organization") or {}
        senate = org.get("senate") or {}
        for e in (org.get("executive") or []):
            yield y["id"], (e.get("office") or "").strip(), (e.get("name") or "").strip()
        for e in (senate.get("officers") or []):
            yield y["id"], (e.get("office") or "").strip(), (e.get("name") or "").strip()
        if committees:
            for c in (senate.get("committees") or []):
                chair = (c.get("chair") or "").strip()
                if chair:
                    yield y["id"], f'Chair, {c.get("name", "")}'.strip(), chair


def main(argv):
    years = json.loads((ROOT / "data" / "years.json").read_text())["years"]
    photos = json.loads((ROOT / "data" / "photos.json").read_text())
    by_year = {(l["year"], l["name"]) for l in photos["leaders"]}
    by_name = {l["name"] for l in photos["leaders"]}

    committees = "--committees" in argv
    every = list(slots(years, committees))
    qualifying = [s for s in every if s[2] and not is_plain_seat(s[1])]
    gap = [s for s in qualifying if (s[0], s[2]) not in by_year]
    people = {s[2] for s in gap}
    never = {s[2] for s in gap if s[2] not in by_name}

    print(f"{len(every)} officer slots in the file, "
          f"{len(qualifying)} of them cabinet or Senate leadership"
          f"{' (committee chairs included)' if committees else ''}")
    print(f"{len(gap)} of those carry no portrait for that person in that year, "
          f"held by {len(people)} people")
    print(f"{len(never)} of those people have no portrait in any year")

    if "--any-year" in argv or "--list" in argv:
        print()
        for yid, office, name in sorted(gap):
            mark = "" if name in by_name else "  (no portrait in any year)"
            print(f"  {yid}  {office}: {name}{mark}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
