# Photograph run, 4 November (scheduled): baseline reconfirmed, both standing network
blocks retested unchanged, search-engine method extended to sixteen more officer-gap names

## Priorities 1, 2 and 4, checked directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, as they have since the 20 August run. The
  trigger's stored brief still names them as missing; it has been stale for over two months.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — "the archive checks out against
  its own rules" — zero presidents or student regents without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as every pass since 28 October: 948 officer slots, 188 without a portrait for that
  person in that year, held by 158 people, 156 of whom carry no portrait anywhere in the file.

## Network state, retested fresh rather than taken on trust

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, with the navigation headers CLAUDE.md specifies
  (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`) and a
  full browser user agent: `HTTP 403` behind a Cloudflare "Just a moment..." challenge. Unchanged
  since 25 August.
- `digitalcommons.wku.edu` ordinary item/landing pages (e.g. `/dlsc_ua_records/593/`): `HTTP 200`.
  Read one all the way through: its own `bepress_citation_pdf_url` meta tag points straight back
  at the blocked `cgi/viewcontent.cgi` endpoint, on the same host, with no alternate CDN or S3
  path for the underlying file. There is no bypass through the landing page; the block is the PDF
  endpoint specifically, and every route to the actual image or page scan still crosses it.
- `digitalcommons.wku.edu/talisman/` and `/do/search/` (collection root and on-site search):
  `404`/`403` respectively. Neither is the right path for browsing Talisman by issue, and neither
  bears on the PDF block either way.
- `archive.org/advancedsearch.php`: `HTTP 200`. Re-queried `identifier:talisman*west` fresh: still
  exactly 19 volumes (1943, 1946-47, 1963-65, 1971-81, 1986-87). No new scan has been added that
  would reach the 1990s-2020s years where almost all of the 156-name gap sits.
- `web.archive.org`: a direct page fetch reset the connection (`curl: (35) Recv failure`), and the
  CDX endpoint answered `403 Blocked by egress policy` outright. Both still closed this session,
  reversing the 30 October finding that direct fetches had reopened — this route swings between
  passes and should keep being retested rather than assumed either way.
- `wkuherald.com`'s WP-JSON endpoint: open, `200`. Checked the ten most recent SGA-tagged posts;
  nothing past 3 November's graduation-regalia story and 20 October's "Pink Out" session piece,
  both already read for captions (the Pink Out photo is an uncaptioned group shot; the regalia
  photo is an unrelated file photo). Nothing new to attach.

## This pass's actual addition: sixteen more names run through the search-engine method

Checked the full `.research/` corpus against every one of the 158 names in the current gap list
before touching anything, counting how many prior reports mention each by name. Picked the
sixteen with the fewest prior mentions that had not already had the `WebSearch` tool (as opposed
to a direct `curl`/WP-JSON crawl) run against them specifically, restricted to `wku.edu`,
`wkuherald.com`, `digitalcommons.wku.edu` and `bgdailynews.com`:

Derek/Derrek Duncan, Jacob A. Miers, Jeff Baker, Jeff Baynham, Jenny Stith, Matt Bogard, Sally
Eilerman, Tim Hatton, Abigail Potter, Amber Daniels/Daniel, Bonnie Newton, Grace Hancock, Joe
Murrell, Lisa M. Kappler, Stacey Schepers, Tony Wong.

Results, all negative for a photograph:

- **Derek Duncan** (Chairperson, Legislative Research Committee, 1993-94 — also recorded as
  "Derrek Duncan"): no hit of any kind, current or archival.
- **Jacob A. Miers** (Secretary of the Senate, 2007-08/2008-09): confirms an October 2007 Senate
  minutes mention and a February 2008 "Reflections on Frankfort Rally" document, neither carrying
  an image.
- **Jeff Baker** (Parliamentarian, 1994-95): no hit; predates `wkuherald.com`'s roughly-2003 floor
  and archive.org's Talisman coverage, which stops at 1987.
- **Jeff Baynham** (Parliamentarian, 1998-99): a February 1998 SGA minutes mention and an
  unconnected WKU Archives personal-papers listing under the same surname; no image, no
  confirmation the two "Baynham"s are the same person.
- **Jenny Stith** (Chairperson, Public Relations Committee, 1997-98 / Justice, Judicial Council,
  1998-99): a February 1998 minutes mention as PR chair, and a separate undated Herald piece
  quoting an "Elizabethtown sophomore Jenny Stith" on a Coming Home dorm-decorating plan. Text
  only; no caption, no photograph.
- **Matt Bogard** (Chairperson, Campus Improvements Committee, 1998-99): the only "Matt Bogard"
  result is a different person — a WKU Libraries facilities specialist and later enrollment-
  research staffer, giving a 2008 economics presentation unconnected to SGA. No lead.
- **Sally Eilerman** (Co-Chair, Hillraisers Committee, 1998-99): two SGA minutes mentions (a
  Public Relations vice-chair nomination; a 26 January 1999 note on running the Hillraisers
  basketball-season effort), both text only.
- **Tim Hatton** (Chairperson, Student Affairs Committee, 1998-99): a 1999 minutes mention as
  "Chairman Hatton" on a Camp Fair, and a c.2000-01 resolution listing him among the members
  signing a request to retain VP of Student Affairs Jerry Wilder. Neither carries an image.
- **Abigail Potter, Bonnie Newton, Grace Hancock, Joe Murrell, Stacey Schepers, Tony Wong**: zero
  hits of any kind connecting any of the six to an SGA role, current or archival, under the
  restricted domains.
- **Amber Daniels/Daniel** (Judicial Council Member, 1994-95 — distinct era from the 2015-16
  Associate Justice "Amber Daniels" the Judicial Council's own 2015 opinion names): the only hits
  are that unrelated 2015-16 Associate Justice and an undated SGA judicial-branch page, neither
  reaching the 1994-95 officer this gap entry is actually about. No image either way.
- **Lisa M. Kappler**: one SGA minutes mention as the author of a bill, speaking to a funding
  request; no date, no title, no photograph.

None of the sixteen surfaced a captioned image. The 1994-99 names remain unreachable by
`wkuherald.com` (predates its ~2002-03 floor) and by archive.org's Talisman text (stops at 1987);
only the still-blocked `cgi/viewcontent.cgi` route could reach them.

## Conclusion

No new portrait landed this pass. `data/photos.json` and `data/photos/` are unchanged from
`origin/research-photos`. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean; the only `site/` diff was the build-date line, reverted before committing. The
digitalcommons PDF endpoint stays blocked, the Talisman catalogue on archive.org is unchanged at
19 volumes, and `web.archive.org` is closed again this session after briefly reopening on
30 October. The officer-portrait gap stands at 158 people, 156 with no portrait anywhere in the
file. Sixteen more of those names now have a search-engine pass on record, all negative for a
photograph specifically.
