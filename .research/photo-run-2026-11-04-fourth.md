# Photograph run, 4 November (fourth scheduled pass): baseline and both standing network
blocks reconfirmed unchanged, eighteen more officer-gap names checked by two different
methods, no new portrait

## Priorities 1, 2 and 4, checked directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, unchanged since 20 August. The trigger's stored
  brief still names them as missing; it has been stale for well over two months.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — zero presidents or student regents
  without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as every pass since 28 October: 948 officer slots, 188 without a portrait for that
  person in that year, held by 158 people, 156 of whom carry no portrait anywhere in the file.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, same navigation headers CLAUDE.md specifies and a
  full browser user agent: `HTTP 403` behind the Cloudflare challenge. Unchanged since 25 August.
- `archive.org/advancedsearch.php` on `identifier:talisman*west`: still exactly 19 volumes (1943,
  1946-47, 1963-65, 1971-81, 1986-87). No new scan reaching the 1990s-2020s years where almost all
  of the remaining 156-name gap sits.
- `web.archive.org` direct page fetch: connection reset (`curl: (35) Recv failure`). Still closed
  this session.
- `wkuherald.com`'s WP-JSON endpoint: open, `200`.

## This pass's addition: two methods, eighteen names total

**Method one — direct WP-JSON article lookup.** Rather than the `WebSearch` tool used in every
prior pass, queried `wkuherald.com/wp-json/wp/v2/posts?search=<name>` directly for five recent
gap names (Kayla Distler, Connor Ferguson, David Darnell, Callison Padgett, Justin Goins — via
the election-results and committee-selection articles their names turned up in) and then pulled
the `featured_media` entry for the matching articles and read its `caption`/`alt_text` field
directly, rather than trusting a WebSearch snippet. Confirmed all five named in article body text
(election results, committee-head announcements), consistent with their `organization` entries.
In every case the attached photograph's caption described a generic meeting or group scene
("Members of the WKU Student Government Association executive cabinet listen to proposals...",
"They met in the SGA chambers...") with no individual named — the same pattern the 20 October
"Pink Out" check already found. CLAUDE.md requires the caption or adjoining text to identify the
subject; a stock chambers photo captioned only with the meeting's date does not meet that bar
for any of the five, so none was used.

**Method two — `WebSearch` restricted to `wku.edu`, `wkuherald.com`, `digitalcommons.wku.edu` and
`bgdailynews.com`**, on thirteen names not covered by method one or by any prior pass's named
checks: Justin Goins, Erika Puhakka, Elizabeth DeLozier, Tribhuwan Singh, Turner Reynolds, Alexis
Mayne, Nicole Massarone, Zachary Skillman, Jesse Banales, Brenna Mathews, Josh Zaczek, Jillian
Kenney, Cassidy Townsend, Mark Clark, Smita Peter, Ryan Richardson, Cody Cox, Hayden
Skinner-Fine, Abhishek Bose, Morgan Wysong (nineteen in total; Goins overlaps both methods).

Results, all negative for a photograph:

- **Justin Goins** (Chief Justice, 2022-23): confirmed by a spring 2023 SGA election packet
  (listed as the contact Chief Justice) and the Herald's election-results story, which has him
  reading results to the Senate. Both text only.
- **Erika Puhakka**: no WKU/Herald/Daily News source names her in any SGA role at all under
  these domains — the search returned only other chief justices (Sophie Stirling, Kelsey
  Luttrell). She is named only as a bill co-author in a separate record (Josh Zaczek's
  constitutional-amendment co-authorship, 21-19-S); that is consistent with the gap entry but
  adds nothing photographic.
- **Elizabeth DeLozier**: confirmed as Secretary of the Senate (Feb 2022 agenda), as a 2022
  Health & Human Services senator, and as Legislative Operations committee chair (Sept 2022).
  All text; no accompanying image in any of the three records.
- **Tribhuwan Singh** (Director of Enrollment and Student Experience, 2021-22): confirmed by a
  September 2021 Herald profile describing his platform and prior role as a sophomore senator.
  Text only — no photograph in the article as indexed.
- **Turner Reynolds**: the only hit places him as a Judicial Council nominee (undated, roughly
  2,600 days old per the search) alongside Jason Herlick, Derek Collins and Holden Schroeder; it
  does not confirm the Associate Chief Justice title the gap entry carries. No image either way.
- **Alexis Mayne**: no hit of any kind under these domains.
- **Nicole Massarone**: one hit, a September 2021 Herald "newly elected members" piece naming her
  as a Judicial Council member and legal-studies major; text only.
- **Zachary Skillman** (Campus Improvements and Sustainability Committee Head, 2021-22): confirmed
  by a 2021-22 legislative packet naming him as committee head and listing Bill 6-22-S under his
  name. Text only.
- **Jesse Banales**: the only hit ties him to a Diversity, Equity and Inclusion Workgroup listing
  in a 2021-22 resolution packet, not the Gordon Ford senate seat the gap entry names. No image.
- **Brenna Mathews**: no hit of any kind under these domains.
- **Josh Zaczek** (Legislative Research Committee Head, 2019-20): confirmed across several 2018-20
  Senate minutes and legislation sponsorships, and a 2022 Bowling Green Daily News career item
  (hired to lead workforce participation) — all text, no photograph.
- **Jillian Kenney**: the only "Jillian Kenney" hit under these domains is an unrelated ~2,800-day-
  old WKU News piece about an alternative-break trip participant; nothing ties her to SGA.
- **Cassidy Townsend** (SAVES Committee Chair, 2018-19): a 2018 candidate packet places her on
  SAVES and Diversity & Inclusion committees and as a Senator-at-Large, and the legislation
  archive lists her as a bill author, but no source explicitly confirms the "Chair" title in the
  gap entry, and none carries an image.
- **Mark Clark**: legislation records list him as a bill author/member under the Committee for
  Diversity & Inclusion in 2018-19, not as its chair (later chairs on record are Megan Farmer and
  Ahatali Tahiri, undated). No image either way.
- **Smita Peter** (Director of Information Technology, recorded 2016-17/2017-18): confirmed by
  November 2017 Senate minutes. Text only.
- **Ryan Richardson** (Speaker of the Senate, 2017-18): confirmed by April 2017 minutes (approved
  unanimously) and November 2017 minutes (presiding over a meeting), plus a Herald piece calling
  him "Speaker of the House" on an academic-freeze proposal. All text.
- **Cody Cox** (Chief Justice, recorded 2016-17): confirmed by April 2017 minutes (a constitutional
  ruling) and an October Herald story on a racism complaint he received and referred to the
  council. Text only, no photograph in either source as indexed.
- **Hayden Skinner-Fine**: confirmed on an undated SGA judicial page and a 2015 Judicial Council
  opinion PDF as an associate justice. Text only, no image.
- **Abhishek Bose** (Director of Information Technology, 2016-17): confirmed by an SGA Executive
  Cabinet page for that year and April 2017 minutes. Text only.
- **Morgan Wysong**: 2017 Senate reports place the name under Public Relations and, separately,
  the Student Publications Committee, but no source calls Wysong the PR committee chair the gap
  entry's title implies. No image either way.

None of the eighteen (nineteen counting the method-one/method-two overlap on Goins) surfaced a
captioned photograph of the subject. All remain in the gap list. Several (Puhakka, DeLozier,
Singh, Mayne, Mathews, Kenney) returned thin or no results even for text confirmation, which is
consistent with this being a genuinely under-documented slice of the record rather than a search
failure — the committee/cabinet rosters these titles come from often have no Herald coverage at
all, only an SGA minutes or legislation-packet mention.

## Conclusion

No new portrait landed this pass. `data/photos.json` and `data/photos/` are unchanged from
`origin/research-photos`. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean; the only `site/` diff was the build-date line, reverted before committing. Both
standing network blocks (digitalcommons PDF endpoint, archive.org's fixed 19-volume Talisman
catalogue) and the closed `web.archive.org` route are unchanged. The officer-portrait gap stands
at 158 people, 156 with no portrait anywhere in the file; eighteen more of those names now have
an individual check on record (88 of 158 total across all passes to date), all negative for a
photograph specifically. The remaining gap is now visibly concentrated in titles whose only
surviving record is a Senate-minutes line or a legislation-packet author credit — categories this
archive's three open sources (digitalcommons PDF endpoint, archive.org Talisman, web.archive.org)
are all currently unable to reach for verification beyond text.
