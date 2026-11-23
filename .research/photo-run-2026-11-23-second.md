# Photograph run, 23 November (second pass)

## Baseline reconfirmed

Unchanged from this morning's pass and every one before it: all four priority-1 presidents
(Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) carry a portrait; every president and
student regent in the record has one; all 61 years carry at least one `years`-level photograph;
`build.py` and `check_data.py` both ran clean before this pass started.

## What's new: two wkuherald.com posts since this morning's check

The morning pass checked `web.archive.org` and the official site's archived headshot
directories but did not re-check wkuherald.com's own recent posts. Two had gone up since the
last such check:

- "SGA celebrates 60th anniversary with alumni homecoming," 15 Nov 2026 (photos by Tanner York)
- "SGA prepares for the holidays with new bills," 17 Nov 2026 (photos by Nathan Pennell)

Read both in full for every captioned photograph. The bills article named only non-student
officials beside its photographs (Dr. Leslie Noth of the Office of Sustainability; a Faculty
Regent-Elect, a Regent and a Staff Regent in sidebar file photos) — none of them an SGA student
office, so nothing there to act on. The homecoming article named four people who hold or held
SGA office: Donald Smith (1993-94 president, already portrayed), Caden/Cayden Lucas (current
president, already portrayed), Sam Kurtz (already portrayed, extensively), and Donté Reed
(2024-25 executive vice president, 2022-23 and 2023-24 director of enrollment and student
experience).

## One portrait upgraded, not a new gap filled

Reed already had a portrait on file — a crop from a 27 August 2024 Herald editorial-board
photo, reused under the same filename (`2024-25-donte-reed.jpg`) across all three of his years
in office, since no year-specific frame existed for 2022-23 or 2023-24 either. That existing
crop is small (18 KB), and a red-shirted shoulder in the foreground partly obstructs the frame.

The new photograph is a sharp, unobstructed, much higher-resolution single-subject frame
(113 KB; saved at 1200×853). Its caption, quoted in part, names him directly: "Former 2024-2025
Student Body Vice President Donte Reed" attending the SGA Homecoming breakfast "showing support
for former SGA Student Body President Sam Kurtz during his speech" on 14 Nov 2026
(wkuherald.com/99339, photo by Tanner York). He is the sharp-focus foreground subject; an
unnamed, out-of-focus man stands behind him in the same frame, not otherwise identified and not
claimed as anyone.

Replaced the image at `data/photos/2024-25-donte-reed.jpg` with this new frame and updated the
`src` on all three `photos.json` entries that share the filename (2022-23, 2023-24, 2024-25) to
describe it, since the old citation no longer matched the file on disk. This is a quality
upgrade of an already-correct identification, not a new name added to the record. Verified the
new file is a real JPEG (`FF D8 FF E0`) before committing.

## Searched and found nothing further

Checked the two articles' full text for every name on the standing Priority 3 gap list
(`portrait_gap.py --any-year`, currently ~155-157 Senate/officer slots): Carter Smith, Tyreesha
Morris, Elizabeth Gannon, Savanna Kurtz, Gabriel Jerdon, Maggie Yelton, Preston Jenkins, Rush
Robinson. None appears in either article.

## Conclusion

`build.py` and `check_data.py` both run clean after the change. One existing portrait replaced
with a better-sourced, better-quality frame; no new name added to the record. The two standing
items raised in the last several passes — the 13-person `_for-the-editor.md` identification
queue open since 8 September, and the trigger cadence itself — are unchanged and still need a
person, not another automated run.
