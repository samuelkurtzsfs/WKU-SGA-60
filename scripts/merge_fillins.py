#!/usr/bin/env python3
"""
Add presidents the record missed: the people who finished a year after the
elected president left.

SGA elects in April and the winner serves the following academic year, so a
president named in the fall and a different one named in the spring means the
office changed hands. The Chambers plaque carries one name per year and cannot
show that, which is why these people go missing. Input is the year-by-year
verification written by the research pass.

A finding is merged only when it is marked confirmed and carries a source. The
rest are printed for an editor to chase, never published on a maybe.

Usage: python3 scripts/merge_fillins.py .research/fillins-*.json
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def clean_date(s):
    s = str(s or "").strip()
    if not re.fullmatch(r"\d{4}(-\d{2})?(-\d{2})?", s):
        return None
    parts = s.split("-")
    return f"{parts[0]}-{parts[1] if len(parts) > 1 else '01'}-" \
           f"{parts[2] if len(parts) > 2 else '01'}"


def main(paths):
    path = ROOT / "data" / "years.json"
    data = json.loads(path.read_text())
    by_id = {y["id"]: y for y in data["years"]}

    added = held = 0
    for p in paths:
        for r in json.loads(Path(p).read_text()):
            y = by_id.get(r.get("year"))
            if not y:
                continue
            for person in r.get("new_people") or []:
                name = (person.get("name") or "").strip()
                src = person.get("src") or {}
                if not name or not src.get("url"):
                    continue
                if any(l["name"] == name for l in y["leaders"]):
                    continue
                if r.get("confidence") != "confirmed":
                    held += 1
                    print(f"  held back ({r.get('confidence')}) {r['year']}: {name}"
                          f" - {person.get('how', '')[:70]}")
                    continue
                took = clean_date(person.get("took_office"))
                leader = {
                    "name": name,
                    "plaque_term": "",
                    "role": person.get("role", "president"),
                    "year_confidence": "confirmed",
                    "name_verified": True,
                    "missing_from_plaque": True,
                    "current": False,
                    "also_regent": bool(person.get("also_regent")),
                    "note": person.get("note", "").strip(),
                    "sources": [{"label": src["label"], "url": src["url"]}],
                }
                if person.get("acting"):
                    leader["acting"] = True
                y["leaders"].append(leader)
                added += 1
                print(f"  + {r['year']}: {name}"
                      + (f", took office {took}" if took else ""))

    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    n = sum(1 for y in data["years"] for l in y["leaders"] if l["role"] == "president")
    print(f"\nadded {added} presidents, held back {held} unconfirmed")
    print(f"{n} president terms now on record")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: merge_fillins.py FILE [FILE ...]")
    main(sys.argv[1:])
