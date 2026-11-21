# Photograph run, 5 November fourth scheduled pass: all three standing blocks reconfirmed closed, one new route tried and closed, no new lead

## Priorities 1, 2 and 4, checked directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Unchanged since August.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — "61 years, 1964 events, 60 people
  have been president," no portrait-coverage complaint. Zero presidents or student regents
  without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as every pass today: 188 officer slots without a portrait for that person in that
  year, held by 158 people, 156 with no portrait anywhere in the file. Every one of the 158 names
  already has an individual check on record as of this morning's pass (ShyAnte'e Williams, the
  last untried name, was closed negative then). `research-photos` is still fully caught up with
  `origin/main` (merge-base equals main's tip, last moved 19 October), so no routine has added a
  new name to the gap list since.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (article 7642, the 2009-10 lead), full browser UA
  plus the navigation headers CLAUDE.md specifies: `HTTP 403`. Unchanged.
- `archive.org/advancedsearch.php`, both the narrow `identifier:talisman*west` query and a
  broader `title:(talisman) AND creator:(western kentucky)` query: still exactly the same 19
  volumes (1943, 1946-47, 1963-65, 1971-81, 1986-87). No new scan reaching the 1990s-2020s years
  where almost all of the remaining officer/Senate gap sits.
- `web.archive.org`: still closed. The proxy's own status endpoint now shows why in more detail
  than a bare curl exit code did on prior passes — `recentRelayFailures` logs
  `ws_closed_mid_exchange` on `web.archive.org:443`, the tunnel closing mid-handshake after the
  client had already sent its request. This is the Internet Archive's side refusing the
  connection, not a local DNS or proxy-allowlist problem; every other host tested in the same
  window (`archive.org`, `google.com`) worked cleanly through the same proxy.
- **New this pass**: tried `timetravel.mementoweb.org`, the Memento aggregator that proxies into
  several web archives (not just the Wayback Machine) and so looked like a possible way around
  `web.archive.org` being closed at the connection level. It does not work here either: the plain
  hostname fails DNS resolution over HTTP, and over HTTPS the proxy's own CONNECT tunnel fails
  with a `502` before any TLS handshake — the memento aggregator service itself appears to be
  unreachable or down, not blocked by this container's network policy specifically. Closed as a
  route; no further value in retrying it without evidence the service is back.

## This pass

With the 158-name officer/Senate gap list fully exhausted (confirmed again against the gap
script's own output, which matches this morning's figures exactly) and all three standing network
blocks unchanged on retest, this pass spent its effort on one genuinely new route
(`timetravel.mementoweb.org`) rather than re-running a name search already closed negative. That
route closed negative too. No name was re-searched that already had a recorded individual check.

## Conclusion

No new portrait landed. `data/photos.json` and `data/photos/` are unchanged from
`origin/research-photos`. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean; the only `site/` diff was the build-date line, reverted before committing. All three
standing blocks (digitalcommons PDF endpoint, archive.org's fixed 19-volume Talisman catalogue,
closed `web.archive.org`) are unchanged, and a fourth candidate route (the Memento aggregator)
is now also closed. Presidents and regents remain fully covered, every year has at least one
photograph, and the remaining 156-person no-portrait-anywhere gap stays blocked on the same three
routes, now with no untried name and no untried route on file. A future pass should keep
retesting those three blocks for a change in state rather than re-searching this list, unless a
block lifts, a new route surfaces, or another routine adds a name to the gap.
