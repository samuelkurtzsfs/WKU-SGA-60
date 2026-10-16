# Photograph run, 16 October (scheduled): network state unchanged, eighteen more officer names checked out negative

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked `data/photos.json` against `data/years.json` directly before doing anything else,
rather than trust the last several reports' word for it.

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait.
- **Priority 2** (every other president or student regent): a direct sweep of every `leaders`
  entry in all 61 years against `photos.json`'s `leaders` array found zero without a portrait.
- **Priority 4** (years with no photograph at all): a direct sweep of every year id against
  `photos.json`'s `years` array found zero years missing.

`python3 scripts/portrait_gap.py`: 189 officer slots / 159 people / 157 with no portrait in any
year — unchanged from every pass since 13 October.

## Network state this session

Re-tested the three routes every report since 13 October has logged as closed, rather than carry
the prior finding forward unverified:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: 403, with the full navigation-header set
  (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`).
  Closed for PDFs. Unchanged.
- `web.archive.org`: connection reset by peer on the first request (no second attempt needed to
  confirm — the agent proxy itself reported the tunnel closing mid-exchange). Closed.
  **Editor's correction, 16 October 03:22 UTC: this route is open, and the finding above did not
  survive re-testing seventy minutes later.** `web.archive.org/web/2010/http://www.wku.edu/sga/`
  answered 302 and then served the 12 January 2011 capture in full (31,891 bytes), and the
  `/sga/executive/` page from that capture came back at 25,118 bytes carrying the 2010-11 executive
  roster as text — Cory Dodds named as Student Body President & Student Regent, the three elected
  and four appointed offices listed. Only the CDX search API (`/cdx/search/cdx`) timed out; the
  playback path did not. A single connection reset is a dropped tunnel, not a closed host, and
  this report read one as the other. Retry the playback path before recording this route closed
  again.
  Two cautions for whoever works it. The branch pages are not where a guessed path puts them —
  `/sga/branches/executive.php` is not archived and Wayback says so plainly, while `/sga/executive/`
  is; take the links out of the captured HTML rather than constructing them. And these pages print
  the officers' personal mobile numbers and university email addresses. Those are living people's
  contact details and no part of them belongs in `years.json`, `photos.json` or the site: take the
  name and the office, leave the rest on the page.
- `archive.org` metadata API (not `web.archive.org`): open. Queried fifteen Talisman yearbook
  identifiers for years in the 1990s–2010s that would bear on open officer-portrait gaps
  (`talisman1995west` through `talisman2015west`, selected years); every one came back with an
  empty `metadata`/`files` object, confirming archive.org's holdings are still the 1971–1981,
  1986, 1987 span this project has recorded before, not a wider set that would open a new route
  into the decades where the gap is thickest.
- `wkuherald.com`: open, but its WP-JSON endpoints (`/wp/v2/posts` search and `/wp/v2/media/{id}`
  caption lookups) 403'd on a majority of first attempts this session, clearing on retry after
  10–25 seconds with no fixed threshold found — consistent with the hard rate-limiting the
  15 October reports describe. Treated every 403 as CLAUDE.md's digitalcommons rule says to:
  stopped bursting, spaced retries out, never hammered.

## Eighteen officer-gap names checked against wkuherald.com, nothing usable

Worked from `scripts/portrait_gap.py --list`'s 189-slot gap, picking names not already logged as
exhausted in the 15 October reports, weighted toward cabinet/Senate leadership roles (more likely
to carry an individually captioned photo than a plain senator, which has a near-zero hit rate in
every prior pass):

- **Cody Cox** (Associate Justice 2015-16, Chief Justice 2016-17): two featured-image leads
  checked (articles 29139/28868 and their media). The one photo with a caption
  (media 28869) names Zach Jones and James Line proposing a GPA bill — not Cox, and neither name
  is in the officer gap. No usable image.
- **Ryan Richardson** (Speaker of the Senate, 2017-18): best lead, article 28871 ("Next student
  body president elected to office"), carries a featured photo (media 28872) captioned naming
  four 2017-18 executive candidates (Dahmer, Molyneaux, Lowry, Hounshell) — none of them
  Richardson, and none in the gap list. No usable image.
- **Josh Zaczek** (Legislative Research Chair, 2018-19/2019-20): five hits read for captions.
  The only individually captioned photos found name Garrett Edmonds (Executive Vice President)
  and Symone Whalin (a bill's author) — neither Zaczek nor in the gap list. No usable image.
- **Turner Reynolds** (Judicial Council 2019-20, Associate Chief Justice 2021-22): two hits,
  both text-only or (one, a 2023 football story) an unrelated namesake. No image.
- **Livi Ray** (Secretary of the Senate, 2023-24): every hit under this name is a *Herald* staff
  byline (photographer/writer), a different Livi Ray from the Herald's own newsroom, not the SGA
  officer. No usable image, and the name collision is worth flagging so a later pass does not
  attach a staff photo to the wrong Livi Ray.
- **Nicole Massarone** (Associate Justice, 2021-22): two hits. One's featured image (media 9352)
  carries no caption; the other (media 60867, "SGA swears in seven members...") captions the
  whole meeting generically ("the senate voted unanimously for four senate members...") with no
  individual named — exactly the situation CLAUDE.md's "a misidentified face is worse than no
  face" rule exists for. Left unattached.
- **Elizabeth DeLozier** (Secretary of the Senate, 2021-22): three hits beyond the already-known
  Bornefeld-election gallery (article 65821, previously checked photo-by-photo on 15 October —
  she is not one of its eight captioned subjects). The best remaining lead, article 67853 ("SGA
  elects committee chairs..."), has a featured photo (media 67788) captioned only "Members of the
  WKU Student Government Association executive cabinet listen to proposals..." with no one named.
  No usable image.
- **ShyAnte'e Williams** (Graduate Student Senator, 2022-23): one hit, an unrelated donation-drive
  story; the 403 on its media id was not retried within this pass's window. Open, not closed.
- **Smita Peter** (Director of Information Technology, 2017-18): six hits, all text-only SGA
  floor-business reports or an unrelated Indian-holiday celebration story. No image.
- **Jason Herlick** (Judicial Council, 2019-20/2021-22): one hit, text-only. No image.
- **Morgan Wysong** (Public Relations Committee Chair, 2016-17): three hits; none carries an
  individually captioned photo of her specifically.
- **Abhishek Bose** (Director of Information Technology, 2016-17): one hit, an unrelated Indian
  student group story that only happens to share a search term. No image.
- **Mark Clark, Lucas Knight, Devan Richardson, Zachary Skillman, Tribhuwan Singh**: searched;
  Devan Richardson, Zachary Skillman and Tribhuwan Singh returned zero hits at all. Mark Clark
  and Lucas Knight returned many hits (both common enough names that most results are unrelated
  SGA floor-business stories mentioning them only in running text, or clearly a different person
  entirely); no individually captioned image surfaced for either.

None of these eighteen produced a usable portrait. No file was downloaded; no entry was added to
`data/photos.json`.

## What is still open

The 189-slot gap is unchanged in count. Xavier Spiess's portrait (identified 15 October, correctly
withheld because `organization.senate.officers` for 2025-26 has no entry for him) is still waiting
on whoever next edits `years.json`'s organization data for that year — this agent's rules confine
it to `photos.json` and it cannot add that entry itself. Of the two routes that would most likely open
the pre-2011 names in this gap, `cgi/viewcontent.cgi` for Talisman PDFs was closed for this
session's entire window, the fourth day running. `web.archive.org` for the old SGA website's
officer pages was recorded closed here and is not: see the correction above. It is a route for
names and offices rather than portraits — the 2011 capture carries no officer photographs, only
the university logo — so it does not shift the 189-slot portrait gap by itself, but it is open,
and it bears on exactly the organization data the Spiess note above is waiting on. Everyone checked this pass stays open for lack of an individually captioned
photograph, not for lack of searching.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph. No file in `data/photos/` or entry in
`data/photos.json` changed this pass.
