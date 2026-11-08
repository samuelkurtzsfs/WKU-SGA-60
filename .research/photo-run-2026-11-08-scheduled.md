# Photograph run, 8 November scheduled pass: both standing network blocks still closed, one new route found and closed negative, eighteen days without a new portrait

## Baseline reconfirmed directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Unchanged since August.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60 people
  have been president. Zero presidents or student regents without a portrait across all 61 years.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same shape as every pass since early November — several hundred officer slots short a portrait
  for that person in that year, around 156-159 people with no portrait anywhere in the file. PR
  #835 already records that every one of these names has had at least one individual check on
  record, all negative. This pass did not re-search names already closed; see below for why.
- **Priority 4** (year photographs): the two standing gaps, 1994-95 and 2000-01, are unchanged.
  Both depend on sources (digitalcommons Herald/Talisman PDFs) behind the same block as the
  officer gap.

## The two blocks, retested fresh rather than assumed

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — tested directly against the UA1C4/10 finding aid
  PDF (`article=1619&context=dlsc_ua_fin_aid`), full navigation headers, one request. **Still HTTP
  403**, 6,027 bytes, a Cloudflare "Just a moment..." challenge page, not a document. This is the
  same gate that has blocked every PDF on the site since at least late October. Plain item pages
  (HTML, no PDF) still answer normally.
- `web.archive.org` — tested directly (`web/2020/https://wku.edu/sga/`). **Connection reset by
  peer** mid-exchange, the same `ws_closed_mid_exchange` failure the agent proxy has logged on
  this host since October.

Both blocks are the same two named in PR #835 on 5 November and reconfirmed in every pass since.
Nothing has changed.

## New route tried this pass: wku.edu/sga's own current pages, read directly rather than through digitalcommons or the Wayback Machine

Earlier passes treated `wku.edu/sga` mainly as an archived (Wayback) source. This pass fetched the
**live** site directly, since `wku.edu` itself is reachable even when digitalcommons is not, and
checked whether its own officer pages carry headshots outside the blocked routes:

- `wku.edu/sga/executive/` carries real headshot photos with adjacent name/title text for the
  sitting executive branch — `caden.jpg` labelled "Caden Lucas | Student Body President, Student
  Regent", `jakobbarker.jpg` "Jakob Barker | Student Body Vice President", `will.jpg` "Will
  Derryberry | Chief Financial Officer", `gabigpace2.jpg` "Gabi Pace | Chief of Staff",
  `caydenbayley.jpg` "Cayden Bailey | Chief Communications Officer". All five already carry a
  portrait in `data/photos.json`; this route rediscovered people this archive already has, which
  at least confirms the method works.
  - One discrepancy worth flagging rather than acting on: the `caden.jpg` image's `alt` attribute
    reads "A headshot image of Student Body President Rush Robinson," while the visible name
    directly beneath the photo reads "Caden Lucas." Caden Lucas is independently established as
    the 60th president (`SGA-60-AGENT-INFO.md` §1), so the stale `alt` text — not the adjacent
    name label — is the one that's wrong, almost certainly a leftover attribute from a previous
    year's page edit that was never updated when the photo was swapped. Noting it here in case a
    future pass meets the same page and is tempted to read the `alt` text as an identification;
    it should not be.
  - `wku.edu/sga/judicial/` carries no headshots this cycle (judicial branch page is currently
    text-only). `wku.edu/sga/legislative/senate_committees.php` lists committee names and chairs
    as plain text, no photos.
  - The site also still links several stale `/sga/2018-2019-*` and `/sga/2025_2026_*` paths from
    its own homepage (meeting-request forms, PDFs, the current budget image) — all 403 when
    requested as a directory listing, and none of the dead ones from 2018-19 resolve to anything
    for a name in the current gap. Tried guessing a same-shape headshot folder for each
    intervening year (`/sga/2019_2020_executive/`, `2020_2021_executive/`, ... `2024_2025_executive/`)
    on the chance an old page is still live but unlinked: five 404s and one 403 (2024-25, which
    403s the same way the 2018-19 links do — a real but unlisted directory). No filenames to guess
    inside it without a page that names them, so this did not go further; guessing image filenames
    blind is not a safe identification method and nothing was added on that basis.
- `archive.org`'s own Talisman catalogue (not the Wayback subdomain) was re-queried by search
  rather than by guessing an identifier: still exactly 19 volumes (1943, 1946-47, 1963-65,
  1971-81, 1986-87). Nothing from the 1990s, 2000s or 2020s — the decades the standing gaps
  actually sit in — has ever been digitized there.

## Conclusion

No file in `data/photos.json` or `data/photos/` changed; no portrait or year photograph added.
`build.py` and `check_data.py` both pass clean. This is worth stating plainly rather than
restating the same "no new lead" line a tenth time: **the last run that actually added a
photograph was 21 October** (`bcd04c44`, the 1978 David Bass identification). Since then, 76
scheduled passes (this one included) have landed a commit each time, and all but that one have
changed nothing in `data/`. Every route this project's own documentation lists for photographs —
the digitalcommons PDF/image layer, archive.org's Talisman holdings, the Wayback Machine, and now
wku.edu's own current pages — has been retried on this stretch and found either closed
(`viewcontent.cgi`, `web.archive.org`) or exhausted (archive.org's Talisman catalogue does not
cover the gap decades; wku.edu's current officer pages only ever surface people already
photographed). PR #835's own assessment from 5 November — that further passes should prioritise
retesting the two network blocks over re-searching names already closed negative — still holds,
and this pass found no reason to revise it. Landed on `research-photos`.
