# Photograph run, 29 October (scheduled): wkuherald.com WP-JSON search extended to the
2003-15 officer names, closing the one range the prior pass's confirmation did not cover; no
new portrait

## Priorities 1, 2 and 4, reconfirmed against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry
  a portrait in `data/photos.json`, each file checked again this pass for valid JPEG magic
  bytes (`FF D8 FF ...`). This trigger's stored brief still names them as portraitless; it still
  isn't true, as every run since 20 August has found.
- **Priority 2**: every leader entry in `data/years.json` whose role contains "president" or
  "regent" has a matching name in `data/photos.json`'s `leaders` list — checked directly against
  the file, not just via the script. Every one of those files exists on disk and opens with a
  JPEG or PNG magic number. No gap.
- **Priority 4**: cross-checked every year in `data/years.json` against both `photos.json`
  arrays (`leaders` and `years`) — all 61 years carry at least one photograph. The standing
  near-misses (1994-95, 2000-01) were not reopened this pass.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports 948
  officer slots, 188 with no portrait for that person in that year, 158 people, 156 with no
  portrait anywhere — unchanged from every pass since 28 October.

## New this pass: wkuherald.com WP-JSON run against the 2003-15 names specifically

The 28 October third pass's report says the wkuherald.com WP-JSON search had been run "against
all of them" for the 2016-26 names, by "the prior pass's name-by-name confirmation" — but does
not claim the 2003-15 range was ever checked that way, and nothing in the `.research/` history
for this branch shows it. CLAUDE.md and `SGA-60-AGENT-INFO.md` both give wkuherald.com full text
as running from roughly 2003, so that range was a genuine gap in coverage, not a retest.

Pulled the 59 unique names in `portrait_gap.py --any-year`'s output for years 2003-04 through
2015-16 and searched each against `https://wkuherald.com/wp-json/wp/v2/posts` with `_embed`,
checking every returned post's featured-media `alt_text` and `caption.rendered` for the
person's surname. 25 of the 59 names returned zero posts at all. Of the rest, eight produced a
caption containing the surname: Tim Howard, Mark Henry, Jessica Williams, Cory Gerald, Justin
McDole, Jackie Stewart and Robert Bell.

**All eight were checked by hand and all eight are the trap CLAUDE.md and
`SGA-60-AGENT-INFO.md` both warn about — never match a person by surname alone:**

- "Tim Howard" hit captions naming Howard Bailey, WKU's former vice president for student
  affairs (obituary coverage) — a shared given name turned surname, not the SGA officer.
- "Mark Henry" hit a Cherry Hall renovation photo (the hall is Henry Hardin Cherry Hall) and a
  football photo of wide receiver Matthew Henry.
- "Jessica Williams" hit a 2019 photo of a different Jessica Williams, a student climate
  organizer, dated four years after this officer's 2005-06 term.
- "Cory Gerald" hit two football photos taken at Gerald Ford Stadium in Dallas.
- "Justin McDole" hit a photo captioned about dance head coach Audrey McDole — different
  surname-holder, no first-name match.
- "Jackie Stewart" hit two photos of WKU athletic director Todd Stewart.
- "Robert Bell" hit a photo of the Robert and Mary Tincher Foundation's gift presentation —
  "Robert" is the foundation's name, not a caption of a person called Robert Bell.

None of the eight is the SGA officer being searched for. No portrait came out of this batch.

## Network state, retested

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (PDF download route): `curl` from this container
  still gets `HTTP 403`, same as every pass since 25 August.
- `web.archive.org`: `curl` still gets `Recv failure: Connection reset by peer`, same as every
  pass since the block was first logged.
- `digitalcommons.wku.edu` ordinary item pages (not the PDF route) and `digitalcommons.wku.edu/sga/`
  both still return `HTTP 200` — browsing and index pages are open, only the PDF download path is
  blocked, as prior passes found.
- `archive.org` (Talisman full text, djvu, and the BookReaderImages single-page API) is open and
  unthrottled, confirmed again by re-pulling `talisman1979west`, `talisman1981west` and
  `talisman1987west` in full. Re-checked the specific archive.org-year names already in the gap
  list — David Young (1978-79), Mark Chesnut/Chestnut (1980-81), Chris Millay, Dwight Austin
  (1986-87), Vern Pulman (1974-75) — against this year's volumes directly, including pulling the
  two full-resolution pages (288-289) the 1978-79 organization record cites for David Young.
  Page 288 is president Steve Thornton at the gavel and two other captioned ASG members (Victor
  Jackson, an unnamed group shot); page 289 is a sidebar naming Young only in running text, no
  photograph of him. Chesnut's own index citation (p. 234) turned out to be an intramural
  sports-winners page naming a "Mark Chestnut" (different spelling) with no photograph attached
  to the name at all — an intramural badminton and racquetball win, not a portrait. Millay and
  Austin do not appear anywhere in the 1987 volume's ASG pages; the only "Millay" and "Austin"
  hits in that volume's text are unrelated students and unrelated place names (Austin Peay).
  Confirms the 28 October finding rather than adding to it: nothing new in this lane.

## Conclusion

No new portrait landed this pass. The one real gap in prior coverage — whether wkuherald.com's
WP-JSON search had actually been run against the 2003-15 officer names, not just 2016-26 — is
now closed, and came back negative, with every apparent hit traced by hand to a different person
sharing a surname. The archive.org Talisman route was re-verified against the same handful of
names already in its reach rather than assumed stale. Both standing network blocks
(`viewcontent.cgi`, `web.archive.org`) are unchanged. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean; `data/photos.json` and `data/photos/` are
unchanged from `origin/research-photos`, and the build-date-only diff in `site/` was reverted
before committing. No push notification: nothing actionable surfaced for the owner, and the
blocked-route state has already been reported. Landed on `research-photos`.
