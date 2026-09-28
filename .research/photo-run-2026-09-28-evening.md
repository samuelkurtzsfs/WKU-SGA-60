# Photograph run, 28 September (evening): baseline reconfirmed, web.archive.org closed to this
container, five wkuherald.com and five wku.edu/sga live-page checks all close negative

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and
6. Checked out `research-photos` and merged `origin/main` forward. One conflict, in this branch's
own `photo-run-2026-09-28-afternoon.md` from earlier today (both sides had independently added the
same report under the same filename); resolved by keeping `origin/main`'s corrected text, which
fixes a transposed issue-date pair in that report's own account of articles 9223/9224.

Independently reconfirmed the baseline before searching for anything new: all 73 `leaders` records
carry a portrait, all four named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan
Gilley) among them; every president and student regent in `data/years.json` resolves to a
`photos.json` entry; all 61 years carry at least one photograph, whether a leader portrait or a
year scene (four years - 1994-95, 1995-96, 2000-01, 2008-09 - still lack a dedicated year-scene
photograph but are covered by a leader portrait). `python3 scripts/merge_photo_finds.py` agrees: 0
to add, 0 to replace, the same 18 standing refusals it has reported since the queue was last
exhausted. Priorities 1 and 2 remain fully done.

## web.archive.org is closed to this container tonight

Every route this project has used to pull a `digitalcommons.wku.edu` PDF - the actual images, not
just landing pages - depends on `web.archive.org`. Tonight it returns a flat `Blocked by egress
policy` on the very first byte, not Cloudflare's interactive challenge and not the Internet
Archive's own intermittent instability the last two runs logged. That is a different failure mode
from anything recorded earlier this week, though `SGA-60-AGENT-INFO.md` already warns reachability
"may vary by container." Direct requests to `digitalcommons.wku.edu/cgi/viewcontent.cgi` still hit
Cloudflare's 403 as always, full browser headers included (confirmed again on
`dlsc_ua_records/6721`, article 7724). With both closed, no Herald or Talisman PDF could be fetched
this run, and none of the open `_topscholar-wanted.json` entries (6721, 6220, 3684, 6645, 8633, the
two Talisman spreads for 2014-15 and 2015-16 through 2019-20, and `dlsc_ua_fin_aid/620`) could be
advanced. Landing pages on `digitalcommons.wku.edu` itself stay reachable over plain HTTPS, so
6721's real `viewcontent.cgi` article id (7724) was resolved and left on record for whenever the
bypass reopens.

`archive.org`'s own item store (not the Wayback host) is unaffected. Used its
`advancedsearch.php` to reconfirm the Talisman collection there is still exactly the nineteen
identifiers `CLAUDE.md` already lists (1943, 1946, 1947, 1963-65, 1971-81, 1986-87). No 2010s
volume exists under this identifier scheme on `archive.org`, so the two open Talisman leads for
2014-15 and 2015-16 through 2019-20 have no `archive.org` route at all, bypass or not - they need
`digitalcommons.wku.edu` specifically, which is closed both ways tonight.

## Five wkuherald.com searches, all negative

Searched the WP-JSON API (`?search=<name>`, no rate limit) for five names drawn from the current
executive/senate officer gap list who recur across multiple years: Justin Goins, Caleb Collins,
Cassidy Townsend, Turner Reynolds, Maiah Cisco. Read the full HTML of every SGA-related hit,
including the one photo gallery among them: "SGA election results announced, Cole Bornefeld wins
presidency" (20 April 2022, wkuherald.com/65821). That gallery captions only Sam Kurtz and Cole
Bornefeld - both already on file - and lists the rest of the 2022-23 senate cohort, Caleb Collins
included, as plain running text with no accompanying photograph. None of the five names turned up
a single-subject captioned photograph in any wkuherald.com SGA article.

## Five wku.edu/sga live-page checks, also negative, plus one dead end confirmed for the future

Checked wku.edu/sga's live pages for the five current-year (2025-26) senate names still missing a
portrait: Tyreesha Morris, Carter Smith, Miles Harvey, Nolan Rongey, Zoe Martin. The live
`legislative/senate_committees.php` page names three of them - Morris as a committee chair, Smith
and Harvey as vice chairs - and carries no images anywhere on the page; Rongey and Martin are not
named on it at all. Unlike the Executive Cabinet's own template,
which does serve current headshots at a predictable path,
`/sga/<year>_executive/headshots_website/<firstlast>.jpg` (this is how Hannah Hash and Sophie
Stirling, both already in `photos.json` for 2025-26, are sourced). That headshot path does not
exist for the Senate at all.

Worth recording for a future run: tried the equivalent Executive Cabinet page for every year before
2025-26 (`2019_2020_executive` through `2024_2025_executive`); none serves a headshot, answering 404 or 403. `wku.edu`
overwrites the SGA site's content each year rather than archiving it, which is exactly why this
project has depended on Wayback copies for historical officer pages - and exactly why tonight's
`web.archive.org` block matters more than a single run's bad luck.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean (61 years, 60
presidents, all portrayed; 1,968 events; the archive checks out against its own rules).
`data/photos.json` and `data/photos/` are unchanged this run. Only `data/photo-finds/_archive-gaps.json`
(one new entry, at the end) and this file changed.

## For the next run

- Priorities 1 and 2 remain fully done.
- Test `web.archive.org` reachability again before assuming either way - it has flipped between
  reachable and blocked more than once this month and appears to depend on the container, not on
  anything this project controls.
- If the bypass reopens, `dlsc_ua_records/6721` is already resolved to `viewcontent.cgi?article=7724`
  and ready to fetch (wanted for Lisa Kappler and Jacob Turner).
- Justin Goins, Caleb Collins, Cassidy Townsend, Turner Reynolds and Maiah Cisco have no
  single-subject photograph anywhere on wkuherald.com's SGA coverage; any face for them would have
  to come from a digitalcommons Herald PDF or a Talisman, both currently unreachable.
- Tyreesha Morris, Carter Smith, Miles Harvey, Nolan Rongey and Zoe Martin (2025-26 senate) are not
  on any live wku.edu/sga page with a photograph; the current-year executive headshot path does not
  extend to Senate committee officers.
