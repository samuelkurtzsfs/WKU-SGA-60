# The Wednesday cluster, second pass, 30 September 2026

The pass of 29 September corrected eighty meeting dates and closed with a count: events sourced
to `wkuherald.com` ran 319 Tuesday to 78 Wednesday, and it described the remaining 78 as
"entries whose article names no day, and entries that really fell on a Wednesday."

That description was right about most of them and wrong about seven. This pass opened all 78
again — 76 fetched, the two `web.archive.org` citations refused by the container's network policy
as before — and read each for a statement of when the business happened. The moved table of
29 September runs from 2011-09-14 to 2023-03-01; every correction below falls at or after
January 2023, which is where the first sweep's coverage thinned rather than stopped.

Same rule as the first pass: a date moved only where the article says the day.

## Moved

| was | is | year | entry | the day, in the article's words |
|---|---|---|---|---|
| 2023-01-25 | 2023-01-24 | 2022-23 | Senate approved five nominations and reviewed a shrinking budget | caption: "during the second session of the spring semester on Tuesday evening, Jan. 24, 2023"; body: "the second meeting of the semester" |
| 2023-08-30 | 2023-08-29 | 2023-24 | Kurtz seated a five-member Judicial Council and seven committee heads | "hosted their first meeting of the fall semester on Tuesday" |
| 2023-09-27 | 2023-09-26 | 2023-24 | Fall election winners sworn in | "sworn-in during the 6th meeting of the 23rd Senate on Tuesday" |
| 2023-11-29 | 2023-11-28 | 2023-24 | Eight bills create Honors senate seat and set Judicial Council office hours | "at the 12th meeting of the 23rd Senate on Tuesday, Nov. 28" |
| 2025-04-16 | 2025-04-15 | 2024-25 | Students ratified the DEI committee amendment with 88% of the vote | "announced the spring election results for the 25th Senate on Tuesday, April 15" |
| 2025-04-16 | 2025-04-15 | 2024-25 | The 24th Senate held its final meeting | "held its final meeting of the 24th Senate on Tuesday, April 15" |
| 2025-09-24 | 2025-09-23 | 2025-26 | Senate moves to surface the Hilltoppers concern form | "In one of two bills passed at SGA's weekly meeting on Tuesday" |

Two of the seven had already stated the right day in their own prose while the `date` field said
otherwise: the 24th Senate's final meeting reads "met for the last time on April 15", and the
Narcan entry discussed below reads "passed Resolution 2-23-S on Feb. 7". An entry whose body
contradicts its own date is the cheapest of all of these to find, and worth a check of its own.

## Read and left alone

- **2023-02-15**, the Narcan resolution. An automated sweep would move this to 7 February, and it
  should not. The article is a follow-up, not a meeting write-up: it reports that the resolution
  "was passed unanimously during the SGA meeting on Feb. 7" — which the entry's body already says
  — and then adds material that only exists on 15 February, Housing and Residence Life asking to
  delay installation to 1 August and the director of housing operations on overdose incidents.
  Moving the date would make that later material anachronistic. It stands at 15 February.
- **2023-02-01** and **2023-02-15** both carry a photograph caption reading "second session of the
  spring semester on Tuesday evening, Jan. 24, 2023". On the 1 February article that caption is
  reused from the previous week and describes neither the 17th Meeting of the 22nd Senate the
  article covers nor any business in it. A caption is evidence of the day only where the body
  agrees, which is why 2023-01-25 moved and 2023-02-01 did not.
- **2011-10-05**, Ransdell on the housing requirement. The 29 September pass recorded that this
  says "tonight" and never names the weekday. Confirmed from the page: the article's only weekday
  is "the Campus Clean-up is set for 3:30-5 p.m. Tuesday", an upcoming event. It stands.
- **2023-10-11**, **2026-09-09** and the rest of the residue name no day for their own business.
  2026-09-09 is not a senate meeting at all: its source is Lucas speaking "in a meeting with
  Herald editors".
- The four entries the first pass found name Wednesday and mean it, and the three it set aside
  for naming a Wednesday resignation, an undated decision and a cancelled meeting, were all
  read again and left again.

## A contradiction in the source, not in the file

**2024-04-17, the 23rd Senate's final meeting.** The article reads "senators gave their last
remarks to the Senate, Tuesday, April 17 at the 23rd meeting of the 23rd Senate." 17 April 2024
was a Wednesday, so the source contradicts itself, and the companion article on the same day
puts the election results "at midnight Wednesday, April 17". The meeting was most likely
Tuesday 16 April and the *Herald* misprinted the date, but that is inference and the first pass's
rule holds: the entry keeps 17 April, and this paragraph records why, so a later pass with the
minutes can settle it rather than guess.

## The check

Events sourced to `wkuherald.com` now run 326 Tuesday to 71 Wednesday. The 71 are entries whose
article names no day and entries that really fell on a Wednesday — this time having read all of
them rather than most.

Moving 2023-11-29 onto 2023-11-28 puts it beside "The 23rd Senate corrects its own governing
documents", which cites the same article and covers three Legislative Operations Committee bills
from the same meeting. Same-day legislative business is genuinely several events, so both stand,
but the three LOC bills are a subset of the eight measures the other entry counts, and the two
overlap more than two entries should. Worth a merge decision by a pass that can read both against
the bill texts; not merged here, because nothing in either is unsourced.

## The next cluster, named so it is not lost

Both passes have looked only at Wednesdays. The same count by weekday shows the fault is almost
certainly larger:

| weekday | events sourced to `wkuherald.com` |
|---|---|
| Tuesday | 326 |
| Thursday | 114 |
| Wednesday | 71 |
| Friday | 43 |
| Monday | 21 |
| Saturday | 2 |
| Sunday | 5 |

The *Herald* printed twice a week for much of the 2000s and early 2010s, Tuesday and Thursday,
while SGA met on Tuesday. A Thursday-dated meeting write-up from those years is the same error as
a Wednesday-dated one, and 114 of them have never been read for a stated day. The Friday and
Monday sets are smaller and the same argument applies. That is the next pass's job, on the same
rule: fetch the article, quote the day, move only where the article says it.
