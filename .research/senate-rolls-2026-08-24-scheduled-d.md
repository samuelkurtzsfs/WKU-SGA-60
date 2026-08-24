# Senate rolls, 24 August 2026 (scheduled run): twenty-three names for 2024-25

Scheduled run on `research-senate`. The branch on origin had already been fully merged
into `main` (0 commits ahead, 7 behind), so it was recreated from current `main` and
pushed to sync the pointer before any new work.

## The stored prompt describes a stale backlog

This routine's stored prompt states "The archive currently records ZERO rank and file
senate members" and directs the run to reconcile `.research/senators-unverified.json`
(105 names) before starting. Neither is true any more. As of this run, 57 of 61
academic years carry `organization.senate.members` (1,442 members before this run's
additions), and `.research/senators-unverified.json` is `[]` and has been for several
runs — confirmed, not re-litigated, per the standing note in `SGA-60-AGENT-INFO.md`
§8 that this file, not the stored prompt, is the live backlog. Whoever owns this
project's scheduled Routines should point the trigger at that file instead of a frozen
description of the project's state from before the senate-rolls work began in earnest.

## Step 1: reconcile `senators-unverified.json`

Already `[]`. Confirmed, not re-litigated.

## Step 2: the oldest unworked year

Only four years carry no `organization.senate.members`: 1966-67, 1969-70, 1979-80 and
2026-27 (the year in progress, not applicable). The first three are documented,
re-confirmed-multiple-times-over-four-separate-runs (20/21/22/23 August) permanent dead
ends — no SGA minutes reach that era on TopSCHOLAR, and the one Talisman year
`archive.org` holds nearby (1971-72) profiles officers, not the body. Not re-attempted
this run; re-litigating an exhaustively documented negative on the same evidence every
run is exactly the failure mode `SGA-60-AGENT-INFO.md` §6.7 warns about.

Followed the standing recommendation left by the three 23 August passes: moved to a
thin post-2003 year with real headroom. Checked current member counts across all 57
years-with-a-roll and picked **2024-25** — 11 members going in, the single thinnest
year on file, with SGA's own Senate minutes hosted directly on `wku.edu`
(`/sga/2024_2025_legislative/senate_minutes/senate_minutes_M_D_YY.docx`), not
`digitalcommons.wku.edu`, so none of that host's pacing/WAF issues apply.

## What this run added

The directory listing at that path 403s (the same block already documented for the
2010-14 uploads path), but individual files are directly fetchable by guessed date.
Eleven citations already on record gave the exact filenames for six meetings; the rest
were found by generating every plausible Tuesday meeting date across the 2024-25
academic year and probing each with a paced, single-threaded `curl` (a browser
User-Agent, no other special headers needed — this host does not WAF-challenge the way
`digitalcommons.wku.edu`'s `viewcontent.cgi` does). Two connection resets during the
probe were retried individually rather than treated as a wall. Seventeen distinct
meetings were recovered, 10 September 2024 through 15 April 2025 — not the complete
year (a handful of guessed dates came back 404, most plausibly weeks with no meeting
or a filename this run didn't guess), but a good working majority of it. `.docx` files
were converted to plain text locally (no `antiword`/`catdoc` needed — a direct
`zipfile` read of `word/document.xml` with the tags stripped) and read start to finish.

A researcher subagent drafted 21 candidates from these 17 meetings' AUTHORS blocks
(SGA's own convention of naming each bill's author with their seat title, which this
project already treats as adequate Senate-membership evidence for the 11 pre-existing
members), plus a handful of nomination/confirmation/swearing-in votes. It explicitly
flagged two as weaker (Caroline Yates, Malick Ibrahim) rather than asserting them at
the same confidence as the rest.

A separate adversarial verifier subagent, given only the raw primary-source text (not
the researcher's paraphrase), independently re-derived every one of the 21 claims,
quoting the actual AUTHORS-block line it found for each. Verdict: **19 accept, 2 trim,
0 reject.** Both trims strengthened rather than weakened the case — the verifier found
corroborating evidence sitting in `years.json`'s own already-cited Herald sourcing that
the researcher, working only from the 17 minutes files, had not seen:

- **Caroline Yates.** The draft's own "weaker evidence" framing held up; the verifier
  found a fourth independent "Senator Yates" floor address the researcher missed, and
  noticed that a non-senator bill author in the same minutes (Kiersten Washington) is
  *never* addressed as "Senator" despite authoring two resolutions — supporting that
  "Senator" in these minutes tracks a real seat, not a courtesy title. An already-cited
  Herald article in `years.json`'s 2025-26 events independently calls her "Senator
  Caroline Yates" as a continuing member the following year.
- **Malick Ibrahim.** The draft over-stated how long "Senator Ibrahim" persisted in
  absence lists (through 4 March 2025); the verifier found no such appearance after 29
  October 2024. The reason surfaced from `years.json` itself: an already-cited 6/7
  November 2024 Herald article reports the Judicial Council removed "Senators Malick
  Ibrahim, Myricle Gholston and Karisha Petty" from their seats that week for excessive
  unexcused absences, naming Ibrahim "Senator Malick Ibrahim" directly — stronger,
  independent evidence than anything the 17 minutes files offered on their own, and it
  explains the disappearance the draft had mis-dated.

That same already-cited censure article names two more sitting senators the 17-file
sweep never surfaced on its own — **Myricle Gholston** and **Karisha Petty** — both
independently confirmed by name as "Senator" in a source already in the archive. Added
alongside the 21, sourced to that article rather than to the minutes.

**23 names merged, `2024-25` now carries 34 senate members, up from 11** — exactly
matching the year's own recorded Senate size. `build.py` and `check_data.py` pass
clean. `check_duplicates.py` still reports only the same six pre-existing pairs from
earlier decades; nothing in this run's additions.

## What's left

- **1966-67, 1969-70, 1979-80** remain settled permanent gaps — do not re-search
  without a genuinely new access route (see `senate-rolls-gap-years-2026-08-20.md`).
- **1999-00** has one member and one officer, from a dedicated piecemeal Herald sweep
  (23 August). Its own notes flag a borderline Billy Lyons mention worth a second look
  and room for a wider date-range sweep if a future run wants to spend the time.
- **2024-25 is not fully swept.** Only 17 of the year's meetings were read; a handful
  of guessed dates 404'd and a future pass could try adjacent days, or pull the
  complete list of filenames from wherever SGA's own site links them (not found this
  run — unlike the 2016-17-era `legislative/minutes.php` page, no index page for the
  `2024_2025_legislative` path was located; every file here was reached by guessing).
  Absence lists also name several bare surnames this run deliberately left out —
  Diltz, Gholston (now added under her full first name from the censure article),
  Norman, Petty (now added the same way), Young — most already resolved or dead ends,
  but worth a second pass against any new full-name source.
- The wku.edu-direct-minutes method (paced date-guessing, no WAF) generalizes cleanly
  to the next-thinnest years: 2019-20 (14), 2020-21/2021-22 (17 each), 2010-11/2011-12/
  2017-18/2023-24 (18 each) are the next candidates in roughly that order.
