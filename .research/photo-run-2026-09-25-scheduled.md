# Photograph run, 25 September (scheduled): bypass reopened but every capture serving a genuine lead was truncated

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md`, `SGA-60-AGENT-INFO.md` (sections 4 and 6),
and `data/photo-finds/_brief.md` before touching anything. `research-photos` had no local divergent
work; fast-forwarded onto `origin/main` cleanly (merge commit, no conflicts). No pull request was
open on this branch at the start of the run (the prior rolling PR had been merged).

Re-checked the four originally-named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan
Gilley) before spending time on anything else: all four already carry a portrait. A scripted
cross-check of every `role: "president"` / `role: "regent"` leader against `data/photos.json`
found zero gaps — priorities 1 and 2 are still fully satisfied. Every one of the 61 years already
carries at least one photograph once leader portraits are counted; the narrower Priority 4 queue
(years with no *year-scene* photograph specifically) stands at five: 1994-95, 1995-96, 2000-01,
2005-06, 2008-09, unchanged from the 24 September reports.

## Priority 3: reproduced the existing dead ends independently, then a working bypass window

Built a fresh list of executive/Senate officers named in `organization.executive` /
`organization.senate.officers` with no entry in `data/photos.json`, filtered to the core cabinet
and Senate-leadership titles (President/VP variants, Secretary, Treasurer, Speaker) rather than
committee chairs or individual senators. Before searching, checked this list against
`data/photo-finds/_archive-gaps.json`: the 19 September entry already records all fifteen of the
pre-2016 names on it (Bass, Young, Wicks, Wilson, Chesnut, Kelly S. Smith, John Holland x2, Connie
Hoffmann, Mickie Hennig, Steve Roadcap, Jamie Fite, Matt Holland, Nathan Cherry, Ryan Richardson)
as dead ends independently reproduced by more than one prior run and more than one route.

Reproduced four of these myself before reading that entry, by coincidence using different methods
each time, and got the identical negative result each time:
- **David Bass** (Activities VP, 1977-78): `archive.org`'s `fulltext/inside.php` search-inside API
  on `talisman1978west` finds the exact caption — "activities vice president David Bass, secretary
  Sharon May and vice president Cathy Murphy" — on printed page 34. Fetched the full-resolution
  page image via the IIIF endpoint (`https://iiif.archive.org/iiif/talisman1978west$38/full/full/0/default.jpg`)
  and read it directly: the photo has three clearly visible faces for four named subjects, with no
  left-to-right key. Cannot support an individual identification. Confirms the 19 September finding
  exactly.
- **David Young** (Administrative VP, 1978-79) and **Alice Wicks** (Secretary, 1978-79): both
  findable in `talisman1979west`'s OCR text (Young quoted in a news paragraph about the new
  constitution; Wicks only in the unpictured name index with no page number), neither tied to a
  photograph.
- **Mark Chesnut** (Treasurer, 1980-81): no photo-adjacent mention found in `talisman1981west`'s
  full text; the only `Chesnut` hits are unrelated senior portraits and index entries.
- **Nathan Cherry** (Speaker of the Senate, 2016-17): the live 2016-17 `wku.edu/sga/legislative/`
  page, read via a `web.archive.org` snapshot (`20170323061915`), is a name-and-title text roster
  with no photographs anywhere on the page — confirms the "wku.edu/sga has never published a
  picture of a senator" finding from the 19 September entry.

## The Wayback bypass into TopSCHOLAR: open today, but throttled to failure on anything but a small file

Confirmed the 24 September report's route (`https://web.archive.org/web/<ts>if_/https://digitalcommons.wku.edu/cgi/viewcontent.cgi?article=<N>&context=dlsc_ua_records`)
is not "shut, full stop" today the way it was that evening — but it is far from reliable. Of
roughly twenty attempts across six different articles, outcomes were:
- **2 clean, complete downloads** (13.4 MB and 19.4 MB PDFs, articles 7724, both against
  `dlsc_ua_records/6721`'s two possible article numbers).
- **~3 captures that came back as exactly 1,048,576 bytes** (articles 7666, 7667, 6164) — a
  suspiciously round number that recurred across different articles and different attempts,
  and which produced either an unopenable PDF (`code=7: Invalid number of pages`) or one that
  opens but errors on most pages (`non-page object in page tree`, `cannot find page N in page
  tree`) and renders the handful of pages it does open as blank. This does not look like the
  genuinely-truncated-in-the-archive case the 24 September second run documented (that one still
  opened cleanly and reported an honest byte count in the CDX record); it looks like the
  connection itself giving up after transferring exactly one megabyte, consistent with the
  agent-proxy's own failure log showing `ws_closed_mid_exchange` at "6s; 517 B sent, 39 B
  received" on the outright failures. The CDX API (`web.archive.org/cdx/search/cdx`), which the 24
  September report recommends checking for a larger alternate capture before accepting a small one,
  itself failed on every one of roughly ten attempts today with the same `ws_closed_mid_exchange`
  signature — so a genuinely larger snapshot could not be located or ruled out for any of these
  three.
- **The rest: plain connection resets** before any bytes arrived, same signature as above.

Archive.org's own status page (`archive.org` root, unrelated to any of these fetches) briefly
returned a "Temporarily Offline" notice mid-run; ordinary `archive.org` endpoints (metadata,
`fulltext/inside.php`, IIIF page images) were unaffected before and after and stayed reachable
throughout at normal speed, unpaced. Worth recording that this is a different, wider outage
surface than the `web.archive.org` tunnel problem, even though both hosts are operated by the same
organisation.

**What the two clean downloads actually contained:** `dlsc_ua_records/6721`, Herald 84:22, 17 Feb
2009 (article 7724). This issue is the one already in `data/photo-finds/_topscholar-wanted.json`
for Jacob Turner and Lisa M. Kappler. Read both stories directly:
- "SGA chief justice resigns" (p. 3): text only, no photograph anywhere on the page. Closes Lisa M.
  Kappler as a lead from this specific issue; she remains without a portrait.
- "Puzzle expert looks to future outside Ky." (p. 8): does carry a captioned, unambiguous photograph
  of "Hazard sophomore Jacob Turner" — but Turner is not an SGA officer in this archive (he is the
  subject of an unrelated feature that happens to share the issue with Kappler's story) and the
  queue's own note already records he carries a portrait from elsewhere. No new coverage from
  either story.

The three 1 MB-truncated captures were the ones that would have mattered: article 7666/7667
(`dlsc_ua_records/6645`/`6644`, the spring 2007 Senate-election mugshot-grid issues, wanted for
Cacy A. Schooler and Jacob Miers among others) and article 6164 (`dlsc_ua_records/5160`, the 2014
Talisman "Stories to Tell" feature naming Mallory Treece). None could be read. These three stay
open in the queue, not closed — the capture exists and is reachable, it is just not yet landed
whole.

## What this means for the queue

No change to `data/photos.json`, `data/photos/` or `data/years.json`. `data/photo-finds/_topscholar-wanted.json`
is unchanged: the entries this run touched (6721, 6645/6644, 5160) stay open rather than closing,
since the failures were transport failures on a route proven to work at least twice today, not
proof the images don't exist. Appended today's findings to `_archive-gaps.json` so a same-day or
next-day run does not have to rediscover the truncation pattern from scratch, and can go straight
to retrying 7666/7667/6164 without re-running the four already-closed 1978-81 names above.

**Recommendation for the next run:** retry articles 7666, 7667 and 6164 through the same bypass
URL a handful of times each, spaced a few seconds apart, before doing any fresh searching — the
route is open today and two different articles did eventually come through whole. Do not spend
time on the 1978-81 Talisman names (Bass, Young, Wicks, Chesnut) or on Nathan Cherry; those are
independently closed by three separate runs now, including this one.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean before and after this
run's research (no data changed, so this mainly confirms no regression). `build.py` printed its
routine "withdrew 1 photograph(s) the archive no longer holds or has barred" housekeeping line,
unrelated to anything this run touched.
