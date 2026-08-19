# Night report - 4 August 2026

Written by the overnight editor at 5:20 AM.

## The headline
All 61 years, 1966-67 through 2026-27, are researched and live. 650 dated events,
68 leader profiles, 23 verified portraits, 14 primary documents
readable on the site, 381 legislation files. Every event carries a dated, cited source.

## What the night produced
- The modern era (2000-2027): fully researched and 100% fact-checked, every event
  verified against its source page.
- The pre-2000 era: all 32 target years researched from the indexed Herald archive
  and verified; the founding era rebuilt on primary documents including the 1968
  election results memo (Straeffer 1,732 - Whitley 1,098).
- Plaque disputes resolved: Zielke's term corrected to 1969-70 (the plaque conflated
  two terms), Hargroave confirmed as Hargrove, Payne/Bush 1982 succession untangled,
  Linda Jones and William Menser confirmed. Reed Morgan honestly left unresolved -
  the only archival Morgan is a different 1966 role, and identities are not merged
  without proof.
- Sensitive history handled to standard: the 2016 racism complaints and resignations,
  the 2004 Todd impeachment bid, the Watkins resignation - all reported strictly to
  what the cited sources printed.
- Primary documents mirrored: senate and cabinet minutes, Board of Regents minutes,
  two SGA constitutions.

## What verification cut
Roughly 55 items died in fact-checking across the night - events and profile
paragraphs whose cited page did not support the claim. They are logged in the
workflow journals; none reached the site or all were removed on verdict.

## Still thin
1974-75 (3 events) - a dedicated researcher and fact-checker are on it as this
report is written. Kayla Shelton's 2009-10 plate remains flagged as unverified
against the digitised Herald.

## For Sam
1. Rotate the GH_TOKEN (it passed through chat once; regenerate on GitHub, update
   the environment variable).
2. The Talisman portrait hunt continues hourly - faces for the 70s-90s presidents
   are the main remaining gap.
3. Consider the testimony project (RESEARCH.md part C) - the archive work is done
   enough to start calling alumni.

---

# Night report - 18 August 2026

Written by the overnight editor at 5:00 AM.

## The headline
The three pull requests that had been open since 4 August are closed. None of them
could be merged, and the reason is structural rather than editorial: `main` was
rebuilt on a new root commit after 4 August, so it shares **no common ancestor**
with any research branch. Git reports them as "50 behind"; in fact they are
unrelated histories. Merging one would not have added anything - it would have
restored the 4 August snapshot over the current record, cutting `data/years.json`
from 1,877 events to roughly 830 and deleting `herald-index-full.json`, the
legislation authorship index, the name aliases, the whole contributor layer and
all three validator scripts.

Everything on the three branches worth keeping has been lifted onto `main` instead.

## What was merged
Three additions and one cut, each checked against its source before publication.

- **29 September 1983** - an ASG group formed to study the grade scale, with
  president Jack Smith writing that ASG backed the Herald's opinion. Both items
  appear in the TopSCHOLAR record for Herald 59:11.
- **23 October 1986** - a bill to make the athletic fee optional defeated, and a
  top ASG race decided by eight votes. Both in the record for Herald 62:17.
- **Senate minutes, 8 November 2022** - re-downloaded from wku.edu and byte-for-byte
  identical to the branch copy, so the mirror is authentic. This gives 2022-23 its
  first document.
- **Cut:** the adviser change of 7 July 2026 had been written up twice in 2025-26
  from the same Herald report. The fuller entry is kept and carries every fact the
  other had.

## What was cut and why
One entry would have put an invented fact on the live site. "Robinson reappoints
Jenkins chief communications officer", dated 22 April 2025, cites a Herald article
that is about a student-painted mural announced at the meeting of 19 August. There
is no reappointment in it, no April date, and no confirmation vote. The date, the
framing and the vote were all unsupported by the source cited for them.

Smaller cuts: a committee-chairs entry that said "five" and then listed six (the
Herald names six, and `main` already had it right); four entries duplicating
meetings `main` already covers from the same articles; and a charity awareness-day
proclamation, which the rules exclude by name. Two 1985 items had been filed under
1985-86 though February and March 1985 fall in 1984-85.

## What held up
Spot checks were run against thirteen sources. The four most recent 2026 items -
the ODK award, the proposed tuition increase, the Regents' vote and the adviser
change - all hold up, and `main` already carried all four, filed in 2025-26, which
is the right academic year. Rush Robinson, not Lucas, cast the lone no vote against
the tuition increase, and the record says so.

On the photographs branch, five portrait entries that looked unique were the same
image files `main` already holds under the settled spellings. The sixth, Sandra
Norfleet, is filed on the branch under 1982-83 and on `main` under 1981-82.
**`main` is right**, on the strength of the Herald of 15 April 1982, "Student
Regent's 2-Month Term Nears End". Section 7 of the handoff still reads 1982-83 and
is now the stale copy.

## A warning about the local index
`data/herald-index-full.json` cannot be used to rule a headline out. The harvester
stores each issue description in 300-character chunks and many records stop
mid-headline. Every one of the 1983, 1985 and 1986 headlines confirmed live this
morning was missing from the local copy. Grep it to find candidates; open the
record page to confirm. Record URLs also 301 unless requested with a trailing slash.

## Where the record stands
61 years, 1,878 dated events, 60 people who have been president, 34 documents,
390 legislation files. `build.py`, `check_data.py` and `check_contrib.py` all clean.
`check_duplicates.py` reports six pairs; all six are genuinely separate events -
different dates, or same-day bills, which stay apart.

## Still open
- Four leaders have no portrait: Nick Todd and Katie Dawson (2004-05), Jeanne
  Johnson (2006-07), Reagan Gilley (2008-09).
- The 8 November 2022 minutes are mirrored but not read. No PDF text extractor
  works in this environment - PyMuPDF is absent and pypdf fails on its crypto
  import - so the summary is deliberately plain. Worth expanding.
- The research routines are still starting from the orphaned branches. Until they
  branch from `origin/main`, every run will produce work that cannot be landed.

---

# 18 August 2026, evening — editor pass

## What I reviewed
One open pull request, #11, "Research: the backlog". The three stale branches from
4 August — #6 photographs, #7 the 1980s, #8 the 2020s — were closed by the morning
pass and needed nothing further. No other pull request was open.

## Merged
**#11, after corrections.** It adds the last three unverified branch histories: the
Senate 2010-11 to 2016-17, the judiciary of the 1970s, and the governing
constitutions 1966 to 1991. The fifteen accounts already published are untouched —
the file's six thousand changed lines are reformatting, not revision — and
`data/years.json` is not edited at all.

I spot-checked thirty-five claims against their sources rather than against the run
report. Twenty-four Herald and archive citations matched the complete local index
exactly on date, volume, issue number, headline and byline. Six 2016-17 bills read
from the PDFs on wku.edu matched on every reading date and vote count. Four SGA
legislation landing pages matched on every date. Nothing I could check contradicted
its citation, which is a better result than this project usually gets.

## What I cut
One fault, of a single kind. A few entries stated detail from inside a PDF as
flatly as the facts that were confirmed, when the checking passes could only reach
landing pages. The block applies the right standard in three places and then fails
to apply it four entries away. I rescued rather than deleted: every fact and every
citation survives, correctly attributed.

- The 26 March 1976 Herald entry attributed a three-fourths removal threshold and a
  thirty-minute limit on discussion to a headline saying only that the Faulk
  impeachment hearings had opened. A headline carries neither. Rewritten to what it
  proves; Steve Henry's offices re-attributed to the 1976 Talisman, which does
  carry them.
- Two entries drawn from the Herald of 7 September 1978. I fetched that record in
  full: it yields an article list and nothing more. Both now say so, as does the
  sentence in the judiciary summary that carried the same detail to the reader.
- The Financial Advisory Council entry keeps the bill's dates, which its TopSCHOLAR
  record gives, and marks the composition and the 26-to-4 vote as resting on the
  bill's unread text.

No trap in the checklist was tripped. Advance notices are worded to what a notice
proves; chairmen are kept distinct from members; nobody is matched by surname; no
April election is filed into the wrong year; the Thompson letter supports the
settled reading of Reed Morgan instead of reopening it; and both conduct matters in
the judiciary account state their outcomes.

## Two notes for the next run
**pypdf now works.** The morning report recorded that no PDF text extractor
functions here, pypdf failing on its crypto import. The cause is a broken `cffi`
backend, and `pip install --upgrade cffi` fixes it. I read six wku.edu bill PDFs
this way. The 8 November 2022 minutes, mirrored but unread, can now be read, and so
can the legislation archive.

**The blocked sources are genuinely blocked.** `viewcontent.cgi` returns the AWS WAF
challenge — HTTP 202, zero bytes — while landing pages return 200. This is not the
burst-rate 403 that patience cures. Landing pages, `archive.org` and `wku.edu` are
all open; plan around the PDFs rather than against them.

## Where the record stands
61 years, 1,878 dated events, 60 people who have been president, 34 documents, 390
legislation files, and now all 18 branch accounts published, so the "what is missing
here" note has correctly disappeared from that page. `build.py`, `check_data.py` and
`check_contrib.py` all clean. `check_duplicates.py` reports the same six pairs as
before; all six are separate events and none come from this work.

## Still open
- Four leaders have no portrait: Nick Todd and Katie Dawson (2004-05), Jeanne
  Johnson (2006-07), Reagan Gilley (2008-09).
- The 235 unmerged branch-research moments in `.research/branches-moments.json`.
- The senate rolls, the three years without a cabinet, the Amanda Coates/Lich
  identity question, roughly 20 weak citations, and the pre-2011 TopSCHOLAR
  legislation.
- The research routines still branch from the orphaned 4 August snapshots. Until
  they cut from `origin/main`, their work will keep arriving unmergeable.

---

# 18 August 2026, evening — editorial pass

Three research pull requests were open. All three are merged, none of them exactly
as they arrived.

## What was reviewed

**#12, the cabinet accounts (merged).** Twenty executive officers from 1971-72
through 1976-77 given a full account of their term, plus a genuine rendering fix:
`profile` was reaching the data and never reaching a reader on officer pages,
so batch one's work had been sitting invisible. Fourteen claims were opened
against their sources — the 1972-1977 Talisman full texts and the Herald index —
and thirteen held, several word for word: Reginald Glass as the first Black vice
president, Boteler as McGovern's campus co-ordinator and an alternate delegate,
Christy Vogt's whole path from Angela Merici High School to the presidency,
the January 1976 book exchange down to the 25 cents a book.

Four things were corrected before it went out. Rick Kelley's 1976-77 account had
cut his own words down to "sold out" and then set them against the yearbook's
report that the Chicago concert was not a sellout. What he said was that the show
sold out of *advance* tickets and grossed over $50,000, which the yearbook does
not contradict. That is the worst kind of error this project can make: it invents
a disagreement and puts a man on the wrong side of it. His 1975-76 account called
the Ronstadt concert the year's most successful show financially, a ranking the
Talisman never makes. Tom Blair's said the record does not preserve what his
charges against Steve Henry concerned, when the archive already records them.
And Stan McDivitt's entry still cited the Herald issue of 7 February 1975 for a
post that issue does not mention him holding.

**#13, the senate rolls (merged after rewriting).** The archive has never
recorded a single rank-and-file Congress member. It now records 104, across
1970-71 to 1975-76, each with its own source. The research is sound and in one
place better than sound: the reading of the 1973 constitutional revision, which
put class presidents and vice presidents on the roll of Congress from 1972-73 but
not before, is correct and correctly argued, and it is why eleven 1971-72 class
officers were rightly left out. The 1976 attendance roll is the find of the pass —
the ASG's own printed Congress roster, effective 6 April 1976, with a
meetings-missed column and a line recording Mitchell Deep's resignation.

It could not be published as written. Forty of the 104 notes were verification
memos rather than history, arguing about vote counts and seat assignments that
were correctly never published, in the voice of a checker: a source "confirms in
full," a figure is "Herald-only and unconfirmed," something "could not be read
this session." A reader would have met a rebuttal of claims they cannot see. The
notes also reproduced about 1,170 words of Talisman prose verbatim, one Lambda Chi
Alpha sentence printed three times over because three men were named in it,
against a standing rule of one quote under fifteen words per source. Forty-seven
notes and three seat lines were rewritten as plain history. Nothing sourced was
lost, and every real limit survived in ordinary words.

**#14, the photographs (merged in part).** Nick Todd and Reagan Gilley have
portraits for the first time, and Katie Dawson's and Jeanne Johnson's existing
portraits now cover their acting and mid-year terms, so no leader is left without
a face. Three further headshots cut from the same 2004 election guide are held
back. No caption was quoted for any of them, and Sarah Cecil's picture comes from
an article covering two women, Alicia Bachicha and Sarah Cecil, so which face
carries which name rests entirely on having read the page right. The Herald PDFs
would not open from here to check. Quoting the caption beside each photograph
restores all three; the files were removed so nothing half-verified sits waiting
to be picked up.

## What this pass suggests about the routines

Both #12's real errors and #13's presentation problem come from the same place:
the checking step producing text that then gets published. A quoted claim is
evidence of what someone said, not of what happened, and a verifier's verdict
belongs in `.research/`, not in a `note` a reader will see. If a claim did not
survive, drop the claim rather than publishing an argument against it.

## Left open deliberately

The name fragmentation the senate rolls introduce: Michael and Mike Inman,
Christy Kay Vogt and Christy Vogt, Carl Stolzfus and Stoltzfus, Frank Mendaris
and Medaris almost certainly each denote one person, and `name-aliases.json`
exists for it. No aliases were added, because an alias asserts two names are one
human. **Thomas A. Blair needs care:** the 1975 senior directory has him a senior
in 1974-75, which sits badly with the Tom Blair elected administrative vice
president for 1976-77, and the 1976 roll carries both a Tom and a Becky Blair.

Also still open: Katie Dawson's portrait is sourced to a commercial newspaper
rather than a university archive, and should be replaced when a WKU-held image
turns up. And #12's `build.py` change steps outside the rule that `years.json` is
the only file edited; it was kept because it fixed a real rendering gap, but the
rule is worth restating to the routines.

## Where the record stands

61 years, 1,878 dated events, 60 people who have been president, 104 Congress
members, 34 documents, 390 legislation files. `build.py`, `check_data.py` and
`check_contrib.py` all exit clean. `check_duplicates.py` reports the same six
pairs as before; all six are separate events — three months between the
designated-driver items, a plan and an event for the Pride Week coffee house,
same-day bills in 1991-92 — and none come from this work.

One note the previous report can be marked resolved on: the research routines are
no longer branching from the orphaned 4 August snapshots. All three of these
branched from current `main` and merged normally.

---

# 18 August 2026, second editorial pass

Four research pull requests open at the start: #15 photographs, #16 profiles,
#17 the senate rolls, #18 the branch-history backlog. The three stale branches
of 4 August that the last pass flagged are gone. Three merged; one is held open
with corrections pushed. All four branches had cut from current `main`, so the
orphan-history problem stayed resolved.

## Merged

**#15, three 2004 headshots.** Jessica Martin, Sarah Cecil and Christina
Kayrouz, off the *Decision 2004* election guide of 16 March. I re-derived the
identifications rather than accepting them: the page's text-block coordinates
put Alicia Bachicha's article and Sarah Cecil's photograph on opposite sides of
the page, which settles the swap risk the previous reviewer raised, and
rendering the page confirmed each photograph under its own headline. Martin was
the exception. There is no photograph under her headline; her portrait sits in
the shaded candidate-profile box between her article and Nick Todd's, and that
box is hers beyond doubt — public relations and sociology, the vice presidency
of administration, PRSSA, the Northeast Hall residency, none of which fit Todd.
The identification was right and the description of it was wrong.

All three captions were rewritten. They had reproduced whole Herald sentences,
seventeen and eighteen words, three quotations from one source, which is over
the archive's limit and not a fair use of a student newspaper. The
reviewer-facing note about comparing two faces came out of Cecil's caption; that
evidence belongs in the pull request, not on the page.

**#16, eighteen cabinet profiles, 1977-79 and 1985-87.** A second batch arrived
on the branch mid-review and was checked with the rest. Every quotation sampled
was exact against the 1978, 1979, 1986 and 1987 Talisman: the "light moment"
caption naming Moore, Bass, May and Murphy; Shockley's "It's tedious and
requires a lot of work"; "Be Kind to Tricia Day"; Young's "force some heads-up
competition"; Carwell's three tests for a promoter, 500 miles, 75 concerts,
$2 million; Elder's "We take students' wants and translate them into action and
results"; Rodriguez's retreat, 45 of a possible 75, and "a great way to finish"
after Kern Alexander's breakfast; Barbara Rush taking notes at Nick Kafoglis's
lecture. Bass's crowd of 3,300 comes from the Herald's report after the
concert, not from the notice before it.

Cut: Cathy Murphy's profile claimed she had won a freshman office in September
1975. The headline is real, correctly dated and correctly quoted, but the
identification is an assumption, and the 1978 Talisman lists two Cathy Murphys —
a senior from Owensboro reading government and public relations, and a second
from Louisville. A 1975 freshman would not be a senior in the 1978 book. The
headline now stands with the identification declared open. Also removed from
David Bass's `note` the detail that students entered the free April 1978 concert
on a Western ID: the run's own verifier had cut it from his profile as
unsupported, but it was still in the note and still on the site. A rejected
claim that survives in a neighbouring field is published just the same.

**#18, the branch-history backlog.** 138 dated moments across sixty years,
clearing `.research/branches-moments.json`. The best-disciplined branch this
project has produced. Eleven claims sampled and all eleven held: eight Herald
index items matched on headline, byline, issue and date, and three modern
documents — the Judicial Council minutes of 3 December 2021, the bill sheet for
13-22-S, and Resolution 3-15-S — read in full and matched to the word. Nothing
cut. The entries built on index-only issues say so in their own text instead of
inventing detail, the living-people handling names no senator the minutes name
for absences, and the Michel/Mitchell Stephens conflict is stated both ways with
both sources and declared unresolved. All seven duplicate pairs read and judged
separate.

## Held open

**#17, the senate rolls.** Corrections pushed, merge refused. The research is
sound and the membership rule — a floor motion or a roll call establishes
membership, a committee report does not — is the right one, applied
consistently. The dating survived the trap that could have wrecked it: the item
pages record `22-2-1977` day-first, and the run read them correctly. But the
names were taken off the OCR text layer of scanned typescript, and rendering
three of those pages as images found three errors:

- Bill No. 12 passed **31/0/1**, not 31-9-1; the wrong tally appeared three
  times. The 34/0/1 in the same paragraph was recorded correctly, which is the
  tell: a zero read as a nine.
- The 22 February 1977 minutes name **George Carlson**, not Georgiana. The note
  called the given name illegible and reconstructed it from the 1977-78 treasury
  candidate. On the page it is not illegible. Substituting a woman's name for
  the man's name in the source, to match someone already on file, is the error
  this archive least can afford.
- The roll of 11 November 1980 records **Maura Fleenor**, not Laura.

Probably a fourth: the International Students chairman is **Sharif** in those
minutes against **Shariff** in the record, from a different meeting, so it wants
checking rather than assuming.

Three errors in roughly ten names sampled, out of thirty-three, all from the
same cause. The next run must re-verify every name by rendering the page region
and looking at it. The embedded text is good for finding the page and useless
for deciding a spelling.

## New finding: the complete index is not complete

`data/herald-index-full.json` is truncated. 3,898 of its 11,850 entries carry an
opening `<li>` with no closing `</ul>`: their article lists stop partway. The
1991 Kevin Colon headline is real and on the live landing page, and invisible
locally for this reason. Every routine is told to grep this file first, so a
third of it silently under-reporting is a live hazard — a miss in the local
index is not evidence of absence. It wants a re-harvest.

Also noticed: `site/photos/` on `main` carried the Martin, Cecil and Kayrouz
files from before #14 held them back, orphaned with no entry in `photos.json`.
#15 makes them legitimate. Stale build output surviving a data-side revert is
worth watching for.

## Where the record stands

61 years, 2,015 dated events, 60 people who have been president, 34 documents,
390 legislation files. `build.py`, `check_data.py` and `check_contrib.py` all
exit clean. `check_duplicates.py` reports seven pairs, all separate events, none
introduced by this work.

---

# Night of 18 August 2026 — editor pass

Four open research PRs reviewed, all four merged to main after corrections.
GitHub was reachable this run (push and merge both worked); the merges are live.

## #17 — the senate rolls — MERGED after five fixes

The Congress roll for 1976-77, 1977-78, 1979-80 and 1980-81. A prior editor had
blocked it over OCR misreads; a re-verification pass answered that by rendering
the scans as images. I could not re-read the PDFs — `viewcontent.cgi` returns
HTTP 202 with an empty body here — so I checked the year a different way, against
the 1981 Talisman on archive.org, an independent source for the same body. It
vindicated every contested reading (Bussell, Ragan, Maura Fleenor, Humphrey all
confirmed in the ASG group photo caption and index). The 1977-78 and 1979-80
Talisman additions are verbatim. Five corrections of my own:

- Minutes/272 is **20 January 1981**, not 29 — carried in four places, all fixed.
- A Freshman Class President election was written up twice with the two
  candidates' vote figures transposed; both entries now say Holland beat Hines
  and give no tally.
- Osama **Sharif** (the 1981 Talisman prints it three times), not Shariff.
- **M. A. Baker** kept and properly sourced: the Talisman names him the Cincinnati
  senior who authored the room-inspection resolution.
- **Bruce Berton** and **Jim McCord** withdrawn — each carried its own admission of
  being a garbled-scan reconstruction. Alan Jackson and Debbie Thomas moved out of
  members (committee chairs only), per the archive's own rule.

## #20 — the backlog — MERGED after one trim

An audit of 92 candidate officers, 89 rejected with specific reasons — the best-
disciplined batch this run. Two survivors verified: **Paul J. Deom** (Judicial
Council, year confirmed independently by the 1981 Talisman) and **Mark Wilson**
(administrative VP, quote and both vote counts verbatim in the Talisman). Trim:
Wilson's note carried an election date, an 821-342 tally and a middle name none
of which are in the cited source — cut, while the same audit had correctly
trimmed an identically shaped tally for Zoeller two rows down. Lesson logged on
the PR: an `accept` verdict still has to cut the note back to what `verify_reason`
actually covers.

## #21 — person profiles — MERGED after cutting an invented election

Twelve officer profiles, 1988-89 to 1990-91, built from ASG minutes. All nine
minutes citations exact, two abstracts corroborating outright (Hennig's
resignation, the freshman elections). **Cut:** three profiles claimed Knowles and
Falmlen were "top two in the primary" and "advanced to the runoff" in April 1991.
No source says so; the full landing pages for all three election issues describe
one election, "three clear-cut" results on 11 April, no primary and no runoff.
The real smear-campaign report was rescued — restated to what the headline proves,
outcome-unknown said plainly (living person), and given its own sourced event.

**Correction I had to make to my own review:** I first cited the local
`herald-index-full.json` as proof of absence. It is truncated (see below) and all
three 1991 entries are cut off mid-list. Re-verified against the live landing
pages; the finding held, but the index must not be trusted for negatives.

## #22 — photographs — MERGED after one caption fix

Six officer portraits from the early-1970s Talismans, all real JPEGs, each
identified from the yearbook's own caption. Reginald Glass's name tag is legible
in the scan (REGINALD GLASS). LaCivita and Pat Newton verbatim; the Nancy Pape
crop-by-position inference checked out against the uncropped group photo already
on main. **Fix:** the Kirkpatrick caption called her "ASG secretary" over a 1974
Talisman photo whose caption gives no office and in a year the secretary was Pam
Stewart; the office is 1974-75, from the 1975 Talisman. Caption corrected to say
so.

## Standing hazard, re-confirmed

`data/herald-index-full.json` is still truncated — 3,898 of 11,850 entries have
article lists that stop partway (`<li>` with no closing `</ul>`). Every routine
greps it first, so a miss there is not absence. It nearly cost this run a wrong
negative finding. Needs a re-harvest. Landing pages carry the full lists at one
request each and are richer than the local subset.

## Where the record stands after this pass

61 years, 2,016 dated events, 60 people who have been president, 1,052 officer
records, 136 senate members recorded, 58 years with a cabinet, 54 officer
profiles, 34 documents, 390 legislation files. Photographs: 73 leaders, 17 year
photos. `build.py`, `check_data.py` and `check_contrib.py` all exit clean on main.
`check_duplicates.py` reports seven pairs, all separate events, none introduced
by this work.

Stale PRs #6, #7, #8 (photos / 1980s / 2020s, open since 4 August) were already
closed on 18 August at 04:57, before this run — no action needed.

---

# Night report - 18 August 2026, fourth editorial pass

Two research pull requests open, both merged. The lasting result of the pass is
not either of them: it is that the tool all four routines are told to search
first has been quietly lying to them, and is now fixed.

## #23 - the backlog - MERGED, with the finding strengthened

The claim was that Amanda Coates, president 1999-2000, is the plaque's "Amanda
Lich". I downloaded the cited Council on Postsecondary Education minutes of 30
July 2001 and they say it exactly: the oath went to Christopher J. Pace,
appointed "to replace Amanda Coates Lich." The two Herald citations behind her
entry (`dlsc_ua_records/8117` and `8053`) both check out headline for headline.
The three citations the branch dropped were genuine duplicates of entries already
held on better permalinks, so that cleanup stands.

But the 2001 minutes never mention Western. On their own they prove a person
named Amanda Coates Lich sat in Kentucky's statewide student seat - not that she
is our president. So I went back through the council's own record for the sitting
where she arrived, and the minutes of **13 November 2000** introduce the incoming
student member as Amanda Coates, "a graduate of Western Kentucky University",
sworn in that morning by a district judge. That is the half the identification
was missing. Both sittings are now cited: the first carries Coates of Western
into the seat, the second carries the surname Lich out of it. The profile's old
line calling the 2001 minutes "the only public record found" is gone, being no
longer true.

Also folded in: two accounts of Joe Rains taking office on 21 April 1992, written
up twice from the same Herald issue under different titles, combined into one
entry keeping every sourced fact from both. `check_duplicates.py` never saw it
because the two titles share almost no words.

## #24 - person profiles - MERGED as is, nothing cut

Eleven early-1990s executive officers. The review shortcut worth recording: all
23 paragraphs restate facts already published in each officer's `note` on main,
so only three claims were actually new. Holcomb's "roughly 1,200 students voting"
is carried by the 16 April 1992 issue, which runs the turnout as its own story
alongside the result. Sivley's two new claims are carried by the 14 and 21 April
1994 issues. Both of the routine's own trims were right.

## The thing that matters more than either PR

I nearly cut Sivley's paragraph. `herald-index-full.json` lists exactly one
article for the 14 April 1994 issue, and nothing about Sivley, an election or a
procedure, in that issue or any 1994 issue. So the claim looked invented.

The live landing page for that issue carries **thirty-seven** articles, including
"Scott Sivley Didn't Follow Student Government Association, University Procedures"
and "Student Government Association Tallies Votes From Primary Election." The
research was right and the index was wrong.

Yesterday's pass noticed this and described it as article lists that "stop
partway". It is sharper than that, and it has a cause. Every line in the file is
cut at exactly 300 characters - the longest of all 17,601 lines is 300, and 5,892
of them (33.5%) sit on that cap, sliced mid-word. A Herald issue's abstract is a
single `<ul>` of thirty or more `<li>` headlines arriving as **one** line, so what
survived locally was the first two or three headlines of each issue and nothing
else.

Two bugs in `harvest_herald_index.py`, both now fixed:

1. The `--all` path truncated every line at 300 characters. It now splits the
   list into one headline per line and keeps them whole, with tags and HTML
   entities resolved so a plain grep matches a name.
2. Worse, the resume logic skipped any URL already on disk, so a bad parse
   already written could never be repaired by rerunning - every rerun printed
   "done" and changed nothing. A new `--refresh` flag reparses what is already
   held.

The full index has been re-harvested with the fix, and the scale of what had
been lost is worth stating plainly: the same 11,850 items now hold **141,079
article lines where they held 17,601**. Eight times the searchable record, from
the same archive, with nothing newly fetched - it had all been harvested and
then thrown away at the parse. The 14 April 1994 issue now carries 35 headlines
instead of one, the Sivley story among them. No line is capped any more; the
longest runs to 2,866 characters.

This is not a small correction. CLAUDE.md called that file "the complete article
index" and instructs every routine to grep it first, which together manufacture
false negatives: a routine greps, finds nothing, and cuts a true claim or writes
"no source found". That very likely happened already - section 8 of the handoff
records 97 dated moments cut in one pass and 68 officer candidates rejected
because the source "didn't say what was claimed". Those deserve a re-check
against the repaired index rather than standing as disproven.

CLAUDE.md is corrected accordingly: the file is no longer described as complete,
the truncation is documented with this issue as the worked example, and the rule
is now explicit - **a hit is good evidence, a miss is not evidence of absence**,
and no claim may be cut on a local miss without opening the landing page first.

## Also worth knowing

The SGA minutes landing pages that #24's profiles cite (`/sga/Meetings/Minutes/`
402, 414, 451, 500) return only a one-line agenda list and never an individual's
name. The PDFs behind them still answer `viewcontent.cgi` with HTTP 202 bot-check
HTML rather than a file, so the granular figures in those profiles cannot be
re-verified from source in this environment; they rest on the earlier pass that
had the PDFs. The `cpe.ky.gov` PDFs, by contrast, download cleanly.

## Stale branches

PRs #6, #7 and #8 were already closed on 18 August at 04:57, before this run. The
six 4-August `research-*` branches still on origin remain orphan snapshots with no
merge base against main, holding about 800 events each against main's 2,015. They
are superseded, not salvageable by merge, and are left closed.

## Where the record stands after this pass

61 years, 2,015 dated events, 60 people who have been president, 73 leader
records with a profile each, 438 executive officer records of which 65 carry a
profile, 614 senate officers, 136 senate members, 58 years with a cabinet, 25
documents, 390 legislation files, 73 leader portraits and 17 year photographs.
`build.py`, `check_data.py` and `check_contrib.py` all exit clean on main, and
main's committed `site/` matches a fresh build. `check_duplicates.py` reports
seven pairs; all seven are genuinely separate events - staged actions weeks apart,
or same-day bills - and none were introduced by this work.

---

# Editor pass, 18 August 2026, evening

Four research pull requests were open. All four were verified and all four are
merged. Every merge published to the live site.

## What was reviewed, and what was cut

**#26, the senate rolls.** 105 rank-and-file senators for seven years that had
none, taken from the seats printed beside the names in SGA's own bills. Because
every cited bill is already mirrored in `data/legislation/`, this was checkable
in full rather than by sample: all 105 names appear verbatim in the PDF cited
for them, and all 105 carry the word Senator immediately beside the name in the
AUTHORS or CONTACTS block. Not one was inferred from authorship, which is the
error that killed the "39 missing presidents" batch. Where a senator also chaired
a committee the seat was recorded and the chair went in the note, which is the
right way round.

Two cuts. **Kahlil Garmon and Roderick Maul** came off the 2021-22 roll — the
only evidence for either is a bill of the 2021-22 session calling them a *former*
senator, in January and March 2022. A sweep of all 390 mirrored PDFs found
nothing else for either name. "Former senator in January 2022" establishes that a
person served, not when, and it could as easily mean 2020-21. Both are now named
in the Senate note for 2021-22 with the bills and the reason neither is on the
roll. **Maksim Zaepfel and Maksim Zaephel** were merged into one entry: the two
spellings had been kept as two senators rather than guess between them, which was
the right instinct and the wrong result, since one person then appeared twice in
one year's roll. One entry now, under the earlier bill's spelling, recording that
the session's own bills disagree and do not settle it. 103 senators merged.

**#27, ten founding-era profiles**, 1966-67 to 1970-71. The 3 May 1968 election
memo is mirrored locally, so the vote counts were checkable directly: Becky
Cooper 1,551 to Mary Miller's 1,122, Tonii Rizzo 1,896 to John Combs's 803, and
turnout of 2,894, about 34 per cent, are all printed in it. Ron Beck did sign it
as vice president. Every Herald claim matched its index line, including the two
8 May 1969 items on the outgoing administration, both in that issue.

Three trims. **Terry Gilpin's vote count** had been reconstructed by reading down
a column: the memo does print 1,516 and 1,206 for the vice-presidential race, but
in a numeric column set apart from the names, and nothing in it says which is
whose. The profile now says what the memo shows, and that Gilpin took the office.
**A sentence in David Porter's profile** was cut whole — it rested on a headline
the profile itself said had never been read, and placed it earlier in the term
than the issue it came from. **Doug Alexander's election date** and its sequence
with the presidential race were cut: no cited source gives a polling day, and
Lyne's unopposed win was reported a fortnight before, not a week.

**#28, six Talisman photographs** for years that had none. Each caption was
checked against the yearbook's own words, pulled from the volume's OCR layer on
archive.org. The 1980-81 group portrait was the one I expected to fail, because
the crop carries bleed-in text about Palestine and Zacharias that reads like a
different article; it is not — the 1981 volume runs the student-opinion-poll
story straight into the group photo's name key, and both officers our caption
names are in its back row. For Nancy Wilk I fetched page 87 itself rather than
trust OCR, because a portrait crop carries no caption of its own and that spread
labels six portraits: the bottom-left portrait is captioned Nancy Wilk and is
pixel-for-pixel the committed crop.

Two caption corrections. **"in Downing University Center"** came out of the
1978-79 caption — the yearbook gives a date and a president and no room at all.
And the 1976-77 caption had 379 as the turnout of "the fall 1976 ASG election";
the yearbook is narrower, those 379 votes decided the freshman class president
and vice president, and for an organisation whose turnout figures are part of its
history that is the wrong impression to leave.

**#29, sixteen citations resting on homepage captures.** All eight new permalinks
verified against the cited issue's full headline list: right date, right volume
and issue, headline present, eight for eight. The date correction from 3 to 2
March 2006 is right. All three of the verifier's own trims were correct, and one
was the advance-notice trap by name — Gov. Beshear's address to the 2010 Rally
for Higher Education had been written up as something that happened, out of a
preview published a week before it.

Two prose fixes, neither a sourcing problem. Four events had picked up a
parenthetical mid-narrative explaining that the citation was a Wayback front page
rather than the article. The transparency is right and every word of its
substance is kept, but it belongs on the source label, where the reader is
already looking at the link — the same pattern this pass had already used for the
leader records. And the 40th-anniversary entry was describing its own drafting,
telling readers what "an earlier draft of this entry" had claimed; it now says
what the surviving headline shows and what it does not.

## Left open for the owner to decide

The photograph routine reached a real wall and stopped at it correctly. There is
**no rendering path for an officer portrait at all**: `apply_photo_overlay()`
only matches a `photos.json` leaders entry to a name in a year's `leaders` array,
and `check_photos()` refuses an entry for anyone outside it, so a vice president
or a speaker cannot carry a portrait however well captioned. Two good candidates
(Cindy Kirkpatrick and Thomas LaCivita, 1974-75) are filed under the `years`
schema as a workaround. Fixing it means either giving officer records their own
identity for the overlay to match, or a second overlay list keyed another way.
That is a schema decision, not a per-run workaround, and it is left here rather
than settled inside a photograph run.

## Stale branches

Nothing to do. PRs #6, #7 and #8 were already closed on 18 August at 04:57,
before this run. The six 4-August `research-*` branches remain orphan snapshots
with no merge base against main and are left as they are.

## Where the record stands after this pass

61 years, 2,015 dated events, 60 people who have been president, 73 leader
records each with a profile, 438 executive officer records of which 76 carry a
profile, 614 senate officers, **238 senate members** (up from 136), 390
legislation files, 73 leader portraits and 23 year photographs. `build.py`,
`check_data.py` and `check_contrib.py` all exit clean on main.
`check_duplicates.py` reports the same seven pairs it reported before this
evening; all seven are genuinely separate events, and none came from this work.

---

# 19 August 2026 — editor's pass, small hours

Two pull requests open, both cut from current main with a proper merge base.
One merged, one refused.

## Merged: #30, profiles for the 1994-99 cabinets

Twenty-three officers of the mid- and late-1990s executive cabinets gained
profiles. Almost every sentence restates an officer note already on file, which
is the right way to build one, so the check was mostly a matter of confirming
that the profile says what the note says and that the note's source says both.

Two entries confirmed themselves outright when the cited record was opened:
TopSCHOLAR catalogues `Documents/Reports/14` as a letter to interim president
Barbara Burch "from Jamie Fite, SGA secretary" about seating in Diddle Arena and
Smith Stadium, and the minutes of 19 January 1999 as covering the introduction
of vice president Cassie Martin. Eight more held up at the level of the
meeting's own topic list — the budget and the swearing-in on 27 August 1996,
provide-a-ride and the blood drive on 18 November 1997, the retreat goals and
the new website in the autumn of 1998. Three Herald letters cited in the
profiles — Shawna Whartenby's on the constitutional amendments, Richard Malek's
"puppet" charge, and Tracie Webb's defence of Horace Johnson — were all found in
the unfiltered index at the issues claimed.

The run also corrected a fact that had been wrong on the site: Ryan Morrison's
1998-99 note said he won the presidency a fortnight after 13 April 1999. The
archive's own 1999-00 record says the 26 April re-run was for vice president of
finance. The routine found its own error while researching something else and
fixed it, which is how that should go.

Five cuts before merging. Two treasurer's figures for 1994-95 came out because
the meeting's landing page carries only a topic list and the PDF sits behind
TopSCHOLAR's bot gate; they are flagged on the pull request for restoration
rather than dismissed. A Herald letter came out of Steve Roadcap's profile
because the issue it is in is cited nowhere in that year, leaving a reader no
way to check it. Carlene Lodmell's profile had a citation caveat written into
the published text, hedging a passage the year's own note states plainly, so the
hedge went and the sourced version went in. Horace Johnson's profile carried
three quoted fragments from a single Herald issue, all three already printed
verbatim in that year's events; it now records the one letter that names him.

And a duplicate that was nobody's fault in this pull request: 1995-96 had
carried the Herald's attack on the skywalk twice, as "The Herald pushes back"
and "The skywalk drew fire within a week," same date, same source, since before
this run. `check_duplicates.py` never saw them because the titles share no
words. Folded into one entry keeping every sourced fact from both.

## Refused: #31, the senate rolls

The rosters in this branch were read off the OCR text layer of the mirrored
minutes. Nobody opened the page images. Rendered at 200 dpi the scans are
legible, and three pages produced seven wrong names or seats.

The 29 April 1982 appointments page gives Sammy Abell, not Sandy; Jorge Garcia
as an on-campus representative, not a Jorge Perez whose surname the branch calls
degraded; Dave Hoffman as the off-campus representative, in a roster the branch
says he does not appear in; Melody Murphy as graduate representative, not Ogden
College; and Susan Beth Tinsley, whose forename the branch says is not legible,
paired with Barry Deweese. The absence list of 20 October 1981 reads Bridget
Wyatt, not Hyatt. The housing report of 29 August 1978 is Shaun Bryant, not
Shawn.

What makes this worse than a run of typos is the hedging. Three of the errors
arrived wrapped in a note telling the reader the scan is illegible at exactly
the point where it is not. A wrong fact wearing a disclaimer still reads as a
fact, and the disclaimer is what stops anyone checking it.

Two entries were people assembled out of parts — John Holland, forename from one
meeting and surname from another, and Tony Whalen, the same in reverse, with the
note admitting as much. Both removed.

Left open, and left for the routine rather than settled here, is the shape of
the thing: some twenty entries sit under `senate.members` above a note saying
membership is not established, two of them on the strength of having moved
adjournment once. People named in a roll-call absence list are members and those
entries are sound. The rest need a home that does not assert what the record
cannot show.

Seven corrections and both removals are pushed to `research-senate`, along with
three document extracts trimmed back under the quote limit and a restored
trailing newline on `years.json`. The twelve mirrored PDFs are genuine files,
165 KB to 547 KB, all beginning `%PDF-`. The validators pass on that branch and
always did, which is the point: they cannot tell you a name is wrong.

The 1978-79 minutes in that branch are cleanly typed and their entries check out
against the page — Buzz Smith on the Complaint Committee, Terri Craig on SGAK,
Dave Roberts on Rules and Elections, Rita Young's appointment to Congress. That
year could be split out and merged on its own.

## Where the record stands after this pass

61 years, 2,014 dated events, 60 people who have been president, 73 leader
records all with profiles, 438 executive officer records of which 98 now carry a
profile, 614 senate officers, 238 senate members, 390 legislation files.
`build.py`, `check_data.py` and `check_contrib.py` all exit clean on main.
`check_duplicates.py` reports seven pairs, the same seven as yesterday, all
genuinely separate events — the eighth, in 1995-96, was folded away tonight and
the checker had never been able to see it.

---

## 19 August 2026, second pass — four branches merged

Four research pull requests were open and all four are now on main: the Congress
rolls (#31), the pre-2011 legislation harvest (#33), three officer photographs
(#34) and ten officer profiles (#35). The three stale branches from 4 August that
the standing brief still names — #6, #7 and #8 — were already closed and needed
nothing.

### The senate rolls, #31

This is the branch that was refused last night over seven names read off an OCR
text layer instead of the page. The routine went back to the images, and the
seven corrections and both removals hold: the appointments page of 29 April 1982
reads Sammy Abell, Jorge Garcia, Dave Hoffman as off-campus representative,
Melody Murphy as graduate representative, Susan Beth Tinsley paired with Barry
Deweese. It then found twelve more names further down the same page and the
year's first three executive officers, and all of them are on the page. Page two
gives Brian Shaw as parliamentarian, Robert Cook as sergeant-at-arms, Claire
Groemling and Melanie Harding in the chairs, and Doug Ball resigning the seat he
had just been given.

The 1993-94 roll was checked name by name against both sets of minutes. The
absence lists of 12 October 1993 and 29 March 1994 carry twenty names between
them; every one is either in the branch or already in the record as an officer,
and nothing is in the branch that is not on those lists. Terra Swanson's
election, the McCarty and Haycraft vacancy fills and Rob Evans's Congress Member
of the Month all read as written. The Fall 1994 membership list pairs to the
seat column exactly, including the two names the routine correctly held back as
duplicates of chairs already recorded.

Three things were wrong or missing and are fixed on the branch. Erin Schepman's
note said she was elected secretary the following year; she was elected on 18
April 1995 and served in 1995-96, which is two years on, not one. The absence
list of 20 October 1981 has four names and only three were taken from it, so
Greg Jennings is added. The same page names Public Affairs Vice-President Laura
Simms and Secretary Alesia Canafax, both of whom the branch's own notes already
lean on without recording them; both are now in the 1981-82 executive.

On the structural argument left open last night: the routine dropped the two
thinnest entries and left the rest, and the labelling is now honest. No entry
claims a Congress seat in the field a reader sees while its note denies one —
the committee people are filed under the committee they reported for, and the
two whose membership is not established say so in the seat itself. That is what
was asked for.

### The legislation, #33

Four hundred and thirty-seven bills and resolutions from 1975-76 to 2008-09.
Every file is present, every one begins `%PDF`, none is a bot-check page saved
under a PDF name, and no source URL or filename is duplicated. Ten were opened
at random across five decades and the number, title and date inside each
document match what the index claims for it. Three item pages were checked
against TopSCHOLAR itself: the titles are exact and the dates match once the
archive's day-month-year display is read correctly, which the harvester does.
The session mapping is right, including the June 1976 and January 1979 items
that fall in the awkward part of the rule.

### The photographs, #34

The two 2026-27 portraits are crops from one Herald group photograph. The
caption names the three men left to right — Barker, Lucas, Derryberry — and the
crops match that order against the original, which I fetched and compared. The
Nolan Miles caption claimed the portrait was taken for his 2016 letter to
students; the page shows only that it was published with it, so the caption is
trimmed to that, and to the two years in office the letter itself claims.

### The profiles, #35

Ten officers between 1966 and 1973, and every fact traces to a source already in
the year. Bucky Lanning's byline is in the index for the Herald of 27 October
1966, the issue the year already cites. The 1968 election memo is signed Ron
Beck, Vice-President, dated 3 May and addressed to Dr Thompson, exactly as the
Cobelli and Heathcoat profiles say. John Lyne ran unopposed, which the year
records from the Herald of 13 March 1970. The 1973 Talisman carries the Fiorella
paragraph almost word for word: two vice presidents under the new constitution,
Boteler and Fiorella holding them, five concerts, the greatest number of
nationally known groups yet to appear at Western, and the $1.50 fee he wanted
raised.

### Two things wrong on main itself

Neither came from tonight's branches, and both were published.

Sandra Norfleet was still listed as the 1982-83 student regent in that year's
executive block, under a note saying her term ran from mid-February to mid-April
1982. Her leader record has been correctly in 1981-82 since yesterday; the
officer entry had not followed it. This is the one thing the editorial rules
name outright and say not to do again, so it is moved, with the Herald's account
of the runoff written into the note.

The Pride Week coffee house of 5 November 1998 was written as an evening that
happened. Its only source is Bill 98-5-F, which funded and scheduled it. It is
rewritten to what the bill proves, and says plainly that no report of the night
has been found. That also resolves the duplicate pair the checker had been
flagging against the 20 October funding vote.

### Where the record stands

61 years, 2,014 dated events, 60 people who have been president. 73 leader
records, all with profiles. 443 executive officer records, 108 of them with a
profile. 616 senate officers and 332 senate members. 827 pieces of legislation,
up from 390. 99 photographs. `build.py`, `check_data.py` and `check_contrib.py`
all exit clean on main. `check_duplicates.py` is down to six pairs, all of them
genuinely separate events: two bill-then-outcome pairs, a lawsuit and its
endorsement, a policy stand and the vote that followed, and the three bills of
1 September 1991, which were three bills.

### Left for the routines

The 1981-82 executive is still thin: Dave Payne's vice-presidency before he
succeeded Bush is in the minutes and not in the record. The 1994-95 membership
list gives Stephanie McCarty and Bonnie Newton seats — Potter College and
Education — that their chair entries do not carry. And the Congress minutes on
TopSCHOLAR run continuously from 1969 to 2008; almost all of it has still never
been read by anyone, because the PDF endpoint refuses these sessions and the
work has been done from what earlier runs happened to mirror.

---

# 19 August 2026, third pass — one merged, one held

Two pull requests were open, #36 (person profiles) and #37 (the backlog). The
three stale branches from 4 August, #6, #7 and #8, had already been closed by an
earlier pass and needed nothing.

## Merged: #37, the author and sponsor lines from the pre-2011 legislation

120 new attributions read off the AUTHOR: and SPONSOR: lines of the bills and
resolutions pulled down from TopSCHOLAR in the previous run, taking
`legislation-authors.json` from 918 rows to 1,038. Eighteen of the 120 were
checked against the actual PDFs in `data/legislation/`, spread across 1975-76 to
2001-02, and every one matched what the document prints. Nothing was cut: the
change is purely additive, and the 918 rows already on file came back
byte-identical when the extractor was re-run, which is the strongest evidence
that the script did what it claimed.

Two of the new rows corroborate settled facts from outside the plaque — a
1978-79 resolution authored by James E. Hargrove, and a 1981-82 one by Margaret
Ragan — and a 1975-76 bill carries Christy Vogt as sponsor.

The run flagged one spelling doubt, Amos Gott against Amos E. Gatt, and kept
both as printed, which is right. It missed three more of exactly the same kind:
Jarnil Sewell against Jamil Sewell in 2001-02, Lena Sweeten against Leena
Sweeten against Lena Sweeten-Garner in 1993-94, and Andrea Cailles against
Andrea D. Cailles. All are left standing as printed and are noted on the pull
request. The failure mode in this data is incompleteness rather than
misattribution — a 1975-76 bill records its sponsor and drops the two authors
printed above him, a 1989-90 resolution records its author and drops the sponsor
beneath — which is the safe direction to fail in, but it means the index
understates who wrote what.

## Held: #36, the person profiles

Twenty profiles across two batches, twelve for the 1980-85 ASG cabinets and
eight for the 1999-2003 vice presidents, the second batch landing while the
first was being read. Twenty-eight claims were checked. Four failed.

Laura Simms was credited with chairing the Communications Committee "in the same
minutes" that named her Public Affairs Vice President. Our own mirror of those
minutes, 20 October 1981, names one committee chairperson and it is Doug Ball of
student-faculty relations. The chairmanship is real but comes from the meeting
of 9 February 1982, and the entry now says so.

Susan Albert's letter was said to support Kerrie Stewart, "who ran on Margaret
Ragan's ticket and went on to serve as Public Affairs Vice President for
1982-83." This archive already carried the refutation: the Herald of 8 April
1982, cited in 1981-82, has Stewart among the candidates the primary eliminated,
running against Ragan rather than with her, and the minutes of 29 April 1982
make her chairperson of the Public Relations Committee. A committee chair
written up as an officer is the commonest error in this project and it very
nearly reached the site.

Marsha Sanner was given a broadcasting major the 1981 Talisman does not give
her — the volume has her full name, her year and her home town and no major at
all — and Sunshine Promotions was said to have declined to renew its concert
contract when the same yearbook twice says it cancelled it. Both corrected.

In the 1999-2003 batch the gazebo money was described as earmarked for "a gazebo
and other campus improvements", a bridge between the $13,000 of the October 2002
report and the $5,000 of the September one that neither source supports; Anna
Coats was credited with organising a forum the Herald credits her only with
speaking about; and two 2002 election facts were carried on the strength of the
Herald index rather than a citation, so the issue dates are now in the prose.

What held up was substantial. The minutes of 29 April 1982 were exact on all six
things three profiles take from them. The 1981 Talisman was exact on the
inspections votes, 16-13 and then 24-9 with three abstentions. Both 1999 vote
counts match the election box in our mirrored Herald 74:51 to the digit, as do
Amy Caswell's, and the whole gazebo account matches the Herald of 1 October 2002
line for line, with Bedo and Martin named as Pruitt's attribution of
responsibility rather than as the archive's own finding. The three separate Jack
Smiths were kept apart and Hoffman against Hoffmann was flagged rather than
merged, both correctly.

It is not merged for two reasons. Four failures in twenty-eight is too high, and
two of them are the same mistake — a sentence pinned to a document nobody
re-opened, in one case contradicting a year this archive had already published.
And the PDF endpoint at digitalcommons refused every request this run, 202 with
an empty body even after a 95-second backoff, so the minutes of 2 September,
7 October and 11 November 1980 and 18 September and 16 October 1984 could not be
opened at all. Seven profiles rest on those. A source that cannot be reached is
neither confirmed nor refuted, so nothing was cut for it, but at that error rate
it will not be published unread either. Most of what those seven assert restates
notes already on main, so the exposure is to the newly written detail only.

One thing in the run's own report is wrong and worth recording. It claims its
verifier caught a fabricated quote attributed to Mark Wilson. The quote is
genuine — the 1981 Talisman prints it in the Kentucky Civil Liberties Union
section, and the replacement is genuine too, from a different section of the
same book. The search missed it because the OCR breaks "absolute" across a line.
A checker that reports fabrication when it has merely failed to find the passage
is dangerous, because what it licenses is the deletion of true material.

## Where the record stands

61 years, 2,014 dated events, 60 people who have been president. 73 leader
records, all with profiles. 443 executive officer records, 108 of them with a
profile. 827 pieces of legislation carrying 1,038 attributions, up from 918.
`build.py`, `check_data.py` and `check_contrib.py` all exit clean on main.
`check_duplicates.py` reports the same six pairs as the last pass; all six were
read again and all six are genuinely separate events.

## Left for the routines

The mirroring gap is now the binding constraint on this work, not the research.
1981-82 and 1982-83 could be checked because somebody once pulled their minutes
into `data/documents/`; 1980-81 and 1984-85 could not, because nobody did, and
the endpoint will no longer serve them. Any routine that succeeds in downloading
a minutes PDF should mirror it on the spot, whether or not the run needs it
twice. The archive can only be audited against the documents it holds.

---

# 19 August 2026, morning — editor pass

Three open pull requests. All three merged. Nothing was left standing that a
source would not carry, and for the first time on this project nothing had to be
cut for being wrong.

## What I reviewed

**#36, person profiles.** Two batches: the twelve 1980-85 cabinet officers an
earlier editor pass held open, and ten 2004-06 executive officers that landed
afterwards and nobody had looked at. I checked twenty-one claims, weighted toward
the newer batch.

**#39, the senate rolls.** Forty-seven Congress members and six officers for
1968-69 and 1983 to 1988. This one mirrors the minutes it works from, so I read
all eight scanned documents rather than sampling.

**#40, photographs.** Eight images from the Talisman, 1971 to 1987, and three
existing captions filled out.

## What held up

Everything, near enough. The March 2004 Herald election coverage is exact on all
of it: Todd 772 to Martin's 424, Petkova over Collins 692 to 481, Abby Lovan with
the most senate votes at 555, and every hometown, class year and platform in the
five senate-candidate write-ups. Petkova's quote about the administrators is
verbatim. The Pruitt gazebo account matches the article of 1 October 2002 line for
line. Copeland's 2004 letter prints him as a 2003 graduate from Bardstown, which
settles the hometown an earlier pass had doubted.

The senate rolls are the cleanest work reviewed on this project. Every roll call
matched: the two absences of 13 February 1969, the six of 30 August 1983, the four
of 4 October 1983, the eight of 4 September 1984, and so on through 1987. Two of
those documents have no text layer at all and had to be read as images; they
matched too. Mike Talbert, amended to a committee at the same August 1983 meeting,
is correctly not filed as a Congress member, and the three students who lost the
1986 Sergeant-at-Arms nomination are correctly absent.

Every photograph caption matches its Talisman volume word for word, and the three
crops that could plausibly have been the wrong photograph on a crowded page are
the right ones — checked against the page images, not the text.

## What I corrected

**The 2004-06 profiles cited none of the reporting they rest on.** Every fact
above came out of three Herald articles that appeared nowhere in the record. The
research was sound and the reading was accurate; it was simply unverifiable the
moment the run ended, and it cost an hour to reconstruct. All are now attached,
along with the two citations the earlier editor pass had asked for on Pruitt and
Copeland.

**Those citations would not have shown up even so.** Officer records could carry a
second source, and the last batch added several, but `render_office` and the
person-page rows printed only the first and `year_sources` counted only the first.
Every `src2` on an officer was dead data. They all print now. That is a change to
`build.py` rather than to `data/`, so it is flagged on the pull request for Sam to
reverse if he would rather it stayed as it was.

**One photograph was labelled the executive photograph and is not.** The 1987
Talisman prints two Associated Student Government groups on one page and names
both without giving anyone an office; four of that year's five executive officers
are in the group that was *not* so labelled. A reader following the caption would
have looked for Tim Todd in the wrong picture. Both years' captions now say which
group is which.

Two lines trimmed to what the source carries: Petkova's paragraph quoted the same
interview twice, and Martin's debate remarks said the programmes she would freeze
were unfunded where the Herald says unimplemented.

## The objection that held #36 open since yesterday

The earlier pass would not publish seven 1980-85 profiles resting on minutes
TopSCHOLAR would not serve. It still will not serve them — `viewcontent.cgi`
returned an empty 202 to me as well. But I diffed each of those profiles against
the note that was on main before the branch touched it, and the routine's answer
was right: they restate already-published content, and the one genuinely new claim
resting on an unread document had already been cut. The same is true of Amanda
Allen's website and iPod mailing list and Kara Ratliff's jump tables in the newer
batch. Discharged.

## Where the record stands

61 years, 2,014 dated events, 60 people who have been president. 73 leader records
and 73 portraits. 447 executive officer records, 138 of them with a profile, 616
senate officers and 379 rank-and-file members — the members up by 47 tonight from
a standing start of nothing before 1989. 47 primary documents on the site, eight
of them added tonight, and 34 photographs of years alongside the portraits. 827
legislation files carrying 1,038 attributions. `build.py`, `check_data.py` and
`check_contrib.py` all exit clean; `check_duplicates.py` reports the same six
pairs as yesterday, and all six remain genuinely separate events.

## Left for the routines

Yesterday's note said the mirroring gap was the binding constraint. #39 is the
answer to it and should be the template: it downloaded its minutes, put them in
`data/documents/`, and so could be audited in full instead of taken on trust. The
years that could not be checked yesterday are still the years nobody mirrored.

Three gaps found while reading, none of them defects. **Sean Peck** seconded the
motion to adjourn on 15 April 1986 and is not recorded, though Bob Conley's second
in 1969 is. The 13 February 1969 minutes read **John Cabelli** where this archive
has John Cobelli, a spelling to record rather than resolve. And the 1981 Talisman
prints **Jeffrey Morris** where the record has Jeff Morris, which wants an alias
entry rather than an implicit match.
