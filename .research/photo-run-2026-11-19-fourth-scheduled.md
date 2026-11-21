# Photograph run, 19 November (fourth scheduled pass): Tyreesha Morris rechecked against the newest article naming her, nothing new anywhere

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: every president and every student regent in `data/years.json` has a portrait.
  Zero missing.
- **Priority 4**: all 61 years carry at least one `years`-level photograph entry.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` is unchanged from the morning's
  three passes - 187 cabinet/Senate leadership slots with no same-year portrait, 155 people with
  no portrait anywhere in the file. Every name already has a documented dead end in
  `data/photo-finds/`. Confirmed by grep that every one of today's gap-list names, including the
  one checked below, is already cross-referenced in at least one `_officers-*`, `*-notes.json` or
  `_do-not-use.json` file.
- All six 2026-27 executive and Senate-officer names (Caden Lucas, Jakob Barker, Will Derryberry,
  Gabi Pace, Cayden Bailey, Veronica Butler) and the current senator roster already carry a
  published portrait.

## What this pass checked

The only 2025-26/2026-27 name `portrait_gap.py` still flags is **Tyreesha Morris** - First
Generation Senator in 2025-26, later named Mental Health and Well-Being Committee chair for
2026-27. The 12 November pass had already searched for her by name and found nothing; this pass
went at it from the other direction, opening the one article that actually names her in the
committee-chair role: "SGA kicks off 60th year on campus, swears in new committee chairs"
(25 August 2026, `wkuherald.com/96580`).

That article embeds one photograph (President Lucas thanking students for Move-In help), but the
WordPress media library holds two more uploaded the same day and not embedded in the piece,
found via `/wp-json/wp/v2/media?search=082526_SGA`: `082526_SGA_BH-5-1.jpg` and
`082526_SGA_BH-6.jpg`, both showing the committee-chair nominees being sworn in as a group. Read
both captions directly rather than assume from the filename: neither names a single person. One
reads "the nominees for speaker of the Senate and committee chairs... are sworn in," the other is
near-identical. No individual in either frame is identified, so CLAUDE.md's rule against
attaching a name without a caption naming that person rules both out on sight - there is no
candidate crop to even weigh.

Also ran a plain WordPress media search for "Tyreesha" directly (zero hits - her name does not
appear in any image caption or alt text the Herald's API indexes) and a web search for her name
against wkuherald.com, which returned nothing beyond the sources already on file (the
presidential-ticket listing, the Senate committee page, Senate minutes). No photograph exists to
find at any of her known mentions.

## Also checked

The most recent Herald SGA coverage (17 November, "SGA prepares for the holidays with new
bills") was already confirmed on file by this morning's second pass. The 15 November homecoming-
breakfast article, which carries the two photographs (Lucas, Donté Reed) already added to
`data/photos.json` on 16 November, was reopened to confirm nothing further was missed; both
subjects already carry portraits and the article names no one else. `digitalcommons.wku.edu` and
`wkuherald.com` both answered plain requests all session - no backoff needed either side.

## Conclusion

No new portrait. Added one note to `data/photo-finds/2016-2025-notes.json` recording this
pass's check so a future run does not repeat the same search against the same article.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both pass clean. Landed on
`research-photos`.
