# Photograph run, 21 November (third pass)

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` — "61 years, 1964 events, 60 people have been
  president" — every president and student regent still carries a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` — unchanged: the same ~187
  same-year officer slots with no portrait, ~155 people with no portrait anywhere. Every name on
  this list already has a documented dead end in `data/photo-finds/`.
- **Priority 4**: all 61 years still carry at least one `years`-level photograph entry.

## What this pass tried, beyond re-confirming the baseline

Two sources that get comparatively little use in `data/photo-finds/_archive-gaps.json` next to
the Herald and the Talisman:

- **WKU Archives UA1C photograph collections.** TopSCHOLAR's own search page is JS-rendered
  (confirmed directly: `do/search/?q=...` returns a 200 with the results templated client-side,
  not server-rendered — this is why CLAUDE.md says to use a Google site search instead of
  crawling the search page itself). `site:digitalcommons.wku.edu UA1C "student government"`
  turned up no UA1C item at all; the closest match is a 2004 finding aid, "UA1B2/1 Student
  Government History," in the Student/Alumni Personal Papers collection, and a separate "UA12/3/1
  Student Government Association - Governance" inventory page — both text finding aids, not
  photograph collections, and neither new to this project (the UA12 collection numbering is
  already the one `data/photo-finds` cites elsewhere). No UA1C image collection keyed to student
  government surfaced.
- **Fresh name-by-name site searches** for four of the most-quoted, never-photographed officers
  from the richest-documented 2014-2022 cohort (Nathan Cherry, Josh Zaczek, Erika Puhakka, Justin
  Goins), since a direct search engine sometimes surfaces a page TopSCHOLAR's own blocked search
  or a prior crawl missed. Cherry's name surfaces only on `wku.edu` SGA minutes/cabinet-note
  pages (already a text-only source, no images); Zaczek, Puhakka and Goins produced no hits on
  `digitalcommons.wku.edu` at all. No new lead for any of the four.

Also confirmed `digitalcommons.wku.edu` is reachable today over plain HTTPS with navigation
headers (200 on a direct `do/search` request), for whoever picks up a `viewcontent.cgi` lead
next.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `build.py` and
`check_data.py` both run clean; the build-date-only diff in `site/` was reverted
(`git checkout -- site/`). The two sources tried this pass (UA1C image collections, fresh search
on four of the standing gap's most-documented names) are now closed without result and should not
be retried on the strength of this note alone. The standing ~155-person officer-portrait gap
remains exhaustively documented elsewhere in this directory; nothing in today's three passes
changed that picture.
