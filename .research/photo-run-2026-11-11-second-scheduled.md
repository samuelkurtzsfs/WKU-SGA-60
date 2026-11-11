# Photograph run, 11 November (second scheduled pass): archive.org's 503s were transient, both standing network blocks reconfirmed closed, six more officer-gap names checked and declined

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, with valid JPEG magic bytes. Already done before
  this run started.
- **Priority 2**: `python3 scripts/portrait_gap.py --any-year` confirms every president and student
  regent in `data/years.json` has a `leaders` portrait entry. Nothing missing at the leader level.
- **Priority 3**: 188 officer-slots with no portrait for that person in that year, 158 people.
  Unchanged from the first scheduled pass earlier today.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.

## What this pass chased, and why it did not add a portrait

**archive.org's djvu route, retried cold.** The first scheduled pass today logged HTTP 503 on
`archive.org/download/<id>/<id>_djvu.txt` all session and flagged it as worth a plain retry. Retried
this pass: `talisman1975west`, `talisman1979west`, `talisman1981west` and `talisman1987west` all
answered 200 with their full text, cleanly and immediately. So that 503 was a transient archive.org
outage, not a standing block - confirmed, not just hoped. This does not open a new route into the
larger 2016-2025 gap, though: archive.org holds no Talisman identifier for any of 2015 through 2020
under the `talisman<year>west` naming (`archive.org/metadata/talisman<year>west` returns an empty
`{}` for each). Searched the four reachable years' full text for the standing pre-2003
archive.org-covered names anyway (Vern Pulman, David Young, Alice Wicks, Steve Wilson, Mark
Chesnut, Chris Millay, Dwight Austin) - zero hits beyond what prior passes already found (an index
page number for Wicks and Chesnut, nothing at all for the rest). The 1981 volume's own
"ASSOCIATED STUDENT GOVERNMENT" composite caption (28 names, front/second/third/back row) was read
in full; none of the six missing 1980-81 names is in it.

**Both standing blocks retested cold, as this file's own instruction says to do every run:**
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` (article 7642) - still the Cloudflare "Just a
  moment..." 403 challenge page, browser navigation headers included.
- `web.archive.org`'s `if_` bypass against the same article - still fails at the TLS layer with
  the same `ws_closed_mid_exchange` tunnel error the proxy log has shown on every recent pass.
  (The plain `digitalcommons.wku.edu/dlsc_ua_records/<id>/` landing page, by contrast, answers 200
  cleanly - it is specifically the PDF route that is closed, same as every pass since this file
  started tracking it.)

**Six officer-gap names not named in any prior sweep, checked against wkuherald.com's REST API**
(posts search, then each matching post's featured-media caption): Reed Hensley (Member of
Organizational Aid Board, 2022-23), Brooke Mitchell (Mental Health and Wellbeing Committee Member,
2022-23), ShyAnte'e Williams (Graduate Student Senator, 2022-23), Danny Vuleta (First Generation
Senator, 2022-23), Garrett Baum (Associate Justice, 2022-23), Neel Patel (Gatton Academy Senator,
2022-23). Three (Hensley, Vuleta, ShyAnte'e Williams) returned no matching post at all. The other
three surfaced posts with captioned photographs, but every caption either names other people
entirely (Olivia Feck, Garrison Reed, Cole Bornefeld, Sam Kurtz) or is an unnamed group shot
("Members of the WKU Student Government Association executive cabinet listen to proposals from
senate member nominees..."). None names any of the six. No new portrait from this batch.

## Conclusion

No new portrait this pass. Both standing network blocks (digitalcommons PDFs, the Wayback `if_`
bypass) are confirmed closed exactly as the last several passes found them - this pass's only
correction to the record is that the archive.org djvu 503s were transient, not a new block, and
that correction changes nothing about what's reachable. Six more names are now checked and
declined against wkuherald.com, logged in `data/photo-finds/2016-2025-notes.json` so a future pass
does not repeat them. `data/photos.json` and `data/photos/` are unchanged. `build.py` and
`check_data.py` both pass clean. Landed on `research-photos`.
