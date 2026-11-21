# Photograph run, 8 November (third scheduled pass): both standing routes closed again, a stale tracking note corrected, eleven recent gap names checked against wkuherald.com with no new portrait

## Baseline

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. No work needed.
- **Priority 2**: `python3 scripts/check_data.py` exits clean - 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports the same 156-person
  gap this file's recent passes have recorded.

## Network state this pass

Both of the two routes this file's recent entries describe as flickering were tested cold at the
start of this pass and found closed, not open:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` direct: HTTP 403 (Cloudflare), as expected.
- `web.archive.org` (both `/web/` replay and `/cdx/search/cdx`): `ws_closed_mid_exchange` on every
  attempt - the agent proxy's tunnel to egress closed before the exchange completed, the same
  standing block recorded through most of this week's passes, not the brief working window the
  second pass today found.

`archive.org` (the item/advancedsearch API, a different host from the Wayback replay layer),
`wkuherald.com` and `wku.edu` were all reachable. Confirmed on `archive.org`'s own catalogue that
no WKU "west" Talisman identifier later than `talisman1981west` exists there (searched
`identifier:talisman*`, every `*west` hit listed) - the 2014-2020 volumes genuinely are
TopSCHOLAR-only and there is no archive.org shortcut around today's closed Wayback bypass for them.

## A stale tracking note corrected

`data/photo-finds/_topscholar-wanted.json` item 14 (the 2016-2020 Talisman magazine cohort,
`dlsc_ua_records/8677` and its eight successors) still read, as of this morning, "what is untried
is the systematic sweep of all nine" - a note dated 30 September. That is wrong, and has been
wrong for weeks: `data/photo-finds/n1419-notes.json` already records that sweep as done. The 2016
"Life More Life" volume's 1,430 portrait-grid nameplates were extracted and matched against all 39
n1419 officer surnames (sixteen surname hits, all other people, no SGA group photograph in the
Clubs & Organizations section), and the other eight 2016-2019 magazines (782 pages, about 1.2
million characters of clean text) were full-text searched against the same 39 names, turning up
exactly one mention - Deven Richardson, named but not pictured - and confirming the redesigned
magazine format carries no portrait grids or club composites at all from 2017 onward. That second
file's own conclusion is explicit: "the yearbook stopped after 2016 and the magazines that
replaced it carry no portrait grids and no club group photographs at all, which is the structural
reason the 2017-18, 2018-19 and 2019-20 officers have no Talisman route." Corrected item 14's note
in place to say so, so a future pass does not spend a session's worth of several-hundred-megabyte
Wayback downloads re-proving a result this archive already has on file. This is the same class of
cross-file staleness today's earlier pass found in item 15 (the UA1C4/10 finding aid, independently
"discovered" on two different dates by two different passes that did not know about each other) -
worth a note for whoever next touches this file: `_topscholar-wanted.json` and the `*-notes.json`
files are not kept in sync automatically, and a note's date is not a guarantee that a later,
unlinked file hasn't already superseded it.

## Eleven recent gap names, checked against wkuherald.com

With both Talisman routes closed, swept `portrait_gap.py --any-year`'s 2021-22 through 2025-26
names that had not already been closed in `n1419-notes.json` or `n2025-notes.json` against
wkuherald.com's own search API, which was reachable all session: Mallory Hardesty, Garrett Baum,
Kayla Distler, Connor Ferguson, Elizabeth Gannon, David Darnell, Reed Hensley, Brooke Mitchell,
Neel Patel, Tyreesha Morris, Danny Vuleta. Danny Vuleta returns no posts at all. Every other name's
SGA-related hits are text-only results or bill-passage stories with no `<figure>` element in the
raw post content, or belong to an unrelated person of the same name (the Brooke Mitchell hits are
2003-04 softball and basketball coverage). Two posts do carry a real photograph - the 25 August
2026 committee-chair swearing-in story (for Morris) and the 12 April 2021 ballot-opening story (for
Baum) - but both are uncaptioned-by-name group shots (a swearing-in ceremony, an executive-cabinet
meeting), not a frame keyed to any one person. Recorded in `n2025-notes.json` so this specific
search is not repeated. Nothing in `data/photos.json` or `data/photos/` changed this pass.

## Conclusion

No new portrait. The two routes that have produced the project's only new content since late
October were both closed this pass, consistent with roughly half of this week's passes; the
`archive.org` catalogue check confirms there is no bypass around that closure for the specific
2014-2020 volumes this gap most needs. The concrete result of this pass is housekeeping rather than
a new face: one stale cross-file tracking note corrected (closing a sweep that was already done so
it stops reading as outstanding), and eleven names newly, explicitly closed against wkuherald.com
rather than left unchecked. `build.py` and `check_data.py` both pass clean. Landed on
`research-photos`.
