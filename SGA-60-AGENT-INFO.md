# SGA 60 — agent handoff

Everything a new Claude Code session needs to pick this project up cold. Read
`CLAUDE.md` first for the editorial rules; this file is about the machinery, the
research method, and what is left to do.

Last updated 20 August 2026, at the close of the 48-hour research push.

---

## 1. What this is

A public history of the WKU Student Government Association, 1966–2026, built for
the 60th anniversary. Static site, pure Python, no dependencies at build time.

- **Repo:** `samuelkurtzsfs/WKU-SGA-60`, branch `main`. Local: `/Users/samkurtz/Downloads/sga60`.
- **Deploy:** Vercel, git-connected, builds on push with `python3 scripts/build.py`.
  Do **not** drag-and-drop: the built site exceeds Hobby's 100MB upload limit.
- **Edit `data/`, never `site/`.** `site/` is generated. Run `python3 scripts/build.py`
  after every change.

### Where the numbers stand

Measured on `main` at commit `117647c`, 20 August 2026, after
`python3 scripts/build.py`. The right-hand column is where the 48-hour push
started, on 17 August, so the two can be read against each other.

| | now | 17 Aug |
|---|---|---|
| academic years | 61 (1966-67 → 2026-27) | 61 |
| dated, sourced entries | 2,025 | 1,877 |
| programmes (things SGA put on) | 633 | 633 |
| people who were president | 60 | 60 |
| people who held the student regent seat | 57 | 57 |
| people recorded in any office | 1,503 | 806 |
| leader records | 73 | 73 |
| cabinet and senate **officer** records | 1,064 | 1,045 (6 Aug figure) |
| senate **member** records | 912, across 35 years | 0 |
| years with a cabinet recorded | 58 of 61 | 58 |
| people whose record carries a written profile | 261 (279 records) | 73 |
| photographs held | 113 files | 61 |
| — of which leader portraits / year photographs | 73 / 45 entries | — |
| years with a leader portrait | 61 of 61 | not recorded |
| years with a year photograph | 32 of 61 | — |
| documents mirrored and referenced | 246 | 34 |
| legislation PDFs held | 827 | 390 |
| authorship attributions from those PDFs | 1,038 | 918 |
| total pages built | 1,587 | 867 |
| complete Herald article index | 11,850 items / 17,601 lines | same |

Two of those rows need reading carefully. **People recorded in any office**
counts the person pages the build actually writes (`site/o/`); the raw name
strings in `data/years.json` number 1,547, and the gap is `name-aliases.json`
folding spellings together. The count nearly doubled in the push because the
senate rolls arrived, and a rank-and-file senator recorded once from a roll call
is a much thinner record than a profiled officer — do not read 1,503 as 1,503
biographies. **Written profiles** counts any record carrying a `profile` array,
leader or officer; every president and every student regent has one, and the
other 195 are cabinet and senate officers.

**Sam Kurtz is the 58th president** and the 55th student regent. Caden Lucas is
the 60th and 57th. Sixty years of student government span 61 academic years
because the constitution was ratified in April 1966, so 2025-26 is the sixtieth
year and 2026-27 is the one now running.

---

## 2. The scripts, and what each is for

| script | what it does |
|---|---|
| `build.py` | The only presentation file. Generates all 1,587 pages. Runs `check_data.py` at the end and shouts if the record broke its own rules. |
| `check_data.py` | Validates `data/years.json` against the archive's own rules. **Exit 1 on any problem, so it can gate a deploy.** Checks dates, sources, duplicate titles, roles, file integrity by magic bytes, photo overlay attachment, status consistency. |
| `check_duplicates.py` | Reports events in one year that look like the same event written twice. Reports only; you judge. Same-day bills are genuinely separate events. |
| `harvest_herald_index.py` | OAI-PMH sweep of the digitised collection. `--all` keeps **everything** into `data/herald-index-full.json`; without it, only student-government lines into `data/herald-index.json`. |
| `extract_authors.py` | Reads AUTHOR/SPONSOR lines off the 827 legislation PDFs with PyMuPDF. Deliberately unmodified: its "read past CONTACT" behaviour is wrong on pre-2011 forms and right on 2016-and-later ones, so the pre-2011 yield is curated by hand instead. |
| `harvest_topscholar_legislation.py` | Pulls SGA legislation off TopSCHOLAR. Carries a shared cookie jar and sends the item page as `Referer`, which is what makes `viewcontent.cgi` answer at all. **Its listing regex only matches `class="dtstart"` exactly and silently skips rows printed as `class="dtstart visually-hidden"` — see §8.3 item 9. Use `harvest_missing_legislation.py` (or fix this one) rather than trusting a clean run of this script alone.** |
| `harvest_missing_legislation.py` | Companion to the script above: parses the same listings by `<tr class="vevent">` block instead of the date span, so it catches both `dtstart` forms. Diffs against `data/legislation.json` by `source_url` and fetches only what is missing. Same pacing. |
| `merge_programs.py` | Merges programmes and plain events into years. Enforces the dating law. |
| `merge_officers.py` | Merges cabinet and senate officers into `organization`. |
| `merge_senators.py` | Merges rank-and-file members into `organization.senate.members`. |
| `merge_fillins.py` | Merges presidents who took office mid-year. |
| `merge_research.py`, `apply_repairs.py`, `apply_dedupe.py` | Older merge paths for specific passes. |
| `attach_pdfs.py` | Joins download URLs from the Herald harvest onto citations. |
| `harvest_legislation.py` | Scrapes wku.edu/sga. Rerun each semester. |

---

## 3. The data model

`data/years.json` is the single source of truth. One object per academic year:

```jsonc
{
  "id": "2023-24", "start": 2023, "org": "Student Government Association",
  "status": "researched",              // researched ≥3 events, partial 1–2, empty 0
  "leaders": [{
    "name": "Sam Kurtz", "role": "president",   // president | regent | unresolved
    "also_regent": true,               // STATE it when a year has >1 name; never infer
    "acting": false,                   // filled the office without being elected
    "year_confidence": "confirmed",    // confirmed | corrected | likely | stated | ambiguous
    "missing_from_plaque": false,
    "note": "...", "profile": ["para", "para"], "sources": [{"label","url"}]
  }],
  "events": [{
    "date": "2023-09-20",              // day 01 = day unknown; 01-01 = year only
    "title": "...", "body": "...",
    "kind": "concert",                 // presence of `kind` makes it a programme
    "money": "free to students; crowd of 7,500",
    "campus": true,                    // context event SGA did not do; keep rare
    "src": {"label","url","pdf","file"}, "src2": {...}
  }],
  "organization": {
    "executive": [{"office","name","note","src"}],
    "senate": {"officers": [...], "members": [...], "size": 35, "committees": [...]}
  },
  "documents": [...]
}
```

Side files: `data/photos.json` (overlay, keyed by name+year),
`data/name-aliases.json` (one person spelled several ways),
`data/legislation.json` + `data/legislation/`, `data/legislation-authors.json`,
`data/herald-index.json` (filtered, drives the site),
`data/herald-index-full.json` (complete, for research).

---

## 4. Sources, and how to actually reach them

**Search locally before crawling.** `data/herald-index-full.json` answers most
"when did X happen" questions in a second and costs nothing.

| source | notes |
|---|---|
| **SGA minutes** `digitalcommons.wku.edu/sga/Meetings/Minutes/` | ~830 items 1969–2008. **The roll.** Names who presided and who attended. Best source for officers and members. |
| **Digitised Herald** `digitalcommons.wku.edu/dlsc_ua_records/` | Item pages list every headline in an issue. Thins out after 2004. |
| **Talisman yearbooks** `archive.org/download/talisman<YEAR>west/talisman<YEAR>west_djvu.txt` | Plain text, **not rate limited, use heavily.** archive.org holds 1971–1981, 1986, 1987. It does **not** hold 1967–1970 or 1982–1985. |
| **wkuherald.com** | Full text from ~2003. WordPress API: `/wp-json/wp/v2/posts?search=SGA&per_page=100`. |
| **Wayback** over `wku.edu/Dept/Org/Student/SGA` | Officer pages ~1997–2010. `formersgapres.htm` is SGA's own numbered presidents roster (archived 24 Sep 2001). **`web.archive.org` is blocked outright from the cloud containers — see §8.1.** |
| **Local legislation** `data/legislation/` | 827 PDFs, 1,038 curated authorship attributions. Free, and needs no network. |

### Access gotchas that cost real time

- **digitalcommons pacing rule:** one request at a time, 3 seconds apart, 90s
  backoff on 403. Bot protection triggers on burst volume. A slow crawl gets
  everything; a fast one gets nothing.
- **digitalcommons PDFs need browser navigation headers** or they return an
  empty HTTP 202: `Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`,
  `Upgrade-Insecure-Requests: 1`.
- **wkuherald.com needs a full browser User-Agent.** A bare `Mozilla/5.0` gets 403.
- **`pdftotext` is NOT installed here.** Use PyMuPDF (`import fitz`), which is.

---

## 5. The research pattern that works

One **researcher** chained to an **adversarial verifier**, per era, in a
`Workflow` pipeline. Never publish unverified research.

```js
await pipeline(ERAS,
  (e) => agent(researchPrompt(e), {schema: FOUND, phase: 'Research'}),
  (found, e) => agent(checkPrompt(found, e), {schema: CHECKED, phase: 'Check'})
                  .then(c => ({found, checked: c})))
```

**Give the verifier a `trim` verdict, not just accept/reject.** About a third of
good findings are real but over-claimed, and trimming keeps them.

### Track record of the verifiers

- 457 programmes → 58 rejected, then 49 of those rescued by rewriting.
- 361 thin-year entries → 106 trimmed, 4 refused.
- 665 officers → 87 notes cut back, 94 refused.
- 39 claimed "missing presidents" → **0 survived.** All were vice presidents or
  committee chairs promoted by accident.
- 15 branch histories → **every single one needed correction** before publishing.

That last line is the argument for never skipping the checker.

---

## 6. Traps. Read this section before researching anything.

1. **An advance notice is not a report.** The Herald index is full of items like
   "Mini-Concert Set Thursday", printed *before* the event. It proves what was
   booked, never how the night went. Do not write a crowd size, a review or a
   financial result out of one. The following week's issue usually has the report.
2. **A committee chair is not an officer. A bill's author is not necessarily a
   member.** This is the single commonest error and it killed all 39 "missing
   president" claims.
3. **A changed surname is not a new president.** Known cases: Christy Vogt /
   Mollozzi, Janet "Nicki" Seay / Nicki Taylor, Amanda Coates / Lich, Steven
   Donte' Reed / Donté Reed.
4. **Never match a person by surname alone.** It puts every residence hall on a
   Hall's page and every phone line on a Line's. Surname matching would have
   added 88 pairings and attributed a reporter's articles to an officer.
5. **Spring elections file forward.** SGA elects in April; the winner serves the
   *following* academic year. An April 1994 result belongs to 1994-95.
6. **Read the article, not the headline.** A page was published claiming Margaret
   Ragan did not hold the Board seat, on the strength of a headline. She did.
7. **Scripts that report success while producing nothing.** This has happened
   four times: the harvester wrote an empty file and printed "done"; an agent's
   35-minute harvest was never saved; a blocked download saved the bot-check
   HTML page under a `.pdf` name; and `pdftotext` failed silently so the
   legislation looked authorless for a day. `check_data.py` catches the data-side
   versions. **Verify output exists and is what it claims.**
8. **Workflow post-processing is unchecked code.** One workflow built the item
   list for its checkers and never interpolated it into the prompt; 361 findings
   were dropped as unverified. Confirm the list actually reaches the prompt.

---

## 7. Settled — do not re-litigate

- **Sam Kurtz is the 58th president.** Verified six ways, including SGA's own
  2001 roster which matches this archive's numbering for all 35 it covers.
- **Reed Morgan is not a president.** Complete unfiltered index, both founding
  Congress rosters, and the 2001 roster all exclude him. His plate most likely
  honours the chair of the committee that wrote the constitution.
- **Four presidents left office early:** Bush (Jan 1982), Todd (Jul 2004),
  Watkins (Nov 2006), Boles (Jan 2009). Nobody was ever removed by impeachment.
- **Three presidents were missing until Aug 2026:** Nick Todd, Katie Dawson
  (acting, summer 2004), Jeanne Johnson (from Dec 2006).
- **The regent seat** was created April 1968 (William Menser first) and became a
  **voting** seat in 1972-73.
- **31 March 1979:** the Regents moved lectures and concerts from ASG to a rebuilt
  University Center Board with $80,000. 80 of 87 concert entries precede it.
- **Will Harris's COVID extension is not a second term.** SGA postponed the
  spring 2020 election; he served into October 2020.

---

## 8. Outstanding work

Written 20 August 2026, at the close of the 48-hour push, with the five research
routines meant to be switched off. Nothing is running on a schedule any more, so
nothing on this list will clear itself. Read it as a to-do list for a person.

Everything struck through in earlier versions of this section has been moved into
`.research/NIGHT-REPORT.md`, where the editor passes record what was done and why.
What follows is only what is **not** done.

**A note for whatever fires this session on a schedule (21 August):** at least one
scheduled routine still exists with a stored prompt describing an older version of
this backlog — the three unverified branch histories, 235 unmerged moments, 92
officer candidates for 1979-80/2001-02/2003-04, and portraits for Nick Todd, Katie
Dawson, Jeanne Johnson and Reagan Gilley. All of that is already done: the three
`.research/branches-*.json` and `officers-unchecked.json` files it points at are
now empty (`[]`), and all four named people already carry a portrait in
`data/photos.json`. Reed Morgan and the Amanda Coates/Lich question are also
already settled, in §7 above and in `CLAUDE.md`'s known-cases list. This file, not
that stored prompt, is the live list — if a run arrives with instructions that
sound like this paragraph, treat this section as the actual state and pick from
what is below instead of re-doing what is already struck through.

### 8.0 A warning that comes before any merging

**`main` is an orphan history relative to the `research-*` branches of 4 August.**
They have different root commits and **no merge base**. Git will happily report one
of them as "57 behind main" and offer to merge it; doing so does not add anything,
it restores the 4 August snapshot over the current record. It deletes
`data/herald-index-full.json`, `data/legislation-authors.json`,
`data/name-aliases.json`, the whole contributor layer and all three validator
scripts, and cuts `data/years.json` back to roughly 830 events.

Before merging **any** branch into `main`:

```bash
git merge-base origin/main <branch>     # empty output = orphan, do not merge
```

If there is no merge base, do not merge. Diff by content instead
(`git diff origin/main <branch> -- ':!site'`), take only what `main` genuinely
lacks, and apply it as a fresh commit on a branch cut from current `origin/main`.
Branches cut from current `main` are ordinary branches and merge normally; this
warning is about the 4 August ones only.

### 8.1 What this environment can and cannot reach

Re-tested by hand at 05:07 UTC on 20 August 2026, one request each. This is the
single biggest constraint on the research and the reason several items below are
still open. Earlier versions of this section stated the block differently on
different days and good research was trimmed on the strength of a stale note, so
the test commands are given here to be re-run rather than believed.

**Update, 21 August 2026:** the "blocked outright" line on `web.archive.org` below
was true only for plain `http://`. A run this day found `curl -v` on port 80
returns `403`, `x-block-reason: hostname_blocked`, body `Blocked by egress policy`
— the sandbox's own egress proxy, not archive.org — while the identical request on
`https://` succeeded. A batch fetch of all 107 unique `web.archive.org` URLs cited
in `data/years.json` over `https://` got real pages back for 82 on the first pass;
the rest were a transient "Internet Archive: Temporarily Offline" 503 that cleared
on retry (a handful of specific captures, e.g. the `formersgapres.htm` and
`wkuherald.com/tag/sga/` snapshots, needed two or three retries a few seconds
apart before succeeding; the editor's check the same night got four straight 503s
on `formersgapres.htm` and gave up on it, so budget more retries than two or three
and treat a run of them as normal — genuinely flaky on archive.org's side, not this
environment's). **Every stored citation using `http://web.archive.org` was
switched to `https://` in this run** (90 occurrences; content and captures are
identical, `https` just isn't egress-blocked here). Re-test with `https://`, not
`http://`, before trusting a "blocked" verdict on this host again.

| host | state | note |
|---|---|---|
| `digitalcommons.wku.edu` **landing pages** | **open**, 200 | titles, dates, one-line abstracts and a Herald issue's headline index. This is how most citation labels get verified. |
| `digitalcommons.wku.edu/cgi/viewcontent.cgi` | **blocked**, HTTP 202, empty body, `x-amzn-waf-action: challenge` | every PDF: Herald page images, Talisman pages, minutes, legislation. Confirmed still challenging on 21 August: 5 retries over 7.5 minutes on two different SGA-minutes items, all 202. **Open again midday 22 August (a later scheduled run):** three Talisman PDFs (68–195 MB each) fetched clean with a plain `curl`, no special headers, no cookie dance. Confirms the earlier finding — this challenge lifts and re-closes by the hour, keep trying rather than treating one 202 as final. |
| `web.archive.org` | **Blocked again, midday 22 August (a later scheduled run) — contradicts the 21 August "open on https" note above.** Every attempt, from the main session and from six independent subagents, reset at the TLS handshake before any HTTP response (`curl: (35) Recv failure: Connection reset by peer`); one subagent that tried a direct (non-proxied) connection got an explicit `403 x-block-reason: hostname_blocked`. `archive.org` (no `web.` prefix) and every other host tested worked fine through the same proxy at the same time, so this is specific to the `web.archive.org` hostname, not a general outage. Re-test before believing either verdict — this has now flipped at least twice in 48 hours. | The ~90-URL fact-check of article-permalink Wayback citations planned for this pass (see §8.3 item 4) could not be run at all as a result — 84 unique URLs, six parallel verifier agents, zero fetched. Nothing in `years.json` was touched because of this; an unreachable source is not evidence against a claim. |
| `archive.org` (no `web.` prefix) | **open** | Talisman full texts, 1971–1981, 1986, 1987. Not rate limited. Use heavily. |
| `wkuherald.com` | **open**, 200, but its live WordPress search (`/wp-json/wp/v2/posts?search=`) returns nothing for anything before roughly 2011 — the old College Publisher-era site (2003–2010) was never migrated into it, so pre-2011 stories only survive via Wayback, not the live site. |

On `viewcontent.cgi`: on 19 August a run got real PDFs out of it by landing on the
item page first and then requesting the file with that cookie, a `Referer` back at
the item page, and the `Sec-Fetch-*` / `Upgrade-Insecure-Requests` headers a
browser sends. That is how the 437 pre-2011 legislation PDFs were pulled down. The
same recipe, headers and all, returns the WAF challenge again today. So it is a
challenge that sometimes lifts, not a permanent wall and not a burst-rate 403 that
patience cures. Try it; if it challenges, work from landing pages and say so in
the write-up rather than writing around it.

The rule this environment keeps proving: **a source you could not open is not a
source that says nothing.** Do not cut a claim because you were blocked. Flag it.

### 8.2 Branches, and what is still unmerged

```bash
git ls-remote --heads origin
git rev-list --left-right --count origin/main...origin/<branch>
```

**As of the 21 August overnight pass, no pull request was open; PR #109 (`research-backlog`)
is now open again, from the scheduled run later that day** (the Eaton alias fix and the
1979-80/1992-93 access notes above). All four branches that were open the previous night —
`research-backlog` (#80), `research-photos` (#81),
`research-profiles` (#82) and `research-senate` (#83) — were reviewed and merged,
each after a correction. The reasoning is in `.research/NIGHT-REPORT.md` under
21 August.

- `research-backlog`, `research-photos`, `research-profiles`, `research-senate` —
  fully merged into `main`, nothing outstanding on any of them. All four cut
  cleanly from current `main`, so none was an orphan.
- **`research-2020s` — unmerged, and it must stay that way.** This is a 4 August
  orphan (see 8.0). No merge base with `main`. 57 commits that are not on `main`
  and cannot be merged onto it. Leave it, or close it, but do not merge it.
- The other 4 August `research-*` branches (`research-1966-79`, `research-1980s`,
  `research-1990s`, `research-2000s`, `research-2010s`) are orphans of the same
  vintage. Check `git merge-base` before touching any of them.

### 8.3 Research still owed, highest value first

1. ~~The three years with no cabinet at all: 1979-80, 2001-02, 2003-04.~~
   **All three done, 22 August (scheduled run) — 1979-80 was the last.**
   2003-04 and 2001-02 were already done, as below. For 1979-80,
   `viewcontent.cgi` was open (plain requests, no special headers) around
   00:25–00:40 UTC on 22 August, and the earlier "no AVP, Secretary or
   Treasurer is named anywhere reachable" conclusion turned out to be wrong —
   not because the officers weren't covered, but because the coverage isn't in
   the issue's own abstract on its TopSCHOLAR landing page, only in the PDF
   itself, which no prior pass had actually opened for this specific issue.
   Herald 54:56 (19 Apr 1979)'s front page, in a third column the abstract
   doesn't index at all, reports Jamie Hargrove's win (1,087-535 over David
   Young, 1,725 votes) *and* the three other executive races: Steve Fuller
   administrative vice president (973-574 over Tom Jecker), Dean Bates
   activities vice president (785-761 over Ben Bratcher, the closest of the
   four), Betty Thompson secretary (1,052-517 over Lynn Driver) and Terri
   Craig treasurer (937-623 over Darell Pierce, continued on p.7). Herald
   54:57 (26 Apr 1979) then names all five by office as they were sworn in at
   the 24 April meeting, and SGA's own minutes of that same meeting — already
   mirrored locally as `1978-79-asg-minutes-1979-04-24.pdf` — independently
   corroborate all four by what they did that night (Fuller on committees,
   Bates on the Center Board, Craig on the budget, and Thompson's own
   signature as secretary). This is exactly the four names an earlier pass
   (`.research/officers-checked.json`) had found and then rejected, because
   the verifier at the time could only see the same incomplete abstract and
   couldn't confirm them — a case of CLAUDE.md's own warning about the local
   index, not a wrong finding. A separate adversarial verifier this run
   independently re-read all three documents at high resolution and confirmed
   every name, race and number; it also caught an unrelated pre-existing
   "70 candidates signing up for offices" clause on the neighbouring
   1978-79 event that traced to no source in either issue, which was cut.
   Landed on `research-backlog`: `organization.executive` for 1979-80, a new
   24 April swearing-in event, Hargrove's profile rewritten around the primary
   record, two Herald issues mirrored into `data/documents/`, and two pairs of
   near-duplicate spring-1979 entries in 1978-79 merged. Nothing further is
   owed here; the 1979-80 cabinet is as complete as the surviving record allows.
2. ~~Twenty-six sets of 1996-97 minutes are mirrored into `data/documents/` and
   referenced by nothing~~ **Done, 20 August.** All 29 files (27 Congress
   meetings, 2 Executive Council) now carry a title, a summary, a sourced
   extract and a TopSCHOLAR link, verified against the PDF text by a separate
   adversarial pass (22 accepted as drafted, 7 trimmed for overclaiming, 0
   rejected). Landed on `research-backlog`.
3. **The rest of the senate rolls.** 1,184 member records across 52 years is a good
   start on a 61-year record and no more than that. SGA's own minutes are the
   roll, roughly 830 items covering 1969–2008 on TopSCHOLAR, and the method that
   worked is in `scripts/merge_senators.py` and in the 20 August night report:
   mirror the year's minutes locally first, then check every name against the
   primary text with no network requests at all.

   **The TopSCHOLAR collection stopping in December 2008 is not the end of the
   evidence (found 21 August).** SGA's own website still serves its Senate minutes
   past that cutoff, and no pass before 21 August had looked there:

   | path | covers | formats |
   |---|---|---|
   | `wku.edu/sga/uploads/minutes/` | 2009-10 through 2014-15 (subfoldered `/2010/`, `/2011/`, `/2012/`, `/2014/`) | `.doc`, `.docx` |
   | `wku.edu/sga/2018-2019-legislative/minutes.php` and `/minutes/`, `/fa20/` | 2020-21 | `.pdf` |
   | `wku.edu/sga/2024_2025_legislative/senate_minutes/` | 2024-25 | `.docx` |

   The host is open and needs no special headers, only a browser User-Agent.
   `antiword` and `catdoc` are **not** installed by default but
   `apt-get install -y antiword catdoc` works; `.docx` is a zip of
   `word/document.xml`; PyMuPDF handles the PDFs.

   These minutes are far richer than a roll: they carry swearing-ins, roll-call
   votes, absence lists by full name, and in the 2024-25 files the full text of
   each bill with its authors and their seats. Three cautions learned the hard way
   on the 21 August pass. **Blanket votes come in pairs** — a Student Senate
   confirmation and an Organizational Aid Board confirmation can sit a few lines
   apart, and reading the wrong one puts seven non-senators on the roll.
   **Absence lines vary**: some print full names, some only surnames, and the
   surname-only ones are useless here. **Roll headings can be missing entirely** —
   `uploads/minutes/2014/sga_minutes.docx` has a generic name and no date in its
   text, so its date has to be inferred from who presides and what is described as
   upcoming.

   **The `uploads/minutes/<year>/` directory listing now 403s (checked 22 August,
   later pass) — but the files inside it are still directly fetchable by name.**
   The block is on listing, not on the files. The live page
   `wku.edu/sga/legislative/minutes.php` links every individual minutes file back
   to 2009-10 with a plain `<a href>`, no WAF challenge on that page at all, so
   scraping its href list with a browser-UA `curl` gives every filename without
   ever needing the directory index. A second page,
   `wku.edu/sga/2018-2019-legislative/minutes.php`, does the same for 2018-19
   through 2021-22 (bare filenames for 2018-19, `minutes_M_D_YY.docx` for 2019-20,
   `.pdf`/`fa20/` for 2020-21, `senate_minutes_M_D_YY.docx` for 2021-22) — found
   late in the 22 August pass and **not yet downloaded or read**.

   This era's minutes (2009-10 through at least 2013-14) are meeting-by-meeting
   prose, not a formal roll-call sheet — no present/absent list of names by
   default. Membership evidence is explicit swearing-in/acceptance/resignation
   language, a blanket "senators at large" appointment vote naming several people
   in one motion, or a full name pinned down elsewhere in the same run of
   documents and tied to a bare "Senator [surname]" floor mention — a bare
   surname on its own is not enough to add someone; do not guess a first name.

   **2010-11, 2011-12 and 2012-13 done, 22 August (later pass):** these three,
   the thinnest years on file (5, 1 and 2 members respectively), were swept using
   the `legislative/minutes.php` trick above — 2010-11 to 18 members, 2011-12 to
   19, 2012-13 to 3, all adversarially verified against the actual downloaded
   text (of 33 drafted names, 1 rejected as a surname-only match to an unrelated
   later year, 5 trimmed for overclaiming). Landed on `research-senate`
   (PR #122). A number of recurring surnames in these years' minutes never
   turned up a confirmable full first name in this corpus and were deliberately
   left out: Cottrell, Asbery, Johnson, Wilcox, Booth/Boothe, Harris, Rhodes,
   Nowland, Karmiller, Powell, Davis, Benton, Sheridan, Preston, Ambriz, Wood,
   George, Wright, Heston. **What is still unswept:** 2013-14 (10 members, more
   files available under the same trick), and the whole 2018-19–2021-22 span
   via the second `legislative/minutes.php`-style page above — 2018-19 (2
   members) and 2020-21 (7 members) are the thinnest of that group. 2015-16 is
   not hosted the way the others are.

   *Checked 20 August (later pass), no names added:* the full Meetings/Minutes
   listing was pulled live (843 item links, 830 of them dated, 1969-02-13 to
   2008-12-02) and mapped to
   academic year. Six of the eighteen years with no `organization.senate.members`
   have **zero** minutes items on TopSCHOLAR, not just an unworked query:
   1966-67, 1967-68 (before the collection starts), 1969-70, 1971-72 (inside the
   date range, but the collection holds exactly one dated item — 13 Feb 1969 —
   between 1968 and 1975-76, so every year from 1969-70 to 1974-75 is equally
   bare), and 1999-00, 2004-05 (genuinely interior gaps: 1998-99 has 43 items
   and 2000-01 has 13; 2003-04 has 26 and 2005-06 has 48; the collection itself
   stops in Dec 2008). 1979-80 stays as already recorded
   above — re-confirmed, nothing new. Talisman substitutes only where
   `archive.org` holds the year: 1971-72's yearbook was read in full and adds
   nothing rank-and-file, only the four officers already on record, plus two
   names sharing an index page reference with no caption identifying a role
   (not added — a bare index cross-reference is not a source for a role). The
   other three pre-1971 years have no Talisman on `archive.org` at all. Herald
   covers 1999-00 and 2004-05 heavily but was not found to print a post-election
   roster the way minutes do — a name-by-name build from individual bill/story
   mentions is possible in principle but wants its own careful, verified pass,
   not a byproduct of this one. Full reasoning and what was actually searched:
   `.research/senate-rolls-gap-years-2026-08-20.md`. **A future run should not
   re-search these six years for minutes** — go straight to a Herald sweep for
   1999-00/2004-05, or leave the four pre-1971 years as a genuine, permanent gap
   in what TopSCHOLAR has digitised.
4. ~~Every Wayback citation in the archive is unverified.~~ **`web.archive.org` is
   reachable from here now (over `https://` — see §8.1), so this run finished the
   two residual citations flagged on 20 August and re-verified the tag-index
   captures along the way:**
   - **The 2006-11-02 I-A-football resolution.** The primary document,
     `data/legislation/2006-07/dc_resolution_124.pdf` (Resolution 06-06-F,
     already on file), shows a first reading dated 31 October 2006 with
     Second Reading / Pass / Fail all left blank — it does **not** show the
     resolution passing, still less passing unanimously, which is what the
     event previously claimed on the strength of an unreachable front-page
     capture. The event was rewritten to say only what the resolution
     document shows, re-dated to 31 October (the date on the document, not
     the guessed 2 November), and re-sourced to the resolution itself rather
     than the Wayback page. The Nov 5 2006 front-page capture that would
     likely settle whether it passed loaded as a transient 503
     ("Temporarily Offline") on every attempt this run — a future run should
     retry it (a handful of attempts a few minutes apart, per §8.1) or open
     the 7 Nov 2006 SGA minutes (TopSCHOLAR `sga/Meetings/Minutes/709`,
     article id 2479) once `viewcontent.cgi` next opens, since the second
     reading would ordinarily fall at the next meeting after the 31 October
     introduction.
   - **The 2007-02-01 Jeanne Johnson student-regent election.** The Wayback
     capture of the 3 Feb 2007 Herald front page (already cited) turned out
     to embed the actual lead story's headline, subhead and lede in full —
     "Johnson wins regent election" / "SGA president took 41 percent" /
     the exact 688-vote, 41-percent lede — even though the article's own
     URL (`.../News/Johnson.Wins.Regent.Election-2690601.shtml`) was never
     independently archived (checked by CDX; zero captures). The citation
     label now quotes that headline and confirms the vote count rather than
     calling the source unconfirmable. The companion claim in the same
     entry — SGA's "first full senate attendance since fall 2004" — is not
     on the front page and was **not** reconfirmed; the entry now says so
     plainly rather than implying the upgraded citation covers it.
   - **Bonus, same method:** the two remaining tag-index captures flagged as
     weak (Stuart Kenderes's Chief Justice record, 10 Nov 2009; the 27 Jan
     2010 senator-resignations entry) turned out, once actually opened, to
     preserve the **full original blog post** under `wkuherald.com/tag/sga/`
     — this was a pre-2011 "notebook"-style full-text post, not a teaser —
     confirming every fact already written against it. Labels upgraded from
     "not the specific article" to name the specific headline and note what
     the capture actually contains.
   - **Mechanical fix:** all 90 occurrences of `http://web.archive.org` in
     `data/years.json` were switched to `https://` (same captures, same
     content — see §8.1).
   - **Content-level check of the 2011–2016 executive-branch/legislative/
     judicial roster captures — done, 21 August.** All 17 `web.archive.org`
     captures of SGA's own site (`/executive/`, `/legislative/`, `/judicial/`
     and successor paths) cited in `organization.executive` or
     `organization.senate.officers` for 2012-13, 2013-14, 2014-15, 2015-16,
     2016-17, 2018-19, 2021-22, 2022-23 and 2025-26 were re-fetched and every
     name each entry claims from them was checked against the captured
     page's own text, not just its reachability. All 17 confirmed clean:
     every officer name is on the page it is cited to, including the two
     records that looked like they might be off at first pass — Director of
     Public Relations "KJ Hall" (2014-15) is confirmed to carry the
     `Katherine.Hall023@topper.wku.edu` address the entry already describes,
     and Director of Enrollment and Student Experience "Tribhuwan Singh"
     (2021-22) is confirmed to be captioned "Trib Singh" on the page with
     `tribhuwan.singh229@topper.wku.edu` beside it, exactly as the entry's
     existing note already says. The Liz Goddard citation (2007-08) was also
     re-checked directly against the archived article text and confirmed
     word for word ("said Liz Goddard, SGA public relations director...").
     Nothing needed correcting. What remains unchecked: roughly 90 of the
     107 unique `web.archive.org` URLs in the archive are specific Herald
     article permalinks rather than homepage/roster captures, and a
     fact-by-fact re-read of those against the sentences they support has
     still not been done — lower priority than the roster pages, since an
     article permalink is a stronger kind of source to begin with, but still
     open for a future pass. **Attempted and blocked, 22 August (a later
     scheduled run):** all 84 unique article-permalink URLs were split into
     six batches and handed to six parallel verifier agents with the
     specific claim each one is cited to support. All six came back
     unable to fetch a single one — `web.archive.org` was hostname-blocked
     at the egress-proxy level all afternoon (see §8.1's updated table),
     unlike 21 August when the same host was open over `https`. No claim
     was touched; per the project's own rule an unreachable source proves
     nothing either way. This is genuinely first in line for whichever
     future run catches the host open again — the batches, the per-URL
     claim text, and the classification of homepage/roster vs. article
     permalink are straightforward to rebuild from `data/years.json` (grep
     every `src`/`src2`.. object for `web.archive.org`) if useful, but
     nothing was saved to disk since the run reused the pattern rather than
     writing a reusable script. `viewcontent.cgi` refused the research run but
     opened later the same day for the editor's pass (see the 1992-93 item
     below).
5. ~~Content-check the 1992-93 roll.~~ **Done, 22 August (scheduled run).**
   `viewcontent.cgi` was open on plain requests around 04:20–04:30 UTC. All 18
   remaining minutes items (405 was already checked; item 406 was settled 21
   August) came down clean on the first attempt at the standard 3-second
   pacing, text-extracted with PyMuPDF, and every one of the 61 names still
   unread was checked directly against its cited document rather than the
   researcher's paraphrase. All 61 confirmed: names, seats, resignation and
   absence notes all matched the primary text exactly, including several
   fine-grained details (Gene Hadden's Non-Traditional Rep seat and later
   resignation, Ryan James's Senior — not Freshman — Class Presidency and
   resignation, Eddie Myers's Sophomore Vice-Presidency, the four Congress
   members seated 2 Feb 1993 and the resignations of Crystal Smith, Rebecca
   Flynn, Jennifer Jaggers and Kevin Moore reported the same night). Nothing
   in the 66-name roll needed correcting.

   One genuine gap turned up in the process, not a correction: **Andrea
   Cailles** — named as Student Affairs committee chair on 25 Aug 1992 and
   already recorded as such under `organization.senate.officers`, replaced by
   Scott Sivley on 1 Sept 1992, then seated as a plain Representative at
   Large on 9 Feb 1993 (SGA Minutes, `sga/Meetings/Minutes/431`) and on the
   absence roll 6 Apr 1993 — was missing from `organization.senate.members`
   even though the officer record's own note already flagged her Feb 1993
   re-seating. Added as the 67th member, following the existing precedent of
   Donnie Miller, who is likewise recorded in both lists. A separate
   adversarial verifier fetched and re-read all three source documents,
   confirmed the finding, and caught one overclaim in the drafted note ("by
   acclamation" was not in the source text for this vote) before it was cut.
   Landed on `research-backlog`; `build.py`, `check_data.py` and
   `check_duplicates.py` all pass clean, the six known duplicate pairs
   unchanged.

   Sixty-six names were merged on a night when the minutes PDFs were
   unreachable, so they were never read against the meetings they cite. That
   was still true of 61 of them going into this run.

   **Editor's trim on merge, 22 August:** the 6 Apr 1993 absence came out of
   the Cailles note. One `src` on a member entry has to carry every fact in
   that note, and the entry cites the 9 Feb 1993 minutes. Do not put it back
   under that citation. Note also that `build.py` drops `profile` and
   `src2`..`src20` when it builds a member's page, so eleven member profiles
   and five sets of extra citations already in `years.json` are written and
   never published. Until that is fixed, a member entry gets one source and
   its note must stay inside what that one source shows.

   Item 406 is now done, and the dating anomaly is resolved rather than
   inferred. `viewcontent.cgi` refused the research run but was open during the
   editor's pass the same day, and article 1918 came down on the first request.
   **The document is headed 22 September 1992** — a Tuesday, like the other
   dated meetings that autumn (items 410, 408 and 405, on 8, 15 and 29
   September). TopSCHOLAR's catalogue date of 20 September is a Sunday and is
   simply wrong; the archive follows the minutes. The meeting was called to
   order at 5.05 p.m. by President Joe Rains, and all five names this archive
   takes from item 406 — Bland, Ezell, Griggs, Smith and Wagner — are in its
   roll call, each recorded absent that night. That confirms them as members,
   which is what the entries claim.

   Two things worth carrying forward. `viewcontent.cgi` is intermittent by the
   hour, not by the day: a 202 challenge is worth retrying in a later session
   before it goes in the handoff as blocked. And the remaining 61 names sit
   behind 19 other minutes items in the same series, all of which can be pulled
   the same way (land on the item page, then request the article with a
   `Referer` back to it) whenever the window is open.

   **Checked again, 21 August (scheduled run) — still challenging.** Two
   attempts on item 412 (article 1912), a few minutes apart, both came back
   HTTP 202 with `x-amzn-waf-action: challenge`. This run worked on 1979-80
   instead (item 1 above) rather than burn more attempts against a closed
   window.
6. ~~The 2013-14 charging-stations entry is written from a first-read report.~~
   **Done, 21 August.** The story was more complicated than either the 24 October
   advance notice or the 30 October follow-up alone: the Senate amended and passed
   the $1,598 bill on 29 October (moving one of SGA's two funded stations from
   Helm 2 to the Commons at Cravens), the Executive Council vetoed it the same
   night for changing a location without consulting WKU Libraries, and a revised
   bill came back to the Senate on 12 November but was tabled again when an
   outdated draft was presented by mistake. No later story reports a final
   passage. The original entry is now written as a proposal rather than a
   settled purchase, and also had a real factual error corrected along the way:
   it paired the wrong three stations as library-funded (the source shows SGA
   funding Glasgow and Helm 2, so the library-funded three are the Educational
   Resources Center, Helm 100 and Owensboro, not Helm 2). Two new events cover
   the veto and the second tabling, both sourced to wkuherald.com. Verified
   against the full text of all three articles by an adversarial pass that
   caught the funding-pairing error and a misattributed 14-day bylaw window
   (that window is the Executive Council's time to act on passed legislation,
   not the Senate's time to override — the source states no deadline on the
   override itself).
7. ~~The 119 undelimited co-sponsor lists~~ **Partly done, 22 August (scheduled
   run).** These names were never actually ambiguous: `extract_authors.py` reads
   the AUTHOR/SPONSOR block as one string and loses the line breaks, but the
   underlying PDF text always had each name on its own physical line (confirmed
   by re-opening the PDF and extracting with line structure intact, which is a
   fact about the document's layout, not a guess about where names split). Two
   methods were used, both without guessing a boundary: (1) segmenting the
   glued string against a dictionary of names already known for that exact
   session — from comma-delimited rows in the same file and from
   `organization`/`leaders` in `years.json` — and accepting a split only when
   it partitions every token with no ambiguity; (2) re-opening the cited PDF
   directly, locating the AUTHOR/SPONSOR block by its own label, and splitting
   on the block's real line breaks, accepted only when rejoining the lines
   reproduces the original glued string exactly (a strict round-trip check, not
   a similarity heuristic). 10 of the ~30 resolved were confirmed by opening the
   source PDF directly and reading the printed line breaks; the rest by the
   round-trip check, which is exact by construction. One further finding:
   `1989-90/dc_resolution_210.pdf` carried the same 5-name author list a second
   time mislabeled as `sponsor` — a genuine mis-extraction, not an undelimited
   list — and that duplicate row was dropped rather than split.
   `data/legislation-authors.json` (the file `build.py` reads) went from 1,038
   to 1,107 rows: 9 previously-published glued rows were split in place, and 21
   rows of real authorship that a curation pass had apparently excluded for
   looking malformed were added back, correctly split. `.research/legislation-authors.json`
   (the full unreviewed pool) went from 1,328 to 1,456 the same way.
   `build.py`, `check_data.py` and `check_duplicates.py` all pass clean
   afterward; the six known duplicate pairs are unchanged. **What's left:** 37
   of the original ~42 still-undelimited rows in the live file (106 in the full
   research pool) did not resolve by either method — some are genuinely
   ambiguous multi-name lists with no independent corroboration for a session,
   and some turned out on inspection to be a different bug entirely (the
   extractor grabbing the wrong block — a committee name captured as
   `sponsor` instead of the people in `CONTACTS`, or body text describing a
   named third party bleeding into what should be a one-name field, as with
   `1991-92/resolution_91-6-f.pdf`, whose "sponsor" field is not a list at
   all). Those need individual review against their PDFs, not another
   automated pass — the two methods above have likely captured everything a
   parser safely can.
8. **Six duplicate pairs that `check_duplicates.py` has reported on every pass.**
   All six have been judged genuinely separate — same-day bills, a bill introduced
   against the same bill failing, a suit planned against a suit endorsed. Nobody
   needs to fix them. They are listed here so the next run does not spend an hour
   re-deciding it.
9. ~~Pre-2011 legislation on TopSCHOLAR, never harvested.~~ **Done, 20 August
   (later pass).** `harvest_topscholar_legislation.py`'s listing parser only
   matched rows whose date carried `class="dtstart"` exactly; a large share of
   the Bills and Resolutions listings print `class="dtstart visually-hidden"`
   instead, so 284 dated documents (128 bills, 156 resolutions, spanning
   1976-77 through 2007-08) were silently skipped by every previous run —
   another instance of trap 7 in §6, a harvester that reported success while
   quietly leaving work undone. `viewcontent.cgi` was open (plain requests,
   no special headers) around 20:30 UTC on 20 August. A companion script,
   `scripts/harvest_missing_legislation.py`, parses each listing by its
   `<tr class="vevent">` block instead of the date span, which catches both
   forms, diffs against `data/legislation.json` by `source_url`, and fetches
   only what was missing, at the same one-request-3-seconds-apart pacing.
   All 284 fetched clean on the first pass, 0 failures, every file verified to
   start `%PDF`. `data/legislation.json` now holds 1,111 entries (827 → 1,111),
   223 MB of PDFs on disk. `build.py`, `check_data.py` and
   `check_duplicates.py` all pass clean against the enlarged set; the six
   duplicate pairs in item 8 above are unchanged, nothing new was flagged.
   What is left: the original `harvest_topscholar_legislation.py` still has
   the narrow regex and should eventually be fixed or replaced outright by
   the companion script, but nothing further needs harvesting — the listing
   pages (644 Bills rows, 812 Resolutions rows including now-stale/duplicate
   entries at different item IDs) were re-parsed by block and everything with
   a real date and a PDF link is now in the archive.

   One correction from the editorial pass: TopSCHOLAR dates some items to a
   year with no month, which reached `session_from_date` as 1 January and filed
   twenty-three fall documents into the previous academic year — among them
   three bills the archive already carried as September 1991 events on
   1991-92. They were refiled off the `-F` in their own numbers. A year-only
   listing date is not enough to place a document; read the semester letter
   out of the title first.

### 8.4 Build-side work, which is not research

- ~~`apply_photo_overlay()` in `build.py` matches `photos.json`'s leaders overlay
  only against a year's top-level `leaders` array, and `render_officers()` renders
  no photo field at all.~~ **Fixed, 21 August.** `apply_photo_overlay()` now falls
  back to `organization.executive`, `organization.senate.officers` and
  `organization.senate.members` when a photo's name does not match a top-level
  leader, attaching `photo` onto that officer or member record instead.
  `officer_index()` carries `photo` through onto each term and onto the person
  object, and `render_officer()` now shows the portrait, credited, at the top of
  the person's own page (`.who-head .portrait`, floated beside the heading). No
  photo currently in `photos.json` needs the *fallback* path — all 73 existing
  portraits already match a top-level leader — but the change is not invisible:
  because `render_officer()` had never shown a portrait at all, **66 person pages
  gained one on merge**, each resolving to a real file in `site/photos/` and
  carrying its existing credit. Checked at merge, 21 August, by building `main`
  and the branch and diffing the output: 66 portraits render, none broken, and
  the only other change is the new CSS rule inlined into every officer page.
  `build.py`, `check_data.py`, `check_contrib.py` and `check_duplicates.py` all
  pass clean; the six known duplicate pairs are unchanged. **Officer and senate
  portraits are now worth hunting.** `render_officers()` (the roster/index page)
  still shows no thumbnails — it is a dense name index by design, not a gallery,
  and adding images there is a separate, optional call for a future run, not a
  bug.
- **Eighteen of the 61 years still have no year photograph, down from twenty-nine**
  (re-measured 22 August, scheduled run): 1981-82, 1982-83, 1983-84, 1987-88,
  1990-91, 1993-94, 1994-95, 1995-96, 1996-97, 1997-98, 2000-01, 2001-02, 2002-03,
  2003-04, 2005-06, 2006-07, 2008-09, 2009-10. Every year still has a leader
  portrait (checked the same run: 0 of 61 leader records are without one, so
  presidents Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley, named in an
  older stored task prompt as missing, are confirmed still covered), so the whole
  remaining photo gap is in photographs of the organisation at work.

  **The stored prompt's own source list is wrong: there is no `digitalcommons.wku.edu/talisman/`
  collection** — that path 404s, a real "page not found" from the server, not a
  block. The Talisman yearbooks are catalogued under
  `digitalcommons.wku.edu/dlsc_ua_yearbooks/` (the collection landing page, itself
  reachable) as individual `dlsc_ua_records/NNNN` items, mixed in with the Herald
  and everything else in that records series. That landing page is not paginated
  and does not list every year — it is a curated subset, and there is a real gap
  between 1979/1981-and-earlier and 2003, then another gap between 2003 and 2013.
  Confirmed by publication date on each item's own page (`grep`-able as `<p>` under
  the `Publication Date` heading) rather than guessed from title order:

  | academic year | item | title | pub. date | article no. (for `viewcontent.cgi?article=`) |
  |---|---|---|---|---|
  | 1981-82 | `dlsc_ua_records/405` | An Uphill Battle | 6-1-1982 | 1405 |
  | 1982-83 | `dlsc_ua_records/406` + `/407` | A Season of Hope, pts. 1–2 | 6-1-1983 | 1406, 1407 |
  | 1983-84 | `dlsc_ua_records/408` | The Touch of Red | 6-1-1984 | 1408 |
  | 1987-88 | `dlsc_ua_records/412` | In a Different Light | 6-1-1988 | 1412 |
  | 1990-91 | `dlsc_ua_records/415` | The Western World | 6-1-1991 | 1415 |
  | 1993-94 | `dlsc_ua_records/418` | Against All Odds | 6-1-1994 | 1418 |
  | 1994-95 | `dlsc_ua_records/420` + `/421` | Xposure: Rites of Passage (spring); Canvas Flesh (summer) | 1-1-1995, 6-1-1995 | 1420, 1421 |
  | 1995-96 | `dlsc_ua_records/419`, `/422`, `/423`, `/424` | Xposure: Prejudice: Beyond Black & White (winter); Fall 1995; Spring 1996; Summer 1996 | 12-1-1995, 9-1-1995, 1-1-1996, 6-1-1996 | 1419, 1422, 1423, 1424 |
  | 2002-03 | `dlsc_ua_records/594` | About Face | 2003 (year only on the item page) | 1594 |

  The article number for `viewcontent.cgi?article=` is not the same as the item
  number in the `/dlsc_ua_records/NNNN/` URL — on every item checked this run it
  was the item number plus 1000, but confirm each one from the item's own page
  rather than assume the offset holds everywhere. No candidate found this run for
  1996-97, 1997-98, 2000-01, 2001-02, 2003-04, 2005-06, 2006-07, 2008-09 or
  2009-10 — the yearbooks landing page simply has no entry in that range; try a
  live TopSCHOLAR search or `wku.edu` Wayback captures for those, not another pass
  over this same landing page. `archive.org`'s Talisman holdings do not help
  either: it holds 1972–1981 and 1986–1987 (by publication year, i.e. the academic
  years up through 1980-81 and 1985-86/1986-87), none of which land inside the
  current 18-year gap.

  **`viewcontent.cgi` was WAF-challenged on every attempt this run** — 5 tries
  across roughly 20 minutes, spread out with real work in between (not a
  sleep-loop), landing on the item page first, carrying its cookie, sending
  `Referer` back to the item page plus the full `Sec-Fetch-*` /
  `Upgrade-Insecure-Requests` header set, and using the article number read
  straight off the page rather than guessed. Every attempt came back HTTP 202
  with `x-amzn-waf-action: challenge`, 0 bytes. Per the 20–21 August notes above,
  this is a challenge that lifts and re-closes by the hour, not a fixed block —
  worth a fresh attempt next run before assuming it is still closed. The table
  above is the ready-made worklist for whenever it opens: land on each item page,
  pull the PDF with the article number listed, find the SGA section, and match a
  name to a caption before using any face from it.

### 8.5 Data hygiene

- ~~`o/nate-eaton.html` and `o/nathan-j-eaton.html` are two pages for one man~~
  **Fixed, 21 August (scheduled run).** All three printed forms — "Nate Eaton"
  (Chair, Campus Improvements Committee, 2006-07 and 2007-08), "Nathan Eaton"
  (Senator, 2007-08, whose own record already noted "Printed as Nate and
  Nathan Eaton") and "Nathan J. Eaton" (Speaker of the Senate, 2008-09) — were
  already the same person by the record's own text; only `name-aliases.json`
  had no entry folding them together. Added `"Nate Eaton": "Nathan J. Eaton"`
  and `"Nathan Eaton": "Nathan J. Eaton"`, following the existing convention of
  mapping short/printed forms onto the fullest recorded name (as with "Jamie
  Hargrove" → "James Hargrove"). `build.py` now writes one page,
  `o/nathan-j-eaton.html`, for all three terms; `check_data.py` and
  `check_duplicates.py` both pass clean, the six known duplicate pairs
  unchanged.
- ~~The 2016–2027 officer names include a batch of garbled scrapes~~ **Done, 22
  August (scheduled run).** All 294 `organization.executive`/`organization.senate.officers`
  entries carrying the note "Named on the document as..." (2016-17 through 2025-26)
  trace to a legislation PDF cited in their own `src.url`. Every one of those 196
  PDFs was re-fetched from wku.edu (open, no special headers needed) and its
  AUTHORS:/SPONSOR:/CONTACTS: block re-extracted with PyMuPDF, giving a ground-truth
  "Name, Office" pairing independent of the original scrape. 158 entries had a
  genuinely garbled `name` (a stray word glued on from an adjacent author's office,
  or from an off-by-one split of a multi-author line) and were corrected to the
  clean name the PDF actually prints; 27 of those also had a visibly truncated
  `office` ("Chief of", "Senator-", bare "Senator") completed from the same
  evidence. 103 were already correct as printed (mostly multi-author lines on one
  paragraph line, e.g. "Andi Dahmer, SGA Senator, Jody Dahmer, SGA Senator, Helen
  Vickrey, MyCampusToo Committee Chair", that a naive comma-splitter had failed to
  separate, not data errors). 33 entries were removed outright: 28 named a real
  person who was never an SGA officer — WKU faculty or staff (a department chair,
  the Provost, three college/office directors, a Vice President for Student
  Affairs, an Assistant Vice President, a Dean, two program directors), an officer
  of a different registered student organization (Residence Hall Association,
  International Diplomats, CISO, ISA, Student Veterans Alliance, Young Democrats,
  Recyclops, Kentucky Veterans Brigade), or a guest co-author of one bill (No Lost
  Generation WKU's director) — each named only in a bill's CONTACTS or AUTHORS
  line, never holding SGA office; the other 5 were not people at all, just a
  committee name ("Organizational Aid", four instances across four years, where
  the source lists several members and the entry can't be pinned to one) or a
  fragment of the bill's own subject text ("Executive Producer", "Food Pantry")
  misparsed as a name. A general-purpose subagent independently re-checked every
  proposed correction and removal against the same PDF evidence in four parallel
  passes before anything was applied; it caught one real bug (a colon-separated
  "Senator at Large: Mark Clark" AUTHORS line had produced a garbage match that
  would have overwritten an already-correct name — reverted to leave it alone) and
  pushed the office-completion count from a handful of manual cases to the full 27
  by flagging every truncated office my first pass had left untouched. One
  genuine spelling conflict surfaced and was flagged rather than resolved, per the
  project rule: "Lauren Willet" (Bill 25-22-F) vs "Lauren Willett" (Bill 6-22-F),
  each entry now correctly matching its own cited document. `build.py`,
  `check_data.py` and `check_duplicates.py` all pass clean; the six known
  duplicate pairs are unchanged. What's left: this pass covered only the 294
  entries an earlier run had flagged with an auto-scrape note; a handful of other
  2016-2027 entries may carry the same class of error without that note and
  weren't in scope here.
- **`Chris Grau` (Office Secretary, 1968-69)** carries a note in the data reading
  "SPELLING UNVERIFIED, do not publish without a second look", possibly
  "Christina L. Graue" per the minutes signature. Still unverified.
- **`Amos Gott` / `Amos E. Gatt`** — the 1989-90 session prints the same person's
  name two ways on two resolutions. Both are kept as printed rather than merged.
  Flagged, not fixed, per the project rule.
- **A third of the senate roll now reads on the site as "recorded absent at a roll
  call."** The membership is what the entry establishes; the absence is only the
  evidence for it. The two should probably swap places. Accurate as it stands,
  which is why it merged, but it reads oddly.

---

## 9. Restarting a session

```bash
cd /Users/samkurtz/Downloads/sga60
git pull
python3 scripts/build.py          # rebuild; runs the validator
python3 scripts/check_data.py     # exit 1 if the record broke its rules
python3 scripts/check_duplicates.py
```

Then pick from §8. Read `CLAUDE.md` and §6 of this file before writing anything
into `data/`.

**Editorial line, in one sentence:** publish only what a cited source carries,
say plainly what the archive does not know, and never let a page imply
completeness it has not earned.
