#!/usr/bin/env python3
"""
Merge cabinet and senate officers into the `organization` block of each year.

The presidents are the easy part of this record. The rest of the cabinet, the
vice presidents, the treasurers and secretaries, the speakers and chiefs of
staff, are named week after week in SGA's own minutes and in the yearbooks, and
almost none of it has ever been written down in one place.

Input is a JSON array:
  {"year": "1970-71", "office": "Vice President", "name": "Doug Alexander",
   "note": "one or two sentences, sourced", "senate": false,
   "src": {"label": "...", "url": "..."}}
`senate: true` files the person under the senate rather than the executive.

Anyone already recorded for that year and office is left alone, so this is safe
to rerun. Run scripts/build.py afterwards.

Usage: python3 scripts/merge_officers.py FILE [FILE ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YEARS = ROOT / "data" / "years.json"


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


def title_office(o):
    """House style: offices read as titles."""
    o = re.sub(r"\s+", " ", str(o or "").strip())
    small = {"of", "and", "for", "the", "to"}
    parts = [w if w.lower() in small else w[:1].upper() + w[1:] for w in o.split()]
    if parts:
        parts[0] = parts[0][:1].upper() + parts[0][1:]
    return " ".join(parts)


def main(paths):
    data = json.loads(YEARS.read_text())
    by_id = {y["id"]: y for y in data["years"]}
    added = dupe = skipped = unknown = 0

    for path in paths:
        for r in json.loads(Path(path).read_text()):
            y = by_id.get(r.get("year"))
            if not y:
                unknown += 1
                continue
            name = str(r.get("name") or "").strip()
            office = title_office(r.get("office"))
            src = r.get("src") or {}
            if not name or not office or not src.get("url") or not src.get("label"):
                skipped += 1
                continue
            org = y.setdefault("organization", {})
            if r.get("senate"):
                bucket = org.setdefault("senate", {}).setdefault("officers", [])
            else:
                bucket = org.setdefault("executive", [])
            if any(norm(o.get("name")) == norm(name)
                   and norm(o.get("office")) == norm(office) for o in bucket):
                dupe += 1
                continue
            entry = {"office": office, "name": name}
            if r.get("note"):
                entry["note"] = str(r["note"]).strip()
            entry["src"] = {"label": src["label"], "url": src["url"]}
            bucket.append(entry)
            added += 1

    # keep the executive in a sensible reading order rather than arrival order
    RANK = ["President", "Acting President", "Executive Vice President",
            "Administrative Vice President", "Vice President",
            "Vice President of Finance", "Chief Financial Officer",
            "Treasurer", "Chief of Staff", "Secretary", "Speaker of the Senate"]
    for y in data["years"]:
        ex = (y.get("organization") or {}).get("executive")
        if ex:
            ex.sort(key=lambda o: (RANK.index(o["office"])
                                   if o.get("office") in RANK else len(RANK),
                                   o.get("office", "")))

    YEARS.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    n = sum(len((y.get("organization") or {}).get("executive") or [])
            + len(((y.get("organization") or {}).get("senate") or {}).get("officers") or [])
            for y in data["years"])
    print(f"added {added} officers; {n} officer records now on file")
    for c, what in ((dupe, "already recorded"), (skipped, "missing a name, office or source"),
                    (unknown, "unknown academic year")):
        if c:
            print(f"  skipped {c} {what}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: merge_officers.py FILE [FILE ...]")
    main(sys.argv[1:])
