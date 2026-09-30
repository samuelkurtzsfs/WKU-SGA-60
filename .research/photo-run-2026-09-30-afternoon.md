# 30 September 2026 (photograph routine, second run) — wkuherald.com tried against the recent-year officer gap

## What was checked before doing anything

Re-derived the same way the morning run did: all 73 leader records carry a portrait, all 61 years
carry at least one photograph, and 1994-95, 1995-96, 2000-01 and 2008-09 remain the only years with
a leader portrait but no year-scene photograph. 217 executive/Senate officer records across the
whole archive still lack a portrait. Cross-referencing those against the archive.org Talisman window
(1971-81, 1986-87) turned up exactly the same eight names the morning run already tried and declined
(Pulman, Bass, Young, Wicks, Wilson, Chesnut, Millay, Austin) — nothing new fell inside that window,
so there was no point repeating it.

The other 209 missing officer records cluster overwhelmingly in 1996-2023, concentrated worst in
2016-17 (15), 2017-18 (14), 2021-22 (14) and 2022-23 (16). That span sits outside the archive.org
Talisman mirror and behind the two routes the morning run confirmed blocked again this session
(`digitalcommons.wku.edu/cgi/viewcontent.cgi` still returns Cloudflare's `cf-mitigated: challenge`
403; `web.archive.org` still resets at the TLS handshake, both retested directly before starting).
`wkuherald.com` was untried this run, is open (plain `curl`, 200), and is the one source in CLAUDE.md's
list built for exactly this span, so this run spent its time there instead of re-knocking on the two
closed doors.

## What wkuherald.com actually gives up for this gap

Tried the WordPress search API (`/wp-json/wp/v2/posts?search=...`) against five of the officers with
the most senior titles in the biggest gap years, on the theory that a Speaker or Chief Justice is the
likeliest rank to get individual coverage: Nathan Cherry (Speaker of the Senate, 2016-17), Cody Cox
(Chief Justice, 2016-17), Ryan Richardson (Speaker of the Senate, 2017-18), Turner Reynolds (Associate
Chief Justice, 2021-22), Justin Goins (Chief Justice, 2022-23).

Every search returned real, on-topic SGA articles — the Herald does cover these people by name — but
none of the three articles read in full carried an individual, captioned photograph:

- **"SGA judicial council 'fully functional' following four nominations"** (25 Sept 2019) names
  Reynolds among four judicial council nominees and quotes her directly. Its one featured image
  (media id 19383) carries no caption and no alt text — a generic file image, not a portrait of
  anyone named in the piece. Not usable.
- **"SGA, University Senate appoints new members"** (21 Sept 2016) quotes Speaker Nathan Cherry
  directly but has no featured image at all (`featured_media: 0`) — text-only coverage.
- **"SGA announces election results"** (19 Apr 2023) is a results roundup naming a dozen-plus
  senators-elect in running prose, including none of this year's still-missing names by coincidence,
  and carries one featured image of the meeting room, not a per-person photograph.

This is consistent with what the pattern looks like across the outlet generally at this remove: Herald
election and appointment stories from the 2010s-2020s are prose roundups naming many people in one
article, and the accompanying image (when there is one) is a generic meeting-room or building shot
rather than a portrait grid with individual captions — a different shape from the Talisman's officer-
portrait pages that make identification possible. Nothing found this run clears the identification
bar CLAUDE.md sets, so nothing was added.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both run clean against the unmodified
tree (61 years, every leader portrait present, every year with at least one photograph). No file in
`data/photos.json` or `data/photos/` changed this run; the only addition is this report.

## For the next run

The 209 missing officer records outside the archive.org Talisman window are concentrated in
2016-23, and a plain per-person Herald search is not the way in — try the Talisman itself for those
years instead. `digitalcommons.wku.edu/talisman/` (where the physical yearbook PDFs for 2010s-2020s
volumes are actually hosted) is behind the same Cloudflare wall as `viewcontent.cgi` and was not
reachable this session either, so this queue stays blocked on the same access problem the morning
run already flagged, not on a new one. wku.edu/news was also tried this run: its search parameter
(`/news/?s=...`) 301-redirects to `/news/articles/?s=...`, which returns 200 but ignores the query
entirely — a request for `SGA president` came back with unrelated recent press releases (a Mesonet
ribbon-cutting, parking updates), not search results. Name-by-name searching does not work against
this endpoint as it stands; reaching individual coverage there would mean browsing the site's own
news archive or an SGA-tagged category by date instead of its search box, which this run did not
attempt.
