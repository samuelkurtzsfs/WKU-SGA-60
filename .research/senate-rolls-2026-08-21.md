# Senate rolls, 21 August 2026: no new names, and why

Scheduled run on branch `research-senate`. Net result: **no changes to
`data/years.json`.** Every avenue this run could reach was checked and
produced either a confirmed dead end or a source this environment could not
open right now. Recorded here so the next run does not repeat the same checks
cold, per the project's own rule that a source you could not open is not a
source that says nothing.

## Step 1 (reconciling `.research/senators-unverified.json`)

Already empty — confirmed, not assumed. An earlier run's adversarial pass had
already reconciled it. Nothing to do.

## Step 2: the six years with no `organization.senate.members`

`data/years.json` currently has empty `organization.senate.members` on
1966-67, 1969-70, 1971-72, 1979-80, 1999-00 and 2026-27.

- **2026-27** is the year in progress. Not a gap to research from old
  minutes — there is no election result to record yet.
- **1966-67, 1969-70, 1971-72** — reconfirmed as permanent gaps in what
  TopSCHOLAR has digitised. `digitalcommons.wku.edu/sga/Meetings/Minutes/`
  carries nothing dated before 13 February 1969 and effectively nothing else
  until 1975-76; no alternate host covers these years. See
  `.research/senate-rolls-gap-years-2026-08-20.md` for the full listing pull
  this claim rests on — reconfirmed this run rather than re-pulled, since
  the collection's contents do not change day to day.
- **1979-80** — already established as a dead end for minutes (the only two
  items dated inside the term swear in *1980-81's* officers). **New this
  run:** its Talisman is on `archive.org` (`talisman1980west`, inside the
  1971-1981 span the site holds) and had not been checked before. Pulled in
  full and searched for every SGA/ASG/Congress/senate mention. It carries a
  single two-page narrative feature on ASG's year (pp. 274-275), built
  entirely around President Jamie Hargrove's own account of the year —
  membership apathy, a phone-in radio show, the representation amendment
  that set eight on-campus, eight off-campus and eight general seats. No
  composite Congress photo, no roll, no list of names beyond Hargrove and
  committee chairman Kevin Kinne (already a chair, not a member claim). So:
  **Talisman does not substitute here either.** 1979-80 is now checked
  against both sources this archive has for it and stays empty. Nothing to
  add, nothing to correct.
- **1999-00** — reconfirmed as the one gap year where a source plausibly
  exists (Herald covers it heavily) but was not safely buildable this run.
  See below.

## What blocked going further

Tested by hand, this run, at roughly 05:00-06:00 UTC on 21 August:

| host | state |
|---|---|
| `digitalcommons.wku.edu` landing pages | **open**, 200 — titles, dates, one-line abstracts, same as always |
| `digitalcommons.wku.edu/cgi/viewcontent.cgi` | **blocked**, HTTP 202, empty body, on every attempt — a fresh Executive Cabinet minutes item (787, 17 March 2008) tried three times over roughly 15 minutes, always 202. This is the route that reads the actual roll call inside any minutes PDF; without it, a landing page's one-line description is all that is reachable, and that never names a single attendee. |
| `web.archive.org` | **connection reset on every attempt**, `https://` included — six separate tries, both the CDX API and a direct page fetch. This is a change from 20 August's notes, which had `https://` open. Worth re-testing fresh rather than trusting either day's note as permanent. |
| `www.wku.edu/sga/...` directory listings | **403** on every folder tried (`uploads/minutes/2010/`, `/2011/`, `/2012/`) — this held even for `2010/`, which is already cited successfully by filename in the archive, so the block is on listing itself, not access to a known file. Specific files inside those folders (e.g. the already-cited `2014/sga_minutes.docx`) still return 200. Without a listing or a Wayback capture of one, the exact filenames for 2011 and 2012 (thin years — 1 and 2 members respectively, against 23-28 for 2014-16) cannot be recovered without guessing, and guessing filenames against a live university server, with no working convention (`9-27-11.docx` vs `10-23-12.docx` vs `9-25-2012.docx` — three different date formats already cited in the same two-year span), was judged not worth the request volume for the likely yield. |

Net effect: the two things that would have moved this run forward — actual
minutes text (via `viewcontent.cgi` or a listing-plus-guess route through
`wku.edu`) and Wayback captures of old listings — were both closed for the
whole run. This is consistent with 20-21 August's own notes describing
`viewcontent.cgi` as intermittent by the hour, not a permanent wall.

## What the next run should do

- **Retry `viewcontent.cgi`.** It has opened mid-run before (see
  SGA-60-AGENT-INFO.md §8.3 item 1, item 5). If it is open, the highest-value
  targets in order are: the 19 remaining 1992-93 minutes items behind the 61
  unverified names already on record (§8.3 item 5), then a fresh push into
  years with `organization.senate.members` under 5 (2011-12: 1, 2012-13: 2).
- **Retry `web.archive.org` fresh**, both the CDX API and direct fetches, before
  assuming it is down — it was open on 20 August and reset on every attempt
  today. If it comes back, CDX search for
  `wku.edu/sga/uploads/minutes/2011/*` and `/2012/*` would recover the actual
  filenames for those two thin years without guessing.
- **1999-00 still wants its own careful pass**, not a byproduct of a run that
  is also trying other years: read the Herald issue by issue (not the local
  truncated index) for the year, hold every rank-and-file name to a
  source that actually shows them seated or voting, not just named in a bill
  story, and run the adversarial verifier before merging. This has now been
  flagged as the plan on two separate runs (20 and 21 August) without being
  attempted — it may be worth a run that does only this and nothing else.
- **1966-67, 1969-70, 1971-72, 1979-80** should be treated as a settled,
  permanent gap in what TopSCHOLAR and `archive.org` hold, not re-checked
  again absent a genuinely new source (a physical archive box, a yearbook
  host other than `archive.org`, etc.). **Correction, flagged by the 21
  August editor's pass:** an earlier draft of this list also named 1967-68,
  which was wrong — 1967-68 already has a senate roll in `data/years.json`
  and was never one of the empty years. The five years above are the actual
  gap.
