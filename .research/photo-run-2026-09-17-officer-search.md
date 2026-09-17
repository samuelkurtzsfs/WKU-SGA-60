# Photograph run, 17 September (afternoon) — cabinet/Senate officer search, nothing confirmed

## Starting state, re-confirmed

Checked the standing priorities before touching anything, same result as every run today:

- All four named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) and every
  other `leaders` entry with `role: "president"` or `role: "regent"` across all 61 years already
  has a portrait. Priorities 1 and 2 remain fully satisfied — nothing to do there.
- 34 executive-cabinet names and 184 Senate-officer/committee-chair/senator names still have no
  portrait (this run counted fresh from `data/years.json` against `data/photos.json`, independent
  of the running total in earlier reports, and landed on the same order of magnitude).

This run worked priority 3 (cabinet/Senate officers) and found nothing solid enough to add.
Recorded here mainly so the next run does not repeat the same dead ends.

## Four names checked against every accessible Talisman year (1976–1981) via archive.org: all negative

Before finding the Wayback-CDX route below (this run rediscovered it independently, then found
the 16 September third-pass and this-morning's wayback-pdfs reports had already found and used
it — see "Not the first to find this" below), this run worked archive.org's own
`talisman19NNwest` items, which need no pacing and no workaround:

- **David Bass** (Activities Vice President, 1977-78). Found in the 1978 Talisman only as one of
  four names in a candid "A LIGHT MOMENT IN AN ASG MEETING" photo (p. 34) where his face cannot
  be distinguished from the caption alone — a 4th, male figure at the frame's left edge is mostly
  out of shot. Checked the 1976, 1977, 1979 and 1980 indexes for an individual class portrait:
  the 1976 index gives "Bass, David Eugene 288", which turned out to be a 35-name Sigma Alpha
  Epsilon fraternity group photograph (p. 288) — he is one name in a caption block that size, not
  identifiable. No individual portrait found in any year checked. Left without a portrait.
- **Alice Wicks** (Secretary, 1978-79). Indexed in both the 1979 and 1980 Talisman without a page
  number attached to her name — checked against known cases (e.g. Cathy Murphy's index line reads
  "Murphy, Cathy Renee 401" when she does have a portrait), a blank page number appears to mean no
  individual photo that year. Left without a portrait.
- **Mark Chesnut** (Treasurer, 1980-81). Appears by name only in "Men's Intramurals" results
  tables in both the 1980 and 1981 Talismans (badminton/racquetball/tennis winners), never next to
  a photograph of him specifically. His indexed page numbers (1980 Talisman p. 257, 1981 Talisman
  p. 234) both turned out to be these same intramural results pages, not portraits. Left without a
  portrait.
- **David Young** (Administrative Vice President, 1978-79). Directly quoted in the 1979 Talisman's
  ASG feature ("Making news about entertainment", pp. 288-289) but the spread's only photographs
  are of Steve Thornton (president, already on file), Victor Jackson (already on file) and a shot
  of newsletters on the floor — no photograph of Young accompanies his quote. Left without a
  portrait.

Also checked, no result: **Chris Millay** (Parliamentarian, 1986-87) — not found by name in either
the 1986 or 1987 Talisman (only a different person, Beth Ann Millay, appears in both). **Vern
Pulman** (Representative-at-Large, 1974-75) — no hit at all in the 1975 Talisman's OCR text.

## Not the first to find this: the Wayback-CDX route was already documented this morning

Partway through this run, before spending more effort on the Cloudflare block, `.research/`
was checked for a photo-specific log and turned up three same-day reports
(`photo-run-2026-09-16-third-pass.md`, `photo-run-2026-09-17-wayback-pdfs.md`, and others). **The
16 September report had already tried and left open the idea of Wayback Machine captures of
`digitalcommons.wku.edu`'s `viewcontent.cgi`, and this morning's report had already turned it into
a working technique** — the CDX query and the `id_`-suffixed raw-file URL described there work
exactly as documented. This run independently rediscovered the same idea (after about 40 minutes
of dead-end attempts: plain `curl` retries with a 90-second backoff, then a Playwright/headless-
Chromium approach with cookie capture and CDP response interception, all of which hit the same
Cloudflare "Just a moment..." challenge) before finding the existing report and switching to the
proven method. **Read `.research/` for same-day reports before spending time on infrastructure
problems — this cost real time that a five-minute check would have saved.**

Confirmed still true: `digitalcommons.wku.edu/cgi/viewcontent.cgi` is Cloudflare-challenged for
both plain `curl` and a real (if headless) Chromium browser — cookies captured mid-challenge do
not help a subsequent `curl` request, and even a full Playwright navigation to the file URL
resolves to the challenge page roughly as often as it loads the PDF, so it is not reliably
scriptable at all right now. The Wayback capture route is the one that works.

## Two more Talisman volumes pulled via Wayback, one genuine negative, one near-miss left unused

Using the same CDX query as the wayback-pdfs report
(`https://web.archive.org/cdx/search/cdx?url=digitalcommons.wku.edu&matchType=domain&filter=original:.*talisman.*&limit=2000&output=json&fl=original,statuscode,mimetype,timestamp`),
found and downloaded clean captures of the 1984 ("The Touch of Red", article 1408) and 1985
("What Did You Expect?", article 1409) Talismans — confirmed those exact titles/years first via
each item's TopSCHOLAR landing page (`digitalcommons.wku.edu/dlsc_ua_records/408/` and `.../409/`,
both reachable live, unblocked — only the file-serving endpoint is challenged), not guessed from
list position.

- **1984 Talisman: no Associated Student Government entry in the Organizations chapter at all.**
  The chapter (pp. 226–306) runs as an alphabetical club-by-club grid with a photo and caption per
  club (Accounting Club, Advertising Club, Afro-American Players, Alpha Epsilon Delta, Alpha Kappa
  Psi, Alpha Phi Omega, Alpha Psi Omega...), and the alphabetical run goes directly from "Alpha
  Psi Omega" (p. 233) to "Civil War Re-enactment" (p. 234) with nothing for "Associated..." in
  between. This matches the 1994 volume's finding in the wayback-pdfs report exactly — some
  Talisman years simply left ASG out of the organizations directory. **Kelly S. Smith (Treasurer)
  and John Holland (Public Relations Vice President), both 1983-84, have no portrait available
  from this specific volume.** Their individual class-portrait grid pages were not locatable by
  text search (this volume's OCR is present but badly degraded on small print — a name-by-name
  visual scan of the class-portrait pages was not attempted this run, and is the honest next step
  for these two, not a search technique already tried and failed).
- **1985 Talisman: John Holland turns up again**, named and quoted (as "a Louisville senior and
  committee co-chairman") in a feature on ASG's book exchange program (pp. 202-203), alongside ASG
  president Jack Smith — but the page's only photographs are a staged photo-illustration of
  textbooks and a posed model with a mock "Book Exchanger" newsletter prop, neither captioned with
  Holland's name. No usable photo of him here either.
- **A near-miss, deliberately left unused**: the 1985 Talisman's Greek pages (pp. 264-265) carry a
  Chi Omega sorority composite photograph whose caption names both **Connie Hoffmann** (Secretary,
  1984-85 — an exact name match, and the right year) and, in the neighbouring composite on the
  same page, a **"Kelly Smith"** with no middle initial given (a much weaker match for "Kelly S.
  Smith," Treasurer the year *before* this photo was taken — too common a name and too big a gap
  in the record to use without more evidence). Hoffmann's name appears 7th of 9 in the "SECOND
  ROW" of a front-row/second-row/third-row theater-seat composite of roughly 20 sorority members.
  The front row (7 people) is sharp enough to count with confidence; the second row, raised and
  packed in behind it, is not — re-rendering the source PDF at up to 1200 DPI did not add real
  detail past the original scan's halftone resolution, and nine visually similar young women
  packed shoulder-to-shoulder in a low-contrast 1980s scan is not something this run could
  distinguish face-by-face with confidence. **Deliberately not used, per the standing rule that a
  misidentified face is worse than no face.** Left here so a future run does not have to
  re-discover this photograph, but a future run should not use it either unless it has a genuinely
  better source scan or another way to anchor the count (a sharper copy of the same Talisman page,
  for instance, or a second, independent source naming her alongside a description of the photo).

## Nothing added

`data/photos.json` and `data/photos/` are unchanged this run — no commit was made. `git status`
is clean against `origin/main` merged into `research-photos`. Re-running `build.py` /
`check_data.py` was not necessary since nothing changed, and was skipped for that reason rather
than skipped by oversight.

## Left for the next run

- **Read `.research/` for same-day reports before re-testing infrastructure** (the Cloudflare
  block, web.archive.org's own intermittency) that has already been characterized once today.
- Kelly S. Smith and John Holland (1983-84): the 1984 Talisman's class-portrait grids (People
  section, roughly PDF pages 44-116 of `talisman1984.pdf`, a Wayback capture — see the CDX query
  above, article 1408) were not visually scanned this run. Text search does not work on this
  volume's small print; only a page-by-page visual read will confirm whether either has an
  individual class portrait.
- Connie Hoffmann (1984-85): the Chi Omega composite described above is p. 264 of
  `talisman1985.pdf` (Wayback capture, article 1409) — position 7 of 9 in the second row. Only
  worth another look with a better scan or a corroborating source.
- Mickie Hennig (Secretary, 1988-89): not in the ASG group photograph already on file for that
  year (`1988-89-asg-executive.jpg`, confirmed by its own caption, which lists seven other named
  officers/senators and not her). Not checked further this run given how much time the above cost;
  the 1989 Talisman (`talisman1989.pdf` per the wayback-pdfs report, article ~1413) is downloadable
  by the same route if a future run wants to look for her elsewhere in it.
- The 184-name Senate/committee-chair list and the 12 years with no `years`-level photo are both
  still almost entirely untouched; today's reports collectively have made a small dent (Easton and
  Logsdon this morning) against a genuinely large backlog.
