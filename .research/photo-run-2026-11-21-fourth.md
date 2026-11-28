# Photograph run, 21 November (fourth pass)

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` — 61 years, 1964 events, 60 people have been
  president; every president and student regent still carries a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` — same standing gap, roughly 150-190
  officer/senate rows with no portrait, all previously logged in `data/photo-finds/` as dead ends.
- **Priority 4**: all 61 years still carry at least one `years`-level photograph entry.

## What this pass tried

wkuherald.com's WP-JSON feed is live again today (confirmed with a plain single request before
anything else). Took 22 names from the standing gap list that were genuinely untried in
`data/photo-finds/_archive-gaps.json` — mostly 2019-2024 senate/committee officers (Jillian
Kenney, Alexis Mayne, Brenna Mathews, Turner Reynolds, Nicole Massarone, Zachary Skillman,
Tribhuwan Singh, Jesse Banales, Elizabeth DeLozier, Garrett Baum, Danny Vuleta, Neel Patel,
Mallory Hardesty, Reed Hensley, Brooke Mitchell, Kayla Distler, Connor Ferguson, Elizabeth Gannon,
David Darnell, Livi Ray, Callison Padgett, Carter Smith) — and searched each against
`wp-json/wp/v2/posts?search=<name>&_embed=1`, paced two seconds apart.

Every hit's featured-media `alt_text` field came back empty, so pulled the actual rendered page
for the most promising lead, "SGA elects committee chairs, hears from provost on enhancement
plan" (wkuherald.com/67853/), which names Elizabeth DeLozier directly in its body text as the new
chair of legislative operations. The page's only substantive photograph is a generic executive-
cabinet group shot ("Members of the WKU Student Government Association executive cabinet listen
to proposals from senate member nominees...") whose `alt` text names nobody individually, and the
same file (`mcinnis_s_SGA_001-1.jpg`) is reused as the featured image on at least four other
unrelated SGA articles pulled by other names in this batch (Baum, Distler, Padgett) — it is a
stock meeting photo, not a portrait of any one officer. "Baum" in that same page's markup turned
out to be a false positive: the byline credit "Josh Baumgardner," not Garrett Baum. No image on
the page sits near the DeLozier sentence at all.

None of the other 21 names turned up an `<img alt="...">` naming that specific person on any of
their matched articles either — every hit was either a reused generic SGA-meeting stock photo,
or an unrelated story (sports, campus-life, other departments) that matched only because the
search is full-text, not headline-scoped. This mirrors every photo-finds entry already on file
for this cohort: wkuherald.com captions a named individual in `alt` text only when the whole
article is about that person (a presidency, an election-results gallery), never for a committee
chair or senator mentioned mid-paragraph. Logged as a new dead end so a future run does not
re-run this exact batch.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `build.py` and
`check_data.py` both run clean; the build-date-only diff in `site/` was reverted. This closes the
wkuherald WP-JSON route for this specific 22-name batch; the broader standing gap (roughly 150-190
officer rows) remains exhaustively documented across `data/photo-finds/` with no open lead this
session could find.
