# Photograph run, 18 November (second scheduled pass): baseline reconfirmed, no new portrait

## What this pass checked

Before touching the officer gap, reconfirmed the priority order in CLAUDE.md programmatically
against the current `data/years.json` and `data/photos.json`:

- The four presidents named as having no portrait at all (Nick Todd, Katie Dawson, Jeanne
  Johnson, Reagan Gilley) all already carry a `leaders` entry in `data/photos.json`, each with a
  captioned source (Nick Todd: Herald "Election Guide 2004", 16 Mar 2004; Katie Dawson: Daily
  News, 31 Mar 2006; Jeanne Johnson: Herald commencement edition, 1 May 2008, captioned "Jeanne
  Johnson, President, Student Government Association"; Reagan Gilley: Herald 84:35, 26 Feb 2009,
  p. 1). Confirmed the JPEG magic bytes on all four files.
- Every president and every student regent in `years.json` has a same- or other-year portrait in
  `photos.json` (checked against the whole file, not a sample: zero missing of either role).
- All 61 years carry at least one `years`-level photograph entry.

So the only open ground left under CLAUDE.md's own priority order is executive-cabinet and
Senate-officer portraits (priority 3) and additional general photographs (priority 4).

## Independent sample, then cross-checked against this branch's own history

Worked a sample of the officer gap from `scripts/portrait_gap.py --any-year` directly against
primary sources before reading this branch's `.research/` log, to get an independent read:

- **Mark Chesnut**, treasurer 1980-81 — traced the 1981 *Talisman* index entry ("Chesnut, Mark
  Cameron 234") to leaf 238 via the item's own `talisman1981west_page_numbers.json`, fetched that
  page image directly from `archive.org`'s BookReaderImages endpoint, and confirmed it is the
  men's intramurals results page: "Mark Chestnut (Sigma Alpha Epsilon)" won a badminton title,
  with no portrait of him on the page. The action photograph beneath has no caption naming
  anyone pictured.
- **David Young**, administrative vice president 1978-79 — found and read the two-page ASG
  spread in the 1979 *Talisman* (pp. 288-289, via the same leaf-lookup method): the only
  individually captioned figure is president Steve Thornton (already in `photos.json`, same
  source); Young is quoted in the body text on p. 289 about the new 24-seat ASG constitution but
  not pictured or captioned anywhere in the spread.

Both are exhausted leads. Reading this branch's own `.research/photo-run-2026-11-18-scheduled.md`
(filed earlier today) afterward, both were checked there too, independently, with the same
result, down to the same page numbers — as were Alice Wicks, Steve Wilson, Chris Millay and
Dwight Austin. `scripts/portrait_gap.py --list --any-year` and a search across every
`.research/photo-run-*.md` and `data/photo-finds/*` file show that essentially every name
remaining in the 155-person any-year gap has already been run down at least once, several of
them (ShyAnte'e Williams, the 2025-26 judicial council, the four unphotographed 2025-26 senators)
repeatedly within the last week. The one concrete lead flagged as actionable-but-unlanded on 14
November — Sophie Stirling and Hannah Hash's SGA-site headshots, pending their addition to
`years.json`'s 2025-26 organization block — is no longer open: both are now in that block and
both already carry `photos.json` portraits from the Herald (Stirling: 5 Apr 2026 Senate Chambers
caption; Hash: 11 Nov 2025 Senate Chambers caption), along with Maggie Phelps and Kaden
Blankenship, so that lead has already been converted since it was logged.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `python3 scripts/build.py`
and `python3 scripts/check_data.py` both pass clean against the unchanged data. The remaining
gap is not a backlog of unexamined names; it is a set of people the digitised Herald, the
Talisman volumes on archive.org, and the Wayback-archived wku.edu/sga simply never photographed,
or photographed without a caption this project's rules allow it to use. Landed on
`research-photos` with only this note, so the next pass does not re-walk the same ground without
knowing it has already been walked.
