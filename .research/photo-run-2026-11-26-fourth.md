# Photograph run, 26 November (fourth pass)

## Baseline reconfirmed, unchanged from all three earlier passes today

- `python3 scripts/build.py` and `python3 scripts/check_data.py` both run clean: 61 years, 1,964
  events, 60 people have been president, every president and student regent carries a portrait.
  Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) already has portraits.
- `scripts/portrait_gap.py --any-year` is unchanged: the only remaining gap is Senate/cabinet/
  Judicial Council officers of 2018-2026, the same names the first three passes today logged.

## What this pass checked that the earlier three had not already covered

- `wkuherald.com`'s WordPress API: no post has been published since 17 November's "SGA prepares
  for the holidays with new bills" (confirmed again, newest-first query). Nothing new to search.
- Checked four 2018-2026 gap names directly against `wkuherald.com` full text and media captions
  rather than against the Herald index, since that is where a recent officer's face would most
  likely surface:
  - **Elizabeth DeLozier** (Secretary of the Senate, 2021-22) appears in "SGA elects committee
    chairs, hears from provost on enhancement plan" (7 Sep 2022, as chair of legislative
    operations the following year), but the article's photograph caption names no individual:
    "Members of the WKU Student Government Association executive cabinet listen to proposals
    from senate member nominees..." Group photo, nobody identified by name. Not usable.
  - **Justin Goins** (Associate Chief Justice 2021-22, Chief Justice 2022-23) appears in body
    text of three 2022-23 articles about a censure hearing and election results, but the one
    photograph from that hearing identifies only "President Cole Bornefeld (center)" in its
    caption — Bornefeld already has a portrait. Goins himself is not named in any caption found.
  - **Brenna Mathews** and **Erika Puhakka**: no usable hits. "Mathews" returns five posts, none
    about SGA from her term; "Puhakka" returns nothing (empty result).
  - All four remain without a portrait. The pattern across this gap is consistent: the Herald's
    SGA photography from this period is captioned by committee or by the president alone, not by
    name for every officer present, so a caption-confirmed identification is the exception rather
    than the rule for this list.
- Network gates, retested cold:
  - `digitalcommons.wku.edu` item/landing pages: 200, following the redirect
    (`dlsc_ua_records/1619` → `/1619/`).
  - `cgi/viewcontent.cgi` with full browser navigation headers: 403. Still closed — this blocks
    both Herald issue PDFs and Talisman yearbook PDFs hosted there.
  - `archive.org/download/talisman2019west/...`: 503, an Internet Archive maintenance-page body.
    Still not resolved. In any case archive.org's own holdings run out after 1987, and WKU did
    not keep publishing a Talisman yearbook through the 2018-2026 gap years, so this route would
    not have reached this particular list even if it opened.
  - `web.archive.org`: connection reset at the egress proxy. Still closed.

## Conclusion

No new portrait landed this pass. Every item on the standing priority list is already satisfied;
the 2018-2026 Senate/cabinet/Judicial Council gap is the only one left, and it has now been
checked against the Herald index, the Herald's own site search, and individual media captions,
with the same result each time: the photography exists but is captioned collectively, not by
name, for exactly the people this list is missing. `data/photos.json` and `data/photos/` are
unchanged; this note is the only new file. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both run clean against unchanged data.
