# 8 October 2026 (photograph agent, morning) — priorities 1–2 confirmed closed, a full local sweep finds nothing new, two leads barred

## Priorities checked first, as instructed

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
portrait in `data/photos.json`, each with a captioned source. No action needed; this matches
`SGA-60-AGENT-INFO.md` §8's record of them being settled in August.

**Priority 2** (any other president or student regent without a portrait): computed directly from
`data/years.json` against `data/photos.json` — every `leaders` record in every year has a matching
`photos.json` entry. Zero missing. This project has had a full set of leader portraits for some
time; the open gap is entirely in priorities 3 and 4 below.

**Priority 4** (years with no photograph at all): only two remain, 1994-95 and 2000-01. Neither
year's Talisman is among the 19 volumes archive.org holds (1943, 1946, 1947, 1963-65, 1971-1981,
1986, 1987), so closing either needs a TopSCHOLAR PDF.

**Priority 3** (officer portraits) is the real gap: 948 cabinet/Senate officer slots, 215 without a
portrait, 174 distinct names, across 42 years. This is unchanged from the figure the 7 October
night report corrected to and is what this run worked.

## What was tried, and what is still closed

Before any name-by-name search, the sources this project depends on were tested directly rather
than assumed from memory of past runs:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare `cf-mitigated: challenge`,
  on a plain GET with full navigation headers (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode:
  navigate`, `Upgrade-Insecure-Requests: 1`) and a `Referer`. This blocks every Talisman and Herald
  PDF on TopSCHOLAR, which is why no portrait in `photos.json` has ever cited a `digitalcommons`
  Talisman URL — confirmed by grepping the file: zero.
- `digitalcommons.wku.edu`'s own search page — HTTP 403, "Just a moment..." (Cloudflare challenge),
  as `CLAUDE.md` already documents. Article landing pages (`dlsc_ua_records/NNNN`, `sga/NNNN`)
  themselves load fine (HTTP 200) and are text-readable; it is specifically the PDFs and the search
  box that are gated.
- `web.archive.org/wayback/available` — HTTP 429, "too many requests."
- `archive.ph` — connection reset mid-handshake.

All four are the same blockers the last several night reports recorded. Nothing has reopened.

## The one new avenue tried: a full local sweep of the harvested Herald photo cache

`data/herald-photos.json` holds 21,304 Herald images harvested with their captions, 2010 to 2026,
and costs nothing to search — it is already on disk. Matched all 174 missing officer names against
every caption in the file in one pass (not a name-by-name sweep). Six names matched anywhere in the
cache: four are already in `_do-not-use.json` (Chris Jankowski, Cody Cox, Mark Clark, Kayla
Distler), and the two new ones both failed on inspection:

- **Jason Heflin** (1997-98, Hillraisers Committee chair) — matches a 24 March 2015 photograph of a
  home-brewer by that name opening White Squirrel Brewery. The caption ties him to a 2015 business,
  not to SGA, with no year of attendance given.
- **Jessica Williams** (2005-06, Academic Affairs Committee chair) — matches a 2010 dance
  performance and two 2019 Climate Strike photographs of a "then-current junior from Florence." The
  2005-06 officer would have graduated years before either; neither caption mentions SGA regardless.

Both are now barred in `data/photo-finds/_do-not-use.json` so a future pass does not re-propose
them. Because the cache only runs from 2010, it cannot help with the two open year-photo gaps
(1994-95, 2000-01), both of which predate it.

## Targeted web searches, for names likely to have press coverage

Tried eight more names from the highest-gap years (2016-17: 15 missing; 2017-18: 14; 2021-22: 14;
2022-23: 16) and the officer roles most likely to draw individual coverage — Speaker of the Senate,
Chief Justice, named directors — rather than rank-and-file senators: Nathan Cherry, Ryan Richardson,
Elizabeth DeLozier, Tribhuwan "Trib" Singh, Smita Peter, Deekshita Madas, Justin Goins. Singh is the
only one with a Herald article under his own name (wkuherald.com/61104, "Newly elected SGA members
share goals for the semester"); the article uses one generic feature image for the whole piece, not
individual photographs, so there is nothing to caption him with. The rest returned nothing citable
at all — not even a misattributed photograph to reject, just no coverage. Nothing added, nothing
barred (a bare absence of search results is not a finding and does not belong in the do-not-use
file).

## Why this run stops here rather than continuing name-by-name

The night reports since late September describe exactly this pattern — TopSCHOLAR, Wayback and
archive.ph all closed, and name-by-name wkuherald.com sweeps turning up nothing — across several
prior passes (30 names tried the evening of 7 October, "none confirmable"; the 7 October night
report calling the hit rate "low and falling"). This run re-verified the blockers directly rather
than taking that on faith, then ran the one search this project had not yet done exhaustively — the
full local caption cache against every missing name at once — and it confirms the same ceiling: six
raw hits out of 174 names, four already dead, the other two dead on inspection. The 167 or so names
with zero hits anywhere in 21,304 captions are not a lead; they are names the Herald's photographed
coverage never happened to catch, in a cache that itself only starts in 2010 and so cannot speak to
the pre-2010 majority of the gap at all.

What would actually move priority 3 and priority 4 is the same thing the 7 October run named: a
working route to the TopSCHOLAR PDFs (Talisman yearbooks for 1988-2026, Herald issues, UA1C image
collections) or a Wayback session that isn't rate-limited. Neither opened this run. No photograph
was added or withdrawn from the published record; `data/years.json`, `data/photos.json` and
`data/photos/` are unchanged from `main`. The only change is the two new barred entries above.

`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean.
