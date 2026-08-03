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
Image files live in `data/photos/`, named `<year>-<slug>.jpg`; the build copies them into
the site.

A leader's portrait:
```json
"photo": {"file": "1989-90-amos-gott.jpg",
          "src": {"label": "1990 Talisman, p. 214", "url": "https://digitalcommons.wku.edu/..."}}
```

A year's photographs, in the year object:
```json
"photos": [
 {"file": "1969-70-registration-line.jpg",
  "caption": "What the photograph shows, one sentence, factual.",
  "src": {"label": "WKU Archives UA1C...", "url": "https://digitalcommons.wku.edu/..."}}
]
```

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

## Campus context — the year around SGA
Major campus events that shaped the year belong in the record even when SGA was not the actor:
a president hired or fired, a building opened, a protest, a tuition hike, an enrollment shock.
Mark them with `"campus": true` in the event and they render with a campus tag:

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
