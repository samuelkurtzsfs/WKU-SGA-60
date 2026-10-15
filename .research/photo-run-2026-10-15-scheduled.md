# Photograph run, 15 October (scheduled pass): reconfirmed, nothing new clears the bar

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against `data/photos.json` and `data/years.json` before anything else, per CLAUDE.md's
"check whether an earlier run already got them."

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`.
- **Priority 2** (every other president or student regent): direct query of `years.json` against
  `photos.json` finds zero leader records in any of the 61 years without a photo.
- **Priority 4** (years with no photograph at all): zero years missing from `photos.json`'s `years`
  array.

`python3 scripts/portrait_gap.py`: 189 officer slots / 159 people / 157 with no portrait in any
year — unchanged from every pass since 13 October.

## Network state this session

- `digitalcommons.wku.edu` item (landing) pages: reachable (301, normal redirect).
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (the PDF route): 403 on the first attempt and
  again after a 95-second backoff. Closed for this session, consistent with every pass since
  13 October.
- `web.archive.org`: connection reset outright, both attempts. Closed for this session.
- `archive.org` (not `web.archive.org`) and `wkuherald.com`: both open.

## What was checked on the open routes

Cross-referenced the 157-person no-portrait list against all prior `.research/photo-run-*.md`
files (grep by name) before spending any new requests. Every name in the list has already been
searched at least once; the 2011-2021 officers were worked exhaustively against wkuherald.com's
WP-JSON API on 13 October (post search, media search, embedded galleries) with close to a zero
hit rate, and the pre-1992 names reachable in archive.org's held Talisman volumes (1971-1981,
1986, 1987) were worked at the actual page-image level on 14 October. Re-ran one spot check
(Lucas Knight, 2017-18 senator, the least-searched name on file) directly against
wkuherald.com's post-content search as a sanity check on the "already exhausted" claim rather
than taking it on faith: nine articles mention him by name, all SGA floor-debate quotes, none
carrying a photograph of him. Confirms the prior finding rather than adding one.

No new photograph identified. No file in `data/photos/` or entry in `data/photos.json` changed
this pass.

## What is still open

The 189-slot officer/senate gap is unchanged, for the reason recorded on 13 and 14 October and
reconfirmed here: the names still open are the ones that need `cgi/viewcontent.cgi` (the bulk of
the pre-2011 and several post-2011 gaps) or `web.archive.org` (the old SGA website's officer
pages, ~1997-2010), and both stayed closed for the whole of this session. Nothing on the
currently open routes (`archive.org`'s Talisman holdings, `wkuherald.com`) remains untried. The
next gain on this gap needs one of the two closed routes to reopen — they are reported
elsewhere in this project's notes as lifting and re-closing by the hour, not fixed shut — not
another pass over wkuherald.com or archive.org with the same name list.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph.
