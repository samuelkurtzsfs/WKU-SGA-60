# Photograph run, 16 October (third scheduled pass): gap unchanged, a new sweep method tried and closed

## Priorities 1, 2 and 4: reconfirmed, with the portrait files themselves checked this time

Checked `data/photos.json` against `data/years.json` before anything else, per CLAUDE.md's
"check whether an earlier run already got them." All three priorities are unchanged from the
last two passes today:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four carry a
  portrait entry. This pass went one step further than re-reading the JSON and read the actual
  bytes of each file on disk:
  - `2004-05-nick-todd.jpg` — `ff d8 ff e0`, 53,122 bytes
  - `2005-06-katie-dawson.jpg` — `ff d8 ff e0`, 9,825 bytes
  - `2007-08-jeanne-johnson-sga.jpg` — `ff d8 ff e0`, 270,664 bytes
  - `2008-09-reagan-gilley.jpg` — `ff d8 ff e0`, 154,011 bytes

  All four are real JPEGs, not a saved bot-check page. No blocked-download failure here.
- **Priority 2** (every other president or student regent): zero `leaders` entries across all 61
  years without a photo.
- **Priority 4** (years with no photograph at all): zero years missing from `photos.json`'s
  `years` array.

`python3 scripts/portrait_gap.py`: 189 officer slots / 159 people / 157 with no portrait in any
year — unchanged from both earlier passes today.

## Network state, retested fresh this session

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: 403 with the full navigation-header set
  (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`).
  Closed for PDFs, same as every pass since 13 October.
- `do/search` on the same host: also 403, same as prior passes.
- `wkuherald.com`: open (200), with the same intermittent rate limit prior reports describe —
  one `wp-json` request came back 403, cleared on retry after a 20-second wait with no further
  backoff needed.

Nothing changed in the network picture. The pre-2011 route this archive needs for most of the
remaining gap is still closed.

## Priority 3: a method tried for the first time at scale, not a re-run of exhausted names

The previous pass (second scheduled, this morning) found one unattached portrait by accident,
while reading a wkuherald related-story card, and flagged that the same mechanism — a photograph
attached to a *known* SGA article, read through the WordPress `wp-json` media API rather than by
searching a person's name — had not been swept across this archive's other cited wkuherald
articles. This pass ran that sweep properly instead of re-running searches on names already
exhausted across 78 prior reports.

Pulled every `src.url` on a `wkuherald.com` article cited for an executive, senate officer, or
senate member in any year 2016-17 through 2026-27 (17 distinct articles). For each, fetched the
post via `/wp-json/wp/v2/posts/{id}` and its attached media via
`/wp-json/wp/v2/media?parent={id}`, and read every caption:

| article | people named in captions |
|---|---|
| 13485 (SGA votes on budget, 2020) | Garrett Edmonds |
| 16659 (SGA confirms 5 senators, 2020) | Kat Howard, Jamison Moorehead, Krystin Hardin |
| 74786 (León censure hearing) | Salvador León |
| 77380 (24th Senate opening meeting) | Jade Ismail |
| 81839 (DEI/constitution piece) | Morgan Gammons, Sam Kurtz |
| 92550 (second-to-last meeting, 2026) | Rush Robinson |
| 97612 (fourth meeting, fall 2026) | Caden Lucas |

Checked every name against `data/photos.json` before treating any of them as a lead. All nine
already carry a portrait entry — most of them individually captioned exactly as above, which is
presumably how they were identified and attached in the first place. The sweep closes clean: it
is a real method (it would have caught a captioned photo a name-search missed, since WordPress's
search endpoint does not index caption or alt text reliably), but this archive's cited wkuherald
articles have already been mined for it. No new file added under `data/photos/`, no new entry
added to `data/photos.json`.

Two articles (13430, 93405) returned HTTP 403 on the `wp-json/v2/posts/{id}` lookup even after
one retry with a 25-second backoff; both are already cited elsewhere and were not pursued further
rather than risk the rate limit for articles already represented by other citations in the sweep.

## Xavier Spiess, re-confirmed still blocked for the same structural reason

The second pass today reconfirmed Xavier Spiess's portrait (identified 15 October, a Judicial
Council candidate who lost the 2025-26 chief justice vote 3-1) has nowhere to attach: he holds no
entry in `organization.senate.officers` or `organization.senate.members` for 2025-26, and the
build's merge (`scripts/build.py`, around line 7885) only attaches a `photos.json` leader entry
to a name it finds in the year's top-level `leaders`, `organization.executive`,
`organization.senate.officers`, `organization.senate.members`, or a committee's `chair` field. A
`photos.json` entry for him would sit in the file unattached to any page. That is a `years.json`
structural edit, out of this agent's scope by CLAUDE.md's "it is the only file you edit" rule for
`data/years.json`. Left for whichever routine adds officer-roster entries.

## What is still open

The 189-slot gap did not move this pass, for the third time today. The blocker is unchanged:
`cgi/viewcontent.cgi` and `do/search` on digitalcommons.wku.edu are both closed, and that is the
only route into Talisman yearbook pages and pre-2011 Herald issue scans, which is where most of
the remaining 157 people-with-no-portrait-anywhere live. wkuherald.com's `wp-json` media route,
tried properly for the first time this pass, has now been swept across every cited article and
found nothing further to add.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph. No file in `data/photos/` or entry in
`data/photos.json` changed this pass. Merged `origin/main` into `research-photos` first
(fast-forward, no conflict).
