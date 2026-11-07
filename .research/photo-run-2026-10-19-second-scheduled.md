# Photograph run of 19 October (second scheduled pass): baseline reconfirmed again, no new names, access unchanged

This run's own brief named the four presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan
Gilley) and the rolling PR #6 as if neither had moved since August. Checked before anything else,
per the brief's own instruction to check whether an earlier run already got them: both are long
stale. #6 was closed many weeks and 800-plus pull requests ago. All four portraits have carried a
source in `data/photos.json` since before this file's own history begins, and every photograph run
since has reconfirmed it again. Treating this file's `.research/` log and `SGA-60-AGENT-INFO.md` as
the live backlog, not the stored prompt, per the practice that history itself recommends.

## Priorities 1, 2 and 4: unchanged from this morning's run

Same checks the 2026-10-19-scheduled.md run made a few hours earlier, repeated fresh rather than
trusted on the strength of that file alone:

- Priority 1 (the four named presidents): all four still carry a portrait.
- Priority 2 (every other president or student regent): `check_data.py` still reports no missing
  leader portrait across all 73 `leaders` records, 61 years.
- Priority 4 (years with no photograph): still zero; every year carries at least a leader portrait
  or a year-level photograph.

## Priority 3: the 189-slot gap, re-measured, not re-searched

`python3 scripts/portrait_gap.py --list` reports the same 189 officer slots, 159 distinct people,
157 with no portrait anywhere in the file — identical to this morning's count and to 18 October's.
Checked `data/years.json` for any `organization` entry added since this morning's run (the two new
2026-27 chairs, Elizabeth Allen and Tyreesha Morris, were already checked and declined there): none
found. There is no new name to search this pass.

Before spending this run's budget re-searching the standing 157, checked how many of them this
project has already searched and how recently. A sample of ten names spread across the list's
decades (Vern Pulman, David Bass, David Young, Alice Wicks, Mark Chesnut, John Holland, Kelly S.
Smith, Connie Hoffmann, Chris Millay, Dwight Austin) turns up in **9 to 29** separate
`.research/photo-run-*.md` files apiece, going back to mid-September. `data/photos.json` has not
gained a single new entry since the 15 October run that is the last commit touching it at all — nine
calendar days and roughly twenty scheduled photograph runs with nothing landed. That is not this
run's finding alone; it is the condition every run since has been operating under without saying so
in those words.

## Network state, retested fresh rather than assumed stale

Same three probes this morning's run made, repeated independently rather than trusted secondhand:

- `cgi/viewcontent.cgi` (the only route to the pre-2003 Herald and the 1988-2003/2012+ Talisman
  volumes TopSCHOLAR holds that archive.org does not): HTTP 403, Cloudflare challenge. Unchanged.
- `web.archive.org`: connection reset mid-exchange at the agent proxy (`ws_closed_mid_exchange`).
  Unchanged.
- A TopSCHOLAR item landing page (`dlsc_ua_records/4039`): answers (301, a normal redirect to the
  canonical item URL), matching this morning's finding that landing pages work while the PDF
  endpoint does not. This gives abstracts and metadata, never the page image a portrait
  identification needs.
- `archive.org` (plain item/download host): the one open image route, and it covers only 1971-1981,
  1986 and 1987 of the Talisman — a range this archive's photograph runs have already worked
  repeatedly, which is why the 157 names sitting in the 1990s-2020s cannot be advanced by it.

No change in any of the three blockers that have held since at least 18 October. Nothing in this
run's own access attempts contradicts what the last several runs already recorded.

## Why this run adds a log entry rather than a tenth search of the same names

Searching the same 157 names again today, under the identical closed access this file already
confirms closed, would not be new research; it would be the same dead end written up a tenth or
twentieth time per name, for names this project's own `.research/` history shows have had that
exact treatment already. The one thing today's pass can honestly add is the measurement above: zero
new portraits in nine days across roughly twenty runs, with the blocking conditions re-verified
rather than assumed. That is worth recording once, plainly, rather than buried identically in a
twenty-first file that reads like the twentieth.

## No file changed in `data/photos.json` or `data/photos/`

`python3 scripts/build.py` then `python3 scripts/check_data.py`: both exit clean. 61 years, 60
presidents, no missing leader portrait, no year without a photograph. This run's only output is
this note.
