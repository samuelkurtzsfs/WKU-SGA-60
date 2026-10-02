# 2 October 2026, evening (photograph routine, scheduled, fourth run of the day)

## What was checked before doing anything

Same starting point as the three earlier runs today: Nick Todd, Katie Dawson, Jeanne Johnson and
Reagan Gilley all still carry a portrait in `data/photos.json`. All 73 top-level `leaders` records
(every president and every student regent) have one. `research-photos` was already merged onto
the current `origin/main` tip (`6f422942`); no conflict work was needed. `python3 scripts/build.py`
and `python3 scripts/check_data.py` both ran clean on the unmodified tree before any new work (61
years, 1963 events, 60 presidents, all portrayed; the build's routine withdrawal of two stale files
from `site/photos/` is normal housekeeping against files no longer in `data/photos/`, not a new
data problem).

## Access re-tested again, nothing changed

- `cgi/viewcontent.cgi` still `403`, Cloudflare "Just a moment..." challenge (tested against a
  fresh article, 1000/dlsc_ua_records).
- `web.archive.org` still resets at the TLS handshake (`curl: (35) Recv failure: Connection reset
  by peer`).
- `wkuherald.com`'s WordPress REST API still answers normally (200).

## The officer-portrait gap list rebuilt fresh: 215, not 217

Rebuilt the executive/Senate officer gap list directly from `data/years.json` against
`data/photos.json` rather than trusting the figure in the last three reports. It now counts 215,
not 217 — the two-record difference is not a regression; the names the gap list use are drawn from
`organization.executive` and `organization.senate.officers` only, and a small amount of
reorganizing elsewhere in `years.json` since the 217 count moved two names out of those two blocks
without changing anything photograph-related. Decade breakdown: 1960s 4, 1970s 5, 1980s 9, 1990s
36, 2000s 43, 2010s 73, 2020s 45.

## Two names in the whole list had never been searched before; neither produced anything

Cross-checked all 215 names against every file in `.research/` (all `photo-run-*.md` reports) to
find names truly untried rather than repeat a name already exhausted. Two turned up — the entire
217/215-record list has now been searched at least once:

- **Deekshita Madas** (Director of Information Technology, 2017-18) — a general web search finds
  only a Spring 2018 WKU CS 560 course-project page listing her among five group members; nothing
  connects her to SGA or carries a photograph.
- **Hayden Skinner-Fine** (Associate Justice, 2016-17) — a general web search finds a current
  staff-directory page at Mount St. Joseph University, where she now works, and nothing from her
  time at WKU. The MSJ page carries a current professional headshot, but it is not a university
  archive or news page from her time in the role and is outside this project's sourcing and privacy
  rules; it was not used.

Neither search produced a usable, caption-identified photograph.

## Checked wku.edu/sga's own current pages for anything missed

Not tried by name in earlier reports: the live `wku.edu/sga` site itself, as distinct from
`wku.edu/news` and `wkuherald.com`. `wku.edu/sga/about/history.php` carries only a 60th-anniversary
banner graphic, no officer photographs or archive gallery. `wku.edu/sga/executive/index.php`
carries headshots for the five current (2026-27) executive officers — Caden Lucas, Jakob Barker,
Will Derryberry, Gabi Pace, Cayden Bailey — all five already in `data/photos.json` from earlier
research, so this produced no new names. The site's navigation confirms it publishes no senator or
Judicial Council roster or photographs, current or historical, so this route is now checked and
does not extend further.

## Nothing added

No file in `data/photos.json` or `data/photos/` changed this run. The gap list (215 officer
records, four years without a scene photograph: 1994-95, 1995-96, 2000-01, 2008-09) is unchanged
in substance from the last three reports.

## For the next run

The officer-portrait gap list is now fully searched, by name, against `wkuherald.com`, the complete
local Herald/Talisman index, general web search, and the live `wku.edu/sga` site. Nothing further
can be done against any of it until `cgi/viewcontent.cgi` or `web.archive.org` reopens. Keep
re-testing both cold on each run — they have reopened briefly before without warning — but stop
re-running name-by-name searches on the existing list without a new source or a reopened route.
