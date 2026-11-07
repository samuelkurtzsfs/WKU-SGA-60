# Photograph run, 21 October third scheduled pass: baseline reconfirmed, archive.org's actual Talisman holdings pinned down, a batch of recent-era gap names checked with nothing to add

## Priorities 1, 2 and 4, checked directly against the current file

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`. Confirmed by reading each entry, not by trusting the last note.
- **Priority 2**: zero presidents and zero student regents without a portrait, 61 years, 60 people.
- **Priority 4**: all 61 years carry at least one year-level photograph (`photos.years`).

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: HTTP 403, Cloudflare "Just a moment..." challenge,
  tested against the SGA-photographs finding aid lead (article=1619, context=dlsc_ua_fin_aid).
  Landing pages on the same host (e.g. `dlsc_ua_fin_aid/620` itself) still answer 200.
- `web.archive.org`: connection reset mid-exchange at the egress proxy before TLS completes,
  confirmed against the proxy's own status endpoint. Still closed.
- `archive.org` (plain item host, not `web.`): open, used below.

## A concrete fact pinned down this pass: what archive.org actually holds

Earlier notes in this file and in `SGA-60-AGENT-INFO.md` §4 record archive.org's WKU Talisman
holdings only as "1971-1981, 1986, 1987," with "does not hold 1967-1970 or 1982-1985" stated
explicitly but nothing said about 1988 onward. Several `.research/photo-run-*.md` files from
September also mention identifiers like `talisman1994west`, `talisman1996west`, `talisman2001west`
in passing, which could be read as implying those volumes exist there and have already been mined.

Queried archive.org's own `advancedsearch.php` API directly for `identifier:talisman*west` rather
than guessing or trusting a prior mention: it returns exactly **19** WKU ("west") identifiers, and
they are 1943, 1946, 1947, 1963-1965, 1971-1981, 1986, 1987. Nothing after 1987 exists under this
naming pattern, confirmed with a second query restricted to `19*west` and a plain-text `curl` of
several specific `_djvu.txt` URLs (1988, 1989, 1990, 1993, 1994, all 503 "Error" pages, not real
content — and archive.org's `/details/talisman1990west` page itself 404s, which a 503 could not
distinguish from a transient fault). So the gap years this project most needs for the officer
backlog — 1988-89 through 2002-03 — have **no** Talisman volume on archive.org at all, not an
untried one. The only copies of those yearbooks are the `dlsc_ua_yearbooks` PDFs on
digitalcommons.wku.edu, reachable only through the blocked `viewcontent.cgi`. This closes the
question of whether archive.org's Talisman holdings for this stretch were ever genuinely
unexhausted — they were never there to exhaust — and it should replace the vaguer prior wording
in `SGA-60-AGENT-INFO.md` §4 the next time that file is touched.

## Priority 3: four recent-era gap names, tried fresh through live web search

Picked four names from `scripts/portrait_gap.py --list --any-year`'s 2016-2023 slice that had not
obviously been exhausted in the 7-13 October reports (Josh Zaczek, Cassidy Townsend, Nathan Cherry,
Justin Goins) and searched each by name plus their office, on the chance that a source outside
`wkuherald.com`'s own search (already tried repeatedly) would turn up a photograph:

- **Josh Zaczek** (Legislative Research Committee Head, 2019-20): found in SGA's own senate
  minutes (`minutes_11_12_19.pdf`, `minutes_9_15_20.pdf`, `minutes_9_22_20.pdf`) confirming the
  office, no image.
- **Cassidy Townsend** (SGA SAVES Chair, 2018-19): no result named her at all; the search surfaced
  only a same-named person at a different university. Still unlocated by any method.
- **Nathan Cherry** (Speaker of the Senate, 2016-17): found in SGA's own senate minutes
  (`smm_3_21_17.pdf`, `smm_3_28_17.pdf`), text only, no image.
- **Justin Goins** (Chief Justice, 2022-23): found in a Judicial Council minutes PDF
  (`jc_minutes_1_20_23.docx`... rendered as PDF in the search), text only, no image.

All four hits are primary-source text documents SGA itself produced — minutes — which read exactly
as CLAUDE.md predicts for this office and era: real confirmation of the role, never a photograph.
No new portrait lead from this batch.

## A genuinely new route found and partly tested: archive.org's IIIF image endpoint

The 20 October third-scheduled-pass note (on this same branch) describes pulling Talisman page
images "directly from archive.org's JP2 scans" for three names, bypassing the blocked
`digitalcommons.wku.edu` PDF endpoint entirely, but does not record the mechanism. Rediscovered and
pinned down here: `https://iiif.archive.org/iiif/<identifier>$<leaf>/full/<size>,/0/default.jpg`
serves a real JPEG of one page directly, with no `viewcontent.cgi` and no `web.archive.org`
involved — confirmed with leaves 0, 295, 305 and 310 of `talisman1979west`, all genuine page
images (two of them the "Organizations" section, printed pages 293 and 303).

**The `<leaf>` index is not the printed page number.** Comparing the printed folio visible on
leaf 295 ("293") and leaf 305 ("303") against their leaf numbers gives a consistent offset of
exactly 2 for this volume: `leaf = printed_page + 2`. This offset is front-matter-dependent and
should be re-derived per volume, not assumed to transfer.

Used this to target **David Young** (Administrative Vice President, 1978-79, currently a gap):
the student directory/index at the back of `talisman1979west` (`grep -n "Young, David"` in the
`_djvu.txt`) gives "Young, David Paul 289", which by the offset above is leaf 291. The route itself
is real — leaves 0, 295, 305, 310 all came back as genuine images earlier in this session — but
`iiif.archive.org` then closed mid-session before leaf 291 (or neighbours 290/292) could be
fetched: four consecutive attempts came back `connection reset by peer` at the egress proxy, and a
fifth attempt against leaf 310 — which had answered cleanly minutes before — reset the same way,
confirming the window shut rather than that leaf 291 specifically is bad. This is the same
open-and-close-within-the-hour pattern `SGA-60-AGENT-INFO.md` §8.4 already documents for
`viewcontent.cgi`; it evidently applies to this endpoint too.

Also checked while the index was open, text only, no image fetch needed: **Alice Wicks**
(Secretary, 1978-79) appears in the same `talisman1979west` directory as "Wicks, Alice Elizabeth"
with **no page number** — every neighbouring entry that has an individual portrait carries one
(e.g. "Wickson, Dick 241" two lines below), so the absence is suggestive that she has no individual
senior portrait in this volume, though an index gap is not certain proof the way a confirmed page
number would be. **Chris Millay** and **Dwight Austin** (Parliamentarian and Sergeant-at-Arms,
1986-87): searched `talisman1987west`'s full text directly; Millay's only hit is a different person
(Lori Millay of Owensboro, a commencement-photo caption, unrelated), and Austin does not appear at
all outside "Austin Peay" (the university).

**For the next run:** the IIIF route is worth trying again on a fresh window, specifically leaf 291
of `talisman1979west` for David Young — the index page number and the offset are already worked
out, so a future pass can go straight to the fetch rather than re-deriving either. Nothing in
`data/` changed from this lead; no portrait was identified or added.

## What this run leaves unchanged

`data/photos.json` and `data/photos/` are unchanged from the last commit on this branch. 189
officer slots (159 people) remain without a portrait, per `scripts/portrait_gap.py` — unchanged.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61 years, 1964
events, 60 presidents, no missing leader portrait, no year without a photograph). Landed on
`research-photos`.

## For the next run

The two blocked routes remain the ceiling on this backlog, as every pass since mid-September has
found. What is new this time is narrower and negative: archive.org's Talisman run genuinely ends
at 1987, so no run should spend time hunting for an 1988-2002 volume there again, and this run's
four fresh name searches confirm again that the 2003-2025 slice's remaining names surface only in
SGA's own text minutes, not in any indexed photograph. Nothing in this pass argues for raising or
lowering this trigger's firing frequency beyond what the 21 October second-pass note already said.
