#!/usr/bin/env python3
"""Give a name in the roster an account of what the person did.

    python3 scripts/merge_notes.py            # show what would change
    python3 scripts/merge_notes.py --write    # write it into data/years.json

Sixty-nine people appear on the site as a name, an office and a year and
nothing else. They are almost all rank-and-file senators of the nineties whose
names survive on one attendance roll. Somebody looking themselves up finds a
line in a list. This puts a sentence behind the name.

The site reads that sentence from the `note` field on the person's record, so
that is what this writes, and it writes nothing else. Rules it will not bend:

  no source, no entry        every note must cite something with a URL
  an existing note stands    researchers disagree; the archive keeps what it
                             has rather than letting a later pass overwrite it
  the person must exist      name and year are checked against years.json, and
                             a note attached to nobody is worse than no note

This edits years.json, which the decade agents also edit, so it is written to
be run and re-run safely: a note already present is left exactly as it is.
"""

import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FINDS = ROOT / "data" / "photo-finds"
YEARS = ROOT / "data" / "years.json"


# A researcher writing for the next researcher does not sound like the archive.
# Thirteen notes in this voice reached the live site once, telling readers what
# a later pass ought to check. The site is read by the people it is about.
INTERNAL = re.compile(
    r"\b(caution|note (for|to) (the )?(editor|researcher|reader)|anyone hunting|"
    r"a later pass|whoever picks this up|do not (merge|publish|use|reopen)|"
    r"needs? (checking|confirming|verifying)|worth flagging|for the editor|"
    r"i could not|i take this|my reading|unconfirmed|not established here)\b",
    re.I)


def start(year):
    """The calendar year an academic year begins in."""
    m = re.match(r"^(\d{4})", str(year or ""))
    return int(m.group(1)) if m else 0


def publishable(fact):
    """Is this an account of a life, or a message to the next researcher?"""
    return not INTERNAL.search(fact)


def clip(fact, limit=600):
    """Cut a long account at a sentence end, never mid-word.

    Cutting on the character count alone put four notes on the site ending
    "she asked me" and "set a policy req". A note that stops mid-sentence
    reads as though the archive does not know how the sentence ended.
    """
    fact = fact.strip()
    if len(fact) <= limit:
        return fact
    ends = [m.end() for m in re.finditer(r"[.!?](?=\s|$)", fact[:limit])]
    return fact[:ends[-1]] if ends else fact[:limit].rsplit(" ", 1)[0]


def fold(s):
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s.lower())


def records(doc):
    """Every person record the roster draws a note from, by year and name."""
    out = {}
    for y in doc["years"]:
        org = y.get("organization") or {}
        sen = org.get("senate") or {}
        for lst in ((y.get("leaders") or []), (org.get("executive") or []),
                    (sen.get("officers") or []), (sen.get("members") or [])):
            for e in lst:
                if e.get("name"):
                    out.setdefault((y["id"], e["name"]), []).append(e)
        # A committee record names the committee, and its chair sits in a
        # separate field. The roster reads those as people; this did not, so a
        # person whose only office was a chairmanship could not be given an
        # account of what they did, which is exactly the sort of person who
        # most needs one.
        for c in (sen.get("committees") or []):
            if c.get("chair"):
                out.setdefault((y["id"], c["chair"]), []).append(c)
    return out


def load():
    rows = []
    for f in sorted(FINDS.glob("*-notes.json")):
        try:
            got = json.loads(f.read_text())
        except (json.JSONDecodeError, OSError) as e:
            print(f"  !! {f.name}: {e}")
            continue
        if isinstance(got, list):
            rows += [(f.name, r) for r in got if isinstance(r, dict)]
            print(f"  {f.name}: {len(got)}")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    print("reading notes")
    rows = load()
    if not rows:
        print("nothing dropped yet")
        return

    doc = json.loads(YEARS.read_text())
    recs = records(doc)
    written, refused, moved, already = [], [], [], 0

    for origin, r in rows:
        name, year = r.get("name"), r.get("year")
        fact = str(r.get("fact") or "").strip()
        src = r.get("src") or {}
        if not (name and year and fact):
            refused.append((origin, name or "?", "missing name, year or fact"))
            continue
        if not str(src.get("url", "")).startswith("http") or not src.get("label"):
            refused.append((origin, name, "no source with a url"))
            continue
        if not publishable(fact):
            refused.append((origin, name, "written to the next researcher, "
                                          "not about the person"))
            continue
        hit = recs.get((year, name))
        if not hit:
            # A researcher dates the note to the year of the thing they read,
            # which is often the year next door to the one the archive files
            # the person under: an April election belongs to the term it
            # decided. The note carries its own dates and citation, so putting
            # it on the person's nearest recorded year loses nothing.
            mine = sorted(y for (y, n) in recs if n == name)
            if mine:
                year = min(mine, key=lambda y: abs(start(y) - start(year)))
                hit = recs[(year, name)]
                moved.append((name, r["year"], year))
            else:
                near = [n for (yy, n) in recs
                        if yy == year and fold(n) == fold(name)]
                refused.append((origin, name,
                                f"spelled {near[0]!r} in {year}" if near
                                else f"nobody called {name!r} is recorded in "
                                     f"{year}"))
                continue
        for e in hit:
            if (e.get("note") or "").strip():
                already += 1
                continue
            e["note"] = clip(fact)
            if not e.get("src") and not e.get("sources"):
                e["src"] = {"label": src["label"], "url": src["url"]}
            written.append((year, name, fact))

    print()
    print(f"{len(written)} people would get an account of what they did")
    for year, name, fact in sorted(written)[:20]:
        print(f"  {year}  {name}")
        print(f"        {fact[:110]}")
    if len(written) > 20:
        print(f"  ... and {len(written) - 20} more")
    if moved:
        print(f"\n{len(moved)} were dated to a year the archive does not "
              f"record them in, and moved to their nearest:")
        for name, was, now in sorted(moved):
            print(f"  {name}: {was} -> {now}")
    if already:
        print(f"\n{already} already had a note; left as they were")
    if refused:
        print(f"\n{len(refused)} refused")
        for origin, name, why in sorted(refused):
            print(f"  {origin}: {name} - {why}")

    if not args.write:
        print("\nthis was a dry run. add --write to apply it.")
        return
    if not written:
        print("\nnothing to write")
        return
    YEARS.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(f"\nwrote {YEARS}")
    print("now run: python3 scripts/build.py && python3 scripts/check_data.py")


if __name__ == "__main__":
    main()
