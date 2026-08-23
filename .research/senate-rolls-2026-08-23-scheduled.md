# Senate rolls, 23 August 2026 (scheduled run): five names for 2012-13

Scheduled run on `research-senate`, cut fresh from current `main` (the branch
on origin was itself fully merged into `main` already — 0 commits ahead, 13
behind — so it was recreated rather than reused).

## Step 1: reconcile `.research/senators-unverified.json`

Already `[]`. Nothing to reconcile; confirmed and moved straight to step 2.

## Step 2: pick the oldest year with no `organization.senate.members`

Six years currently have none: 1966-67, 1969-70, 1971-72, 1979-80, 1999-00,
2026-27 (the year in progress, not applicable). Every one of the other five
has already been exhaustively checked and documented as a genuine dead end
in `.research/senate-rolls-gap-years-2026-08-20.md` and the 21/22 August
follow-ups:

- 1966-67, 1969-70, 1971-72: no minutes on TopSCHOLAR reach this era (the
  collection is essentially empty before 1975-76), and archive.org's
  Talisman holdings don't reach 1966-67/1969-70 at all. 1971-72's yearbook
  was read in full previously with nothing rank-and-file found.
- 1979-80: re-checked this run. The only two dated minutes items inside the
  term swear in *1980-81's* officers, not 1979-80's (confirmed again, no
  change). The 1980 Talisman's ASG spread (pp. 274-275) was re-read in full
  this run looking specifically for a Congress/Senate composite roster of
  individual names — none exists; the volume profiles officers and
  committee chairs only, exactly as 1972's did. No new source found; this
  stays a genuine permanent gap.
- 1999-00: needs `viewcontent.cgi` or `web.archive.org` for full pre-2003
  Herald text, or its own careful piecemeal Herald sweep — already
  attempted and documented as unproductive on 20/22 August. Not re-attempted
  this run; see "what's left" below.

Per the standing "for the next run" note in `.research/senate-rolls-2026-08-22b.md`,
went to the highest-value real target instead: 2012-13, the thinnest year
with real headroom (10 members going in, all from the 22 August pass).

## Access re-tested

- `wkuherald.com`'s WordPress API — open, full article text, confirmed
  again for the 2012-13 date range. No pacing needed on this host.
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` and `web.archive.org` were
  not retried this run — this run's Herald sweep did not need them.

## What this run added

Pulled every SGA/senate/congress/student-government-tagged wkuherald.com
post between 1 Aug 2012 and 1 Jun 2013 (168 raw hits across five keyword
searches, 79 judged actually about SGA after excluding unrelated hits like
"CHH Politics" columns and Rand Paul coverage), read all 79 in full text,
and searched for individuals explicitly identified as senators — not bill
authors, not committee chairs alone — being sworn in, appointed, or quoted
in their capacity as a sitting senator.

Five survived: three new drafted from direct "student senator NAME" /
"NAME, an SGA senator" quotes, and two from an explicit appointment
sentence. A separate adversarial verifier subagent was given the five raw
article texts (not a paraphrase) and instructed to try to refute each
claim against the traps this project has been burned by before (chair ≠
member, bill author ≠ member, wrong year, ambiguous appointment). All five
survived: **5 accept, 0 trim, 0 reject.**

- **Laura Harper**, senator at large — "Student senator Laura Harper" at a
  17 Oct 2012 picnic with President Ransdell, and again "an SGA
  senator-at-large" on 12 Apr 2013.
- **Mac Mullins**, senator — "Student senator Mac Mulcins" on 23 Oct 2012.
  The rest of this year's record spells the same person "Mac Mullins"
  (Public Relations Committee chair); flagged as a spelling variant per
  project convention, not silently resolved, and his Senate membership
  rests only on the direct "student senator" quote, not on the chair title.
- **Taylor Gwinn**, senator — appointed 12 Feb 2013, named alongside Cockrel
  in the same sentence that separately and correctly identifies Seth Church
  and Kara Raley's appointments as Judicial Council, not Senate.
- **Brad Cockrel**, senator — appointed the same 12 Feb 2013 meeting. He
  later ran for executive vice president and became 2013-14 Chief of
  Staff, both already recorded elsewhere in the archive; this entry covers
  only the 2012-13 Senate seat.
- **Roy Ratliff**, senator at large — presidential appointment approved by
  the senate 16 April 2013, the same meeting that elected Paige Settles the
  next speaker.

2012-13 now has 15 members, up from 10. `build.py`, `check_data.py` and
`check_duplicates.py` all pass clean; the six known duplicate pairs are
unchanged.

## What's left

- **1999-00** is still the one plausible remaining gap year, and still
  needs either a working `viewcontent.cgi`/`web.archive.org` for full
  pre-2003 Herald text, or a dedicated, carefully-verified piecemeal sweep
  of the local index hits — the 20/22 August notes already found the
  September/October 1999 issues carry no post-election roster, so a future
  pass should expect this to be slow, individual-mention work, not a single
  list.
- 2013-14 and other post-2003 years likely have the same kind of headroom
  this run found in 2012-13 — this run only worked one year's worth of
  wkuherald.com text; the method (pull full text via the WP API, read for
  direct "senator" attributions, verify adversarially) generalizes cleanly
  and costs nothing in pacing.
- `1966-67, 1969-70, 1971-72, 1979-80` remain settled permanent gaps.
