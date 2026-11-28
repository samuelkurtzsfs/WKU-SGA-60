# Photograph run, 14 November (scheduled): network gates unchanged, one live-site channel checked and closed

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a `leaders` portrait entry in `data/photos.json`, unchanged since prior runs.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports 186 officer-slots without
  a same-year portrait, 155-156 people with no portrait in any year — essentially unchanged from
  13 November's three passes (which also reported 187/157).
- **Priority 4**: all 61 years already carry at least one photograph.

## Network state, retested fresh

Same four checks this project runs every time, repeated now:

- `cgi/viewcontent.cgi` (TopSCHOLAR PDF download) — `403`, same Cloudflare challenge, tested
  against article 7642 (the 2009-10 lead).
- `web.archive.org` — `curl: (35) Recv failure: Connection reset by peer`.
- `archive.org` (no `www.`) — open; confirmed again that no Talisman volume exists there for
  1998 or 1999 (`talisman1998west` / `talisman1999west` both `404`), closing off that route for
  the 1994-99 committee-chair cohort (Anne Guillory, Tim Hatton, Bonnie Newton, Matt Bogard, etc.)
  exactly as the 16 October pass found.
- `wkuherald.com` — `200`, open as usual; its WP-JSON search still returns nothing usable for
  ShyAnte'e Williams (checked again, same null result as 13 November).

No change in any gate from yesterday.

## New channel tried: the live wku.edu/sga site's own headshot pages

Nothing in the prior reports had fetched `wku.edu/sga`'s current executive and judicial pages
directly to compare their headshots against what `data/photos.json` already holds. Did that this
pass:

- `wku.edu/sga/executive/index.php` carries headshots for the five 2026-27 executive officers —
  Caden Lucas (President), Jakob Barker (Vice President), Will Derryberry (Chief Financial
  Officer), Gabi Pace (Chief of Staff), Cayden Bailey (Chief Communications Officer) — each
  headshot sitting beside a heading that names the officer. All five already carry a portrait in
  `data/photos.json` (the `2026-27-*` files, sourced from WKU News and Herald photo frames), so
  this confirms rather than adds. One oddity worth a note for whoever next touches this page:
  Caden Lucas's `<img>` tag carries a stale `alt` attribute reading "A headshot image of Student
  Body President Rush Robinson" (Robinson was his predecessor) even though the heading beside it
  correctly says "Caden Lucas" — a leftover from the page template, not a misidentification in
  our record.
- `wku.edu/sga/2018-2019-judicial/judicial-council.php` (current content despite the stale URL
  slug) lists four 2025-26/2026-27 judicial council members, two with headshots: Sophie Stirling
  (Chief Justice) and Hannah Hash (Associate Chief Justice). Elliott Tapp and Maggie Phelps
  (Associate Justices) are listed by name with no headshot. **None of these four names are in
  `data/years.json` for 2025-26 or 2026-27** — the judicial council isn't currently recorded in
  either year's `organization` block at all (older years do carry a judicial council under
  `senate.officers`, e.g. 2020-23's Chief/Associate Justices). Since this task's rule is that a
  `photos.json` leader entry's name must exactly match a name already in `years.json`, I did not
  add these two photographed names — there is nothing in `years.json` yet for them to attach to.
  Flagging this for whichever routine researches 2025-26/2026-27's organization: once Stirling and
  Hash (and Tapp and Phelps) are added as judicial officers, their portraits are sitting ready at
  `wku.edu/sga/2018-2019-judicial/judicial-council.php`, captioned by name, with Stirling's and
  Hash's images at
  `wku.edu/sga/2025_2026_executive/headshots_website/sophiestirling.jpg` and `.../hannahhash.jpg`.
- `wku.edu/sga/legislative/senate_committees.php` — no headshots on the page at all.
- No other page under the current `wku.edu/sga` navigation (About, Signature Services,
  elections, scholarships, org-aid, initiatives) carries officer headshots.

This closes the live SGA site as a route for any name already in the gap list: the only headshots
it holds belong to people this archive had already photographed by another route.

## Lowest-coverage names re-checked

Counted how many `.research/photo-run-*.md` files mention each of the 156 remaining no-portrait
names, to find anything under-searched relative to the rest. The floor (excluding the already
re-confirmed ShyAnte'e Williams) was Anne Guillory and Tim Hatton at 2 mentions each — both
1990s committee chairs, both already traced in the 16 October pass to the same closed Talisman/
`viewcontent.cgi` gate as the rest of the 1994-99 cohort, and both still closed today for the
reasons above. No route opened for either this pass.

## Conclusion

No new portrait this pass, and no change to `data/photos.json`. `build.py` and `check_data.py`
both pass clean: 61 years, 1964 events, 60 presidents, every one portrayed. The remaining ~156
officer/Senate names stay unphotographed in the record as far as every reachable source is
concerned; the one genuinely new lead this pass turned up (Stirling and Hash's judicial-council
headshots) is blocked on a `years.json` gap rather than a photo gap, and is noted above for the
organization-layer routine rather than acted on here. `viewcontent.cgi` and `web.archive.org`
remain closed; a future pass should keep retrying those at different hours rather than re-sweeping
`wku.edu/sga`, `wkuherald.com` or the Talisman `archive.org` holdings again for this cohort, all
three of which are now confirmed exhausted for it. Landed on `research-photos`.
