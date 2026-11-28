# Photograph run, 7 November scheduled pass: baseline and all three network blocks reconfirmed, no new lead

## Priorities 1, 2 and 4, reconfirmed directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60 people
  have been president. Zero presidents or student regents without a portrait across all 61 years.
- **Priority 4**: every one of the 61 academic years still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as every pass since 4 November: 948 officer slots, 188 without a portrait for that
  person in that year, held by 158 people, 156 with no portrait anywhere in the file. No name
  added or removed by any other routine since the last recorded pass.

## All three standing network blocks retested cold this pass

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` with full browser navigation headers
  (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`, a
  current desktop Chrome user agent), against a known article id — **403, Cloudflare "Just a
  moment..." challenge page**, unchanged from every pass since early November.
- `web.archive.org`, direct fetch — **connection reset mid-exchange** at the network layer,
  unchanged.
- archive.org's own Talisman catalogue (`archive.org/metadata/talisman<year>west`) spot-checked
  again across 1967-2000 — still exactly the same 19 volumes documented in prior passes
  (1971-1981, 1986-87, plus the older ones), none in the 1988-2026 range where the whole
  remaining gap sits.

## Independent check of five names from the gap, as a cross-check on the exhaustive-search claim

Before finding this branch's open PR and its own gap list, this pass independently searched
TopSCHOLAR-adjacent routes for five names picked cold from the officer gap: Tribhuwan Singh
(2021-22), Smita Peter (2017-18), Abhishek Bose (2016-17), Rachel Keightley (2015-16) and Sawyer
Coffey (2014-15, 2015-16). Searched wkuherald.com's WP-JSON endpoint (open) and general web
search. Found only text mentions — committee reports, meeting-minutes attendance lines, one
article headline — never a photograph with a caption naming any of the five. This matches the
branch's own prior conclusion for all five names exactly: no result changes the 158-person gap.

## Conclusion

Nothing added to `data/photos.json` or `data/photos/`. Confirms, independently, what the last
several passes already found: every name in the 158-person officer/Senate gap has had at least
one real check, the three routes that could still reach new material (digitalcommons PDFs,
archive.org Talisman beyond its fixed 19 volumes, web.archive.org) are all still closed, and
nothing has reopened in the days since the last confirmation.
