# Senate rolls, 22 August 2026: no new names, access unchanged from 21 August

Scheduled run on a fresh `research-senate`, cut from current `main` (the
previous `research-senate` was merged as PR #111). Net result: **no changes
to `data/years.json`.**

## Step 1

`.research/senators-unverified.json` is `[]` — confirmed again, nothing to
reconcile.

## Step 2: the six years with no `organization.senate.members`

Unchanged from the 21 August note: 1966-67, 1969-70, 1971-72, 1979-80 are
settled permanent gaps (nothing dated in that span in the digitised minutes
collection, and 1979-80's Talisman was already read in full on 21 August
with nothing rank-and-file found). 2026-27 is the year in progress. 1999-00
is the one gap that plausibly has a source — see below.

## Access, re-tested by hand this run

Same two hosts that gate almost all new senate-roll research were tested
twice, roughly forty minutes apart, since both are documented elsewhere as
intermittent by the hour rather than reliably down for a whole day:

| host | result |
|---|---|
| `digitalcommons.wku.edu/cgi/viewcontent.cgi` | **HTTP 202, WAF challenge**, both attempts — an SGA minutes item (article 1912) that would have been read first this run |
| `web.archive.org` | **connection reset on every attempt**, `https://` included, both times — same failure mode as 21 August, not the "open on https" state from 20 August |
| `digitalcommons.wku.edu` landing pages | open, 200, as always |
| `wku.edu/sga/uploads/minutes/2011/` and `/2015/` (directory listing) | `/2015/` **404**; `/2011/` still **403**, as the 21 August note recorded — re-checked by the editor on merge, so the two paths fail differently rather than both having changed. Same result either way: no listing, so no filenames for the thin 2011-12/2012-13 years or for 2015-16 without guessing, which the 21 August note already judged not worth the request volume. |
| `wku.edu/sga/` and its current `legislative_archive_2.php` | open, but only link to the current (2025-26) legislative session's bills — no path to a pre-2016 minutes archive was findable from the live site's own navigation. |

So today's access is the same practical dead end as 21 August, reached by a
slightly different route on the `wku.edu` side.

## What was tried instead, and why it did not produce names

With `viewcontent.cgi` closed, full Herald text for 1999-00 is not
reachable, and `wkuherald.com`'s live search does not cover pre-2011
content. The one thing this run could still check was whether the *local*
`data/herald-index-full.json` undercounts 1999-00 the way CLAUDE.md warns a
busy issue can — spot-checked the fullest single day found (18 April 2000,
issue 8115, 32 stored lines) against the live TopSCHOLAR landing page, which
is reachable even with `viewcontent.cgi` closed. The two matched exactly,
line for line — this issue was not truncated locally. That is one data
point, not a guarantee for the rest of the SGA-related issues in the 1999-00
window, but it means the hits already surfaced from the local index for
1999-00 are a reasonable starting list for whoever next has `viewcontent.cgi`
access, not a possibly-incomplete one.

The count of those hits depends entirely on the keyword set, so state the
filter next time rather than the bare number. Across both calendar years
1999 and 2000 the full index holds 246 items, 112 of them Herald issues;
matching on student government / SGA / ASG gives 65 issues, and adding
senate and congress gives 75.

Read in full, those 78 hits are almost entirely spring 1999 election
coverage (candidates for president, administrative vice president and
treasurer — Amanda Coates, Ryan Morrison, Cassie Martin, Leslie Bedo and
others already recorded as leaders/executive) and routine committee-business
headlines. None names a rank-and-file senator being sworn in, seated, or
voting — the kind of primary-source statement the project's own rules
require before adding a member. Candidacy for an executive office is not
senate membership, and a headline naming who ran for president is not
evidence about who sat in Congress that year. No names were added on this
basis, per the same judgment the 21 August note already reached for 1999-00.

## For the next run

Nothing here changes the 21 August plan: retry `viewcontent.cgi` and
`web.archive.org` fresh rather than trusting any single day's note, and if
`viewcontent.cgi` opens, prioritize the 19 remaining 1992-93 minutes items
(61 unverified names already on record) and the thin 2011-12/2012-13 years
before a fresh 1999-00 sweep, since a 1999-00 roll still needs full article
text this run could not reach.
