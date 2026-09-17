# Photograph run, 17 September — the Wayback-Machine-PDF route opened, two new portraits

## Starting state, re-confirmed

Checked the standing brief's priorities before doing anything else:

- All four named presidents — Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley — already
  carry portraits.
- Every `leaders` entry with `role: "president"` or `role: "regent"` across all 61 years already
  has a portrait. Priorities 1 and 2 remain fully satisfied.
- 218 executive/Senate-officer/committee-chair names across the archive still have no portrait;
  166 of those are cabinet- or Senate-leadership-level (excluding rank-and-file senators).
- 12 years still carry no `years`-level context photograph.

## The idea the 16 September (third pass) report left open, followed through

That report flagged, untried: whether the Wayback Machine holds its own captures of
`digitalcommons.wku.edu`, which would sidestep the live Cloudflare "Just a moment..." challenge
on `/cgi/viewcontent.cgi` (re-confirmed still HTTP 403 today, same as every report since it was
first hit). It does. `web.archive.org`'s CDX API over **HTTPS** (the plain `http://` scheme is
blocked by this container's own egress policy, which reads as "Blocked by egress policy" rather
than reaching archive.org at all — worth remembering, since it looks exactly like the site being
down) returns real capture data, though a wide unfiltered domain query can time out or get
reset mid-transfer; a narrower, still-domain-wide `filter=original:.*talisman.*` query came back
clean and fast.

That query turned up **archived, HTTP-200, `application/pdf` captures of the WKU Talisman
yearbook PDFs from `digitalcommons.wku.edu/cgi/viewcontent.cgi` for essentially every year from
1906 through 1995**, including the run of years archive.org's own `talisman19NNwest` items do
not cover: 1982-1985 and 1988 onward. This is a second, independent source for exactly the gap
archive.org left, reachable without ever touching the live, Cloudflare-gated site.

Mechanics for the next run: query
`https://web.archive.org/cdx/search/cdx?url=digitalcommons.wku.edu&matchType=domain&filter=original:.*talisman.*&limit=2000&output=json&fl=original,statuscode,mimetype,timestamp`
(narrow the `filter` further, or drop `matchType=domain`, if a full run times out), then fetch a
chosen capture at `https://web.archive.org/web/<timestamp>id_/<original-url>` — the `id_` suffix
returns the raw file rather than a toolbar-wrapped page. **Retry on a fresh timestamp if the
first download reports success but `fitz` can't open all its pages** — one capture of
`talisman1989.pdf` came back as a curl "stream not closed cleanly" truncated at page 45 of 189
despite `curl` reporting HTTP 200; a different timestamp of the same file downloaded whole. Treat
a page-count/page-tree error from PyMuPDF as a signal to retry with another snapshot, not as the
file being unrecoverable.

**PyMuPDF (`import fitz`) was not actually importable this session** despite CLAUDE.md and
AGENT-INFO both saying it is installed — `pip install pymupdf` was needed first. Worth checking
at the start of a run that touches PDFs rather than assuming.

**Whether a given Talisman volume's PDF has an OCR text layer varies by volume**, and this
matters a great deal for how fast the ASG section can be found. The 1989 volume's text extracts
completely (591,000 characters, badly garbled by 1980s scan quality but present, enough to
`grep` for "ASG" and get a page number via `page.get_text()`). The **1994 volume has no OCR
layer at all** — `get_text()` returns only the TopSCHOLAR cover-sheet metadata, 3,118 characters
for the whole 148-page book — so finding a section means rendering and visually reading spreads.
Archive.org's own `fulltext/inside.php` "search inside" endpoint, used successfully in earlier
Talisman work on this project, is **specific to archive.org's own hosted books and does not
apply to a PDF pulled from a Wayback capture of digitalcommons** — there is no equivalent search
API for these; page-finding there is TOC-plus-visual-scan only.

## Two portraits added

**Lori Easton and Honor Logsdon, both 1988-89**, cropped from the "Associated Student
Government" group photograph, 1989 Talisman p. 198 (`digitalcommons.wku.edu/dlsc_ua_records/413`,
recovered via the Wayback capture above). The photograph's own caption reads "FIRST ROW: Amos
Gott, John Seiber, Scott Whitehouse SECOND ROW: Victor Click, Mari Knights, Lori Easton, Honor
Logsdon" — this is the same photograph already on file as the year's `1988-89-asg-executive.jpg`
context photo. Of the three people from this frame who already had portraits, only Scott
Whitehouse's was cropped from it: Amos Gott's comes from the Herald of 13 April 1989, p. 1, and
Victor Click's from the 1989 Talisman's junior portrait grid on p. 107. The reading order
therefore does not rest on three prior crops from this frame — it rests on the figure count (three
in front and four behind against the caption's three and four names), the back row reading one man
then three women as Click, Knights, Easton and Logsdon does, and two front-row anchors: Gott, named
first, is the man in glasses at front left, which his independent Herald portrait confirms, and
Whitehouse, named last, is the man at front right. Both `years.json` senate-member entries
(`Lori Easton` — "Freshman class officer sworn into ASG"; `Honor Logsdon` — "Potter College
Alternate, then off-campus representative, then Representative At-Large") give an exact name
match. Easton is third of four in the back row (the one with dark, voluminous hair); Logsdon is
fourth (striped shirt, shorter curly hair) — read off the left-to-right row order established
above and visually confirmed against the full-page scan before cropping either one.

**"Mari Knights"** (the caption's spelling) and **John Seiber** are also pictured in this same
photograph — Knights second in the back row (the blonde in the pale blouse), Seiber second in the
front row (the man in the patterned sweater), per the caption's own order — but neither has a standalone named
entry in `data/years.json` for 1988-89 to attach a portrait to. The person actually named in
`years.json` is "Mary Knights," and only inside another leader's note text (Lori Easton's:
"Sworn in with Dan Knowles, John Seiber and Mary Knights..."), not as her own list entry; John
Seiber's only standalone 1988-89-year entry does not exist either — his own named entry is for
1991-92, where he already has a different portrait on file. Per this agent's brief, `years.json`
is out of scope to create a new entry to attach to, so both were left alone rather than guessed
onto the nearest plausible year.

## A near-miss, caught before it landed: do not reuse a filename already on file

The 1989 Talisman also carries a full-page profile, "Images of Kim Summers: In the thick of
things" (p. 117, photo by Rob McCracken), with a pull-quote captioned "Kim Summers" — a strong,
individually-confirmable portrait naming the same Kim Summers already recorded in `years.json`
as 1987-88 Public Relations Vice-President and 1988-89 Rules and Elections co-chair. But she
already has a portrait on file for both years (from a *different* source, a 1987 Talisman
sophomore class portrait), saved under `1987-88-kim-summers.jpg` — the exact filename this run
independently chose for the new photo. Saving over it silently replaced the existing file on
disk before `build.py` caught the resulting duplicate `leaders` entry (one name, one year, two
sources) and refused to build clean. **Both the file and the JSON entry were reverted**
(`git restore` on the image; the duplicate JSON entry removed) rather than the older, already-
verified portrait discarded in favor of the new find — one photo per person per year is the
existing rule, and an already-sourced entry is not something this agent should silently overwrite
on a naming collision. The lesson for next time: check `data/photos.json` for the exact
`(name, year)` pair — not just whether the person is missing from a worklist — before writing a
new file, since the *file* can collide even when the JSON *entry* looks new.

## `build.py` / `check_data.py`

Both pass clean after the revert and the two genuine additions. `check_duplicates.py` reports
four pre-existing same-day-event pairs in `years.json`, unrelated to this run and out of this
agent's scope (photo metadata only).

## Left for the next run

- The Wayback-PDF route is open for 1982-1985 and 1988-1995 (and earlier). Untried this pass:
  1988, 1990, 1991, 1992, 1993, 1995 (parts a/b/c). 1994 is now closed — confirmed no SGA/ASG
  content anywhere in its "Organizations" section (pp. 178-209), which this particular volume
  ("Against All Odds") gives over entirely to magazine-style photo essays on other topics
  (ROTC, cheer, Habitat for Humanity, Black History Month, campus religious life, concerts) with
  no group-photo directory at all — a genuine negative result, not an unsearched one.
- 1995 (parts a/b/c, ~57MB+ each) was downloaded but not yet read; like 1994 it has almost no OCR
  text (1,244 characters across 51 pages for part A), so finding its Organizations section will
  need the same visual page-by-page approach once budget allows.
- 166 cabinet/Senate-leadership names across the archive still have no portrait; this run
  resolved 2 of them. The technique now exists to make faster progress on the 1988-1993 stretch
  specifically, where archive.org has nothing and the live site is blocked.
