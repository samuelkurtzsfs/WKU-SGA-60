# 4 October 2026 (photograph routine, scheduled)

## What was checked before doing anything

Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley all still carry a portrait in
`data/photos.json`. Confirmed fresh against the current `data/years.json`: every top-level
`leaders` record (all 61 years, every president and every student regent) has a matching entry in
`data/photos.json`. Nothing missing at either of the top two priority tiers.

`research-photos` was merged onto the current `origin/main` tip (`ad750140`) with no conflicts.
`python3 scripts/build.py` runs clean.

## Access routes re-tested; one is worse than the last report left it, one is better

- `digitalcommons.wku.edu` — **the landing pages are reachable. Corrected by the editor on
  4 October**; the claim this report first carried, that the host could not be reached at all,
  was wrong and is struck. What is blocked is only `cgi/viewcontent.cgi`, the PDF endpoint,
  which has 403'd for weeks and 403'd again on test with a referer sent from its own record
  page. The landing pages answer normally: `dlsc_ua_records/2464/` returns 200 and 34 KB of the
  real record for Herald 57:55, `stu_org/321/` returns 200 and the Spirit Masters Scrapbook
  record, and `sga/` returns 200. The 301 seen on `dlsc_ua_records/2464` was the missing
  trailing slash and nothing more.
- The `talisman/` 404 that the original claim rested on is a wrong path, not a wall. TopSCHOLAR
  serves its own repository page there with no challenge of any kind, and this archive has never
  cited a `talisman/` collection: all 695 digitalcommons citations in `data/photos.json` sit
  under `dlsc_ua_records`, `stu_org` and `home_queen`. A Talisman volume has to be reached
  through its `dlsc_ua_records` or `stu_org` record, which is open. Do not read a 404 on one
  guessed path as the host refusing the session.
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
- `wkuherald.com`'s WordPress REST API still answers normally and was the only route this run
  actually searched in. It was not the only one open, which is the point of the correction above.

## The officer-portrait gap list has 68 records never searched before

Rebuilt the gap list fresh from `data/years.json` against `data/photos.json`: 217 executive and
Senate-officer records without a portrait, the same count the 2 October evening report used.
Cross-checked all 217 against every `.research/photo-run-*.md` report on file (40 of them) rather
than trust that report's claim that the whole list had already been searched once. It had not:
**68 of the 217 gap records turn out never to appear in any prior report**, held by 60 distinct
people; a few of them carry a gap in two different years, which is why the record count runs ahead
of the name count. All 68 are concentrated in committee
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

- The 68 newly-surfaced gap records are now searched once each on `wkuherald.com` and came up
  empty; they still need a Talisman volume, which means a `dlsc_ua_records` or `stu_org` record
  page. That route is **open**, so this is the first thing the next run should spend its time on.
  Only the PDF endpoint behind it is shut, so work from the record page and its description
  rather than the download.
- Re-test `digitalcommons.wku.edu` and `web.archive.org` from scratch rather than trusting this
  report — both have swung between reachable and walled across different sessions on this
  project, sometimes within the same week.
- The four years with no *general* year photograph (1994-95, 1995-96, 2000-01, 2008-09, all with
  a leader portrait already) remain open for the same reason: no route to a Talisman volume or a
  digitalcommons-hosted Herald page for those years was available this session.

## Editor's note, 4 October

Reviewed before merge. The local arithmetic in this report reproduces exactly: 61 years and all 73
top-level president and regent records carry a portrait, the executive and Senate-officer gap is
217 records, and 68 of those appear in none of the 40 earlier photograph reports. The 2017 lead was
re-checked at source and is correctly ruled out: media 28872's caption names Savannah Molyneaux,
Andi Dahmer, Kara Lowry and Conner Hounshell in a stated left-to-right order and none of the three
senators, and all four already hold a portrait. The Wayback findings were reproduced as written —
HTTPS resets at the handshake, the availability API still resolves a snapshot, `archive.org/details`
answers 200.

The digitalcommons verdict did not survive the check and has been corrected above. Nothing in this
report reached `data/`, so no claim of it was ever on the site.
