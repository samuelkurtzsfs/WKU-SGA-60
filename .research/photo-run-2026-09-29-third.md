# Photograph run, 29 September (third pass): the web.archive.org block traced to this
container's own network policy, not the remote site

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and
6. `research-photos` was already even with `origin/main` (the second pass, commit `c5eeb8a4`, had
just landed). Reconfirmed the baseline independently rather than trust the note: all 73 `leaders`
records, including Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley, carry a portrait; all
61 years carry at least one photograph; four years (1994-95, 1995-96, 2000-01, 2008-09) have only a
leader portrait and no dedicated year-scene photograph; 176 executive/senate officer records still
lack one. `python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean before this
run touched anything.

## What is actually different this pass

Every report since mid-September has logged `web.archive.org` as "closed" and moved on, treating it
as the remote site being unreachable or rate-limiting this project the way `digitalcommons.wku.edu`
does. That was never checked against this container's own outbound network policy. This pass did:

- `curl -sS "$HTTPS_PROXY/__agentproxy/status"` — the agent egress proxy's own status endpoint,
  which every session in this environment has and which no earlier photo run appears to have called.
  Its `recentRelayFailures` carried exactly one entry, from minutes before this run started:
  `{"kind":"ws_closed_mid_exchange","detail":"tunnel closed (code 1006, Connection ended) after
  11s; 517 B sent, 39 B received, client reading, 0 B still queued in the relay","host":
  "web.archive.org:443"}`. The proxy's own README (`/root/.ccr/README.md`) describes this exact
  failure shape — a tunnel that opens and is then cut mid-exchange — as what a *policy-denied* host
  looks like from inside the container, distinct from a remote refusal (which the proxy would
  normally turn into a clean HTTP error, since it re-terminates TLS itself).
- Called this environment's own documentation tool for a blocked host
  (`read_documentation`, topic `environment.network`, situation `blocked`). Its answer: tell the
  person the environment's network policy denied the host, and that they can change it themselves
  in the cloud environment's settings (the environment menu in the session title bar → Edit →
  Network access), either broadening the access level or adding the specific host to the allowed
  domains list.
- Cross-checked with a second client to rule out a TLS-fingerprint block specific to `curl` (which
  `data/photo-finds/_topscholar-wanted.json`'s own notes flag as a real phenomenon on this project's
  other blocked route): `python3 urllib.request` against the same `web.archive.org` URL failed the
  same way, `Connection reset by peer`, immediately. Not a curl-specific issue.

**This does not prove the block is policy rather than a genuinely flaky remote** — `data/photo-finds/
_topscholar-wanted.json`'s own notes record `web.archive.org` working cleanly as recently as 25-28
September (several items fetched at 3-25 MB apiece via its `id_` bypass), which a static, unchanging
container-level policy denial would not be consistent with, unless the policy itself changed
sometime after the 28th. What it does establish, that no earlier report checked: the failure mode
matches a policy cutoff rather than a remote-side rate limit or challenge page, the proxy's own
status output names the host directly, and there is a one-click place — the environment's Network
access setting — worth a look regardless of which explanation is right, because it is either the
fix or it rules the theory out cleanly. Recording this rather than re-logging "closed" a further
time, since every report so far has treated this route the same way it treats the genuinely
external `digitalcommons.wku.edu/cgi/viewcontent.cgi` block, and the two are not the same kind of
problem.

## The other route, retested and confirmed genuinely external

`digitalcommons.wku.edu/cgi/viewcontent.cgi?article=7724&context=dlsc_ua_records` (the Turner/
Kappler lead) — tested with both `curl` and `python3 urllib.request`, full navigation headers on
both (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`, a full
browser UA). Both tools got an identical Cloudflare `Just a moment...` JS challenge page, HTTP 403,
same body. The landing page for the same item (`digitalcommons.wku.edu/dlsc_ua_records/6721/`)
loads cleanly at 200 for both tools and carries no cover-image or thumbnail URL in its markup (`og:
image`/`cover_page` meta tags checked directly) that would offer a way to a portrait without going
through the blocked endpoint. This is a genuine site-side bot challenge on that one path, unrelated
to the container's network policy, and not something this project can solve without executing
Cloudflare's JavaScript challenge, which CLAUDE.md's access rules do not permit chasing.

## Net for this run

No file added to or removed from `data/photos.json` or `data/photos/` — no route opened to fetch
anything new. `python3 scripts/build.py` and `python3 scripts/check_data.py` both still run clean.
Landed on `research-photos`.

## For the next run

- If `web.archive.org` is still closed, check the environment's Network access setting (cloud
  environment menu → Edit) before assuming it is a remote flake again — that is the one thing this
  pass could not itself change. If it is not in the allowed-domains list, or the access level is
  narrower than it was in late September, that is the fix.
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` is a separate, genuinely external block. It is not
  fixed by anything on the container side.
- The standing queue is unchanged: `dlsc_ua_records/5160` (Mallory Treece), `6721` (Jacob Turner /
  Lisa Kappler, article 7724), `6220` (Daniel Shaw / Mitchell Stevens), `8633` (Katherine Smith,
  unconfirmed identity), `6645` and `6644` (spring 2007 senate cohort — Brian Fisher, Drew Eclov,
  Emilee England, Jessica VanWinkle, Cacy A. Schooler, Jacob Miers), the 2014-15 and 2015-16-
  through-2019-20 Talisman spreads, and the SGA-photographs finding aid at `dlsc_ua_fin_aid/620`.
  Every name behind these has already been searched against every currently reachable source; there
  is no untried name, only a route to reopen.
