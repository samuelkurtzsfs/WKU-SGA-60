# What to paste into Claude Code

Work one decade at a time. Do not hand it the whole sixty years.

---

## Prompt 1 — the four open pairs (do this first, it is short)

```
Read CLAUDE.md and RESEARCH.md first.

Four leader entries in data/years.json still have role "unresolved". Resolve them:
  1968-69  Reed Morgan
  1970-71  John Lyne and Larry Zielke
  1982-83  David Payne

We already know the student regent was a separately elected office from April 1968,
so in each pair one is president and one is regent.

For each name, search TopSCHOLAR through Google using site:digitalcommons.wku.edu with the
name in quotes, plus these terms: "student government association", "associated student
government", "student government", SGA, ASG, "student regent". Also check
site:digitalcommons.wku.edu/wku_timeline. April and May issues of the College Heights
Herald carry election results every year — that is where the answer will be.

Set role to "president" or "regent", set year_confidence to "confirmed" only when a source
says so outright, write what you found into note, and add the source to the year's events
array. If you cannot confirm one, leave it unresolved and say so.

Then run: python3 scripts/build.py
Report what you confirmed, what you could not, and every source URL you used.
```

---

## Prompt 2 — a decade sweep (repeat, changing the years)

```
Read CLAUDE.md and RESEARCH.md first.

Work only on 1966-67 through 1975-76 in data/years.json. For each year, in this order:

STEP 1 — verify the names. Search each leader's name on TopSCHOLAR with the SGA keyword set.
If the archive consistently places them in a different year than the plaque says, move the
leader object to the correct year, set year_confidence to "corrected", and record the old
plaque reading in the note. Never silently change a year.

STEP 2 — sweep the year. Search each of these against BOTH calendar years of the academic
year: "student government association", "associated student government", "student
government", SGA, ASG, "student regent". Use site:digitalcommons.wku.edu on Google.
Also search site:digitalcommons.wku.edu/wku_timeline.

STEP 3 — log everything SGA did that year, not only what the president did. Resolutions,
elections, turnout numbers, budgets, committees, appointments, fights, failures, editorials
attacking it. Aim for 4 to 8 events per year where the material exists.

Format each event exactly like the ones already in the file, with date as YYYY-MM-DD and a
src object containing label and url. Every event needs a source. Never invent one.

Then run: python3 scripts/build.py

Report per year: how many events you added, which names you confirmed or moved, and
anything you could not verify. Do not commit anything.
```

Then swap the years and run it again:
`1976-77 through 1985-86` → `1986-87 through 1995-96` → `1996-97 through 2005-06` →
`2006-07 through 2015-16` → `2016-17 through 2026-27`

---

## Prompt 3 — when you want it pushed

```
Run python3 scripts/build.py, then commit and push to main with a message describing
which years changed.
```

Vercel picks it up and the site is live about a minute later.

---

## Check its work before you push

Spot-check three events per decade by opening the source URL. You are looking for two
failure modes: a source URL that does not contain the claim, and an event that reads
plausibly but has no source at all. Both are recoverable if you catch them in the first
decade and expensive if you catch them in the sixth.
