# Photograph run, 22 November (third pass)

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` — 61 years, 1,964 events, 60 people have been
  president; every president and student regent still carries a portrait. The current president,
  Caden Lucas (2026-27), is portrayed (`2026-27-caden-lucas-solo.jpg`, WKU News), and that same
  file is already reused back onto 2024-25 and 2025-26 for Lucas and Rush Robinson where no
  year-specific photograph exists.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` — unchanged: 187 same-year
  officer/Senate slots, 157 people, 155 with no portrait anywhere in the file. Spot-checked a
  sample against `data/photo-finds/` and this morning's two passes; still no untried name.
- **Priority 4**: all 61 years carry at least one `years`-level photograph entry.

## Access check

- `digitalcommons.wku.edu/` answers 200 directly.
- `web.archive.org` still resets mid-TLS from this container, consistent with every pass since
  mid-September.
- No new wkuherald.com SGA post since the ones this morning's two passes already read.

## What this pass did not repeat

This is the third automated pass today. The first two (`photo-run-2026-11-22.md` and
`-second.md`) already reconfirmed the baseline, retested every open network gate, ran fresh
distinctive pre-2011 names against web search, checked the 2016-2025 cohort for the fourth time
in two weeks, and cleaned five resolved cases out of `data/photo-finds/_for-the-editor.md`. There
is no untried lead left for a fourth automated attempt to find today; running the same exhausted
165 or so search terms a further time would not change the outcome. No new portrait, no change to
`data/photos.json` or `data/photos/`.

## The two standing items that need a person, not another run

1. **`data/photo-finds/_for-the-editor.md`: 13 people, 14 entries, open since 8 September 2026
   (two and a half months).** Each is a case where a specific, well-documented photograph has been
   found and the only open question is whether the face in it is the same person as the named SGA
   officeholder — a yes/no editorial call CLAUDE.md requires a source-backed certainty for, which
   automated research cannot manufacture. Full detail in the file itself.
2. **The trigger cadence.** `research-photos`'s PR (#835) has carried a note for three weeks that
   this routine fires multiple times a day against a ~155-person officer-portrait gap that has
   been exhaustively searched through every open route. `update_trigger` was refused in an earlier
   run as "created via http_api, not by an agent" — only the account holder can change the
   schedule or stored prompt.

## Conclusion

`build.py` and `check_data.py` both run clean. No new portrait, no data change. Landing this
report only, and flagging both standing items above directly to the project owner rather than
writing a fourth identical "nothing new" pass into the PR body today.
