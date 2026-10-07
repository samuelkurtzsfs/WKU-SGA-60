# 7 October 2026, fourth run (photograph routine, scheduled)

## Baseline, reconfirmed against the current file rather than trusted from the last note

Merged `origin/main` into `research-photos` (already fast-forward; no new commits on `main` since
the third run today). `build.py` and `check_data.py` both run clean: 61 years, 1,967 events, 60
presidents. All 73 `leaders` records (every president, every student regent) carry a matching
`data/photos.json` entry — Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley included.
The officer-portrait gap is unchanged, on both of the bases the counting rule asks for: **217
slots**, counted per person per year, and **174 people**, counted across all years, over 42 years
of the file. (Editor's correction, 7 October: the figures filed with this run read 215 slots / 174
distinct names / 41 years. Recomputing cabinet and Senate leadership in `data/years.json` against
`data/photos.json` gives 217 and 174, the same pair the 4 October note and the first run of
7 October recorded, and 268 slots with committee chairs folded in. 215 is not a reading the data
yields; 174 is the all-years people count, not the number of distinct names in the slots, which is
176.) The four
year-photo gaps are unchanged: 1994-95, 1995-96, 2000-01, 2008-09.

## Access routes retested fresh

- `cgi/viewcontent.cgi` — HTTP 403, Cloudflare challenge. Closed.
- `web.archive.org` (the `if_` bypass, the CDX API, and the plain host) — connection reset at the
  TLS layer on every attempt, confirmed at the agent proxy (`ws_closed_mid_exchange`), not just at
  curl. Closed.
- `archive.ph` — same reset. Closed.
- `archive.org` itself (not the `web.` subdomain), `wku.edu/news` and `wkuherald.com` — all open
  and used below.

## Archive.org's Talisman catalog has no volume this file doesn't already know about

Queried `archive.org/advancedsearch.php` directly for every item whose identifier matches
`talisman*west` rather than trusting `scripts/talisman.py`'s own `YEARS` list. It returned exactly
the same 19 identifiers the script already holds (1943, 1946, 1947, 1963-65, 1971-81, 1986, 1987).
There is no newer or older volume sitting on archive.org that the script has missed. Since the
8-name overlap between this range and the officer gap was already fully searched and exhausted on
the third run today, this closes the question of whether that search was working from an
incomplete list — it was not.

## A fresh sweep of seven under-searched officer names on wkuherald.com

Picked the seven gap names with the fewest prior mentions in this file's own run history (checked
by grepping `.research/*.md`, 1-2 mentions each, against 3-7 for most others): Madison Keller
(Public Relations Committee Head, 2015-16), Devan Richardson (Associate Justice, 2017-18), Smita
Peter (Director of Information Technology, 2017-18), Abhishek Bose (Director of Information
Technology, 2016-17), Morgan Wysong (Public Relations Committee Chair, 2016-17), Jillian Kenney
(Sustainability Committee Head, 2019-20), Connor Ferguson (Gordon Ford College of Business
Senator, 2023-24).

Queried `wkuherald.com`'s WordPress REST API by name, then opened every post it returned
(`_embed` for featured media, plus the body text) rather than stopping at the search-result list:

- **Devan Richardson** — zero results.
- **Abhishek Bose** — one result, about an Indian student group's cultural celebration, no SGA
  content and no photograph of him.
- **Jillian Kenney** — two results, neither about SGA and neither carrying a photograph of her.
  Both are city-government stories the search matched on a committee name SGA happens to share;
  false matches from the search term, not leads.
- **Madison Keller, Smita Peter, Morgan Wysong, Connor Ferguson** — each returned genuine
  SGA-election or SGA-meeting stories, but every one checked carries either no image at all, or a
  featured photograph captioned for someone else entirely (Dahmer/Molyneaux/Lowry/Hounshell in
  28871; Richey/Neeper/Hart/Hushell in 32654; an uncaptioned group of "members of the WKU Student
  Government Association executive cabinet" in 71533; an uncaptioned group "sworn into their new
  committees" in 73874; Cissell and Bryant, not Ferguson, in 75688). None names the person being
  searched for in a caption or in the surrounding text next to an image.

No usable portrait for any of the seven. Consistent with the standing conclusion that the easy
wkuherald.com leads for this gap are exhausted; what remains is mentions in running text, which
CLAUDE.md's identification rule does not let a photograph be attached to.

## Nothing added

No portrait and no year photograph were added or removed. `data/photos.json` and `data/photos/`
are byte-identical to the merge-in of `origin/main`. `check_data.py` reports 61 years, 1,967
events, 60 presidents, clean, before and after this run.

## For the next run

- `viewcontent.cgi`, `web.archive.org` and `archive.ph` are closed for a fourth time today.
- The archive.org Talisman list is confirmed complete at 19 volumes; no further benefit in
  re-checking whether the script is missing one.
- Searching the remaining 167 under-mentioned officer names one by one on `wkuherald.com`, as this
  run did for seven, has a low and falling hit rate — every one checked today returned either
  nothing, an unrelated false match, or a photograph captioned for someone else. A route that
  reaches `digitalcommons.wku.edu`'s PDFs or a working `web.archive.org` session remains the most
  likely source of further portraits; working the open-web name list further without one is
  diminishing-returns work, not a dead end, but it should not be the whole of a future run.
