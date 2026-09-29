# Photograph run, 29 September (second pass): two new mirror hosts tried and closed, standing routes unchanged

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and
6. `research-photos` was already current with `origin/main` (this morning's first pass, commit
`429b1753`, had just merged and reconfirmed the baseline a few hours earlier). Re-read that pass's
report (`.research/photo-run-2026-09-29.md`) before doing anything, rather than repeat it.

Reconfirmed independently, not trusted from the note: all 73 `leaders` records (including Nick
Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley) carry a portrait; all 61 years carry a
photograph of some kind, four (1994-95, 1995-96, 2000-01, 2008-09) with only a leader portrait and
no dedicated year-scene photograph. `python3 scripts/build.py` and `python3 scripts/check_data.py`
both ran clean before this run touched anything.

## Standing routes, retested fresh rather than assumed

- `web.archive.org` — closed. Three `curl` attempts, spaced, all `Recv failure: Connection reset by
  peer` before the exchange completed. Same failure mode this file has logged since mid-September.
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — closed. `403` behind the Cloudflare challenge on a
  plain GET with full navigation headers (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`,
  `Upgrade-Insecure-Requests: 1`, a full browser UA), tested against article 7724 (the
  Turner/Kappler lead).
- `archive.org`'s own item store — open (`200` on its advanced-search API). No new
  `talisman*west` identifiers beyond the 19 this file already lists.
- `wkuherald.com` — open (`200` on the WP-JSON search endpoint).

This morning's pass already established that every one of the 176 executive/senate officer records
still lacking a portrait has been searched at least once against every reachable source, so this
pass did not repeat a name-by-name `wkuherald.com` sweep. Instead it spent the open window looking
for a way around the two closed routes.

## Two mirror hosts tried for the first time, both closed

The standing queue in `data/photo-finds/_topscholar-wanted.json` is blocked entirely on getting a
PDF off `digitalcommons.wku.edu`, one way or another. This project has tried the direct route and
the `web.archive.org` bypass repeatedly; it had not yet tried a third-party mirror that might have
crawled and cached the same open-access repository independently.

- **`core.ac.uk`**, an open-access aggregator that harvests institutional repositories by OAI-PMH
  (the same protocol `harvest_herald_index.py` already uses against `digitalcommons.wku.edu`
  itself) — a plausible independent copy of the same PDFs. `core.ac.uk/search?q=...` answered
  `308`, and following the redirect to the results page returned `403`. Not usable.
- **`base-search.net`** (Bielefeld Academic Search Engine), another OAI-PMH aggregator — answered
  `200`, but the body is a proof-of-work bot challenge page ("Making sure you're not a bot!",
  an Anubis challenge with a JavaScript difficulty puzzle), not a results page. Not usable without
  solving a bot challenge, which this project does not do.
- **`catalog.hathitrust.org`** — re-tested rather than trusted from the 12-13 September entries
  that first logged it: still `403` behind the same Cloudflare "Just a moment..." challenge.
  Unchanged.

None of these three produced a usable page. Recording them so a future run does not spend a window
rediscovering the same three dead ends.

## Net for this run

No file added to or removed from `data/photos.json` or `data/photos/`. No new candidate identified
— this morning's pass already established there is no untried name behind the closed routes, only
a blocked route in front of a fully-searched queue. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both still run clean. Landed on `research-photos`.

## For the next run

Same standing queue as this morning: the `_topscholar-wanted.json` items (Turner/Kappler at
article 7724, Shaw/Stevens at `dlsc_ua_records/6220`, Katherine Smith at `dlsc_ua_records/8633`,
the SGA-photographs finding aid at `dlsc_ua_fin_aid/620`, Mallory Treece at `dlsc_ua_records/5160`)
and the two Talisman spreads (2014-15, 2015-16 through 2019-20) are the entire remaining queue.
Closing any of them needs `viewcontent.cgi` or `web.archive.org` to reopen, or a fourth mirror host
this run did not find. Test connectivity fresh before assuming either way; it has flipped
repeatedly all month.
