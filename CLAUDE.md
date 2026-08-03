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
