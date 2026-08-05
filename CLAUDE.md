# CLAUDE.md — rules for this repo

A public history of the WKU Student Government Association, 1966–2026, built for SGA 60.
Accuracy beats completeness. An empty year is fine. A wrong year is not.

## Architecture
- `data/years.json` is the single source of truth. **It is the only file you edit.**
- `scripts/build.py` regenerates `site/`. Run it after every change. Never hand-edit `site/`.
- The spine is the academic year, not the person. People attach to years and can be moved.

## Why the plaque is not trusted
Names come from the plaque in the SGA Chambers. **People who served have reported their year on it
is wrong.** Treat every `plaque_term` as a claim to verify, not a fact to copy.

## Settled facts — do not re-litigate these
- The student regent was a **separately elected office** from April 1968. That is why plaque years
  carry two names. William Menser was the first, April 1968. The seat was non-voting until at least 1972.
- Confirmed regents rather than presidents: Michael Fiorella 1972-73, Gregory McKinney 1974-75
  (first African American student regent), Sandra Norfleet 1982-83.
- By ~2001 the offices merged. After that, a second name in a year is a mid-year succession.
- Still open: Reed Morgan 1968-69, John Lyne vs Larry Zielke 1970-71, David Payne 1982-83.

## Sources, in order of usefulness
1. `digitalcommons.wku.edu/dlsc_ua_records/` — Herald back file, indexed article by article
2. `digitalcommons.wku.edu/wku_timeline/` — dated, described, citable single events
3. `digitalcommons.wku.edu/sga/` — SGA's own constitutions, minutes, legislation, correspondence
4. `wkuherald.com` — full text, roughly 2003 onward

TopSCHOLAR blocks bots on its own search page. Use `site:digitalcommons.wku.edu "query"` on Google.

**Pace yourself on digitalcommons.wku.edu or lose the whole run.** Its bot protection triggers
on burst volume: parallel or rapid requests get every subsequent request refused with a 403.
One request at a time, 3 seconds apart, and if you get a 403, wait 90 seconds and retry.
A slow polite crawl gets everything; a fast one gets nothing.

## Per-year workflow

### 1. Verify the leader, before anything else
For each person in `leaders`, search TopSCHOLAR for their name crossed with:
`"student government association"`, `"associated student government"`, `"student government"`,
`SGA`, `ASG`, `"student regent"`.

Then:
- Name confirmed in the plaque year → set `"name_verified": true`, add the source.
- Name appears consistently in a *different* year, within a year or two → **move the leader object
  to the correct year**, set `"year_confidence": "corrected"`, and record the old value in the note:
  `"Plaque reads 1974-75; Herald election coverage places this term in 1975-76."`
- Name found but the role is clear (president vs student regent) → set `role` accordingly.
- Nothing found → leave `name_verified` false. Do not guess.

Never silently change a year. The correction is part of the history.

### 2. Sweep the year
Search each keyword above against **both** calendar years of the academic year (1974 and 1975 for
1974-75). The digitised *Herald* on TopSCHOLAR is indexed article by article, so these return the
specific issues.

Log **everything SGA-related**, not only what the president personally did. Resolutions, elections,
turnout numbers, fights, budgets, appointments, committee work, things that failed. This is a
history of the organisation.

### 3. Write the entries
```json
{"date":"1975-04-16",
 "title":"Short factual headline",
 "body":"Two or three sentences. What happened and why it mattered. Plain past tense.",
 "src":{"label":"Herald 51:39, 25 Feb 1972","url":"https://digitalcommons.wku.edu/..."}}
```
- `date` is `YYYY-MM-DD`. If only the month is known use `-01`. If only the year, use `YYYY-01-01`.
- Events sort chronologically on build. Order in the file does not matter.
- Update `status`: `researched` (3+ events), `partial` (1–2), `empty` (0).

## Presidents are the heart of this project
The single most important deliverable is a full, verified account of every president and
student regent: profile, portrait, their year's complete record. When choosing what to work
on, presidential material outranks everything except name/year verification. A year whose
president has a rich profile and a portrait beats a year with two extra events.

## President profiles — the full term, not a caption
Every leader can carry a `profile`: a list of paragraphs telling the whole story of their time
in office, as deep as the archive physically allows. What they ran on, the election and its
numbers, what they passed, what failed, what they fought with the administration or the Herald
about, how the term ended, and what the record says happened to them after. Every fact in it
must be traceable to a source already cited in the year's events, documents, or leader sources.

```json
"profile": [
 "Paragraph one. Elected on ... The campaign promised ...",
 "Paragraph two. In office, the Senate under them ...",
 "Paragraph three. The term ended ..."
]
```

Plain past tense. No filler, no praise, no guessing at motive. If the archive is thin, the
profile is short. Short and true beats long and padded.

## Pictures — as many as the archive gives up
Every president should eventually have a portrait, and every year should have photographs.
Image files live in `data/photos/`, named `<year>-<slug>.jpg`. **All photo metadata goes in
`data/photos.json`, never in years.json** — photos have their own file so the photograph
agent and the decade agents never collide. The build merges it in automatically.

`data/photos.json`:
```json
{
 "leaders": [
  {"year": "1989-90", "name": "Amos Gott", "file": "1989-90-amos-gott.jpg",
   "src": {"label": "1990 Talisman, p. 214", "url": "https://digitalcommons.wku.edu/..."}}
 ],
 "years": [
  {"year": "1969-70", "file": "1969-70-registration-line.jpg",
   "caption": "What the photograph shows, one sentence, factual.",
   "src": {"label": "WKU Archives UA1C...", "url": "https://digitalcommons.wku.edu/..."}}
 ]
}
```
The `name` in a leaders entry must exactly match the leader's name in years.json.

Old Herald articles on TopSCHOLAR usually print the subject's name in the caption or the
article text right by the photograph — that is your identification. Quote it in your PR
report as evidence.

Where to hunt, in order:
1. **The Talisman yearbooks** on TopSCHOLAR (`digitalcommons.wku.edu/talisman/`) - every
   yearbook has a student government section with names in the captions. The best source
   for portraits, decade after decade.
2. **WKU Archives photograph collections** on TopSCHOLAR (search `UA1C` image collections).
3. **Herald pages** - the digitised issues are image PDFs; a page with a good photograph
   can be excerpted as an image.
4. **wku.edu/news and wkuherald.com** for the recent decades.

Rules: only images from the university's own open archives or news pages. Always record
`src` with the exact volume and page where you found it. Verify the file is a real image
(JPEG starts with bytes FF D8, PNG with 89 50 4E 47). Never use a photo whose subject you
cannot confirm from the caption or context - a misidentified face is worse than no face.

## Campus context — a high bar, not a catch-all
An event earns a place in this archive one of two ways: SGA did it, decided it, debated it or
was formally part of it; or it is major news that shaped the year for students — September 11,
the 2021 tornado, the COVID shutdown, a university president resigning, a murder trial, a
tuition increase, a campus lockdown.

Capital projects count. New buildings, renovations and the fees that pay for them come
before the Board of Regents, where the student regent sits and votes, so a building opening
belongs in the record as the visible end of a decision students had a seat in.

What does not belong: charity proclamations, ribbon cuttings, awareness days and other
university publicity where SGA neither acted nor voted. An officer being present at something
does not make it SGA's history.

Mark true context events — the second category, where SGA was not the actor — with
`"campus": true`. Never mark SGA's own business as campus context; the tag exists to tell a
reader "this is the world around student government," and it is worthless if it is on
everything.

```json
{"date": "1969-05-01", "title": "...", "body": "...", "campus": true,
 "src": {"label": "...", "url": "..."}}
```

Same rule as everything else: no source, no entry. Campus context should stay the minority of
a year's events — it frames the SGA story, it does not replace it.

## Documents — the actual files, not just links
When a TopSCHOLAR document is central to a year (minutes, a constitution, correspondence,
a Herald issue), download the PDF into `data/documents/`, named `<year>-<what-it-is>.pdf`.
The build copies it into the site so readers get the real file. Attach it to the year:

```json
"documents": [
 {"file": "1974-75-senate-minutes.pdf",
  "title": "Senate minutes, 12 November 1974",
  "summary": "Two or three sentences: what this document is and why it matters.",
  "extract": "A tight paraphrase, or a quote under 15 words, of the part about SGA.",
  "sga_pages": "3-5",
  "page": 3,
  "src": {"label": "TopSCHOLAR UA68/6/1", "url": "https://digitalcommons.wku.edu/..."}}
]
```

- `page` is where the embedded viewer opens. `sga_pages` is the range shown to readers,
  so they know which part of the file is relevant.
- Only mirror files that are openly downloadable from TopSCHOLAR. Always keep `src`
  pointing at the original. Never upload a file that did not come from the archive.

**Mirror the article behind every event where you can.** When the source an event cites is
itself an openly downloadable PDF (a Herald issue on TopSCHOLAR, minutes, a letter), download
it into `data/documents/` and add `"file": "<filename>.pdf"` inside the event's `src` object.
The site then shows a "read it on this site" link next to the citation, so a reader never has
to leave the archive to check a claim. The external `url` stays; the file is in addition.

## The legislation archive
`data/legislation/` holds the actual PDF of every piece of SGA legislation we can get, one
folder per session (`2016-17/`, `governing/`, `undated/`), indexed by `data/legislation.json`:

```json
{"session": "2016-17", "type": "bill",
 "title": "Funding for ...", "file": "2016-17/bill_7-16-f.pdf",
 "source_url": "https://..."}
```

The build renders these into `site/legislation.html` and onto each year's page automatically.

- `scripts/harvest_legislation.py` pulls everything on wku.edu/sga and is rerun each
  semester. Do not duplicate what it already fetched.
- **Older legislation (pre-2011) lives on TopSCHOLAR** in the SGA collection
  (`digitalcommons.wku.edu/sga/`). When your decade's sweep turns up legislation there,
  download the PDF into `data/legislation/<session>/`, add its entry to
  `data/legislation.json` with `source_url` pointing at TopSCHOLAR, and give it a real
  `title` and `type` (bill / resolution). Verify it starts with `%PDF`.
- Missing recent sessions (2013-14 through 2015-16, 2020-21, 2024-25) were never posted on
  wku.edu; they may exist on TopSCHOLAR or in the Wayback Machine
  (`web.archive.org/web/*/wku.edu/sga/*`). Same rules apply.

## The organization — break down the exec and the Senate
Where sources allow, record the whole structure for a year, not just the president:

```json
"organization": {
 "executive": [
  {"office": "President", "name": "...", "note": "...", "src": {"label": "...", "url": "..."}},
  {"office": "Administrative Vice President", "name": "...", "src": {"...": "..."}}
 ],
 "senate": {
  "officers": [{"office": "Speaker of the Senate", "name": "...", "src": {"...": "..."}}],
  "size": 35,
  "committees": [{"name": "Campus Improvements", "chair": "...", "note": "..."}],
  "note": "Anything structural: how many seats, what changed, what the fights were."
 }
}
```

Every field is optional. Same rule as events: no source, no claim.


## Cloud agents: how to land your work - token first, always
The GH_TOKEN in your environment is proven to have full push and pull-request rights.
Do NOT use the platform's GitHub App or proxy git path; it is broken for this repo and
wastes your run complaining about it. Instead, FIRST thing after reading this file:
run `gh auth setup-git` (gh reads GH_TOKEN automatically and becomes git's credential
helper). Then normal `git push` of your research-* branch works, and `gh pr create`
opens your rolling PR if none is open. Never print or write the token anywhere.
If the token path itself fails, put your complete findings - every fact with its
source URL - into your final run report so nothing is lost.
Never abandon verified research because a push was refused, and never push to main.
When GH_TOKEN is absent from your environment, that is a known platform hiccup, not an
access problem the owner can fix: put your findings in the report, describe it in your
summary as "findings preserved in report for the editor," and never phrase it as needing
the user's attention or an admin fix. The next run lands it automatically.

## No tool attribution
This is a university history archive published under its authors' names. Nothing in the
repository or the generated site may advertise the tools used to build it: no
`Co-Authored-By` trailers, no session links, no "generated with" lines in commit messages,
code comments, HTML comments, meta tags, or visible text. Write commit messages in plain
editorial voice describing the history that changed.

## Hard rules
- **Never invent.** No plausible-sounding filler. If a year is thin, it is thin.
- **Every event needs a `src`.** No source, no entry.
- **Quote under 15 words, once per source, maximum.** Paraphrase and link. This is a public site
  reusing a university archive and a student newspaper; do not reproduce their text.
- **Do not merge people by name.** Two people can share a name. Verify before claiming a later career.
- **Flag, do not fix, spelling doubts.** `Hargroave` and `Keyanna`/`Keyana` are unverified.
- **Living people.** Some entries touch resignations, investigations and conduct cases. Report only
  what a cited source reported, name no accusers who were not named publicly, and state outcomes
  where they exist. If a source only covers an allegation and never a resolution, say so.
- Run `python3 scripts/build.py` before finishing. Report what you could not confirm.

## Scope per session
One decade at a time. Do not attempt the whole sixty years in one run.
