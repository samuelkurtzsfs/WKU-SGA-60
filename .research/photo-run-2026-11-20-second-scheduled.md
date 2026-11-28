# Photograph run, 20 November (second scheduled pass): baseline reconfirmed, no new portrait

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, checked directly against the file.
- **Priority 2**: `python3 scripts/check_data.py` still reports every president and student
  regent with a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still returns the same shape as
  every pass since mid-November — roughly 157 cabinet/Senate officers with no portrait anywhere
  in the file.
- **Priority 4**: all 61 years still carry at least one `years`-level photograph entry.

## What this pass checked

Tested the three network gates directly rather than trust the morning pass's numbers:
`wkuherald.com`'s WordPress API answered 200, `digitalcommons.wku.edu/sga/` answered 200,
`web.archive.org` reset the connection mid-handshake again — same shape as the first pass today
and every pass since the block was first isolated.

Pulled wkuherald.com's ten most recent SGA-tagged posts by date directly (not from a cached
list): newest is still 17 November ("SGA prepares for the holidays with new bills"), the same
post the first pass today already had on file. Nothing has been published since the morning
check.

Sampled nine names from the current `portrait_gap.py` output that were *not* among the dozen the
morning pass re-checked, to make sure this pass wasn't just re-reading the same file: Jillian
Kenney, Alexis Mayne, Erika Puhakka, Brenna Mathews, Turner Reynolds, Jason Herlick, Justin
Goins, Nicole Massarone, Garrett Baum. All nine are already cross-referenced as exhausted leads
across `_officers-truly-missing-2026-09-06.json` and the dated notes files (`n1419-notes.json`,
`n2025-notes.json`, `2016-2025-notes.json`), with `digitalcommons.wku.edu` reachable this pass too
— so the dead end is the record, not a closed gate.

## Conclusion

No new portrait. `digitalcommons.wku.edu` and `wkuherald.com` are both open this pass;
`web.archive.org` is still blocked. No data changed, so nothing new to commit to `data/`; this
note is the only addition, landed on `research-photos`.
