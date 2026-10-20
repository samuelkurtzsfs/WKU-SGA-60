# Photograph run of 20 October (scheduled): baseline unchanged, both blocked routes retested and still closed, one fresh article checked and nothing in it to add

## Priorities 1, 2 and 4: reconfirmed by script, not by reading the brief's own word for it

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked against
  `data/photos.json` directly before touching anything. All four already carry a portrait, as
  every run since August has found.
- **Priority 2** (every other student body president or student regent): `check_data.py` reports
  no missing leader portrait across all 73 `leaders` records, 61 years.
- **Priority 4** (years with no photograph at all): zero. Every year carries at least a leader
  portrait or a year-level photograph.

## Priority 3: the gap, re-measured, not re-searched a twenty-first time

`python3 scripts/portrait_gap.py --list`: 189 officer slots, 159 distinct people, 157 with no
portrait anywhere in the file — unchanged from every run since 15 October. `data/photos.json` has
not gained an entry in that same window. Rather than re-running the same name list against the
same closed routes again, spent this run's budget on access and on the one genuinely new item
since the last pass.

## Network state, retested fresh

- `cgi/viewcontent.cgi`: HTTP 403, Cloudflare "Just a moment..." challenge, confirmed with a plain
  `curl` carrying the full navigation header set. Still closed.
- `web.archive.org`'s `if_` bypass: `curl: (35) Recv failure: Connection reset by peer` on two
  attempts five seconds apart, confirmed at the agent proxy as `ws_closed_mid_exchange`. Still
  closed, not intermittently open this session.
- `archive.org` (the plain item/download host): open, confirmed with a fresh `_djvu.txt` pull of
  the 1978 and 1979 *Talisman* volumes. Covers only 1971-1981, 1986 and 1987, a range this
  routine's prior passes have already worked through repeatedly.
- `wkuherald.com`'s WP-JSON API: open, used below.

## The one new item since the 19 October runs: no new lead

`wkuherald.com`'s most recent SGA-tagged post is "SGA funds new Preston Center area, rental
services, campus events" (14 Oct 2026, `wkuherald.com/98116/...`), posted after the last
photograph run read the feed. Its featured image (media id 98118) captions as "Student Body
President Caden Lucas presents his officer report during a SGA meeting... Tuesday, Oct. 13,
2026" — Lucas already carries a portrait, so this is not a new identification, just a newer
photograph of a person already pictured. Read the full article body for any other named officer:
it names only Lucas, CFO Will Derryberry (no photograph, already pictured from an earlier
occasion) and guest speaker Rachel Goodman (WKU staff, not an SGA officer and outside this
project's scope). **Elizabeth Allen and Tyreesha Morris**, the two officers newest to the record
without a portrait (checked and declined 19 October), are not named in it. No lead to add.

## Why this note is short

Both routes that hold the bulk of the unexploited pre-2003/pre-2012 leads — `viewcontent.cgi` and
`web.archive.org` — have now read closed on every attempt across at least six calendar days.
`archive.org` and `wkuherald.com`, the two routes genuinely open from this container, have been
swept repeatedly enough that a new post is the only thing left to check each pass; today's new
post carried nothing. No file in `data/photos.json` or `data/photos/` changed this run.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61 years, 60
presidents, no missing leader portrait, no year without a photograph). Landed on `research-photos`.
