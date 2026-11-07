# Photograph run, 27 October (scheduled): baseline reconfirmed, both standing blocks still closed, a per-name wkuherald.com sweep and a live wku.edu CMS check both tried and closed

## Priorities 1, 2 and 4, reconfirmed directly against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 60 people have been president,
  archive checks out against its own rules. No missing leader portrait.
- **Priority 4**: unchanged; every year still carries at least one photograph. The two standing
  year-photo near-misses (1994-95, 2000-01) are unchanged; neither was reopened this pass, since
  both are documented as fully read at every reachable issue with no usable frame (see the 7-8
  October entries above).
- **Priority 3** (officer/Senate gap): `scripts/portrait_gap.py --any-year` reports the same 948
  officer slots, 188 with no portrait for that person in that year, 158 people, 156 with no
  portrait anywhere. Unchanged from every pass since 20 October.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403, Cloudflare interactive challenge, tested
  directly with full browser navigation headers. Still closed.
- `web.archive.org` — connection reset (`curl: (35) Recv failure: Connection reset by peer`). Still
  closed.
- `archive.org` (not `web.archive.org`) — HTTP 200, same 19 `talisman*west` identifiers as every
  prior check. No new volume; the five Talisman-reachable gap slots (1974-75 Pulman, 1978-79 Young/
  Wilson/Wicks, 1980-81 Chesnut) were already checked and closed on the 26 October fourth pass and
  were not re-tried today.
- `wkuherald.com` — open, both the WP-JSON search and the plain site.

## A per-name wkuherald.com sweep, beyond the tag-based search prior passes used

Earlier sweeps (22 September, and the general SGA-tag checks since) searched by `SGA`-tagged posts.
This pass instead queried the WP-JSON search endpoint by each of 20 names still open in the
2016-17 through 2021-22 slice of the gap list (Nathan Cherry, Cody Cox, Amarah Reed, Ian Hamilton,
Morgan Wysong, Devan Richardson, Ryan Richardson, Josh Zaczek, Cassidy Townsend, Brenna Mathews,
Turner Reynolds, Justin Goins, Elizabeth DeLozier, Garrett Baum, Mallory Hardesty, Livi Ray, Erika
Puhakka, Jason Herlick, Alexis Mayne, Zachary Skillman), with `_embed=1` to pull each hit's
featured-media caption, and separately re-scanned each hit's raw `content.rendered` for
`<figcaption>` text or `<img alt="">` text naming the person (catching inline, non-featured images
a plain caption check misses). Zero of the roughly 90 posts returned across these 20 names carried
a caption or alt text naming the person next to a photograph. These committee-chair and
Senate-officer-level roles are evidently covered in wkuherald's SGA reporting by name in running
text, not by captioned photograph - consistent with every sweep this gap has had since September.
No lead; nothing added.

## wku.edu's own SGA pages: checked live, and found to be a dead end for history, not a new route

The live `wku.edu/sga` site still links year-specific paths from past administrations (for example
`/sga/2018-2019-judicial/judicial-council.php`, `/sga/2018-2019-executive/meetingrequest.php`).
These resolve (HTTP 200), which looked promising - CLAUDE.md's priority order never named the live
`wku.edu/sga` site directly, only its Wayback-archived captures. But reading the actual response
shows why that distinction doesn't matter here: the 2018-2019 judicial council page's body carries
no 2018-2019 content at all - no names, no roster - only the site's standard navigation chrome,
plus a "headshots" widget showing `sophiestirling.jpg` and `hannahhash.jpg`, two names that belong
to the *current* (2026-27) executive branch, not 2018-19. The same pattern held on
`/sga/2025_2026_executive/...` paths implied by the live executive page's own image URLs (confirmed
those specific files exist and are real headshots, but for the 2026-27 slate, one year past
anything this archive's gap list needs). The CMS has evidently retired the old per-year page bodies
and now serves the current roster's data under the stale URL. So a "200 OK" from one of these
legacy paths is not evidence of historical content behind it, and this is not a route a future pass
should spend time on for the 1996-2024 officer gap - the real historical rosters for those years, where
they exist online at all, are only in Wayback's captures of these same pages, which is the route
already known to be closed by the `web.archive.org` block above.

## Conclusion

No new portrait landed this pass. Both standing blocks are confirmed still closed; the two routes
that are open (`wkuherald.com`, plain `archive.org`) were both pushed on genuinely new angles (per-
name caption/alt-text search; the live wku.edu CMS check) rather than re-running an old query, and
both came back empty or closed-as-dead-end. `python3 scripts/build.py` and `python3
scripts/check_data.py` both exit clean. Nothing in `data/photos.json` or `data/photos/` changed
this pass; this run's only output is this note. Landed on `research-photos`.
