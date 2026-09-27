# Photograph run, 27 September (afternoon, scheduled): both walls retested from a second, independent
network path, and the wall is confirmed not to be this container's alone

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and
6. `research-photos` (last touched by this morning's run, PR #622) was already merged into
`origin/main`; checked it out fresh from `origin/main` rather than build on the merged branch,
since the old PR is closed and a new one is needed for any further work.

Re-verified the baseline directly against the files, not against this morning's note: all 73
`leaders` records in `data/photos.json`, including Nick Todd, Katie Dawson, Jeanne Johnson and
Reagan Gilley, carry a portrait. `python3 scripts/merge_photo_finds.py` (no `--write`) proposes
0 to add, 0 to replace, the same 18 standing refusals. Priorities 1 and 2 are unchanged and fully
done.

Rebuilt the officer/senate-officer portrait gap directly from `data/years.json` against
`data/photos.json`: 217 records lack a portrait, of which exactly 8 fall inside `archive.org`'s
Talisman coverage (1971-72 through 1981-82, 1986-87, 1987-88) — Vern Pulman, David Bass, David
Young, Alice Wicks, Steve Wilson, Mark Chesnut, Chris Millay, Dwight Austin. These are precisely
the eight this morning's run re-checked page by page and closed as dead ends against the volumes
themselves (no photograph, or a caption too weak to identify a face). Nothing new to attempt there
without a source outside `archive.org` and `digitalcommons.wku.edu`.

## Both blocked routes retested, and a second independent path tried against them for the first
time

`digitalcommons.wku.edu/cgi/viewcontent.cgi` — tested with full browser navigation headers
(`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`), a warmed
referer from the item's own landing page, against both a Talisman volume (`article=5695`) and a
Herald issue (`article=1465`, already cited elsewhere in this archive): Cloudflare's interactive
`Just a moment...` challenge, HTTP 403, on every attempt. Confirmed again that the item **landing
pages** are not behind the same wall — `dlsc_ua_records/2464/` returned a normal HTTP 200 with the
full item page and index lines, from the same container in the same minute as the 403 on its own
`viewcontent.cgi` link. Scanned that landing page's HTML for any second image URL (a thumbnail, a
preview, an `og:image`) that might carry the scanned page without going through `viewcontent.cgi`:
none exists. The only `href` on the page pointing at content is the `viewcontent.cgi` link itself.

`web.archive.org` — reset the TLS handshake on a direct `curl` attempt (`ws_closed_mid_exchange` at
the proxy, matching every prior entry in this section for two weeks running).

**New this run: the WebFetch tool, which runs through Anthropic's own fetch infrastructure rather
than this container's egress proxy, was pointed at the same two `digitalcommons.wku.edu`
`viewcontent.cgi` URLs (the WKU Archives SGA-photos finding aid, `article=1619&context=
dlsc_ua_fin_aid`, still never successfully opened by any route; and the Talisman `article=5695`
lead).** Both came back the identical `HTTP 403 Forbidden`, with no response body retrieved.
That is a materially different fact than anything logged before it: every earlier attempt in this
file's `viewcontent.cgi` history reasoned about *this container's* network path (curl through the
agent proxy, or a local Chromium whose own TLS trust store was the point of failure). A completely
different requesting path — a different IP range, a different client, no relationship to this
container's proxy at all — hits the same wall. That rules out "it's something about this
container's egress" as the explanation for the `viewcontent.cgi` block, and points instead at
Cloudflare filtering on the request itself (client/TLS fingerprint, or blanket bot rules on that
one script) rather than on where the request comes from. It does not open the route; it narrows
what a future run should try next, away from anything that changes only the network path and
toward something that changes what the request looks like (which no automated tool in this
container can do, per the CA-trust dead end this morning's run already logged for the browser
route).

**Also new: `web.archive.org` via WebFetch returned a hard tool-level refusal
("Claude Code is unable to fetch from web.archive.org") rather than a network error, and
`archive.ph` (archive.today), a mirror host never tried anywhere in this file before, reset the
TLS handshake at the proxy exactly like `web.archive.org` does (`ws_closed_mid_exchange`, two
attempts).** Neither is a new route in; both are recorded so a future run does not spend a cycle
rediscovering them.

## Officer names: no new candidate found

Cross-checked the 8-name Talisman-coverage gap above programmatically against `data/photos.json`
rather than by re-reading last run's list, confirming the set is unchanged and all eight are
already-closed dead ends. Did not re-open any of the eight Talisman pages again this run — this
morning's pass already read each one against the page image and the text layer; re-reading them a
second time in the same day would not change what the page says.

Ran two open-web searches for genuinely new hosts for the four year-photo gap years (1994-95,
1995-96, 2000-01, 2008-09): a WNKY-TV "Throwback Thursday" retrospective on WKU SGA's 60-year
history (no photographs at all in the piece; the only name given is Jim Haynes, 1966, already
portrayed) and a search crossing bgdailynews.com against 2005-06/2008-09, which returned nothing
usable. `wku.edu/news` articles "Robinson elected as SGA president" and "Lucas elected as SGA
president" were checked against `data/photos.json` and are already the cited source for the Rush
Robinson and Caden Lucas portraits on file — not a new lead.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean (61 years, 60
presidents, all portrayed). No file in `data/` changed this run.

## For the next run

- Priorities 1 and 2 remain fully done; do not re-verify them a third time in one day — the count
  above already confirms it programmatically.
- `viewcontent.cgi` is now confirmed blocked from two independent network paths (this container's
  proxy and Anthropic's separate fetch infrastructure). Retrying it with a different curl header
  set or a different container is very unlikely to succeed; the block is on the request's
  signature, not the sender's address. `archive.ph` is now a closed dead end too, at the proxy
  level, same as `web.archive.org`.
- The 8-name officer gap inside `archive.org`'s Talisman coverage is fully exhausted for today. The
  ~180 remaining senate-member (not officer) portraits and the four year-photo gaps are untouched.
