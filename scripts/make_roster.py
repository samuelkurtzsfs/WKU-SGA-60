#!/usr/bin/env python3
"""Build the SGA people roster as an Excel workbook.

    python3 scripts/make_roster.py [-o SGA-60-roster.xlsx]

Reads data/years.json and writes one row per person per office per year,
plus an index of distinct people, a quarantine sheet for records the archive
cannot vouch for, and a coverage sheet saying plainly what is not in here.

Nothing is invented. Every row carries the source the archive holds for it,
and any row whose name had to be repaired is flagged and reproduced with its
original text so it can be checked against the source.
"""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "years.json"
ALIASES = ROOT / "data" / "name-aliases.json"

# Words that name an office, not a person. When one of these opens a name it
# means the office title bled into the name field during an earlier harvest.
OFFICE_WORDS = {
    "senator", "senators", "at-large", "at", "large", "chair", "chairperson",
    "chairman", "chairwoman", "speaker", "president", "vice", "justice",
    "secretary", "treasurer", "director", "staff", "committee", "college",
    "academy", "class", "senate", "student", "public", "engineering",
    "business", "well-being", "generation", "freedom", "fairness", "history",
    "alz", "affairs", "republicans", "democrats", "professor", "representative",
    "chief", "associate", "administrative", "executive", "international",
    "sophomore", "junior", "senior", "freshman", "graduate", "law", "relations",
    "gatton", "honors", "mahurin", "ogden", "cebs", "pcal", "gordon", "ford",
    "education", "behavioral", "sciences", "sciences,", "arts", "letters",
}

# Titles that are people-descriptions rather than SGA offices. A row whose
# name begins with one of these is probably not an officer at all.
NOT_AN_OFFICER = {"professor", "republicans", "democrats"}

SUFFIXES = {"jr", "jr.", "sr", "sr.", "ii", "iii", "iv", "v"}
PARTICLES = {"van", "von", "de", "del", "della", "di", "da", "la", "le",
             "mac", "mc", "st", "st.", "o'"}

# An office string that stops mid-phrase was cut off by the same harvest.
TRUNCATED_OFFICE = re.compile(r"\b(of|at|and|for|the|to|in|on|At-|Senator-at)$",
                              re.IGNORECASE)

NICK_QUOTED = re.compile(r'"([^"]+)"|“([^”]+)”')
NICK_PAREN = re.compile(r"\(([^)]+)\)")


ORDER = {"President": 0, "Student Regent": 1, "Unresolved": 2,
         "Executive officer": 3, "Senate officer": 4, "Senator": 5}


def load_aliases():
    if not ALIASES.is_file():
        return {}
    try:
        return json.loads(ALIASES.read_text()).get("aliases", {})
    except (json.JSONDecodeError, OSError):
        return {}


def strip_office_prefix(name):
    """Remove office words that bled onto the front of a name.

    Returns (cleaned, removed, is_suspect). Only strips when at least two
    plausible name tokens survive, so a real name is never eaten.
    """
    tokens = name.split()
    i = 0
    while i < len(tokens) and tokens[i].strip(",.").lower() in OFFICE_WORDS:
        i += 1
    if i == 0 or len(tokens) - i < 2:
        return name, "", False
    removed = " ".join(tokens[:i])
    suspect = tokens[0].strip(",.").lower() in NOT_AN_OFFICER
    return " ".join(tokens[i:]), removed, suspect


def split_name(name):
    """Split a recorded name into first / middle / last / suffix / nickname."""
    nickname = ""
    m = NICK_QUOTED.search(name)
    if m:
        nickname = (m.group(1) or m.group(2) or "").strip()
        name = NICK_QUOTED.sub(" ", name)
    m = NICK_PAREN.search(name)
    if m:
        nickname = nickname or m.group(1).strip()
        name = NICK_PAREN.sub(" ", name)
    name = " ".join(name.split())

    tokens = name.split()
    if not tokens:
        return "", "", "", "", nickname
    if len(tokens) == 1:
        return "", "", tokens[0], "", nickname

    suffix = ""
    if tokens[-1].strip(",").lower() in SUFFIXES and len(tokens) > 2:
        suffix = tokens[-1].strip(",")
        tokens = tokens[:-1]

    # A surname particle belongs with the surname, not the middle name.
    cut = len(tokens) - 1
    while cut > 1 and tokens[cut - 1].lower().strip(".") in PARTICLES:
        cut -= 1

    first = tokens[0]
    last = " ".join(tokens[cut:])
    middle = " ".join(tokens[1:cut])
    return first, middle, last, suffix, nickname


def src_of(obj):
    s = obj.get("src") or {}
    if isinstance(s, dict):
        return s.get("label", ""), s.get("url", "")
    return "", ""


def collect(years, aliases):
    """Every person-office-year the archive records. Returns (rows, quarantine)."""
    rows, bad = [], []

    for y in years:
        yid = y["id"]
        start = y.get("start", "")

        for l in y.get("leaders", []):
            role = l.get("role", "")
            if role == "president":
                office = "Student Body President"
                category = "President"
            elif role == "regent":
                office = "Student Regent"
                category = "Student Regent"
            else:
                office = "Not established"
                category = "Unresolved"
            if l.get("acting"):
                office = "Acting " + office
            also = bool(l.get("also_regent"))
            if also:
                office += " and Student Regent"
            labels = [s.get("label", "") for s in (l.get("sources") or [])]
            urls = [s.get("url", "") for s in (l.get("sources") or [])]
            rows.append({
                "year": yid, "start": start, "category": category,
                "office": office, "name": l["name"],
                "note": l.get("note", ""),
                "src": "; ".join(x for x in labels if x),
                "url": next((u for u in urls if u), ""),
                "verified": "yes" if l.get("name_verified") else "no",
                "confidence": l.get("year_confidence", ""),
                "plaque": l.get("plaque_term", ""),
                "profile": "yes" if l.get("profile") else "no",
                "regent": "yes" if (also or role == "regent") else "",
                "flag": "", "original": "",
            })

        org = y.get("organization") or {}
        senate = org.get("senate") or {}
        for lst, category in ((org.get("executive") or [], "Executive officer"),
                              (senate.get("officers") or [], "Senate officer"),
                              (senate.get("members") or [], "Senator")):
            for e in lst:
                raw = e.get("name", "")
                # senators carry `seat` (their constituency or committee)
                # where executive and Senate officers carry `office`
                office = (e.get("office") or e.get("seat") or "").strip()
                if category == "Senator" and office:
                    office = f"Senator, {office}"
                elif category == "Senator":
                    office = "Senator"
                clean, removed, not_officer = strip_office_prefix(raw)
                label, url = src_of(e)
                flags = []
                if removed:
                    flags.append(f'office text "{removed}" removed from the name')
                if TRUNCATED_OFFICE.search(office):
                    flags.append("office title is cut off mid-phrase")
                if not_officer:
                    flags.append("may not be an SGA officer at all")
                row = {
                    "year": yid, "start": start, "category": category,
                    "office": office, "name": clean,
                    "note": e.get("note", ""),
                    "src": label, "url": url,
                    "verified": "", "confidence": "", "plaque": "",
                    "profile": "yes" if e.get("profile") else "",
                    "regent": "",
                    "flag": "; ".join(flags),
                    "original": raw if removed else "",
                }
                (bad if flags else rows).append(row)

    # Second pass. The harvest also glued non-office words onto names, so
    # "Redz Coach Andi Dahmer" is Andi Dahmer with two words of prose in
    # front. Only trust this where the tail exactly matches a name the same
    # year already records cleanly, which makes it a match rather than a guess.
    clean_by_year = defaultdict(set)
    for r in rows + bad:
        if len(r["name"].split()) == 2:
            clean_by_year[r["year"]].add(r["name"])
    for r in rows + bad:
        tokens = r["name"].split()
        if len(tokens) < 3:
            continue
        tail = " ".join(tokens[-2:])
        if tail in clean_by_year[r["year"]]:
            r["original"] = r["original"] or r["name"]
            note = f'"{" ".join(tokens[:-2])}" removed from the name'
            r["flag"] = "; ".join(x for x in (r.get("flag"), note) if x)
            r["name"] = tail

    for r in rows + bad:
        first, middle, last, suffix, nick = split_name(r["name"])
        r.update(first=first, middle=middle, last=last, suffix=suffix, nick=nick)
        canon = aliases.get(r["name"], r["name"])
        r["person"] = aliases.get(canon, canon)

    rows, bad = dedupe(rows), dedupe(bad)

    # A quarantined row whose person, year and office already sit on the main
    # sheet is the same fact recorded worse. Drop it rather than have one
    # person appear twice in the workbook under two spellings.
    good = {(r["year"], norm_person(r), norm_office(r["office"])) for r in rows}
    keep = []
    for r in bad:
        if (r["year"], norm_person(r), norm_office(r["office"])) in good:
            for g in rows:
                if (g["year"], norm_person(g), norm_office(g["office"])) == \
                        (r["year"], norm_person(r), norm_office(r["office"])):
                    g["merged"] += 1 + r["merged"]
                    break
            continue
        keep.append(r)
    return rows, keep


# "SGA President", "WKU Student Body President" and "President" are one office.
STRIP_OFFICE = re.compile(
    r"\b(sga|wku|western|associated students|student body|the|of|for)\b",
    re.IGNORECASE)


def norm_office(office):
    o = STRIP_OFFICE.sub(" ", office or "")
    return re.sub(r"[^a-z0-9]+", " ", o.lower()).strip()


def norm_person(r):
    """Match on surname plus first initial, so Jim and James Haynes are one."""
    first = (r["first"] or "").lower()
    return (r["last"].lower(), first[:1])


def dedupe(rows):
    """Collapse the same person holding the same office in the same year.

    The 2016-2026 harvest recorded some people several times over, each with a
    different fragment of office text stuck to the front of the name. Andi
    Dahmer is in 2017-18 four times. Keep the fullest record of each and count
    what was folded in, rather than shipping one person as four.
    """
    best = {}
    order = []
    for r in rows:
        key = (r["year"], norm_person(r), norm_office(r["office"]))
        if key not in best:
            best[key] = r
            r["merged"] = 0
            order.append(key)
            continue
        kept = best[key]
        kept["merged"] += 1
        # A leader record is richer than an officer record of the same office:
        # it carries the verification, the plaque reading and the profile.
        score = lambda x: (ORDER.get(x["category"], 9) <= 2,
                           len(x.get("note") or ""), len(x.get("src") or ""),
                           -len(x["name"]))
        if score(r) > score(kept):
            r["merged"] = kept["merged"]
            best[key] = r
    return [best[k] for k in order]


HEAD = PatternFill("solid", fgColor="0B0B0C")
HEADF = Font(color="FFFFFF", bold=True, size=10)
WARN = PatternFill("solid", fgColor="FDECEC")


def sheet(wb, title, headers, data, widths, freeze="A2", fill=None):
    ws = wb.create_sheet(title)
    ws.append(headers)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill, cell.font = HEAD, HEADF
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    for row in data:
        ws.append(row)
    if fill:
        for r in range(2, ws.max_row + 1):
            for c in range(1, len(headers) + 1):
                ws.cell(row=r, column=c).fill = fill
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = freeze
    if ws.max_row > 1:
        ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{ws.max_row}"
    ws.row_dimensions[1].height = 30
    return ws


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default=str(ROOT / "SGA-60-roster.xlsx"))
    args = ap.parse_args()

    doc = json.loads(DATA.read_text())
    years = doc["years"]
    aliases = load_aliases()
    rows, bad = collect(years, aliases)

    key = lambda r: (str(r["start"]), ORDER.get(r["category"], 9),
                     r["last"].lower(), r["first"].lower())
    rows.sort(key=key)
    bad.sort(key=key)

    wb = Workbook()
    wb.remove(wb.active)

    cols = ["Last name", "First name", "Middle", "Suffix", "Known as",
            "Full name as recorded", "Academic year", "Year began", "Category",
            "Office held", "Held the regent seat", "Name verified",
            "Year confidence", "Plaque reads", "Has a profile",
            "What the archive says", "Source", "Source link"]
    widths = [18, 15, 12, 7, 12, 26, 13, 11, 17, 34, 15, 12, 14, 12, 12, 60,
              34, 46]

    def to_row(r):
        return [r["last"], r["first"], r["middle"], r["suffix"], r["nick"],
                r["name"], r["year"], r["start"], r["category"], r["office"],
                r["regent"], r["verified"], r["confidence"], r["plaque"],
                r["profile"], r["note"], r["src"], r["url"]]

    sheet(wb, "Every office held", cols, [to_row(r) for r in rows], widths)

    # one row per person, however many offices they held
    people = defaultdict(list)
    for r in rows:
        people[r["person"]].append(r)
    idx = []
    for person, rs in people.items():
        rs.sort(key=lambda r: str(r["start"]))
        best = min(rs, key=lambda r: ORDER.get(r["category"], 9))
        yrs = sorted({r["year"] for r in rs})
        offices = []
        for r in rs:
            o = f'{r["office"]} ({r["year"]})'
            if o not in offices:
                offices.append(o)
        idx.append([best["last"], best["first"], best["nick"], person,
                    len(yrs), yrs[0], yrs[-1], "; ".join(yrs),
                    best["category"], "; ".join(offices)])
    idx.sort(key=lambda r: (r[0].lower(), r[1].lower()))
    sheet(wb, "People", ["Last name", "First name", "Known as",
                         "Name used by the archive", "Years served",
                         "First year", "Last year", "Every year",
                         "Highest office", "Every office held"],
          idx, [18, 15, 12, 26, 12, 11, 11, 34, 17, 72])

    badcols = cols[:10] + ["Original text in the file", "What is wrong with it",
                           "Source", "Source link"]
    sheet(wb, "Needs checking",
          badcols,
          [[r["last"], r["first"], r["middle"], r["suffix"], r["nick"],
            r["name"], r["year"], r["start"], r["category"], r["office"],
            r["original"], r["flag"], r["src"], r["url"]] for r in bad],
          widths[:10] + [30, 46, 34, 46], fill=WARN)

    n_pres = len({r["person"] for r in rows if r["category"] == "President"})
    n_reg = len({r["person"] for r in rows if r["regent"] == "yes"})
    n_exec = sum(1 for r in rows if r["category"] == "Executive officer")
    n_so = sum(1 for r in rows if r["category"] == "Senate officer")
    n_sen = sum(1 for r in rows if r["category"] == "Senator")
    yrs_sen = sorted({r["year"] for r in rows if r["category"] == "Senator"})
    missing_sen = [y["id"] for y in years if y["id"] not in yrs_sen]
    per_year = defaultdict(int)
    for r in rows:
        if r["category"] == "Senator":
            per_year[r["year"]] += 1
    thin = sorted(per_year.items(), key=lambda kv: kv[1])[:5]

    notes = [
        ["What this is",
         "Every person the SGA 60 archive records as holding an office in "
         "student government, 1966-67 to 2026-27. One row per person per "
         "office per year, so somebody who served three years appears three "
         "times. The People sheet has one row each instead."],
        ["Where it comes from",
         "data/years.json in the SGA 60 archive. Regenerate this file with "
         "python3 scripts/make_roster.py after any research lands."],
        ["", ""],
        ["Distinct people who were student body president", n_pres],
        ["Distinct people who held the student regent seat", n_reg],
        ["Executive officer rows (one per person per year)", n_exec],
        ["Senate officer rows (Speaker, clerks, committee chairs)", n_so],
        ["Rank and file senator rows", n_sen],
        ["Distinct people in this workbook", len(people)],
        ["Rows in total on the main sheet", len(rows)],
        ["Rows on the Needs checking sheet", len(bad)],
        ["", ""],
        ["How complete the Senate roll is",
         (f"Senators are recorded for {len(yrs_sen)} of {len(years)} academic "
          f"years. The years with none at all are "
          f"{', '.join(missing_sen) if missing_sen else 'none'}. Even a year "
          "that has senators is very unlikely to have all of them: the roll "
          "was rebuilt from whichever minutes and rosters survive, and a "
          "meeting nobody minuted leaves no trace. Treat a year's count as a "
          "floor, not a total. The thinnest years here are "
          + ", ".join(f"{y} ({n})" for y, n in thin) + "."
          if yrs_sen else
          "No rank and file senator is recorded. Every name here held an "
          "executive office, a Senate office such as Speaker, or the "
          "presidency.")],
        ["", ""],
        ["Why some rows are quarantined",
         "The Needs checking sheet holds rows whose name or office was "
         "damaged before it reached the archive: an office title glued to the "
         "front of a name, an office cut off mid-phrase, or an entry that "
         "looks like it is not an SGA officer at all. They are kept out of "
         "the main sheet so nothing misleading is circulated, and kept in the "
         "workbook so the work is not lost. Each shows its original text."],
        ["Names",
         "Where the archive holds several spellings for one person, the "
         "People sheet uses the settled one from data/name-aliases.json. The "
         "Every office held sheet keeps each source's own spelling, which is "
         "why a name there may differ."],
        ["Empty cells",
         "An empty cell means the archive holds nothing for that field. It "
         "does not mean the thing is untrue. A thin record is a thin record, "
         "not a quiet year."],
    ]
    ws = sheet(wb, "Read me first", ["", ""], notes, [46, 104], freeze="A1")
    for r in range(1, ws.max_row + 1):
        ws.cell(row=r, column=1).font = Font(bold=True, size=10)
        ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True,
                                                       vertical="top")
    wb.move_sheet("Read me first", offset=-4)

    wb.save(args.out)
    print(f"wrote {args.out}")
    print(f"  {len(rows)} office-year rows, {len(people)} distinct people")
    print(f"  {n_pres} presidents, {n_reg} regents, {n_exec} executive, "
          f"{n_so} senate officers, {n_sen} senators")
    print(f"  {len(bad)} rows quarantined for checking")


if __name__ == "__main__":
    main()
