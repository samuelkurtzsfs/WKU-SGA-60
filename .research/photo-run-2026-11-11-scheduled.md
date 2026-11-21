# Photograph run, 11 November (scheduled pass): the Alex Cissell headshot question closed as declined, the September "truly missing" tail re-checked, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`. Already done before this run started.
- **Priority 2**: every president and student regent in `data/years.json` has a `leaders` portrait
  entry; `scripts/portrait_gap.py --any-year` (the only reliable way to re-derive this, see its own
  docstring) confirms nothing is missing at the leader level.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` reports 188 officer-slots with no
  portrait for that person in that year, 158 people, 156 of whom carry no portrait anywhere in the
  file. Unchanged from the fourth scheduled pass on 10 November. Checked the two non-exact-string
  names the gap script's `--list` turns up that are not in `data/photo-finds/_officers-truly-missing-2026-09-06.json`
  verbatim (`Jacob A. Miers`, `Lane (Caroline) Simpson`, `Lisa M. Kappler`) - all three are spelling
  variants of names already on that list (Jacob Miers, Caroline Simpson, Lisa Kappler), not new gaps.
- **Priority 4**: every one of the 61 years carries at least one photograph. No gap.

## What this pass chased, and why it did not add a portrait

**The Alex Cissell headshot, flagged open in `data/photo-finds/2016-2025-notes.json` as "LEAD, NOT
A CONFIRMATION."** A prior run found a studio headshot of an Alex Cissell credited to the Herald's
Student Publications Advertising Staff and suspected it might be a better portrait of the same Alex
Cissell who chaired SGA's Mental Health and Wellbeing Committee in 2021-22 - the person this
archive already has a published, cited portrait for, cropped from a 2024 Herald photograph of her
presenting SGA legislation. The prior run could not download either image to check. This run could:
`wkuherald.com` answered a plain `curl` with a browser `User-Agent` cleanly all session, no
Cloudflare block. Fetched both frames and viewed them side by side against the published crop.

The two faces are plausibly the same person - similar coloring, a similar brow and nose - but nothing
stronger than a by-eye impression across two dissimilar photographs (a broad studio smile versus a
mid-sentence three-quarter angle from across a meeting room). That is not the kind of confirmation
CLAUDE.md requires before attaching a name to a face, and the stakes here are exactly the ones its
"never use a photo whose subject you cannot confirm" rule exists for: the headshot's own caption
identifies a Herald advertising-staff member, a different role from the SGA officer, and the project
has a standing rule against merging two people who share a name. The published portrait already
rests on a real caption naming Cissell inside SGA business, so there was no gap to fill here, only a
quality upgrade on offer, and it is not worth the identification risk. Declined. The existing
`data/photos/2021-22-alex-cissell.jpg` is unchanged. Logged in `data/photo-finds/2016-2025-notes.json`.

**The "NOT INSPECTED" note on Aniya Johnson and Preston Romanov.** A prior run's handoff said two
quarantined crops for these two people were never opened. Checked `data/photos.json` directly
rather than chasing files that are not in this repository (a `_unverified` quarantine directory is
evidently a scratch convention of whatever browser-driven tooling produced those crops, not
something committed): both people already carry published portraits from other sources. Moot.
Logged.

**Six names from the 6 September 2026 "truly missing" list, re-checked against fresh sources.**
Chose Josh Zaczek, Erika Puhakka, Justin Goins, Nathan Cherry, Brenna Mathews and Hope Wells -
officers from 2018-19 through 2022-23, a span where `wkuherald.com`'s own REST API should be the
best-populated source. For each: searched `/wp-json/wp/v2/posts?search=<name>`, then pulled
`/wp-json/wp/v2/media?parent=<post id>` for every post returned and read every caption. No post's
attached media names any of the six. A web search for the same six names surfaced text mentions
(senate minutes, bylines, and - for Goins - a Herald story on a Judicial Council hearing he
presided over) but the hearing's own photographs caption Speaker Julie Mischuck and President Cole
Bornefeld, not Goins, so nothing usable came of it either. This matches the September determination
exactly; none of the six moved.

**archive.org's djvu full-text route was unavailable all session.** `archive.org/download/<id>/
<id>_djvu.txt` returned HTTP 503 for every Talisman identifier tried, including a known-good older
one (`talisman2015west`, which this project has used before). The agent proxy's own status log
shows `ia801234.us.archive.org` unreachable at the connection level, which points to an
archive.org-side or routing problem tonight rather than anything about this project's request
pattern. Nothing to conclude from this about Talisman coverage for 2016-2020 either way; worth a
plain retry on a later run before assuming those volumes are inaccessible.

## Conclusion

No new portrait this pass, and none expected: every lead this run could find had already been
closed by earlier passes (`data/photo-finds/_officers-truly-missing-2026-09-06.json`,
`_topscholar-wanted.json` and `2016-2025-notes.json` between them cover all of it). The one genuine
open thread left in the research notes - the Cissell headshot - is now closed with a reasoned
decline rather than left dangling. `data/photos.json` and `data/photos/` are otherwise unchanged.
`build.py` and `check_data.py` both pass clean. Landed on `research-photos`.
