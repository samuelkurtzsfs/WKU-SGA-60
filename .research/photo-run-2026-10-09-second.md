# 9 October 2026 (photograph agent, second pass this day) — priorities 1–2 reconfirmed, all three gates retested cold on two independent fetch paths, nothing open

> **Editor's note, 9 October.** The counts and the gate results in this file were re-derived and
> hold exactly. One conclusion did not: this run reported the 159-name officer gap as a fully
> worked queue, and eight of those names have no recorded photograph search at all. The section
> below is corrected and names them. Nothing on the public site was affected — this file is a
> working note — but it would have told the next run to stop looking.

## Priorities 1–2, checked first as instructed

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Settled since August; nothing to do.

**Priority 2** (any other president or student regent without a portrait): every `leaders`
record in every year still has a matching `photos.json` entry (checked by script against the
current tree, not assumed from this file). Zero missing.

## The gap, recounted against the tree this run actually has

`scripts/portrait_gap.py` on the current `main` tip (after the 07:59 and 09:26 UTC commits
landed earlier today): 189 officer slots short a face, held by 159 distinct people, 157 of whom
carry no portrait anywhere in the file. That is down from the 09:26 note's 217/176 — the morning
runs' twelve cleared names and the editor's recount both already reduced it before this run
started. Cross-checked every one of the 159 names against every `.research/photo-run-*.md` file
and `NIGHT-REPORT.md`: **151 have been named in at least one prior search attempt** (the wkuherald
caption sweep, the local Herald photo-cache sweep, or a Talisman read). One that looked untried by
a plain name search, ShyAnte'e Williams, turns out to have been tried twice (23 August under both
spelling variants, zero hits both times).

**Eight have not.** Editor's recount, 9 October, matching all 159 names from
`portrait_gap.py --list` against the 53 `photo-run-*.md` logs and `NIGHT-REPORT.md`, with
accents and apostrophes normalised so spelling variants could not hide a hit:

| Year | Office | Name |
|---|---|---|
| 1994-95 | Judicial Council Member | Grace Hancock |
| 1995-96 | Chairperson, Cultural Diversity Committee | Margaret Carter |
| 1995-96 | Chairperson, Public Relations Committee | Cindy Chiapetta |
| 1997-98 | Chairperson, Campus Improvements Committee | Callie Varner |
| 1998-99 | Chairperson, Academic Affairs Committee | Larry Murphy |
| 2008-09 | Chair, Public Relations Committee | Vanessa Scott |
| 2012-13, 2013-14 | Justice, Judicial Council | Justin McDole |
| 2014-15 | Justice, Judicial Council | Allie Payne |

All eight appear elsewhere in `.research/` — in `officers-eras.json`, `profiles-done.txt` and the
2003-09 senate rolls — which is roster and profile work, not a photograph search, and is what a
plain grep of `.research/` mistakes for one. None of them carries an entry in
`data/name-aliases.json`, so no alias is masking a prior attempt either.

So the gap is a **mostly** worked queue, not a fully worked one, and the three gates below are
not the only remaining route. The last three names sit in 2008-09 and later, which is the
wkuherald.com era, and wkuherald.com answered HTTP 200 this session while all three gates were
shut. A first search of these eight is owed before anyone writes that the queue is finished.

## The three gates, retested cold, on two fetch paths rather than one

Every recent note says to retry these cold rather than trust the last verdict. Did so twice this
run — once with `curl` (full browser navigation headers, correct `Referer`), once with the
platform's `WebFetch` tool, a separate code path from a different egress point:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (article 7642, a known-good PDF when this gate is
  open) — `curl`: HTTP 403, Cloudflare "Just a moment..." challenge, 6,038 bytes. `WebFetch`:
  HTTP 403 Forbidden, no body. Same block, both paths.
- `web.archive.org` (`if_` bypass against the same article) — `curl`: TLS handshake reset
  (`Recv failure: Connection reset by peer`), logged identically at the agent proxy as
  `ws_closed_mid_exchange`. `WebFetch`: "unable to fetch from web.archive.org." Same block, both
  paths.
- `archive.ph` — `curl`: same TLS reset, same proxy log line. Not re-tried under `WebFetch`,
  since the `curl` failure is at the handshake and a different client would not change what the
  network does to the packet.

None open. `archive.org/download/...` (the Talisman full-text route) was not re-tested for
access this run, since it was not needed: checked which of the 159 gap names fall in academic
years archive.org actually holds a Talisman for (1971-72 through 1980-81, and 1986-87) and the
answer is zero — every gap name in that span (Pulman, Bass, Young, Wicks, Wilson, Chesnut,
Holland, Smith, Millay, Austin) was already tried against those exact volumes by earlier runs and
failed on caption ambiguity or absence, not on access, which is why they are still in the gap
rather than why they haven't been looked at. There is nothing left in the currently-open archive.org
holdings that this gap's names would still benefit from re-reading.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed. `data/years.json` is untouched, as
always. `build.py` and `check_data.py` both exit clean (61 years; all 73 `leaders` records carry a
portrait for their own year, held by 66 distinct people; same 189/159/157 officer-gap figures as
above). This run's only output is this
note.

## For the next run

The three gates are the whole remaining problem now, not a research backlog — every name reachable
by any other method has a negative result already on file, most of them more than once. Retry the
gates cold at the top of the next run, as always; the intermittency documented across September and
October is real, so a closed window today says nothing about tomorrow. If a gate opens, the leads
already named in the 24 August and 7-9 October entries of `SGA-60-AGENT-INFO.md` §8 (the 1619 finding
aid, now closed for good as a non-image inventory; the 1994-95 and 2000-01 year-photo gaps; the
pre-2003 officer names above) are where to spend the window.

But do not wait on a gate to start. The eight names in the table above have never been searched
for a photograph, and the three from 2008-09 onward are reachable by a route that is open now.
Search those eight first, on wkuherald.com and in the local Herald photo cache, and record the
result either way — a negative recorded by name is what lets the next run skip it honestly.
