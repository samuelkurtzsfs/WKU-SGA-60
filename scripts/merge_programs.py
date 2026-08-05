#!/usr/bin/env python3
"""
Merge verified SGA/ASG programmes - concerts, speakers, films, festivals,
traditions and standing services - into data/years.json.

Input is a JSON array of programme objects, each carrying the academic year it
belongs to, a date, a `kind`, a title, a body and a source. They become ordinary
events in the year's chronology, distinguished only by the `kind` field, so one
merged dataset drives the year pages, the complete timeline and the programmes
page without any of them holding a second copy.

Usage: python3 scripts/merge_programs.py FILE [FILE ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YEARS = ROOT / "data" / "years.json"
KINDS = {"concert", "speaker", "film", "festival", "tradition",
         "service", "program", "other"}


def norm(t):
    """Titles match on their words, not their punctuation."""
    return re.sub(r"[^a-z0-9]+", " ", str(t).lower()).strip()


def clean_date(d):
    """The dating law: a year at minimum, and never more precision than we have.
    Returns a full ISO date, using the house convention that a day of 01 means
    the day is unknown and 01-01 means only the year is known."""
    s = str(d or "").strip()
    if not re.fullmatch(r"\d{4}(-\d{2})?(-\d{2})?", s):
        return None
    parts = s.split("-")
    y = parts[0]
    m = parts[1] if len(parts) > 1 else "01"
    day = parts[2] if len(parts) > 2 else "01"
    if not (1 <= int(m) <= 12) or not (1 <= int(day) <= 31):
        return None
    return f"{y}-{m}-{day}"


def main(paths):
    data = json.loads(YEARS.read_text())
    by_id = {y["id"]: y for y in data["years"]}
    seen = {yid: {norm(e["title"]) for e in y["events"]}
            for yid, y in by_id.items()}

    added = skipped = undated = unknown_year = dupe = badkind = 0
    per_year = {}

    for path in paths:
        for p in json.loads(Path(path).read_text()):
            y = by_id.get(p.get("year"))
            if not y:
                unknown_year += 1
                continue
            date = clean_date(p.get("date"))
            if not date:
                undated += 1
                continue
            kind = p.get("kind")
            if kind not in KINDS:
                badkind += 1
                continue
            key = norm(p.get("title"))
            if not key or key in seen[y["id"]]:
                dupe += 1
                continue
            src = p.get("src") or {}
            if not src.get("url") or not src.get("label"):
                skipped += 1
                continue
            ev = {"date": date, "title": p["title"].strip(), "body": p["body"].strip(),
                  "kind": kind}
            if p.get("money"):
                ev["money"] = p["money"].strip()
            ev["src"] = {"label": src["label"], "url": src["url"]}
            if src.get("pdf"):
                ev["src"]["pdf"] = src["pdf"]
            if src.get("file"):
                ev["src"]["file"] = src["file"]
            # some entries rest on two sources - an advance notice and the report,
            # or a Herald item and the yearbook. Both get cited.
            s2 = p.get("src2") or {}
            if s2.get("url") and s2.get("label"):
                ev["src2"] = {k: v for k, v in s2.items()
                              if k in ("label", "url", "pdf", "file")}
            y["events"].append(ev)
            seen[y["id"]].add(key)
            per_year[y["id"]] = per_year.get(y["id"], 0) + 1
            added += 1

    for y in by_id.values():
        n = len(y["events"])
        y["status"] = "researched" if n >= 3 else ("partial" if n else "empty")

    YEARS.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    print(f"merged {added} programmes into {len(per_year)} years")
    for bad, label in ((dupe, "already present"), (undated, "failed the dating law"),
                       (unknown_year, "unknown academic year"),
                       (badkind, "unrecognised kind"), (skipped, "no usable source")):
        if bad:
            print(f"  skipped {bad} {label}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: merge_programs.py FILE [FILE ...]")
    main(sys.argv[1:])
