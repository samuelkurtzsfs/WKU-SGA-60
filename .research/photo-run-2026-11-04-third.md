# Photograph run, 4 November (third scheduled pass): baseline reconfirmed, both standing network
blocks retested unchanged, search-engine method extended to sixteen more officer-gap names

## Priorities 1, 2 and 4, checked directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, as they have since the 20 August run. The
  trigger's stored brief still names them as missing; it has been stale for well over two months.
  (Gilley held the 2008-09 student regent seat, not the presidency — noted in prior passes, not
  re-litigated here.)
- **Priority 2**: `python3 scripts/check_data.py` exits clean — zero presidents or student regents
  without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as every pass since 28 October: 948 officer slots, 188 without a portrait for that
  person in that year, held by 158 people, 156 with no portrait anywhere in the file.

## Network state, retested fresh rather than taken on trust

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, with the navigation headers CLAUDE.md specifies
  (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`) and a
  full browser user agent: `HTTP 403` behind the Cloudflare challenge. Unchanged.
- `archive.org/advancedsearch.php` on `identifier:talisman*west`: re-queried fresh, still exactly
  19 volumes (1943, 1946-47, 1963-65, 1971-81, 1986-87). No new scan reaching the 1990s-2020s
  years where almost all of the remaining gap sits.
- `web.archive.org` direct page fetch: connection reset (`curl: (35) Recv failure`), confirmed by
  the agent proxy status as a closed tunnel to that host specifically. Still closed this session.

## This pass's actual addition: sixteen more names run through the search-engine method

Before touching anything, rebuilt the full 158-name gap list from `portrait_gap.py --any-year`
and checked each name against every `.research/photo-run-*.md` file on this branch (bolded-name
extraction, normalized for middle initials, slashes and parentheticals) to find names with no
prior individual check on record of any kind — not just the search-engine method specifically.
43 names had never been individually named in any prior pass. Picked sixteen of those, favoring
2000s-2020s titles with more online surface area (IT/PR directors, Chief/Associate Justices,
committee heads), and ran each through `WebSearch` restricted to `wku.edu`, `wkuherald.com`,
`digitalcommons.wku.edu` and `bgdailynews.com`:

Christopher Jankowski, Hunter Sprowles, Monique Gooch, Samantha Hughey, Sarah Howell, Rachel
Keightley, Jessi Wurth, Jeremy Glass, Matthew Johnson, Hope Wells, Caroline Simpson, Lane
Simpson, Ian Hamilton, Dajana Crockett, Kara Raley, Kelly Simmons.

Results, all negative for a photograph:

- **Christopher Jankowski** (Chief Justice, 2012-13): confirmed by a cached August 2012 Judicial
  Council ruling PDF (`wku.edu/sga/uploads/judicial/8-28_attendance.pdf`) written on his
  authority — "Written by Chief Justice Chris Jankowski to represent ... a unanimous 5-0 vote."
  Text only, no image.
- **Hunter Sprowles** (Chair, Public Relations Committee, 2005-06): no hit of any kind. The only
  similarly-named officer on record is a different person, "Jonathan/Jonathon Sprowles," Director
  of Public Relations around 2007 — not the same title or year as this gap entry, and the search
  does not establish them as the same person either way.
- **Monique Gooch** (Director of Public Relations, 2008-09): no hit of any kind.
- **Samantha Hughey** (Director of Information Technology, 2007-08): one undated SGA webpage
  names her in the role ("Director of Information Technology: Samantha Hughey. I am open to
  suggestions about the web site.") — text only, no image, no date on the page itself.
- **Sarah Howell** (Director of Information Technology, 2009-10): confirmed by the 20 October 2009
  Senate minutes, consistent with the gap entry's year. She is a different person from the
  WKU ITS staff member of the same name found on the university's current IT-services staff
  directory — that page is a current employee listing, not a photograph of her acting in an SGA
  role, and CLAUDE.md's rule is to archive people in their student-government capacity, not
  pull an unrelated current staff headshot, so it was not used even though it is on wku.edu.
- **Rachel Keightley** (Director of Information Technology, 2015-16): no hit of any kind.
- **Jessi Wurth** (Director of Public Relations, 2010-11): no hit of any kind.
- **Jeremy Glass** (Director of Information Technology, 2007-08 — recorded on some legacy pages
  as "Director of Technology"): confirmed by the fifth Senate's 22nd meeting minutes, March 2007,
  which list him present under that title and reporting a website problem. Text only, no image.
- **Matthew Johnson** (Academic and Student Affairs Committee Head, 2019-20): confirmed by SGA
  Senate minutes (filed under a 2018-2019/sp20 path, so the exact meeting date needs independent
  confirmation) speaking in favor of a Tree Campus USA bill in that capacity. Text only, no image.
- **Hope Wells** (SAVES Committee Head, 2019-20): confirmed as a bill co-author and SAVES
  Committee member across several 2018-19 bills and a Herald quote criticizing SGA's response to
  a campus speaker controversy. All text; no photograph on any of the pages the search surfaced.
- **Caroline Simpson** (Associate Justice, 2018-19) and **Lane Simpson** (Associate Justice,
  2016-17 — recorded in the gap list as "Lane (Caroline) Simpson"): neither name search turns up
  any WKU SGA or Judicial Council record under either form. The only "Caroline Simpson" hits are
  unrelated people (a 2019 WKU alumna now in Nashville; a Belmont University student; a different
  "Lindsey Caroline Simpson" on a 2024 dean's list), and the only "Lane Simpson" hits are South
  Warren High School honor-roll items with no WKU or SGA connection. Nothing to attach either way.
- **Ian Hamilton** (Gordon Ford College of Business Senator, 2016-17): no hit of any kind. The
  search surfaced several other, later holders of the same seat (Tyreesha Morris, Carter Smith,
  Karlee Powell, Connor Ferguson) but nothing naming Hamilton.
- **Dajana Crockett** (Justice, Judicial Council, 2009-10): no SGA-connected hit. The only
  "Dajana Crockett" result is a 2010 Warren County dean's/president's list entry, which does not
  establish the same person and carries no photograph regardless.
- **Kara Raley** (Justice, Judicial Council, 2013-14): no hit of any kind.
- **Kelly Simmons** (Justice, Judicial Council, 2012-13): no hit of any kind.

None of the sixteen surfaced a captioned photograph. All sixteen remain in the gap list; the
ones with a text confirmation (Jankowski, Hughey, Howell, Glass, Johnson, Wells) corroborate the
`organization` records already in `data/years.json` but add nothing photographic.

## Conclusion

No new portrait landed this pass. `data/photos.json` and `data/photos/` are unchanged from
`origin/research-photos`. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean; the only `site/` diff was the build-date line, reverted before committing. Both
standing network blocks (digitalcommons PDF endpoint, archive.org's fixed 19-volume Talisman
catalogue) are unchanged; `web.archive.org` is closed again this session. The officer-portrait
gap stands at 158 people, 156 with no portrait anywhere in the file; sixteen more of those names
now have a search-engine pass on record (70 of 158 total across all passes), all negative for a
photograph specifically.
