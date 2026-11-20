# Photograph run, 20 November (third scheduled pass): baseline reconfirmed, newest Herald photo checked and ruled out

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` — "61 years, 1964 events, 60 people have been
  president" — every president and student regent still carries a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` returns the same shape as every
  pass since mid-November: 187 cabinet/Senate leadership slots with no same-year portrait (157
  people), 155 of whom have no portrait anywhere in the file.
- **Priority 4**: all 61 years still carry at least one `years`-level photograph entry.

## What this pass checked

Extracted the full current gap list from `portrait_gap.py --any-year` (154 distinct names after
normalising) and grepped every file in `data/photo-finds/` and `.research/` for each one
verbatim, rather than trust the "already exhausted" claim from memory. **All 154 names are
already cross-referenced in a notes file** — there is no name on the standing gap list that
has not already been searched and written up by a prior pass.

Tested the three network gates directly: `wkuherald.com`'s WordPress API and
`digitalcommons.wku.edu/sga/` both answered 200; `web.archive.org` closed the connection
mid-handshake again (`ws_closed_mid_exchange` at the egress proxy), consistent with every pass
since the block was first isolated on 16 November.

Pulled wkuherald.com's ten most recent SGA-tagged posts by date directly: newest is still 17
November ("SGA prepares for the holidays with new bills"), the same post the first two passes
today already had. Nothing has been published since.

Opened that 17 November article's own photograph rather than assume it was already checked in
full: one figure, by Nathan Pennell, captioned "Dr Leslie Noth, WKU director of the Office of
Sustainability, thanking all the student volunteers from the WKU Food Pantry as they recieve a
$2,000 grant during the SGA meeting at Downing Student Union on Nov. 17, 2026." The caption
names only Noth, who is a university administrator, not an SGA officer, and does not name any
of the "student volunteers" pictured. The article's text separately quotes Parliamentarian and
Senior Senator Amelia Tucker and Chief Financial Officer Will Derryberry, but neither is tied to
this photograph by its caption, and both already carry a portrait in `data/photos.json` from
earlier sourcing. No usable new identification here.

## Conclusion

No new portrait. The standing gap list (155 cabinet/Senate officers with no portrait anywhere)
has no untried name left on it — every one is already a documented dead end across
`_officers-truly-missing-2026-09-06.json` and the dated notes files. The two open network gates
(`wkuherald.com`, `digitalcommons.wku.edu`) produced nothing newer than the 17 November post
already on file, and that post's own photograph does not caption an SGA officer. `python3
scripts/build.py` and `python3 scripts/check_data.py` both pass clean against an unchanged
`data/`; `site/` was rebuilt only to confirm it still builds, then reverted rather than
committing a same-content, new-date rebuild. Landing this note only on `research-photos`.
