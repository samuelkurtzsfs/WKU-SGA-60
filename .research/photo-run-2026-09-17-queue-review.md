# Photograph run, 17 September (evening) — independent re-check, and the merge queue cleaned

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and SGA-60-AGENT-INFO.md §4 and §6 before
touching anything. `research-photos` had already been squash-merged into `main` (its tip was fully
contained in `main`'s history — `git log origin/main..research-photos` returned nothing), so per
CLAUDE.md's rule for a merged branch, it was restarted from `origin/main` rather than reused.

Confirmed the standing priorities fresh: all four named presidents (Nick Todd, Katie Dawson, Jeanne
Johnson, Reagan Gilley) and every other `leaders` entry with `role: "president"` or `role: "regent"`
already carry a portrait. Every year has at least one photograph on file. Priorities 1, 2 and 4 are
satisfied.

## Priority 3, sampled independently before finding today's other logs

Cross-referenced `organization.executive` and `organization.senate.officers` against
`photos.json` for the years archive.org's Talisman collection covers, and searched
`scripts/talisman.py` for eight names before checking `.research/` for same-day work already done:
**David Bass** (1977-78), **Vern Pulman** (1974-75), **David Young**, **Alice Wicks**, **Steve
Wilson** (all 1978-79), **Mark Chesnut** (1980-81), **Chris Millay** and **Dwight Austin**
(1986-87). Every one came back negative or ambiguous, matching
`photo-run-2026-09-17-officer-search.md` exactly:

- Bass: the 1978 Talisman p.34 "A LIGHT MOMENT IN AN ASG MEETING" group photo names him but the
  caption cannot be pinned to a specific face among the several men in frame — already correctly
  left as a year-level photograph rather than a leader portrait.
- Chesnut: both his indexed page numbers (1980 Talisman p. 257, 1981 p. 234) are intramural
  results tables, not photographs — a name collision, not a lead.
- Pulman, Wicks, Wilson, Young, Millay, Austin: no photograph found at all, either by name or by
  reading the back-of-book index.

Also checked `data/herald-photos.json` (the local, non-rate-limited index of 21,304 captioned
`wkuherald.com` photographs) against 23 cabinet/Senate officer names from 2007-2024 with no
portrait on file (Nathan Cherry, Ryan Richardson, Sawyer Coffey, Cole McDowell, Ian Hamilton,
William Hurst, Cassidy Townsend, Jessi Wurth, David Spalding, Brittany Crowley, Kara Raley, Amber
Daniel, Rachel Keightley, Abhishek Bose, Josh Zaczek, Brenna Mathews, Turner Reynolds, Tribhuwan
Singh, Elizabeth DeLozier, Justin Goins, Maksim Zaepfel, Livi Ray, Maiah Cisco). Zero hits on any
of them. This is a caption-text index, so a miss is not proof of absence, but it is one more
signal alongside the live-API checks two of today's other runs already made.

No new portrait added. This duplicates real effort — three other logs already on `main` from
earlier today reached the same conclusions on the same names, which was only discovered partway
through. **Grep `.research/photo-run-2026-09-17-*.md` for a name before spending a Talisman
download or an archive.org search on it.**

## The merge queue had three stale entries, now removed

`python3 scripts/merge_photo_finds.py` (dry run) reported one addition and two "improvements"
pending in `data/photo-finds/`. All three turned out to be already-superseded, not real findings:

- **`n2025.json`, "Annie Finch" (2024-25).** The researcher's own note flagged this correctly: SGA's
  2024-25 record spells this person's name two ways, "Annalise Finch" (senator) and "Annie Finch"
  (Community Relations Committee chair), tied to one NetID
  (`annalise.finch161@topper.wku.edu`) in two roster captures. `data/name-aliases.json` already
  maps `"Annie Finch": "Annalise Finch"` and the build already renders one page for her with the
  portrait attached — confirmed by rendering `site/o/annalise-finch.html` and finding no separate
  `annie-finch.html`. Merging the finding as filed would have added a second, redundant
  `photos.json` entry under the alias name for no visible effect on the site. Removed the entry
  from `n2025.json` rather than merge it.
- **`herald-sweep.json`, Katie Stillwell (2010-11) and Eric Smiley (2011-12).** Both already have
  the identical crop file in `photos.json`, cited there with a fuller, better-documented label
  (naming the source article, the four-up composite, and the position each person occupies in it)
  than the finding proposed. The finding's `src.url` pointed at the raw image file rather than the
  article page, which was enough for `merge_photo_finds.py` to read it as a different photograph
  and offer to overwrite the existing citation with a shorter one — a documentation regression, not
  an improvement. Removed both entries from `herald-sweep.json`.

`python3 scripts/merge_photo_finds.py` now reports zero additions and zero improvements pending.
The remaining eighteen "refused" entries are all `FACE PROVED, PERSON NOT PROVED` flags or one
withdrawn frame, correctly held for an editor's judgment rather than merged.

## Checks

`build.py` and `check_data.py` both pass clean. `data/years.json` untouched. Only
`data/photo-finds/herald-sweep.json` and `data/photo-finds/n2025.json` changed, and only by
removing the three entries above; nothing was added to `data/photos.json` or `data/photos/`.

## Still open

The cabinet/Senate officer portrait gap (roughly 200 names, see today's earlier logs for exact
counts under stated filters) remains the standing queue. Every lead in archive.org's Talisman
collection and `wkuherald.com`'s local index has now been tried for the names sampled here and in
today's other three runs; the pre-2003 slice still needs `viewcontent.cgi`, which stayed behind a
Cloudflare challenge all day.
