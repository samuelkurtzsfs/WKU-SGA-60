# Photograph run, 11 October (second pass) — the Wayback `id_` bypass is open and reliable this session; four standing Herald leads re-checked by rendered page image rather than text layer alone, all still negative; the 2012-2025 magazine-era Talisman PDFs are confirmed absent from Wayback entirely

## Priorities 1, 2 and 4, reconfirmed before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Nothing to do.

**Priority 2** (any other president or student regent without a portrait): checked every `leaders`
record in `data/years.json` against `data/photos.json` by name, programmatically. Zero missing.

**Priority 4** (years with no photograph at all): same standing gap as every recent note —
1994-95 and 2000-01 carry no entry in the `years` array of `data/photos.json`, though both clear a
looser "any photo at all" test on their leader-portrait composites. Unchanged.

`scripts/portrait_gap.py` reports 189 officer slots with no portrait, held by 159 distinct people,
157 of them with no portrait anywhere in the file. Unchanged from every pass since 9-10 October.

## The `cgi/viewcontent.cgi` gate, retested cold: still shut

`curl` with full navigation headers (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`,
`Upgrade-Insecure-Requests: 1`) against a known article returned HTTP 403, Cloudflare "Just a
moment..." challenge, 5995 bytes. Same as every pass since this gate closed.

## `web.archive.org` was open and reliable all session — confirmed by four separate PDF downloads, not just a CDX probe

Earlier notes (10-11 October) logged this route as intermittent or shut. This run retested it
properly rather than taking one timeout as the answer, and it worked: `web.archive.org/web/<ts>id_/<url>`
(the `id_` modifier serves the raw archived resource with no Wayback banner, which matters for a
binary file) returned real, magic-byte-verified PDFs on four separate fetches this run:

- `article=9903&context=dlsc_ua_records` (2000-01 gap) — 8.2 MB, `%PDF-1.7`
- `article=4695&context=dlsc_ua_records` (2005-06 gap) — 4.6 MB, `%PDF-`
- `article=10372&context=dlsc_ua_records` (2003-04 gap) — 6.2 MB, `%PDF-`
- `article=7740&context=dlsc_ua_records` (2008-09 gap) — 31.5 MB, `%PDF-`

Two individual requests inside this run did hit `curl: (35) Recv failure: Connection reset by
peer` or a timeout (one on `7740` cold, one on a CDX query) and succeeded on a bare retry a few
seconds later — the known intermittency is real, but it resolves on retry rather than blocking the
whole session the way recent notes described. **For the next run: do not conclude the Wayback
route is shut from one failed request. Retry at least once before moving on.**

## All four PDFs opened and read page-by-page as rendered images, not just the text layer — same four leads this file has carried since early October, now checked by eye rather than by keyword

Prior passes (3 October, this file) read these same four issues through PyMuPDF's text extraction
and ruled them out that way. Herald PDFs from the 2000s are frequently a poor-quality text layer
(broken ligatures, garbled OCR-like output on scanned pages), so this run went further: rendered
every page containing a relevant name or `SGA`/`overnment Association` match at 150 DPI and looked
at the actual image, to make sure a real photograph next to a relevant name was not being missed
by a text-layer artifact.

- **Article 9903** (Herald 76:52, 17 Apr 2001): confirms the 3 October finding exactly. The SGA
  election story ("SGA election produces low voter turnout") runs on printed page 1 with no
  photograph of its own — the only image on that page is the unrelated Tiffany concert photo.
  Corrected on review, 11 October: Rawlings was **not** unopposed. He won the only contested
  office, vice president of public relations, defeating Holly Skidmore 343-315; the presidency
  (Leslie Bedo) and the three other executive offices were the unopposed ones. The story also
  continues on printed page 7, which this note first said no other page carried — that jump page
  was read on review and carries no photograph either, its only image being an advertisement.
  **Still no usable frame for 2000-01**, which the jump page confirms rather than disturbs.
- **Article 4695** (Herald 81:42/46, 13 Apr 2006): three pages carry `SGA`/`Student government` —
  an opinion piece ("SGA president should lead"), a news story ("Judicial council to help students
  understand SGA responsibilities," about Judge John Minton visiting a forum — not about any
  officer on the gap list), and a "Vote Professor of the Year, forms at the SGA office" notice. All
  three pages rendered and inspected directly. **No photograph on any of them** — the judicial
  council story runs as plain text with no accompanying image. Does not support Jenna Haugen,
  Jessica Williams or Hunter Sprowles (the names this lead was originally logged against); none of
  the three are named in this issue at all.
- **Article 10372** (Herald 79:53, 20 Apr 2004): two pages carry `SGA` — the front-page
  continuation on Todd's impeachment/election dispute and "Watkins upheld as speaker" on page 5.
  Both rendered and read directly: all-text coverage of a contested speaker vote (Brittany Fausey,
  Troy Ransdell, Skylar Jordan — none on the current officer gap list), no photograph on either
  page. The earlier substring match for "Gretchen Light" on pages 8 and 11 was a false positive
  (those pages are a step-dance competition recap and a baseball brief; no occurrence of "Gretchen"
  anywhere in the document). **Does not support the Gretchen Light / Matthew Pava / Cameron Yancey
  lead this article was logged against.**
- **Article 7740** (Herald 84:46, 16 Apr 2009): the richest of the four — a full front-page SGA
  election story ("All smiles, Smiley wins SGA election," with a vote-tally graphic for Kevin
  Smiley/Kayla Shelton) and a page-5 "Regent falls short on office hours" story quoting Chief
  Justice Corey Bewley twice and naming Reagan Gilley. Both pages rendered and inspected. **No
  photograph of Bewley, Gilley, or anyone from the officer gap list** — the front page's only
  photographs illustrate an unrelated homelessness feature, and the office-hours story runs as
  plain text with one pull-quote graphic, no portrait. "Vanessa Scott" does not appear anywhere in
  this issue; the one text match on "Scott" was Missouri gubernatorial spokesman Scott Holste, an
  unrelated person in an unrelated wire story.

**All four of this file's standing Herald leads for the 2000-01/2003-04/2005-06/2008-09 gaps are
now exhausted by direct page image, not just by text search.** This is a stronger negative than
the 3 October pass recorded, because it rules out the specific failure mode (a real photograph
sitting on a page whose garbled text layer hid the name) that a text-only check cannot rule out.

## A genuinely new finding: the 2012-2025 magazine-era Talisman PDFs are not in Wayback's archive at all

The 10 October afternoon note flagged this specific gap: it had read these 20 volumes' TopSCHOLAR
abstract pages (open, not Cloudflare-gated) and found no SGA content indexed in the table of
contents, but noted "what remains untried... is opening one of these volumes' actual page images
once a PDF route opens, to check whether an SGA page exists that the TOC abstract simply doesn't
index as such."

With the Wayback bypass open this run, tried exactly that: fetched eight of the twenty magazine-era
`viewcontent.cgi` PDFs (articles 8679, 8696, 5160, 5162, 8678, 8677, 8685, 8686 — chosen to cover
the years with the densest officer-gap lists, 2012-13 through 2016-17), paced 3 seconds apart.
**Every one came back HTTP 404 from Wayback** (a 4,678-byte "not in archive" page, not a PDF) except
one connection reset on a retry-eligible request not re-attempted this run. A direct CDX query for
one of them (`article=5160&context=dlsc_ua_yearbooks`) returned an empty result set, confirming
these specific URLs were simply never crawled by Wayback — consistent with the Herald issue PDFs
(linked constantly from citations across the web) being crawled while the far less commonly linked
yearbook downloads were not.

This closes the "untried" item the 10 October afternoon note left open: **Wayback cannot be the
route into the magazine-era Talisman PDFs.** The only way into that content remains the live
`cgi/viewcontent.cgi` endpoint directly, which is Cloudflare-gated and has been shut on every
single test since it closed.

Also checked `archive.org` (not `web.archive.org`) by title/identifier search for any independently
uploaded WKU Talisman scan after 1987: none exists. The `talisman<year>west` identifier scheme this
collection uses stops at `talisman1987west`; nothing under that scheme or a plain title search
exists for 1988 onward. This reproduces, by a different method, the standing finding that
`archive.org`'s plain-text route only covers 1971-81 and 1986-87.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed; `data/years.json` is untouched.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61 years, 1,967
events, 60 presidents; "the archive checks out against its own rules"). The `site/` rebuild this
produced was discarded (`git checkout -- site/`) since nothing in `data/` changed. This run's only
output is this note.

## For the next run

- The Wayback `id_` bypass works and is worth retrying on a transient failure rather than treating
  one timeout as the route being shut.
- The four standing Herald leads for 2000-01/2003-04/2005-06/2008-09 are now exhausted by direct
  page image, not just text search. Do not re-open 9903, 4695, 10372 or 7740 without a new reason
  to think a page was missed.
- **Follow the jump line, not just the keyword hits.** The editorial review of 11 October found
  this note had missed the continuation of the 9903 election story on printed page 7, because the
  sweep listed pages matching `SGA` and read those, and the jump page was reached by a "See
  Election, Page 7" line rather than by a repeat of the keyword. The conclusion survived — the
  jump page carries no photograph — but on another issue it need not. When a story runs on from a
  front page, read the page it runs on to before calling the lead exhausted.
- The magazine-era Talisman (2012-2025) is now confirmed absent from Wayback. The only remaining
  route into that content is the live `cgi/viewcontent.cgi` endpoint, gated by Cloudflare on every
  test to date. If that gate ever opens, the 2012-13 through 2016-17 volumes are the highest-value
  target — they cover the densest stretch of the current 159-person officer gap (Justin McDole,
  Kelly Simmons, Jackie Stewart, Kara Raley, Tyler Scaff, Abigail Potter, Allie Payne, Amber
  Daniels/Daniel, Robert Bell, Stacey Schepers, Cole McDowell, Kasey Glasgow, and more).
- 189 officer slots / 159 people / 157 with no portrait anywhere remains the live count.
- Priority 4's narrow queue is still open: 1994-95 and 2000-01 carry no scene photograph in the
  `years` array.
