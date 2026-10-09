# 9 October 2026 (photograph agent, scheduled) — priorities 1–2 reconfirmed, gates still closed, twelve more names checked and cleared

## Priorities 1–2, checked first as instructed

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Settled since August; nothing to do.

**Priority 2** (any other president or student regent without a portrait): every `leaders`
record in every year still has a matching `photos.json` entry. Zero missing.

The real gap remains entirely in priority 3 (officer portraits): 217 cabinet/Senate officer
slots short a face, across 176 distinct names, of which 27 carry a bar in
`data/photo-finds/_do-not-use.json` with a documented reason. (Editor's correction, 9 October:
this paragraph first read 215 slots across 174 names "101 of them already barred". The 101 is
the number of distinct names in `_do-not-use.json` altogether, not the overlap with the
faceless set: 74 of those barred names hold a portrait from another source or sit in no counted
officer slot, so only 27 of the 176 are barred. The next run should treat 149, not 73, as the
names a bar does not already close off.) Priority 4 is still just 1994-95 and 2000-01 — the two
years with no entry in `photos.json`'s `years` list, though both do carry leader portraits —
both outside the archive.org Talisman holdings (1971-1981, 1986, 1987 only) and both needing a
TopSCHOLAR PDF to close.

## The three blocked gates, retested cold rather than assumed

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403 on a plain GET with full navigation
  headers (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`).
  Same Cloudflare challenge every prior run has logged since September.
- `web.archive.org` — connection reset mid-handshake at the proxy (`ws_closed_mid_exchange`).
- `archive.ph` — same, connection reset mid-handshake.

None have reopened. `wkuherald.com`'s WP-JSON API and plain `archive.org` downloads were not
retested for access (both have been reliable all along) but were used below and worked cleanly.

## Twelve more names run through the wkuherald caption sweep

Continuing the method the 8 October evening run started and left unfinished (query
`wp-json/wp/v2/posts?search=<name>&_embed=1`, scan each hit's featured-media caption and any
`<figure>` block in the body for the candidate's name) — before picking new names, checked the
8 October evening and morning reports for who had already been tried, to avoid repeating the
same 38 names. Picked twelve untried names from the 2007-2015 window, all holding titles the
Herald is more likely to photograph individually (Chief Justice, Secretary of the Senate,
Director roles) rather than rank-and-file senators:

Jeremy Glass, Samantha Hughey, Cacy Schooler, Jacob Miers, Corey Bewley, Monique Gooch,
Aaron Pawley, Sarah Howell, Dajana Crockett, Jessi Wurth, Brittany Crowley, Cole McDowell.

**Zero produced an individually-captioned photograph.** Post counts ranged from 0 (Samantha
Hughey, Jacob Miers, Corey Bewley, Monique Gooch — no matching posts at all) to 10 (Brittany
Crowley, Cole McDowell), but no featured-media caption or in-body figure caption named any of
the twelve. The method itself was sanity-checked against a name already known to produce a hit
(Julie Mishchuk, who has a portrait already in `data/photos.json` from exactly this kind of
caption) before trusting the empty results — it still returns her flag-photo caption correctly,
so the twelve empty results are the sweep working, not a broken query. Nothing was added to
`_do-not-use.json`: a bare absence of posts or captions is not a finding, per the existing rule
in this file.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed. `data/years.json` is untouched, as
always. `build.py` and `check_data.py` both exit clean. This run's only change is this note.

## For the next run

- 135 of the 176 missing officer names are still genuinely untried by any method (the local
  Herald photo-cache sweep from 8 October covered all 176 at once and found nothing new beyond
  two names since barred; the live wkuherald caption sweep has now covered roughly 50 of them,
  this session's twelve included, all empty). The untried majority skews toward the 1990s and
  early 2000s, before wkuherald.com's full text coverage and before the 2010-2026 photo cache —
  those years have no local avenue at all until TopSCHOLAR or Wayback reopens.
- Retry `viewcontent.cgi`, `web.archive.org` and `archive.ph` cold at the top of the next run
  regardless of today's result, as every recent report has said — the intermittency is real but
  unpredictable.
