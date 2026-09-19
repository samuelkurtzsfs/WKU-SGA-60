# Photograph run, 19 September (second scheduled pass) — a real source mapped, no portrait landed

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` §4 and §6 before
touching anything. `research-photos` was already merged into `main` up through the caption-paraphrase
commit; fast-forwarded to `origin/main` (801ae8f8) rather than merging, since it was a clean ancestor.

Re-checked the four standing priorities fresh:

- **Priorities 1 and 2 (presidents and regents): still fully satisfied.** All four named presidents
  (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) and every other `leaders` entry with
  `role: "president"` or `role: "regent"` has a portrait.
- **Priority 4: still satisfied at the minimum bar.** Every year has at least one photograph.
- **Priority 3, computed fresh rather than trusted from an earlier count**: 220 executive/Senate rows
  across `organization.executive` and `organization.senate.officers` have no matching entry in
  `photos.json`'s `leaders` list. By decade: 1960s 5, 1970s 5, 1980s 9, 1990s 37, 2000s 45, 2010s 73,
  2020s 46. 2016-17 (15 missing) and 2017-18 (14 missing) are the two densest single years.

## A new source, mapped rather than guessed at

Earlier reports in `data/photo-finds/_archive-gaps.json` had tried `wku.edu/Dept/Org/Student/SGA`
page by page, guessing individual filenames. This run instead prefix-searched the whole path through
the Wayback CDX API (`web.archive.org/cdx/search/cdx?url=wku.edu/Dept/Org/Student/SGA*`), which
returned the complete list of everything Wayback ever crawled under that path — 209 distinct URLs for
1996-2010 alone. That surfaced two genuinely new leads and closed off several more as structurally
empty, without spending requests guessing filenames one at a time.

**`cab9900.htm`** (despite the name, the live capture from December 2001) is the 2001-02 Executive
Cabinet page: a group photograph explicitly captioned "From L-R: Mark Rawlings, Jamie Sears, Leslie
Bedo, Jamil Sewell, & Aaron Spencer", credited to Sheryl Hagan-Booth, plus a second table pairing each
name to an office that matches `years.json`'s 2001-02 `organization.executive` exactly — Bedo
president, Sears executive VP, Sewell VP of administration, Spencer VP of finance, Rawlings VP of
public relations. All five already carry a portrait from another source, so this closes nothing new,
but it is an independent confirmation of five identifications already on file, from the organization's
own contemporary website.

**`e_profiles.html`** (five captures, all inside the 2004-05 academic year) is the Executive Officers'
Profiles page, and it embeds an individual headshot for two of its nine listed officers: Katie Dawson
(already covered) and — new to this archive — **Brittany Fausey**, Director of Academic and Student
Affairs 2004-05, pictured directly beside her own name, e-mail and biography in the page's own table.
That is as firm an identification as this project accepts.

**The image itself does not exist in the archive to retrieve.** A CDX prefix search of the entire
`Pics/ProfilePics/` directory these headshots live in returns exactly one file Wayback ever actually
fetched: `64aa.jpg`, captured 5 November 2004. Neither `Katie.jpg` nor `Brittany.jpg` — both plainly
embedded in a page Wayback did capture — was ever independently crawled, so their bytes are not
recoverable from this or any other route this run could find. This is now flagged in
`_archive-gaps.json` rather than dropped: if the Internet Archive ever re-crawls this path, or another
mirror of the live-2004 site surfaces, Brittany Fausey's portrait is at (what was)
`http://www.wku.edu/Dept/Org/Student/SGA/Pics/ProfilePics/Brittany.jpg`. The directory listing itself
is complete and static — re-running the same CDX search will not produce a different answer.

The one image Wayback did keep from that folder, `64aa.jpg`, turned out to be an uncaptioned outdoor
group photograph of roughly 25 people (a retreat, from the setting) with no names linked to it
anywhere this run could find. Declined under CLAUDE.md's rule against an unidentifiable photo.

**Checked and found photo-free**, so a future run does not re-open them looking for images: `cab.htm`
(three captures 2000-2002, one literally reading the placeholder text "<<Insert Picture Here>>"),
`exec.htm` (one capture, 2001), `executive.html` (four captures, 2004-05), `executive.php` (one
capture, 2005), and `c_profiles.html` / `j_profiles.html` / `l_profiles.html` (2004 captures — Congress,
Judicial and Senate bio pages, no embedded images at all). These pages are rich in names and titles and
may be worth a research routine's time, but they are not a photograph source.

The later "Site/" redesign (`executive.html` capture 2007) is likewise photo-free apart from a banner
graphic. Its one real photograph, `Site/Welcome_files/photo-filtered.jpg` (2007), is another
uncaptioned group shot (roughly 24 people), declined for the same reason as `64aa.jpg`.

## The 41-name Herald sweep, narrowed but not closed

The prior run (`.research/photo-run-2026-09-19-scheduled.md`) found that its own full-name matcher had
produced false negatives for Zach Skillman, Maksim/Makism Zaepfel, Daniel Vuleta and Trib Singh, and
located real Herald posts naming each of them — but had only confirmed the posts existed, not that
their photographs caption the person. This run opened the five specific posts at the image level:

- `wkuherald.com/60866` and `/61104` (Sept 2021 swearing-in and goals pieces): featured photos
  captioned only with meeting-description text, no names.
- `/65850` (Jan 2022 funding vote): captioned "members... listen", no names.
- `/65821` (the April 2022 election-results gallery): captions its one embedded photo with Sam Kurtz
  and Cole Bornefeld by name, nobody else.
- `/73655` (Aug 2023 swearing-in): captioned with a generic oath-taking description, no names.

None of the four names is individually captioned in any of these five posts, so none can be confirmed
pictured from them specifically. This narrows the lead but does not close it — the prior run's
surname searches returned several more posts per name than the single post each this run opened, and
the other 36 of the 41 names remain entirely unchecked at the image level.

## Nothing added to `data/photos.json` or `data/photos/`

`python3 scripts/build.py` and `python3 scripts/check_data.py` both pass clean on the unmodified data.
`site/` was regenerated, diffed against the committed copy (no change), and reverted. The only new
content this run produced is this report and the new entry in `data/photo-finds/_archive-gaps.json`.

## Left for the next run

- **Brittany Fausey's 2004-05 portrait is identified but unreachable by any route this run found.**
  Worth a fresh CDX check periodically in case Wayback backfills the crawl, or a search for a mirror
  of the live-2004 `wku.edu` SGA site outside the Internet Archive.
- **35 of the 41-name Herald cohort are still unchecked at the image level** — the prior run only
  established that Herald text mentions them; this run checked one post each for four of them and
  found no individual caption. Reading every post each surname search returned, not just the one
  quoted, is the next step.
- The 2016-17 and 2017-18 officer gap (29 names between them) has no Talisman route — confirmed again
  by an earlier run this same day that the mid-2010s Talisman is magazine-format with no club section
  — and now has no obvious `wku.edu`-site route either, since the Wayback captures of that domain this
  run found run out around 2010. `wkuherald.com`'s live search is the only source left untried at
  scale for this specific cohort.
