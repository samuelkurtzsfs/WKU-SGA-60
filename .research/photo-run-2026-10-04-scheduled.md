# 4 October 2026 (photograph routine, scheduled)

## What was checked before doing anything

Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley all still carry a portrait in
`data/photos.json`. Confirmed fresh against the current `data/years.json`: every top-level
`leaders` record (all 61 years, every president and every student regent) has a matching entry in
`data/photos.json`. Nothing missing at either of the top two priority tiers.

`research-photos` was merged onto the current `origin/main` tip (`ad750140`) with no conflicts.
`python3 scripts/build.py` runs clean.

## Access routes re-tested; two are worse than the last report left them

- `digitalcommons.wku.edu` — not just `cgi/viewcontent.cgi` (the PDF endpoint, long known to
  403 with a Cloudflare challenge). The **landing pages are now blocked too**: `talisman/`
  returns a plain 404, and a direct fetch of the same URL through the WebFetch tool returns the
  same 404. The 2 October reports could still reach landing pages and only lost the PDF route;
  this session cannot reach the host at all.
- `web.archive.org` — HTTPS resets at the TLS handshake (`curl: (35) Recv failure: Connection
  reset by peer`); HTTP gets a flat 403. The separate `archive.org/wayback/available` lookup API
  (a different host) still answers normally and resolves a snapshot timestamp, but the snapshot
  itself is unreachable through either scheme. Same wall as 2 October, confirmed again rather
  than assumed.
- `archive.org`'s own Talisman mirror is unchanged: only 1971-81 and 1986-87 exist there.
  Checked by direct item fetch and by `advancedsearch.php` query, both paced a second apart:
  1984, 1995, 1996, 1997, 2001, 2009, 2017 and 2018 all come back with no item on file (503 from
  the download URL, zero hits from the search API). None of the years still carrying an
  officer-portrait gap fall inside the covered window, so this route cannot reach any of them.
- `wkuherald.com`'s WordPress REST API still answers normally and was the only usable route this
  run.

## The officer-portrait gap list has 68 names never searched before

Rebuilt the gap list fresh from `data/years.json` against `data/photos.json`: 217 executive and
Senate-officer records without a portrait, the same count the 2 October evening report used.
Cross-checked all 217 against every `.research/photo-run-*.md` report on file (38 of them) rather
than trust that report's claim that the whole list had already been searched once. It had not:
**68 names turn out never to appear in any prior report.** All 68 are concentrated in committee
chairs, Judicial Council justices and senators-at-large — offices that other research branches
(the senate and roster passes) have been adding to `organization` on `main` since the last
exhaustive photograph sweep, so the gap list grew with real new entries rather than staying the
closed set the last report believed it to be.

Searched all 68 against `wkuherald.com`'s search API (one request per name, paced a second apart,
full browser user agent). Every one returned either no hits or hits whose `featured_media` belongs
to an unrelated article that happens to contain the same name string — sports box scores, opinion
columns, unrelated news stories — not a photograph of the SGA officer being searched. Checked each
"hit with an image" by reading the article; none names the person in a caption or an SGA context.
Two examples of the pattern: "Jason Cole" (1997-98 Student Affairs chair, later 1998-99 Judicial
Council) matches nine WKU Herald photos, none about him — a 2023 football recruiting story, a 2023
Masters-degree feature, a baseball recap; "Kelly Simmons" (2012-13 Judicial Council) matches five
images, all 2013 WKU softball box scores for a player of the same name. This confirms, rather than
overturns, the finding the 1-2 October reports already reached by testing a smaller sample: the
WordPress-era Herald does not carry individually captioned photographs for officers below
president/regent, and a `featured_media` hit on a name search is not evidence of one.

One near-miss worth recording for whichever run next has a working digitalcommons or wayback
route: the Herald's "Next student body president elected to office" piece (28871, 19 Apr 2017) is
the only hit that is genuinely about SGA for three of the 68 names — Luke Edmunds, Morgan Wysong
and Jordan Tackett, all named in the body as newly elected senators. Its featured photograph (media
28872) carries a caption identifying exactly four people by a stated left-to-right order —
Savannah Molyneaux, Andi Dahmer, Kara Lowry and Conner Hounshell, all of whom already have
portraits in `data/photos.json` — and none of the three senators-at-large. Checked and ruled out,
not a lead.

## Nothing added

No portrait and no year photograph were added this run; every lead this session's open routes
could reach was checked and did not identify a usable photograph. `data/photos.json` and
`data/photos/` are unchanged from the merge-in of `main`.

## For the next run

- The 68 newly-surfaced names are now searched once each on `wkuherald.com` and came up empty;
  they still need the Talisman/digitalcommons route this session could not reach at all (not even
  landing pages), or a working `web.archive.org`.
- Re-test `digitalcommons.wku.edu` and `web.archive.org` from scratch rather than trusting this
  report — both have swung between reachable and walled across different sessions on this
  project, sometimes within the same week.
- The four years with no *general* year photograph (1994-95, 1995-96, 2000-01, 2008-09, all with
  a leader portrait already) remain open for the same reason: no route to a Talisman volume or a
  digitalcommons-hosted Herald page for those years was available this session.
