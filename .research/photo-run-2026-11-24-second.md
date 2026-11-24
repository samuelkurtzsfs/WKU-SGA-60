# Photograph run, 24 November (second pass)

## Baseline reconfirmed

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  `leaders` portrait in `data/photos.json`.
- Priority 2: `portrait_gap.py --any-year` confirms every student body president and every student
  regent in `data/years.json` already carries a portrait. The only "President"/"Regent" lines it
  still prints are a different office entirely (Paul Gerard, 1969-70 Senior Class President) or
  executive-cabinet vice presidencies (David Young, John Holland), not the student body
  presidency or the regent seat.
- Priority 3 unchanged: 187 same-year officer/Senate gaps, 157 people, 155 with no portrait
  anywhere in the file.
- Priority 4: all 61 years already carry at least one `years`-level photograph.

## What this pass tried, specifically

**Network gates, tested cold rather than taken on trust:**
- `digitalcommons.wku.edu` item pages returned HTTP 404/403 even with full browser navigation
  headers (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`).
  Closed again today, consistent with this morning's first pass.
- `web.archive.org` reset at the TLS layer on every attempt (`curl: (35) Recv failure`). Closed.
- `archive.org/download/talisman<year>west/..._djvu.txt` was retried for every gap year outside
  the already-mapped 1971-1981/1986/1987 window (1967, 1968, 1969, 1970, 1983-1985, 1988, 1989,
  1992, 1996, 1998, 2001, 2005, 2010, 2016) to check whether more volumes had been added to
  archive.org since the last sweep. All returned 503 (no such item) — the archive.org Talisman
  collection still stops where this project's notes already say it does. No new OCR text became
  available.
- `wkuherald.com`'s WordPress JSON API is open and was used directly (not blocked, no pacing
  issue): confirmed again that nothing has posted since 17 November's "SGA prepares for the
  holidays with new bills," already read and ruled out on 23 November.

**A fresh batch of name searches against wkuherald.com**, picked from `portrait_gap.py`'s list of
the 12 most recent (2021-2024) gap names that do not appear in any prior `.research/photo-run-*`
note or in `data/photo-finds/_do-not-use.json`: Danny Vuleta, Neel Patel, Connor Ferguson, David
Darnell, Callison Padgett, Elizabeth Gannon, Mallory Hardesty, Reed Hensley, Brooke Mitchell,
Garrett Baum, Jesse Banales, Nicole Massarone. Danny Vuleta returned nothing at all. The other
eleven each turned up one or more real SGA articles, so eight full posts were opened and their
images checked:

- `wkuherald.com/65821` (election results, Bornefeld wins presidency, Apr 2022) — featured image
  photographs Sam Kurtz and Cole Bornefeld by name; does not mention Hardesty or Hensley, who
  appear in the body text only.
- `wkuherald.com/67791` (SGA votes in new senators and cabinet members, Sep 2022) — featured image
  is an unnamed group shot of "members of the WKU Student Government Association executive
  cabinet"; no individual is named in the caption, so it cannot identify Garrett Baum.
- `wkuherald.com/60866` and `/61104` (new members sworn in / share goals, Sep 2021) — same
  problem: group captions describing the meeting, not individuals, so Nicole Massarone is not
  identifiable from either.
- `wkuherald.com/71147` (election-process changes, Jan 2023) — featured image caption names only
  "Senior Senator Olivia Feck," not Neel Patel, who is covered in the text.
- `wkuherald.com/73874` and `/72365` (Aug 2023 Senate meetings) — featured images are oath-taking
  and chamber-wide group shots with no names in the caption; neither identifies Callison Padgett.
- `wkuherald.com/68255` (fall election results, Apr 2022) — caption names Cole Bornefeld and
  Garrison Reed only.

None of these photographs name the specific gap-list officer in a caption or in text immediately
beside the image, which CLAUDE.md's identification rule requires. No portrait added from this
batch.

## No change to the record

`data/photos.json` and `data/photos/` are unchanged. `scripts/build.py` and `scripts/check_data.py`
both run clean (61 years, 1,964 events, 60 people have been president); the only diff `build.py`
produced was the footer's build-date stamp, which was not committed. The two items every recent
pass has flagged still stand and still need a person rather than another automated run:

1. `data/photo-finds/_for-the-editor.md` — 13 people, 14 entries, open since 8 September 2026,
   each a proved photograph whose tie to the named officeholder needs a yes/no editorial call.
2. The photograph trigger's cadence against a 155-person gap that has now been checked,
   repeatedly, against every reachable source, including network-gate retests on a day both
   `digitalcommons.wku.edu` and `web.archive.org` happened to be closed.
