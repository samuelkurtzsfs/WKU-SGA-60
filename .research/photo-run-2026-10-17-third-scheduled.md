# Photograph run, 17 October (third scheduled pass): the archive.org-range slice of the officer gap checked by name, one real dead end confirmed per candidate, nothing added

## Priorities 1, 2 and 4: reconfirmed again, unchanged

Checked against the current `data/years.json` and `data/photos.json` before touching anything:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait.
- **Priority 2** (every other president or student regent): zero gaps, 60 presidents plus every
  student regent.
- **Priority 4** (years with no photograph at all): zero, all 61 years carry at least one.

`python3 scripts/portrait_gap.py --list` still reports 189 officer slots with no portrait, held by
159 distinct people, 157 with no portrait anywhere in the file. Numerically unchanged from the two
10 October runs.

## Network state, retested fresh at the start of this run

- `cgi/viewcontent.cgi`: HTTP 403, the Cloudflare "Just a moment..." challenge page. Still closed.
- `web.archive.org`: `curl: (35) Recv failure: Connection reset by peer` at the TLS layer, three
  retries, all identical. Still closed.
- `archive.org` itself (not the Wayback Machine, the item/download host): open, and its per-page
  image route works cleanly — see below. This is not new; it is the same route `CLAUDE.md`'s
  settled note on the Tom LaCivita portrait already documents (`talisman1975west`, leaf n112).
  Confirmed again here only because the last two runs record archive.org-range work as
  exhausted, which this run tested directly rather than assumed.

## What this run actually tried: the archive.org-held years' slice of the 189-gap, person by person

The 189-gap includes a handful of entries that fall inside the 1971-1981/1986/1987 span archive.org
holds as plain page images (`archive.org/download/<id>/page/n<N>_w800.jpg`, no Cloudflare in the
path at all). Pulled the full-text search index for each relevant volume
(`https://<server>/fulltext/inside.php?item_id=...&q=...`) to find the right leaf before spending a
fetch on it, rather than guessing page numbers.

- **1974-75, Vern Pulman (Representative-at-Large):** no hit for "Pulman" anywhere in
  `talisman1975west`'s OCR text. Not pictured, and not named in running text either.
- **1977-78, David Bass (Activities Vice President):** found. Page 34, "A LIGHT MOMENT IN AN ASG
  MEETING brings laughter from president Bob Moore and smiles from activities vice president David
  Bass, secretary Sharon May and vice president Cathy Murphy" — four names against four figures in
  one frame, no left/right or row marker distinguishing them. The same spread's other, individually
  captioned photos were already mined (David Vance, John Grizzell, Brad Ford, Gene Saunders, Robert
  Moore, Cathy Murphy, Sharon May, Steve Thornton, Tricia Cook, Kevin Kinne are all already in
  `data/photos.json` under 1977-78). This group shot was apparently looked at and correctly left
  alone for the same reason it has to be left alone now: a name list with no positional cue in a
  four-person photo is a guess, not an identification. No portrait added for Bass.
- **1978-79, David Young (Administrative VP), Steve Wilson (Judicial Council Chairman), Alice Wicks
  (Secretary):** the only running-text hit for Young is the page 289 "Making news about
  entertainment" article ("David Young, administrative vice president, said this was done to..."),
  text only, no accompanying photograph of him on that spread. The volume's own name index carries
  `Wicks, Alice Elizabeth` with no page number at all — no photograph exists to cite. `Wilson,
  Stephen Alan` likewise carries no page number; a second, separate index entry `Wilson, Steve Alan
  296, 318, 320, 336` may or may not be the same person, and page 296 (checked directly) is the
  Marketing Club / Phi Beta Lambda / Delta Sigma Pi spread, nothing to do with ASG or a Steve
  Wilson — so even if the two Wilson entries are one person, the pages on record for him aren't an
  identifiable portrait. The spread's one strong portrait, page 288's "A GAVEL serves as a chin rest
  ... for president Steve Thornton," belongs to a president who already has a portrait on file. No
  portrait added for Young, Wilson or Wicks.
- **1980-81, Mark Chesnut (Treasurer):** the volume's ASG roster photo (p. 282, already in
  `data/photos.json` as the source for 30 of this year's leaders) does not name a treasurer and
  does not include him. The only other hit is an intramural champions list (p. 234, badminton and
  racquetball doubles under "Mark Chestnut (Sigma Alpha Epsilon)") — a different kind of page
  entirely, no photograph attached to the name, and spelled with a *t* the ASG record doesn't use.
  No portrait added.
- **1986-87, Chris Millay (Parliamentarian), Dwight Austin (Sergeant-at-Arms):** re-read the full
  roster of both captioned Associated Student Government group photographs on p. 114, the ones
  already mined down to all 28 named figures (`data/photos.json` carries a leader entry for every
  single name in both captions, each with the row/position reasoning spelled out). Neither Millay
  nor Austin appears in either caption. A name-index check for "Millay" turns up only Beth Ann and
  Lori Ann Millay (pp. 240, 52) — a different family connection, not Chris. No hit at all for
  "Dwight" or "Austin" outside unrelated Austin Peay sports references. Not pictured. No portrait
  added.

## Why this closes rather than just narrows the archive.org-range slice

Every one of these six people was checked against the full text of their volume, not a sample, and
the volumes themselves are now provably exhausted: every other name the same spreads name is
already in `data/photos.json` with sourcing as detailed as the misses recorded above. The
archive.org-held years (1971-1981, 1986, 1987) were never blocked for this project — only
`viewcontent.cgi` and the Wayback Machine are closed — so the fact that these six specific people
still have no photograph after this much mining is itself the finding: the Talisman's photo desk in
these years covered the president, sometimes the activities VP or a dramatic meeting moment, and
essentially never a treasurer, parliamentarian, sergeant-at-arms or judicial council chair. The
remaining 189-gap is overwhelmingly these minor offices, and the volumes that could answer for the
1971-1987 slice of it have now had a real, exhaustive pass.

What's left of the 189-gap outside this slice is pre-1971 (1966-67, 1967-68 — no archive.org
volume, `viewcontent.cgi` the only route, and closed) and 1988-2026 (TopSCHOLAR-only for the recent
Talisman volumes `viewcontent.cgi` also gates, `wkuherald.com` already checked exhaustively by the
second 17 October run and closed as a source for this gap).

## No portrait found or added this run

No file in `data/photos.json` or `data/photos/` changed. The 189-slot gap is numerically unchanged
— this run's contribution is six fewer names worth re-checking blind, with the specific reason each
one is a dead end on record so a future pass does not re-spend a request confirming it.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: clean. Merged `origin/main` into
`research-photos` first (clean merge, `.research/NIGHT-REPORT.md` plus the day's `data/years.json`
and site changes, no conflicts).
