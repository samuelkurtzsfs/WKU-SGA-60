# Photograph run, 18 October (scheduled): network state unchanged, the archive.org Talisman volume list confirmed exhaustive rather than assumed, a web-search spot check of six recent officer names closed without a hit

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked against the current `data/years.json` and `data/photos.json` before touching anything:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait. No work needed here.
- **Priority 2** (every other student body president or student regent): zero gaps. All 73
  `leaders` records across 61 years carry a portrait.
- **Priority 4** (years with no photograph at all): zero. Every year carries at least a leader
  portrait or a year-level photograph in `data/photos.json`.

`python3 scripts/portrait_gap.py --list` still reports 189 officer slots with no portrait, held by
159 distinct people, 157 of them with no portrait anywhere in the file — numerically unchanged
from every pass this week.

## Network state, retested fresh rather than assumed

- `cgi/viewcontent.cgi`: HTTP 403, the Cloudflare "Just a moment..." challenge page (5,984 bytes).
  Still closed.
- `web.archive.org`: every request failed at the proxy layer (`ws_closed_mid_exchange`, tunnel
  closed after ~10s). Tried the plain Wayback path, the `if_` raw-content bypass, and
  `timetravel.mementoweb.org` as a third-party alternative; all three failed identically. Still
  closed, and the proxy's own status endpoint confirms this is a relay-level failure specific to
  that host, not a credential or access-policy gate.
- `archive.org` (the item/download host, distinct from the Wayback Machine): open. Pulled a page
  image from `talisman1975west` directly to confirm (HTTP 200, valid JPEG, 629KB).
- `wkuherald.com`: open, confirmed again but not re-swept — the second pass on 17 October already
  checked every name in the 2001-02-through-2025-26 slice of the gap against the Herald's search
  API and closed it as a source for this gap.
- `digitalcommons.wku.edu` item landing pages (not the PDF route): open, HTTP 200, no usable images
  (only site logos).

## What this run checked that hadn't been nailed down before: whether archive.org holds any
## Talisman "west" volume outside the documented 1971-1981/1986/1987 run

A loosely-scoped archive.org search for `identifier:talisman*` returned a 200-row page dominated by
unrelated items (a board game, several unrelated books, a trademark-dispute blog network that
happens to use "Talisman" in dozens of identifiers) and, by coincidence of relevance ranking, looked
at first glance like it was missing 1974, 1976 and 1978 from the WKU run. Re-ran the query properly
scoped to the actual yearbook (`title:(talisman)` crossed with the WKU creator, then confirmed with
the unpaginated `/services/search/v1/scrape` endpoint) and got a clean, authoritative list of all 19
"west" items archive.org holds: 1943, 1946, 1947, 1963, 1964, 1965, then an unbroken run from 1971
through 1981, then 1986 and 1987. No gaps inside 1971-1981, and nothing between 1988 and the present.
This matches `SGA-60-AGENT-INFO.md`'s documented range exactly — it is now confirmed by an
authoritative enumeration rather than carried forward as a claim, and the false lead (that 1974,
1976 and 1978 might be newly available) is closed before it could waste a future run's time chasing
volumes that were never actually missing.

## A web-search spot check on six names from the 2000s-2010s slice of the gap

With the `WebSearch` tool available this run (not every photograph run has had it), tried six names
from the officer-portrait gap that hold titles senior enough to plausibly draw press or SGA-site
coverage, searching each restricted to `wkuherald.com`, `wku.edu` and `digitalcommons.wku.edu`:
Nathan Cherry (Speaker of the Senate, 2016-17), Ryan Richardson (Speaker of the Senate, 2017-18),
Liz Goddard (Director of Public Relations, 2007-08), David Spalding (Chief Justice, 2011-12), Sawyer
Coffey (Director/Public Relations, 2014-15/2015-16) and Morgan Wysong (Public Relations Committee
Chair, 2016-17).

None produced a photograph. The hits that came back were legislation-archive sponsor listings,
Senate meeting minutes naming the person in text, and (for Morgan Wysong) her own byline as a Herald
staff reporter years after her SGA role — never an image with her own name in a caption. This is a
narrow, six-name sample, not a sweep, and it does not reopen or extend the wkuherald.com conclusion
the 17 October second pass already reached; it is consistent with it.

## No portrait found or added this run

No file in `data/photos.json` or `data/photos/` changed. The 189-slot gap is numerically unchanged.
This run's contribution is confirming the archive.org Talisman volume list is exactly what the
documentation says (closing a false lead before it cost a future run time) and reconfirming, rather
than assuming, that both blocked routes (`viewcontent.cgi`, `web.archive.org`) are still closed this
session.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: clean. 61 years, 60 presidents, no
missing leader portrait, no year without a photograph. Merged `origin/main` into `research-photos`
first (clean merge, `.research/NIGHT-REPORT.md` only, no conflicts).
