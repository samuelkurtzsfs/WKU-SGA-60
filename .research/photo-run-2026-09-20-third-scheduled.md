# Photograph run, 20 September (third scheduled firing): one year-photograph gap closed

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` §4 and §6.
This is the third time today's scheduled photograph trigger has fired; `.research/photo-run-
2026-09-20-scheduled.md` and `.research/photo-run-2026-09-20-second.md` were both already merged
into `main` before this run started. `research-photos` fast-forwarded cleanly onto `origin/main`
(no divergent work to merge). `gh` is not installed; `git push --dry-run` was not re-tested since
the prior two runs both confirmed direct write access this session.

Re-checked the standing priorities fresh rather than trust the morning reports as still current:

- **Priorities 1 and 2 (president and regent portraits): still fully satisfied**, including the
  four originally-named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley). A
  scripted cross-check of every `president`/`regent` leader entry in `data/years.json` against
  `data/photos.json` came back with zero gaps, and the four named files (plus the general
  population) still check out as real JPEGs (`ffd8ffe0`).
- **Priority 4 (a year-photograph for every year): seven gaps remained** after the second run's
  four additions: 1994-95, 1995-96, 1996-97, 2000-01, 2005-06, 2006-07, 2008-09 (the last is the
  Kevin Smiley photo's old slot, now empty after the second run's editor pass re-filed it to
  2009-10).
- **Priority 3 (cabinet/Senate officers): unchanged, roughly 175 names still without a portrait.**

## digitalcommons.wku.edu and web.archive.org, tested fresh

`digitalcommons.wku.edu/cgi/viewcontent.cgi` is still behind a Cloudflare managed challenge on a
direct request (`cf-mitigated: challenge` in the response headers, a "Just a moment..." interstitial
body) — confirmed again on a fresh article (the 2017 Talisman, article 9669). Landing pages on the
same domain are unaffected.

`web.archive.org` **was reachable this run**, intermittently — several individual CDX and raw-capture
requests came back as connection resets or timeouts, but a plain retry cleared every one of them.
Used the same method the second run documented: read the real `article=` number from a `dlsc_ua_
records/<item>/` landing page (not gated), query `web.archive.org/cdx/search/cdx?url=...viewcontent.
cgi%3Farticle%3D<N>...&filter=statuscode:200` for a clean capture, then pull the PDF from that
timestamp's `if_` raw endpoint. `pymupdf` read and rendered pages; several of these mid-1990s issues
carry no OCR text layer at all (not merely poor OCR — zero characters on every content page except
the TopSCHOLAR cover sheet), so pages had to be paged through visually rather than found by keyword
search.

## One year-photograph gap closed: 1996-97

Chased three leads out of `data/herald-index-full.json`'s local index for the three-year 1994-97
window, all via the CDX/raw-capture route:

- **`dlsc_ua_records/3012`, "New SGA president maps upcoming term" (Herald 72:54, 24 Apr 1997,
  p. 3), succeeded.** The page carries a headshot of Keith Coffman inset beside a pull-quote
  captioned "— Keith Coffman, Russellville junior," reporting his election as SGA president for
  1997-98 four days after the vote. This photograph was taken and published within the 1996-97
  academic year (Aug 1996 – Jul 1997), so it fills that year's photograph slot on its own
  terms — it does not need to depict anyone who held office *during* 1996-97, per the standing
  dating rule that a photograph is dated by when it was taken, not by whose term it later
  concerns. Coffman already has a leader portrait for 1997-98 (from Herald 73:54, 5 May 1998,
  a different, later photograph), so this is a genuinely new, independently sourced image, not a
  re-use. Cropped from the page image, verified as a real JPEG (`ffd8ffe0`), saved as
  `data/photos/1996-97-keith-coffman-elected.jpg`, and added to `photos.json`'s `years` array.
  The same page also settles the full slate of 1997-98 election results (Coffman/Sears for
  President/VP, Fite for Secretary, Lewis for Treasurer) in a results box, for whichever routine
  next works the organization/officer data — no photograph of any of the other winners runs with
  it, so nothing further was added here.
- **`dlsc_ua_records/3020`, "Miller reflects on year as SGA president" (Herald 72:46, 27 Mar
  1997, p. 15), closed negative.** Its inset photograph of Kristen Miller is the exact same
  image already on file as her leader portrait (same page, same citation) — not a second,
  distinct photograph, so it cannot also serve as the year's general photograph.
- **`dlsc_ua_records/2989`, "Debate reflects attitudes" (Herald 71:53, 16 Apr 1996, p. 1),
  closed negative for 1995-96.** Front-page story on the Kristen Miller/Rick Malek presidential
  debate; the only photograph on the page is an unrelated pageant photo. No image of either
  candidate.
- **`dlsc_ua_records/8003`/`dlsc_ua_records/7936` (Higdon "Last Words" and "Sees New Beginning,"
  Herald 70:53 and 70:56, Apr 1995), closed negative for 1994-95.** Both are text-only pieces —
  the Higdon "New Beginning" write-up on p. 12 runs opposite a movie-ad photograph, not one of
  her, and confirms the same officers-sworn-in slate the 25 Apr 1996 Herald reported for the
  following year's turnover (Yan as VP, Rucker's award, the Lodmell sisters' award), but carries
  no photograph itself.
- **`dlsc_ua_records/9098`, "Bedo lone candidate for SGA president" (Herald 76:45, 13 Mar 2001,
  front page and p. 7), closed negative for 2000-01.** A distinct article from the one that
  already sources Leslie Bedo's existing leader portrait (a different issue, 76:49, 5 Apr 2001).
  Confirmed it carries no photograph of Bedo or any candidate on either page — the front page's
  photographs are of unrelated international-student and campus-clinic stories.

## Left for the next run

Six year-photograph gaps remain: **1994-95, 1995-96, 2000-01, 2005-06, 2006-07, 2008-09.** The
1994-95/1995-96 pair is proving genuinely hard against the local Herald index's SGA-tagged
headlines — every lead chased today and by the two earlier runs today is either text-only or
reuses an already-filed photograph. A future run might do better starting from the *photo credit*
side rather than the headline side: these image-only, no-OCR issues cannot be keyword-searched, so
finding a photograph requires either a specific known page reference or paging through an entire
issue visually, which is slow. The 175-name cabinet/Senate-officer backlog (Priority 3) was not
touched this run; the two earlier runs today already document it as substantially exhausted
against `wkuherald.com`'s live search, with the Cloudflare-gated `digitalcommons.wku.edu` PDF
route (now confirmed reachable indirectly via `web.archive.org`, when that route is up) the most
promising remaining avenue for the pre-2003 names in it, and the 2013-2019 Talisman route
confirmed structurally closed for the same purpose.

## Validation

`python3 scripts/build.py`, `scripts/check_data.py` and `scripts/check_duplicates.py` all pass
clean. `check_data.py` confirms every leader/year photo file is attached and carries valid magic
bytes. `check_duplicates.py`'s four flagged pairs are pre-existing event pairs, untouched by this
run (this run only touched `data/photos.json`, one new file in `data/photos/`, and the
`site/` files the build regenerates from them). No JSON was hand-typed without a `json.load`
validation pass first.
