# Senate rolls, 23 August 2026 (scheduled run, second pass): 1999-00 opened

Scheduled run on `research-senate`. The branch on origin had already been fully
merged into `main` again since the previous scheduled pass earlier the same
day (the one that added five 2012-13 senators) — 0 commits ahead, 17 behind —
so it was recreated from current `main` rather than reused, then fast-forwarded
to catch a further 9 commits that landed on `main` from other routines while
this run's research was in flight.

## Step 1: reconcile `senators-unverified.json`

Already `[]`. Confirmed, not re-litigated.

## Step 2: the oldest unworked year

Six years carried no `organization.senate.members`: 1966-67, 1969-70, 1971-72,
1979-80, 1999-00, 2026-27 (in progress, not applicable). The first four are
documented permanent gaps — no minutes reach that era, and the relevant
Talisman volumes (only 1971-72 is held on archive.org) profile officers, not
the body, per `senate-rolls-gap-years-2026-08-20.md` and the 22 August
re-check of 1979-80. **1999-00 was the one live target left**, per that same
file's note that Herald coverage of the year exists but "does not print a
roster" — names would have to come piecemeal, from individuals doing
something newsworthy, with each one adversarially checked rather than lifted
from a list. That is what this run did.

## What this run added

A researcher subagent read all 36 candidate Herald issues between the
September 1999 and April 2000 for individual mentions of sitting Congress
members — not committee chairs, not bill authors. `viewcontent.cgi`'s WAF
challenge, open earlier in the day, had closed again by the time this run's
research started; the agent worked around it using Wayback Machine mirrors of
the same PDF URLs. It surfaced two names; a corrected OCR misread ("who is 1
SGA member" was actually "who is **not** an SGA member") kept a false
positive out before it ever reached the verifier.

A separate adversarial verifier subagent re-fetched the primary sources
directly (this time `viewcontent.cgi` was open again — the challenge appears
to toggle over the course of hours, consistent with what earlier runs already
found) and read the actual page images rather than trusting either agent's
transcription.

- **Mark Rawlings — accept.** "Louisville freshman and SGA Congress member
  Mark Rawlings said he credited ignorance among students to SGA's low
  turnout" (Herald 75:32, 25 Jan 2000, "SGA enrollment numbers down"). A
  direct identification in the reporter's own voice, in a story specifically
  about Congress attendance. The archive already carries a Mark Rawlings
  appointed VP of Finance in January 2001 and elected VP of Public Relations
  for 2001-02 — a coherent trajectory for the same person, not proof on its
  own but consistent, and no other Rawlings anywhere in the file or in
  `name-aliases.json`.
- **Dwight Campbell — trimmed, not accepted as a bare member.** Every
  1999-00-dated source calls him only "LRC Chairman" / "chairman of the
  Legislative Research Committee." The one place "Congress" attaches to him
  personally — an April 2000 quote that he "came into SGA Congress in the
  spring of 1998" — is testimony about the past, not a stated 1999-00 status,
  and the archive already files his 1998-99 role the same way, as committee
  chair rather than roster member. Recorded instead under
  `organization.senate.officers` as Chairperson, Legislative Research
  Committee, matching the established pattern, with the spring 2000
  recollection folded into the note as biographical material rather than
  used to claim continuous Congress membership the sources don't actually
  assert.

1999-00 now has one senate member and one senate officer recorded, up from
zero of either. `build.py`, `check_data.py` and `check_duplicates.py` all
pass clean; none of the six pre-existing duplicate-checker pairs touch this
year.

## What's left

- 1999-00 is not closed out — two names from 36 issues of a full year's
  Herald coverage is a thin roster, and the method (piecemeal individual
  mentions, each independently verified) generalizes to further passes over
  the same 36 issues or a wider date range if a future run wants to spend
  more time on it. Nothing found this run was strong enough to include and
  left out for time; see the researcher's full transcript notes on Billy
  Lyons ("a three-year SGA member... co-chairman of... Campus Improvements")
  as the one borderline case worth a second look, ideally against an SGA
  minutes or legislation roster from spring 2000 if one surfaces.
- `1966-67, 1969-70, 1971-72, 1979-80` remain settled permanent gaps.
- 2013-14 and other post-2003 years likely have the same kind of headroom the
  22 August/23 August passes found in 2012-13 via wkuherald.com's WordPress
  API — not attempted this run, which spent its time on the older, harder gap
  year instead.
