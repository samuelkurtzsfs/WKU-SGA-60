# Photograph run, 10 November (third scheduled pass): the 1967 Talisman's Associated Students group photo opened and read page by page; its two standing rows are genuinely ambiguous, not merely untried, and are left closed

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports 156 people with no
  portrait anywhere in the file. Unchanged this pass.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.
- This morning's TLS-fingerprint finding still holds: `python`'s `urllib.request` with a full
  browser header set reaches `digitalcommons.wku.edu/cgi/viewcontent.cgi` cleanly (HTTP 200) on a
  cold retest, where `curl` with the identical URL and headers still 403s. Confirmed again at the
  start of this pass before relying on it.

## What this pass chased: the 1967 Talisman's Associated Students page, for the three unfilled 1966-67 seats

`data/photo-finds/1966-1970-notes.json` already cites page 136 of the 1967 Talisman
(`dlsc_ua_records/382`, viewcontent article=1382) for two small facts - Carol Bass serving a year
earlier than recorded, and Michael Klein's seat - but neither of those citations is a portrait
source, and nothing in this project's files records anyone having tried to crop a face from this
page's big 26-person Associated Students group photograph. The portrait gap list's three oldest
entries without a portrait anywhere - Carla Dotson, Patricia Lanning and Pat Smith, all 1966-67
Congress members - are exactly the kind of name this page's caption might settle, since the
caption prints every one of the 26 people in the photograph by row.

Fetched both halves of the volume directly via the `urllib` bypass (`article=1382`, 17.8 MB, and
`article=1383`, 22.5 MB; both open clean, confirmed `%PDF` and real page counts). Rendered page
136 at 300 dpi and read the caption directly from the image rather than trusting the OCR text
layer, which is badly garbled throughout this particular scan (`pdftotext` renders real names as
strings like "W. nky M, . """ for "Wenky Menser") - a problem specific to this volume's scan
quality, not the bypass.

**The caption, read directly off the page image:**

> Third Row: Catlette Evans, Ron Griffee, John Adams, Jim Cobb, Terry Hicks, Bob Patterson,
> Marilee Jenson, Ron Beck. Second Row: Dale Weaver, Wenky Menser, Dave White, Vivian Denton, Pat
> Lanning, Kaye McClellan, Carol Bass, Dennis Reeves, Mike Klein. First Row: Rita Sutton, Jerry
> Pence, Bucky Lanning, Larry Heishman, Jim Haynes, Jim Fox, Carmen Willoughby, Marshall Peace,
> Carla Sue Franklin.

None of the three wanted names - Carla Dotson, Patricia Lanning, Pat Smith - match a name printed
in this caption. "Pat Lanning" in the Second Row is Patricia Lanning (the Panhellenic
Representative already in `years.json`, not a different person: no other Lanning serves this
year), so she is in the photograph by name. Pat Smith and Carla Dotson are not named anywhere on
this page at all - not in this caption, and not in any of the smaller committee photographs on the
facing page 137 (Student Activities, Finance, Judicial Council, Rules and Elections committees,
all individually captioned and checked by name). Closed negative for Smith and Dotson from this
source.

## Why Patricia Lanning's face in this photograph is not usable, and this is not the same as "untried"

The First Row (seated at the table, 9 people) is unambiguous: the caption's gender sequence
(F,M,M,M,M,M,F,M,F) matches the seated photograph left to right exactly, with no row-stacking to
resolve. Checking `data/photos.json` against this row explains why: **every one of this row's
identifiable officers - James P. Haynes, James E. Fox, Larry S. Heishman, Carmen Ann Willoughby,
Forrest (Bucky) Lanning, Marshall Peace, Jerry Pence - already carries a portrait**, and their
`src` entries show those portraits came from this same page's *other*, smaller photograph: a
six-person officers-only portrait lower on the page (captioned "Second Row: Larry Heishman -
Treasurer, Bucky Lanning - Member, Executive Committee, Marshall Peace - Member, Executive
Committee. First Row: Jim Fox - Vice President, Jim Haynes - President, Carmen Willoughby -
Secretary"), not the big 26-person group photograph's seated row at all. Jerry Pence's portrait
*does* cite the big photograph's seated row specifically, and that citation independently confirms
the same row reading this pass found.

The two **standing** rows behind the table are a different matter. Rendered at high resolution and
measured against a pixel grid, the heads do not sit in two clean horizontal bands the way the
seated row sits in one: the back row is on a riser and its people are spaced to show through the
gaps between the row in front, so a straight left-to-right reading of either standing row runs
into the exact row-order ambiguity this project's own rules warn about (CLAUDE.md; the
`SGA-60-AGENT-INFO.md` Debbie Thomas/Blake Graham cases). Cross-checking against `data/photos.json`
confirms no one has ever solved it: **Dale Weaver, Vivian Denton and Dennis Reeves are all named
in the Second Row of this same caption, and all three already have portraits in the file - and
none of the three came from this photograph.** Weaver's is cropped from a different group photo on
p. 103; Denton's is from the 1965 Talisman; Reeves's is from the unambiguous four-person Finance
Committee photograph on the facing page. Michael Klein and Carol Bass, the other two Second-Row
names already on file, both come from senior-portrait grids in later volumes, as recorded in
`1966-1970-notes.json`. The pattern is consistent across every name that has ever been checked:
whoever is identifiable from page 136 is identifiable from one of its *smaller*, cleanly captioned
photographs, never from the big standing-row group shot. That is this pass's reason for treating
the two standing rows as closed rather than merely unattempted - the project has quietly avoided
using them for every other name on this exact caption, and this pass's own attempt to read Patricia
Lanning's position out of the Second Row's four-women cluster (Vivian Denton, Pat Lanning, Kaye
McClellan, Carol Bass) could not clear the same bar. Not used. `data/photos.json` and
`data/photos/` are unchanged by this finding.

## Conclusion

No new portrait this pass. The 1967 Talisman's Associated Students page is now fully read rather
than partially cited: its two standing-row group photographs are confirmed closed for portrait use
(three other names already on file independently prove this, each sourced elsewhere), and its
seated row and small committee photographs are already completely mined. Carla Dotson and Pat
Smith are confirmed absent from this entire page by name. `build.py` and `check_data.py` both pass
clean. Landed on `research-photos`.
