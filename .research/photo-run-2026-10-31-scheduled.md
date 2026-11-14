# Photograph run, 31 October (scheduled pass): search-engine method extended to twelve more officer-gap names, Herald photo galleries checked directly, no new portrait

## Priorities 1, 2 and 4, checked directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, as they have since the 20 August run. The
  trigger's stored brief still names them as missing; it has been stale for over two months.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — "the archive checks out against
  its own rules" — zero presidents or student regents without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as the last several passes: 948 officer slots, 188 without a portrait for that
  person in that year, held by 158 people, 156 with no portrait anywhere in the file.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, with the navigation headers CLAUDE.md specifies:
  `HTTP 403`. Unchanged.
- `digitalcommons.wku.edu/talisman/` (plain index path): `HTTP 404` — this path itself isn't the
  right one on this host; it doesn't bear on the PDF endpoint block, which is the one that matters.
- `archive.org/advancedsearch.php`: `HTTP 200`. Queried the full Talisman catalogue
  (`identifier:talisman*west`) fresh rather than trusting the earlier count: still exactly 19
  volumes — 1943, 1946-47, 1963-65, 1971-81, 1986-87. No new scan has been added that would reach
  the 1990s-2020s years where nearly all of the 156-name gap sits. (It also doesn't cover 1966-70
  or 1982-85, so the handful of gap names in 1966-67/1967-68/1969-70 were never reachable by this
  route regardless.)
- `web.archive.org` direct page fetch: `HTTP 302` (redirect to the resolved snapshot), consistent
  with the 30 October finding that direct fetches work again while the CDX/index endpoints stay
  blocked at this session's egress policy.

## This pass's actual addition: the search-engine method, run against twelve names not in the 23 already logged in the PR body

The rolling PR description records 23 of the 158 names as already run through WebSearch
restricted to wku.edu, wkuherald.com, digitalcommons.wku.edu and bgdailynews.com. Checked the
`.research/` corpus first so this pass wouldn't repeat that work: all twelve of the following
already had deep Talisman/minutes/Herald-index search histories (3-17 prior files apiece) but no
record of having been run through the search-engine method specifically. Ran it on each:

Cody Cox, Nathan Cherry, Justin Goins, Turner Reynolds, Mark Clark, Ryan Richardson, Garrett Baum,
Elizabeth DeLozier, Liz Goddard (re-run — the PR's own "partial lead"), Matt Holland, Stuart
Kenderes, David Spalding.

Every one of these turned up confirmation of the office and term already on record (SGA minutes,
legislation sponsor lines, Herald news text) — useful corroboration for whichever routine owns
`organization`, but exactly what the last several passes already found for the other 23: text
confirmation, never a photograph. Full detail per name:

- **Cody Cox**: April 2017 Senate minutes name him Chief Justice. No photo.
- **Nathan Cherry**: Speaker of the Senate, spring 2017; also 2015-17 Colonnade Committee rep. No photo.
- **Justin Goins**: Chief Justice through the 2022-23 election; presided over the Bornefeld
  censure case. No photo in any of the Herald pieces that name him.
- **Turner Reynolds**: a Herald piece on a four-justice slate of Judicial Council nominations
  describes her (sophomore, communications/media major, Panhellenic Delegate) in prose, but
  the article carries no photograph of the nominees.
- **Mark Clark**: legislation sponsor on several 2018-19 Diversity & Inclusion Committee bills.
  No photo; no title confirmed either.
- **Ryan Richardson**: Speaker of the Senate 2017-18, confirmed in two sets of minutes. No photo.
- **Garrett Baum**: only turns up as a bill author line ("Junior Senator"), not as Associate
  Justice — the title in this archive's gap list may predate or postdate that record. No photo.
- **Elizabeth DeLozier**: Secretary of the Senate, 21st Senate (named alongside Speaker Tess
  Welch), after an April 2021 election as a College of Health and Human Services senator. No photo.
- **Liz Goddard**: re-checked the 2008 banquet lead directly. It does not hold up — no Daily News
  or Herald result ties her to the SGA awards banquet at all; the only "Goddard" hit in Herald
  archives is a 1998 byline, "Goddard, Holly," a different person. Dropping this lead; it was
  never more than a title match in a snippet.
- **Matt Holland, Stuart Kenderes, David Spalding**: no source ties any of the three to the
  Judicial Council office this archive's `organization` block gives them, let alone a photograph.
  (Kenderes does show up in October 2007 Senate minutes as a member asking questions — consistent
  with, not contradicting, the gap entry — just with no title and no photo attached.)

## Checked three current Herald articles directly for photo galleries, since current-decade pieces run photos most often

Fetched the full pages (not just search snippets) of three stories the searches above surfaced as
likely to carry named cabinet/committee photos:

- `wkuherald.com/72365/.../wku-student-government-association-selects-judicial-council-committee-heads/`
  (30 Aug 2023): one photo, of the chamber generally, captioned with no names. The committee
  chairs and Judicial Council nominees are named in the article text only.
- `wkuherald.com/65821/.../gallery-sga-results-announced-cole-bornefeld-wins-presidency/`: the one
  SGA-specific photo on the page is already on file — Sam Kurtz and Cole Bornefeld calling their
  mothers after the April 2022 election, captioned by name. No photo of Elizabeth DeLozier or any
  other senator on the page.
- `wkuherald.com/96580/.../sga-kicks-off-60th-year-on-campus-swears-in-new-committee-chairs/`
  (25 Aug 2026): the swearing-in photo's caption names only President Caden Lucas, who is shown
  taking a photo of the group — the nine incoming chairs it lists in text (Jade Ismail, Tyreesha
  Morris, Amelia Tucker, Landon Terry, Jackson Smith, Ethan Vietze, Gabi Pace, Elizabeth Allen,
  Molly Ricke) are not individually identified in any caption. One other photo on the same page,
  of Carter Smith being sworn in 22 Sep 2026, is already in `data/photos.json`.

## Conclusion

No new portrait landed this pass. `data/photos.json` and `data/photos/` are unchanged from
`origin/research-photos`. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean; the only `site/` diff was the build-date line, reverted before committing. The
digitalcommons PDF endpoint stays blocked, the Talisman catalogue on archive.org is unchanged at
19 volumes, and the officer-portrait gap stands at 156 people with no portrait anywhere. Twelve
more of those 158 names now have a search-engine pass on record (35 of 158 total), all negative
for a photograph specifically; one previously-logged "partial lead" (Liz Goddard) was checked
again and does not hold up, and is dropped.
