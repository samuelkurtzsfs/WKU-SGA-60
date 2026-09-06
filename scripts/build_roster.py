#!/usr/bin/env python3
"""Compile every recorded person-in-office into one roster.

Reads data/years.json and data/name-aliases.json and writes, into site/:

  roster.csv       one row per person-office-year holding
  roster-people.csv  one row per person, their whole service collapsed
  roster.json      the same, as data

Nothing here is research. It only gathers what years.json already records,
so every row carries the source the archive already holds for it. A person
who is not in years.json is not in the roster.
"""

import csv
import json
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")

# Rank offices so a person's most senior post can be named. Lower sorts higher.
RANK = [
    (r"^president$|student body president", 0),
    (r"student regent|^regent$", 1),
    (r"vice[- ]president|^vp$", 2),
    (r"speaker", 3),
    (r"chief justice", 3),
    (r"secretary|treasurer|chief of staff", 4),
    (r"justice", 5),
    (r"chair", 6),
]


def rank(office):
    o = (office or "").lower()
    for pat, r in RANK:
        if re.search(pat, o):
            return r
    return 7


def load():
    with open(os.path.join(ROOT, "data", "years.json")) as f:
        years = json.load(f)["years"]
    with open(os.path.join(ROOT, "data", "name-aliases.json")) as f:
        aliases = json.load(f)["aliases"]
    return years, aliases


def same_names():
    """Names the archive holds more than one person under.

    first_year, last_year and years_served read as one person's career, so a
    row for a shared name has to say that it is not one."""
    p = os.path.join(ROOT, "data", "same-name.json")
    if not os.path.exists(p):
        return {}
    with open(p) as f:
        return json.load(f).get("names", {})


def what_they_did(rec):
    """The archive's own account of this person's service, if it has one."""
    prof = rec.get("profile")
    if prof:
        return " ".join(p.strip() for p in prof)
    return (rec.get("note") or "").strip()


def src_of(rec):
    s = rec.get("src")
    if isinstance(s, dict):
        return s.get("label", ""), s.get("url", "")
    srcs = rec.get("sources")
    if srcs:
        return srcs[0].get("label", ""), srcs[0].get("url", "")
    return "", ""


def holdings(years, aliases):
    """Every person-office-year the archive records, flattened."""
    rows = []

    def add(rec, year, body, office, extra=None):
        name = (rec.get("name") or "").strip()
        if not name:
            return
        label, url = src_of(rec)
        row = {
            "person": aliases.get(name, name),
            "name_as_recorded": name,
            "year": year,
            "body": body,
            "office": office or "",
            "what_they_did": what_they_did(rec),
            "source": label,
            "source_url": url,
        }
        row.update(extra or {})
        rows.append(row)

    for y in years:
        yid = y["id"]
        org = y.get("organization") or {}

        for L in y.get("leaders", []):
            add(L, yid, "Leader", L.get("role", "president"), {
                "acting": "yes" if L.get("acting") else "",
                "also_regent": "yes" if L.get("also_regent") else "",
                "name_verified": "yes" if L.get("name_verified") else "no",
                "plaque_term": L.get("plaque_term", ""),
            })

        for e in org.get("executive", []):
            add(e, yid, "Executive", e.get("office"))

        senate = org.get("senate") or {}
        for o in senate.get("officers", []):
            add(o, yid, "Senate officer", o.get("office"))
        for m in senate.get("members", []):
            add(m, yid, "Senate", m.get("seat") or m.get("office") or "Senator")
        for c in senate.get("committees", []):
            if c.get("chair"):
                add({"name": c["chair"], "note": c.get("note", ""),
                     "src": c.get("src")},
                    yid, "Committee", "Chair, " + (c.get("name") or ""))

    return rows


def people(rows):
    """Collapse holdings into one record per person."""
    by = defaultdict(list)
    for r in rows:
        by[r["person"]].append(r)

    shared = same_names()
    out = []
    for person, rs in sorted(by.items()):
        yrs = sorted({r["year"] for r in rs})
        offices = []
        for r in sorted(rs, key=lambda r: (rank(r["office"]), r["year"])):
            tag = f'{r["office"]} ({r["year"]})'
            if tag not in offices:
                offices.append(tag)
        senior = min(rs, key=lambda r: (rank(r["office"]), r["year"]))
        told = [r["what_they_did"] for r in rs if r["what_they_did"]]
        variants = sorted({r["name_as_recorded"] for r in rs} - {person})
        out.append({
            "person": person,
            "also_recorded_as": "; ".join(variants),
            "first_year": yrs[0],
            "last_year": yrs[-1],
            "years_served": len(yrs),
            "years": "; ".join(yrs),
            "most_senior_office": senior["office"],
            "all_offices": "; ".join(offices),
            "what_they_did": " ".join(told),
            "sources": "; ".join(sorted({r["source"] for r in rs if r["source"]})),
            "same_name": "yes" if person in shared else "",
        })
    return out


def write_csv(path, rows, fields):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main():
    years, aliases = load()
    rows = holdings(years, aliases)
    ppl = people(rows)
    os.makedirs(OUT, exist_ok=True)

    write_csv(os.path.join(OUT, "roster.csv"), rows, [
        "person", "name_as_recorded", "year", "body", "office",
        "acting", "also_regent", "name_verified", "plaque_term",
        "what_they_did", "source", "source_url"])

    write_csv(os.path.join(OUT, "roster-people.csv"), ppl, [
        "person", "also_recorded_as", "first_year", "last_year",
        "years_served", "years", "most_senior_office", "all_offices",
        "what_they_did", "sources", "same_name"])

    with open(os.path.join(OUT, "roster.json"), "w") as f:
        json.dump({"holdings": rows, "people": ppl}, f, indent=1)

    described = sum(1 for r in rows if r["what_they_did"])
    print(f"  {len(rows)} recorded terms of office, held by {len(ppl)} people")
    print(f"  {described} of those terms ({100*described//len(rows)}%) carry an "
          f"account of what the person did")
    print(f"  {sum(1 for p in ppl if p['also_recorded_as'])} people are recorded "
          f"under more than one spelling or name")
    print("  -> site/roster.csv, site/roster-people.csv, site/roster.json")


if __name__ == "__main__":
    main()
