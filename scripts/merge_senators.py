#!/usr/bin/env python3
"""
Merge the rank and file of the Congress and the Senate into data/years.json.

These are not officers and are kept apart from them: they go under
`organization.senate.members`, while the speakers, secretaries and justices stay
in `organization.senate.officers`. Thousands of people have sat in this chamber
and the archive held ten of them by name before this pass.

Input is a JSON array:
  {"year": "2004-05", "name": "Josh Collins", "seat": "Senator at Large",
   "note": "optional, only where a source shows them doing something",
   "src": {"label": "...", "url": "..."}}

Anyone already recorded for that year, as a member OR as an officer, is skipped,
so this is safe to rerun and will not duplicate somebody who has since been
promoted into the officer list.

Usage: python3 scripts/merge_senators.py FILE [FILE ...]
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YEARS = ROOT / "data" / "years.json"


def key(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", s.lower())


def main(paths):
    data = json.loads(YEARS.read_text())
    by_id = {y["id"]: y for y in data["years"]}

    # everybody already on record for a year, in any capacity
    known = {}
    for yid, y in by_id.items():
        org = y.get("organization") or {}
        names = {key(o.get("name")) for o in (org.get("executive") or [])}
        sen = org.get("senate") or {}
        names |= {key(o.get("name")) for o in (sen.get("officers") or [])}
        names |= {key(m.get("name")) for m in (sen.get("members") or [])}
        names |= {key(l.get("name")) for l in y["leaders"]}
        known[yid] = names

    added = dupe = skipped = unknown = 0
    for path in paths:
        for r in json.loads(Path(path).read_text()):
            y = by_id.get(r.get("year"))
            if not y:
                unknown += 1
                continue
            name = str(r.get("name") or "").strip()
            src = r.get("src") or {}
            if not name or len(name.split()) < 2 or not src.get("url") or not src.get("label"):
                skipped += 1
                continue
            if key(name) in known[y["id"]]:
                dupe += 1
                continue
            sen = y.setdefault("organization", {}).setdefault("senate", {})
            entry = {"name": name}
            if r.get("seat"):
                entry["seat"] = str(r["seat"]).strip()
            if r.get("note"):
                entry["note"] = str(r["note"]).strip()
            entry["src"] = {"label": src["label"], "url": src["url"]}
            sen.setdefault("members", []).append(entry)
            known[y["id"]].add(key(name))
            added += 1

    for y in data["years"]:
        mem = ((y.get("organization") or {}).get("senate") or {}).get("members")
        if mem:
            mem.sort(key=lambda m: m["name"].split()[-1].lower())

    YEARS.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    total = sum(len(((y.get("organization") or {}).get("senate") or {}).get("members") or [])
                for y in data["years"])
    years_with = sum(1 for y in data["years"]
                     if ((y.get("organization") or {}).get("senate") or {}).get("members"))
    print(f"added {added} members; {total} now on record across {years_with} years")
    for c, what in ((dupe, "already recorded for that year"),
                    (skipped, "missing a full name or a source"),
                    (unknown, "unknown academic year")):
        if c:
            print(f"  skipped {c} {what}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: merge_senators.py FILE [FILE ...]")
    main(sys.argv[1:])
