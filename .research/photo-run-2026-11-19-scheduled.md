# Photograph run, 19 November (scheduled): one new portrait — Stacy Kitchens, 1990-91 — via a live viewcontent.cgi window

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: every president and every student regent in `data/years.json` has a portrait.
  Checked programmatically against the whole file, not sampled.
- **Priority 4**: all 61 years carry at least one `years`-level photograph entry.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reported 187 cabinet/Senate
  leadership slots with no same-year portrait (157 people), 155 of whom have no portrait anywhere
  in the file. Every name on that list has a documented dead end in `data/photo-finds/` from prior
  passes — this run did not find an unexamined officer slot.

## What actually moved

`digitalcommons.wku.edu/cgi/viewcontent.cgi` answered a plain `urllib.request` GET with full
navigation headers directly — no web.archive.org detour needed this pass, 200 and a real PDF on
the first try, against article 1415 (the 1991 Talisman). This is the same TLS-fingerprint-shaped
gap prior passes have logged open and closed roughly a dozen times since September; it was open
this pass.

Spent the window on `data/photo-finds/_do-not-use.json`'s one entry carrying an explicit
"someone should read this page directly" instruction: Stacy Kitchens, 1990-91, barred in September
because an earlier identification rested on surname-plus-class-year guesswork. A companion
proposal in `n8892.json` said the 1991 Talisman, p. 185 "Associated Student Government" group
photograph would settle it if anyone could ever open the PDF. Opened it.

The photograph (printed p. 185, "Taking the Lead" spread) is captioned with ten names in two rows
of five. The back row — Allison N. Ade, Mary Susan Bunce, Gregory L. Willoughby, Donald Smith,
Mark Miller — runs woman, woman, man, man, man in the photograph itself, which is what fixes the
caption as left-to-right rather than assumed; the front row of five women then reads off the same
way. Kitchens is third of the five in front: dark hair, a floral waist wrap, the central and most
forward figure in the frame. Cropped and saved as `data/photos/1990-91-stacy-kitchens.jpg` — soft
and small (the source scan is roughly 96-150 dpi on a ten-person group photo), but a face, which
this project's own quality floor accepts over an empty frame.

One spelling note for the record, not an edit: the yearbook prints "Staci J. Kitchens"; SGA's own
minutes of 13 Nov 1990, already cited in `years.json` for this year, spell it "Stacy." Filed under
the `years.json` spelling so the name matches on the site; the discrepancy is recorded in the
`photos.json` entry's own note rather than touched in `years.json`, which is outside this agent's
remit.

Updated the `_do-not-use.json` entry in place to record the resolution, so no future pass re-opens
it expecting the old "page could not be checked" state. She is a rank-and-file Congress member
(`organization.senate.members`, not an officer slot), so this does not move the 155-person
officer-gap figure in §6 above — the headline priority-3 number is unchanged — but it is one more
named person in this archive who now has a face.

## What did not move

No other lead in `_topscholar-wanted.json` is still open; every entry there already carries a
"CLOSED" or equivalent resolution note from a prior pass. Did not spend the rest of the open
network window re-testing items already logged closed — the marginal value of a thirteenth
confirmation that `viewcontent.cgi` is a TLS-fingerprint gate, not a durable fix, is low next to
reading one new page end to end.

## Conclusion

One new portrait. `python3 scripts/build.py` and `python3 scripts/check_data.py` both pass clean.
Landed on `research-photos`.
