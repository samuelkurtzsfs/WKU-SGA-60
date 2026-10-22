# Photograph run, 22 October (scheduled): a full systematic sweep of the officer gap against wkuherald.com's media-caption search, one near-miss correctly left unattached, no new portrait

## Priorities 1, 2 and 4, reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait in `data/photos.json`.
- **Priority 2**: zero presidents and zero student regents without a portrait, across all 61 years.
- **Priority 4**: every year carries at least one year-level photograph. Zero gaps.
- **Priority 3** (officer gap): 188 officer slots / 158 people with no portrait in any year, per
  `scripts/portrait_gap.py` — down one person from the 157 the 21 October fourth pass left, which
  checks out: David Bass landed that run.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare "Just a moment..." challenge,
  tested with the full browser-navigation header set (`Sec-Fetch-Dest: document`,
  `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`). Still closed. Retested a second time
  at the end of the run; unchanged.
- `web.archive.org` — connection reset mid-exchange (`curl: (35) Recv failure: Connection reset by
  peer`), both at the start and the end of the run. Still closed.
- `archive.org` (plain item/download host) — open.
- `wkuherald.com` WP-JSON API — open throughout.

Given both PDF routes were closed for the whole session, this run did not repeat the
already-exhausted archive.org Talisman sweep (1971-81/86/87, worked through name by name across
several prior runs) and instead pushed a route that had only ever been used post-hoc, one post at a
time, into a systematic sweep of the whole gap list.

## A full sweep: wkuherald.com's media caption search against all 158 gap names

`scripts/portrait_gap.py --list` gives 158 distinct people with no portrait in any year. Queried
`https://wkuherald.com/wp-json/wp/v2/media?search=<name>` for every one of them — not the per-post
`?parent=<id>` lookup this file's prior runs used on specific articles already in hand, but the
caption full-text search across the whole Herald photo library at once, which no prior run's notes
describe running exhaustively against the complete list. 158 requests, paced roughly a second
apart; all returned cleanly.

29 names returned at least one hit. Read every one. 27 are unambiguous false positives: the search
matches on first name, last name, or both separately, against unrelated subjects — sports players
(Cody Cox, Robert Bell, Ian Hamilton, Carter Smith's own name also false-positive-matched several
football articles about a different "Carter"), movie-review capsule text (Tim Howard, Lane, Steve
Wilson — all pulling in unrelated "Director:", "Howard", or "Wilson" text from a Herald film
listicle), a mayoral candidate (Pat Smith → Patti Minter), an attorney general (Amber Daniel →
Daniel Cameron), a different student entirely with the queried name (Amanda Cole → Amanda Collins,
Jessica Williams → a 2019 climate-strike organizer two years after the gap entry's term, David
Young → an elephant-orphanage photo caption and an unrelated faculty profile), and so on. None of
these name a WKU Student Government Association officer.

Two needed a closer look:

### Carter Smith (2025-26, Freshman Senator) — already on file, under a different year

Hit: media id 97546, "WKU Student Government Association Sophomore Senator Carter Smith gets sworn
in to be a sophomore senator during SGA's fourth meeting of the 2026 fall semester Tuesday, Sept.
22, 2026 in the SGA Chambers." A clean, single-subject, captioned SGA photograph. Checked
`data/photos.json` before doing anything else: this exact photograph, same file size (235,070
bytes), is already filed as `2026-27-carter-smith.jpg` against his **2026-27** Sophomore Senator
entry (`organization.senate.members`), landed by an earlier run. It does not close the 2025-26
Freshman Senator slot the gap list still shows, because the caption documents him sworn in to the
*sophomore* seat, a different office and a different academic year from the one the gap list
flags, and reusing it there would misstate what the photograph shows. The gap list's 2025-26 entry
is correct to stay open; this is not a new find, just confirmation the right photograph is already
attached to the right year.

### Mark Clark (2017-18, Chair of the Committee of Diversity and Inclusion) — left unattached

Hit: media id 24653, a 13 April 2018 Herald article on the Pride Center's move to Downing Student
Union, captioned "Junior Mark Clark and freshman Kat Tyler work in the new Pride Center relocated
in Downing Student Union room 2084. Clark has been a part of the center since it first began two
years ago." The year lines up (a junior in spring 2018 is the 2017-18 academic year) and the
subject matter is suggestive — Pride Center work alongside a diversity-and-inclusion committee
chairmanship — but the caption never mentions SGA, student government, or any committee, and a
follow-up search for "Mark Clark SGA" in the same WP-JSON index returns nothing that ties this
specific Clark to the Senate seat. Same name, same year, adjacent subject matter is exactly the
shape of case CLAUDE.md's rule exists for: the caption does not confirm the person. Left
unattached, flagged here for whoever next works this name rather than merged into
`data/photos.json`.

129 of the 158 names returned no hit at all from this search.

## Conclusion

No new portrait landed this pass. The systematic sweep closes off wkuherald.com's caption-search
index as a source for the current 158-name gap — not because any individual name was untried
before (most had been, across many prior runs, by other methods), but because this was the first
pass to query the full list against this specific endpoint in one sweep, and it surfaces nothing
the file didn't already have or couldn't confirm. The gap remains blocked on the two closed PDF
routes (`cgi/viewcontent.cgi`, `web.archive.org`) for the pre-2003 names, and on the Herald/Talisman
simply never having printed a usable photograph for most of the post-2003 names it covers.

`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean. Landed on
`research-photos`.
