# Photograph run, 18 September (morning) — one new portrait, six leads checked and rejected

## Starting state, re-confirmed

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` §4 and §6
before touching anything. `research-photos` was not merged into `main` (`git log
origin/main..research-photos` returned five unmerged commits), so it was reused: checked out from
`origin/research-photos` and `origin/main` merged into it cleanly (a real merge base exists,
`e5bef824`).

Checked the four standing priorities fresh against current `data/years.json` and `data/photos.json`:

- **Priority 1 and 2 (presidents and regents): fully satisfied.** All four named presidents (Nick
  Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) and every other `leaders` entry with
  `role: "president"` or `role: "regent"` across all 61 years already has a portrait, and every
  file checked (`ffd8ffe0`) as a real JPEG.
- **Priority 4 (a photo for every year): satisfied at the minimum bar.** All 61 years carry at
  least one photograph, leader portrait or year-level context image.
- **Priority 3 (cabinet/Senate officers): the open queue.** 218 named executive/Senate-officer
  entries across `organization.executive` and `organization.senate.officers` still carry no
  portrait. This is the same order of magnitude every report this week has found.

## Independently re-confirmed: the same eight 1970s-80s names are still dead ends

Before finding today's applicable `.research/` logs, this run worked archive.org's own
`talisman19NNwest` items for the eight names flagged as still open in
`photo-run-2026-09-17-officer-search.md`: **David Bass** (1977-78), **Vern Pulman** (1974-75),
**David Young, Alice Wicks, Steve Wilson** (1978-79), **Mark Chesnut** (1980-81), **Chris Millay,
Dwight Austin** (1986-87). Reading `.research/photo-run-2026-09-17-officer-search.md` and
`photo-run-2026-09-17-queue-review.md` afterward confirmed this run's findings exactly duplicate
what both already established:

- Bass: 1978 Talisman p. 34, "A LIGHT MOMENT IN AN ASG MEETING" — a candid group photo naming him
  as one of four people, no face distinguishable from the caption alone (a fourth, male figure at
  frame left is mostly out of shot). Left without a portrait.
- David Young: directly quoted in the 1979 Talisman's ASG feature (pp. 288-289) but the spread's
  only photographs are of Steve Thornton and Victor Jackson (both already on file) and a shot of
  newsletters on the floor. No photograph of Young accompanies his quote.
- Wicks, Wilson, Chesnut, Pulman, Millay, Austin: no usable photograph found by name or by the
  back-of-book index in any accessible Talisman year.

Also opened the 1984 Talisman ("The Touch of Red," Wayback capture, article 1408, 198 pages) to
try Kelly S. Smith and John Holland's individual class-portrait grids, a lead the 17 September
wayback-pdfs report left untried. This volume's OCR text layer is present (564,651 characters
total) but badly degraded — text-searching "Holland" or "Chesnut" returns nothing real; a sample
page pulled from a fuzzy "olland" substring match turned out to be unrelated fraternity-housing
copy with no connection to either name. A genuine answer here needs a page-by-page visual read of
the class-portrait section, which this run did not have the budget to do properly (198 pages,
unknown section boundary) — left open rather than guessed at.

**Confirms again**: read `.research/photo-run-<today>-*.md` for a name before spending a Talisman
download or an archive.org search on it. This cost real time before the existing reports were
found.

## New source tried: cross-referencing all 218 missing names against `data/herald-photos.json`

Earlier reports sampled 23 names from 2007-2024 against this local, non-rate-limited index of
21,304 captioned `wkuherald.com` photographs and got no hits. This run ran the *complete* current
list of 218 missing executive/Senate names against it (a fast, offline check) and got ten
substring hits. Checked every one:

- **Jason Heflin** (1997-98, Hillraisers Committee chair). The only hit is a 2015 Herald piece
  about home-brewing, 17 years later, with no connection to his SGA role and too common a name to
  use as identity evidence on its own. Not used.
- **Jessica Williams** (2005-06, Chair, Academic Affairs Committee). The only hit is a 2010 dance
  photo captioned "WKU seniors ... and junior Jessica Williams" — a junior in 2010 could not have
  chaired a committee in 2005-06. Age arithmetic rules this out as the same person. Not used.
- **Chris Jankowski** (Associate Justice, 2010-11 and 2011-12). One hit, in the right timeframe
  (Dec. 2010, "Versailles sophomore Chris Jankowski"), but the caption is about dorm-cleaning-staff
  appreciation, not SGA, and in the photograph his figure is bent over, face down and not visible.
  Even granting the identity, there is no usable face here. Not used.
- **Cody Cox** (Associate Justice 2015-16, Chief Justice 2016-17). One hit, a solo 2014 profile
  photo with strong timeline consistency (freshman in 2014 fits sophomore/junior for the 2015-17
  offices) — but the caption is a personal coming-out story unconnected to his SGA role. Per the
  brief's privacy rule ("archive photographs of people acting in their student government role"),
  repurposing a photo from an unrelated personal-identity feature as his public SGA-officer
  portrait is not appropriate even though it is the right person and an open university-news
  source. Not used, on privacy grounds rather than identification grounds.
- **Mark Clark** (2017-18, Diversity & Inclusion committee chair / Senator at Large). Same
  situation: the only hit is a 2018 photo of him working in the campus Pride Center, unconnected to
  his SGA office. Left out for the same reason as Cox — not an SGA-role photograph.
- **Kayla Distler** (2023-24, senator). The hit is a screenshot of a Change.org petition page (a
  photo of McLean Hall, not of her) that merely names her as the petition's starter. Not a
  photograph of the subject at all. Not used.
- **Jackson Smith** (2025-26, Freshman Senator) — **used.** See below.

## One portrait added: Jackson Smith, 2025-26

The Herald's "SGA supports Go With the Flow program" (12 Nov 2025,
`wkuherald.com/88699/news/sga-supports-go-with-the-flow-program/`) photographs the three Campus
Improvements and Sustainability Committee members who presented the community-umbrellas bill,
captioned "Campus Improvements and Sustainability Committee members Malachi Humble, Jackson Smith
and Ciin Lun present a bill that will obtain funding for community umbrellas in the SGA Office
during the weekly SGA meeting on Tuesday, Nov. 11, 2025 in the Senate Chambers." Confirmed the
caption text against the live article page directly (not just the local index) before using it.

Three people stand at a podium, all in matching SGA polo shirts, and the caption's three names run
left to right exactly as the figures stand: a curly-haired man at the podium (Humble), a man in a
white cap in the middle (Smith), and a woman with long dark hair on the right (Lun, a name
consistent with her appearance). Cropped the middle figure — the only one of the three named in
`years.json` for 2025-26 — as `data/photos/2025-26-jackson-smith.jpg`. This is also the exact
event `years.json` already cites in Smith's own `profile` paragraph ("co-sponsoring a bill to fund
community umbrellas for the Senate office in November 2025 — the Herald's report names him
alongside Malachi Humble and Ciin Lun"), so the identification is corroborated by research already
on file, not new guesswork.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both pass clean after the addition.
`python3 scripts/check_duplicates.py` reports the same four pre-existing same-day-event pairs
noted in earlier reports, all in `years.json` text and out of this agent's scope (photo metadata
only). `python3 scripts/merge_photo_finds.py` (no `--write`) reports zero pending additions and
zero pending improvements; the 18 refused entries are unchanged `FACE PROVED, PERSON NOT PROVED`
flags correctly held for an editor.

## Landing

Committed on `research-photos` as `SGA 60 <kurtztoddsam2@gmail.com>`. Pushed via
`git push -u origin research-photos` (route one — ordinary git push worked; no GitHub-access gate
hit this run).

## Left for the next run

- **1984 Talisman class-portrait grids, unread.** Kelly S. Smith and John Holland (both 1983-84)
  still need a visual, page-by-page read of the People section — text search does not work on this
  volume's OCR. The PDF is at the Wayback capture described in `photo-run-2026-09-17-wayback-pdfs.md`
  (article 1408); this run downloaded it fresh again rather than assuming a prior copy persisted
  container-to-container, and it is not saved anywhere persistent, so the next run will need to
  re-fetch it too unless a shared cache is added.
- **166 cabinet/Senate-leadership names (excluding rank-and-file senators)** still have no
  portrait; this run resolved one. `data/herald-photos.json` is now fully cross-checked against
  the current missing list and re-checking it without new missing names added since is unlikely to
  find anything new.
- The six names rejected above for privacy or identification reasons (Heflin, Williams, Jankowski,
  Cox, Clark, Distler) should not be re-tried against the same sources — the negative reasoning is
  specific to each photo, not to a search technique that might work better next time.
