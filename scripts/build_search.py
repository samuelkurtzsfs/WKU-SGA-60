#!/usr/bin/env python3
"""Build the search index the site's search page loads.

Everything on the site that a reader might look for: the people, the years,
the dated entries, and the legislation. It is deliberately small. The full
roster is three and a half megabytes and nobody should download that to look
up a name, so each record here keeps only what a result needs to show, and the
searchable text is folded to lowercase once at build time rather than on every
keystroke in the browser.

Written by build.py; not run on its own.
"""

import json
import re
import unicodedata


def fold(s):
    """Lowercase, accents removed, so a search for Donte finds Donté."""
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower()).strip()


def slugify(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def build(years, roster_people, leg, aliases):
    """Return the index as a list of records, smallest useful shape.

    k = kind, t = title, s = subtitle, u = url, x = the text searched
    """
    out = []

    # ---- people
    for p in roster_people:
        name = p.get("person", "")
        if not name:
            continue
        offices = p.get("all_offices", "")
        # one person can hold a dozen posts; the subtitle only needs the top
        alts = p.get("also_recorded_as", "")
        years_txt = p.get("years", "")
        sub = p.get("most_senior_office", "") or "Served in student government"
        if years_txt:
            sub = f"{sub} · {years_txt}"
        out.append({
            "k": "person", "t": name, "s": sub[:120],
            "u": f"o/{slugify(name)}.html",
            "x": fold(" ".join([name, alts, offices[:220], years_txt])),
        })

    # ---- academic years
    for y in years:
        leaders = [l["name"] for l in y.get("leaders", [])]
        sub = ", ".join(leaders) if leaders else "no leader recorded"
        n = len(y.get("events", []))
        out.append({
            "k": "year", "t": y["id"], "s": f"{sub} · {n} entries",
            "u": f"y/{y['id']}.html",
            "x": fold(" ".join([y["id"], y.get("org", "")] + leaders)),
        })

    # ---- dated entries
    for y in years:
        for e in y.get("events", []):
            title = e.get("title", "")
            if not title:
                continue
            out.append({
                "k": "entry", "t": title[:150],
                "s": f"{e.get('date','')} · {y['id']}",
                "u": f"y/{y['id']}.html",
                # the opening of the body is enough to find an entry by;
                # indexing all of it doubled the file for very little reach
                "x": fold(" ".join([title, e.get("body", "")[:110],
                                    e.get("date", ""), y["id"]])),
            })

    # ---- legislation
    for item in (leg or []):
        title = item.get("title", "")
        if not title:
            continue
        out.append({
            "k": "legislation", "t": title[:150],
            "s": f"{item.get('type','')} · {item.get('session','')}".strip(" ·"),
            "u": "legislation.html",
            "x": fold(" ".join([title, item.get("type", ""),
                                item.get("session", "")])),
        })

    return out
