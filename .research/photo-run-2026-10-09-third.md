# 9 October 2026 (photograph agent, third pass this day) — the eight named gaps searched, none found; the three gates re-tested, two open, one still shut

## Priorities 1, 2 and 4, reconfirmed against the current tree before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Nothing to do.

**Priority 2** (any other president or student regent without a portrait): checked every
`leaders` record in `data/years.json` against `data/photos.json` by name. Zero missing.

**Priority 4** (years with no photograph at all): checked every year's `leaders` entries and the
`years` array in `data/photos.json` together. Every one of the 61 years has at least one
photograph. Zero missing.

So this pass's whole job was priority 3, and specifically the eight names the 9 October second
pass named as never searched.

## The eight names, searched and still empty

| Year | Office | Name | Result |
|---|---|---|---|
| 1994-95 | Judicial Council Member | Grace Hancock | Not found |
| 1995-96 | Chairperson, Cultural Diversity Committee | Margaret Carter | Not found |
| 1995-96 | Chairperson, Public Relations Committee | Cindy Chiapetta | Not found |
| 1997-98 | Chairperson, Campus Improvements Committee | Callie Varner | Not found |
| 1998-99 | Chairperson, Academic Affairs Committee | Larry Murphy | Not found |
| 2008-09 | Chair, Public Relations Committee | Vanessa Scott | Not found |
| 2012-13, 2013-14 | Justice, Judicial Council | Justin McDole | Not found |
| 2014-15 | Justice, Judicial Council | Allie Payne | Not found |

**Why each one fails.**

- **Hancock, Carter, Chiapetta, Varner, Murphy (1994-95 through 1998-99).** The WKU Talisman
  stopped publishing after the 1994 volume and did not resume until 2003 (confirmed against
  `digitalcommons.wku.edu/dlsc_ua_yearbooks/index.2.html` and the base yearbooks listing, which
  together show no 1995 through 2002 volume exists in any form — not a crawl gap, an actual
  publication gap). So there is no yearbook for any of these five years to search. The local
  `herald-index-full.json` (11,852 items, no keyword filter) was grepped for each surname paired
  with SGA/ASG/"Student Government" context: Hancock returns ten hits, all a *Herald* reporter
  named Catherine Hancock; Carter returns thirteen, all a reporter named Carter Pence; Murphy
  returns two, neither this Murphy; Chiapetta and Varner return nothing at all. None is our
  person. This is the index's known limit (a miss there is not evidence of absence, since it only
  covers headlines), but it rules out the fast route and leaves only reading full *Herald* issues
  by hand for 1994-1999, which this pass did not have room for.

- **Vanessa Scott (2008-09).** Searched `wkuherald.com`'s WordPress API
  (`/wp-json/wp/v2/posts?search=`) for her name directly: two results, neither about her (one a
  2023 film column, one a 2004 concert announcement that predates her term and is a coincidence
  of the search ranking, not a name match). No article from her actual term surfaced.

- **Justin McDole (2012-13, 2013-14) and Allie Payne (2014-15).** The Talisman volumes for these
  years exist, but only on `digitalcommons.wku.edu` — archive.org's Talisman holdings stop at
  1986-87 and do not reach the 2010s (checked by direct identifier lookup, not inference: no
  `talisman2013west`, `talisman2014west` or `talisman2015west` item exists on archive.org). The
  digitalcommons copies are enormous: the 2013 volume ("Form") is 897.6 MB, the 2014 volume
  ("Reckoning") is split into two parts of 341.2 MB and 495.2 MB, and the 2015 volume
  ("Resurgence") is 558.5 MB. None of these is retrievable in this environment in one piece, and
  `cgi/viewcontent.cgi` — the only gate that serves digitalcommons PDFs at all — was shut for this
  entire pass (see below), so even a partial fetch was not possible today.

## Two more names chased on the strength of a caption lead, both dead ends worth recording

The 9 October second pass's note on the archive.org-held years (Pulman, Bass, Young, Wicks,
Millay, Austin) said these had already failed on caption ambiguity or absence. Re-opened two of
them today to check that verdict rather than take it on trust, since both looked promising from
the raw OCR text:

- **David Bass**, 1977-78 activities vice president. The 1978 Talisman (`archive.org`, page 34)
  carries a caption reading "A LIGHT MOMENT IN AN ASG MEETING brings laughter from president Bob
  Moore and smiles from activities vice president David Bass, secretary Sharon May and vice
  president Cathy Murphy" over a photograph of four people. The caption names him but gives no
  position (no "left", "foreground", or similar), and the photograph shows four people in a
  cluster with no way to match name to face. `data/photos.json` already carries this exact image
  as a `years` entry for 1977-78, captioned without naming an individual — which is the correct
  call on an unidentifiable group photo, and matches what this pass would have done had it not
  already been done.

- **David Young**, 1978-79 administrative vice president. The 1979 Talisman (`archive.org`, printed
  page 289) has a direct quote from him in a text feature on ASG's year ("David Young,
  administrative vice president, said this was done to 'force some heads-up competition'..."),
  but the two photographs on that spread are an uncaptioned office scene and a captioned photo of
  newsletters on a dorm floor — neither shows him. Confirmed by pulling the actual page image
  (archive.org's `BookReaderImages.php` endpoint against the `_jp2.zip`, one page at a time, not
  the 45 MB full PDF), not by text alone.

A third, **Mark Chesnut** (1980-81 treasurer), looked like a hit in the 1981 Talisman's name
index ("Chesnut, Mark Cameron 234") but page 234 turns out to be an intramural-sports results
page naming a badminton and racquetball player spelled "Chestnut" — a different spelling in a
sports context, not the SGA treasurer. Discarded as a false match rather than used.

## The three gates, retested cold again

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — still shut. `curl` with full navigation headers
  against a known-good article number returned HTTP 403 and a 5,986-byte HTML bot-check page, not
  a PDF. This is the only digitalcommons route this pass needed and could not get: ordinary
  digitalcommons pages (item pages, the yearbooks collection index) loaded fine all session on
  plain `curl`, so the block is specific to the PDF-serving endpoint, not the domain.
- `archive.org` — open and used heavily this pass: the `_djvu.txt` full text, the
  `_page_numbers.json` page maps, and single-page JPEGs pulled through
  `BookReaderImages.php` against the `_jp2.zip` (never the full archive PDF or zip). This is a
  materially faster route to a single Talisman page than anything tried before, and is worth
  recording for the next run: given a server/dir from `archive.org/metadata/<id>` and a leaf
  number from `_page_numbers.json` or the `_djvu.xml` `usemap` attribute, one page comes back as a
  normal JPEG in a single request, for any of the nineteen Talisman identifiers archive.org holds
  (1943, 1946, 1947, 1963-65, 1971-81, 1986-87).
- `wkuherald.com` — open, both the site and its WordPress REST API
  (`/wp-json/wp/v2/posts?search=`, `/wp-json/wp/v2/media/<id>`). Used for all three 2008-and-later
  names above. The API is fast and avoids the bot defenses a plain scrape would hit, but its
  search is a blunt keyword match (it returned an unrelated 2004 article and a 2026 column for
  "Vanessa Scott" before anything from her actual term), and recent SGA coverage photographs are
  almost always wide meeting-room shots credited to a staff photographer with a caption
  describing the scene, not naming who is in it — which is a structural problem for identifying
  individual senators and committee chairs from this source, not a search-technique one.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed; `data/years.json` is untouched.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean, same 61
years/1,967 events/60 presidents as before this pass started. The only other change this pass
made was syncing `research-photos` to the current `main` tip (a merge with one conflict, in
`.research/NIGHT-REPORT.md` only, resolved by keeping both sides' text — no data file was
touched by the conflict). This run's output is this note.

## For the next run

All eight names from the second pass are now genuinely searched and negative, with reasons on
file rather than a bare miss. The five pre-2003 names (Hancock, Carter, Chiapetta, Varner,
Murphy) have no yearbook route at all — the Talisman gap is real, not a crawl failure — and the
only path left for them is reading *Herald* issues from 1994-1999 by hand, which the local
headline index cannot do for a committee chair who was never a headline subject. The three
2010s names (McDole, Payne, and Scott's 2008-09) are blocked by file size and the closed
`cgi/viewcontent.cgi` gate respectively; if that gate opens, McDole and Payne are reachable with
the same page-at-a-time archive.org technique used today, applied to a digitalcommons PDF instead
— fetch by byte range if the server honors `Range` on `cgi/viewcontent.cgi`, rather than pulling
340-900 MB in one request.

Beyond these eight, the missing-officer list is far larger than this or any single pass can clear:
`organization.executive` and `organization.senate.officers` across `data/years.json` currently
name 33 executive officers and 182 Senate officers/committee chairs with no `photos.json` entry,
the great majority of them Senate seats and committee chairs from the 1990s through 2020s. This
pass sampled eight of them on a prior run's specific flag and a handful more on its own leads; it
did not attempt the other roughly 200. A future pass working this list should expect the
Vanessa-Scott pattern to be the common case post-2008: a real photograph exists in Herald
coverage, but the caption names the scene, not the people in it, and the rule against guessing a
face from an unlabelled crowd shot will close most of these off by source, not by search effort.
