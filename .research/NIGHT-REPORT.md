# Night report - 4 August 2026

Written by the overnight editor at 5:20 AM.

## The headline
All 61 years, 1966-67 through 2026-27, are researched and live. 650 dated events,
68 leader profiles, 23 verified portraits, 14 primary documents
readable on the site, 381 legislation files. Every event carries a dated, cited source.

## What the night produced
- The modern era (2000-2027): fully researched and 100% fact-checked, every event
  verified against its source page.
- The pre-2000 era: all 32 target years researched from the indexed Herald archive
  and verified; the founding era rebuilt on primary documents including the 1968
  election results memo (Straeffer 1,732 - Whitley 1,098).
- Plaque disputes resolved: Zielke's term corrected to 1969-70 (the plaque conflated
  two terms), Hargroave confirmed as Hargrove, Payne/Bush 1982 succession untangled,
  Linda Jones and William Menser confirmed. Reed Morgan honestly left unresolved -
  the only archival Morgan is a different 1966 role, and identities are not merged
  without proof.
- Sensitive history handled to standard: the 2016 racism complaints and resignations,
  the 2004 Todd impeachment bid, the Watkins resignation - all reported strictly to
  what the cited sources printed.
- Primary documents mirrored: senate and cabinet minutes, Board of Regents minutes,
  two SGA constitutions.

## What verification cut
Roughly 55 items died in fact-checking across the night - events and profile
paragraphs whose cited page did not support the claim. They are logged in the
workflow journals; none reached the site or all were removed on verdict.

## Still thin
1974-75 (3 events) - a dedicated researcher and fact-checker are on it as this
report is written. Kayla Shelton's 2009-10 plate remains flagged as unverified
against the digitised Herald.

## For Sam
1. Rotate the GH_TOKEN (it passed through chat once; regenerate on GitHub, update
   the environment variable).
2. The Talisman portrait hunt continues hourly - faces for the 70s-90s presidents
   are the main remaining gap.
3. Consider the testimony project (RESEARCH.md part C) - the archive work is done
   enough to start calling alumni.

---

# Night report - 18 August 2026

Written by the overnight editor at 5:00 AM.

## The headline
The three pull requests that had been open since 4 August are closed. None of them
could be merged, and the reason is structural rather than editorial: `main` was
rebuilt on a new root commit after 4 August, so it shares **no common ancestor**
with any research branch. Git reports them as "50 behind"; in fact they are
unrelated histories. Merging one would not have added anything - it would have
restored the 4 August snapshot over the current record, cutting `data/years.json`
from 1,877 events to roughly 830 and deleting `herald-index-full.json`, the
legislation authorship index, the name aliases, the whole contributor layer and
all three validator scripts.

Everything on the three branches worth keeping has been lifted onto `main` instead.

## What was merged
Three additions and one cut, each checked against its source before publication.

- **29 September 1983** - an ASG group formed to study the grade scale, with
  president Jack Smith writing that ASG backed the Herald's opinion. Both items
  appear in the TopSCHOLAR record for Herald 59:11.
- **23 October 1986** - a bill to make the athletic fee optional defeated, and a
  top ASG race decided by eight votes. Both in the record for Herald 62:17.
- **Senate minutes, 8 November 2022** - re-downloaded from wku.edu and byte-for-byte
  identical to the branch copy, so the mirror is authentic. This gives 2022-23 its
  first document.
- **Cut:** the adviser change of 7 July 2026 had been written up twice in 2025-26
  from the same Herald report. The fuller entry is kept and carries every fact the
  other had.

## What was cut and why
One entry would have put an invented fact on the live site. "Robinson reappoints
Jenkins chief communications officer", dated 22 April 2025, cites a Herald article
that is about a student-painted mural announced at the meeting of 19 August. There
is no reappointment in it, no April date, and no confirmation vote. The date, the
framing and the vote were all unsupported by the source cited for them.

Smaller cuts: a committee-chairs entry that said "five" and then listed six (the
Herald names six, and `main` already had it right); four entries duplicating
meetings `main` already covers from the same articles; and a charity awareness-day
proclamation, which the rules exclude by name. Two 1985 items had been filed under
1985-86 though February and March 1985 fall in 1984-85.

## What held up
Spot checks were run against thirteen sources. The four most recent 2026 items -
the ODK award, the proposed tuition increase, the Regents' vote and the adviser
change - all hold up, and `main` already carried all four, filed in 2025-26, which
is the right academic year. Rush Robinson, not Lucas, cast the lone no vote against
the tuition increase, and the record says so.

On the photographs branch, five portrait entries that looked unique were the same
image files `main` already holds under the settled spellings. The sixth, Sandra
Norfleet, is filed on the branch under 1982-83 and on `main` under 1981-82.
**`main` is right**, on the strength of the Herald of 15 April 1982, "Student
Regent's 2-Month Term Nears End". Section 7 of the handoff still reads 1982-83 and
is now the stale copy.

## A warning about the local index
`data/herald-index-full.json` cannot be used to rule a headline out. The harvester
stores each issue description in 300-character chunks and many records stop
mid-headline. Every one of the 1983, 1985 and 1986 headlines confirmed live this
morning was missing from the local copy. Grep it to find candidates; open the
record page to confirm. Record URLs also 301 unless requested with a trailing slash.

## Where the record stands
61 years, 1,878 dated events, 60 people who have been president, 34 documents,
390 legislation files. `build.py`, `check_data.py` and `check_contrib.py` all clean.
`check_duplicates.py` reports six pairs; all six are genuinely separate events -
different dates, or same-day bills, which stay apart.

## Still open
- Four leaders have no portrait: Nick Todd and Katie Dawson (2004-05), Jeanne
  Johnson (2006-07), Reagan Gilley (2008-09).
- The 8 November 2022 minutes are mirrored but not read. No PDF text extractor
  works in this environment - PyMuPDF is absent and pypdf fails on its crypto
  import - so the summary is deliberately plain. Worth expanding.
- The research routines are still starting from the orphaned branches. Until they
  branch from `origin/main`, every run will produce work that cannot be landed.
