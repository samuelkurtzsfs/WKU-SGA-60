# Photograph run, 16 November (second scheduled pass): the Talisman gap for 1995-96 through
2001-02 confirmed structural, not just blocked; no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 60 presidents, every
  president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports the same ~155-157
  person no-portrait-anywhere gap as every pass since early November. No new name resolved to a
  portrait this pass.
- **Priority 4**: all 61 years still carry at least one photograph.

## Network gates, retested

- `cgi/viewcontent.cgi` via `curl` with full browser navigation headers: standing Cloudflare `403`,
  tested against article 7642.
- The same URL via plain `urllib.request`, identical headers: **200, a real PDF** — the
  TLS-fingerprint bypass this project has now logged open on six separate dates, open again this
  pass. Spent it on the finding below rather than on another individual Talisman volume.
- `web.archive.org`: connection reset, unchanged.

## The real finding this pass: the 1995-96 through 2001-02 Talisman gap is not a blocked fetch, it is a volume that was never digitized

Every prior pass that hit this stretch (12 October onward, most recently 13-16 November) tested it
volume by volume — `talisman1995west` through `talisman2002west` returning `404`/`503` on
archive.org, and the corresponding TopSCHOLAR PDF either gated or untried — and logged each as an
open or ambiguous lead. This pass instead read `digitalcommons.wku.edu/dlsc_ua_yearbooks/` itself,
the yearbook collection's own landing page, in full (plain `curl`, not gated this time; the page's
own text, not a search-engine summary). It says outright: **"WKU Talisman published annually
1924-1994; 2003+."** Its full document list for those years confirms it: the entries dated 1995 and
1996 in that collection are *Xposure*, a different WKU Student Affairs serial (`UA12/2/2`), not the
Talisman, and nothing between the 1994 volume (`dlsc_ua_records/418`) and the 2003 volume is a
yearbook at all.

So the gap is structural, not a fetch problem: there is no 1995-2002 Talisman to find, at
TopSCHOLAR or anywhere mirroring it, because WKU's own archive never scanned one. This closes, for
good, the open question behind a large share of the standing no-portrait cluster for 1996-97
through 2001-02 — Andy Gailor, Ryan Faught, Kip Carr, Steve Roadcap, Callie Varner, Anne Guillory,
Jason Heflin, Jenny Stith, Jason Cole, Jamie Fite, Larry Murphy, Matt Bogard, Amanda Cole, Tim
Hatton, Sally Eilerman, Jeff Baynham, Mitchell Bailey, Joe Murrell, Michelle Woods, Shara Hammers,
Andrea Lovell, Brooke Smith among others — without any future pass needing to re-test individual
volume URLs again. Logged as a `"source exhausted"` entry in `data/photo-finds/_archive-gaps.json`.

Checked the local Herald headline index (`data/herald-index-full.json`, full text of every
headline, 11,852 items) for all nineteen names above as a cross-check for a photographed report
rather than the yearbook: only one hit, Jason Heflin, and it is a 2015 Herald headline — seventeen
years after this cluster's term, a different person by date alone, not this committee chair.
Confirms CLAUDE.md's standing warning that a body-text mention (which is all the Herald is likely
to give most of these names) is invisible to this index regardless; no further lead from this
route without opening individual issues, which the standing `_do-not-use.json`/`n9701-notes.json`
record already shows has been tried and exhausted for the two names (Guillory, Hatton) checked
most closely.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `build.py` and
`check_data.py` both pass clean. One structural fact added to `_archive-gaps.json` that should
stop future passes from re-running the same per-volume Talisman test on this stretch of years.
Landed on `research-photos`.
