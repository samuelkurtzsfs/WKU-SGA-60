# Photograph run, 11 October (second scheduled pass): priorities 1-2 reconfirmed at zero, both PDF routes closed all session, several new officer leads checked on wkuherald.com with nothing usable

## Priorities 1 and 2: reconfirmed, nothing to do

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked directly against
`data/photos.json` before anything else. All four still carry a portrait. Nothing to do, as every
run since 20 August has found.

**Priority 2** (any other president or student regent without a portrait): every `leaders` record
in `data/years.json` checked programmatically against `data/photos.json` by name. Zero missing —
all 73 leader records, across all 61 years, carry a portrait. (This is the leader portraits
only; 1994-95 still carries no year photograph, which is the gap described below.)

## Access this session: both PDF routes closed throughout

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — Cloudflare 403 challenge on every attempt, with
  full browser navigation headers. The plain `digitalcommons.wku.edu/` homepage answers 200, so
  only the download endpoint is gated, consistent with every pass since the gate closed in late
  September.
- `web.archive.org` (the `id_`/`if_` bypass) — unreachable all session. The agent proxy's own
  status endpoint logged `ws_closed_mid_exchange` on every attempt, including a plain fetch of
  `https://web.archive.org/` itself, not just the bypass URL form.
- `archive.org` (direct, not Wayback) — reachable, but intermittently: a `talisman<year>west`
  `_djvu.txt` request sometimes 500'd on the first try and came back 200 on a retry a few seconds
  later (1980, 1987 both did this). Confirmed again this run that archive.org's Talisman holdings
  stop at 1987 — 1988 through 2002 tested in the 1990s/2000s range relevant to the officer gap,
  all came back 503 (item not available at this path), matching the coverage
  `SGA-60-AGENT-INFO.md` and the earlier photograph runs already document (1971-1981, 1986,
  1987 only; CLAUDE.md notes the archive.org Talisman full texts but states no year range).

With both PDF routes closed, the 1994-95 year-photograph gap the last run (11 October, later
scheduled) left as its specific next step — re-fetching viewcontent article 8989 (Herald 69:51)
and reading printed pages 6-9, and finishing the unread pages of article 8933 (Herald 70:56) —
could not be attempted this pass. Neither Wayback snapshot nor the live endpoint would answer.
Left exactly as that run described it for whichever pass next finds the route open.

The 8-name archive.org-covered officer gap (Pulman, Bass, Young, Wilson, Wicks, Chesnut, Millay,
Austin — the only `portrait_gap.py` entries that fall inside 1971-1981/1986/1987) was not re-walked
again this pass. It was independently re-walked from source on 3 October and every name confirmed
exhausted then; nothing in this run's access situation gave reason to doubt that finding, so
re-doing it a third time would have spent the Talisman-reachable window on a question already
answered rather than on anything new.

## Priority 3: new officer names checked on wkuherald.com, nothing usable found

`portrait_gap.py` still reports 189 officer slots / 159 people / 157 with no portrait in any year
— unchanged by this run. wkuherald.com's WordPress search API was reachable this session (its own
front page returns 403 to a bare fetch, but `/wp-json/wp/v2/posts?search=...` answers normally,
intermittently 403'ing roughly one request in three regardless of pacing — a retry a few seconds
later usually cleared it). Searched names from the 2016-2025 slice of the gap list not already
recorded as tried in this file's own history:

- **Erika Puhakka** (Associate Justice 2018-19, Chief Justice 2020-21) — 5 hits, none captioned
  with her name. One hit's photograph is captioned for Isaac Keller alone (it is filed in
  `data/photos.json` as Keller's own portrait, for 2018-19, 2019-20 and 2020-21, and not as
  Puhakka's; she has no portrait on file in any year); the rest are uncaptioned
  featured images or caption other people (crowd photos, Resolution 4-19-S coverage).
- **Turner Reynolds** (Associate Justice 2019-20 through Associate Chief Justice 2021-22) — 2
  hits, one a football photo matched on an unrelated "Turner" in the caption, the other's
  featured image uncaptioned.
- **Jason Herlick** (Judicial Council 2019-20, Associate Justice 2021-22) — search returned 403
  on every attempt this run; not reached.
- **Brenna Mathews** (Secretary of the Senate 2019-20 through 2020-21) — 2 hits, neither captioned
  with her name (a Model Arab League story, an SGA meeting story with an uncaptioned image).
- **Nicole Massarone** (Judicial Council 2021-22) — 2 hits. "Newly elected SGA members share goals
  for the semester" (23 Sep 2021) profiles her by name along with ten others, Tribhuwan Singh
  among them (also in the gap list) — but the article carries zero `<img>` tags in its body, text
  only, and its featured thumbnail has no caption. No usable photograph.
- **Josh Zaczek** (Legislative Research Chair 2018-19, 2019-20) — 6 hits, captions identify other
  people in SGA meeting photographs (Garrett Edmonds, Symone Whalin, Kenan Mujkanovic, Anthony
  Survance) but never Zaczek.

No name this pass produced a caption meeting CLAUDE.md's bar — a photograph whose subject is
named, alone or clearly, in the caption or the text immediately beside it. Several hits are
generic SGA-meeting featured images with no caption at all, which the project has already ruled
out as a source (a face with no identifying text is worse than no face).

## Nothing changed

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run. No new file
to verify. `python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61
years, 1968 events, 60 presidents; "the archive checks out against its own rules") — reconfirming
the state inherited from the prior run rather than this pass's own change, since this pass made
none.

## For the next run

- The two closed PDF routes are the actual blocker on the 1994-95 year-photo gap. Test both before
  anything else; if either opens, the specific next step is unchanged from the 11 October
  (later-scheduled) report: re-fetch viewcontent article 8989 and read printed pages 6-9, and
  read the unread tail (printed pp. 8-29) of article 8933.
- Priority 3's 159-person gap is large and this pass covered six names from its 2016-2025 slice
  without opening a new one. The remaining untried names in that slice, from `portrait_gap.py
  --list`: Matthew Johnson, Hope Wells, Jillian Kenney, Alexis Mayne, Tribhuwan Singh, Jesse
  Banales, Garrett Baum, Danny Vuleta, Neel Patel, ShyAnte'e Williams, Mallory Hardesty, Reed
  Hensley, Brooke Mitchell, Kayla Distler, Connor Ferguson, Elizabeth Gannon, David Darnell, Livi
  Ray, Callison Padgett, Tyreesha Morris, Carter Smith, and the 1990s/2000s names that archive.org
  cannot reach while Talisman coverage stops at 1987 (Chairperson/Committee names from 1992-93
  through 2007-08 in the list, none of them reachable by the routes open this session).
- wkuherald.com's search API 403s roughly one request in three regardless of pacing; a short retry
  clears it. Budget for that when scripting a sweep rather than treating one 403 as the host being
  closed.
