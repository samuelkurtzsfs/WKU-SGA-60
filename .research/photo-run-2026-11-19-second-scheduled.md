# Photograph run, 19 November (second scheduled pass): live exec-cabinet page and newest Herald issue checked, both already on file

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: every president and every student regent in `data/years.json` has a portrait.
- **Priority 4**: all 61 years carry at least one `years`-level photograph entry.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` is unchanged from this morning's
  pass — 187 cabinet/Senate leadership slots with no same-year portrait, 155 people with no
  portrait anywhere in the file, every one with a documented dead end in `data/photo-finds/`.

## What was checked this pass

`digitalcommons.wku.edu` answered a plain GET at 200 this pass (no rate-limit testing needed;
nothing on `digitalcommons` was pulled).

**The live `wku.edu/sga/executive/index.php` page** currently serves headshots for the 2026-27
executive cabinet (Caden Lucas, Jakob Barker, Will Derryberry, Gabi Pace, Cayden Bailey), each
name set in an `h4` heading directly beside its photo with a matching office title underneath —
a real caption, not just an `alt` attribute (the `alt` text on Lucas's own image is stale,
reading "Rush Robinson" from a previous year's markup that was never updated when the filename
and heading were). Checked all five against `data/photos.json`: every one of them already has
a `leaders` portrait on file for 2026-27, sourced from WKU News and the Herald's own photo
record. Nothing new.

**The newest Herald SGA coverage**, 17 November's "SGA prepares for the holidays with new bills"
(wkuherald.com/99560/), was checked for individually captioned officer photographs. Its lead
image is a group shot ("SGA Senate members watch and listen to the 2026-2031 WKU Strategic Plan
..."), and its one named-subject caption is Dr. Leslie Noth, the Office of Sustainability
director thanking Food Pantry volunteers — not an SGA officer. Nothing usable. The four Herald
SGA stories before it (15, 14, 10, 4 November) were already checked in the prior pass that
produced the Stacy Kitchens portrait and the 60th-anniversary homecoming photographs.

## Conclusion

No new portrait this pass. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
pass clean; no changes to commit. Priority-3's 155-person gap stands as the honest remaining
state of this archive's photography: every name on it has already been run to ground against
Talisman, Herald, WKU Archives and the live site, more than once.
