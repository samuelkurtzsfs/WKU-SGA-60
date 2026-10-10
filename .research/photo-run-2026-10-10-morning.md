# Photograph run, 10 October (morning) — every embedded photo caption on 186 SGA-related wkuherald.com articles checked against the full officer-gap list, nothing found

## Priorities 1, 2 and 4, reconfirmed before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Nothing to do.

**Priority 2** (any other president or student regent without a portrait): checked every
`leaders` record in `data/years.json` against `data/photos.json` by name, programmatically. Zero
missing.

**Priority 4** (years with no photograph at all): every one of the 61 years has at least one
photograph in `data/photos.json`. Zero missing. The two standing gaps, 1994-95 and 2000-01, are
unchanged — see gates, below.

So this pass's whole job was priority 3, same as every recent run: `scripts/portrait_gap.py`
reports 189 officer slots with no portrait, held by 159 distinct people, 157 of them with no
portrait anywhere in the file. Unchanged from 9-10 October.

## A genuinely new method, not another keyword search

Every name in the 159-person gap has already been searched once or more by surname/full-name
keyword against `wkuherald.com`'s `/wp-json/wp/v2/posts?search=` endpoint (documented across the
9-10 October notes) and, for the 2021-26 span, by scanning each hit's `_embed`-ded figure captions
(8 October evening). Both methods depend on the search API's keyword ranking surfacing the right
article in the first place, and both missed a second gallery format the site uses.

This run instead worked from the image side: built a list of 186 distinct SGA-related
`wkuherald.com` posts (dedup of eighteen search terms covering elections, judicial hearings,
censures, appointments, committee and cabinet business, swearings-in, and constitutional
business, run 2004-2026), fetched each post's actual HTML page (not the REST API, which does not
carry the gallery), and pulled every image reference out of it by two patterns:

- `data-photoids="..."` — the dedicated gallery shortcode (confirmed on article 65821, the
  2022 election-night gallery, in a prior run)
- `wp-image-(\d+)` — the class WordPress stamps on every ordinary inline attachment, which also
  appears on the newer "VISUALS" gallery format (confirmed this run on article 92840, the 2026
  election-night piece, which uses this format instead of `data-photoids` and so was invisible to
  anything only checking the shortcode)

Every image ID found this way (several thousand individual lookups across the 186 posts) was
resolved through `/wp-json/wp/v2/media/<id>` for its actual caption text — the same per-photo
caption that identifies individuals in a multi-person frame, as already used for the portraits on
file for Alexis Courtenay, Sam Kurtz, Garrison Reed and others from article 65821. Every caption
was checked against all 159 gap names by surname.

## Result: 21 surname matches, all of them a different person

- Article 65821 (2022 election-night gallery, already fully mined for the names it actually
  supports): recurring hits on "Cole" (Bornefeld, matching gap candidates Amanda Cole/Jason Cole)
  and "Reed" (Garrison Reed, matching gap candidate Amarah Reed). Both are the same people whose
  portraits are already on file from this exact gallery; no new information.
- Article 87022 (23 Sept 2025 guest-speaker meeting): "Simpson" is Associate Director of Career
  Development Wayne Simpson, not gap candidates Caroline Simpson / Lane (Caroline) Simpson.
- Article 88699 (SGA committee bill, 2025): "Smith" is senator Jackson Smith, not any of the four
  gap candidates named Smith (Brooke, David, Kelly S., Pat).
- Article 90099 (Feb 2026 SGA meeting): "Johnson" is De'Anasia Johnson of Black Women of Western,
  a guest, not gap candidate Matthew Johnson.
- Articles 86647 and 82327 (Sept 2025 and Feb 2025 guest-speaker meetings): "Stewart" is WKU
  Athletic Director Todd Stewart, not gap candidate Jackie Stewart.
- Article 90713/90387 (Feb 2026 meeting coverage): "Carter" is senator Eli Carter, not gap
  candidate Margaret Carter (1995-96); "Murphy" is Kelci Murphy of the WKU Restaurant Group, a
  guest, not gap candidate Larry Murphy (1998-99).
- Article 82565 (24 March 2025 meeting): "Bailey" is senator Cayden Bailey, not gap candidate
  Mitchell Bailey (1998-99).

Every hit checked and ruled out by reading the full caption, not just the surname match. None is
a new portrait.

## The two PDF gates, retested cold, both still shut

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare "Just a moment..."
  challenge page, with full navigation headers. Same as every pass since this gate closed.
- `web.archive.org` (`if_` bypass) — connection reset mid-exchange (`ws_closed_mid_exchange` at
  the agent proxy), on two separate attempts. Not open this session.
- `archive.org` (not `web.archive.org`) — the direct `_djvu.txt` download route works when
  followed through its redirect (`curl -L`; a bare request without `-L` returns the item's own
  302 to a CDN node, which untranslated looks like a dead end and was fetched incorrectly on a
  first attempt this run before being caught). Verified by reading `talisman1975west`'s cover
  story in full. The Talisman identifiers this catalogue holds are unchanged and well-documented
  elsewhere in this project's notes (1943, 1946-47, 1963-65, 1971-81, 1986-87 — a search of the
  full archive.org identifier catalogue this run confirms nothing from the 1980s-mid, 1990s, or
  2000s-2020s exists under this naming scheme), so this route adds nothing new for the
  1994-95/2000-01 year-photo gaps or the post-1987 officer gaps, which was already the standing
  finding.

Both of this run's new candidate-post sweeps logged in `/tmp` scratch files
(`sweep2.log`/`sweep3.log`, `sweep2_hits.json`/`sweep3_hits.json`) are not checked into the
repository — they are search scaffolding, not findings, consistent with how prior runs have
treated their own scratch batches.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed; `data/years.json` is untouched.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean against the
unchanged tree (61 years, 1,967 events, 60 presidents); the `site/` rebuild this produced was
discarded (`git checkout -- site/`) since nothing in `data/` changed and `site/` is never
committed from this routine. This run's only output is this note.

## For the next run

The full-gallery-caption method is now exhausted for the posts this run's eighteen search terms
could surface — 186 distinct articles, every embedded image's actual caption checked against all
159 gap names — and it found nothing the keyword-search method had not already ruled out by a
different path. This closes out the lead the 10 October scheduled run flagged ("the articles
carry photo galleries whose attachments each hold their own caption... reachable at
`wkuherald.com/wp-json/wp/v2/media/<id>`... and is the first thing the next run should try") as
tried and unproductive, not untried.

What is left, unchanged from recent notes:

- The `cgi/viewcontent.cgi` and `web.archive.org` gates are both still the blocker for the 2010s
  Talisman volumes (Justin McDole, Allie Payne), the 2008-09 Herald issues beyond what wkuherald's
  own archive carries (Vanessa Scott), and the three 1995-96 *Xposure* issues that could speak to
  Margaret Carter and Cindy Chiapetta. Retry cold at the top of the next run regardless of
  today's result, as always.
- A wider net of search terms on `wkuherald.com` could still turn up posts this run's eighteen
  terms missed, particularly for the pre-2015 span where the site's own archive is thinner and
  less consistently tagged. But the pattern across every method tried so far — keyword search,
  `_embed` figure captions, and now full gallery-caption cross-reference — is consistent: routine
  SGA meeting coverage photographs the room, the speaker, or whoever is quoted, not a committee
  chair or ordinary justice sitting in the gallery. The 157-people-with-no-portrait-anywhere
  figure should be read against that structural limit, not as a sign the search method is failing.
