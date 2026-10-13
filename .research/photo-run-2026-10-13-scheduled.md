# Photograph run, 13 October (scheduled): priorities 1/2/4 reconfirmed at zero, a fresh route tried and closed, two more officer names checked and ruled out

## Priorities 1, 2 and 4: reconfirmed against the current file, unchanged

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked against
`data/photos.json` before anything else. All four still carry a portrait.

**Priority 2** (any other president or student regent without a portrait): every `leaders`
record in `data/years.json`, across all 61 years, checked by name against `data/photos.json`.
Zero missing.

**Priority 4** (years with no photograph at all): checked which year ids in `data/years.json`
have no entry in `photos.json`'s `years` array. Only **1994-95**, unchanged since 11 October.

## Access this session

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403 against article 8989 (the standing
  1994-95 lead). Closed, same as every pass since late September.
- `web.archive.org` — connection reset at the TLS layer (`ws_closed_mid_exchange` at the agent
  proxy). Closed, matching the standing egress-policy denial.
- `archive.org` (plain, Talisman route) — open (302 then 200 on the djvu text). The eight names
  this volume range covers (Pulman, Bass, Young, Wilson, Wicks, Chesnut, Millay, Austin) are
  individually exhausted across at least five prior passes; not re-walked again today.
- `wkuherald.com` — open on both the bare search API and individual post fetches, with one
  mid-session 403 on a retry of the same query that cleared itself about 15 seconds later,
  consistent with the intermittency every recent note records.

## A genuinely new route tried: `wku.edu/news`'s own Student Government Association category

`wku.edu/news` carries a dedicated news category for "Student Government Association News"
(`index.php?view=default&categoryid=96&multinewsid=65`), reachable from the site's own category
dropdown and distinct from the general `?s=SGA` search this file's September/early-October passes
already used. Not tested as its own route before. Fetched it directly: it returns a normal page,
not a block, with the single line **"No News Articles Found."** This WKU news category has never
been populated — it is a dead end structurally, not an access problem, and does not need retrying
by a future pass with different access.

## Priority 3: two more names checked on wkuherald.com, neither usable

Picked two gap names with the thinnest prior search history in this file (per a grep count across
all `.research/photo-run-*.md`): **Jesse Banales** (Gordon Ford College of Business Senator,
2021-22) and **Jason Herlick** (Judicial Council 2019-20, Associate Justice 2021-22 — recorded in
the 11 October second-scheduled pass as returning a 403 on every attempt that session, so genuinely
unresolved rather than checked).

- **Jesse Banales** — 2 hits. "SGA discusses critical race theory legislation" has no image at
  all in the body. "SGA voting opens today: Who is on the ballot" carries a featured image whose
  caption names three other scenes (the Executive Cabinet, a DSU meeting, senators during
  Executive Reports) and never Banales by name.
- **Jason Herlick** — 1 hit, reachable this pass. "SGA judicial council 'fully functional'
  following four nominations" names him in running text (nominated alongside Derek Collins,
  Turner Reynolds and Holden Schroeder) but the article body carries no `<img>` tag at all. Its
  one image is a featured image (media id 19383), and that is unusable on its own terms: no
  caption, no alt text, and a hash filename uploaded in September 2019, so it identifies nobody.
  CLAUDE.md's identification rule needs a caption or text beside the photograph, and this one
  carries neither.

Neither name produced a usable portrait. `portrait_gap.py` still reports 189 slots / 159 people /
157 with no portrait in any year, unchanged.

## Nothing changed

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run. The build's
own photo-sync step withdrew 5 stale files from `site/photos` that `data/photos.json` no longer
references (routine housekeeping covered in `build.py`'s own comment, not a data change).
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean: 61 years, 1,968
events, 60 presidents, "the archive checks out against its own rules." `site/` was reverted
(`git checkout -- site/`) since the build output is not committed to this branch.

## For the next run

- The `wku.edu/news` SGA category is now a confirmed, permanent dead end (empty, not blocked) —
  do not retest it as an access question again.
- Jason Herlick's standing 403 from 11 October is resolved: the route opened this pass and his
  only hit carries no identifiable photograph. He can be dropped from the "blocked, not yet
  reached" list to the ordinary "checked, no usable portrait" list.
- Check `featured_media` separately from body `<img>` tags on every wkuherald post. A post can
  carry a featured image with an empty body, so a body-only check can read as "no photograph"
  when there is one. It is usually unusable anyway — uncaptioned and hash-named, as 19383 is —
  but that has to be established from the media record, not assumed from the body.
- The remaining untried names in the 159-person gap are still the ones the 11-12 October notes
  already named as untried: Matthew Johnson, Hope Wells, Alexis Mayne, Tribhuwan Singh, Garrett
  Baum, Danny Vuleta, Neel Patel, ShyAnte'e Williams, Mallory Hardesty, Reed Hensley, Brooke
  Mitchell, Kayla Distler, Elizabeth Gannon, David Darnell, Livi Ray, Callison Padgett, Tyreesha
  Morris — all post-2011 names reachable only through wkuherald.com's intermittent search, whose
  hit rate on the names already checked (Banales, Herlick, and the longer list in the 7-12 October
  notes) has been zero for several passes running. The two genuinely closed routes
  (`cgi/viewcontent.cgi`, `web.archive.org`) remain the more promising ones if either opens, for
  both the 1994-95 year-photo gap (article 8989, Herald 69:51, pp. 6-9) and the pre-2011 slice of
  the officer gap.
