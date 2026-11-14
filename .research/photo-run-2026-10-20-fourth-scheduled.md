# Photograph run, 20 October fourth scheduled pass: baseline reconfirmed a fourth time today, both blocked routes still closed, eight more under-searched names run to ground with nothing new

## Priorities 1, 2 and 4, checked directly against the data rather than assumed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` reports no missing leader portrait. Independently
  cross-checked every `leaders` entry in `data/years.json` against `data/photos.json` by script:
  zero presidents and zero student regents without a portrait.
- **Priority 4**: cross-checked every one of the 61 years in `data/years.json` against
  `data/photos.json`'s `years` list and leader-portrait coverage: every year carries at least a
  year-level photograph or a leader portrait. The two year-photo gaps this file's own history
  carried as open through 8 October (1994-95, 2000-01) are both now closed — `2000-01-sga-debate.jpg`
  and `1994-95-evans-higdon-campaign-ad.jpg` are both on file, landed by one of this morning's
  earlier passes on this branch.

## Priority 3: eight names picked for the fewest prior mentions, checked fresh

Before searching, grepped every `.research/photo-run-*.md` for each of the 159 names on
`scripts/portrait_gap.py --list`'s standing gap and ranked by hit count, same method the 7 October
fourth pass used. Excluded the five names already run down earlier today (Bass, Chesnut, Wilson in
the third pass; Pulman, Young, Wicks, Millay, Austin in the second). Picked the eight with the
fewest remaining mentions: Jeff Baker (Parliamentarian, 1994-95), Jenny Stith (Chairperson, Public
Relations Committee, 1997-98 / Justice, Judicial Council, 1998-99), Sally Eilerman (Co-Chair,
Hillraisers Committee, 1998-99), Kathleen Hennessey (Justice, Judicial Council, 2004-05), Emilee
Bishop (Parliamentarian, 2006-07), Jacob A. Miers (Secretary of the Senate, 2007-08/2008-09), Jeff
Baynham (Parliamentarian, 1998-99), Cacy A. Schooler (Secretary of the Senate, 2007-08).

Queried `wkuherald.com`'s WordPress REST API by surname (the exact two-word query already tried by
an earlier run for Baker, Stith, Bishop and Miers in full name form had returned nothing, so this
pass tried the bare surname instead, in case the exact-phrase match was the reason):

- **Jenny Stith, Sally Eilerman, Jeff Baynham** (1994-95/1997-98/1998-99): all three predate
  `wkuherald.com`'s roughly-2003 coverage start; confirmed by running the search anyway rather than
  assuming — Stith and Eilerman return zero posts, Baynham returns two unrelated hits (a 2011
  fraternity-award story and a 2004 letter to the editor from a different Baynham). No lead.
- **Jeff Baker**: same era problem; zero posts.
- **Kathleen Hennessey**: one hit, a 2024 story about Kyle Rittenhouse speaking on campus —
  an unrelated Hennessey named in passing, not this officer. No lead.
- **Emilee Bishop**: zero posts under either the full name or the surname alone.
- **Jacob A. Miers**: zero posts under the full name or "Miers" alone.
- **Cacy A. Schooler**: "Schooler" returns eight posts, 2023-2026, none naming this person — an
  unrelated recent byline/source sharing the surname. No lead.

None of the eight pre-2003 names (Baker, Stith, Eilerman, Baynham) can be checked against
`archive.org`'s Talisman full text either: that route's known coverage is 1971-1981, 1986 and 1987
only (per `SGA-60-AGENT-INFO.md` §4), and 1994-95/1997-98/1998-99 fall outside it. No open route
reaches these four years at all right now; only `digitalcommons.wku.edu`'s blocked PDF endpoint
could.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: HTTP 403, Cloudflare "Just a moment..." challenge,
  tested with the full navigation header set. Still closed.
- `digitalcommons.wku.edu` ordinary item/landing pages: HTTP 200 (`/dlsc_ua_records/4686/` and the
  `/talisman/` collection root both answer normally; only the file-download endpoint is blocked).
- `web.archive.org`: `curl: (35) Recv failure: Connection reset by peer` at the agent proxy. Still
  closed, consistent with the last several passes today.
- `archive.org` (plain item host): open, used to independently re-verify the current year-photo and
  leader-portrait baseline.
- `wkuherald.com` WP-JSON: open. No post newer than 14 October's "SGA funds new Preston Center
  area..." exists yet — checked the ten most recent SGA-tagged posts by date; nothing past that one.

## What this run leaves unchanged

`data/photos.json` and `data/photos/` are unchanged from this morning's third pass. 189 officer
slots (157 people) remain without a portrait, per `scripts/portrait_gap.py`. Every name on that list
has now been searched, by this file's running count, at least three times apiece against every
route reachable from this container today, and the eight picked this pass for being the least-tried
reached the same dead end the better-tried names already had. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean (61 years, 60 presidents, no missing leader
portrait, no year without a photograph). Landed on `research-photos`.
