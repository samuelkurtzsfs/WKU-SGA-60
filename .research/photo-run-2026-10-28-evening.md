# Photograph run, 28 October evening (scheduled): independently reconfirmed, no new portrait

Started cold, without reading the branch's prior commits first, and arrived at the same place:
the stored trigger brief's priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley)
has carried a portrait in `data/photos.json` since August and is unchanged. Priority 2 (every
other president/regent) and priority 4 (every year has at least one photograph) are both still
zero-gap — confirmed directly against `data/years.json` and `data/photos.json`, not assumed from
this file.

Priority 3 (executive/Senate officer portraits) is where the three earlier passes today already
spent their effort, landing `photo-run-2026-10-28-scheduled.md`,
`-second-scheduled.md` and `-third-scheduled.md`. This pass re-derived the same two findings
independently before reading those notes, which is worth recording as a second confirmation
rather than a restatement:

- **David Bass** (1977-78, Activities VP) — found in the 1978 Talisman, p. 34, the "A LIGHT
  MOMENT IN AN ASG MEETING" photo. Rendered the actual page (PyMuPDF, 200dpi) rather than
  trusting the OCR text alone: the photo holds three visible people for four named ones, with
  no left-to-right order given. Not usable — matches the reasoning already on file in
  `data/photo-finds/_do-not-use.json`.
- **Mark Chesnut** (1980-81, Treasurer) — the only `data/years.json` hit in the 1981 Talisman's
  back index is page 234, which resolves to the men's intramural all-sports champions list
  ("Mark Chestnut," a spelling variant), not a photograph, and not ASG. Also already on file.

New this pass, not in the prior three notes:

- Re-pulled archive.org's full Talisman catalog (`advancedsearch.php?q=identifier:talisman*west`)
  rather than trusting CLAUDE.md's written coverage table. It still returns exactly 19 items —
  1943, 1946, 1947, 1963-65, 1971-81, 1986-87 — unchanged from what the prior passes assumed.
  Nothing has been digitised there since the last check.
- Retested both standing blocks directly (not through `WebFetch` this time, through `curl` from
  this container): `viewcontent.cgi` still answers `403`; `web.archive.org` still resets the
  connection mid-exchange. Same as every test since 23-25 August. 20:01 UTC.
- Tried two 2000s officer names neither prior pass had searched by name alone, outside the
  archive.org/WP-JSON methods already exhausted: Aaron Pawley / Sarah Howell (2009-10) and
  Matthew Pava / Mark Henry (2003-05, IT roles). Plain web search, no site restriction and a
  `site:wku.edu` / `site:wkuherald.com` variant each. Nothing came back naming any of the four
  in an SGA context.

## Conclusion

No new portrait. Nothing in `data/` changed. The two network blocks and the archive.org
coverage ceiling are the whole constraint, and both are unchanged from this morning. This
trigger is now firing roughly every six hours and landing an equivalent "still blocked, still
nothing new" conclusion each time — four such passes today alone. Not raising this to the owner
again since the state itself was already reported 23 October; noting it here only so the next
run doesn't have to re-derive that the cadence, not the research, is what's unproductive right
now. Not posting a PR comment this pass — three already went up today saying the same thing, and
nothing has changed to justify a fourth. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean. Landed on `research-photos`.
