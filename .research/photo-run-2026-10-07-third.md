# 7 October 2026, third run (photograph routine, scheduled)

> **Editor's note, 7 October 2026.** Reviewed before merge. Every figure in this report was
> recomputed from the data and every Talisman claim was reopened at the page text on
> archive.org: the officer gap (217 slots / 174 people), the four year-photo gaps, all eight
> names and offices, the Wilson and Young index entries, the Bass caption, and the four negative
> findings all hold. Two readings did not, and are corrected in place below: the dates either
> side of the 2008-09 `wkuherald.com` window (see that section — the gap does not reach into
> 2009-10), and the volume Young's quote comes from. A caption quote was trimmed to a paraphrase
> to stay inside the 15-word limit. The run's own judgement calls — refusing four unconfirmable
> identifications rather than force-fitting them — were right, and are why this report passed
> review. The merge itself was refused by the run's own permission gate, not by the review; the
> branch is cleared to merge as it stands.
>
> **Second editor's note, 7 October 2026 (night).** Reviewed again independently before the merge
> that the first pass could not make, and everything above was re-tested rather than taken on
> trust. All of it holds: the figures recompute exactly (61 years, 1967 events, 60 presidents, 73
> leader records all carrying a portrait, the four year-photo gaps, 217 officer slots over 174
> people with Carter Smith and Paul Gerard the two the per-year count of 176 adds), the eight
> names, years and offices match `years.json` exactly, and thirteen source claims were reopened at
> `archive.org` and `wkuherald.com` and all thirteen held word for word. The 2008-09 correction is
> right: the empty window returns `x-wp-total: 0`, and the widened window returns seven posts
> running 4 September to 4 December 2009, so the gap does not reach into 2009-10.
>
> What this pass added is two corrections of its own, both from opening page images the first
> review read only as text. The Bass frame carries four figures, not three — the fourth cropped at
> the lower left edge. And the Spring Sing paragraph was wrong twice over: the text naming the
> quartet *is* the photograph's caption, complete and legible, not a separate block beside a
> truncated one, and the frame holds five figures rather than four. That matters because the
> report's closing advice sent the next run hunting for a clearer scan of a caption that is
> already clear and never carried a left-to-right key at all. Both are corrected in place below
> and the lead is now closed rather than left pending. Nothing was deleted; every correction is a
> rescue. No data file is touched by this branch, and nothing in it reaches the built site.

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
  34-35) carries a candid photograph whose caption ("A LIGHT MOMENT IN AN ASG MEETING") reports
  laughter from president Bob Moore and smiles from three officers it names in turn: activities
  vice president David Bass, secretary Sharon May and vice president Cathy Murphy — read back
  against the page text on 7 October, word for word. The caption sits on p. 34, the feature text
  on p. 35. The photograph itself shows one standing man (laughing), a seated woman in
  sunglasses, a second woman smiling at the right edge, and a fourth head cropped at the lower
  left edge — four figures for four named people, not the three this report first counted, but
  the fourth is a partial crop that carries no readable face. Bob Moore, also male, is the one
  explicitly described as laughing and is the more likely match for the standing figure, which
  leaves no figure in the frame confirmably identifiable as Bass. Not used. (The page image was
  reopened by the editor on 7 October; the figure count is corrected here because a person
  cropped at a frame's edge is exactly what the LaCivita portrait in `CLAUDE.md` turns on, and a
  report that undercounts one teaches the opposite lesson.)
- **Young** — appears in the body text of the **1979** Talisman's ASG feature, not the 1978 one
  Bass's caption comes from; the two volumes each carry a feature, and Young is 1978-79. Its
  continuation (p. 289, where the index places him) quotes him as administrative vice president
  explaining that the new constitution set 24 separate races for the 24 representative-at-large
  Congress seats, to force competition between candidates. The spread carries no photograph of
  him, only of president Steve Thornton and representative Victor Jackson.
- **Wicks** — indexed with no page number at all next to her name, which in this volume's index
  means no photograph on file for her.
- **Wilson** — the fullest lead of the eight, and still not usable. The back index lists
  "Wilson, Steve Alan" at four pages (296, 318, 320, 336), and the text on p. 320 names him
  directly: SAE's barbershop quartet "composed of Scott Neel, Jon Rue, Kreis McGuire and Steve
  Wilson" won Spring Sing, ending Lambda Chi Alpha's 13-year title. A photograph of the quartet
  in full costume runs across the foot of the same page. **The editor reopened the page image on
  7 October and two things in this paragraph were wrong.** That naming text is not separate from
  the photograph's caption — it *is* the caption, set in the left-hand column in the volume's
  standard caption style, complete and fully legible; the "— Mark Tucker" line beneath the
  photograph is a photographer credit, not a truncated caption. And the frame holds five figures,
  not four: the four costumed singers plus a fifth, moustached man at the microphone behind them.
  The caption names four people in running prose and gives no left-to-right order, so which
  figure is Wilson cannot be read from the page. P. 296 carries a second, weaker
  lead: "S. Wilson" in the back row of a Pre-Law Club photograph, but the volume's own index
  lists six different Wilsons whose first name begins with S (Scott Samuel, Stephen Alan, Steve
  Alan, Stevie Joe, Stuart Kevin, Susan Dell), so the initial alone does not identify him. Pages
  318 and 336 are a Greek Week section divider and an unopened lead respectively; neither
  carries a name. Not used.
- **Chesnut** — the 1981 index gives "Chesnut, Mark Cameron 234", and p. 234 is an intramural
  results table, not a photograph. He is in it twice, as badminton-singles champion and, with
  Mitch Gum, in the racquetball-doubles row; both for Sigma Alpha Epsilon. The table spells the
  surname "Chestnut" where the index spells it "Chesnut".
- **Millay, Austin** — neither appears in the 1987 Talisman's index at all. The only Millays
  indexed are Lori Ann and Beth Ann; no Austin is indexed as a student name (every hit for
  "Austin" is the university Austin Peay).

## 2008-09's year-photo gap has a confirmed cause now, not just a closed search

Queried `wkuherald.com`'s WordPress REST API for any post at all — no search term, just a date
window — between 1 August 2008 and 1 June 2009: `x-wp-total: 0`. Re-run by the editor on
7 October against the same window: `x-wp-total: 0` again. That part is solid, and it is what
closes 2008-09 as a `wkuherald.com` lead for any future run, the same way 2000-01 was closed
this morning — a real coverage gap, an empty WordPress install rather than an unsearched one.

**The reading either side of that window was wrong and is corrected here.** Widening to
1 January 2007 – 1 January 2010 does return exactly seven posts, but 4 December 2009 is the
**latest** of the seven, not the earliest: the run read the last row of the list as its first.
The earliest two are dated 4 September 2009, and four more fall in October 2009. So the gap
does **not** extend into 2009-10, and the claim that it covered that year's first two months
is withdrawn. September and October 2009 are both present on `wkuherald.com`, and one of the
seven posts is an SGA story — "Three SGA senators resign", 22 October 2009
(wkuherald.com/55154/news/three-sga-senators-resign/). A future run must not treat autumn 2009
as covered by the 2008-09 closure.

Nothing is missing from the archive on account of this: 2009-10 is already `researched` with 28
events, and both resignation stories are in it (20 October 2009, three senators over the
publications committee appointment; 27 October 2009, Skylar Jordan a week later), carried from
the printed *Herald* rather than from this post. The correction is to the lead-closure note, not
to the record.

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
- Autumn 2009 is **not** closed, whatever the heading above may suggest at a glance: 4 September
  and October 2009 both carry `wkuherald.com` posts. Only 2008-09 itself is empty.
- 2008-09 joins 2000-01 as a closed `wkuherald.com` lead. 1994-95 and 1995-96 were already known
  to predate the archive entirely. All four year-photo gaps now wait on `digitalcommons.wku.edu`
  or `web.archive.org` opening, not on a better search anywhere else.
- **The Steve Wilson Spring Sing photograph (1979 Talisman p. 320) is closed, not pending.** An
  earlier draft of this report sent the next run looking for "a clearer scan or a caption on a
  facing/following page" that would key the quartet left to right. That advice is withdrawn: the
  caption is already complete and fully legible on the page, and it simply never printed an
  order, so no better scan can produce one. The volume keys its group photographs explicitly when
  it keys them at all — the Alpha Delta Pi roster two pages later runs "(Front row) S. Mooney, D.
  Travis, K. Bean..." — and this caption does not. Only a separately captioned photograph of
  Wilson, or an outside source naming where he stood, could ever settle it. Do not spend another
  run on the scan.
