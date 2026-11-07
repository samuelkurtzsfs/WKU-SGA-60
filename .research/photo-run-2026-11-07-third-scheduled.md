# Photograph run, 7 November third scheduled pass: same three blocks, one new negative lead, no portrait landed

## Priorities 1, 2 and 4, reconfirmed directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60 people
  have been president. Zero presidents or student regents without a portrait across all 61 years.
- **Priority 4**: every one of the 61 academic years still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports 948
  officer slots, 188 without a portrait for that person in that year, held by 158 people, 156 with
  no portrait anywhere in the file — unchanged from the two passes earlier today.

## Network state retested cold

- `digitalcommons.wku.edu` item pages: **HTTP 200**, real content, no challenge
  (`/dlsc_ua_records/9505`, confirmed with `-L` and a current desktop Chrome UA).
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (the actual PDF/image download): **still HTTP 403**,
  a Cloudflare "Just a moment..." challenge page, `cf-mitigated: challenge` header, same navigation
  headers that work on the item page. Tested against `article=9678&context=dlsc_ua_records`, the
  same id the second scheduled pass used a few hours ago. No change.
- `archive.org` (`talisman1987west_djvu.txt`): reachable with `-L` (redirects once), 939KB of text,
  consistent with every prior pass.
- `web.archive.org`: connection reset mid-exchange, unchanged.
- `wkuherald.com` WP-JSON: inconsistent within this single pass — a raw `curl` with a spoofed
  desktop UA was refused by this session's own tooling (not a site block), and a direct fetch
  without special headers returned 403. The second scheduled pass earlier today recorded this same
  endpoint open. Treat it as flaky rather than newly closed; the next pass should retest with
  whatever fetch path the tooling actually allows.

## New angle tried this pass: archive.org's own Talisman copy for the two 1986-87 gap names

1986-87 is one of the few gap years that falls inside archive.org's fixed 19-volume Talisman
holding (1971-1981, 1986-87), so unlike most of the 156-person gap it does not depend on the
blocked `viewcontent.cgi` route at all. Tried it directly against the two 1986-87 names still open:
Chris Millay (Parliamentarian) and Dwight Austin (Sergeant-at-Arms).

- Searched the full `talisman1987west_djvu.txt` for both surnames: every hit is an unrelated
  namesake (an "Austin Peay" opponent in the sports section, students named Millay/Austin in the
  portrait index with no SGA context) or the alphabetical class-portrait index, which gives a page
  number but no caption connecting the person to student government.
- Read the "Governing bodies" / ASG section of the same volume in full (the only passage mentioning
  ASG by name): it profiles ASG President Tim Todd and names a treasurer, nothing else — no
  Parliamentarian or Sergeant-at-Arms is named anywhere in that article.
- **Conclusion: ruled out for this volume.** The 1987 Talisman's ASG coverage is a short feature
  article, not an officer roster with a group photo, so it was never going to carry these two names
  regardless of network access. This closes the one case in the current gap list where archive.org
  access (rather than the blocked digitalcommons PDF route) was the limiting factor — there is no
  further point sending another pass back to this specific volume for these two names.

## Also checked: a WKU Archives finding aid and a Herald lead photo, both dead ends

- `digitalcommons.wku.edu/dlsc_ua_fin_aid/620` describes the **UA1C4/10 "Student Government
  Association Photos"** finding aid — a real WKU Archives photograph collection, the kind CLAUDE.md
  points at as the second-best photo source. The finding-aid page itself names no individuals and
  gives no box/folder list; it is a 2019 abstract only, with a 174KB PDF linked that was not opened
  this pass. **Worth a future pass**, but only if the PDF or a fuller finding-aid page turns out to
  itemize folders by year or name — the abstract page alone gives nothing to go on.
- A Herald article on newly elected 2021-22 officers (`wkuherald.com/61104`, confirmed independently
  as the lead for Tribhuwan Singh, Director of Enrollment and Student Experience) carries one lead
  image with no caption identifying anyone pictured — fails the archive's "confirm from caption"
  rule outright, so it was not used.

## Conclusion

Nothing added to `data/photos.json` or `data/photos/`. The standing picture is unchanged from the
last two passes today: digitalcommons' catalogue pages are open, its PDF/image download is not,
`web.archive.org` resets, and archive.org's own Talisman holding is fixed at 19 volumes. The one
new result this pass adds is negative but specific: Millay and Austin (1986-87) are ruled out
against the one archive.org volume that was actually reachable for their year, because the source
itself doesn't name them, not because of a network block. The UA1C4/10 WKU Archives finding aid is
a loose thread for whoever next has time to open its PDF.
