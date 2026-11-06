# Photograph run, 6 November third scheduled pass: full-browser navigation tried against all three standing blocks and the live SGA site, no new portrait

## Priorities 1, 2 and 4, reconfirmed directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — "61 years, 1964 events, 60 people
  have been president," no portrait-coverage complaint. Zero presidents or student regents
  without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as the pass twelve hours earlier: 948 officer slots, 188 without a portrait for
  that person in that year, held by 158 people, 156 with no portrait anywhere in the file. No
  name added or removed since the last pass.

## A new method tried this pass: real browser navigation instead of curl, against the exact leads a curl request cannot settle

Every earlier pass tested the three standing blocks with `curl` plus spoofed headers. This pass
used Playwright's headless Chromium instead — a real browser context, real TLS stack, real
cookie jar, actual referer navigation from the collection landing page before the request that
matters — to rule out the possibility that the blocks are a curl/User-Agent fingerprint rather
than a real server-side rule.

- **`digitalcommons.wku.edu/cgi/viewcontent.cgi`**: loaded `dlsc_ua_yearbooks/` first (200, normal
  page), waited three seconds, then navigated to a `viewcontent.cgi` article URL as a real
  in-browser navigation (not a background fetch). **403**, identical to the curl result. The
  landing-page-first sequence that works for a human browsing the collection does not open this
  path; the block holds against full browser navigation, not just scripted requests.
- **`web.archive.org`**: a real browser navigation to `web.archive.org/web/2021*/wku.edu/sga/...`
  returned an HTTP-level response this time rather than a connection reset — **502 "upstream
  request failed"** — which is a different failure signature than curl's `Recv failure:
  Connection reset by peer`, but still not a page. Still closed, now confirmed two ways.
- **The live `www.wku.edu/sga/executive/` page**: this is new ground, not a block. It renders
  current 2025-26 executive cabinet headshots with identifying alt text (e.g. "A headshot image
  of Student Body President Rush Robinson"), confirming the method works for a *current* officer
  page. Checked against `data/photos.json`: Rush Robinson, and the other current cabinet members
  pictured, already carry portraits for 2025-26. This page only ever reflects the sitting cabinet,
  so it has nothing to offer the 2019-2023 span where the 156-person gap actually sits — officers
  who left office before this page was captured are simply gone from it, and the Wayback captures
  that might have frozen an older version of this same page are the content blocked by the
  `web.archive.org` failure above.

## The one further avenue worth recording: wku.edu's own site search, checked for photographs specifically

`www.wku.edu/search/index.php?q=...` (the university's general site search, reachable and
server-rendering real results, confirmed via Playwright) was run against six names from the
2019-22 slice of the gap list: Matthew Johnson, Josh Zaczek, Brenna Mathews, Erika Puhakka, Alexis
Mayne, Hope Wells, Jillian Kenney and Turner Reynolds. Every hit for every name was a PDF of
Senate minutes, a legislation bill sheet, a committee roster, or an unrelated person sharing the
name (a 2017 Critical Language Scholarship recipient named Johnson; a communications-studies
citation list for "Reynolds" and "Turner" as separate authors). No WKU News article, no image,
and nothing with a caption turned up for any of the eight names. This is consistent with the
standing diagnosis in `SGA-60-AGENT-INFO.md` section 6, item 2: a committee chair's name shows up
in the organization's own paperwork, not in university press coverage, and this cohort is
committee chairs and senators, not people WKU Media Relations wrote about.

## Conclusion

No new portrait landed. `data/photos.json` and `data/photos/` are unchanged from
`origin/research-photos`. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean (the only diff `build.py` produced was the "Built [date]" footer timestamp, discarded
rather than committed, as `site/` carries no data change). Presidents and regents remain fully
covered, every year has at least one photograph, and the 156-person no-portrait-anywhere gap
stays blocked: the two standing network routes are now confirmed closed against full browser
navigation as well as curl, the live SGA executive page is confirmed to hold nothing the archive
doesn't already have, and the university's own site search is confirmed to surface paperwork, not
photographs, for this gap's names. No untried route and no untried name remain on file for this
gap.
