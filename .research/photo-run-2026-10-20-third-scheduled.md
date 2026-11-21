# Photograph run, 20 October third scheduled pass (trigger "SGA 60 - portraits"): baseline reconfirmed independently, both blocked routes still closed, three more leads from the gap list run to ground with the same result prior runs already recorded

## Priorities 1, 2 and 4: checked directly against the data, not assumed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`, each a valid JPEG (`ffd8ffe0` magic bytes checked directly).
  Nick Todd and Katie Dawson both from Herald election coverage; Jeanne Johnson from her 1 May 2008
  commencement-edition portrait captioned "Jeanne Johnson, President, Student Government
  Association"; Reagan Gilley from Herald 84:35's caption of him celebrating a student regent
  election win.
- **Priority 2**: `python3 scripts/check_data.py` reports no missing leader portrait across every
  year. Independently cross-checked `data/years.json` leaders against `data/photos.json` by
  script: zero presidents and zero student regents without a portrait.
- **Priority 4**: every one of the 61 years carries at least a leader portrait or a year-level
  photograph; none is empty.

## Priority 3: three untried names from `scripts/portrait_gap.py --list`, checked fresh

Before searching, checked `git log --all` and `.research/photo-run-*.md` for each name. **Bass,
Chesnut and Wilson had each already been searched and declined by earlier runs** (the 20 October
second pass's report lists Bass among names "prior runs had already run to ground" without stating
the finding itself). Ran them again anyway, independently, rather than taking that on faith, and
reached the same dead ends by a different path:

- **David Bass, Activities Vice President, 1977-78**: appears, named and captioned, in the
  existing `1977-78-asg-meeting.jpg` group photograph already in `data/photos.json` ("activities
  vice president David Bass" among four named officers in one Talisman group shot). Confirmed the
  file is this exact photograph (fetched the same page from archive.org's JP2 scan of
  `talisman1978west`, page 34, independently, and matched it). Not a standalone portrait — the
  caption names four people in one shot and nothing in the photograph distinguishes which face is
  Bass's — so no new leader-portrait entry can honestly be added for him specifically. This is
  already the best the volume offers and is already on file.
- **Mark Chesnut (printed "Chestnut" in-page), Treasurer, 1980-81**: the 1981 Talisman's senior
  name index gives only one page for him, 234. Pulled that page directly as an image
  (`talisman1981west`, archive.org JP2 scan, leaf 238): it is the men's intramural-champions
  results table, where "Mark Chestnut (Sigma Alpha Epsilon)" is listed twice as a badminton and
  racquetball winner, in text only. No photograph of him anywhere on the page or elsewhere in the
  volume — a single index page with no photo is this volume's way of saying he was never
  photographed. No portrait exists to find.
- **Steve Wilson, Judicial Council Chairman, 1978-79**: the only "Wilson" tied to a first name in
  `talisman1979west` is "Wilson, Steve Alan", pages 296/318/320/336 — all Greek Week and Spring
  Sing coverage, as the barbershop-quartet tenor for the SAE fraternity's winning entry, with no
  connection anywhere in the text to ASG or the Judicial Council. Per this project's rule against
  matching people by surname alone, this is not treated as the same person on a shared name; it is
  flagged as a likely-different Steve Wilson, not used. No portrait tied to the Judicial Council
  chairmanship found.

## Network state, retested fresh rather than carried over from the last report

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (the PDF endpoint): HTTP 403, Cloudflare "Just a
  moment..." challenge page, confirmed with a plain request carrying the full navigation header
  set (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`).
  Still closed.
- `digitalcommons.wku.edu` ordinary item pages (e.g. `/dlsc_ua_records/4686/`): HTTP 200, loads
  cleanly. Only the file-download endpoint is blocked, not the domain.
- `web.archive.org`: connection reset (`curl: (35) Recv failure: Connection reset by peer`,
  `ws_closed_mid_exchange` at the agent proxy). Still closed.
- `archive.org` (the plain item/file host, distinct from `web.archive.org`): open. Used for all
  three leads above, via the `_djvu.txt` full text and, for two of them, the actual JP2 page scans
  pulled directly (bypassing `digitalcommons.wku.edu` entirely — the same route the previous pass
  flagged as available but had not yet exercised for an actual page image this cycle).
- `wkuherald.com` WP-JSON search API: open. Newest SGA-tagged post is still "SGA funds new Preston
  Center area..." (14 Oct), already read by the previous pass. The next-newest, "SGA senate
  complete following fall election" (29 Sep, `wkuherald.com/97897/...`), has a featured image but
  was already fetched and read by the 11 October run, which confirmed the REST API's `link` field
  resolves it correctly; nothing in it names any of the still-missing officers.

## What this run leaves unchanged

`data/photos.json` and `data/photos/` are unchanged from the last commit on this branch — every
lead chased this run was either already on file (Bass) or a genuine dead end (Chesnut, Wilson).
189 officer slots (157 people) remain without a portrait, per `scripts/portrait_gap.py`, unchanged
from the last several passes; the overwhelming majority are 2000s-2020s Senate and Judicial Council
names already searched repeatedly against the two routes this container can actually reach, with
nothing on either domain carrying a face for them. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean (61 years, 1964 events, 60 presidents, no missing
leader portrait, no year without a photograph). Landed on `research-photos`.
