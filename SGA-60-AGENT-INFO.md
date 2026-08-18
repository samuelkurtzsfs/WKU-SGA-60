# SGA 60 — agent handoff

Everything a new Claude Code session needs to pick this project up cold. Read
`CLAUDE.md` first for the editorial rules; this file is about the machinery, the
research method, and what is left to do.

Last updated 6 August 2026.

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

| | |
|---|---|
| academic years | 61 (1966-67 → 2026-27) |
| dated, sourced entries | 1,877 |
| programmes (things SGA put on) | 633 |
| people who were president | 60 |
| people who held the student regent seat | 57 |
| people recorded in any office | 787 |
| officer/leader records | 1,045 + 73 |
| years with a cabinet recorded | 58 of 61 |
| person profile pages | 787 |
| total pages built | 867 |
| legislation PDFs held | 390 |
| authorship attributions from those PDFs | 918 |
| complete Herald article index | 11,850 items / 17,601 lines |

**Sam Kurtz is the 58th president** and the 55th student regent. Caden Lucas is
the 60th and 57th. Sixty years of student government span 61 academic years
because the constitution was ratified in April 1966, so 2025-26 is the sixtieth
year and 2026-27 is the one now running.

---

## 2. The scripts, and what each is for

| script | what it does |
|---|---|
| `build.py` | The only presentation file. Generates all 867 pages. Runs `check_data.py` at the end and shouts if the record broke its own rules. |
| `check_data.py` | Validates `data/years.json` against the archive's own rules. **Exit 1 on any problem, so it can gate a deploy.** Checks dates, sources, duplicate titles, roles, file integrity by magic bytes, photo overlay attachment, status consistency. |
| `check_duplicates.py` | Reports events in one year that look like the same event written twice. Reports only; you judge. Same-day bills are genuinely separate events. |
| `harvest_herald_index.py` | OAI-PMH sweep of the digitised collection. `--all` keeps **everything** into `data/herald-index-full.json`; without it, only student-government lines into `data/herald-index.json`. |
| `extract_authors.py` | Reads AUTHOR/SPONSOR lines off the 390 legislation PDFs with PyMuPDF. |
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
| **Wayback** over `wku.edu/Dept/Org/Student/SGA` | Officer pages ~1997–2010. `formersgapres.htm` is SGA's own numbered presidents roster (archived 24 Sep 2001). |
| **Local legislation** `data/legislation/` | 390 PDFs, 373 print an AUTHOR line. Free. |

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

## 8. Outstanding work, highest value first

1. **The senate rolls.** `.research/senators-unverified.json` holds 105 names
   from a run whose checkers died. **Do not merge as-is** — the researcher's own
   notes disown several. Re-run verification, then `merge_senators.py`. Thousands
   of members are still unrecorded; the minutes are the roll.
2. ~~**Three branch histories unverified.**~~ **Done, 18 Aug 2026.** L9 (2010s
   Senate), J1 (1970s judiciary) and C1 (constitutions 1966–91) were checked —
   each against its cited sources by an independent checker, then against a
   *second*, adversarial re-checker, since the first-pass agents hit an
   environment limit worth recording: `digitalcommons.wku.edu/cgi/viewcontent.cgi`
   PDF downloads and `web.archive.org` are both hard-blocked from this session
   (confirmed by two agents working alone, not a burst-traffic 403 — a future
   run should expect the same and plan to work from digitalcommons *landing
   pages* — title, date, one-line abstract, or a Herald issue's table of
   contents — plus `archive.org`, which is open and unrestricted, rather than
   count on reaching PDF or Wayback text). All three needed correction: wrong
   constitution section numbers in L9 (traced and fixed against the redline in
   `data/legislation/2012-13/r5-13-s.pdf`), a miscited Herald issue and an
   unconfirmable vote tally in J1 (softened), and in C1 a wrong "correction" the
   first pass itself introduced (reverted), a citation covering two different
   Herald issues (split), and several claims that turned out to rest only on a
   citation's title, never on text anyone could actually read (trimmed or
   flagged rather than published as confirmed). All three are now in
   `.research/branches-checked.json` and on `branches.html`; the incidental
   finding that Kelly Thompson's 1 April 1966 letter names Reed Morgan as the
   constitution committee's chairman is folded into item 6 below.
   `.research/branches-unverified.json` is now empty.
3. ~~**235 dated moments** from the branch research, unmerged.~~ **Done, 18
   August 2026.** All 235 were deduped (many were the same event written up
   twice by different research passes — the December 1970 constitution vote
   alone had three versions), checked against their cited sources by a
   researcher, then re-checked by a second, adversarial pass before
   publication, in eight batches by era. **138 survived and are now events in
   `data/years.json`; 97 were cut**, mostly because their only source was
   `web.archive.org` or `digitalcommons.wku.edu/cgi/viewcontent.cgi`, both
   hard-blocked in this environment on this run — those remain candidates for
   a future run with different source access, not disproven claims. A
   recurring pattern worth remembering: TopSCHOLAR/digitalcommons landing
   pages usually show only a headline, byline and one-line abstract, never
   full article text, so most surviving "trim" verdicts kept the bare
   confirmed headline and cut specific vote tallies, quotes and named detail
   the landing page couldn't support. **SGA's own minutes and legislation
   pages on `digitalcommons.wku.edu` and `.doc`/`.pdf` files on `wku.edu/sga`
   store their date fields as DD-MM-YYYY, not MM-DD-YYYY** — a naive
   MM-DD-YYYY read of a field like "1-3-1983" would misdate a real event by
   two months; confirm the convention against a same-collection page with an
   unambiguous day (>12) before trusting a date field. Along the way, checking
   turned up and fixed three unrelated existing-entry errors: an unsourced
   vote tally on the 1999 Morrison/Matheis vice-president-of-finance re-run
   was cut and a second citation added; a naming conflict between a Herald
   report and SGA's own 2009 minutes on two resigning senators (Michel/Mitchell
   Stephens, Emmett/Emmitt) is now stated both ways rather than picked
   silently; and two 2022/2023 entries that stated a Bowling Green Pride
   sponsorship and a committee merger as settled fact were corrected after
   SGA's legislation table showed the Executive Cabinet never passed either
   one — one of those two also turned out to duplicate another entry
   word-for-word, which is now removed. `.research/branches-moments.json` is
   now empty.
4. ~~**Three years still have no cabinet.**~~ **Attempted, 18 August 2026 — the
   three years are still empty.** All 92 candidates in `.research/officers-unchecked.json`
   were checked one at a time against their cited source (paced, 3+ seconds
   apart on `digitalcommons.wku.edu`). Only 3 survived, and none of them are
   for 1979-80, 2001-02 or 2003-04 — every candidate for those three years was
   sourced to either a `digitalcommons.wku.edu/sga/Meetings/Minutes/NNN`
   landing page (which in this environment shows only a generic one-sentence
   agenda-topic list — "budget, appointments, blood drive" — never an
   individual's name, because the PDF behind it is blocked) or to
   `web.archive.org`, which is flatly unreachable from this session (curl
   returns HTTP 403, WebFetch errors outright). Two 1980-81 candidates were
   confirmed instead and merged: **Mark Wilson as administrative vice
   president**, fully confirmed including two vote counts and a direct quote
   against archive.org's OCR text of the 1981 Talisman, and **Paul J. Deom as
   a Judicial Council member**, trimmed to what his own February 1982 Herald
   letter actually supports. A third, Greg Zoeller, was found genuinely
   elected to "one of the top three ASG offices" in April 1980 by the cited
   Herald headline, but the headline never states which office, so — per this
   file's own standard that a specific claim needs a source that actually
   carries it — he was held back rather than filed under the guessed title of
   "activities vice president." The full audit of all 92, including every
   rejection reason, is in `.research/officers-checked.json`.
   `.research/officers-unchecked.json` is now empty. **The three years remain
   genuinely without a recorded cabinet** — not for lack of trying, but
   because nothing in this candidate batch survives contact with a source this
   session can actually read. A future run with working `viewcontent.cgi` or
   `web.archive.org` access could recheck the 21 items marked
   "source unreachable" in the audit file; the other 68 were checked against
   a source that loaded fine and simply didn't say what was claimed.
5. ~~**Four people have no portrait.**~~ **Done, 18 August 2026** (a separate
   photographs pass, recorded in `.research/NIGHT-REPORT.md`) — Nick Todd,
   Katie Dawson, Jeanne Johnson and Reagan Gilley all have portraits in
   `data/photos.json` now.
6. ~~**Two names unconfirmed.**~~ **Both settled, 18 August 2026.** Reed Morgan
   (1968): the C1 branch check (item 2, above) found that Kelly Thompson's 1
   April 1966 approval letter (`digitalcommons.wku.edu/dlsc_ua_records/527`) is
   addressed to "committee chair Reed Morgan and vice chair John Lovett" —
   direct documentary support, independent of the sources already behind this
   project's settled reading in section 7, that Morgan's plaque credit honours
   the constitution committee's chairmanship rather than the presidency.
   Amanda Coates/Lich: two sittings of the Kentucky Council on Postsecondary
   Education carry it. The minutes of 13 November 2000
   (`cpe.ky.gov/aboutus/records/cpe_meetings/minutes-2000-11-13.pdf`) introduce
   the incoming holder of the council's statewide student seat as Amanda
   Coates, "a graduate of Western Kentucky University" — which is what ties
   the council's student member to this university at all. The minutes of 30
   July 2001 (`.../minutes-2001-07-30.pdf`), recording Governor Patton's
   appointment of her successor, name the outgoing member "Amanda Coates
   Lich". The first carries Coates of Western into the seat, the second
   carries Lich out of it, and between them they tie the plaque's surname to
   the Coates named in every source from her actual SGA year. The 30 July
   minutes alone would not have done it: they never mention Western. The 1999-00 leader entry's
   note, sources and profile are updated accordingly; two degraded duplicate
   citations (a bare collection-root URL and a wildcard web.archive.org
   search URL, both standing in for specific pages already cited properly
   elsewhere in the same list) were also dropped from that entry, an instance
   of the item 7 problem below caught along the way. A WKU staff-directory
   trace of "Amanda Coates Lich" as a current university employee turned up in
   the same search and was deliberately left out of the archive: it says
   nothing about her SGA service, and this project does not record a living
   person's post-office career absent a source connecting it to that service.
7. ~~**~20 citations rest on homepage or tag-index captures.**~~ **Done, 18
   August 2026.** All 16 found (a systematic scan of every `src`, leader,
   officer and document citation in `data/years.json` for a bare Wayback
   homepage, a `/tag/` index, or a bare `digitalcommons.wku.edu/dlsc_ua_records/`
   collection root) were checked one at a time, then the 8 proposed upgrades
   were sent to a separate adversarial verifier before anything was committed.
   `web.archive.org` is not rate-limited in this environment, it is a hard
   **"Blocked by egress policy"** on both `https` and `http`, so none of those
   captures could be read directly; the `archive.org/wayback/available` API
   confirms the snapshots still exist, and `archive.org` (no `web.` prefix) and
   `digitalcommons.wku.edu` landing pages remain open.
   **8 citations got a real digitalcommons.wku.edu/dlsc_ua_records permalink**
   in place of a bare Wayback homepage or collection root, found by matching
   the event's own text against that issue's indexed headline list in
   `data/herald-index-full.json`: Sandra Norfleet's citation, which had decayed
   to a bare collection root, now points at `dlsc_ua_records/2464`, the exact
   issue this file's own settled-facts section already names; and seven 2005-06
   /2009-10 events/leaders moved from a dateless Wayback front page to the
   specific issue whose headline names the story (e.g. "Rob Watkins elected SGA
   president" → `dlsc_ua_records/3692`, headlined "See Rob Run, Win . . .
   Barely"). The verifier caught real overclaiming in three of those eight and
   they were trimmed rather than published as found: a "10 pieces of
   legislation" count and an itemised list of bills that only the headline
   "Approves Less Legislation This Semester" could not support (the count is
   now dropped, keeping only the confirmed decrease and the confirmed
   election of Jeanne Johnson as speaker, whose full name the headline gives
   directly — the entry no longer hedges her as "a senator named Johnson");
   a $2,000/two-bills/unanimous claim for a 40th-anniversary party story that
   only the headline "Plans Anniversary Party" could confirm (the figures are
   cut); and a Rally for Higher Education preview wrongly written up as
   reporting that Gov. Beshear did address the rally, an advance-notice error
   this file's own §6.1 warns about (cut back to what the preview actually
   said). **6 citations could not be upgraded** — a Wayback front-page or
   `/tag/sga/` capture with no better source found locally or on the live
   `wkuherald.com` WordPress API — and were left in place with the citation
   itself marked as a front-page or tag-index capture rather than the specific
   article, so a reader can see the citation is weaker than it looks without
   the caveat intruding on the entry's prose: the 2006-07 events for the I-A resolution
   and Johnson's regent-election win, the 2006-07 Jeanne Johnson leader record,
   the 2009-10 Judicial Council removal and two-senators-resign events, and
   Chief Justice Stuart Kenderes's senate-officer record. **2 looked
   suspicious but checked out fine and were left untouched**: the
   `wkuherald.com/36017/uncategorized/sga/` URL used for the 2014-15 election
   challenge and Jay Todd Richey's 2015-16 leader record turned out to be a
   real, specific post — fetching it directly shows an `og:type` of "article"
   and a description matching the claim word for word, just filed under a
   generic "uncategorized" WordPress category rather than a descriptive slug.
8. **Pre-2011 legislation** on TopSCHOLAR (~444 docs) never harvested.

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
