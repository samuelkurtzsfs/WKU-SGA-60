# Senate rolls, 22 August 2026 (second run): seven names for 2012-13

Scheduled run on `research-senate`, cut forward from the branch merged as PR
#111 by bringing in current `main`. Net result: **7 new senate members added**
for 2012-13, all adversarially verified.

## Step 1

`.research/senators-unverified.json` is `[]` — confirmed again, nothing to
reconcile.

## Access re-tested

Same two gating hosts, tested fresh rather than trusted from earlier notes:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 202 WAF challenge,
  three attempts spread over the run. Still closed.
- `web.archive.org` — connection reset on every attempt, both direct fetch
  and (implicitly) the CDX route. Still closed.
- `archive.org` (plain, not `web.archive.org`) direct Talisman downloads —
  **open and working** (confirmed against `talisman1980west`, 200, full
  text). Not a new source for the remaining gap years, since 1979-80's
  Talisman was already read in full on 21 August with nothing rank-and-file
  found, and 1966-67/1969-70/1971-72/1999-00 fall outside the 1971-1981,
  1986-87 span `archive.org` holds.
- **`wkuherald.com`'s WordPress API is open and gives full article text**,
  confirmed for both 2011-12 and 2012-13 date ranges. This is the productive
  route this run, and it was not exhausted before now for 2012-13 — it is a
  different host from `digitalcommons` and `web.archive.org`, so today's
  block on those two did not close it off.

## What this run added

2012-13 was the last remaining thin senate year with under 5 members (3, per
the 21/21 August notes' own count of thin years). The Herald's "SGA welcomes
new senators" (26 Sep 2012, https://wkuherald.com/46320/news/sga-welcomes-new-senators/)
reports SGA's fifth meeting of the year swearing in a full cohort:

- Barrett Greenwell, Taylor Ruby, Cole McDowell, Paige Settles — freshman
  senators
- Linda Cruz — the Gatton Academy of Mathematics and Science's dedicated
  seat
- Mark Reeves, Katie Martin — Graduate Students senators

All seven were already known to the archive by name — Reeves, Settles and
Cruz have full profiles under later offices (Reeves as 2013-14 executive
vice president, Settles as 2013-14/2015-16 speaker, Cruz as 2013-14
secretary, McDowell as 2014-15/2015-16 secretary) that already narrate this
same 2012-13 swearing-in in prose — but none of the seven were recorded in
`organization.senate.members` for 2012-13 itself. That gap is now closed.

A separate adversarial verifier subagent was given the full article text
(not a summary) and instructed to try to refute each of the seven claims
against it, explicitly warned about this project's history of bill-authors
and committee-chairs being mistaken for members. Verdict: **7 accept, 0
trim, 0 reject** — the article's own topic sentence ("The new senators were
welcomed and sworn in") governs all three following sentences naming all
seven people, none of whom appear elsewhere in the article in a competing
role.

One thing found and *not* added: the same article names an eighth person,
Hannah Garland, as author of a plus-minus grading resolution in a different
article (44945, 20 Feb 2013) — a resolution's author is not itself
membership evidence per this project's own traps, and no source calls her
"Senator Garland" or otherwise confirms a seat, so she was left out.

## A spelling flag, not a merge

The same article spells the senator filling a September 2012 vacancy "Shea
Wyatt"; the archive's existing entry for that appointment (sourced to the
SGA minutes of 25 Sep 2012 rather than the Herald) spells it "Shey Wyatt".
Per the project's rule to flag rather than resolve spelling doubts, a note
was added to the existing entry recording the discrepancy. Not treated as a
new person — same seat, same date, same appointment circumstance in both
sources.

## What is still not moved

- **1966-67, 1969-70, 1971-72, 1979-80** remain settled permanent gaps —
  unchanged from 21/22 August's notes, not re-tested again this run since
  nothing new opened up for them.
- **1999-00** still needs `viewcontent.cgi` (for full pre-2003 Herald
  article text) or a working `web.archive.org`, neither of which opened
  this run. `wkuherald.com`'s coverage does not reach back to 1999-2000.
- **1992-93's 19 remaining minutes items** (61 unverified names already on
  record per the 20/21 August notes) still want `viewcontent.cgi`
  specifically, since minutes for that era were never posted to
  `wkuherald.com` (which only carries Herald articles, not SGA's own
  minutes) — not addressed this run.
- **2011-12** was left alone this run (already at 18 members from the batch
  merged as `eaaf66e`) so effort went to the emptier 2012-13 instead.

## For the next run

`wkuherald.com`'s full-text API is confirmed open and is a real route
forward independent of the two hosts that have been closed for three
consecutive runs now. The highest-value next targets by this same method:
read 2012-13's remaining ~85 unread articles (of ~95 pulled this run) in
full for any further named senators speaking or voting on the floor (as
opposed to committee chairs or bill authors, which do not qualify alone),
then move to any other thin post-2003 year the same way before returning to
`viewcontent.cgi`/`web.archive.org` for the pre-2003 years those two hosts
gate.
