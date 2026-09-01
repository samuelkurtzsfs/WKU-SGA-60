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

The same goes for **every later list**: the plaque, the history page on wku.edu/sga, the officer
lists on the old SGA website, any banquet programme. These were all compiled after the fact, they
all carry one name per year, and they all drop the people who held the office for part of a year.
A contemporaneous source beats a later list every time. In order: SGA's own minutes recording a
resignation or a swearing-in, Board of Regents minutes naming who sat in the student seat, a
*Herald* report from the week it happened. Only then a list.

## Who counts as a student body president
**Anyone who held the office, for any length of time, by any route.** Elected in April and served
the year; won a special election; succeeded to it as vice president when the president left; or
filled it in an acting capacity. **Duration is not a qualification. A week counts.** Someone who
served eleven days between a resignation and a successor being sworn in was the student body
president, and belongs on the list with everyone else.

A person is counted **once**, at the first time they held the office, however many terms they serve
later. Two plates for one person is not two presidents: check for a changed surname before adding
anyone. Known cases in this record are Christy Vogt / Christy Mollozzi, Janet "Nicki" Seay / Nicki
Taylor, Amanda Coates / Amanda Lich, and James Hargrove / James Hargroave.

Because SGA elects in April and the winner serves the next academic year, the test for a missing
president is simple: find who the sources name as president in the **fall**, then again late in the
following **spring**. If they differ, someone is missing. Mark an acting officeholder with
`"acting": true`, and record whether they also held the Board seat with `"also_regent"`.

## Settled facts — do not re-litigate these
- The student regent was a **separately elected office** from April 1968. That is why plaque years
  carry two names. William Menser was the first, April 1968. The seat was non-voting until at least 1972.
- Confirmed regents rather than presidents: Michael Fiorella 1972-73, Gregory McKinney 1974-75
  (first African American student regent), Sandra Norfleet **1981-82**.
- **Sandra Norfleet is 1981-82, not 1982-83.** The plaque reads 1982 and this file said
  1982-83 until 18 August 2026. The *Herald* puts the whole term inside 1981-82: no majority
  in the vote of 9 February 1982, Norfleet won the runoff on 16 February, and 15 April 1982
  carried "Student Regent's 2-Month Term Nears End" (Herald 57:55,
  digitalcommons.wku.edu/dlsc_ua_records/2464). Who held the seat earlier that year, before
  what the paper called the first campus-wide election for it, is not established. Do not
  file her forward again.
- By ~2001 the offices merged. After that, a second name in a year is a mid-year succession.
- **The 1974-75 Tom LaCivita portrait is correctly identified. Do not withdraw it again.**
  The brick-wall photograph in the left column of p. 109 of the 1975 *Talisman* was cut on
  25 August 2026 as uncaptioned and restored on 27 August, so the reasoning for cutting it is
  still in the history where a later pass can act on it. Checked against the page image itself
  on 28 August (archive.org/details/talisman1975west, scan leaf n112): the frame carries a
  second person at its left edge, a hand and forearm on the document the visible man is
  holding. The caption naming LaCivita "(right)" with treasurer Ricky Johnson therefore
  describes this photograph, and Johnson is the figure cropped out of the printed frame. The
  withdrawal read the caption onto the stairway picture above it and was wrong.
- **Reed Morgan was not a student body president, and did not hold the regent seat.** Settled
  28 August 2026, and settled on positive evidence rather than on his absence from the record.
  Both offices in 1968-69 are occupied by other people, each confirmed contemporaneously:
  Straeffer won the presidency on 2 May 1968 by 1,732 to 1,098 (Beck's results memo of 3 May,
  reported in the *Herald* of 9 May), and Gerard held the regent seat (Bruce Tucker's profile
  of him as student regent, *Herald* 48:19, 27 Feb 1969). There is no vacancy for a third
  officeholder. He had also already graduated: the *Herald* of 7 April 1966 calls him a
  senior, "Senior Triples as Greek Editor, Debater, Government Chairman", so the
  returning-graduate-student theory is moot. His plate honours his chairmanship of the
  committee that wrote the constitution, which Kelly Thompson's approval letter of 1 April
  1966 addresses to him by name. Why it reads 1968 and not 1966 is still not established, and
  is not worth guessing at. Do not reopen the presidency question without a source that puts
  him in an office.
- **Carlene Lodmell and Darlene Lodmell are two different people.** Their names differ by one
  letter and any name-similarity check flags them as one person spelled two ways. They are not.
  They held office side by side: in 1995-96 Darlene chaired Student Affairs while Carlene chaired
  Legislative Research, and in 1996-97 Carlene was Vice President while Darlene was Secretary
  (SGA minutes of 14 Nov 1995, 5 Mar 1996, 27 Aug 1996 and 22 Apr 1997). Confirmed independently
  against the university's own records, 1 September 2026. Never merge them, and never let a
  portrait of one attach to the other.
- Still open: John Lyne vs Larry Zielke 1970-71, David Payne 1982-83.

## Search locally before you crawl
`data/herald-index-full.json` covers the whole digitised collection with no keyword filter:
11,850 items and 17,601 index lines, 1875 to 2026. Grep it first. It answers most "was X
president that spring" questions in a second and costs TopSCHOLAR nothing.
Rebuild with `python3 scripts/harvest_herald_index.py --all` (about 35 minutes, paced).

**But it is not complete, and a miss in it proves nothing.** Every stored line is cut at 300
characters; 5,892 of the 17,601 lines (a third) sit exactly at that cap, truncated mid-headline.
A *Herald* issue page lists thirty or more articles in one abstract, so what survives locally is
usually the first two or three. Checked on 18 August 2026: the 14 April 1994 issue
(`dlsc_ua_records/7878`) keeps one headline locally out of the thirty-seven the landing page
actually carries — and the one that matters, the SGA election story, is among the thirty-six cut.
So: a **hit** in this file is good evidence. A **miss** is not evidence of absence, and must never
be the grounds for cutting a claim or writing "no source found". Open the issue's landing page
before you conclude anything negative.

`data/herald-index.json` is the filtered subset the site renders and is **not** a research tool:
it keeps only issues whose index mentions student government, so anyone named in a headline that
does not say SGA, ASG or student government is invisible in it.

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
- **Flag, do not fix, spelling doubts.** `Keyanna`/`Keyana` is still unverified. `Hargroave`,
  `Mollozzi` and `Marcell` are settled: the Herald and SGA's own 2001 roster of former
  presidents give Hargrove, Vogt and Marcel, and the site follows them with the plaque printed beside.
- **Living people.** Some entries touch resignations, investigations and conduct cases. Report only
  what a cited source reported, name no accusers who were not named publicly, and state outcomes
  where they exist. If a source only covers an allegation and never a resolution, say so.
- **Do not write an event up twice.** Successive passes have described the same event in
  different words, and matching whole titles never catches it. Before you add to a year, read
  the entries already in it. After any merge run `python3 scripts/check_duplicates.py`, which
  compares the words in titles and prints close pairs. It only reports; you judge. Same-day
  legislative business is genuinely several events, so three bills introduced on 1 September
  stay three entries. When two entries really are one event, combine them so that no sourced
  fact from either is lost, and cite both sources if they differ.
- **An advance notice is not a report.** The digitised *Herald* index is full of items like
  "Mini-Concert Set Thursday", printed before the event. It proves what was booked, never how
  the night went. Do not write a crowd size, a review or a financial result out of one. The
  following week's issue often carries the actual report, and the *Talisman* full texts on
  archive.org are readable as plain text and are not rate limited.
- Run `python3 scripts/build.py` before finishing. Report what you could not confirm.

## Scope per session
One decade at a time. Do not attempt the whole sixty years in one run.
