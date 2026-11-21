# Photograph run, 5 November (scheduled): baseline and all three standing network blocks
reconfirmed unchanged; the one apparently-untried officer-gap name checked and closed negative

## Priorities 1, 2 and 4, checked directly against the files

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. The trigger's stored brief still names them as
  missing; it has been stale since August.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — zero presidents or student regents
  without a portrait across all 61 years.
- **Priority 4**: every year still carries at least one photograph.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports the
  same figures as every pass since 28 October: 948 officer slots, 188 without a portrait for that
  person in that year, held by 158 people, 156 with no portrait anywhere in the file.

## Network state, retested fresh

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`, full browser UA and the navigation headers
  CLAUDE.md specifies: `HTTP 403`, Cloudflare challenge. Unchanged since 25 August.
- `archive.org/advancedsearch.php` on `identifier:talisman*west`: still exactly 19 volumes (1943,
  1946-47, 1963-65, 1971-81, 1986-87). No new scan reaching the 1990s-2020s years where almost all
  of the remaining gap sits.
- `web.archive.org` direct page fetch: connection reset (`curl: (35) Recv failure`). Still closed.
- `wkuherald.com`'s WP-JSON endpoint: open, `200`.

## This pass

Cross-checked the 158-name gap list against every prior `photo-run-*.md` note by name. All but one
name has a prior individual check on record. The one that did not, **ShyAnte'e Williams** (Graduate
Student Senator, 2022-23), was searched via `WebSearch` restricted to `wku.edu`, `wkuherald.com`,
`digitalcommons.wku.edu` and `bgdailynews.com`. Confirmed as a graduate student senate candidate
(fall elections article) and as a University Athletic Committee member (Senate minutes, 8 Nov
2022), both text only. The only photograph found under these domains is a 2021 Homecoming Queen
candidate page — a different, non-SGA role, and CLAUDE.md's rule is to archive people acting in
their student government capacity, not any photograph of the same name found elsewhere. Not used.

## Conclusion

No new portrait landed this pass. `data/photos.json` and `data/photos/` are unchanged from
`origin/research-photos`. `python3 scripts/build.py` and `python3 scripts/check_data.py` both
exit clean; the only `site/` diff was the build-date line, reverted before committing. All three
standing blocks (digitalcommons PDF endpoint, archive.org's fixed 19-volume Talisman catalogue,
closed `web.archive.org`) are unchanged. With every one of the 158 gap names now individually
checked at least once and all three open-source routes still closed to the pre-2000s and
2010s-2020s material the remaining gap sits in, further scheduled passes should prioritise
retesting the three network blocks over re-searching names already closed negative, unless a
block lifts or a name is later added to the gap list by another routine.
