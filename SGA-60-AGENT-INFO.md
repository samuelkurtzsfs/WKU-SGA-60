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
| `digitalcommons.wku.edu/cgi/viewcontent.cgi` | **blocked**, HTTP 202, empty body, `x-amzn-waf-action: challenge` | every PDF: Herald page images, Talisman pages, minutes, legislation. Confirmed still challenging on 21 August: 5 retries over 7.5 minutes on two different SGA-minutes items, all 202. |
| `web.archive.org` | **open on `https://`**; plain `http://` is egress-blocked by this sandbox, not by archive.org (see note above) | every Wayback citation in the archive is now checkable from here over https. Individual captures can 503 transiently — retry a few times before concluding a specific snapshot is gone. |
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

**As of the 21 August overnight pass, no pull request is open.** All four branches
that were open that night — `research-backlog` (#80), `research-photos` (#81),
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
   **2003-04 done, 2001-02 already done by `research-senate`, 1979-80 still
   genuinely open — see below.** `viewcontent.cgi` opened again around 12:30
   UTC on 20 August (plain requests, no special headers needed) and stayed open
   long enough to pull four full SGA minutes PDFs straight from TopSCHOLAR:
   2 Sep 2003, 16 Sep 2003, 2 Dec 2003, 13 Apr 2004 (all `sga/Meetings/Minutes/`
   items 524, 522, 541, 543), reusing the recipe in §8.1 (this time no special
   headers were even needed). Against that primary text, an adversarial
   verifier trimmed six of thirteen officer claims for overclaiming ("held the
   office throughout the year" narrowed to "confirmed at the meetings actually
   checked"; "sworn in" narrowed to "approved by unanimous vote" where the
   swearing-in itself wasn't shown) and cut two of five committee co-chair
   claims down to one confirmed name apiece (Evelina Petkova and Tim Howard are
   each named once, alongside an already-confirmed chair, with no stated role —
   recorded as such rather than as "co-chair"). What survived and is now on
   `data/years.json`: a nine-seat executive and Judicial Council roster
   (Executive VP Patti Johnson, VP Finance Nick Todd, VP Public Relations Abby
   Lovan, VP Administration Jessica Martin, IT Designate Matthew Pava, Sergeant
   at Arms Cameron Yancey, Parliamentarian Mason Stevenson, Coordinator of
   Committees Scott Wolfe, Chief Justice Troy Ransdell and Justices Josh
   Collins/Gretchen Light/Scott Broadbent), the first Speaker of the Senate
   Robert Watkins (elected 13 April 2004, 9-8 over Brittany Fausey — this also
   corroborates, from the primary minutes, an event already in the record
   sourced only to the Herald), and five senate committee chairs. 1979-80 is
   not the same kind of gap: the digitized minutes collection has no meeting
   from inside that term at all (only the 29 April and 6 May 1980 transition
   meetings, which swear in *1980-81's* officers), and the only Herald coverage
   the local index or the TopSCHOLAR landing pages surface is the presidential
   race itself — no AVP, Secretary or Treasurer is named anywhere reachable
   from here. The four previously-rejected 1979-80 candidates (Fuller, Bates,
   Thompson, Craig) stay rejected; nothing found this run changes that. Leave
   1979-80 for a run that can search full-text Herald PDFs or a yearbook, not
   another pass over the same index.
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

   What is still unswept: 2011-12 and 2012-13 hold one and two member records
   against 33 for 2014-15, so those years were mined for particular names rather
   than read through. 2015-16 is not hosted the way the others are.

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
   - **Not done this run, and worth a future pass:** the broader claim that
     Liz Goddard's profile and "several 2011–2016 executive-branch records"
     rest on Wayback was not re-verified fact-by-fact. All 107 unique
     `web.archive.org` URLs in the archive were fetched once each and 82
     loaded real pages immediately (Goddard's among them — hers is already a
     specific article permalink, not a homepage/tag capture, and loads
     fine); nobody has yet re-read each one against the sentence it
     supports the way this run did for the two flagged citations. That
     content-level check, not just reachability, is what should happen
     next, plus a real attempt at `viewcontent.cgi` for the two open items
     above.
5. **Content-check the 1992-93 roll.** Sixty-six names were merged on a night when
   the minutes PDFs were unreachable, so they were never read against the meetings
   they cite. Also: TopSCHOLAR dates minutes item 406 to Sunday 20 September 1992,
   when every other meeting that year is a Tuesday or a Thursday. The metadata may
   itself be wrong. Whoever next has that PDF open should settle it.
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
7. **The 119 undelimited co-sponsor lists** dropped from the legislation
   authorship extraction. Late-1970s and 1980s forms print several names with no
   comma between them, and they cannot be split into individuals without guessing
   a boundary. They are in `.research/legislation-authors.json`, the full
   unreviewed 1,328-row extraction, and they want a smarter name-boundary parser
   rather than another pass of the same one.
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

- **`apply_photo_overlay()` in `build.py` matches `photos.json`'s leaders overlay
  only against a year's top-level `leaders` array, and `render_officers()` renders
  no photo field at all.** A portrait of a vice president or a senate officer can
  therefore sit correctly in the data and never appear anywhere on the site. The
  photographs routine found this, correctly declined to do research it could not
  render, and flagged it. Until it is fixed, officer portraits are not worth
  hunting. This is the highest-value item in this section.
- **Twenty-nine of the 61 years still have no year photograph** — every year has a
  leader portrait, so the gap is entirely in photographs of the organisation at
  work. That is a research job, but it is gated on nothing except the Talisman and
  the archives.

### 8.5 Data hygiene

- **`o/nate-eaton.html` and `o/nathan-j-eaton.html` are two pages for one man**,
  who chaired Campus Improvements under the short name and took the Speaker's
  chair under the long one. `name-aliases.json` has no Eaton entry. Adding one
  asserts they are the same person, which the record here supports, but that
  assertion should be made by a run that sets the evidence out, not slipped into a
  merge.
- **The 2016–2027 officer names include a batch of garbled scrapes** — titles glued
  onto names, "Senator Andi Dahmer", "Public Health Kate Hart". They inflate the
  person count and they are not safe to profile under. They want a deliberate
  cleaning pass against a real roster, not a guess.
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
