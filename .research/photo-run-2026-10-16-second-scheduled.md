# Photograph run, 16 October (second scheduled pass): no new portrait; gap confirmed fully mined

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked `data/photos.json` against `data/years.json` directly before anything else, per
CLAUDE.md's "check whether an earlier run already got them" and the standing instruction to
re-verify rather than trust a prior report's word for it.

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait.
- **Priority 2** (every other president or student regent): zero `leaders` entries across all 61
  years without a photo.
- **Priority 4** (years with no photograph at all): zero years missing from `photos.json`'s
  `years` array.

`python3 scripts/portrait_gap.py`: 189 officer slots / 159 people / 157 with no portrait in any
year — unchanged.

## Network state, retested fresh this session

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: 403 with the full navigation-header set. Closed
  for PDFs, same as every pass since 13 October.
- A plain `do/search` query on the same host: also 403. The block covers more than the PDF route.
- Item landing pages on the same host (not `viewcontent.cgi`, not `do/search`): 200, confirming
  the block is specific to those two paths rather than the whole host. Checked a landing page
  that carries no image reference of any kind (`og:image`, thumbnail, or inline `<img>`) to rule
  out a non-`viewcontent.cgi` route to a usable picture on this template; none exists on a Herald
  issue index page. (Herald issues are the one Talisman/UA1C landing-page type this archive has
  tested so far; a yearbook item's own landing page was not reached this pass, since the search
  path that would locate one is itself 403'd.)
- `web.archive.org`: 302, resolves normally. Open, consistent with yesterday's corrected finding.
  Not used this pass beyond the network check — the two captures already read (12 Jan 2011 and
  21 Oct 2012) carry no officer photographs, only the university logo, and no new capture was
  identified that would.
- `wkuherald.com`: open, with the same intermittent rate-limit the last several reports describe
  (one 403 on a gallery page, cleared after a 20-second wait with no retry needed beyond that).
- `archive.org` metadata API: open.

## Priority 3 (officer portraits): a fresh-leads check, not a re-run of exhausted names

Before searching anyone, cross-checked candidate names from the open 189-slot gap against all
prior `.research/photo-run-*.md` files (now 77 of them) rather than pick names at random. Every
name in the gap has been searched at least once; the great majority have been searched several
times across different routes. Picked the handful with the thinnest search history — Luke
Edmunds, Chase Coffey, Helen Vickrey, Amarah Reed, Hayden Skinner-Fine — and re-read what those
single prior passes actually found, rather than add a sixth identical attempt:

- **Luke Edmunds** (2016-17) — the one hit that is genuinely about SGA (Herald, "Next student
  body president elected to office," 19 Apr 2017) carries a captioned photo naming four other
  people by a stated left-to-right order; Edmunds is not one of them. Checked and ruled out, not
  reopened.
- **Chase Coffey** (2016-17) — searched and recorded with no individually captioned photograph
  found.
- **Helen Vickrey** (2016-17) — searched in a 30-name batch; zero of that batch produced an
  individually captioned photograph.
- **Amarah Reed** (2016-17) — the only hits found are for other people who share part of her
  name (Garrison Reed, a different "Reed"); no portrait of her specifically.
- **Hayden Skinner-Fine** (2016-17) — a general web search turns up a current staff-directory
  headshot at her present employer, outside this project's university-archive/news sourcing rule
  and outside its privacy rule; correctly not used.

Tried one new angle rather than re-running old searches: checked wkuherald.com's most recent SGA
coverage (the fifteen latest posts tagged SGA, back to 7 July 2026) for anything that might
caption a current officer still in the gap — Tyreesha Morris or Carter Smith, both 2025-26
senators with no portrait on file. "SGA senate complete following fall election" (29 Sept 2026)
names Carter Smith in its text but carries only one photograph, of a guest dean addressing the
Senate, with no senator pictured. Nothing else in the batch mentions either name. No usable
image.

Also opened the one wkuherald gallery already on file for this project's other open names
(article 65821, the 2022 election-night gallery) to check how its captions are actually
delivered, since an earlier report (15 October) described the mechanism as unreadable without a
script-rendering tool it did not have. The first of the gallery's eight photos carries its
caption directly in the static page HTML (`sam Kurtz (left) and Cole Bornefeld call their moms...
in WKU's Student Government Association's chamber`); the remaining seven are referenced only by
numeric ID (`data-photo-ids`) with no caption text anywhere in the static page, consistent with
captions for photos 2-8 being fetched by script on demand. This confirms, rather than overturns,
what prior reports already worked out by a different method (the `wp-json/wp/v2/media/{id}`
lookup): the gallery's full caption set is reachable, and it has already been read photo-by-photo
for this archive's open names, with no match. No new ground opened here.

## What is still open

The 189-slot gap did not move this pass. Nothing was added to `data/photos.json` and no file was
added under `data/photos/`. The three things blocking further progress are unchanged from
yesterday's report:

- `cgi/viewcontent.cgi` and `do/search` on digitalcommons.wku.edu are both closed, which is the
  only route into Talisman yearbook pages and pre-2011 Herald issue scans for the pre-2011 names
  that make up most of the remaining gap.
- `web.archive.org`'s captures of the old SGA website confirm officer names and offices but carry
  no photographs at all (only the university logo), so an open Wayback route does not by itself
  close any part of this gap.
- Xavier Spiess's identified portrait (found 15 October) is still waiting on an
  `organization.senate.officers` entry for 2025-26 that this agent's rules do not let it add
  itself, since all photo metadata is confined to `data/photos.json`.

Everyone checked this pass stays open for lack of an individually captioned photograph or a
usable route to one, not for lack of searching. Given how thoroughly the current 189-slot list has
been worked across more than a week of passes with every open route, whoever next picks this up
should prioritize checking whether `cgi/viewcontent.cgi` has reopened over searching further names
on wkuherald.com — the remaining gap is concentrated in decades that route alone can reach.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph. No file in `data/photos/` or entry in
`data/photos.json` changed this pass. Merged `origin/main` into `research-photos` first (one
conflict, in the prior report file this pass follows on from — both branches had independently
added the same filename; kept `origin/main`'s version, which carries two later corrections the
`research-photos` copy was missing) and the merge carried no other substantive change.
