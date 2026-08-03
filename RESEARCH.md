# SGA 60 — research method

The site has 61 year pages. Four are researched, 20 are started, 37 are empty. This is how to fill them.

Edit `data/years.json`, run `python3 scripts/build.py`, push. Nothing in `site/` is hand-edited.

---

## Order of work

**A. Verify names and years.** Nothing else is worth doing until the spine is right — people have
reported the plaque has them in the wrong year, and 25 leader entries are already flagged as
role-unresolved or year-ambiguous. On the site these show a red `?`.

**B. Sweep each year.** Everything SGA-related that year, chronological, sourced.

**C. Testimony.** The only part with a clock on it.

---

## A. Verifying a name and a year

Every year page has the searches pre-built in the sidebar. For each leader:

1. **Name + SGA terms on TopSCHOLAR.** The keyword set is
   `"student government association"`, `"associated student government"`, `"student government"`,
   `SGA`, `ASG`, `"student regent"`.
2. **Read the dates on the hits.** Election coverage runs every April; installation coverage runs
   every spring. Those two pin a term precisely.
3. **Decide:**

   | What you found | What to do |
   |---|---|
   | Name in the plaque year | `"name_verified": true`, add source |
   | Name consistently in a different year, within a year or two | move the leader object to that year, set `"year_confidence": "corrected"`, explain in `note` |
   | Role stated (president / student regent) | set `role` |
   | Nothing | leave it false and move on |

**Record every correction in the note.** `"Plaque reads 1974-75; Herald coverage places this term in
1975-76."` A history project that quietly edits its own primary source is worse than one with an
error in it.

### The one question that unlocks 18 entries
The plaque does not distinguish presidents from student regents, and 18 plates share a year with
another name. The overlaps: 1968–70, 1970–71, 1972–73, 1974–75, 1982 (three names), 2006, 2007–09, 2014.

Two explanations, not mutually exclusive: mid-year successions, or a separately elected student
regent from before the offices merged. WKU began lobbying Frankfort for a student regent seat in
February 1968, which is exactly when the pairs start.

Settle it at: the 1966 constitution and 1969 minutes (`digitalcommons.wku.edu/sga/`), Board of
Regents minutes for the first year a student appears (`digitalcommons.wku.edu/bor/`), the legislative
history of KRS 164.321, or one email to `archives@wku.edu`. The email is fastest.

---

## B. Sweeping a year

Twelve searches per year page, already built into the sidebar: six keywords against each of the two
calendar years. The *Herald* on TopSCHOLAR is indexed article by article, so a keyword-plus-year
search returns the specific issues.

**Log everything the organisation did, not just the president.** Resolutions and what happened to
them. Election results and turnout numbers. Budget fights. Committee formations. Appointments.
Things that failed. Editorials attacking it. This is a history of a body, not a series of
personal highlight reels.

Entry format:

```json
{"date":"1975-04-16",
 "title":"Short factual headline",
 "body":"Two or three sentences. What happened and why it mattered.",
 "src":{"label":"Herald 51:39, 25 Feb 1972","url":"https://digitalcommons.wku.edu/..."}}
```

Dates are `YYYY-MM-DD`. Month only → `-01`. Year only → `YYYY-01-01`. Sorting happens at build time.

### Where the material is thick and thin
- **1966–1979** — richest and hardest. Herald indexes are detailed, the politics are real, and none
  of it is full-text searchable in the modern sense.
- **1980–1995** — thinner. Committee minutes and organisation charts more than headlines.
- **1996–2003** — outgoing letters survive; the Herald archive online starts around 2003.
- **2004–present** — mostly already online and quick.

Budget accordingly. The 1970s are worth twice the time of the 2010s.

---

## C. Testimony

The archive will still be there in twenty years. Jim Haynes was elected sixty years ago.

- Start with the least-documented and oldest cohort: the 1970s and 1980s.
- Donald Smith (1993–94) is president of the College Heights Foundation and has already spoken to
  the *Herald*. Easy first call, and a route to older alumni.
- Three questions, not twenty: what you ran on, what you actually got done, what you would tell the
  person holding the job now.
- Record audio, get a written release, deposit copies with WKU Archives so it outlives the anniversary.

---

## Standards

- Never invent. An empty year is information.
- Every event carries a source URL. The CI build fails without one.
- Quotes under 15 words, once per source. Paraphrase and link — this reuses a university archive and
  a student newspaper.
- Do not merge two people because they share a name.
- On resignations, investigations and conduct cases: report only what a cited source reported, and
  state the outcome. Where a source covers an allegation but never a resolution, say that plainly.
