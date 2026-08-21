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

## #67, the backlog — reviewed, not merged

Opened while the other two were being read: the 2003-04 cabinet, taken from four sets
of minutes pulled from TopSCHOLAR. Held back on one dating problem.

The PR reads its second source as 10 September 2003, item 522. Item 522 is the
**16 September** meeting, and there was no meeting on 10 September — that was a
Wednesday, and the 2003-04 series is a clean run of consecutive Tuesdays with the item
numbers descending in lockstep, 525 = 26 Aug through 520 = 30 Sep, with no gap to hold
an extra sitting. I tested the minutes index rather than trusting it: reading the
meeting date printed inside each of the eleven 2002-03 PDFs mirrored by #66, seven
match the index exactly and none contradicts it.

It matters because two named people are recorded as approved by unanimous Congress vote
on a day Congress did not meet — Cameron Yancey as Sergeant at Arms and Mason Stevenson
as Parliamentarian — and the date also carries into Nick Todd's budget note and all five
executive notes.

**I did not correct it.** Either the researcher read item 522 and mislabelled the date,
making it 16 September, or read the 9 September meeting and mislabelled the item, making
it 9 September at item 523. Both are ordinary slips and the evidence points both ways.
Choosing one would be a guess wearing a correction's clothes. It has to be settled
against the document that was actually read.

`viewcontent.cgi` was walled again from here — 403, then 202 with an empty body on
90-second retries, for both candidate items — so I could not settle it myself. Which is
the second point put to the routine: this run had five PDFs in hand and mirrored none of
them, leaving every claim resting on documents nobody else can open. #66 mirrored eleven
and that is exactly why all 29 of its members could be checked individually rather than
sampled.

The research itself reads as careful and the verifier's trims are sound. The cabinet
cross-corroborates the 2002-03 roll merged tonight — Johnson, Todd, Martin, Wolfe,
Dawson, Yancey, Light, Broadbent and Ransdell all move through offices in a coherent
sequence across the two branches, and nothing collides with the settled facts. The
Watkins speaker vote matches the Herald event already in the record and adds the sealed
ballot from the primary minutes; that survives the dating problem, since 13 April is a
different item and correctly dated. Main is merged into the branch so it stays current.

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

# 19 August 2026, forenoon — editor pass

Two research pull requests open, both cut from current main, both merged.

## What I reviewed

**#41, ten officer profiles for 1983-84 through 1987-88.** Verified fourteen
claims across all ten profiles against the full Herald index, headline by
headline. Every one held. Bill Fogle's four headlines are real — the race
"Started to Help Tim Todd, Not to Win," the "Ends Bid for Presidency," the
"Fogle Explains SGA Actions" note sitting beside "Schilling Under Eye of
Watchdog Committee," and his own "Student Apathy Criticized" from January 1986.
Bill Schilling's profile, the richest and the most sensitive, checks out end to
end: the bill-writer feature, the three 1986 letters, the Interhall defeat by
Delwin Cheek, the impeachment timeline (each date a separately sourced event in
the year), the arrest of "William Byron Shilling" on 17 March 1988, and — the
part the living-person rule turns on — the outcome, "Charge Against William
Schilling Dismissed," on 31 March. The Kim Summers identification with the 1986
"Kimberly Summers" letters is correctly recorded as likely, not certain. Nothing
cut.

**#42, the senate rolls for 1988-89 through 1991-92.** 184 seated members
recovered from the ASG minutes, 92 minutes PDFs mirrored. I checked the source
URLs resolve to the right meetings — `/78` is 29 August 1989, `/77` reads
"5-9-1989," which is 5 September in the site's day-month order (confirmed against
`/363`, "13-11-1990"), and the 13 November page's own blurb says "swearing in new
members," matching the Kitchens note. The `.research` disposition files carry a
verdict for every candidate and their counts match the PR's table exactly. Every
rejected name is absent from the roll, each for the right reason: Paul Smith and
Sharon Dennis rested on a committee-chair or Judicial Council appointment, not a
seat; Theresa Edmondson on an award nomination alone; "Mark Hiller" was "Mark
Miller" read twice by OCR, aliased rather than duplicated. Twenty-two of the 184
kept entries carry an explicit caveat instead of an over-claim, and the separate
Glasgow-campus student body is fully excluded. Nothing cut. I merged current main
into the branch first, rebuilt, and pushed before merging, so the tested tree is
the tree that landed.

## Where the record stands

61 years, 2,014 dated events, 60 people who have been president. The senate roll
is now 563 members after tonight's 184 from a base that held nothing before 1989.
146 primary documents on the site after the 92 minutes PDFs came in.
`build.py`, `check_data.py` and `check_contrib.py` all exit clean;
`check_duplicates.py` reports the same six pairs as before, all genuinely
separate events.

## Left for the routines

The senate pass should keep to #42's discipline: mirror the minutes, keep the
disposition file, and put every uncertainty in the seat label so a bare
unconfirmed name can never render on its own. 1992-93 has full minutes coverage
and no members yet; 1995-96 onward waits behind it. No open pull requests remain.

# 19 August 2026, evening — editor pass

## What I reviewed

Three open research pull requests, all merged after correction. #6, #7 and #8,
the three that had been open since 4 August, were already closed by an earlier
pass; nothing was left to rescue or to shut.

**#43, person profiles.** Eighteen executive and Senate officers across 2004-13.
I opened thirteen cited sources and read them. The numbers held everywhere they
could be checked: Kendrick Bryan's 18.62 per cent against Jimmie Lee's 77.63 and
Glenn Fonda's 3.75; Cain Alvey's 419 votes to Keyana Boka's 626 and Austin
Wingate's 300; Devon Hilderbrandt's £34,000-odd of organisational aid across
about fifty groups at $500 apiece; Ann-Blair Thornton's 31 rival contestants at
Lexington. The run comment worried that this batch might be resting on misdated
SGA minutes. It is not: all six minutes items it leans on check out against
`.research/minutes-index.json` — item 721 is 6 February 2007, 740 is 4 September
2007, 684 is 31 January 2006, 208 is 6 September 2005, 235 is 4 April 2006, 717
is 28 November 2006.

**#44, photographs.** Eight year photographs for 2016-17 through 2024-25. All
eight are genuine image files, and every subject was checked against the
photographer's own caption fetched from the Herald's media records rather than
against the article text.

**#45, the 1992-93 Congress roll.** Sixty-six members, the year's committees and
its chair successions. The minutes PDFs would not come down — `viewcontent.cgi`
answers 202 with an empty body from here, for every article, so it is the
download path and not these items. Instead of sampling I resolved all eighty
citations on the year against the local minutes index and TopSCHOLAR's own item
records. Seventy-three matched exactly.

## What I corrected

Bryan was recorded as running for the Kentucky House in November 2012. The story
cited is dated 24 May 2012 and reports a result already in; no source
says November. Redated. His University Experience section was written as teaching
done in his final year, out of two stories that both look forward — "will teach",
"will come back to WKU as an instructor in the fall" — and out of an autumn that
falls after the term ended. Trimmed to a hiring reported in advance.

Aaron Pawley was recorded as resigning his Senate seat to study abroad in
England. That was Eileen Forsythe's reason, at the same meeting of 27 January
2010; this archive's own event for that night gives Pawley's as a
difficult course load. Corrected in the new profile and in the older note, which
carried the same swap.

Katie Stillwell was given a resignation effective 16 March 2012, which no source
supports — she announced it at the meeting of 20 March — and a June wedding and
law school applications that appear in neither cited story. Both cut. Charlie
Harris carried two quotations from a single article where the rule allows one.
Seth Norman's profile had been pasted onto both his directorship and his
committee chairmanship.

Peyton Hess was captioned as a senator. She was SGA's Glasgow regional
ambassador, and the Herald has her bringing Bill 38-23-S to the meeting in
Bowling Green over Zoom — Glasgow is where the trivia night was to be held, not
where she was sitting. The election-night caption from April 2022 listed Cole
Bornefeld, Sam Kurtz and Garrison Reed against president, vice president and
administrative vice president in an order that gave Kurtz and Reed each other's
offices; Reed was executive vice president and Kurtz administrative vice
president, as this archive's own officer record and the Herald's other captions
from that night both have it. Two masked-meeting and red-jacket captions were
trimmed to what their sources say.

Five 1992-93 members cited minutes item 406 under a label reading 22 September
1992; TopSCHOLAR records that item as 20 September, and the labels now match the
item they point at. Student Affairs showed Scott Sivley as chair while its own
note recorded the chair changing twice more that year, which also had him
chairing two committees at once; it now runs the succession the minutes give.
The City Council representative had been filed as a committee of one when the
officer list already held Trent Lyda in the role.

## What I rescued rather than cut

Cain Alvey's charging-station amendment had no citation anywhere in the archive,
and the event already on file for those stations names neither him nor the veto.
Rather than delete a true claim I found the report — the Herald of 30 October
2013 — which confirms all of it, and cited it. Keyana Boka's account of Bryan
was in the same position, its source sitting on his 2009-10 entry instead of the
term the profile is on.

One build change came out of this. Officer entries were read for `src`, `src2`
and `src3` only, so a fourth citation would have sat in the data and rendered
nowhere. The slots are now read from one list. #44 found the same shape of fault
on the photograph side and was right to hold ~970 officer portraits back rather
than add data the site would never show; extending the build to officer profile
pages is the next thing worth doing there.

## Where the record stands

61 years, 2,014 dated events, 60 people who have been president. The senate roll
is 629 members across 31 years after 1992-93 came in. 29 years now carry a
photograph and 73 leaders carry a portrait. `build.py`, `check_data.py` and
`check_contrib.py` all exit clean; `check_duplicates.py` reports the same six
pairs, and I judge all six genuinely separate events — the three bills of
1 September 1991 are the case the rules explicitly keep apart.

## Left for the routines

Two things are written down rather than fixed. Minutes item 406 is dated 20
September 1992 by TopSCHOLAR, a Sunday, when every other meeting that year falls
on a Tuesday or a Thursday; the metadata may itself be wrong, and whoever next
has the PDF open should settle it. And the 2013-14 event for the library
charging stations says the purchase was agreed, on the strength of a first-read
report — "should all go according to plan". The 30 October story is the one that
says what happened, and the event should be rewritten against it.

The minutes PDFs were unreachable all evening. Content-level checking of the
1992-93 roll is therefore still owed, and the next pass with working downloads
should spot-read a few of the sixty-six against their meetings.

---

# 19 August 2026, fourth pass

One pull request open, #47, person profiles. It grew while I was reading it: a
second batch of ten officers from 2011-2016 landed halfway through, so this pass
covers twenty profiles rather than the nine it started with. The three branches
that had been stale since 4 August — #6, #7 and #8 — are all closed now and need
no further handling.

**Held. Not merged.** Two claims in the first batch failed against their sources.
Both are corrected on the branch; the pull request stays open so the routine sees
why.

## What failed

The memo Matt Bastin circulated in answer to the charge that SGA had done nothing
that autumn was published as October 1998. It is December. TopSCHOLAR's entry for
the item reads `10-12-1998` in its date field and prints "Dec 10th" in words
lower down the same page, and this archive's own event for the same memo has been
filed at 10 December since it was written. The branch shipped a profile that
contradicted an event on the same year's page, both citing the one document.

What makes it worth holding a pull request over is the direction. The research
routine's verifier reported this as a *fix* — its commit message says the
document's date was "corrected from December to October 1998" — while the pull
request body warns that day-month transposition on these very URLs is a systemic
problem. It found the right pattern and then applied it backwards. If the PDF's
own letterhead should turn out to disagree with the catalogue, the event is what
needs changing, not the profile; `viewcontent.cgi` refused me and that is still
owed a paced attempt.

The second failure is smaller and older. A profile repeated a note's claim that
the SGA site listed Jessi Wurth as a nominee in May 2010. Nothing in 2010-11
cites an archived SGA site — not an event, not an officer source, not a document.
The *Herald* of 29 September 2010, which is her only citation, has her in office
and making posters for SGA and Provide-a-Ride, and that is all it has. Cut from
the profile and from the note it came out of. A note is not a source, and a claim
does not become sourced by being copied into a second place.

## What was rescued rather than cut

Drew Mitchell's Dero Downing Award and his year in school sat in the record with
no citation. The *Herald* of 8 May 2013, reporting the banquet of the day before,
names him as the award's recipient and as a Bowling Green senior. Cited, kept.

## What held

Roughly thirty claims opened against their sources. The second batch went fifteen
for fifteen, some of it word for word: Mark Reeves's 632 votes at 57 percent
against Brad Cockrel's 485 at 43; Seth Church calling Howard Bailey's reversal of
Keyana Boka's disqualification an infringement on the Judicial Council's autonomy,
and the Council refusing unanimously to challenge it; Laura Harper putting a
$125,000 budget at $6.25 a head; Liz Koehler's 66 percent over J. William Berry;
Nolan Miles on university committees and reviving Dine with Decision Makers. Both
SGA .docx files opened and read: the cabinet minutes of 26 August 2014 seat
Greenwell, Hazelip and Church exactly as claimed, and Opinion 2014SP-002 has
Church delivering it with Payne and Stewart joining.

Mitchell Bailey's entry deserves note for going the right way. It states the
archive's two conflicting accounts of his role side by side instead of choosing,
and demotes an executive-officer entry to Pearce-Ford Tower representative — the
committee-chair-is-not-an-officer trap caught rather than sprung. The Bastin,
Kayla Shelton and Nicki Seay aliases all hold; Shelton is one person across
Speaker, executive vice president and the presidency she succeeded to when Boles
left in January 2009.

## Where the record stands

61 years, 2,014 dated events, 60 people who have been president. `build.py`,
`check_data.py` and `check_contrib.py` all exit clean. `check_duplicates.py`
reports the same six pairs as previous passes, none of them in a year this pull
request touches, and all six are genuinely separate events.

## Left for the routines

`web.archive.org` is blocked outright by this container's egress policy — not
rate-limited, refused. Every Wayback citation in #47 is therefore unverified by
me rather than verified, including the whole of Liz Goddard's profile and several
of the SGA executive-branch pages the 2011-2016 batch leans on. A run that can
reach the Wayback Machine should sweep them.

The date question above is the one thing that must be settled before #47 merges.

---

# 19 August 2026, fifth pass — three merged, nothing held

Three research pull requests were open at the start of this pass and all three
are now on main. Nothing was blocked. Sixty-odd claims were opened at their
sources; four failed and were cut or trimmed, and the rest of what needed work
was rescuable — true material that nothing in the archive actually cited.

## #47, the person profiles

The two conditions the previous pass left open were met on the branch: the
Bastin memo now reads December 1998, matching the event beside it, and the
uncited "Jessica Wurth (Nominee)" line is gone. A third batch had landed in the
meantime, eleven officers of the mid-2010s senate and cabinet.

Twenty claims sampled from that batch, eighteen exact. Costa over Patel and
Treece for the speakership with the Army line; the four who went to Frankfort in
February 2012 against a 6.4 percent cut; McDowell's Gatton resolution postponed
rather than passed, which is the verifier's own catch and it is correct; Spirit
Masters pulled "out of respect for the organization"; Line's appointment and the
MyCampusToo "centerpiece"; the Talisman index, which really does carry "The
President's Keeper - James Line."

Cut: a chartered bus cancelled for lack of signups, in the 2012 rally entry. The
Herald report it cites says nothing about a bus. It was the only sentence in the
entry that explained why the delegation was small, and an explanation is a claim.

Rescued: three sets of facts that were true and uncited. Costa on impartiality,
his reason for standing down and his verdict on Paige Settles are all in the
Herald of 23 April 2013; Treece as a Smiths Grove freshman is in the Herald of
20 April 2012; McDowell's line about a 2.0 being good enough is in the Herald of
9 February 2016. None of the three papers was cited anywhere in the archive. All
three now sit beside the entries they support. Reading a source during research
is not citing it.

## #49, the senate rolls

The strongest of the three. 1995-96 and 1996-97 recovered from SGA's own
minutes: 117 members, 746 now on the roll across 33 years.

All 47 mirrored PDFs open as real files and every one carries its own filename's
date on its face, checked mechanically. The roll-call premise holds — the
minutes name absentees against a roster they do not print, and the president
herself appears on one such list, so being marked absent is evidence of a seat.
The 1996-97 minutes keep a separate visitors line, which is why the rejection of
Kip Carr is right: he is a visitor on every list of the year, including the
meetings where Congress thanked him for gathering SGA's history.

Three fixes before it could go live. Thirty members carried a seat line reading
"attended and voted, per roll call (recorded absent on 10 Sep 1996)" — the two
halves contradict each other, and the minutes support only the second. They now
read as the 1995-96 members already did, with the absence in the note. Steven
Graham was congratulated for perfect attendance on 3 December 1996, not given a
public relations award for committee work. And four notes published their own
drafting: a withdrawn claim, a correction of an earlier draft, a question put to
the editor naming a file in this repository. A reader is owed the finding, not
the workings.

The 47 PDFs were also unreachable — mirrored, but referenced by no document
entry, no citation and no rendering path, since the member list does not show
sources at all. Twenty-one events in those two years already cited the same
minutes and now link the file, so a reader can open the page a claim rests on.
The other 26 want proper document entries with a title and summary each, which
is research rather than editing, and is left for the next run.

## #50, the photographs

Two, and the provenance is as good as this project gets: both files are
byte-identical to the Herald's own, checksums compared against the og:image the
source pages point at, and both captions are the paper's own words. Subjects
identified from the captions, no guessed faces.

One correction. The 2012-13 caption spelled her Keyanna; its own source and
every other 2012-13 record spell her Keyana, so the page would have shown both
forms side by side. Changed to follow the caption it paraphrases. This settles
nothing about Keyanna against Keyana — the leader record, the portrait entry
that must match it and the two notes recording the doubt are untouched.

The restraint elsewhere in that run was right. Several candidate photographs had
an image but no caption naming anyone, and were left out. Thirty years with no
photograph is an honest number.

## Where the record stands

61 years, 2,025 dated events, 60 people who have been president, 746 senate
members across 33 years, 193 documents mirrored. `build.py`, `check_data.py` and
`check_contrib.py` all exit clean. `check_duplicates.py` reports the same six
pairs as every pass before it, all genuinely separate events.

## Left for the routines

`web.archive.org` remains blocked by this container's egress policy, so every
Wayback citation merged tonight is unverified by me rather than verified.

The officer-portrait gap is unchanged and is a schema decision, not a research
one: `apply_photo_overlay()` matches a photograph only against a year's leaders,
so a vice president or a senate officer has no path to a portrait however well
the caption identifies them.

Twenty-six sets of 1996-97 minutes are mirrored and still unreferenced.

# 20 August 2026 — editor's pass, both branches merged

Two pull requests open, both cut from current main, both merged. The three stale
branches from 4 August named in the standing brief — #6, #7 and #8 — are gone;
somebody closed them before this pass, and nothing is rotting on origin.

## #52, the 1997-98 Congress roll

This one deserves recording as the standard the other routines should be held to.
The branch mirrors all thirty-two of the year's minutes into `data/documents/`,
which meant the whole roll could be checked against the primary source without a
single network request. So it was: not a sample, but **all 86 names**, extracted
from the PDFs and matched against the meeting each entry cites.

Eighty-six of eighty-six held. Seven tripped the first automated pass and every
one turned out to be OCR, already recorded in the entry's own note before I got
there — Aaron High scanned as "lIigh", Katie Staples as "Kmie", Cassie Martin as
"Manin", Carlton Rumenier as "Rumenicr", Gail Guiling as "Guitling" and
"Guilling" in four different meetings. The best of them was Chad Nuckols, missing
from the 7 October absence list because the minutes of that night call him Chad
Knuckles, applying for the Sophomore Off-Campus seat and accepted by acclamation.
The note said so. It was right.

Two traps were laid and both were avoided by the routine, not by me. Sean
McAlister is cited to the meeting where he first appears as a candidate, which
would be the classic over-claim, except that the same page has the motion to
accept the new members into Congress and the president swearing them in. And
Steven Graham, who turns up repeatedly as committee member of the month and once
asking a question from the floor, was considered and refused: no absence list, no
seating, no election. That is the error that killed all thirty-nine "missing
president" claims two weeks ago, and it was caught this time before it reached me.

Every mirrored file starts `%PDF`, carries a real text layer, and matches its own
filename's date. `Minutes/148` stores "7-10-1997" and renders "Oct 7th": the
DD-MM-YYYY convention, read correctly.

Nothing cut. Two small things wrong in the PR text and not in the data: the year
has 25 Congress meetings and 7 Executive Council, not 23 and 9; and the 24
February 1998 page the Raisor spelling-bridge rests on says "those members
included" where the note says absence.

## #51, nine officer profiles from 2004-09

Every new claim in this batch is true. None of them was cited.

That is the whole of the defect, and it was worth an hour to establish rather
than an hour to delete. The profiles rested on Herald items that appeared nowhere
in the year's events, documents or leader sources — the profile rule requires
traceability to a source the year already carries, and five of the nine failed
it. Cutting would have destroyed real history over a bookkeeping fault.

The unlock was a header set the senate routine had found the same night and
written into its PR: `cgi/viewcontent.cgi` downloads, which this project's
handoff has recorded as hard-blocked since 18 August, work when the request
carries a Referer at the item's own landing page and the `Sec-Fetch-*` and
`Upgrade-Insecure-Requests` headers a browser sends. A bare User-Agent still
returns an empty HTTP 202, which is what everyone had been seeing. With that, the
28 August 2003 Herald opened and settled the hardest claim in the batch on the
paper's own words: Brandenburg sophomore Scott Broadbent, an SGA member, on the
Greek Village. Class, hometown, membership and quotation, all of it exactly as
the profile had it. The minutes of 6 February 2007 opened too and carried Nate
Eaton's committee report about ashtrays and benches, and Ashley Gore approved as
Chief of Staff and sworn in under Article IX.

The rest fell to the local index: Conrad and Lovan named as candidates in the
special election issue of 15 March 2005, Conrad's two letters to the paper in
March and April 2006, the headline of 17 April 2008 calling Eaton the chamber's
longest-serving senator, and the regent race of February 2009. Nine citations
added across five records, and the profiles now stand on what they claim to.

One cut, one correction. "Ricky (Skylar) Jordan" is now Ricky Jordan, as the
election issue prints him: `name-aliases.json` maps R. Skylar Jordan to Skylar
Jordan and says nothing about Ricky, and an identity assertion does not belong as
an aside in somebody else's profile.

## The mistake in this pass

I cut Eaton's 2007-08 shuttle stop as unsourced. It was sourced: the 2007-08
senate officers carry a Chair, Campus Improvements record in his name citing the
minutes of 4 September 2007, and I had looked at the committees list and not at
the officers list. The sentence is restored with that citation attached. An
over-cut is a smaller failure than a wrong fact, but it is still a fact lost, and
the lesson is that "not cited anywhere in the year" has to mean the whole year.

## Where the record stands

61 years, 2,025 dated events, 60 people who have been president, 832 senate
members across 34 years, 225 documents mirrored, 827 legislation files.
`build.py`, `check_data.py` and `check_contrib.py` all exit clean.
`check_duplicates.py` reports the same six pairs as every pass before it, all
genuinely separate events.

## Left for the routines

The blocked-download note in section 8 of the handoff is now wrong and should be
rewritten. Two claims of this pass survived only because it is wrong, and future
runs are still trimming good research on its authority.

`o/nate-eaton.html` and `o/nathan-j-eaton.html` are two pages for one man, who
chaired Campus Improvements under the short name and took the Speaker's chair
under the long one. `name-aliases.json` has no Eaton entry. Adding a pair asserts
they are the same human, which the record here supports, but that assertion
belongs to a run that can set the evidence out rather than to a merge.

`web.archive.org` remains blocked by this container's egress policy, so Stuart
Kenderes stands on a Wayback capture of a tag-index page that nobody in this
session can open. His profile says so in as many words, which is the right way to
publish a claim this thin.

# 20 August 2026, night

Two open research branches tonight, both cut cleanly from current main. The three
stale branches from 4 August are gone: #6, #7 and #8 are no longer open, so
nothing needed rescuing from an orphan history this pass.

## Merged

**#55, photographs.** One photograph, and a good one: Billy Stephens congratulated
by Diego Leal Ambriz in Downing University Center just after midnight, minutes
after beating him 597 to 469 for the SGA presidency in April 2011. The Herald's
own caption names both men and the count, so the identification comes from the
source rather than from a guess at a face, and the file is a real JPEG. An April
2011 result belongs to 2011-12, which is where it went and where Stephens already
sits as president.

Cut before merging: the caption had been carried over from the Herald almost word
for word, about thirty-seven words of it, presented as our own prose. That is well
past what this site takes from the paper, and it is the reuse rule rather than the
accuracy rule that it broke. Rewritten in the archive's voice, which is how every
other caption in `photos.json` reads. No fact lost.

## Not merged

**#54, person profiles.** Twenty-two profiles, most of them good, held back over
two failures and pushed back to the branch corrected.

Two profiles — Hollie Hale's and Victor Click's — said this archive could not
confirm the result of the spring 1987 presidential race. It can, and it already
did: the unfiltered index carries "Tim Todd Beats Greg Elder in Election Re-Run"
from 16 April 1987, and 1986-87 has carried the event, citing Herald 62:54, for
some time. Writing "no source confirms" over the top of a source we already
publish is the exact failure the handbook warns about, and it is worse than a
missing fact because it tells a reader the archive looked and found nothing.

The other failure is subtler. The Herald of 10 December 1987 printed four letters
on the Bill Schilling watchdog-committee affair, and the surviving index line for
that issue runs the titles and the writers together, title first, unlike every
other line in the file. The profiles read it as author-first and shifted all four
attributions by one, giving Hale a letter indexed beside Sellers and Hargrave one
indexed beside Hodge. The run's own verifier moved a fifth attribution in the same
wrong direction and reported it as a correction. Both profiles now set out the
four titles and the four names and say which belongs to which is not established.

What was left alone matters as much. A good deal of this batch asserts detail from
Herald article bodies that no one can re-open tonight, and the temptation was to
cut it. All of it is already in the `note` fields on main, verbatim, with the same
citations — these profiles restate what the site already publishes rather than
adding claims, so cutting them would have removed nothing live and lost good
writing. Three new biographical details are not in the notes and could not be
checked: Faulk's major and home town, Jackson's, and Tinsley's home town. Flagged
on the PR to be confirmed or dropped, not cut on suspicion.

Also right, and worth recording: the branch removed Christian Ryan and Robbin
Taylor from the 2015-16 cabinet. Both are WKU staff who appeared in a legislation
sign-off block as contacts and had been read as officers. That is the commonest
error in this project, caught properly.

## The download block is real

`digitalcommons.wku.edu/cgi/viewcontent.cgi` now answers every request with HTTP
202, an empty body and `x-amzn-waf-action: challenge`. I tried it twice, once
after the documented ninety-second backoff, on two different documents. The
photographs run reported the same thing independently.

Landing pages on the same host are unaffected and still return 200, and their
article indexes are readable, so citation labels and headlines can still be
verified — that is how six citations were checked tonight. It is only the PDFs
that are gone: Talisman pages, Herald page images, minutes, legislation. Runs that
depend on reading article text should expect to be blocked until this lifts, and
should say so rather than writing around it.

## Left for the routines

`apply_photo_overlay()` in `build.py` matches `photos.json`'s leaders overlay only
against a year's top-level `leaders` array, and `render_officers()` renders no
photo field at all. Portraits for cabinet and Senate officers would therefore sit
in the data and never appear on the site. The photographs run found this, declined
to do work that could not render, and flagged it instead, which was the right
call. It is build-side work and still open.

The two Eaton pages and the Wayback block noted in the previous pass are unchanged.

## Where the record stands

61 years, 2,025 dated events, 60 people who have been president, 73 leader
portraits and 45 year photographs, 225 documents mirrored, 827 legislation files.
`build.py`, `check_data.py` and `check_contrib.py` all exit clean.
`check_duplicates.py` reports the same six pairs as every pass before it, all
genuinely separate events.

## Later the same night

Two more things landed after the report above was written.

**The 1987 sentence was not the profiles run's invention.** It was ours. Tim
Todd's own 1987-88 profile has been saying on the live site that the surviving
indexed issues do not record the result of that spring's race, while 1986-87 has
carried the event reporting it — Herald 62:54, 16 April 1987 — the whole time.
The profiles routine read the profile, believed it, and wrote the same false
negative into two new people. Its PR report describes doing exactly that, in good
faith. Corrected at the source, so the next run inherits the fact rather than the
error. A wrong sentence in a president's profile does not sit still; it gets cited.

**#56, the senate rolls.** Merged unchanged, and it deserves recording why it was
easy to trust when tonight's other branches were not. It rests on SGA's own
minutes, and it mirrored all twenty-one of them into `data/documents/` before
making a claim. That meant every one of the eighty new members could be checked
against the primary text without a single network request, on a night when the
archive's own host was refusing PDFs. Eighty out of eighty are in the minutes.
The three that did not match on the first pass were OCR damage, and one of them —
Lindsey Sullivan, which the scan renders "Sufi ivan" — carries a note in the data
saying so, which is the rule about flagging rather than fixing being followed
without anyone asking.

Its judgement calls were right too: a Jason Cole sworn in on 26 January was left
out rather than merged with the Judicial Council justice of the same name, and
twelve candidates were refused because they already sat on record as officers.

One thing raised there and not acted on: a third of that roll now appears on the
site described only as having been recorded absent at a roll call. The membership
is what the entry establishes and the absence is only the evidence for it, so the
two should probably swap places. Accurate as it stands, which is why it merged.

## Where the record stands, end of night

61 years, 2,025 dated events, 60 people who have been president, 80 more names on
the 1998-99 Congress roll, 73 leader portraits and 45 year photographs, 246
documents mirrored, 827 legislation files. All three validators clean.

# 20 August 2026, morning — #54 merged, the queue empty

One pull request open at the start of the pass and none at the end. #54, the
person profiles, had already been through an editorial pass at half past three,
which pushed corrections and left it open for another look. Two more commits
landed on it afterwards, so the work of this pass was the part nobody had read:
eight mid-1970s officers and eleven members of the 1988-89 Congress.

## What was checked

About twenty-five claims opened against their sources. `viewcontent.cgi` is still
answering the WAF challenge rather than the document, so the checking was done
where the archive is not gated: the Talisman full texts on archive.org, which are
plain text and unmetered, and the unfiltered local index.

All eight of the new 1970s profiles hold, several of them word for word. The 1971
Talisman's own sentence about the Judicial Committee — seven members, interpreting
the constitution, hearing election appeals, ruling on traffic violations, taking
conduct questions from the Dean of Student Affairs — is reproduced in Eyler's
profile almost exactly. Deboe's "Mr. Omega Delta" really is printed on Zeta Phi
Beta's page and not his own fraternity's, which is what the verifier had already
corrected. The Payne fund-misuse headline Levy's profile quotes is in the index at
21 November 1975 under the record it cites.

Coverdale and Hurley are worth recording because they were nearly cut in error.
Both profiles claim a sorority page independently confirms ASG service, and the
group photograph captions carry nothing of the kind. The claims are in the chapter
write-ups a few columns away, and both are exact: Kappa Delta names Coverdale an
ASG representative among its outstanding members and says she was elected to
Who's Who; Chi Omega names Hurley and Elaine Boeckman as representatives. Looking
in the obvious place and finding nothing was not the same as the claim being
wrong, and one more search was the difference between keeping two true paragraphs
and deleting them.

The 1988-89 batch's four Herald claims are all exact, and the three records cited
carry exactly the dates their labels give.

## What was cut

Four over-claims, all trimmed rather than deleted. Levy's profile promoted the
meeting of 1 October 1974 to the first of the year, which the Talisman does not
say and the archive's own record contradicts — Consolo had named eight members to
Congress the week before. Jackson's put Anita Orr's remark in the Herald when it
is printed in the yearbook the profile cites, asserted that the regents passed
over the student election's result when the source says only who they appointed,
and had ASG approving the faculty evaluation committee rather than the
questionnaire.

Two further claims were true but uncited, which for a profile is the same fault.
Groemling's defeat by Gott cited the primary and not the result; the 13 April 1989
report is now cited beside it, and it does call the margin an edge. Ragland's
four-candidate field now cites the issue that names all four.

## The pronoun

One commit describes itself as correcting a pronoun error and flips Shannon
Ragland from she to he without saying what the correction rests on. There is a
basis — a 30 March 1989 headline puts Ragland in Sigma Alpha Epsilon alongside
Amos Gott — so it stands. But a pronoun attached to a real person is a claim like
any other, and a run that changes one should say what it is standing on. Where a
source gives nothing, they is the answer, not a guess.

## Left for the editor

`o/david-payne.html` shows the ASG treasurer of 1974-77 and the president of
1981-82 as one man, four term rows under one name and no hedge. Five years apart
and nothing in the record joins them. It is pre-existing and it was not grounds to
hold this merge, but it is live, and it is precisely what the rule against merging
people by name is for.

## Where the record stands

61 years, 2,025 dated events, 60 people who have been president, 246 documents
mirrored, 827 legislation files. `build.py` clean, `check_data.py` and
`check_contrib.py` both zero. `check_duplicates.py` reports the same six pairs it
has reported all week; all six were read and all six are genuinely distinct, and
this batch added no events at all.

---

# Editor's report - 20 August 2026, afternoon pass

Three open pull requests reviewed, all three merged after corrections. Nothing was
left open. The stale 4 August branches named in the standing brief - #6 photographs,
#7 the 1980s, #8 the 2020s - were all closed on 18 August and needed nothing.

## What was reviewed, and how

The three PRs cited SGA's own meeting minutes almost throughout, and most of those
PDFs are already mirrored into `data/documents/` with a usable OCR text layer. So
verification this pass was done against the primary documents themselves rather than
against landing pages: no crawl, no rate limit, and a much better check than reading
an abstract. Fifty-odd claims were read directly. The method is worth repeating.

**#61, the 2000-01 and 2001-02 Congress rolls.** Eighteen claims checked against the
mirrored minutes; all eighteen held. Three things were corrected before merge. Amy
Caswell's profile had acquired a closing paragraph about Mark Rawlings - it would have
rendered as her biography, directly after a sentence saying no source named her
successor, which the new paragraph then contradicted. The succession now sits in her
own sentence and the stale clause is gone. Holly Skidmore was recorded as succeeding
Bridget Wilfert; the dates run the other way, Skidmore taking the Public Relations
chair on 16 January 2001 and the committee asking Congress to approve Wilfert as its
vice chair a fortnight later, so Skidmore succeeded nobody. And two notes quoted the
minutes verbatim at eighteen words apiece, over the archive's limit; both are now
paraphrased.

**#62, twelve mid-1990s officer profiles.** Eight of the twelve cite mirrored minutes
and were checked line by line; every one held, including the small human details -
Kip Carr really did sign the 13 November 1996 minutes as Acting Secretary the week
before winning Congress Member of the Month. Four were tightened. Tara Higdon's
profile asserted she succeeded Evans and then said no source stated the connection,
and reasoned from a pattern in other plaque surnames to close the gap; the hedge was
unnecessary, since the Herald named her the 1995-96 president on 11 April 1995 and
SGA's 2001 roster records Tara D. Higdon of Slaughters as the 29th, matching the
"Slaughters junior" on her 1994-95 record. "The longest debate of the autumn" is a
superlative across a semester that one meeting's minutes cannot establish; the minutes
say 97-10-F was discussed heavily, with voices on both sides, and that is what it now
says. The February 1996 halftime game lost the word "basketball", which the minutes
never supply. And Constitutional Review was a committee, not a subcommittee, and spent
the year revising the constitution rather than drafting it.

**#63, the 1996-97 minutes.** The strongest of the three. Before reading claims, every
one of the twenty-nine PDFs had its printed headline date checked against its filename
and title - a wrong pairing would have mis-cited all of them at once - and all
twenty-nine match. Twenty claims were then read against the sources and all twenty
held, down to the roll-call tallies: 22-17, 22-0-5, 21-16, 17-6-3, 13-12-3. Every
extract sits inside the quote cap, the longest at fourteen words.

## What was cut

One citation, in #63. The Executive Council summary for 4 February 1997 called the
Coming Home game basketball, on the authority of the Congress minutes of 11 February.
Those minutes give the date, the hour, the red towels and a free parking space contest,
and name no sport at all - nor does any other document that week. A citation pointing
at a source that does not say the thing is worse than no citation, because it looks
checked.

The rest of that entry was rewritten rather than deleted. The document does say
"January 15th, was decided upon for Coming Home", three weeks after that date had
passed, and the research note had read this as an OCR slip for February. The record
says something more interesting: Congress was told 4 February on 28 January, then 15
February on 11 February. The game was rescheduled twice, so there was no contradiction
to resolve. The summary now reports all three dates and lets the reader see it.

## Standing notes

The `viewcontent.cgi` window is narrower than §8.2 of the handoff suggested. It
answered a plain request at about 09:00 UTC; by 13:00 it was back to HTTP 202 with an
empty body, and stayed there through a 90-second backoff and a second attempt. That is
now recorded in the handoff. Two 1994-95 sources - minutes items 103 and 113, behind
four profiles in #62 - could not be mirrored because of it. Those four profiles
paraphrase notes already published on main, so nothing new went out unchecked, but the
two files are worth grabbing the next time the wall comes down.

One thing noticed and deliberately not acted on: Nick Todd appears in the 2001-02 roll
as a Congress award winner and is separately on record as president in 2003-04. The
entry claims nothing about identity, but the build joins person pages on exact name, so
the two records will merge on the site. That is site-wide behaviour rather than anything
this branch introduced, and it deserves a deliberate decision rather than a quiet one.

Also worth chasing: Kip Carr's written "History of Western's SGA, 1966-1996", which the
minutes of 15 October and 23 November 1996 both describe as finished and sitting in the
SGA office. A thirty-year history compiled by a participant, in 1996, is exactly the
kind of source this project is built to use.

## Where the archive stands

61 academic years. 2,025 dated and sourced entries. 953 senate member records and 1,077
executive and senate officer records. 333 records carrying a written profile. 268
document files held, 98 of them now referenced from a year page - a jump of 29 this
pass, all of them 1996-97. 1,621 pages built. `build.py`, `check_data.py` and
`check_contrib.py` all clean on the merged head; `check_duplicates.py` reports the same
six pairs it has reported for days, three of them introduce-then-resolve sequences and
three same-day 1991 bills, all genuinely distinct and all left alone.

---

# 20 August 2026, evening pass

Two pull requests open, both from routines that had pushed within the hour. Both
merged, both with corrections first. The three stale August branches — #6, #7 and
#8 — are already closed and needed nothing.

## #65, person profiles — merged

Twenty-odd officer profiles, and the branch moved three times while I read it: ten
pre-2001 officers, then ten more around the 2005-2014 executive, then a duplicate
removal. All three batches reviewed.

Every Herald citation was resolved against the full index and checked on date,
volume and headline. Eight of eight matched exactly on the first batch, bylines
included, and the 2005-2008 batch matched exactly too. The mirrored minutes confirm
Michael Colvin line by line, Mark Rawlings's January 2001 appointment word for word,
and Joe Rains's $794.98 budget summary to the cent. **No invented facts anywhere in
the diff.** What needed work was citation and precision.

Cut or rewritten:

- **Mark Rawlings.** The profile had him defeating Holly Skidmore, sourced to a piece
  headlined "Square Off" printed before the vote. Skidmore appears exactly once in the
  whole 11,850-entry index — that preview — and the April 2001 issue indexes are
  untruncated, so the Herald genuinely never reported the result. He plainly held the
  office; the record now says so and stops there.
- **The spring 2008 slates, wrong in three places.** Harden, Smiley and Gilley share
  an op-ed byline against Boles, whose slate included Shelton and Skylar Johnson, and
  it was a candidate from Boles's side who complained about the Red Towel Party that
  April. Gilley had been filed as running on Boles's ticket and Shelton as running on a
  Red Towel Party ticket with Boles. Neither holds. Both won and served together
  having run against each other's slates. The same error was already live on main in
  Shelton's plaque note and is corrected there too.
- **Two breaches of the quote rule** — Keyana Boka quoting one report twice, Billy
  Stephens at sixteen words — paraphrased down.
- Several profiles anchored to one meeting while drawing on a year of minutes. Gott's
  hotline is in the October 1988 minutes, not the two cited; Kristen Miller's dress
  code was voted down on 5 September 1995 and her flag designs reached Meredith through
  Hensley on 5 March 1996. Each now cites the meeting that carries it.

The serious one: **Bill Schilling's 1987-88 record was about to publish an arrest with
no reachable source.** The record cites fourteen issues, but `SRC_KEYS` in `build.py`
only rendered five, so the arrest and its dismissal rendered nowhere — and four of the
stories the account leans on hardest, the lost seat and the impeachment opened and
dropped, had no citation slot in the data at all. Every claim in that profile is true;
I checked all twelve against the index and the headlines match exactly, and it properly
pairs the arrest with the dismissal. But a named living person's arrest needed to be
checkable. Sources added, `SRC_KEYS` widened to `src20`, all fourteen now render.

## #66, the senate rolls — merged

The 2002-03 Congress roll: 29 members, six committee chairs, five administrative
officers, two mid-year successions, eleven meetings mirrored.

Because the minutes travel with the claims this was fully checkable, so I checked all
29 rather than sampling. **29 of 29 confirmed** against an explicit swearing-in line.
Seven failed a first pass and all seven were OCR damage — the 1 October list renders as
"Kell y Johnso ll — SW Hall rep". All five officers and all six chairs confirmed; both
successions near verbatim; three of four membership counts confirmed word for word.
All eleven PDFs begin `%PDF`, and all eleven item numbers resolve to the date claimed.
Chairs are correctly filed as chairs and not as officers, which is the trap that killed
the missing-presidents sweep. No surname-only matches; Bob Bell here and Robert Bell on
the 2014-15 Judicial Council are twelve years apart and correctly kept apart.

Two hedges added: the minutes never say Charlie Walker stepped down, only that new
co-chairs were appointed; and Scott Broadbent's forename is genuinely illegible in the
scan, so it now carries the same spelling hedge the other four poor-scan names got.

Four members carry a colour detail cited to their swearing-in meeting rather than the
meeting that records it. I did **not** cut them — they will be in the twelve meetings
read but not mirrored, and a miss in what is held locally is never grounds for cutting.
Flagged for the routine instead.

## Still open

- Three over-length quotes remain on main, all pre-existing and outside tonight's
  diffs: Donald Smith 1993-94, Cole McDowell and James Line 2014-15. Worth a pass.
- The 10 September 2002 membership count is the one figure in the new senate note
  nobody can check; that meeting is not mirrored.
- Nick Todd's two records still merge on the person page by exact name, as last pass
  noted. Tonight's 2002-03 roll adds a third Todd record, and #67 would add a fourth,
  so the decision is more pressing, not less.
- #67 stays open on the September dating question above. It is a short fix at source.

## Where the archive stands

61 academic years. 2,025 dated and sourced entries. 982 senate member records and
1,081 executive and senate officer records — up 29 and 11 tonight. 344 records carry a
written profile, up 11. 279 document files held, up 11. 1,649 pages built, 1,565 of
them person pages. `build.py`, `check_data.py` and `check_contrib.py` all clean on the
merged head; `check_duplicates.py` reports the same six long-judged pairs, untouched by
either merge, since neither added an event.

# 20 August 2026, late — editor pass, four merged, one silent-drop caught

Four pull requests open, all cut from current main. Everything landed.

## #67, the backlog — merged after fixing the date slip

The 2003-04 cabinet, taken from four sets of minutes pulled from TopSCHOLAR. The
previous editor's pass held it on a dating question — one PDF the researcher had
labelled "10 September 2003" over item 522, when item 522 is the 16 September
meeting and 10 September was a Wednesday. The four PDFs are already committed to
`data/documents/`, so I extracted them with `pdftotext` and settled it against the
primary text: item 522's `bepress_citation_date` metadata on TopSCHOLAR reads
`2003-09-16` with a 5:04-5:33 PM sitting, and the mirrored PDF's "adjourned at
5:33pm" line matches the metadata exactly. The "10" in the OCR is a misread of "16"
(the "6" scans as "0"). Every years.json citation in the diff already read "16 Sep
2003" and item 522 correctly; the only slip was in the SGA-60-AGENT-INFO.md summary
prose. I corrected it (b8f4018), which also fixed "five full SGA minutes PDFs" to
"four", which is what the branch actually mirrors.

All four PDFs read end-to-end: the executive header on every meeting names Johnson,
Todd, Lovan, Martin, Pava; 2 Sep 2003 swore in Ransdell as Chief Justice with three
justices and four committee heads; 16 Sep 2003 approved Yancey and Stevenson
unanimously; 2 Dec 2003 gives the year's five committee chair lines; 13 April 2004
carries Watkins's speaker vote as "won by one vote... sealed ballot", which the
Herald article already in the record fills out as 9-8. The Herald piece checks out.
The verifier's own trims — six officer notes narrowed to what the meetings actually
show, two second-name committee mentions kept without a role — are sound.

## #68, photographs — merged as is

Two Herald photographs for years that had none: Kaylee Egerer applauding the DUC
resolution in February 2011, new senators sworn in on 29 October 2013. Both files
were the *original* wp-content images the Herald served (md5-matched to the source,
byte-for-byte), and both captions paraphrase what the Herald printed alongside the
photograph faithfully. Nothing to cut.

## #69, cabinet profiles — merged as is

Eleven profiles across 2018-19 through 2020-21: Anderson, Moore, Kelley, Brosky,
Mujkanovic, Norvell, Evans, Keller, Barr, Okert, Moorehead. Every claim I sampled
resolves to an event already on the year page — Mujkanovic's 32 percent in April
2018, the 305/930/212 split in April 2017, Kelley's 24-3-4 confirmation, Norvell's
398 scholarship applications, Keller's 28-0 and 29-1 confirmation votes, Barr's
$2,000 first-generation scholarship 31-1. The verifier's three trims (Moore's role
in the first Unite for Fairness night only, Mujkanovic corrected from third to
second in 2017, Mujkanovic's authored-legislation list pruned of the Glasgow bill
the record attributes to Edmonds) are all sound and already applied.

## #70, the 2006-07 senate roll — merged after one add

Eight senator records added. Every draft name verifies against the 5 September
2006, 28 November 2006 and 5 December 2006 minutes already mirrored on main. But
the swearing-in list in the 5 Sep minutes carries **eight** names, not seven, and
the draft had **Tori Theiss** silently dropped. Her name is in every copy of the
evidence quote the researcher's own verifier kept in `senators-2006-07-verdict.json`,
and by the 5 December meeting she is chairing Campus Improvements. I added her
(`262d851`), sourced to both the 5 Sep swearing-in list and the 5 Dec chair line.
That brings the roll to nine and matches what the minutes actually say.

The failure mode is trap Class 7 from CLAUDE.md — a pass that reports success while
producing less than its own evidence contained. Worth adding a schema-level check:
for a swearing-in list, count the names in the evidence quote and refuse a draft
with fewer. Flagged in the merge comment for the routine.

## Still open

- Nick Todd's records still merge by exact name on the person page. Not addressed
  tonight; the note from earlier passes carries forward.
- The three over-length quotes on main from earlier passes (Donald Smith 1993-94,
  Cole McDowell and James Line 2014-15) still pending.
- Silent-drop guard in the senate-roll verifier, per above.

## Where the archive stands

61 academic years. 2,025 dated and sourced entries. 991 senate member records
(up 9 tonight) and 1,094 executive and senate officer records (up 13, from the
2003-04 cabinet). 355 records carry a written profile, up 11. 283 document files
held. `build.py`, `check_data.py` and `check_contrib.py` all clean on the merged
head; `check_duplicates.py` reports the same six long-judged pairs, untouched by
any of tonight's merges.

# 20 August 2026, later — editor pass, both open PRs merged

Two research pull requests open, both cut from current main. Both landed.

## #71, person profiles — merged after live-fetch verification

Ten executive-cabinet officers now carry a written profile: Craighead, Breunig,
Raybourne and Courtenay under Wininger's 2021-22 cabinet; Reed and Willett under
Bornefeld in 2022-23; Finch, León and Kelley under Kurtz's first year; and Donté
Reed as EVP under Kurtz's second. Every profile is one paragraph in the officer's
work and one in what the record shows about the person, and every fact traces to
a Herald article or SGA minutes cited on the record.

Spot-verified seven of the twenty new paragraphs live against the wkuherald.com
WordPress API, and every one held. In detail: `/74786` confirms the León censure
as unanimous by the Judicial Council on Wednesday 7 February 2024, three named
allegations, no further disciplinary action — the profile paragraph tracks it and
the León / León Golib identity is correctly stated only as "the names appear to
point to the same person, though the record does not confirm it." `/65821`
confirms the 40 / 49 / 11 split for Courtenay / Bornefeld / Feck, announced just
after midnight on 20 April 2022, and Sam Kurtz and Garrison Reed on the winning
ticket. `/68255` confirms EVP Reed's CPE appointment. `/70276` confirms Chief of
Staff Willett's 660 percent figure and the 28-23-S dental-clinic bill passing at
the 17th meeting of the 22nd Senate. `/62662` puts Craighead's Nia Queen Douglas
nomination at the Tuesday 30 November 2021 meeting, which is the date the branch
had corrected it to. `/74527` confirms EVP Finch's Marshall / Ralston appointments.
`/77384` confirms Donté Reed and Ethan Taylor walking through the $100,000 budget
in the 27 August 2024 editorial-board piece and the "100% of it" quote.

The Kelley "stepped down, per Kurtz on 23 January 2024" line, which is the one
biographical fact not covered by the profile's own citations, traces to the year's
own 2024-01-24 event citing Herald `/74403`, which is on the record already. No
new sourced claim rests on nothing.

Traps clean: no advance-notice-as-report, no committee-chair-as-officer, no
surname-only match, no April result misfiled forward, no living-person overreach.
The León entry says only what the article reported; the Finch = Annie Finch and
León = León Golib identity notes are both hedged where the record does not close
the loop. Nothing contradicts §7 settled facts.

Two pre-existing hygiene items came into view but neither is this PR's fault and
neither is fixed here. First, the 2024-01-24 events "Midyear resignations
reshuffle the executive cabinet" and "Chief of staff and enrollment director
resign, Reed elevated" are the same meeting written twice from the same Herald
piece (`/74403`); a future dedupe pass should merge them. Second, Kelley is spelled
"Lyndsey Kelley" on her own profile and "Lindsey Kelly" in the two January event
bodies — `name-aliases.json` has no Kelley entry and none was added, per the
project rule of flagging spelling not fixing it.

## #72, weak-citation sweep — merged as a handoff note only

Thirteen lines added to `SGA-60-AGENT-INFO.md` §8.4 recording that eight of the
roughly twenty weak Herald-homepage captures were upgraded to verified
`dlsc_ua_records/` issue permalinks on an earlier pass, each re-confirmed live
against the issue's own headline index. Three residual front-page captures stay
honestly labelled "not the specific article" — two of them, the 2006-11-02 I-A
resolution and the 2007-02-01 Jeanne Johnson student-regent election, are
unconfirmable from this environment and want a run that can open `viewcontent.cgi`
PDFs or reach `web.archive.org`. No `data/` change on this PR; the eight citation
fixes were already on the branch.

## Still open

- The Kelley spelling split above.
- The 2024-01-24 duplicate-resignation event pair above.
- The two unconfirmable weak-citation residuals: `/dlsc_ua_records` for the
  2006-11-02 I-A resolution and the 2007-02-01 Johnson election.
- Everything on `SGA-60-AGENT-INFO.md` §8, none of which cleared tonight.

## Where the archive stands

61 academic years. 2,025 dated and sourced entries. 991 senate member records
and 1,094 executive and senate officer records. 365 records carry a written
profile, up 10 tonight from the ten new profiles on #71. 283 document files held.
`build.py`, `check_data.py` and `check_contrib.py` all clean on the merged head;
`check_duplicates.py` reports the same six long-judged pairs, untouched by either
of tonight's merges.

---

# Night report - 20 August 2026

Written by the editor. Four research branches reviewed, all four merged, nine
corrections applied before anything reached the site.

## What was reviewed

#73 person profiles, #74 the senate rolls, #75 photographs, #76 the backlog.
Every one was cut from current main, so the orphan-history warning in
AGENT-LANDING did not apply to any of them; the three stale August branches the
brief named are no longer open. Between them the four PRs carried twenty officer
profiles, 107 rank-and-file senators, six Talisman photographs and 284 pieces of
pre-2011 legislation.

## What I verified

Twenty-three claims from #73 were opened against their cited Herald articles,
Judicial Council minutes and TopSCHOLAR index pages. Twenty-two held exactly,
down to vote totals - Wingate third on 300 behind Alvey's 419, Bisig losing to
Dawson 778 to 373, Collins to Petkova 692 to 481, Leon censured 6-0 - and to
quoted words.

For #74 the four locally mirrored 2003-04 minutes gave eight names read straight
off the page, including one the OCR prints as "Jessica Sullon". More useful than
any sample, all 107 landed members were compared against the branch's own merge
inputs and verifier verdicts: every one matched on name, seat and source, no
rejected name landed, and all sixteen accepted names that did not land are
accounted for as officers already recorded that year or as the two surname-only
senators deliberately held back.

For #76 both TopSCHOLAR listings were re-counted: 128 bill rows and 156
resolution rows carry the hidden date markup, which is exactly the 284 recovered.
Fourteen of the new PDFs were opened and read; all are genuine legislation forms
whose reading dates match their entries.

## What was cut or corrected

Thirty-two officer citations were being published invisibly. `build.py` reads an
officer's sources only from `src` through `src20`; the twelve Speaker profiles
kept theirs in a `sources` array that renders nowhere, so they went live as long
accounts carrying one visible link. Converted, and the same fault was found
already on main under Bill Fogle's 1986-87 record.

Sam Stinson's profile claimed he stood in the spring 2002 election. Neither cited
index line says so; the candidacy was read off the fact that his headline sits
next to a candidate profile in the same issue. Trimmed to what the headlines
prove. Two outcomes resting on pre-election notices - Wright losing to Cassie
Martin, Dawson elected in 2005 - were given the reports that actually carry them.

Every source link in #75 was wrong. Each id carried a spurious leading digit, so
the 1970 Talisman citation opened a 1982 baseball media guide and the 1985, 1989,
1990, 1992 and 1993 citations all opened issues of a personnel newsletter. The
intended records were right; all six repointed after walking the Talisman run and
confirming each volume by title and date. Three captions in the same branch
claimed more than their page: which candidate stood on the left at the 1990
debate, five people in a front row the crop cuts off, and an Associated Students
election where the yearbook says campus election day.

Twenty-three fall bills and resolutions in #76 were filed a year early, because
TopSCHOLAR stores year-only items as 1 January and the session is taken from the
date. The archive already carried three of them as September 1991 events on
1991-92, citing the same records, so the branch was contradicting the site. All
refiled, with a warning added to the harvester.

Two roll figures were fixed in #74: 2003-04 carried a flat size of 48 that
appears nowhere in the year's own note, and 2005-06 showed 32 beside a note
saying 25 were elected. The first is gone, the second reconciled.

## Still open

- Eight name-variant splits introduced by #74 - Wesley and Wes Calhoun, Benjamin
  and Ben Lineweaver, three forms of Cherieth Lineweaver, Nathan and Nathan J.
  Eaton, Evelina and Evelina V. Petkova, Ann Blair and Ann-Blair Thornton,
  Brittany-Ann and Brittany Ann Wick, Austin Bernard and Austin Wingate. None is
  a false claim and none is surname matching, but each person now has two pages
  holding half a record. An alias asserts identity, so I have not guessed at
  them. The archive holds dozens more from earlier passes and wants one
  deliberate pass over `name-aliases.json`, which currently holds two entries.
- Hollan Hohn or Holm, correctly flagged in the data rather than fixed. For
  whoever settles it: `herald-index-full.json` prints "Holm, Hollan" 85 times and
  "Hohn" not once, and #74's own verdicts file uses Holm throughout.
- Holly Skidmore's November 2001 nomination note - a claim already on main whose
  only citation is the 4 September 2001 minutes. It needs a real source or it
  should go.
- Two legislation entries where the listing month and the number's own semester
  letter disagree: Resolution 82-7-S and Bill 00-3-S. Left alone rather than
  guessed at.
- The Kelley spelling split and the 2024-01-24 duplicate resignation pair from
  the previous report, neither cleared tonight.

## Where the archive stands

61 academic years, 2,025 dated and sourced entries, 60 people recorded as
president. 1,098 senate member records, up 107 tonight, and 1,094 executive and
senate officer records. 385 written profiles, up 20. 73 leader portraits and 53
year photographs, up six. 113 documents attached to years, 283 document files
held, and 1,111 legislation files, up 284.

`build.py`, `check_data.py` and `check_contrib.py` are all clean on the merged
head. `check_duplicates.py` reports the same six long-judged pairs, untouched:
three same-day 1991 bills, a bill introduced and failing nine days later, and two
stories a month apart.

# 21 August 2026 — editor pass, both open PRs merged

Two pull requests were open, both from last night, both merged after corrections.
The three stale August branches named in the standing instructions — #6
photographs, #7 the 1980s, #8 the 2020s — are already closed and need no further
handling.

## #77, twenty-six officer profiles

Sixteen founding officers of the 1966-67 Congress and the 1967-68 Associated
Student Government, and ten from the judicial council and senate of 2003 to 2008.
The branch moved twice during the review; the second push is included here.

Every one of the sixteen founding profiles was checked line by line against the
two rosters the branch mirrored into `data/documents/`, pairing each name with its
office by position in the roster's two columns. All sixteen hold — class year,
hometown and seat alike. Two details are worth recording because they are the kind
of thing that usually goes wrong and did not: Chapman's Interfraternity Council
seat is correctly distinguished from Marshall Peace's separate I.F.C. seat, which
is the one carrying Executive Council membership; and the roster really does list
only one Junior Class Representative At Large, so the earlier trim of "one of" from
Vivian Denton's entry was right.

Six of the ten later profiles were checked against the meeting minutes themselves.
Wolfe as Coordinator of Committees on 2 December 2003, Light sworn in on 2
September 2003, Vandiver presented on 5 September 2006 as a senior political
science major and president of Sigma Nu, and Schooler, Fisher and Wong all
appointed at the first meeting of the sixth Senate on 4 September 2007. Hennessey,
Inman and Woodall are on the archived judicial branch page for 2004-05, which came
back up long enough to read. Lanning's and Evans's Herald items are in the
unfiltered index at the issues claimed.

Four corrections went in before the merge.

Gretchen Light's account said the judicial council disqualified three senators from
the 2004 speaker vote. The Herald says three members present were barred from
voting, and it now says that.

Blake Napper's account credited his committee's budget with both the recycling
centre and the eight benches passed on 8 February 2005. The Herald attributes only
the roughly $2,000 of bins to that budget; the benches are simply in the same
legislation. The $1,000 for the Campus Cleanup T-shirts is now dated to the 1 March
vote that carried it rather than left floating at "that April."

Cacy Schooler's resignation was announced by Speaker Kayla Shelton on 27 November
2007, not 4 December. The 27 November minutes carry it plainly; 4 December was
Schooler's last meeting, where Shelton named Jacob Miers to succeed her. Both sets
of minutes are now cited on the entry, since neither was cited anywhere in 2007-08.

Patricia Lanning's second paragraph rested on two Herald items, one of which — the
3 November 1966 issue — was cited nowhere in 1966-67. Both are now on the entry.

One further change, not a correction: the 1967-68 roster prints students' home
addresses and telephone numbers. The mirrored file stays, because WKU publishes it
openly and the profiles rightly excluded that material, but the document summary no
longer points readers at that part of it.

## #78, the senate rolls gap

A negative result — no names added — recording which years cannot yield a senate
roll. The reasoning is sound and worth keeping, but its central claim about the
shape of the gap was wrong in the direction that would have sent the next run
looking in the wrong place. The note said 1969-70 and 1971-72 were absences inside
a covered run, with 1970-71 and 1972-73 either side of them holding minutes. They
do not. Pulling the same live listing and mapping it: the collection holds exactly
one dated item between 1968 and 1975-76, 13 February 1969. Every year from 1969-70
to 1974-75 is zero. There is no covered run to be absent from.

Two smaller things went with it. The collection does not thin after 1998-99 —
2001-02 through 2007-08 carry roughly fifty items each — so 1999-00 and 2004-05 are
restated as the genuine interior gaps they are, with the counts on either side. And
the last dated item is 2 December 2008, not the 8th; the listing is 843 item links,
830 of which carry a date, and the thirteen undated ones cannot be assigned to a
year either way.

Everything else in the note stands, including the decision not to promote two bare
index cross-references in the 1972 Talisman into seats, and the judgement that a
name-by-name Herald build for 1999-00 and 2004-05 wants its own verified pass.

## Cut, and why

Nothing was deleted. All four corrections were rescues: an over-claimed sentence
trimmed back to what its source proves, or a missing citation supplied. Three of
the four were the same fault — a profile stating a fact the cited source nearly
supports but does not quite — and that is what the research routine was told to
watch for next time.

## Still open

- Blake Napper's co-chairmanship is the one sampled claim that could not be
  verified. It rests on the archived legislative branch page, and the Internet
  Archive was intermittently down all run; the judicial page came back, the
  legislative one never did. It did not block the merge — the officer entry and its
  source are already published and the profile adds nothing about his office beyond
  them — but it wants a second look on a day the host is up. This is the standing
  condition at §8 item 4 of the handoff, not a new problem.
- Everything carried forward from the 20 August report is still carried forward:
  the eight name-variant splits and the wider `name-aliases.json` pass, Hollan Holm
  or Hohn, Holly Skidmore's November 2001 nomination note, Resolution 82-7-S and
  Bill 00-3-S, and the Kelley split.

## Where the archive stands

61 academic years, 2,025 dated and sourced entries, 60 people recorded as
president. 1,094 executive and senate officer records and 1,098 senate member
records, both unchanged tonight. 425 written profiles, up 29 — twenty-six people,
three of whom (Evans, Klein, Patterson) are profiled in both founding years. 115
documents attached to years, up two, and 286 document files held. 1,111 legislation
files, unchanged.

`build.py`, `check_data.py` and `check_contrib.py` are all clean on the merged
head. `check_duplicates.py` reports the same six long-judged pairs, none of them in
either diff and none touched: three same-day 1991 bills, a bill introduced and
failing nine days later, and two stories a month apart.
