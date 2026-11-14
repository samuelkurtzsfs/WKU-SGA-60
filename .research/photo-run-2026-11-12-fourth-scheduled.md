# Photograph run, 12 November (fourth scheduled pass): the three queued Talisman item numbers close, all already mined under other names, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 187 officer-slots
  without a same-year portrait, 155 people with no portrait anywhere, held by this pass's start
  unchanged from the day's three prior passes.
- **Priority 4**: every one of the 61 years carries at least one photograph, confirmed again
  including the three years this pass's own research touched (1985-86, 1989-90, 1991-92).

## Closing the three TopSCHOLAR item numbers the day's first pass found but did not open

The first scheduled pass today identified three Talisman volumes (`dlsc_ua_records/410`, `/414`,
`/416`) as genuine gaps in this project's own tracking table - item numbers between already-known
408 and 412 that nobody had opened under those numbers before - and the second pass opened the
other four in the same batch (409, 411, 413, 417). This pass opened the remaining three. Network
state at the start: `curl` against `digitalcommons.wku.edu/cgi/viewcontent.cgi` still 403s
(Cloudflare), Python's bare `urllib.request` with the same URL and headers still answers 200 -
the TLS-fingerprint gate this project has now logged open on four separate dates. `archive.org`
answered cleanly for metadata lookups but its djvu transcript only exists for the volumes this
project's notes already named (1971-1981, 1986, 1987); `talisman1990west` and `talisman1992west`
return empty `{}` from the metadata API, confirming the gap rather than a fetch failure.

- **410 - 1986 Talisman (covers 1985-86), article 1410.** Fetched the PDF (87.4 MB, 392 pages),
  found its scan carries almost no OCR text layer, and used `archive.org/download/talisman1986west/
  talisman1986west_djvu.txt` instead (not rate-limited, real OCR). Printed pp. 193-194 carry two
  "Associated Student Government" group photographs, FRONT ROW/BACK ROW captioned, 19 names
  total: Mitchell McKinney, Cindy Richards, Greg Elder, Tara Wassom, Loree Zimmerman, Roland
  Spencer, Edward Kenney, Lori Scott, Kent Groemling, Mark Lovell, Sean Peck, Donna Pack, Tim Todd,
  Lori Dohrn, Jennifer Borsch, Naheed Shafi, Nell Withers, Nancy Johnson, Holger Velastegui, Debra
  Wredman, Caroline Miller, Dana Cunningham, Stephanie Sims, Terry Malone, Henry Meadows. Cross-
  checked every one against `data/photos.json`: **every single one already has a portrait on
  file**, including Mitchell McKinney (1985-86 president) and Tim/Timothy Todd (1986-87
  president). The photograph was already mined, just not under this item number.
- **414 - 1990 Talisman (covers 1989-90), article 1414.** Fetched the PDF (47.1 MB, 375 pages;
  this one does carry a garbled-but-present text layer). Page-by-page `pdftotext` search located
  "Associated Student Government" at PDF leaf 166 / printed p. 162 ("Activate: Changing the
  rules"). Caption: Front Row Joe E. Rains, Emily G. Morgan, Julie M. Fleming, Van C. Hodge, Jr.;
  Middle Row Amos E. Gott, Dawn Bradley, William H. Engle, Jr., Jeremy W. Lasley, Shannon
  Montgomery; Back Row Eddie D. Smith, Gregory L. Willoughby, Todd Johnson, Michael Colvin, Brian
  Sewell. All fourteen already carry a portrait, including Amos Gott - the 1989-90 president, and
  CLAUDE.md's own worked example for the `photos.json` format.
- **416 - 1992 Talisman (covers 1991-92), article 1416.** Fetched the PDF (48.9 MB, 185 leaves,
  two printed pages per leaf). Used the volume's own back-of-book index (leaf 176, "Associated
  Student Govern-ment ... 180") to go straight to the right page rather than guess - leaf 94,
  printed pp. 180-181, "Representing Interests." Two group photographs there: First Row Scott A.
  Sivley, Devin L. Delano, Melony A. Jones, Huma Ahsan, Chad Gray; Second Row Nancy L. Rascoe,
  Mistianna Holcomb, Kathleen Young, Tom Springer; Third Row Melissa A. Maggard, Eric D. Griggs,
  Jennifer J. Jaggers. / First Row Alan N. Thomason, Deanna L. Mills, **Heather E. Falmlen**,
  India Wilson, Pamela R. Wells, Joe Rains; Second Row John M. Seiber, Gretchen S. Ploch, Andrea
  D. Cailles, Andrea C. Wilson, Kevin Colon. Falmlen - the 1991-92 president and student regent -
  sits third in a clean six-person standing front row with no ambiguity. All but four of the
  sixteen names already have a portrait; the four that don't (Devin Delano, Melony Jones, Chad
  Gray, Pamela R. Wells) are rank-and-file members with no officer record in `years.json` to
  attach a portrait to, not a tracked gap. This entry's real hope - David Smith and Trent Lyda,
  the two 1992-93 officer gaps - do not appear anywhere in this 1991-92 volume; they are a year
  later than this photograph covers.

All three are now logged `CLOSED` in `data/photo-finds/_topscholar-wanted.json` with the full
caption text and the cross-check against `photos.json`, so no future pass re-opens them on the
strength of their item numbers looking unfamiliar. The lesson for whoever reads this next: a
TopSCHOLAR item number being absent from this project's own tracking tables does not mean its
*content* is unseen - several of these photographs had already been mined via `archive.org`'s
djvu transcripts or other Herald sources under short-form names, long before anyone logged the
TopSCHOLAR item number itself.

## Conclusion

No new portrait this pass. All three item numbers the day's queue carried forward are now closed
with full reasoning on file. `build.py` and `check_data.py` both pass clean: 61 years, 1964
events, 60 presidents, every one portrayed. The remaining 155 people with no portrait anywhere
are, as far as every source this project can currently reach is concerned, genuinely not in the
photographic record, or are rank-and-file members this project does not track as officer gaps.
Landed on `research-photos`.
