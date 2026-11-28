# Photograph run, 20 November (scheduled): baseline reconfirmed, no untried lead found

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: every president and every student regent in `data/years.json` has a portrait
  (`check_data.py`: "60 people have been president", all with portraits; checked programmatically
  against the whole file, not sampled).
- **Priority 4**: all 61 years carry at least one `years`-level photograph entry.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same shape as every
  pass since mid-November — 187 cabinet/Senate leadership slots with no same-year portrait (157
  people), 155 of whom have no portrait anywhere in the file.

## What this pass checked

Spot-checked a dozen names off the current gap list against `data/photo-finds/` rather than
trust the "documented dead end" claim on faith: Danny Vuleta, Neel Patel, Mallory Hardesty, Reed
Hensley, Brooke Mitchell, Kayla Distler, Elizabeth Gannon, David Darnell, Livi Ray, Callison
Padgett, Jesse Banales, Zachary Skillman, Tribhuwan Singh, Elizabeth DeLozier. Every one is
already cross-referenced in `2016-2025-notes.json`, `_officers-truly-missing-2026-09-06.json` and
`n2025-notes.json`, and the detailed note in `n2025-notes.json` confirms they were searched
against wkuherald.com's WordPress API directly (zero individually captioned hits; Danny Vuleta
returns zero posts at all).

Checked `data/photo-finds/_topscholar-wanted.json`'s three entries that are not marked CLOSED in
so many words: items 9 and 10 (the two April 2007 Herald issues for the Fisher/Eclov/England/
VanWinkle/Schooler/Miers cohort) both carry a "do not refetch" conclusion already — neither issue
contains the senate-candidate photo grid the lead was hoping for. Item 13 (2015 Talisman) carries
a 10 November update: the volume's text layer was grepped whole against its worklist, one
portrait (William Berry) was already published from it, and the rest of the cohort either never
appears by name or appears only in un-rowed crowd photographs with no caption key — "treat this
volume as exhausted." None of the three is live ground.

Checked the two `_archive-gaps.json` entries that read as open ("THIRTY-FIVE TALISMAN VOLUMES...")
in full: the class-composite sweep (dental hygiene, nursing, Spirit Masters booklets) is marked
"SPENT for the current worklists," and the Talisman-title-year note is a methodology fix already
folded into the 14 November passes that closed out the 2012-2025 Talisman cohort as a magazine-
format dead end.

Tested live network gates directly rather than assume from yesterday's logs: `wkuherald.com` and
`digitalcommons.wku.edu` both answered plain requests at 200; `web.archive.org` reset the
connection mid-handshake (consistent with the standing note that it is blocked from this
container, intermittently). Pulled wkuherald.com's five most recent SGA-tagged posts by date —
17, 15, 14, 10 and 4 November — all already on file from the 19 November passes. Nothing has
been published since.

## Conclusion

No new portrait. Every lead this pass could find was already closed by a prior run, and the two
open network gates (`wkuherald.com`, `digitalcommons.wku.edu`) turned up nothing newer than what
the 19 November passes already checked. `python3 scripts/build.py` and `python3
scripts/check_data.py` both pass clean against an unchanged `data/`; no data changes to commit
this pass, so `site/` was rebuilt only to confirm it still builds, then reverted rather than
committing a same-content, new-date rebuild. Landed this note on `research-photos`.
