# Photograph run, 13 October (afternoon): priorities 1/2/4 reconfirmed at zero, three more genuinely-untried officer names checked and ruled out, both gated routes still closed

## Priorities 1, 2 and 4: reconfirmed against the current file, unchanged

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked against
`data/photos.json` before anything else. All four still carry a portrait.

**Priority 2** (any other president or student regent without a portrait): zero missing,
reconfirmed across all 61 years.

**Priority 4** (years with no photograph at all): still only **1994-95**, blocked by the same
closed route as every pass since late September.

## Access this session

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403 against article 8989 (the standing
  1994-95 lead), full browser navigation-header set. Still closed.
- `web.archive.org` — TLS-layer connection reset (`Recv failure: Connection reset by peer`
  / `ws_closed_mid_exchange` at the agent proxy). Still closed.
- `wkuherald.com` — open, with the same short-lived intermittent 403s every recent note
  describes (cleared on a retry within 10-60 seconds each time this session).

## Priority 3: three genuinely untried officer names checked, none usable

Before picking names, grepped all `.research/photo-run-*.md` files for each remaining name in
`portrait_gap.py --list`'s pre-2016 slice to separate "actually searched, zero hit" from "only
ever named in a future-target list." Justin McDole, Tyler Scaff, Robert Bell, Cole McDowell,
Jackie Stewart, Kara Raley and Amber Daniel/Daniels had all already been individually searched in
earlier runs with no usable result. Three names in that same list had never actually been queried
— they had only appeared once each, inside a single sentence in `photo-run-2026-10-11-wayback-reopened.md`
naming future Talisman targets, not a search record:

- **Stacey Schepers** (Justice, Judicial Council, 2014-15) — zero hits in the local
  `data/herald-photos.json` caption index (21,304 captions) and zero posts from
  `wkuherald.com`'s live search API. A genuine absence on both the offline and live route, not an
  access failure.
- **Kasey Glasgow** (Student Affairs Committee Chair, 2014-15) — zero hits in the local caption
  index. One live hit, "SGA Holds First Meeting Tuesday" (3 Sep 2014,
  `wkuherald.com/39087/news/sga-holds-first-meeting-tuesday/`), which names her as the new
  Student Affairs chair in running text but carries no `<figure>` and no image at all in the
  body. Text naming an officer without a photograph beside it does not meet CLAUDE.md's
  identification bar.
- **Abigail Potter** (Justice, Judicial Council, 2014-15) — zero hits in the local caption index.
  Six live hits on the bare name, none about SGA, student government, or a Judicial Council
  (PCAL cultural programming, the folk studies program closure, a building-namesake debate, an
  art exhibit, a speaker series, a campus band performance) — checked each post's full body text
  for "SGA," "Student Government" or "Judicial Council" and found none. This is a different
  Abigail Potter, not the 2014-15 officer.

All three ruled out on their own terms, not on a closed route. `portrait_gap.py` still reports
189 slots / 159 people / 157 with no portrait in any year, unchanged.

## Nothing changed

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean: 61 years, 1,968
events, 60 presidents, "the archive checks out against its own rules." `site/` was reverted
since build output is not committed to this branch.

## For the next run

- The pre-2016 slice of the officer gap that this file's "future Talisman target" list named
  (Justin McDole, Kelly Simmons, Jackie Stewart, Kara Raley, Tyler Scaff, Abigail Potter, Allie
  Payne, Amber Daniels/Daniel, Robert Bell, Stacey Schepers, Cole McDowell, Kasey Glasgow) is now
  **fully exhausted on every open route** — every name in it has an individual search record
  somewhere in `.research/photo-run-*.md`, with zero portraits produced. The only path left into
  this slice is the 2012-13 through 2016-17 Talisman volumes behind the still-closed
  `cgi/viewcontent.cgi`.
- Both gated routes (`cgi/viewcontent.cgi`, `web.archive.org`) were tested directly this session,
  not assumed closed from memory, and both answered the same way they have since late September.
  Test them again before assuming either way, per this file's own standing advice — but do not
  expect a different answer without checking first.
- With the open-route (`wkuherald.com`) name list now run down to nothing new, the next session's
  highest-value use of an open window is either of the two gated routes reopening, not another
  pass over names already checked.
