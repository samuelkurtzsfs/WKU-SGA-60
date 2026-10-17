# Photograph run, 16 October (fifth scheduled pass): gap re-confirmed, one new route tried and closed

## Priorities 1, 2 and 4: reconfirmed before searching anything

Per CLAUDE.md, checked whether an earlier run already closed these before spending time:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait entry in `data/photos.json`.
- **Priority 2** (every other president or student regent): a direct script comparison of every
  `leaders` entry in `data/years.json` against `(name, year)` pairs in `data/photos.json` found
  zero gaps.
- **Priority 4** (years with no photograph at all): zero years missing from `photos.json`'s
  `years` array.

Unchanged from the five prior passes today. Nothing to do on any of the three.

## Priority 3: the 189-slot gap, re-walked

`python3 scripts/portrait_gap.py --list` still reports 189 officer slots (159 people, 157 with no
portrait anywhere), the same count as every pass since 13 October. Diffed the full 189-name list
against the text of all 80 prior `.research/photo-run-*.md` reports before touching anything, per
the caution the fourth pass left behind: of 189 entries, 188 have already been typed into a prior
report. The one exception, 2022-23 graduate senator ShyAnte'e Williams, was itself retried and
closed by the fourth pass earlier today (the paper names her twice, under two spellings, in
articles with no identifying photograph).

### One route not tried before: WebSearch rather than direct curl

Every prior pass reached its sources with `curl`/`WebFetch` against digitalcommons, archive.org
and wkuherald.com directly. This pass instead ran general web search queries against a sample of
names from the gap that had stayed open for lack of a reachable source rather than a confirmed
negative, on the chance a search index would surface a cached page or an image URL the direct
site-crawling missed: ShyAnte'e Williams (2022-23), Nathan Cherry (2016-17, Speaker of the
Senate), Cody Cox (2015-17, Chief Justice) and Justin Goins (2022-23, Chief Justice).

All four searches confirmed the person and the office from WKU SGA's own minutes or legislation
PDFs, legitimate sources but ones that carry no photographs. None returned an image, a yearbook
page, or a Herald article with an identifying caption. The Cody Cox query is worth flagging for
whoever reads this next: it returned a current (modified 2/6/25) WKU SGA Judicial Council page
listing Morgan Gammons as chief justice and Gavin Grawe as associate chief justice, with no
mention of Cox at all — the page reflects 2024-25 officers, not 2015-17, so its absence proves
nothing about Cox's actual service and should not be read as a reason to doubt the roster entry.

No portrait found. No file added, no entry changed.

## Network state, retested fresh this session

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: still HTTP 403, Cloudflare "Just a moment..."
  challenge page, same as every pass since 13 October. This remains the only route into a 1990s
  Talisman page image, and it stays the structural blocker on the eight 1994-99 names in the gap.
- `archive.org` (not `web.archive.org`): open and working once requests are paced with a 2-3
  second gap and a full browser `User-Agent`; a burst of three unpaced requests briefly drew a
  503 from an unrelated archive.org outage, not a block, and cleared on retry.
- `web.archive.org`: unreachable again this session — the proxy reported the tunnel closing
  mid-exchange on a direct CDX request. Consistent with the fourth pass's finding that this block
  is intermittent and container-dependent; it was not available to test the Wayback route into
  `wku.edu/Dept/Org/Student/SGA` officer pages this pass either.
- `wkuherald.com`: open.

## What is still open

The 189-slot gap is unchanged in count, as it has been for six passes running today. Every name
in it has now been typed into at least one `.research/photo-run-*.md` report and searched without
success — not for lack of trying, but because the structural blockers (closed `cgi/viewcontent.cgi`
for 1990s Talisman pages, an archive.org Talisman holding that does not cover 1988-1994 or
1995-2002, an unreachable `web.archive.org` this session, and a wkuherald.com index that does not
reach earlier than roughly 2013) rule out every remaining name's only plausible source. Xavier
Spiess's withheld portrait, identified 15 October, is still waiting on a `years.json` roster entry
outside this agent's scope.

Nothing in this file is a new negative result on names nobody had tried; it is a confirmation,
using one additional search method, that the prior passes' negatives hold. The gap will not move
further under this session's network access. Whoever picks this up next should watch specifically
for `cgi/viewcontent.cgi` or `web.archive.org` coming back, since those are the two routes that
would open new 1990s and late-1990s/2000s names respectively.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean, 60 presidents,
no missing leader portrait, no year without a photograph, legislation files all present and real
PDFs. No file in `data/photos/` or entry in `data/photos.json` changed this pass. Merged
`origin/main` into `research-photos` first (clean merge, no conflict).
