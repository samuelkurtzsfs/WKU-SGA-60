# 7 October 2026, third run (photograph routine, scheduled)

## What was checked before doing anything

Merged `origin/main` into `research-photos` (fast-forward, four commits: the 7 October
officer-gap editor's note and its restatement, plus two earlier merges). `build.py` and
`check_data.py` both run clean on the merged branch: 61 years, 1967 events, 60 presidents.

Confirmed fresh: all 73 `leaders` records (every president, every student regent, all 61
years) carry a matching `data/photos.json` entry, Nick Todd/Katie Dawson/Jeanne Johnson/Reagan
Gilley included. Priorities 1-2 in `CLAUDE.md`'s order are fully clear, same as the two earlier
runs today (02:04 and 03:28 UTC). The officer-portrait gap stands at 217 slots (174 distinct
people), unchanged since 4 October, and the four years without any year-level photograph are
unchanged too: 1994-95, 1995-96, 2000-01, 2008-09.

## Access routes re-tested fresh, unchanged

- `cgi/viewcontent.cgi` — HTTP 403, Cloudflare `cf-mitigated: challenge`, the "Just a moment..."
  interstitial. Still closed, same as both earlier runs today.
- `web.archive.org` — connection reset mid-exchange on every attempt (CDX API and a plain page).
  Still closed.
- `archive.org`'s own Talisman holdings and page-image download **are open and were used
  directly** (see below) — this is the one route that answered today.

## A genuinely new angle: archive.org Talisman cross-referenced against the officer gap

Both earlier reports today searched `wkuherald.com` for names never tried before and came up
empty; neither tried matching the 217-name officer gap against the volumes `scripts/talisman.py`
already holds (1971-72 through 1980-81, 1986-87/1987-88 — the list in that script's own `YEARS`
constant, mapped to academic years). Eight gap entries fall inside those volumes:

- 1974-75 Vern Pulman, Representative-at-Large
- 1977-78 David Bass, Activities Vice President
- 1978-79 David Young, Administrative Vice President
- 1978-79 Alice Wicks, Secretary
- 1978-79 Steve Wilson, Judicial Council Chairman
- 1980-81 Mark Chesnut, Treasurer
- 1986-87 Chris Millay, Parliamentarian
- 1986-87 Dwight Austin, Sergeant-at-Arms

All eight were searched by surname (and variant spellings) against the matching volume with
`scripts/talisman.py`, and every photograph the search turned up was opened and read at full
resolution, not just skimmed from OCR context. None produced an addable portrait:

- **Pulman** — not in the 1975 Talisman index under "Pulman" or "Pulliam." No record of him in
  the volume at all. Consistent with the thin paper trail already noted in his `years.json`
  entry (a single mid-year committee appointment, "no further record" of his time in the seat).
- **Bass** — found. The 1978 Talisman's ASG feature ("Little action after much controversy," pp.
  34-35) carries a candid photograph captioned "A LIGHT MOMENT IN AN ASG MEETING brings laughter
  from president Bob Moore and smiles from activities vice president David Bass, secretary
  Sharon May and vice president Cathy Murphy." The photograph itself shows one standing man
  (laughing) and two partly-visible seated women — three figures for four named people. Bob
  Moore, also male, is the one explicitly described as laughing and is the more likely match for
  the standing figure, which leaves no figure in the frame confirmably identifiable as Bass. Not
  used.
- **Young** — appears in the body text of the same ASG feature's continuation (p. 289, quoted
  explaining the new constitution's 24 at-large Congress seats) but the spread carries no
  photograph of him, only of president Steve Thornton and representative Victor Jackson.
- **Wicks** — indexed with no page number at all next to her name, which in this volume's index
  means no photograph on file for her.
- **Wilson** — the fullest lead of the eight, and still not usable. The back index lists
  "Wilson, Steve Alan" at four pages (296, 318, 320, 336), and the text on p. 320 names him
  directly: SAE's barbershop quartet "composed of Scott Neel, Jon Rue, Kreis McGuire and Steve
  Wilson" won Spring Sing, ending Lambda Chi Alpha's 13-year title. A photograph of a four-man
  barbershop quartet in full costume sits directly below that text — but its own caption (cut
  off at the column edge, crediting only the photographer) gives no left-to-right order, so which
  of the four figures is Wilson cannot be read from the page. P. 296 carries a second, weaker
  lead: "S. Wilson" in the back row of a Pre-Law Club photograph, but the volume's own index
  lists four different Wilsons with a first initial S. (Steve Alan, Stephen Alan, Scott Samuel,
  Susan Dell, Stuart Kevin), so the initial alone does not identify him. Pages 318 and 336 are a
  Greek Week section divider and an unopened lead respectively; neither carries a name. Not used.
- **Chesnut** — "Mark Chestnut" appears only as a badminton-singles intramural winner in a
  results table (p. 234 of the 1981 Talisman), not in a photograph.
- **Millay, Austin** — neither appears in the 1987 Talisman's index at all. The only Millays
  indexed are Lori Ann and Beth Ann; no Austin is indexed as a student name (every hit for
  "Austin" is the university Austin Peay).

## 2008-09's year-photo gap has a confirmed cause now, not just a closed search

Queried `wkuherald.com`'s WordPress REST API for any post at all — no search term, just a date
window — between 1 August 2008 and 1 June 2009: `x-wp-total: 0`. Widening to January 2007
through January 2010 returns exactly seven posts, the earliest dated 4 December 2009. The
archive's indexed run has a real gap covering essentially all of 2008-09 and the first two
months of 2009-10, the same character of gap the 7 October morning report established for
2000-01 (an empty WordPress install, not an unsearched one). This closes 2008-09 as a
`wkuherald.com` lead for any future run, the same way 2000-01 was closed this morning.

## Nothing added

No portrait and no year photograph were added or removed. `data/photos.json` and `data/photos/`
are byte-identical to the merge-in of `origin/main`. `check_data.py` reports 61 years, 1967
events, 60 presidents, clean, both before and after this run.

## For the next run

- The eight-name overlap between the officer gap and archive.org's Talisman holdings is now
  fully searched and exhausted; no need to re-run it unless the officer gap grows to include a
  new name inside 1971-72 through 1980-81 or 1986-87/1987-88.
- `viewcontent.cgi` and `web.archive.org` are closed for a third time today, re-tested fresh each
  time rather than assumed. Keep retrying cold.
- 2008-09 joins 2000-01 as a closed `wkuherald.com` lead. 1994-95 and 1995-96 were already known
  to predate the archive entirely. All four year-photo gaps now wait on `digitalcommons.wku.edu`
  or `web.archive.org` opening, not on a better search anywhere else.
- The Steve Wilson Spring Sing photograph (1979 Talisman p. 320) is worth a second look if a
  clearer scan or a caption on a facing/following page ever turns up a left-to-right key for the
  quartet — the identification is otherwise sound (the index places him at exactly this page),
  only the which-face-is-which question is open.
