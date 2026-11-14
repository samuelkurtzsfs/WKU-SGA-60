# Photograph run, 13 November (scheduled): queue re-checked, one fresh name tried, nothing new

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry
  a `leaders` portrait entry in `data/photos.json`, unchanged.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 187 officer-slots
  without a same-year portrait, held by 157 people with no portrait in any year — unchanged from
  12 November's closing passes.
- **Priority 4**: all 61 years carry at least one photograph.
- `data/photo-finds/_topscholar-wanted.json` carries 20 entries; all 20 are already logged
  `CLOSED` with reasoning on file. No open lead sat in the queue at the start of this pass.

## Looking for anything genuinely untried before repeating closed work

Rather than re-open a lead another pass already exhausted, checked every name on the current
187-slot gap list against the full text of every `.research/photo-run-*.md` report on file
(160+ files). All but one gap name has already been searched by full name at least once; most
have been searched repeatedly across several passes, including the 1996-97 to 2002-03 Talisman-
window cohort (Roadcap, Faught, Fite, Cole, Bailey, and others), which 19 September and
30 September already established has **no Talisman route at all** — `digitalcommons.wku.edu/
talisman/` 404s outright, the collection's own index of 469 slugs contains nothing matching
talisman/yearbook/annual, and archive.org's djvu mirror does not hold 1995-1999. Reconfirmed that
finding stands rather than re-attempting it.

**One name had never been searched by full name in any prior report: ShyAnte'e Williams**, the
2022-23 Graduate Student Senator (`years.json` already carries her election source, Herald
21 Sep 2022, "SGA fall election results announced"). Checked both Herald articles already cited
in her entry:

- *SGA fall election results announced, VP Reed appointed to Council on Postsecondary Education*
  (wkuherald.com/68255, 21 Sep 2022) — its only photograph shows President Cole Bornefeld
  congratulating VP Garrison Reed after the **spring** election, captioned to name only those two.
  No image of Williams.
- *SGA fall elections open for voting* (wkuherald.com/68206, 19 Sep 2022) — carries a photograph
  of the SGA executive cabinet listening to senate-nominee proposals at the 30 Aug 2022 meeting,
  but the caption names no one in it, so under this archive's own rule (never use a photo whose
  subject cannot be confirmed from the caption or article text) it cannot be used for Williams or
  anyone else pictured in it, confirmed or not.

No usable portrait for Williams. Logged here so a future pass does not re-open this search
thinking it untried.

## Conclusion

No new portrait this pass, and no change to `data/photos.json`. `build.py` and `check_data.py`
both pass clean. The remaining 157 ungapped people are, as far as every source this project can
currently reach is concerned, genuinely unphotographed in the record, barred by the no-caption
rule, or behind a Talisman window this archive does not hold. Landed on `research-photos`.
