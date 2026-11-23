# Photograph run, 23 November (fourth pass)

## Baseline reconfirmed

Unchanged from this morning's three earlier passes today: all four priority-1 presidents (Nick
Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) carry a portrait; every president and student
regent in the record has one; all 61 years carry at least one `years`-level photograph.
`scripts/build.py` and `scripts/check_data.py` both run clean (61 years, 1,964 events, 60
presidents, 1,111 legislation files). `scripts/portrait_gap.py --any-year` is unchanged: roughly
155-157 Senate/officer slots with no portrait in any year, almost all 2018-2026, concentrated in
Judicial Council, Senate secretary/parliamentarian seats and college senators.

## What this pass checked, independently of the three earlier today

Tried one angle not explicitly logged in today's first three passes: whether the *Talisman*'s
post-2003 magazine-format volumes for the exact years the standing gap covers (2018, 2019, 2020 —
"Grit," "Movement," "Paradise," "Balance," "Zeitgeist") might, this late in the run, carry a
student-organization section after all. Pulled the landing page and full table of contents for
the 2018 Spring volume ("Grit," `dlsc_ua_records/8684`) directly from digitalcommons. It is
twenty-three feature articles (profiles, recipes, horoscopes) with no organizations section of
any kind; neither "Student Government," "SGA," nor "student senate" appears anywhere on the page.

This reproduces, rather than extends, a conclusion this archive reached independently several
times before — most explicitly in the 10-11 October passes and 20 November's fourth pass, which
found the entire 2012-2025 magazine-era *Talisman* run lacks an organizations section and is
absent from the Wayback Machine as PDFs. Recorded here only so a future run does not spend time
re-opening a volume already checked today.

## No change to the record

`data/photos.json` and `data/photos/` are unchanged. This note is the only new file. The two
standing items are unchanged and still need a person, not another automated run:

1. `data/photo-finds/_for-the-editor.md` — 13 people, 14 entries, open since 8 September 2026,
   each a proved photograph whose tie to the named officeholder needs a yes/no editorial call.
2. The trigger cadence, now having fired at least four times today against a 155-person gap that
   every reachable source — Talisman (traditional and magazine-format), WKU Archives UA1C,
   digitalcommons Herald pages, wku.edu/news, wkuherald.com, and (when reachable) web.archive.org
   — has been checked against repeatedly without turning up anyone new.
