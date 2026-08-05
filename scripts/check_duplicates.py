#!/usr/bin/env python3
"""
Report events in the same year that look like the same event written twice.

Successive research passes have described one event in two sets of words, and a
deduplicator that matches whole titles never sees it. This compares the words in
the titles instead, and flags close pairs for an editor to judge. It changes
nothing: same-day legislative business is genuinely several events, so the call
has to be made by someone reading both.

Run it after any merge. Exit status is 1 when anything is flagged, so it can
gate a build.

Usage: python3 scripts/check_duplicates.py [--json OUT]
"""
import itertools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STOP = {"the", "a", "an", "of", "for", "and", "to", "in", "on", "at", "is",
        "its", "with", "as", "by", "after", "over"}


def words(t):
    return set(re.sub(r"[^a-z0-9 ]", " ", str(t).lower()).split()) - STOP


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
    if "--json" in argv:
        dest = Path(argv[argv.index("--json") + 1])
        dest.write_text(json.dumps(pairs, ensure_ascii=False, indent=1) + "\n")
        print(f"wrote {len(pairs)} candidate pairs to {dest}")
    else:
        for p in pairs:
            print(f'{p["year"]}  similarity {p["similarity"]}')
            print(f'   {p["a"]["date"]}  {p["a"]["title"]}')
            print(f'   {p["b"]["date"]}  {p["b"]["title"]}')
        print(f"\n{len(pairs)} pairs to judge. Same-day bills and votes are "
              f"usually separate events; read both before merging.")
    return 1 if pairs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
