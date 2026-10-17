# Photograph run, 17 October (scheduled): the recent-decade Talisman volumes TopSCHOLAR actually holds, mapped for the first time

## Priorities 1, 2 and 4: reconfirmed before searching anything

Checked by script against the current `data/years.json` and `data/photos.json` rather than taken
on faith:

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a portrait. Unchanged for weeks.
- **Priority 2** (every other president or student regent): zero gaps. All 60 presidents and every
  student regent carry a leader-level portrait.
- **Priority 4** (years with no photograph at all): zero. Every one of the 61 years has at least
  one photograph in `data/photos.json`.

`python3 scripts/portrait_gap.py --list` reports the same count every recent pass has reported:
948 officer slots, 189 with no portrait for that person in that year, held by 159 distinct people,
157 of whom have no portrait anywhere in the file. No change from the fifth pass of 16 October.

## Network state, retested fresh

- `cgi/viewcontent.cgi`: HTTP 403, the Cloudflare "Just a moment..." challenge page, 5,984 bytes,
  on every article id tried — including brand-new ones this run first discovered (see below). That
  rules out a theory worth ruling out: the block is on the host/session, not cached per already-known
  resource. Still closed.
- `web.archive.org`: `curl: (35) Recv failure: Connection reset by peer` at the TLS layer, same as
  most passes this week. Still closed this session.
- `archive.org` (not Wayback): open, and re-queried its full catalog
  (`advancedsearch.php?q=identifier:talisman*west`) rather than trusting the standing list. Still
  exactly 19 identifiers — 1943, 1946, 1947, 1963-1965, 1971-1981, 1986, 1987 — nothing added in the
  1988-2002 or 2003+ range since this file's last count. archive.org remains a dead end for every
  Talisman after 1987.
- `wkuherald.com`: open.

## What's actually new this run: TopSCHOLAR holds digitized Talismans from 2012 all the way to 2025, not just the single 2012 volume this file had on record

Every prior note stopped at "the next item cataloged after the 2003 Talisman is Vol. 83, whose
description opens '2012 Talisman' — nothing between 2003 and 2012 is digitized, and nothing after
2012 was checked." That last clause was never true after this run looked: the yearbook collection
landing page (`digitalcommons.wku.edu/dlsc_ua_yearbooks/`) lists a continuous run of digitized
*Talisman* volumes from 2012 through 2025, each with its own `dlsc_ua_records` item and its own
`cgi/viewcontent.cgi` article id. Whether these were added to TopSCHOLAR since this project's last
look or simply never walked past 2012, the standing notes do not say — worth being honest that this
could be either. Either way, it directly bears on four of the largest slots in the 189-name gap:
2014-15 (10 missing), 2016-17 (12 missing), 2021-22 (9 missing) and 2022-23 (9 missing) all now have
a specific, identified Talisman volume to open, where before this run the working assumption was
that none existed.

Confirmed `cgi/viewcontent.cgi` is still blocked on every one of these new ids (tested 6164 and
9666 directly; both returned the identical 5,984-byte challenge page), so **nothing in this table
was opened or read this run** — this is a target list for the next pass that catches the route
open, not a set of findings. Record page, article id and file size, read from each item's own
download link (not guessed):

| Academic-year label as published | digitalcommons record | viewcontent.cgi article id | PDF size |
|---|---|---|---|
| 2013 Talisman: Form | `dlsc_ua_records/8696` | 9683 | 897.6 MB |
| 2014 Talisman: Reckoning, Part I | `dlsc_ua_records/5160` | 6164 | 341.2 MB |
| 2014 Talisman: Reckoning, Part II | `dlsc_ua_records/5162` | 6167 | 495.2 MB |
| 2015 Talisman: Resurgence | `dlsc_ua_records/8679` | 9665 | 558.5 MB |
| 2016 Talisman: Identity | `dlsc_ua_records/8678` | 9666 | 94.4 MB |
| 2016 Talisman: Life More Life | `dlsc_ua_records/8677` | 9667 | 720.6 MB |
| 2017 Talisman: Power | `dlsc_ua_records/8686` | 9669 | 149.8 MB |
| 2017 Talisman: Well Being | `dlsc_ua_records/8685` | 9670 | 93.0 MB |
| 2018 Talisman: Grit | `dlsc_ua_records/8684` | 9671 | 23.2 MB |
| 2019 Talisman: Balance | `dlsc_ua_records/8683` | 9672 | 17.7 MB |
| 2021 Talisman | `dlsc_ua_records/8776` | 9764 | 129.6 MB |
| 2022 Talisman: Forge | `dlsc_ua_records/9256` | 10255 | 140.5 MB |
| 2022 Talisman: Illuminate | `dlsc_ua_records/8898` | 9883 | 87.1 MB |

Not fetched this run (lower priority by officer-gap size, or already covered): 2018 Movement
(`8690`), 2019 Paradise (`8682`), 2020 Zeitgeist (`8681`), 2023 Dimension/Surreal Issue No. 14
(`9740`/`9836`), 2024 Legacy/Pulse (`9809`/`9821`). The collection page also carries a 2025 volume
(Connection), outside this project's 1966-2026 window only by a year and worth a look once the
recent gap is closed.

**One genuine unknown, flagged rather than guessed at:** which academic year each volume actually
covers. A yearbook titled "2016" could document the 2015-16 year, the 2016-17 year, or (per some
of the split titles) a single semester — the 1975 convention this file documents elsewhere
(`talisman1975west` = 1974-75) does not obviously carry forward once the yearbook stops being
dated by a single fall-to-spring academic year and starts splitting into two or more themed
issues a year. Whoever opens these PDFs should check the volume's own masthead/colophon for its
coverage dates before matching a photograph to a slot in the gap, not assume from the cover year.

## A second new lead checked and ruled out: the "other" WKU Archives photo finding aid

`UA1C4/7 Student Groups & Association Photos` (`dlsc_ua_fin_aid/633`, article id 1632) had never
been checked — distinct from `UA1C4/10 Student Government Association Photos`
(`dlsc_ua_fin_aid/620`/1619), the SGA-specific finding aid this file has ruled out since September
as a six-page text inventory with no reproducible image. 633's own abstract reads "Images of
student groups and associations **not otherwise listed**" — SGA has its own aid, so by the
collection's own cataloging logic this one does not cover SGA. Also blocked behind the same closed
`cgi/viewcontent.cgi` regardless. Closed as a lead on the abstract alone; not worth reopening even
if the route comes back, since it explicitly excludes what this project needs.

## No portrait found or added this run

No file in `data/photos.json` or `data/photos/` changed. The 189-slot gap is numerically unchanged.
This run's only output is this note, a real target list for the next pass with working network
access to a Cloudflare-protected PDF, and the confirmation that archive.org's Talisman holding has
not grown.

## Checks

`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, 1964 events, clean, 60
presidents, no missing leader portrait, no year without a photograph, legislation files all
present and real PDFs. Merged `origin/main` into `research-photos` first (clean merge, no
conflict — one 2017-18 events.json fix and a night report landed on main since this branch last
synced).
