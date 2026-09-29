# Photograph run, 29 September (fourth pass): both archive routes reconfirmed closed; one new dead end ruled out

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and
6. `research-photos` was three commits behind `origin/main` (the day's senate-date corrections);
merged cleanly, real merge base, no conflicts. Reconfirmed the baseline directly against
`data/years.json` and `data/photos.json` rather than trust the last log: all 73 leader records,
including Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley, carry a portrait; all 61 years
carry at least one photograph except four — 1994-95, 1995-96, 2000-01, 2008-09 — which have a
leader portrait but no dedicated year-scene photograph, exactly as the third pass reported.
`data/photo-finds/_topscholar-wanted.json` still lists four genuinely open leads with no `note`
field marking them closed: `dlsc_ua_records/5160` (Mallory Treece), `6721` (article 7724, Jacob
Turner/Lisa M. Kappler — Turner already has a portrait from elsewhere, so this lead is open only
for Kappler), `6220` (Daniel Shaw/Mitchell Stevens), `8633` (Katherine Smith, unconfirmed identity),
plus two `talisman/` entries for the 2014-15 and 2015-20 spreads and the SGA-photographs finding
aid at `dlsc_ua_fin_aid/620`.

## Retested both blocked routes independently, not by reading the last log

- `digitalcommons.wku.edu/cgi/viewcontent.cgi?article=7724&context=dlsc_ua_records` (the Kappler
  lead): full navigation headers, HTTP 403, Cloudflare's "Just a moment..." interstitial — same
  as every pass this week.
- `web.archive.org`, three different request shapes: a plain page fetch, the
  `web/<timestamp>id_/<url>` replay bypass with a generic year, and the same bypass with the exact
  timestamp (`20240721095749`) that `archive.org/wayback/available` itself reports as the closest
  snapshot for article 7724. All three reset the connection (`curl: (35) Recv failure: Connection
  reset by peer`); the agent proxy's own log named the host directly each time
  (`ws_closed_mid_exchange`, `web.archive.org:443`). Plain `archive.org` (a different host) answered
  the `/wayback/available` JSON API cleanly in under a second and confirmed the snapshot exists —
  confirming again that this is specific to the `web.archive.org` hostname, not a general Internet
  Archive outage, and not something an exact timestamp gets around.

Both findings match the third pass exactly. Nothing has reopened since this morning.

## One new avenue tried and closed

The SGA-photographs finding aid (`dlsc_ua_fin_aid/620`) had not been checked for a route around
`viewcontent.cgi` before. Its landing page loads at 200 and embeds an image at
`/assets/md5images/52b6811bea543c1b783dd8dc627eaf16.jpg` — a real 3.3 MB JPEG (2670x3877, `%FF%D8`
confirmed), not a bot-check page, served without going through the blocked endpoint. Worth checking
because if TopSCHOLAR exposes full-resolution scans through this path generally, it would open every
item on the site, not only this one.

It does not. The image is a photograph embedded in the finding aid's own descriptive text — two
archives staff members going through a box of correspondence at a desk labelled "MRS. HARRISON" —
unrelated to student government and unidentifiable as any of the people this project is looking
for. Checked the same pattern against the Kappler item's own landing page (`dlsc_ua_records/6721/`):
its only `md5images` sources are the PDF-icon PNG and the download-arrow GIF that decorate every
item page on the site, not a scan of the article itself. The `md5images` path exposes whatever
images an individual page's description happens to embed, not the underlying PDF; it does not
generalize to the Herald issues this queue actually needs. No photograph was extracted from it, and
no name in the queue was confirmed or ruled out.

## Net for this run

No file added to or removed from `data/photos.json` or `data/photos/`. `python3 scripts/build.py`
and `python3 scripts/check_data.py` both run clean. Landed on `research-photos`.

## For the next run

The queue and its blockers are unchanged from the third pass: `viewcontent.cgi` is a genuine,
external Cloudflare challenge; `web.archive.org` resets before any exchange completes, on every
request shape tried across two passes today, while `archive.org` itself stays reachable — worth
checking the cloud environment's Network access setting (session title bar → Edit) against the
allowed-domains list, since that is the one variable neither pass could change from inside the
container. Until one of those two doors reopens, this queue has no further routes to try that
have not already been tried and logged: three mirror hosts (`core.ac.uk`, `base-search.net`,
`catalog.hathitrust.org`) are closed behind their own challenges, and the finding aid's embedded-
image path, tried for the first time this pass, does not generalize.
