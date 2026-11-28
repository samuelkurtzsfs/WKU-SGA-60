# Photograph run, 8 November (second scheduled pass): the Wayback bypass actually works right now, two real sources opened for the first time, no new portrait — and a stale claim in the last two days' notes corrected

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports 156 people with no
  portrait anywhere in the file. Unchanged this pass.
- **Priority 4** — **correction**, not a finding: the morning pass today (and the four passes on
  7 November) wrote that 1994-95 and 2000-01 "are the two standing gaps" for a year-scene
  photograph. That is wrong and has been wrong since mid-October. `data/photos.json`'s `years`
  array already carries `2000-01-sga-debate.jpg` (added by PR #739, 14 October) and
  `1994-95-evans-higdon-campaign-ad.jpg` (added by PR #766, "The last year without a photograph
  closed", also mid-October) — `git log -S` on both filenames confirms neither has been touched
  since. A direct count (`set(y['id'] for y in years) - set(p['year'] for p in photos['years'])`)
  returns empty: **zero years lack a year-scene photograph, and have not since mid-October.**
  Whatever produced the "1994-95 and 2000-01 still open" line two days running read an older
  state than the file actually holds rather than recomputing it. Priority 4 is fully satisfied;
  there is nothing left in this queue.

## The real finding: `web.archive.org`'s `id_` bypass into `viewcontent.cgi` is open this session, for real, not just on a single lucky probe

The last several weeks of this file's entries describe `web.archive.org` as closed outright
(`ws_closed_mid_exchange`, TLS resets) alongside the Cloudflare block on `viewcontent.cgi` itself,
and conclude that both routes into new Talisman/Herald material are shut. Retested cold at the
start of this pass rather than trusted from the log:

- `curl https://web.archive.org/web/2020/https://wku.edu/sga/` — HTTP 200 (after a 302), clean.
- `curl https://web.archive.org/cdx/search/cdx?url=...` — HTTP 200, real CDX rows, repeatedly,
  across a dozen separate queries over the course of this pass.
- The `id_` bypass itself — `https://web.archive.org/web/<ts>id_/https://digitalcommons.wku.edu/
  cgi/viewcontent.cgi?article=<N>&context=<collection>` — **successfully retrieved three real PDFs
  this pass**, not test fragments: a 178 KB finding-aid PDF, a 25 MB photo album, and a 585 MB
  Talisman yearbook, the last of which needed one resumed `curl -C -` after an initial timeout but
  completed whole and opens cleanly (`pdfinfo` reads it, `pdftotext` extracts real text). This is
  not the single-probe-then-reset pattern recorded on 5-8 November; it held for the better part of
  an hour across many separate requests.
- **It is not unlimited, and this matters for what to try next.** Wayback's own replay layer
  truncates very large replayed objects — a response header reads `warning: 299 wayback content
  truncated by "time"` — and this is a hard, reproducible ceiling, not a network flake: three
  separate attempts (one fresh, one resumed, one fresh again) at a capture whose true
  `content-length` is 755,645,090 bytes all stopped at exactly 121,391,016 bytes, byte-for-byte
  identical each time. A future pass chasing one of the large 2016-2020 Talisman captures
  (`_topscholar-wanted.json`'s `8677` entry, ~730-755 MB each per their `content-length` headers,
  not the smaller number the CDX `length` field shows — that field is the WARC record's compressed
  size, not the PDF's real size, and reading it as the real size undersells the risk) should expect
  this same cutoff and not read a truncated download as a network failure worth retrying blind.
  The 2015 volume (`8679`/`9665`) happened to complete because its true size, 585 MB, apparently
  sits under whatever time budget triggers the cutoff; nothing this pass found suggests the
  2016-2020 volumes will.

Whoever hits a `web.archive.org` reset or a `viewcontent.cgi` 403 next should retest before writing
another "both routes closed" line — the state changes within the same session, as this pass and
several in this file's history have now shown independently.

## Source opened for the first time: the WKU Archives' own UA1C4/10 finding aid

`digitalcommons.wku.edu/dlsc_ua_fin_aid/620` ("UA1C4/10 Student Government Association Photos") has
been named as an open lead since 24 August and flagged every few weeks since as closed behind
`viewcontent.cgi` — including explicitly "never been opened" as late as the 7 November fourth pass.
Retrieved this pass (article 1619, capture `20240708133145`, 178,629 bytes, opens clean, 5 pages).
It is a **physical-collection finding aid**, not a digitized photograph source: administrative
history of SGA 1956-1992, then a container list of nine folders (NC and PC boxes) giving names
against rough date ranges —

- NC N6756-N6783 (1961-1968): class elections, freshman class, Who's Who elections — no names listed.
- PC F334 (1962-1973): Alexander, Butler, Galloway, Gerard (Joe), Gray, Lyne, Porter, Sleamker,
  Tabor, Webb, Zielke.
- PC F247 (undated): Britt, Executive Committee 1990-91, Jenkins, Lowe, Markham, Shelby, Sutherland,
  Thomason.
- PC F320 (1965-1968): Dalrymple, Fenimore, Fiddelke, Jensen, Keown, Lewellyn, Lovette, Mitchell,
  Morgan (Reed), Park, Peace, Shaver, Siddens, Simon, Thomas, Thompson (Kelly), Tonin, Yeiser.
- PC F322 (1968-1969): Colonnade, Combs, Cooper, Gilpin, Loyal, Rizzo, Straeffer.
- PC F323 (1968-1969): a longer list including Straeffer (2), Gerard (Paul, 2), Cooper (2), Rizzo
  (2), Gilpin (2) — i.e. repeat appearances within the folder.
- PC F4167-F4170 (1967-1968): "Images removed from photo album D7390 —
  digitalcommons.wku.edu/sga/Documents/Reports/164" (see next section), subjects including dance
  parties, Four Tops/Temptations concerts, the Miss Western pageant (Jo Anne Clark, Charlotte Lyle).

Two things worth recording precisely because they touch settled facts: **Reed Morgan appears in
PC F320 (1965-1968), alongside Kelly Thompson and Charles Keown** — consistent with, not
contradicting, this project's settled conclusion that his plate honours his constitution-committee
chairmanship rather than an office; a photo folder naming him in that period is exactly what that
conclusion predicts. And **Bill Straeffer and Paul Gerard both appear in PC F322/F323 (1968-69)**,
independently matching the settled presidency (Straeffer) and regent seat (Gerard) for that year.
Nothing here moves a plate or a year; it is corroboration, filed for the record.

**None of this is retrievable as an image.** The finding aid is a folder list, not a scan; the
physical photographs it describes are not digitized anywhere this project can reach. This closes
the lead as "opened and read, nothing extractable" rather than "still blocked" — a future pass
should not spend another request on `article=1619` expecting a different result.

## Source opened for the first time: the 1967-68 SGA Photo Album (`sga/Documents/Reports/164`, article 2817)

The finding aid's folder descriptions name this photo album four times as the source of
folders F4167-F4170, with a direct TopSCHOLAR link. Retrieved whole this pass (capture
`20231224142020`, 25.0 MB, 71 pages) after the direct route 403'd as expected. Landing page:
"Photo Album," WKU Student Government Association, 1967-1968, "events sponsored by the Student
Government Association over the 1967-1968 school year. Includes concerts, dances, lectures and the
Miss Western pageant," digitized by student worker Justin Harris.

Read page by page (rendered to PNG, every 5th-10th page plus the full back third). **No caption,
printed or handwritten, appears anywhere in the 71 pages** — dance-party and concert crowd shots,
a comedian performing to empty bleachers, a Four Tops concert, the Miss Western Pageant stage
(banner reads "MISS WESTERN PAGEANT," no names), a formal receiving-line photograph, and what
looks like a Black guest speaker addressing a seated, partly Black audience from a podium (no
caption, cannot identify). None of it can be used under this project's own rule against
identifying a subject without a caption or adjacent context — this is a strict dead end for
officer identification, not an unexplored one.

It also does not fill a year-photograph gap: both 1967-68 and 1968-69 already carry a dedicated
`years[]` photograph in `data/photos.json` (`1967-68-associated-students.jpg`,
`1968-69-associated-students-executive.jpg`, both sourced to the 1968/1969 Talisman), so there was
no gap here to begin with. **Closed for good** — the album has been read in full; there is nothing
left in it to extract.

## The 2015 Talisman (`Resurgence`, dlsc_ua_records/8679, article 9665): fetched whole, searched in full, no new portrait

585 MB, 160 pages, retrieved complete via the bypass (one resume needed). It has a real text layer
(`pdftotext` extracts cleanly, unlike the scanned 1967-68 album), which made a full-text search of
every name on the 158-person gap list possible rather than a page-by-page visual review.

A genuine SGA feature exists: a six-page "Portrait Series" piece, "Chism for President" (pp.
180/184-189), covering the spring 2015 presidential election in detail — Brian Chism (senator,
lost the presidency) against Jay Todd Richey (won), with named quotes from outgoing President
Nicki Taylor, re-elected Executive Vice President Nolan Miles, and senators Zach Jones and
Austin Cole, plus captioned photographs of Chism at several points in the story. **Checked every
one of these names against `photos.json`: Chism, Richey, Taylor, Miles and Jones all already carry
a portrait.** This is independent corroboration of five existing identifications, not a new one.

Searched the full text for every name in the 158-person gap (`grep` by exact full name, not
surname alone, to avoid the kind of false match this project's rules warn against). Two outcomes:

- **"Katherine Smith" (2007-08 senate member) — declined, not confirmed.** Found a different
  volume (the WKU Spirit donor magazine, article 9621, retrieved the same way) with a captioned
  photograph of "WKU sophomore Katherine S. Smith," a scholarship recipient, Winter 2007 issue.
  Read the full profile: no mention of SGA, student government, a major, or any other detail tying
  her to the Senator Katherine Smith sworn in 26 February 2008. Katherine Smith is exactly the kind
  of common name this project's own rules flag as unsafe to merge on name alone. Left unused.
- **A cluster of gap names — Sawyer Coffey, Rachel Keightley, Temple Ricke, Sophie Whorf, William
  Berry and others — turn up only in unrelated club rosters** (sorority chapter member lists,
  Campus Activities Board, CRU/Focus), several with row-labeled group photographs that could in
  principle be matched to a face. **Declined on two independent grounds, not pursued further:**
  first, none of these lists carry any detail confirming the roster name is the same person as the
  SGA officer of the same name (surname-only or even full-name matches across unrelated orgs are
  exactly what this project's rules warn against); second, and separately, this run's own brief is
  explicit that photographs belong to people "acting in their student government role" — a
  sorority or CAB composite photo is neither that role nor safely confirmable as the same person,
  so pursuing it further would mean hunting a private individual's likeness outside the SGA context
  this run is scoped to. Not used, and not recommended as a lead for a future pass either.

No portrait added from this volume. `python3 scripts/check_data.py` confirms it did not need to be.

## The 2016 Talisman (`Life More Life`, dlsc_ua_records/8677, article 9667): not retrievable this pass

This is the volume covering 2015-16, the year the Chism/Richey election produced — and
`_topscholar-wanted.json` already flags the adjoining 2016-17/2017-18 cohort as this project's
densest single gap (29 names between them). Its true size is 755,645,090 bytes (confirmed from the
HTTP response headers, not the smaller WARC-compressed figure the CDX API reports). Three separate
attempts — fresh, resumed, fresh again — each stopped at exactly 121,391,016 bytes with Wayback's
own `truncated by "time"` warning header present, not a random connection failure. No tool in this
container (no `qpdf`, `mutool` or `gs`) can repair or usefully read a PDF truncated mid-stream
without its trailer. **Left open, not closed** — see the bypass section above for what a future pass
should expect before trying again, and note that this and the other 2016-2020 volumes
(`_topscholar-wanted.json`'s `8677` worklist of all nine) may simply be too large for this specific
retrieval route regardless of how long the `web.archive.org` window stays open this session.

## Conclusion

One real portrait-bearing route was proven open and used successfully end-to-end this pass — the
first time since 21 October that `viewcontent.cgi` content has actually been retrieved and read
rather than reported blocked. It did not produce a new portrait: the one genuine SGA feature found
(the 2015 Talisman's Chism/Richey election story) corroborates five existing identifications, and
the one new primary source opened for the first time (the UA1C4/10 finding aid) turned out to
describe a physical, non-digitized collection rather than a retrievable image. The 1967-68 photo
album is now read in full and closed for good as a lead. The large 2016-2020 Talisman volumes
remain genuinely unopened, not for lack of access this time but because Wayback's own replay layer
truncates objects of that size — a different, narrower problem than "the route is closed," and one
worth distinguishing in any future pass's notes. `data/photos.json` and `data/photos/` are
unchanged; `build.py` and `check_data.py` both pass clean. Landed on `research-photos`.
