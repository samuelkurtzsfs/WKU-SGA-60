# Photograph run, 18 October (second scheduled pass): a live `wku.edu/sga` headshot directory found and checked out, closing a lead rather than opening one

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against the current `data/years.json` and `data/photos.json` before touching anything,
after merging `origin/main` into `research-photos` (clean merge, carried forward commit #821, the
student escort service entry, and #820/#819, the night report and the earlier photograph pass from
today — no conflicts):

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait.
- **Priority 2** (every other student body president or student regent, including the sitting
  2026-27 president, Caden Lucas, who doubles as student regent): zero gaps. All 73 `leaders`
  records across 61 years carry a portrait.
- **Priority 4** (years with no photograph at all): zero.

`python3 scripts/portrait_gap.py --list` still reports 189 officer slots with no portrait, held by
159 distinct people, 157 with no portrait anywhere in the file. Numerically unchanged from this
morning's pass and every pass this week.

## Network state, retested fresh

- `cgi/viewcontent.cgi`: HTTP 403, Cloudflare's "Just a moment..." challenge. Still closed.
- `web.archive.org`: every request failed at the proxy layer (`ws_closed_mid_exchange`, tunnel
  closed after 8-11s, confirmed against the proxy's own status endpoint, which logs the same four
  failures against `web.archive.org:443` this session). A plain `http://` request to the CDX API
  was refused separately by egress policy (http, not https, is blocked outright — a different,
  unrelated restriction). Still closed.
- `archive.org` (the item/download host): open, confirmed again with a direct page-image pull.
- `wkuherald.com` and `www.wku.edu`: both open.

## A new live route found, chased down, and closed: `wku.edu/sga`'s own current-year headshot folder

The current `wku.edu/sga/executive/index.php` page (the live 2026-27 cabinet page, not an archived
one) links five headshot images directly: `/sga/2025_2026_executive/headshots_website/caden.jpg`
(Caden Lucas, "Student Body President, Student Regent"), `jakobbarker.jpg` (Jakob Barker, "Student
Body Vice President"), `will.jpg` (Will Derryberry, "Chief Financial Officer"), `gabipace2.jpg`
(Gabi Pace, "Chief of Staff") and `caydenbayley.jpg` (Cayden Bailey, "Chief Communications
Officer") — each name printed directly beside its own image in the page's own markup, a
caption-grade identification by CLAUDE.md's rule. (The folder is named for the prior academic year
even though the page content is this year's; WKU's site evidently reuses the directory name across
an officer rotation rather than renaming it.)

This looked new — it is a live route, not a Wayback capture, and `SGA-60-AGENT-INFO.md` §8's
record of this exact lead (16 September) was built entirely from `web.archive.org` CDX captures of
`wku.edu/sga/*/headshots/` and `*_headshots/` paths, never from the live current-year page directly.
Checked all five names against `data/photos.json` before concluding anything: **all five already
carry a portrait** — `2026-27-caden-lucas-solo.jpg`, `2026-27-jakob-barker-portrait.jpg`,
`2026-27-will-derryberry-portrait.jpg`, `2026-27-gabi-pace.jpg`, `2026-27-cayden-bailey.jpg` — so a
prior run had already taken this exact live page, by this or a different route, and the lead is
spent rather than open. Also checked the Senate speaker named in the same session's minutes
(Veronica Butler) and the defeated opponent folded into the Senate (Jaden Marshall, Amelia Tucker):
all three already carry portraits too.

Tried the equivalent live folder for every other gap year still open to confirm the directory isn't
more broadly reachable than one year: `2024-2025-executive`, `2022-2023-executive`,
`2021-2022-executive` and their underscore equivalents all 404 on `/headshots/`, and WKU's site
disables directory listing (plain `403` on the bare folder), so there is no way to enumerate a past
year's actual filenames from the live site without already knowing them — which is exactly why the
16 September run had to use Wayback's CDX index instead, and exactly why that route is closed again
this session. **This is not a new usable source; it is the same source as 16 September, reachable
today through its current front door instead of an archived one, and already exhausted.**

Also checked the pages for the roles that actually make up the open gap — Judicial Council and
individual Senate seats, which the exec headshot page has never pictured in either its archived or
live form. The live judicial-council page 404s outright on the current site, and the senate
committee and legislative-archive pages carry no images of any kind. The gap is concentrated in
offices the university's own site has never photographed.

## No portrait found or added this run

No file in `data/photos.json` or `data/photos/` changed. The 189-slot gap is numerically unchanged.
This run's contribution is tracing a route that looked new back to a source already fully mined,
and confirming (rather than guessing) that the live site offers no way around the two blocked
routes for any of the still-open names.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: clean. 61 years, 60 presidents, no
missing leader portrait, no year without a photograph.
