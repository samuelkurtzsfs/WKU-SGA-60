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
