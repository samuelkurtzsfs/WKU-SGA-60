# Photograph run, 21 October second scheduled pass: baseline reconfirmed, a genuinely new route tried and closed, both blocked routes retested fresh

## Priorities 1, 2 and 4, checked directly

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`.
- **Priority 2**: zero presidents and zero student regents without a portrait, 61 years, 60 people
  — confirmed against `data/years.json` directly, not assumed from a prior report.
- **Priority 4**: all 61 years carry at least one year-level photograph in `data/photos.json`
  (`photos.years`), in addition to leader portraits. This has moved since the 20 August count of
  49/61 recorded in `SGA-60-AGENT-INFO.md` §1 — that figure is stale and should be updated by
  whoever next touches that file.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: HTTP 403, same Cloudflare challenge every pass
  since mid-September has hit. Ordinary item/landing pages on the same host still answer 200.
- `web.archive.org`: connection reset by the egress proxy before the TLS exchange completes
  (`ws_closed_mid_exchange`, confirmed against the proxy's own status endpoint, not just a curl
  error). Still closed.
- `archive.org` (the plain item host): open, used below.
- `wkuherald.com` WP-JSON: open.

## A genuinely new route tried this pass: `wku.edu/sga`'s legislative pages

Two pages on the live SGA site had not been fetched by name before, found via a web search rather
than by guessing the URL: `wku.edu/sga/legislative/senate_committees.php` (current year) and
`wku.edu/sga/2018-2019-legislative/branch.php` (an archived year, which raised hope that other
academic years might have their own parallel page carrying headshots). Both are plain-text rosters
— the only image on either page is the site's own `mywku-logo.png` masthead. The current committees
page does list two gap names (Carter Smith, Tyreesha Morris) among its members, confirming they
hold the offices `data/years.json` already records, but with no photograph on the page there is
nothing to attach. This closes the lead: the legislative section of `wku.edu/sga` carries no
headshots for any year, current or archived, alongside the already-confirmed finding (2 October)
that the executive section's five current headshots are already on file.

Also checked, prompted by the same search: wkuherald.com's newest SGA story, "SGA kicks off 60th
year on campus, swears in new committee chairs" (article 96580, 26 August 2026). It names Tyreesha
Morris among nine new committee chairs sworn in that week, but carries exactly one photograph, and
its caption names only President Caden Lucas (already on file). Checked 96580's and 92808's full
media galleries directly via the WP-JSON `media?parent=` endpoint rather than trusting the post
body alone — 96580 attaches only the one image; 92808 (Lucas's own election story) attaches none
beyond its featured image. No new lead for Morris.

## Priority 3: the standing officer gap

Not re-searched by name this pass. The 7-13 October reports already worked through the 2003-2025
slice of the 159-person gap by name, several names 5-8 times over with `wkuherald.com`'s search and
its media-caption method; the 18-21 October reports did the same for the pre-1988 slice reachable
through `archive.org`'s Talisman holdings. Re-running an identical name-by-name sweep today without
either blocked route open or a new venue to try would not improve on that work, so this pass spent
its budget on the two routes above instead, both now closed off cleanly rather than left untested.

## What this run leaves unchanged

`data/photos.json` and `data/photos/` are unchanged from the last commit on this branch. 189
officer slots (159 people) remain without a portrait, per `scripts/portrait_gap.py` — unchanged.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61 years, 1964
events, 60 presidents, no missing leader portrait, no year without a photograph). Landed on
`research-photos`.

## A note for whoever next reviews this branch

`data/photos.json` has not gained an entry since the commit of 15 October. In the six calendar days
since, roughly thirty scheduled passes (the `.research/photo-run-*.md` count for that window) have
each independently reconfirmed the same two closed routes and worked through the same name list
without landing anything, this one included. That is not a sign any individual pass did its job
poorly — each has tried a genuinely different angle, and this one's two new leads (the `wku.edu/sga`
legislative pages, the 96580 article) are evidence of that, not padding. But the project's remaining
gap now rests almost entirely on `digitalcommons.wku.edu`'s PDF endpoint and `web.archive.org`
reopening, or on a source this file has not yet thought to try; neither can be produced by searching
harder inside the two already-open, already-exhausted venues. Worth deciding, outside an agent
session, whether this trigger's firing frequency should drop until one of the two blocked routes
shows signs of opening again.
