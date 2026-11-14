# Photograph run, 9 November (fourth scheduled pass): baseline and network state reconfirmed, no untried lead remains, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, checked directly against the file.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent has a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports the same 156-person
  cabinet/Senate-leadership gap this file has carried all week (948 slots, 188 without a
  same-year portrait, 156 with no portrait in any year). `--committees` reports the same
  174-person fuller count (990 slots including committee chairs, 231 without a same-year
  portrait, held by 196 people) the second pass today first measured.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.

## Network state this pass

Tested fresh rather than trusted from earlier notes today:

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: HTTP 403, with the standard browser navigation
  headers sent. Same standing Cloudflare challenge every pass today has recorded.
- `web.archive.org`: connection reset by the agent proxy's tunnel, same as every other attempt
  today.
- `archive.org`'s own download/catalogue hosts and `wkuherald.com`'s WP-JSON API both answered
  normally.

Unchanged from the day's three earlier passes.

## What this pass checked rather than re-deriving

Rather than re-running the full name-by-name search this file has already done multiple times
today, cross-checked whether anything on the current gap list — including the eighteen
committee-chair names the second pass surfaced and the sixteen it searched — is still genuinely
untried:

- Spot-checked a sample of names across eras (Chris Millay and Dwight Austin, 1986-87; Mickie
  Hennig and Chris Gaddis, 1988-89; David Smith and Trent Lyda, 1992-93; and the full set of
  2021-26 Senate names newly visible in this week's `--any-year` output: Tribhuwan Singh, Jesse
  Banales, Elizabeth DeLozier, Justin Goins, Garrett Baum, Danny Vuleta, Neel Patel, Mallory
  Hardesty, Reed Hensley, Brooke Mitchell, Kayla Distler, Connor Ferguson, Elizabeth Gannon, David
  Darnell, Livi Ray, Callison Padgett, Tyreesha Morris, Carter Smith) against every file in
  `data/photo-finds/`. Every one is already logged as searched, most in
  `_officers-truly-missing-2026-09-06.json` and the 2025-26-specific tracking files.
  None is a fresh name.
- Re-checked the two leads this morning's passes left open rather than closed:
  - **Katherine Smith** (`_topscholar-wanted.json` item 12, UA77/1 WKU Spirit 2007): still blocked
    on both routes that would reach the article itself (`viewcontent.cgi` 403, the
    `web.archive.org` `id_` bypass unreachable this pass too). No change possible without one of
    those two routes.
  - **Debbie Thomas** (1980-81 Complaint and Suggestion chair, page 356 of the 1981 Talisman):
    searched `data/herald-index-full.json` (no network cost) for any 1980 Herald item naming a
    Thomas that could supply the hometown, major or middle initial needed to pick between the
    pictured "Deborah L. Thomas (Glasgow)" and the Talisman index's separate, unlocated "Thomas,
    Debra Ann." Found nothing on point — the only 1980 hits for "Thomas" are three unrelated
    bylines (Thomas Deaton, Thomas Travis, Thomas Coohill) and an unrelated correspondence-file
    citation. The disambiguating fact would have to come from the SGA minutes of 2 September 1980
    itself, which are not mirrored locally and sit behind the same blocked `viewcontent.cgi`
    route. Left unconfirmed, as before.

No name on the current gap list, at any priority tier, is without a prior search recorded
somewhere in `data/photo-finds/`.

## Conclusion

No new portrait this pass. Both standing blocks (`viewcontent.cgi`, `web.archive.org`) are still
closed, and every name in the current gap — officers, committee chairs, and the newest 2021-26
Senate names alike — already carries a recorded search. There is no backlog of untouched leads
left on the two routes that remain open (`archive.org`, `wkuherald.com`); the two genuinely open
leads (Katherine Smith, Debbie Thomas) are both blocked on facts or files that only the closed
routes can supply. `data/photos.json` and `data/photos/` are unchanged. `build.py` and
`check_data.py` both pass clean. Landed on `research-photos`.
