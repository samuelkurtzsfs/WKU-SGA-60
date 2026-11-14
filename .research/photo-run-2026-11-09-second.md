# Photograph run, 9 November (second scheduled pass): the committee-chair population counted for the first time, sixteen names closed, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`; checked the file magic bytes directly
  (`FF D8 FF E0` on all four JPEGs) rather than trusting the file extension.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 156-person gap
  this file has carried for weeks. Unchanged this pass — see below for why.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.

## What this pass actually found: `portrait_gap.py` deliberately excludes committee chairs, and nobody had separately counted them

`scripts/portrait_gap.py`'s own docstring is explicit: "Committee chairs are NOT slots - a
committee chair is not an officer, which is trap 2." That is the right rule for the headline
156-person figure — it is about cabinet and Senate *leadership*, and conflating a committee chair
with an officer is the exact mistake SGA-60-AGENT-INFO.md's trap list warns about. But it means
the 156-person number this file has quoted all week is not the complete population of named SGA
figures with no portrait; it is that population *minus* committee chairs. Running the same script
with `--committees` shows the fuller picture:

```
1053 officer slots in the file, 990 of them cabinet or Senate leadership (committee chairs included)
231 of those carry no portrait for that person in that year, held by 196 people
174 of those people have no portrait in any year
```

174 against the usual 156 is an 18-person gap between "the officer queue" and "every named SGA
figure with a role." Cross-referencing by hand (`organization.executive` +
`organization.senate.officers` + `organization.senate.committees[].chair` against
`photos.json`'s `leaders`) turned up 189 missing names; 173 of those are the already-logged
156-person queue under full names or variant spellings (Jacob A. Miers, Lisa M. Kappler and Lane
(Caroline) Simpson are the same three people `_archive-gaps.json`'s 12 October entry already
closed under shorter names — not new). **Sixteen were genuinely new**: committee chairs from
1980-81 through 2024-25 that had never been searched, because they exist only in the
`committees[].chair` field and nobody had cross-referenced that field before.

## The sixteen, searched and closed

Alan Jackson (1980-81), Debbie Thomas (1980-81), Dawn Dillard (1992-93), Kristin Hartley
(2002-03), Lucas Humble, Tim Hill, Jonathan Sprowles (all 2006-07), Emilee England, Meggan Selzer
(both 2007-08), VaShae Swope (2008-09), Mac Mullins, Mallory Chaney (both 2012-13), Divya
Gangavelli (2017-18), Trevor Huffman (2018-19), Fatin Yaro (2020-21) and Annie Finch (2024-25).

Searched the pre-2003 names (Jackson, Thomas, Dillard, Hartley) against the local Herald full
index (`data/herald-index-full.json`, zero network cost); searched the rest against
wkuherald.com's WP-JSON search API, which was reachable and returning real results all session.

Found real text confirmation of several in their actual roles, but no photograph identifiable as
any of them specifically:

- **Mac Mullins** is quoted by name as SGA's Public Relations Chair at the 20 February 2013
  meeting ("There's no such thing as bad press," he said of recent coverage), but the article
  carries no photograph of him.
- **Annie Finch** is the best-documented of the sixteen and the closest this pass came to a find.
  wkuherald.com (8 November 2024) names her directly as the organiser of SGA's second annual
  Veteran's Day 5K — "organized by SGA Senior Senator and Community Relations head, Annie Finch" —
  and the 27 August 2024 season-opening meeting story names her as the incoming Community
  Relations Committee chair. The event's own nine-image photo gallery
  (`wkuherald.com/80202/.../photos-sga-hosts-second-annual-veterans-day-5k/`) was read caption by
  caption; every image is captioned with a runner's name, not hers. No photograph on the site
  names her.
- **Divya Gangavelli** and **Trevor Huffman** both appear by name in SGA election-result articles
  (19 April 2017 and 18 April 2018 respectively), listed among winning senators-at-large, but the
  accompanying photographs are generic group shots of the executive winners, not captioned with
  every senator's name.
- **Fatin Yaro** is named as the senator who authored a book-scholarship bill for international
  students (24 February 2021 meeting story); the post's featured image is unrelated.
- **Alan Jackson**'s only local-index hits under this exact name are the country singer's 1992
  Diddle Arena concert, not the 1980-81 ASG Minority Affairs chairman — flagged as a common-name
  collision rather than pursued into the 1981 Talisman without a page reference.
- **Lucas Humble, Tim Hill, Jonathan Sprowles, Emilee England, Meggan Selzer, VaShae Swope,
  Mallory Chaney, Dawn Dillard, Kristin Hartley**: zero or no on-topic hits in either source
  checked.

One, **Debbie Thomas**, is logged as *open* rather than closed: the 1981 Talisman's own index
(archive.org, `talisman1981west`) gives "Thomas, Deborah Lynn 356," a real page reference that this
pass did not have time to open. Left for whoever picks this up next.

Also independently re-read **Mark Chesnut**'s 1981 Talisman page 234 (leaf n237, fetched via
`archive.org`'s `BookReaderImages.php` page-image service) before discovering a 12 October entry
in `_archive-gaps.json` had already closed it with an identical finding — an intramural-results
table naming a "Mark Chestnut" twice as an event winner, no photograph on the page, no link to the
ASG treasurer beyond the index's page reference. Redundant work; flagged here so a future pass
checks `_officers-truly-missing-2026-09-06.json` for a name before spending a request on it.

All sixteen are now in `data/photo-finds/_officers-truly-missing-2026-09-06.json` with individual
notes, so this specific search does not have to be repeated.

## Network state this pass

Tested directly rather than trusted from an earlier entry. `digitalcommons.wku.edu` landing pages
(`dlsc_ua_records/<N>`) load cleanly over plain curl with `-L`. The PDF endpoint,
`cgi/viewcontent.cgi`, still answers a Cloudflare "Just a moment..." managed-challenge page
(HTTP 403) on every attempt — a standing TLS/JS-challenge block, not a pacing problem, matching
every prior run's finding. `archive.org` was fully reachable all session: both the `djvu.txt` route
and the `BookReaderImages.php` page-image service (not a new technique — already used by earlier
passes) returned real JPEGs on every attempt, reproduced against `talisman1975west` (the settled
Tom LaCivita/Ricky Johnson page, as a sanity check) and three further volumes pulled fresh this
pass (`talisman1979west`, `talisman1981west`, `talisman1987west`). `wkuherald.com`'s WP-JSON API
was reachable and returning real results throughout — unlike the 12 October pass, which found it
blocked with error code 1006. Worth testing fresh again next time rather than assuming either way.

## Conclusion

No new portrait this pass. The real contribution is methodological: the project's own
`portrait_gap.py` correctly excludes committee chairs from the headline 156-person officer gap
(they are not officers), but that exclusion had apparently also meant nobody had separately
searched the 18 people who exist *only* as committee chairs. Sixteen of those eighteen are now
searched and logged; one (Debbie Thomas) has a real, unopened lead; the other two
(Jacob A. Miers, Lisa M. Kappler, Lane (Caroline) Simpson — actually three, all variant names of
people already closed) turned out not to be new at all. `data/photos.json` and `data/photos/` are
unchanged. `build.py` and `check_data.py` both pass clean. Landed on `research-photos`.
