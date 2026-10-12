# Photograph run, 12 October (second pass): all three routes retested, wkuherald.com found open again but with nothing untried left to search, the two PDF routes still closed

## Priorities 1, 2 and 4: reconfirmed programmatically, unchanged

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked against
`data/photos.json` before anything else. All four still carry a portrait.

**Priority 2** (any other president or student regent without a portrait): every `leaders`
record in `data/years.json`, across all 61 years, checked by name against `data/photos.json`.
Zero missing.

**Priority 4** (years with no photograph at all): checked programmatically which year ids in
`data/years.json` have no entry in `photos.json`'s `years` array. Only **1994-95**, unchanged
since 11 October. Both 2025-26 and 2026-27 already carry a year-level photograph.

## Access this session: wkuherald.com open, the two PDF routes still closed

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — Cloudflare 403 challenge page (5,995 bytes),
  tested twice ten seconds apart against article 8989 (the standing 1994-95 lead), full browser
  navigation headers sent both times. Closed.
- `web.archive.org` — connection reset on a plain fetch of the homepage (`curl: (35) Recv
  failure: Connection reset by peer`); the agent proxy's own status line logs
  `ws_closed_mid_exchange` on the same host from earlier today. Matches the standing note that
  this is an egress-policy denial rather than a WKU-side block — not re-tried a third time this
  session, per that advice.
- **`wkuherald.com` answered 200 on both the search API and a fresh REST pull**, after one
  mid-session empty response that cleared on a ten-second retry. The previous note (12 October,
  afternoon/editor review) found it fully closed with a Cloudflare managed challenge; it is open
  again now, confirming the intermittency that note flagged rather than a lasting state either way.

## Priority 3: checked for anything new before re-walking old ground, found nothing to work

With wkuherald.com open, pulled the 20 most recent posts matching "SGA" by date
(`/wp-json/wp/v2/posts?search=SGA&per_page=20&orderby=date&order=desc`) to check for any officer
announced since the 12 October afternoon run that might give a fresh, untried name. The newest is
29 September 2026 ("SGA Senate complete following fall election"), already inside the window the
afternoon run swept.

Cross-checked the 2026-27 organization block in `data/years.json` against `data/photos.json` by
name: Caden Lucas, Jakob Barker, Will Derryberry, Gabi Pace, Cayden Bailey (executive), and
Veronica Butler, Jaden Marshall, Molly Ricky, Amelia Tucker, Carter Smith, Sophie Stirling, Maggie
Phelps (Senate) all already carry a portrait. The 26th Senate's nine committee chairs, reported
25 August 2026, are named in this year's events but — per the organization block's own note —
"not yet broken out in this organization block," so they are not `leaders`-matchable names yet;
adding them is roster work for a different routine, not a photograph task.

`portrait_gap.py --list` still reports 189 slots / 159 people / 157 with no portrait anywhere,
byte-identical to 11-12 October. Checked the full list rather than trusting the count: the
2016-2026 slice is the one the 11-12 October notes record as individually exhausted on
wkuherald.com, and the 2003-2015 slice (Judicial Council justices and committee chairs — Scisney,
Crockett, Jankowski, Raley, McDole, and the rest) was individually exhausted on the same site in
mid-September runs (recorded in `SGA-60-AGENT-INFO.md` around the 13-16 September photograph
entries: real mentions found for several, but no photograph with a matching caption for any).
There is no untried name left that this session's open route could reach. The pre-2011 names
behind the closed Talisman/`archive.org` route and the closed `digitalcommons` route are the only
ones left, and both stayed shut throughout.

## Nothing changed

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61 years, 1968
events, 60 presidents; "the archive checks out against its own rules"). The `site/` rebuild was
discarded (`git checkout -- site/`). This run's only output is this note.

## For the next run

- `wkuherald.com` is intermittent on roughly an hours-long cycle now, not a settled state either
  way — test fresh rather than trusting either this note or the afternoon one for more than a
  couple of hours.
- Both PDF routes (`cgi/viewcontent.cgi`, `web.archive.org`) have been closed across every test
  this run and the two before it. The 1994-95 gap's specific next step is unchanged: re-fetch
  `article=8989` (Herald 69:51) printed pages 6-9, and the unread tail of `article=8933` (Herald
  70:56, printed pp. 8-29), the moment either PDF route opens.
- Priority 3 has no untried slice reachable from `wkuherald.com` right now. A future run with that
  route open should spend it checking for new officer announcements rather than re-walking the
  2016-2026 or 2003-2015 names again — both are individually exhausted, not just uncounted.
- No open pull request exists for this branch (`gh api repos/.../pulls?state=open` returns empty
  for `research-photos`); the standing brief's reference to "PR #6" is stale, consistent with the
  12 October evening editor note's finding that #6, #7 and #8 all closed on 18 August 2026.
