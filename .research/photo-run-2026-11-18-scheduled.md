# Photograph run, 18 November (scheduled pass): baseline reconfirmed, independent gap sample finds nothing new

## Baseline reconfirmed

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- Every president and every student regent in `data/years.json` has a `data/photos.json`
  `leaders` entry (checked programmatically against the whole file, not sampled).
- All 61 years carry at least one `years` photograph entry.
- `python3 scripts/build.py` and `python3 scripts/check_data.py` both pass clean. No `data/`
  changes this pass, so the `site/` rebuild (date-stamp only) was discarded rather than committed.
- `python3 scripts/portrait_gap.py --any-year`: 187 officer slots without a same-year portrait,
  held by 157 people, 155 of whom have no portrait anywhere in the file — the same standing count
  as every pass this month.

## Independent sample of the officer gap

Before consulting this branch's own `.research/` history, worked a handful of the executive and
Senate officer gap directly against the Talisman PDFs on archive.org, to see whether a fresh pass
over the primary source turned up anything the chain of prior passes had not:

- **David Young**, administrative vice president 1978-79 — 1979 *Talisman* (`archive.org/details/talisman1979west`),
  full PDF, p. 289 area: quoted on the new 24-seat ASG constitution, no captioned photograph of him.
- **Alice Wicks**, secretary 1978-79 — same volume; her name does not appear outside the alphabetical
  index, which carries no page number for her.
- **Mark Chesnut**, treasurer 1980-81 — 1981 *Talisman* (`archive.org/details/talisman1981west`),
  full PDF p. 234 (the intramurals section) and the ASG group photograph on p. 282-283: the
  captioned ASG group shot names 28 people and Chesnut is not among them.
- **Steve Wilson**, Judicial Council chairman 1978-79 — 1979 *Talisman*: named twice in body text
  (Spring Sing, a track reference) but no captioned photograph tied to the Judicial Council.
- **Chris Millay** (Parliamentarian) and **Dwight Austin** (Sergeant-at-Arms), 1986-87 — 1987
  *Talisman* (`archive.org/details/talisman1987west`): neither name appears in the index at all.
- **Tribhuwan Singh**, Director of Enrollment and Student Experience 2021-22 — the one Herald
  piece that names him (`wkuherald.com/61104/...`, 23 Sep 2021) carries one uncaptioned lead photo
  that does not identify him.

All six came back empty against the strictest reading of the "confirm from caption or context"
rule. Checked afterward against `data/photo-finds/1976-1980-notes.json`: it already carries the
David Young and Mark Chesnut biographical facts quoted above, from an earlier pass, with the same
conclusion — present in the record, never captioned in a photograph. This pass reconfirms rather
than newly discovers that those two are exhausted leads; Wicks, Wilson, Millay and Austin were not
separately logged there but turn out to be equally empty.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. The 155-person gap is a very
thoroughly worked seam at this point — six fresh primary-source checks across two different
decades of Talisman volumes, done without reference to the prior logs, reached the same wall the
existing `.research/` history already describes. Landed on `research-photos` with only this note.
