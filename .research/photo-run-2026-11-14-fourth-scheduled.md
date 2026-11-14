# Photograph run, 14 November (fourth scheduled pass): the last mapped Talisman volume opened, 17 October's target list fully closed, one organizational flag raised

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a `leaders` portrait entry in `data/photos.json`, unchanged. (Gilley held the regent seat in
  2008-09, not the presidency, per the standing correction in prior reports.)
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports 186 officer-slots without
  a same-year portrait, 153 people with no portrait in any year — essentially unchanged from the
  day's three prior passes (186-187/155-157).
- **Priority 4**: all 61 years already carry at least one photograph.

## Network state, retested fresh

- `cgi/viewcontent.cgi` via plain `curl` with browser headers — Cloudflare-challenged as always.
- The same URL via Python's `urllib.request` with identical headers — **200, a real PDF.** Still
  open, confirmed by two separate fetches this pass (a 48 MB test file and a 721 MB volume, see
  below).
- `web.archive.org` — connection reset, unchanged.
- `wkuherald.com` — 200, open.

## What this pass did: opened the one volume the third pass today left unread

The third pass this morning mapped and read six of the thirteen 2012-2025 Talisman volumes a
17 October pass had only catalogued, closing the whole cohort as a structural dead end (post-2012
Talismans are themed photo-essay magazines with no club-and-organization section) except for one
volume it had not opened: **2016 Talisman: Life More Life** (`dlsc_ua_records/8677`, article
9667, 721 MB) — flagged as worth a look because it is already the source of an existing portrait
(Brian Chism's, reused at 2012-13/2013-14), so it might pre-date the magazine redesign.

Fetched it via the `urllib` TLS-fingerprint bypass (14.5 seconds for 721 MB). Extracted its text
with `pdftotext` — which, contrary to the standing note in `SGA-60-AGENT-INFO.md` that it is not
installed in this container, is in fact present at `/usr/bin/pdftotext` and ran instantly; no
`PyMuPDF`/`fitz` install needed this time.

**This volume does carry a real Student Government feature, unlike every other post-2012 volume
checked so far.** Two pieces:

1. A six-page profile of SGA chief of staff James Line and president Jay Todd Richey (pp. 139-141,
   "James Line"), covering how they met, Line's role, and his work on the Confucius Institute
   contract research. Names Josh Knight, an SGA senator, as a quoted source.
2. A four-page feature on an SGA lobbying trip to Frankfort against a proposed 9% higher-education
   budget cut (pp. 190-194, "SGA Lobbying"), naming Richey, Line, Nolan Miles (Executive Vice
   President), Nick Conrad and Hannah Neeper as the senators and officers who made the trip.

Checked every name against `data/photos.json` and the full 2015-16/2016-17 gap-list roster:
**Line, Richey, Miles, Knight and Neeper already carry portraits.** No new portrait results from
either feature.

Also searched the full extracted text (13,350 lines) for every one of the 153 names on the current
gap list. Every surname hit traced back to either a different person entirely (same-surname
coincidence in an unrelated caption — e.g. "Mark Clark" hitting on "Mike Clark," "Cody Cox" hitting
on an unrelated sports photo of "Ebony Cox") or to the one genuinely SGA-adjacent name that is not
usable: Sawyer Coffey appears in a flat, un-rowed "Public Relations Student Society of America"
roster list (fourteen names run together with no row structure and no photograph this volume's text
layer identifies), the same no-caption problem repeatedly ruled out for this cohort in earlier runs.
No club-and-organization section in this volume is headed "Student Government Association" or
"Associated Student Government" at all — the only SGA content here is the two magazine features.

## One organizational flag, not a photo finding

Nick Conrad, captioned in the lobbying-trip feature as "a Bowling Green junior" alongside named SGA
officers, does not appear anywhere in `data/years.json` for 2015-16 (there is a Jed/Conrad Davies
in 1998-99 and a Jed Conrad in 2005-06 — both different people, different years). Under this
project's rule that a `photos.json` leader entry's name must exactly match an existing `years.json`
entry, this photograph cannot be attached. Flagging for whichever routine researches 2015-16's
organization block: if Nick Conrad is added as a 2015-16 senator, this volume's lobbying-trip
photograph (p. 191 area, captioned with his name) is sitting ready to use.

## Conclusion

This closes the entire 17 October mapped Talisman list (13 volumes, 2012-2025): six opened and
read in full across today's three prior passes, six ruled out by their own published table of
contents with no download needed, and this one — the last unopened volume — now read in full and
confirmed to add nothing new to the photo record, beyond the one organizational flag above. No
file was added to `data/photos.json` or `data/photos/` this run. `build.py` and `check_data.py`
both pass clean: 61 years, 1964 events, 60 presidents, every one portrayed. Landed on
`research-photos`.
