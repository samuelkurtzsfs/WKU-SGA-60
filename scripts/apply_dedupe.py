#!/usr/bin/env python3
"""
Apply an editor's duplicate rulings to data/years.json.

Each ruling covers one candidate pair: `distinct` leaves both entries alone,
`merge` replaces the two with a single entry that carries every sourced fact
either of them had. Titles are matched exactly, and a ruling whose titles are
not both present is reported rather than guessed at, so a stale ruling can
never delete the wrong entry.

Usage: python3 scripts/apply_dedupe.py .research/deduped-*.json
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEEP_SRC = ("label", "url", "pdf", "file")


def clean_src(s):
    return {k: v for k, v in (s or {}).items() if k in KEEP_SRC and v}


def main(paths):
    path = ROOT / "data" / "years.json"
    data = json.loads(path.read_text())
    by_id = {y["id"]: y for y in data["years"]}

    merged = distinct = missed = bad = 0
    for p in paths:
        for r in json.loads(Path(p).read_text()):
            if r.get("decision") != "merge":
                distinct += 1
                continue
            y = by_id.get(r.get("year"))
            if not y:
                missed += 1
                print(f"  ! unknown year {r.get('year')}")
                continue
            titles = [t.strip() for t in r.get("remove", [])]
            found = [e for e in y["events"] if e["title"].strip() in titles]
            if len(found) < 2:
                missed += 1
                print(f"  ! {r['year']}: only {len(found)} of "
                      f"{len(titles)} titles still present, left alone")
                continue
            ent = r.get("entry") or {}
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(ent.get("date", ""))) \
                    or not (ent.get("src") or {}).get("url"):
                bad += 1
                print(f"  ! {r['year']}: merged entry has no usable date or "
                      f"source, left alone")
                continue
            new = {"date": ent["date"], "title": ent["title"].strip(),
                   "body": ent["body"].strip()}
            for k in ("kind", "money"):
                if ent.get(k):
                    new[k] = ent[k]
            if ent.get("campus") or any(e.get("campus") for e in found):
                new["campus"] = True
            new["src"] = clean_src(ent["src"])
            if clean_src(ent.get("src2")).get("url"):
                new["src2"] = clean_src(ent["src2"])
            y["events"] = [e for e in y["events"] if e["title"].strip() not in titles]
            y["events"].append(new)
            merged += 1

    for y in data["years"]:
        n = len(y["events"])
        y["status"] = "researched" if n >= 3 else ("partial" if n else "empty")

    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    total = sum(len(y["events"]) for y in data["years"])
    print(f"merged {merged} pairs into one entry each, left {distinct} pairs "
          f"as distinct events")
    if missed or bad:
        print(f"  {missed} rulings skipped as stale, {bad} as unusable")
    print(f"{total} events remain")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: apply_dedupe.py FILE [FILE ...]")
    main(sys.argv[1:])
