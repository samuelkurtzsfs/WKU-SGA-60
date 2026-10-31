# Photograph run, 26 October (fourth scheduled pass): a genuinely new access route found and tested, five candidate officer slots checked against it, none confirmed, no new portrait

## Priorities 1, 2 and 4, reconfirmed directly against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 60 people have been president,
  archive checks out against its own rules. No missing leader portrait.
- **Priority 4**: unchanged; every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `scripts/portrait_gap.py --any-year` reports the same 948
  officer slots, 188 with no portrait for that person in that year, 158 people, 156 with no
  portrait anywhere. Unchanged from every pass since 20 October.

## digitalcommons.wku.edu and web.archive.org, retested: both still closed

Same two standing blocks every pass this week has reported: `digitalcommons.wku.edu/cgi/viewcontent.cgi`
returns HTTP 403 with a Cloudflare interactive challenge even with full browser navigation headers,
and `web.archive.org` resets the connection outright. Retested fresh against article 1619
(the SGA-photographs finding aid) and a Wayback SGA-site URL respectively. Both still closed.
Not re-litigated further this pass - see the third pass's report for the proxy-status check that
already ruled out a session-side policy gate.

## A new route found and verified: archive.org's own page-image and search-inside APIs

Every prior pass treated `archive.org/download/<id>/<id>_djvu.txt` (plain OCR text, not rate
limited) as the only thing archive.org offers beyond the advanced-search API. It offers two more
things, both tested working this pass, and **neither goes anywhere near web.archive.org**, so
neither is affected by that block:

1. **Per-page JPEG images**, with no need to download the full derivative PDF (100MB for the 1975
   volume). The URL shape is:

   ```
   https://archive.org/download/<identifier>/page/n<leaf>_w<width>.jpg
   ```

   This 302-redirects twice (first to a type-detection hop, then to the actual image server) and
   `curl -L` follows it cleanly. Confirmed against `talisman1975west`, `talisman1979west` and
   `talisman1981west`: real JPEGs each time (verified by `file`, not just HTTP 200), 900px-1200px
   wide, legible at that width. No pacing trouble was seen on archive.org across roughly 15 image
   fetches this pass, but it has not been pushed to volume, so treat it with the same courtesy as
   everywhere else.

2. **A search-inside API that returns the internal leaf number for a text match**, which is what
   makes the page-image route usable without guessing:

   ```
   https://<d1-server>/fulltext/inside.php?item_id=<identifier>&doc=<identifier>&path=<dir>&q=<term>
   ```

   `<d1-server>` and `<dir>` come from `https://archive.org/metadata/<identifier>` (the `d1` and
   `dir` fields - they differ per item and are not guessable). The response gives the matched OCR
   line and a `page` field, which is the **leaf** number the page-image route wants - not the
   printed page number. The offset between leaf and printed page is not constant across a volume
   (front matter, foldouts and inserted color plates shift it), so it has to be calibrated per
   target by fetching one candidate leaf and reading the printed folio off the image itself before
   trusting the arithmetic. That cost a wasted fetch twice this pass (leaf 238 landed on printed
   page 235, not 234; a later guess for a different target landed two pages short again) - budget
   for it rather than treating the subtraction as reliable.

This matters beyond today: the open `_djvu.txt` route lets a researcher find *that* a name is on a
page, but says nothing about whether that page carries a photograph, and the only way to check a
caption's wording against a photo (CLAUDE.md's identification rule) has, until now, meant pulling
the page up on `digitalcommons.wku.edu/talisman/` - which is the route that has been closed all
week. This one reaches the same yearbook pages from the archive.org side instead, and it was open
the entire time.

## The five remaining archive.org-reachable gap slots, checked against the new route

Talisman volumes on archive.org only run 1971-1981, 1986 and 1987 (per CLAUDE.md), which narrows
the 158-person, 156-year-unconfirmed gap from `portrait_gap.py` to five slots. All five were
checked this pass - the first time any of them has been checked since this run can actually see
yearbook pages again:

- **1974-75 Vern Pulman, Representative-at-Large.** Not in `talisman1975west` at all: no hit for
  "Pulman" in the full djvu text, nor for the OCR variants "ulman"/"ullman". The ASG section of
  that volume (pp. around 109, already used for the Tom LaCivita portrait per CLAUDE.md) does not
  name him either. No lead.
- **1978-79 David Young, Administrative Vice President.** Found once, in `talisman1979west`: a
  quote attribution in a constitution-reform story ("David Young, administrative vice president,
  said this was done to 'force some heads-up competition'..."), p. 289. No photograph on that
  page shows him - the page's two captioned photographs are both of his running mate, president
  Steve Thornton, and both are already in `data/photos.json` (`1978-79-asg-meeting.jpg`, src
  "1979 Talisman, p. 288"). Confirms the earlier run that found this photo made the correct call
  not to extend it to Young - he's quoted, not pictured. No lead.
- **1978-79 Steve Wilson, Judicial Council Chairman.** One "Steve Wilson" appears in
  `talisman1979west`, but only in the alphabetical senior-portrait grid, captioned "STEVE WILSON,
  agriculture / Tompkinsville" - major and hometown only, no SGA tie of any kind. Per CLAUDE.md's
  rule against using a photo whose subject can't be confirmed from its own caption, this cannot be
  used: a shared name with no office named beside it is not an identification, it's a coincidence
  waiting to be disproven. No lead.
- **1978-79 Alice Wicks, Secretary.** The only mention of "Wicks" in `talisman1979west` is her own
  index entry ("Wicks, Alice Elizabeth") with no page number attached at all - meaning the index
  itself records that she has no photograph in the volume. No lead.
- **1980-81 Mark Chesnut, Treasurer.** The only name match in `talisman1981west` is "Mark Chestnut
  (Sigma Alpha Epsilon)" on the intramural-sports results page (p. 234-235, badminton singles and
  racquetball doubles winner) - a different spelling, no photograph of him on that page (the page
  is a results table plus two unrelated action shots of other students), and no SGA/ASG context of
  any kind. Confirmed as the wrong lead, not merely an unconfirmed one: the surname is spelled
  differently in a sports column with no connection to student government.

None of the five produced a usable portrait. This was expected to be a low-yield list - these are
exactly the slots every prior pass already failed to clear by other means - but it is now a
*checked* low-yield list rather than an unreachable one, which it has not been since the two main
routes closed.

## What a future pass should do with this

The new route does not reopen 1996-97 through 2009-10, the years the standing `digitalcommons`
block has stalled (see the 23-24 August entries in `SGA-60-AGENT-INFO.md` section 8.4 for that
backlog) - archive.org's Talisman holdings stop at 1987. But every one of the 156 fully-missing
officer portraits that falls in 1971-1981/1986/1987 can now be searched image-by-image through
this route without waiting on either blocked site, and the search-inside API means that doesn't
require downloading a full volume to do it. Calibrate leaf-to-page offset per target before
trusting the arithmetic; it moves within a single volume.

## Build and validation

`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean. `site/` was
rebuilt to confirm it and is untracked, as always, per the no-hand-edit rule. Nothing in `data/`
changed this pass. Landed on `research-photos`.
