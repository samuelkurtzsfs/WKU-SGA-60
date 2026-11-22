# Photograph run, 22 November (second pass)

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` — 61 years, 1964 events, 60 people have been
  president; every president and student regent still carries a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` — same standing gap as this
  morning's pass: 187 same-year officer/Senate slots with no portrait, 157 people, 155 with no
  portrait anywhere in the file. Spot-checked a sample of names against `data/photo-finds/` and
  this morning's own report; all match a logged dead end. Did not re-run the exhausted searches a
  further time.
- **Priority 4**: all 61 years carry at least one `years`-level photograph entry.

`build.py` and `check_data.py` both ran clean; the `site/` build-date-only diff was reverted.

## What this pass tried

This morning's pass (`photo-run-2026-11-22.md`) already found the baseline unchanged and did the
one piece of real work available — cleaning five resolved cases out of
`data/photo-finds/_for-the-editor.md`. Rather than repeat that morning's exhausted-search list a
further time today, this pass took the one concrete lead that file still describes as open on its
own terms: **Sawyer Coffey's PRSSA group photograph** (2016 Talisman, p. 314), where the face and
the group membership are settled but the row position within the photograph is not, and the note
says "one more source of her face settles it either way."

Checked whether a second photograph of her exists on archive.org, which is not rate-limited and
was the obvious place to look first:
- `archive.org/metadata/talisman2016west` and `talisman2017west` both return an empty object —
  those identifiers do not exist on archive.org. The 2016-17 Talisman is not among the volumes
  archive.org holds under this project's naming convention (consistent with the already-documented
  gaps elsewhere in the run, e.g. 1967-70 and 1982-85).
- `talisman2018west` also 503'd / was unreachable by direct djvu-text download even where the
  identifier might exist; did not pursue further, since the 2016-and-later Talisman is a magazine
  without a yearbook-style club-photo grid (established in this morning's pass), so a second PRSSA
  photo in a later volume is unlikely to exist in the first place even if the file could be read.

A second source for Sawyer Coffey would need the digitalcommons TopSCHOLAR PDF of the 2016
Talisman itself (paced, browser-header fetch) or a wkuherald.com individual photo, and the latter
is already closed as a dead end per `_for-the-editor.md`. Did not open a digitalcommons session
for a single, already-flagged editorial judgement call — the file itself states plainly that no
further automated research can resolve this one, and that stands.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. The standing 155-person
officer gap and the 13-person editorial-judgement backlog in `_for-the-editor.md` are both
unchanged from this morning's pass; there is nothing new for a future automated run to add on
either front without either new access (the Wayback Machine, still unreachable) or a person's
decision on the open identifications.
