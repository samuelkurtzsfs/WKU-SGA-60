# Photograph run, 17 September (afternoon/evening) — the back-of-book index checked directly, four genuine negatives

## Starting state, re-confirmed

Checked the standing priorities before touching anything: all four named presidents (Nick Todd,
Katie Dawson, Jeanne Johnson, Reagan Gilley) and every other `leaders` entry with
`role: "president"` or `role: "regent"` already carry a portrait. Priorities 1 and 2 remain fully
satisfied. Read the two same-day reports already in `.research/`
(`photo-run-2026-09-17-wayback-pdfs.md`, `photo-run-2026-09-17-officer-search.md`) before starting,
per the standing instruction not to re-discover routes already open today.

Cross-referenced `data/years.json` against `data/photos.json` fresh (leaders plus
`organization.executive` plus `organization.senate.officers`) for 1988-89 through 1993-94, the
stretch this morning's Wayback-PDF route newly opened. Five names, across three years, had no
portrait: **Mickie Hennig** (Secretary, 1988-89), **Chris Gaddis** (Vice-Chair, Judicial Council,
1988-89), **David Smith** (Chair, Academic Affairs, 1992-93), **Trent Lyda** (City Council
Representative, 1992-93) and **Derrek Duncan** (Chairperson, Legislative Research Committee,
1993-94). 1989-90, 1990-91 and 1991-92 are already fully covered for this class of name.

## Method: the alphabetical index at the back of the yearbook, not just free-text search

This morning's two reports both searched Talisman PDF text for a name directly and, when that came
back empty, treated the search as exhausted or moved to visually scanning group photographs. Every
Talisman from this era (1989, 1992, 1993 — all three downloaded and checked this run, via the same
Wayback CDX route documented in `photo-run-2026-09-17-wayback-pdfs.md`) carries its own
several-page alphabetical name index near the back, giving a page number for every student the
book mentions anywhere, portrait or not. A direct text search for a full name can miss this index
even when the person is in it, because 1980s-90s OCR is degraded enough that a two-word name often
doesn't survive as one contiguous, correctly-spelled string — but the surname usually does, and the
index is dense enough that reading the whole alphabetical run around where a name should sit is a
stronger check than a keyword search. This run located and read that index by eye for all three
volumes, immediately around where each target surname belongs alphabetically, rather than trusting
`in`-string search alone.

## Four genuine negatives

- **Trent Lyda** (1992-93): not indexed in either the **1992 Talisman** (p. 177's index runs
  `Lunsford, Micah D. ... 177` directly to `Lyle, Keith E. 174` with no `Lyda` between them) or the
  **1993 Talisman** (p. 278's index runs `Luckey, Beth ... / Lucken, Amy ... / Lupy, Susan ...`
  directly to `Lyell, Jenny 178` / `Lyle, Keith 160`, again with no `Lyda` between). Both volumes
  cover his years as an active ASG figure — he wrote three signed Herald op-eds in this window, one
  of them about ASG (Herald 65:51, 5 Apr 1990, "Rude Awakening – Facilities Services",
  `dlsc_ua_records/7631`; Herald 67:26, 26 Nov 1991, "Sorority Dorms are Discriminatory – Meredith
  Hall", `dlsc_ua_records/7798`; and the ASG one, Herald 67:40, 20 Feb 1992, "Associated Student
  Government: Don't Complain, Get Involved", `dlsc_ua_records/8015` — found via
  `data/herald-index-full.json`, not re-crawled) — but neither yearbook
  pictures or indexes him. The Herald PDF for the 20 Feb 1992 issue (`dlsc_ua_records/8015`,
  article 9020) was checked for a Wayback capture as a possible route to an op-ed column
  photograph; none exists (`web.archive.org`'s CDX has no capture of that specific article, unlike
  the Talisman PDFs, which appear to have been crawled far more heavily).
- **David Smith** (1992-93, Chair of Academic Affairs): not indexed in the **1993 Talisman** at
  all — its index's Smith run goes `Smith, Deborah / Smith, Denise / Smith, Derrick / Smith,
  Donald / Smith, Frances / Smith, Gary` with no `David` in it. The 1993 Talisman does carry a
  **"Student Government Association" group photograph** (p. 204, caption transcribed in full)
  naming a "**Donald Smith**" in the third row — a different, already-sourced person: `Donald
  Smith` already has his own 1992-93 portrait on file from Herald 69:7 (16 Sept 1993). The two
  names are one letter apart and the site's own `CLAUDE.md` warns against exactly this kind of
  near-miss; confirmed they are not the same index entry and left both alone rather than
  reattributing the existing Donald Smith portrait to David Smith or cropping his face from the
  group photo under the wrong name.
- **Mickie Hennig** (1988-89, Secretary): not indexed anywhere in the **1989 Talisman**'s H
  section — the run reads `Helton, Dale 241 / Heltsley, Juliana 234 / Hendon, Stephanie 232 /
  Hendricks, Adna 190 / Hensley, Concheta Ann 145 / Hensley, Fred 68 / Herbert, Cynthia 110, 214`,
  so the slot between `Hendricks` and `Hensley` where `Hennig` belongs is empty, and the volume
  carries no `Hennig` or close variant anywhere. Consistent with the 16 September finding that she
  is absent from the year's own ASG group photograph.
- **Chris Gaddis** (1988-89, Vice-Chair, Judicial Council): not indexed under that first name. The
  1989 Talisman's G section does carry **"Gaddis, Sherry" (p. 195)** — a different first name, and
  not used for the same reason as the Donald/David Smith case above. No `Chris Gaddis` or `Gaddis,
  C.` entry exists in the index.

## Left untried

- **Derrek Duncan** (1993-94): the 1994 Talisman was already established by the 16 September and
  17 September (Night-Report-reviewed) passes to carry no SGA/ASG content anywhere in its
  Organizations section — a volume-wide negative, not a per-name one. This run did not re-open that
  question and did not find another route to him; he remains uncovered.
- The Herald-PDF-via-Wayback route (tried once, for Lyda's Feb 1992 column) is evidently much
  thinner than the Talisman coverage — worth knowing before spending time trying it on other
  individual Herald issues, but not disproven as a route in general; it may simply be that the
  Talisman PDFs were crawled specifically (heavily linked/searched externally) while ordinary
  Herald issues mostly were not.

## Nothing added

`data/photos.json` and `data/photos/` are unchanged this run. No commit needed for those files.
`build.py` and `check_data.py` were not re-run since nothing in `data/` changed.

## Editor's check, 17 September

Every conclusion above was re-tested independently before merge, and all four negatives hold. The
1989 and 1993 Talisman PDFs were pulled again from the Wayback captures and read directly, by
rendering the index pages rather than trusting their text layer, which on the 1989 volume is bad
enough to turn `Gaddis` into `Co.ddi`.

Confirmed on the page image: the 1993 Smith run goes `Deborah / Denise / Derrick / Donald /
Frances / Gary` with no `David`; the 1993 index runs `Luckey / Lucken / Lupy / Lyell` with no
`Lyda`; `Gaddis, Sherry 195` is in the 1989 index verbatim, filed out of alphabetical order between
`Ged, Denise` and `Gensheimer, Joseph`, which is why this volume needed reading by eye; and no
`Hennig` or `Chris Gaddis` appears in either volume. Against `data/years.json` and
`data/photos.json`: all five officers named here do lack portraits, their offices and years are
recorded exactly as given, every president and regent in the archive carries a portrait, and
Donald Smith's existing portrait has not been reattributed.

Four supporting citations were wrong and have been corrected in place: two of Trent Lyda's three
Herald op-eds carried the wrong volume and issue, only one of the three is about ASG rather than
all three, and three of the four index neighbours quoted in the Hennig bullet were misread
(`Hendon, Sondra` is Stephanie, `Hendley, Fred` is Hensley, `Hart, Cynthia` is Herbert). None of
these reached `data/`. The lesson for the next pass is the one this log already half-states: on
these volumes, transcribe index neighbours from the rendered page, never from the text layer.
