# Senate rolls, 23 August 2026 (scheduled run, third pass): nine names for 2016-17

Scheduled run on `research-senate`. The branch on origin had already been
fully merged into `main` again (0 commits ahead, 7 behind) since the second
pass earlier the same day (which opened 1999-00), so it was recreated from
current `main` and pushed to sync the pointer before any new work.

## Step 1: reconcile `.research/senators-unverified.json`

The file does not exist in the repository — already reconciled by an earlier
run. Confirmed, not re-litigated. Went straight to step 2.

## Step 2: pick the oldest unworked year

Checked every year in `data/years.json` for an empty
`organization.senate.members`. Only four qualify: 1966-67, 1969-70, 1979-80
and 2026-27 (the year in progress, not applicable). 1971-72 and 1999-00, both
listed as gaps in earlier notes, have since been filled (38 and 2 members
respectively) by other passes today. The remaining three are documented,
re-confirmed-multiple-times permanent dead ends (no minutes reach that era on
TopSCHOLAR, and the Talisman years archive.org holds for that range profile
officers, not the body).

With the literal "zero members" years exhausted, followed the standing
recommendation left by this morning's two passes
(`senate-rolls-2026-08-23-scheduled.md`, `-scheduled-b.md`): move to a thin
post-2003 year with real headroom. Checked current member counts across all
57 years-with-a-roll; picked **2016-17** (10 members going in) — SGA's own
Senate minutes for that year are hosted directly on `wku.edu`, not
`digitalcommons.wku.edu`, so none of that host's pacing/WAF issues apply.

## What this run added

A researcher subagent pulled all 22 distinct 2016-17 Senate meeting minutes
from `wku.edu/sga/legislative/leg_minutes_2016_17/` (indexed at
`/sga/legislative/minutes.php`) and read every roll-call, swearing-in and
appointment passage, cross-checking names already on record (executive,
senate officers, senate members, and `data/name-aliases.json`) before
drafting anything.

Nine survived a separate adversarial verifier subagent, which independently
re-fetched all five cited minutes PDFs and the one cited Herald article
(fresh, not trusting the researcher's transcription) and tried to refute each
claim against this project's known traps (chair ≠ member, author ≠
member, ambiguous appointment). Verdict: **9 accept, 0 trim, 0 reject.**

- **Fransisco Serrano**, Senator — sworn in 27 Sep 2016.
- **Desherra Bronston**, Senator at Large — sworn in 11 Oct 2016 alongside
  Helen Vickrey's committee-chair appointment.
- **Asha Wasuge**, **Kenan Mujkanovic**, **Flavio Chavarri**, **Blake
  Bowden** — four of a nine-person at-large swearing-in batch on 31 Jan
  2017 (the other five — Andrea Ambam, Shantel Pettway, Will Hurst,
  Hizareth Linares, Lily Nellans — were already on record, Nellans under
  a name variant the minutes themselves also use, "Lillian Nellan").
- **Sara Saeed**, Senator at Large — sworn in 7 Feb 2017.
- **Olga Shoyat**, Senator at Large — sworn in 21 Feb 2017 to fill Chase
  Coffey's seat after his resignation; appointed by Executive Vice President
  Kate Hart, not President Richey — corrected in the note field.
- **Lucas Knight**, Senator At-Large — appointed September 2016 to close
  a one-seat shortfall left by the spring 2016 at-large election. Already
  narrated in Nathan Cherry's profile text and already a recorded senator for
  2014-15 and 2015-16, but never had his own structured 2016-17 membership
  entry until now.

2016-17 now has 19 members, up from 10. `build.py`, `check_data.py` and
`check_duplicates.py` all pass clean; the same six known duplicate pairs are
unchanged.

Two spelling splits flagged, not resolved, per project rule: the Senate's own
minutes spell one senator both "Fransisco" and "Francisco" Serrano across
different meetings (years.json's existing prose already uses "Francisco");
and one senator both "Mujkanovic" (31 Jan 2017 minutes) and "Mujcanovic" (21
Feb 2017 minutes).

One WKU server anomaly found, not acted on: `smm_10_18_16.pdf` on
`wku.edu/sga/legislative/leg_minutes_2016_17/` is byte-for-byte identical to
`smm_10_25_16.pdf` — the true 18 October 2016 minutes were never located;
WKU's own site appears to have uploaded the 25 October file twice under two
names.

## What's left

- **1966-67, 1969-70, 1979-80** remain settled permanent gaps.
- **1999-00** was opened this morning by a separate pass on this same branch
  (one member, one officer) and could still use more piecemeal Herald work;
  not touched further this run.
- The `wku.edu/sga/legislative/*minutes.php` route (own-minutes, no pacing,
  full roll-call/swearing-in language) is confirmed to work cleanly at least
  for 2016-17 and should generalize to any other post-2009 year still under
  20 members — 2024-25 (11), 2019-20 (14), 2021-22 and 2020-21 (17 each),
  2010-11/2011-12/2017-18/2023-24 (18 each) are the next-thinnest candidates,
  in roughly that order, for a future pass using the same method.
- 2016-17's remaining minutes content (committee sign-up lists, "Student
  Speaker" floor mentions) was read and deliberately left out — Amy Wyer,
  Michael Shelton and Alex Sergent were sworn in only as committee chairs,
  not senators; several other names appear only as public-forum speakers or
  guests with no seat claimed. None of these should be re-added on a future
  pass without new evidence of an actual seat.
