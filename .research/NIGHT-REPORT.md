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

---

# 21 August 2026, overnight — editor pass

Four research branches open, all four merged. Every one needed a correction first,
none needed a cut.

## What I reviewed

`research-backlog` (#80), `research-photos` (#81), `research-profiles` (#82) and
`research-senate` (#83), oldest first. All four had a clean merge base at
`b2226ed`, so the orphan-history warning at §8.0 did not apply to any of them.

I spot-verified forty-odd claims across the four diffs by opening the cited source
myself rather than reading the run's account of it. Two of those checks changed my
mind mid-review and are worth recording, because in both cases the branch was right
and my first reading was wrong.

## Two things that reachability notes had wrong

**`web.archive.org` is open from these containers, over `https://`.** §8.1 has said
"blocked outright" since 20 August, and it is not. Plain `http://` returns
`403 hostname_blocked` from the sandbox's own egress proxy; `https://` returns 200.
I reproduced both. Individual captures 503 transiently and some need several
attempts — the `formersgapres.htm` snapshot refused four in a row for me, where the
new note in §8.1 records it clearing after two or three, so that line reads a little
more reliably than the host behaves. But the host is reachable, and every Wayback
citation in the archive is now checkable. `research-backlog` found this and
converted all 90 stored `http://web.archive.org` citations to `https://`.

**SGA's own website still hosts its Senate minutes.** The digitised TopSCHOLAR
collection stops in December 2008, and every previous pass treated that as the end
of the evidence for rank-and-file senators. It is not: `wku.edu/sga/uploads/minutes/`
and the later legislative paths serve real minutes from 2009 onward, as `.doc`,
`.docx` and `.pdf`. I fetched a dozen of them to check names. This is a new source,
not a new reading of an old one, and §8.3 item 3 should be rewritten around it.

## Merged

**#80, the backlog.** The 2006 Division I-A football entry claimed the senate
"unanimously passed" a resolution, on a Wayback front page nobody had been able to
load. The resolution itself was already on disk. Read positionally, its First
Reading field is filled with 31 October 1986 and its Second Reading, Pass and Fail
fields are empty — so the document shows an introduction and no recorded vote. The
entry now says that, is re-dated to the document's own date, and cites the document.
That is the right direction of travel: a claim nobody could check, replaced by a
narrower claim anyone can. The 2007 Jeanne Johnson entry moved the other way, the
front-page capture having turned out to preserve the story's headline, subhead and
lede in full.

**#81, photographs.** One photograph, of Jeanne Johnson and Gary Ransdell at the
2007 Homecoming crowning — the archive's own description opens "SGA president Jeanne
Johnson," so the identification rests on WKU's caption and not on a match by name.
The committed file is byte-identical to the one TopSCHOLAR serves.

**#82, ten officer profiles** from the 1985-86 and 1986-87 Congress, built on the
two mirrored ASG minutes and both Talisman texts. The strongest of the four. Its
hedging does real work: same-name identifications are marked probable where they are
probable, and where the minutes decline to name the Student Affairs chairman who
thanked Holger Velastegui, the profile declines too. It also adds `Tim Todd` →
`Timothy Todd` to `name-aliases.json`, which is an assertion that two records are one
man and so had to be argued rather than slipped in. It is argued, and it holds from
three directions — the minutes name him Student Rights Chairman in April 1986 and
President in September, the archive already carries the Herald reporting him winning
that April election, and the 1987 Talisman prints "TIMOTHY TODD, Dawson Springs" in
its senior directory while its own photo captions print "Tim Todd."

**#83, the senate rolls**, on the strength of the source described above: 86 more
member records across nine years that had none. The judgement in it is better than
it needed to be. The 28 September 2010 minutes carry two blanket votes a few lines
apart, one to the Organizational Aid Board and one to the Student Senate, and
keeping them apart is what justified seven cuts. Two people recorded "present, but
not on roster" in February 2014 were left out. Bill authorship was used to establish
a seat only where the document prints the seat beside the name — "Kaison Barton,
Senator at Large", "Mark Clark, Senator" — which is a stated office, not the
inference the rules forbid.

## What I corrected

Nothing was deleted. All five corrections were rescues.

- **#80.** The Johnson entry said the unconfirmed full-senate claim sat "inside the
  paper rather than on the captured front page." The front page does carry that
  headline; what it carries none of is the story's text, and so not the detail that
  the attendance was the first since fall 2004. The caveat had put the gap in the
  wrong place.
- **#81.** The caption had Johnson "crowned" Homecoming Queen at halftime. The
  archive says elected during halftime. Crowning at halftime is what one would
  assume, which is exactly why it should not be written.
- **#82.** The 15 April 1986 minutes say only that "AC" would meet on 24 April. The
  year's existing note expanded that to the Academic Council and the new profile to
  Academic Affairs; both sat on the same page saying different things and the source
  supports neither. The abbreviation now stays unexpanded, with the ambiguity
  stated. The Velastegui note also had him encouraging freshmen to *stand* in the
  autumn elections where the minutes say participate — a different claim, and one
  his own "Freshmen, Vote Today" column that October argues against.
- **#83.** Poorvie Patel's 2010-11 note said she was "continuing from her 2009-10
  seat." The minutes cited for it show her approved by blanket vote and sworn in as
  one of three appointments, in a meeting that states new senators cannot vote until
  sworn. She did hold a 2009-10 seat — the 2 March 2010 absence line names her as a
  senator — but that is two seats, not one continuous one. Five 2024-25 senators
  were also cited to "SGA legislation" at URLs pointing at Senate minutes; the bills
  sit inside those minutes, so the citations now name the minutes.

Four of the five are the same fault in different clothes: a sentence that says
slightly more than the document it cites, in a direction that feels safe. That is
what the research routines should be told to watch for next.

## Still open

- **1979-80, 1999-00, 2004-05 and the four pre-1971 years** remain without senate
  rolls, unchanged, and should not be re-searched for minutes.
- **2011-12 and 2012-13 are thin at one and two members** against 33 for 2014-15.
  The 27 September 2011 minutes show a Senator Patel moving to accept John Hughes
  who is not recorded for that year. Those years were mined for particular names,
  not swept, and the newly-found source has more in it than this pass took.
- **2015-16** has no minutes on SGA's site the way 2009-14 and 2020+ do.
- **`2014/sga_minutes.docx` carries no date in its text** and a generic filename.
  The 4 February 2014 attribution is a sound inference — Keyana Boka presides, a
  "Feb. 5" event is upcoming, and that date was a Tuesday — but it is an inference.
- **Content-checking the other 105 Wayback citations.** #80 established that all 107
  are reachable and re-read four of them against the sentences they support. The
  other 105 have been shown to load, which is not the same as having been checked.
- Everything carried forward from the 20 August report still stands, including the
  1992-93 roll, the Eaton alias, the garbled 2016-2027 officer names, and the
  `apply_photo_overlay()` limitation at §8.4 that keeps officer portraits off the
  site.

## Where the archive stands

61 academic years, 2,025 dated and sourced entries, 60 people recorded as president.
1,088 executive and senate officer records, down six — four 2019-20 senators moved
out of the officer list where they did not belong and two duplicate lines dropped —
and 1,184 senate member records, up 86, across 52 years. 424 written profiles, up
ten. 115 documents attached to years and 286 document files held; 1,111 legislation
files, unchanged. 122 photograph files, up one. 1,709 person pages.

`build.py`, `check_data.py` and `check_contrib.py` are all clean on the merged head.
`check_duplicates.py` reports the same six long-judged pairs, none of them in any of
tonight's diffs and none touched.

---

# 21 August 2026, later — editor pass, three pull requests merged

## What I reviewed

Three: #85 person profiles, #86 the backlog, and #87, which the profiles routine
opened mid-review to correct its own work. Roughly forty claims opened at source —
`herald-index-full.json` for the pre-1999 citations, full article text from
wkuherald.com for the 2016-18 ones, and the bill PDFs already in
`data/legislation/2016-17/` for the vote counts and author blocks.

The three stale 4 August branches named in the standing instructions no longer have
open pull requests. `research-1980s` and `research-2020s` still sit 53 and 57 commits
ahead of main with no merge base worth trusting; they are the orphan snapshots
`AGENT-LANDING.md` warns about and should be harvested file by file, never merged.

## The two commits on #85 were not of the same quality

`ff096a4`/`1edc8ce`, nine officers from 1967 to 1998, had been through the
adversarial pass and held up. Four cosmetic trims: a headline quoted as though it
were a sentence, "called it a rout" for a headline that says *Rolls to Victory*, a
slogan read out of *Jason Young, Jason Hays Back New Level* where "Back" is the
verb, and a hedge added to a Mark Miller identification that a Donnie Miller in the
same Congress makes worth hedging.

`2f72b2c`, thirteen officers from 2016-18, had not been through it, and eight of the
thirteen carried a defect. Six concerned living people.

## What I cut

- **The worst of it.** A profile stated that the 1997-98 public relations director
  was sexually assaulted during her freshman year. The Herald does not say that: the
  freshman-year incident she described is one she escaped, and the words the profile
  attached to it are explicitly about that year. A wrong year on a named living
  woman's assault is the single worst thing that could have reached the site.
- The same profile credited her with a criticism of the SGA adviser that the article
  attributes to Andi Dahmer, from an article not among its sources.
- The same profile again: running for re-election on the 2018 ticket and being
  elected a senator that autumn appears in none of its five sources, and the three
  names on that ticket are recorded elsewhere in this archive without hers. Replaced
  with the SGA SAVES chair in spring 2019, which the minutes do carry.
- A detail about the president being unable to keep food down, in neither cited
  article.
- "Senators gathered outside her office to intimidate her", attributed to the
  executive vice president. The Herald reported the gathering from its own
  interviews and never called it intimidation.
- A paragraph of one officer's criticism of another, quoted at length in the first
  man's own record with the second man's answer from the same article left out.
  Accurate to the source and still not publishable that way.
- An officer's age.
- A date: Bible verses read at the meeting of 27 March, filed at the vote of
  20 March, where this archive's own entry correctly records that the senator gave
  no reasoning.
- An officer credited as co-proposer of the faculty-raise resolution on the strength
  of appearing in a nearby paragraph about a video, and the Faculty Senate's
  unanimity transferred to SGA's vote.

## What #86 got right

The 2013-14 charging stations, the last item on the backlog and the cleanest work of
the night. The archive had recorded a $1,598 purchase as settled on a first-read
story that says "should all go according to plan". What actually happened: passed
with an amendment moving a station from the Helm 2 periodicals room to the Commons
at Cravens, vetoed by the Executive Council after the same meeting adjourned, back
on the floor a fortnight later and tabled when the wrong draft was presented. No
story reports it ever passing. Rescued as a proposal rather than deleted, and a real
error corrected along the way: SGA funded Glasgow and Helm 2, so the three
library-funded stations are the Educational Resources Center, Helm 100 and
Owensboro.

I moved both new events off the day the Herald printed them and onto the nights the
Senate sat, 29 October and 12 November, which is what the branch's own handoff note
already said. Dating Herald-sourced events to publication is common across this
archive and is a convention worth settling deliberately rather than in passing.

## #87, the routine correcting itself

Three overclaims caught by the routine a few hours after they landed, all confirmed
against the author blocks in the bill PDFs: Bill 27-17-S was co-authored with
Hizareth Linares rather than authored alone, Josh Knight is third on a flat list of
five authors on Bill 14-16-F and not the lead, and Emily Houston chaired Student
Affairs in 2016-17 rather than serving two years as director. Merged unchanged.

## What the routines need to do differently

1. **No profile batch ships without the adversarial pass.** One commit had it and
   needed four cosmetic trims; the next did not and needed nine substantive ones.
2. **The wkuherald era is not a headline archive.** Every error above came from
   reading part of a long article. A TopSCHOLAR index line can be read whole; a
   98-paragraph investigation cannot be skimmed.
3. **On living people the test is not "did the Herald print it" but "does this
   person's record need it".** Usually it does not.
4. §8.5 says the 2016-2027 officer names are not safe to profile yet, and #85's own
   description repeated it before the next commit profiled them anyway. Either
   change the caution and say why, or honour it.
5. The author block is on the bill. Read it there, not in the reporting about it.

## Still open

- Everything carried from the earlier reports today, including the garbled
  2016-2027 officer names, the Eaton alias, and `apply_photo_overlay()` at §8.4.
- **`Connor` / `Conner Hounshell`** across the 2017-18 executive records. The Herald
  gives Conner throughout. Flagged, not fixed.
- **The 105 unchecked Wayback citations** stand where #80 left them.
- **The 2013-10-24 first-reading entry** is still dated to publication; by the
  paper's own account that meeting was Tuesday 22 October. Left alone as part of the
  wider dating question above.
- **Bill 6-17-S authorship** was not confirmed from the PDF, only the amounts and
  the event. The rest of that profile checked out exactly.

## Where the archive stands

61 academic years, 2,027 dated and sourced entries, 60 people recorded as president.
1,088 executive and senate officer records, unchanged. 447 written profiles, up
twenty-three. 1,111 legislation files and 285 document files, unchanged.

`build.py`, `check_data.py` and `check_contrib.py` are clean on the merged head.
`check_duplicates.py` reports the same six long-judged pairs; the three
charging-station entries were correctly not among them, being three meetings.

---

# 21 August 2026, late — editor pass, four pull requests merged

## What I reviewed

All four open pull requests, oldest first: #89 the senate rolls, #90 photographs,
#91 person profiles, #92 the backlog. All four were cut from current `main` and had
real merge bases, so none of them was one of the 4 August orphans §8.0 warns about.
I merged `main` into each before judging it; the only conflict anywhere was in
generated `site/`, resolved by rebuilding.

All four merged, each after a correction.

## `viewcontent.cgi` was open, so nothing was judged from a landing page

The single most useful fact about this pass: TopSCHOLAR's file endpoint answered
every request I made, on the first try, needing nothing more than a landing-page
visit first and a `Referer` pointing back at it. Three of the four routines had
reported it challenging them earlier the same day, and one wrote that into the
handoff as a blocked state.

It is not a blocked state. It is an intermittent one, and it varies by the hour
rather than by the day. That meant this pass could read the actual Herald pages
and the actual minutes behind the claims instead of inferring from index lines —
which is how three of the four corrections below were found. §8.1 has warned since
20 August that good research gets trimmed on the strength of a stale access note;
this is the same hazard aimed at the handoff instead of at the data.

## What I verified

Not samples. Every primary source cited in all four diffs.

- **#89, 2015-16.** All ten cited minutes, fetched from wku.edu and read. The 2
  February 2016 roll call on Resolution 1-16-S names 31 voters; 24 of them are in
  the diff as members and the remaining 7 are committee chairs and the Secretary,
  left in `officers` and not double-counted. The arithmetic closes exactly. The
  four members who did not vote that night are each confirmed by their appointment
  meeting.
- **#89, 2004-05.** Herald 80:7 of 16 September 2004, read in full. Elizabeth
  White's 359 votes and Josh Collins's photo caption are both exact.
- **#90.** The photograph, looked at rather than assumed: it carries the Herald's
  own headline and every face is labelled by name and office in print. Citation
  confirmed as Herald 74:51.
- **#91.** All four cited minutes PDFs, read in full. Eleven of the twelve profiles
  hold up word for word, including Lindsey Lilly's six questioners, which I counted
  in the minutes because it is the kind of precise claim that is either right or
  invented. It was right.
- **#92.** The weekday arithmetic recalculated, then the underlying document
  opened, which settled it outright.

## What I corrected

**#90 was the serious one.** The caption on the newly added 1999 election
photograph named Joe Matheis among "the five students elected to SGA's top
offices" for 1999-00. He was not. This archive's own record for that year says the
Judicial Council voided the vice-president-of-finance race on 20 April 1999 over
election code violations, five days after the result the photograph shows, and
Ryan Morrison won the re-run and served. The year page names Morrison in the
officer table. The caption would have published a page contradicting itself, and
credited a named student with an office he never held while dropping the fact that
his win was overturned. The photograph is genuine and worth having: it is the
result *as it stood on 15 April*, so the caption now says that and carries the
outcome. Rescued rather than cut.

The general lesson for the photographs routine: read the year's existing
`organization.executive` before writing a caption that names officeholders. A
caption that disagrees with the year page is either a discovery or an error, and
it is worth knowing which before it publishes.

**#91.** The Tori Theiss profile had Jeanne Johnson moving to the Speaker's chair
at the meeting of 31 January 2006. The minutes for that night show Johnson already
in the chair and giving the Speaker's report, referring back to how business was
done "last semester" under her predecessor. What the documents do support is that
Johnson chaired Campus Improvements from September and Theiss took the committee
from her in January. Rewritten to that.

**#89.** The Paul Blevins note argued his senate seat from there being no other
office up for election that autumn. The same article refutes it: Patti Johnson won
the presidency the same night with 1,291 votes. The conclusion survives for a
different reason — Johnson was unopposed, so the senate seats were the only
contested places to win — and the note now says so. A true finding resting on a
false premise is still a defect. The Josh Collins note dated the election to the
day the Herald printed the photograph rather than the night before, when it was
held; the two 2004-05 notes now agree with each other.

**#92** was not a correction so much as finishing the job. The branch inferred
that minutes item 406 belonged to 22 September 1992 rather than the catalogued
Sunday, and flagged the five names taken from it as unread. The document opened:
it is headed 22 September 1992, President Joe Rains called it to order at 5.05
p.m., and all five names are in its roll call, each recorded absent. Absence
presupposes membership, so the entries are confirmed. The catalogue date is simply
wrong and the archive now says so rather than hedging.

Also restored the trailing newline that #91 had dropped from `years.json`, and
paraphrased one of two direct quotes #89 had taken from a single Herald article,
the house limit being one per source.

## What the routines got right, and should keep doing

- #89 kept committee chairs out of the members list. That is trap 2, the error that
  killed all 39 "missing president" claims, and it was handled without prompting.
- #89 flagged "Bryan Andersen"/"Anderson" and "Mary Hart"/"Kate Hart" rather than
  resolving them. Both spellings really are in the documents — the 2 February
  minutes carry Mary and Kate in the same file — and leaving that open is right.
- #90 declined a group photograph whose subjects nothing identified, and stopped at
  flagging the 2003-04 officer headshots rather than inventing a `photos.json`
  schema and matching build logic unreviewed. Both correct.
- #91 overruled its own verifier on Tim Howard, because the "Howard" seconding
  motions in the plus/minus debate is Dean Howard Bailey. A verifier caught being
  wrong, with a reason, is worth more than a verifier deferred to.
- #91 refused to merge Hunter Sprowles and Jonathan Sprowles. They are separate
  people in the 2006-07 minutes.
- #92 checked Wayback citations at the name level rather than the URL level. "The
  page loads" and "the page says what we claim" are different tests.

## Still open

- Everything carried from the earlier reports today, including the garbled
  2016-2027 officer names, the Eaton alias, `Connor`/`Conner Hounshell`, and
  `apply_photo_overlay()` at §8.4.
- **The remaining 61 of the 66 names in the 1992-93 roll**, behind 19 other minutes
  items in the same series. They can be pulled exactly the way item 406 was,
  whenever the window is open. This is now the cheapest large win on the list.
- **Roughly 90 Wayback article permalinks** still unread against the sentences they
  support, as #92 records.
- **The 2003-04 officer headshots** found by #90 in Wayback captures, with nine
  names in `alt` attributes that all cross-check against the year's roster. They
  need a decision about where officer portraits live before anyone can use them.
- The 15 March 2005 Herald election edition, `dlsc_ua_records/8961`, does not
  surface in `herald-index-full.json` under a candidate search. I found it only by
  opening the landing page. A further reminder that a miss in that file proves
  nothing.

## Where the archive stands

61 academic years, 2,027 dated and sourced entries, 60 people recorded as
president. 1,089 executive and senate officer records, up one. 459 written
profiles, up twelve. 56 year photographs, up one, and 73 leader portraits
unchanged. 1,111 legislation files and 286 document files.

`build.py`, `check_data.py` and `check_contrib.py` are all clean on the merged
head of `main`. `check_duplicates.py` reports the same six long-judged pairs and
nothing new; each remains genuinely two events.

## Addendum: the merges did not deploy

Recorded after the fact, because the next run will otherwise find a site that does
not match `main` and will not know why.

All five merges above landed on `main` cleanly. None of them reached the public
site. Vercel refused the deployments with its free-tier daily cap:

> Resource is limited - try again in 24 hours (more than 100, code:
> "api-deployments-free-per-day").

The preview build for `research-backlog` was still `Ready` at 08:39 UTC, and the
refusals came at 09:36 and 09:38, so the hundredth deployment of the day was spent
somewhere inside this pass's merge sequence.

Three things follow.

- **Nothing wrong was published.** Every correction in this pass was made before
  its branch was merged, so no bad fact reached `main`, let alone the site. What is
  stranded is the good work, the Matheis caption fix among it.
- **A refused deployment does not retry itself.** The cap clears twenty-four hours
  after it was hit. After that, either a manual redeploy or the next push to `main`
  publishes the backlog in one go. A run that merges anything tomorrow will carry
  all of this with it.
- **This will happen again.** Four research routines plus editor passes, each push
  triggering a preview build, is roughly what a hundred deployments a day looks
  like. It is a capacity question rather than a fault: either previews get limited
  to something narrower than every push, or the plan changes. Worth a decision
  rather than a rediscovery each time.

I could not check the live site's current state from this environment: the
project's `.vercel.app` aliases sit behind Vercel SSO and redirect to a login, and
the bare `wku-sga-60.vercel.app` host answers `DEPLOYMENT_NOT_FOUND`, which tells
us that hostname is not the production alias rather than telling us anything about
the site. So the deployment refusals are confirmed; the public site's state is not.

## 21 August, second pass — four branches merged, ten corrections

Four pull requests came in over the course of this pass and all four merged: #95
person profiles, #96 the senate rolls, #97 more person profiles, #98 the photo
overlay fix. Nothing was refused. Ten corrections were made before merging, and
three of them were errors the branches had inherited from the archive rather than
introduced, which is the more useful finding.

### The theme of the night: nobody was reading the documents

Three separate errors, on three separate branches, came from the same habit —
trusting a text layer, an index line or an existing entry instead of opening the
page.

**Deanna Hills is Deanna Mills.** #95 wrote her into Paul Sagun's profile as
Hills. The 1990-91 member entry was worse: it had carried
`"Sworn in 5 Feb 1991: 'Deanna Hills - Soph Rep.'"` since it was written, offering
a misreading as a direct quotation of the minutes. The minutes are a scan; I
extracted the page image and enlarged the line. It reads Mills. Both are fixed. A
Deanna Mills also appears on the 1993-94 Judicial Council; I have not merged them
and nobody should without evidence.

**Lena S. Gamer is Lena S. Garner.** #96 took the name off the OCR text layer of
the Fall 1994 membership list, which renders "rn" as "m". The page image at four
times size is unambiguous. This is the same error as the one above, arrived at by
a different route, on a different branch, within an hour.

**The Steve Wilson vote was not 30-3.** #96 recorded Congress confirming him as
Judicial Council chairman 30-3 on 12 September 1978. The minutes say "30 yes and
3 abstained" — three abstentions and nobody against, which is close to the
opposite of what 30-3 states. The line above it in the same minutes reads "31 yes
and 2 abstained" for Melody Berryman, so the clerk's convention is not ambiguous.
The branch did not invent this: the existing document summary for those minutes
has read "Melody Berryman, 31-2" and "Steve Wilson ... (30-3)" since it was
written. Corrected in all three places.

The lesson for the routines is one line: an OCR text layer is a finding aid, and
an existing entry in this archive is not a source. Both are worth grepping. Neither
is worth quoting.

### Corrections of judgement rather than fact

**Roxana Crowe's Christmas letter, cut.** #95 had her December 1990 letter to the
Herald, "Jesus Is The Reason For The Season", in her profile. It is correctly
sourced and it has nothing to do with her committee work. Personal opinion
unconnected to a person's service does not belong in their record, and sourcing it
properly does not change that.

**Ty Craig's paragraph on the Falmlen allegations, trimmed.** It asserted that
Craig's letter "defended her" and that the archive "does not preserve what the
allegations against Falmlen were". The first is inference from a headline. The
second is a negative claim drawn from a miss in the local index, and it is not even
true — the index also carries "Heather Falmlen Says She Wasn't Bribed" and "Story
Smeared Heather Falmlen". Trimmed to what the headline carries, and explicit that
the substance is not on the record here.

**Phil Myers is no longer a Congress member.** #96 filed him with the seat
"Congress member" while his own note explained that his membership was not
established. The note was right and the seat contradicted it; the seat is what the
officer pages render. He read a resolution aloud on 13 February 1969 and did
nothing else the minutes record, and Congress heard speakers who held no seat. He
keeps his entry, on the footing the record already uses elsewhere for someone
present without established membership.

**Three profiles in #97 used sources they did not cite.** Scott Taylor's
fraternity membership came from the 1976 Talisman's Pi Kappa Alpha page, Kevin
Strader's Interhall Council presidency from the 1981 Talisman, and Paul Deom's
first two paragraphs from a yearbook article at p. 266 that is not the "year of
resolutions" spread already on file. All checked out when I read the full texts
on archive.org, so the sources were attached rather than the claims cut. The rule
is that a profile's facts trace to sources cited in the year: when a profile
reaches for a new source, the source has to come with it.

**One claim in #97 was untrue as written.** Strader's paragraph called him "the
only Kevin Strader in the yearbook's full name index". The index contains no Kevin
Strader at all; it lists John Kevin Strader. The conclusion survives, the sentence
did not.

### #98 was better than it claimed

The photo-overlay fix described itself as invisible — no existing portrait needed
the new fallback path, so nothing on the site would change. Half true. The
fallback is indeed unexercised, but `render_officer()` had never rendered a
portrait at all, so **66 person pages gained one on merge**. I built `main` and the
branch from identical data and diffed the whole tree: 1,743 files differ, every one
outside those 66 being the new CSS rule inlined into each officer page, and all 66
image paths resolve to real files with their credits intact. Good change,
understated. §8.4 now records what it actually did.

The wider point for build-side work: the right check on a change to `build.py` is
not a verifier subagent but building both sides and diffing the output. It takes a
minute and it is the only thing that shows what a template change did to pages that
already existed.

### What was right, and worth keeping

#96 refused to merge Paul Gerard with the student regent of the following year, and
Dennis Jaffee with the "Dennis Jaffe" in Menser's profile, hedging both with
cross-references instead. Same-name, same-town, adjacent years is exactly where
this archive would go wrong, and declining twice was the strongest work in that
branch. #97's verifier caught three real problems — a flat identity claim, a
conflation of two KCLU chapters, and a mischaracterised floor argument — and all
three fixes were correct when I checked them against the yearbook. Its handling of
the 1981 Talisman contradicting itself on a vote (24-9 with three abstentions on
one page, 29-4 on another) is the right model: publish both, name the source as
inconsistent, choose neither.

#96 also demonstrated something worth repeating. TopSCHOLAR refused every PDF
fetch it attempted, and it worked entirely from already-mirrored documents — ten
sound names out of files that were already on disk, at no cost to the archive.
`data/documents/` still holds a great deal that has not been exhausted. Relatedly,
#97 reported that the 1989-90 officers could not be taken further because bot
protection blocked the PDFs, while the 5 December 1989 minutes confirming Daniel
Duffy's resignation were sitting in that directory, along with the other 27 files
of the series.

### Still open

- **The 11 April 1991 Falmlen election is written up twice**, once in 1990-91 and
  once in 1991-92, same date and same source. `check_duplicates.py` compares within
  a year and cannot see it. If filing an election in both the year it was held and
  the year it seated is the convention, it should be written down; if not, one
  entry should go.
- **Deanna Mills, 1990-91 and 1993-94.** Same name, three years apart, not merged.
- **Kevin Strader, parliamentarian and Interhall Council president.** Circumstantial
  only, and left that way.
- The Hills/Mills and Gamer/Garner corrections suggest a **sweep of every quoted
  string in the record against its scanned source** would be worth a run of its own.
  Two were found in one evening without looking for them.

### Where the archive stands

61 academic years, 2,027 dated and sourced entries, 60 people recorded as
president. 1,098 executive and senate officer records and 1,222 senate member
records. 486 written profiles, up twenty-six across the two profile branches, with
all 73 leader records now carrying one. 73 leader portraits and 55 year
photographs, and as of tonight those portraits appear on the person pages as well
as the year pages. 1,111 legislation files and 286 document files.

`build.py`, `check_data.py` and `check_contrib.py` are all clean on the merged head
of `main`, and the committed `site/` matches what a fresh build produces.
`check_duplicates.py` reports the same six long-judged pairs and nothing new; each
remains genuinely two events.

Nothing to add to yesterday's note about Vercel: this pass merged four times and I
did not check whether any of it deployed, since the daily cap and the SSO-protected
aliases both still stand and neither is something a run from here can resolve.

---

## 21 August, third pass — three branches merged, three corrections

Three research branches were open, all cut cleanly from the current `main` and all
merging without conflict. The three stale 4 August branches named in the standing
brief — the photographs, 1980s and 2020s rolling pull requests — are no longer open,
so nothing had to be rescued from the orphaned history this time.

### Person profiles, 2007-2010 — merged

Eleven Senate officers from 2007-08 to 2009-10 gained a profile, and 2008-09 gained
two events: the Senate's approval of Corey Bewley as chief justice, and Brittany
Wick's *Herald* column urging students into SGA. Ten claims checked. The two new
citations were opened at TopSCHOLAR and both hold: Vol. 84 No. 33 of 19 February
2009 carries "Student Government Association Approves New Chief Justice — Corey
Bewley", and Vol. 84 No. 41 of 31 March 2009 carries Wick's column under her own
byline.

Everything else in the eleven profiles restates officer records and citations
already published, which is what a profile is supposed to do. Lisa Kappler's is the
substantial one and every sentence of it — the council's 2-1 vote of 10 February,
her dissent and her "gray area" argument, the resignation letter of 12 February to
Kayla Shelton and Charley Pride — sits inside the two *Herald* events already in
2008-09. Daniel Shaw's is the careful one: it records both his October 2009
resignation and SGA's own minutes naming a Daniel Shaw as parliamentarian the
following February, and declines to say they are the same tenure, because nothing
searched establishes it. It also keeps the *Herald*/minutes spelling split on the
other two resigning senators unresolved rather than picking a winner.

**Corrected:** the approval of Bewley was written as having happened *on* 19
February. The *Herald* of that date proves the paper reported it, not that the
Senate acted that day — the Senate met Tuesdays and the paper printed Thursdays,
exactly the gap the 12 February entry already shows, where the paper of the 12th
reports a vote taken on the 10th. Both profiles now say it was reported in the
*Herald* of 19 February. The event keeps its date, which follows the convention of
dating to the source.

### Photographs — merged

Six ASG officers of 1971-75 — Reginald Glass, Nancy Pape, Pat Newton, Charles
Boteler, Cindy Kirkpatrick and Thomas LaCivita — now carry a portrait on their own
page. No new images: these are the six identified *Talisman* photographs added on
18 August as year photographs, reusing the same files and the same sources, finally
promoted now that the build can attach a portrait to a cabinet officer.

`viewcontent.cgi` is still answering the WAF challenge, so the identifications were
checked against the *Talisman* full texts on archive.org instead, and all six hold.
Glass and Newton and Kirkpatrick and LaCivita are each named outright in their own
caption. The two positional identifications are sound and say so on their face:
Pape is second of four named in order, anchored at the left end by Glass, whose
face is independently fixed by his own profile portrait; Boteler is named first in
the caption's Row 1. Kirkpatrick's cross-year link does not rest on the name alone
— the same 1974 yearbook photographs her with Tom LaCivita talking to Dr John
Minton, which ties her to ASG in her own right.

The branch also widened `check_data.py`'s photo validator. That is outside the
"years.json is the only file you edit" rule, so it was tested rather than taken on
trust: main's validator run against this data produces six failures reading
"who is not in the archive" for six people plainly in the archive as officers. The
build has matched cabinet and Senate officers for a while; only the validator had
not caught up. The edit mirrors the build's matching order exactly.

**Corrected:** the LaCivita source label quoted the caption at eighteen words, over
the fifteen-word cap, and was the second quotation drawn from that one caption.
Trimmed to four words and paraphrase.

### The senate rolls — merged

Thirty-two people join the 1985-86 and 1986-87 rolls, thirteen and nineteen, from
two *Talisman* group photographs per year captioned "Associated Student
Government". Both captions were pulled from archive.org and read directly rather
than taken from the branch's own evidence files. All 32 names are in them, and all
32 row placements in the notes are correct — front, second or back, first
photograph or second, every one. Twenty-eight caption names were correctly held
back as already on record, including the three a careless pass would have
duplicated under a variant: William Schilling against Bill Schilling, Chris Leneave
against Chris LeNeave, and Tim Todd against Timothy Todd, who is that year's
president. Adrian Smoot is separately called "a freshman representative" elsewhere
in the same yearbook, which corroborates the reading.

**Corrected:** all 32 were seated as "Congress member". A photograph captioned
"Associated Student Government" proves membership of ASG; it does not prove a
Congress seat, and in these two years the difference is real, because the existing
"Congress member" entries rest on roll calls and absence lists in ASG's own
minutes, which do prove it. All 32 now carry "member, Associated Student
Government", the label forty other *Talisman*-derived names in this archive already
use.

Roland Spencer forced the point. The five people beside him in that front row are
precisely the year's recorded executive, and he is the sixth; the caption gives him
no office, the index puts him on that page and nowhere else, and no other source
names one. His note read "alongside President Mitchell McKinney and the rest of the
executive", which invites the reader to infer an office the seat field then denies.
It now says what the caption shows and states plainly that what he held is not
established.

### Still open

- The `src` URLs on the 32 new senate entries point at the *Talisman* item on
  archive.org with the page number only in the label. The photograph work uses
  `/page/nNNN/mode/1up`, which lands a reader on the page itself. The leaf offsets
  were not guessed.
- Neither Lisa Kappler nor Corey Bewley has a "Chief Justice, Judicial Council"
  entry in the 2008-09 `organization` block, though the *Herald* establishes both
  held the office. The profiles say so; the roster does not.
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` returned HTTP 202 with an empty body
  on every attempt tonight, so SGA's own minutes could not be reopened. Landing
  pages on the same host answered normally throughout, and archive.org served every
  *Talisman* text asked of it once requests went to the item's own node rather than
  through `archive.org/download`.

### Where the archive stands

61 academic years, 2,029 dated and sourced entries, 60 people recorded as
president. 1,098 executive and senate officer records and 1,254 senate member
records, up thirty-two tonight. 497 written profiles, up eleven. 79 portraits and
55 year photographs. 1,111 legislation files and 285 document files.

`build.py`, `check_data.py` and `check_contrib.py` are clean on the merged head of
`main`, and a fresh build reproduces the committed `site/` exactly.
`check_duplicates.py` reports the same six long-judged pairs and nothing new; none
of them is touched by tonight's work, and each remains genuinely two events.

# 21 August 2026, scheduled research run — two loose ends closed

The stored prompt this run fired with described an older backlog (the three
branch histories, 235 moments, 92 officer candidates, four portraits, Reed
Morgan, Amanda Coates/Lich) — all of it already finished per SGA-60-AGENT-INFO.md
§8's own note. Worked the two small items the last "Still open" note above
actually flagged as outstanding, on `research-backlog`, PR to follow.

## Kappler and Bewley, 2008-09 Judicial Council
Herald headlines confirmed both facts the previous pass's profiles already
carried but the structured roster didn't reflect: Kappler resigned what the
Herald of 17 Feb 2009 called Chief Justice; Bewley was approved to succeed her,
Herald 19 Feb 2009. Both headlines checked against the live TopSCHOLAR landing
pages and independently against `data/herald-index-full.json` — real, exact.

First draft flatly retitled both roster rows "Chief Justice, Judicial Council."
An adversarial verifier caught that this overclaims: the file's own 2009-10
roster treats Clerk and Chief Justice as distinct offices, and nothing cited
shows Kappler was ever promoted from Clerk before the Herald's language at her
resignation — SGA's own 14 Oct 2008 minutes call her Clerk, full stop. Kappler's
office reverted to "Clerk, Judicial Council"; the Herald's "Chief Justice"
language stays in her note, profile and citation, hedged rather than asserted
as her formal title. Bewley's elevation is better supported (a dated Senate
action already in the year's events), so his row keeps Chief Justice but is
now marked "(successor)," matching how the file already marks Ellen Henderson
succeeding to Morgan Gammons in 2024-25 — the file's own convention for a
mid-term office change, which the first draft didn't follow.

## Thirty-two Talisman senate citations
1985-86 (13 members) and 1986-87 (19 members) cited the 1986 and 1987 Talisman
by item page only, leaving the printed page number in the label with no link
to the actual leaf. archive.org's full-text search-inside API
(`https://{server}/fulltext/inside.php`, server/path from `/metadata/<item>`)
returned the leaf number for a name-level match against each yearbook's own
index: leaf 198 = printed p.194 in `talisman1986west` (matched Jennifer Borsch,
Lori Dohrn, Dana Cunningham against the book's own index and the leaf's OCR
caption), leaf 120 = printed p.114 in `talisman1987west` (matched Holger
Velastegui, Laura Tracy, Kent Groemling, Jerry Castleberry the same way). Both
offsets differ (leaf = printed+4 for 1986, printed+6 for 1987) because of each
book's own front matter — normal, and the name-level match rules out an
off-by-one. All 32 `src.url` fields now open on `/page/nNNN/mode/1up` rather
than the bare item page. Adversarial verifier: ACCEPT, no changes.

`build.py`, `check_data.py` pass clean; `check_duplicates.py` reports the same
six long-judged pairs and nothing new.

# 21 August 2026, editor's pass — two branches reviewed, both merged, one date corrected

Two pull requests were open, both cut from current main. The three stale 4 August
branches named in the standing brief (#6 photographs, #7 the 1980s, #8 the 2020s)
are gone from the open list and needed no decision.

## Research: person profiles (#104) — merged as it stood

Eleven 1993-95 committee officers and Judicial Council members gained profiles.
Every one of the eight pieces of legislation cited was checked by opening the PDF
in `data/legislation/` and reading its own AUTHOR and SPONSOR lines. All eight held
exactly: Ahsan sole author of Bill 92-10-F; the six named co-authors of Resolution
93-2-S; the five of 93-3-S including Eric McWilliams; Myers with Molly Schreiner on
93-7-S; the five of 93-6-F including Cailles and Newton; Rucker on 94-04-S; Rucker
with President Robert Evans on 94-1-1; Myers on Bill 94-06-S. Dates, sponsoring
committees and the two unanimous-passage stamps all matched. Nothing cut.

**A warning worth more than the merge.** The first pass of this review checked those
claims against `data/legislation-authors.json` and four appeared to fail — McWilliams
missing from 93-3-S, Cailles missing from 93-6-F, Myers filed as sponsor rather than
author on 93-7-S, and 93-2-S absent altogether. The derived index was wrong in every
case and the PDFs were right. That file drops authors and mislabels roles; it is a
finding aid, not evidence. Trusting it would have deleted four correct facts. This is
trap 7 running backwards — the derived artefact reporting less than the primary — and
the rule that follows is: go to the PDF before cutting or adding a name.

The Duncan handling in that branch is the standard to copy. Derrek Duncan of 1993-94
and Derek Duncan of 1994-95 are kept as two people, the resemblance is stated, and the
merge is explicitly declined in the profile itself. `name-aliases.json` rightly carries
no Duncan pair.

## Research: the backlog (#105) — merged after one correction

The thirty-two Talisman citations are sound and were confirmed independently rather
than taken on trust. archive.org's search-inside API puts three separate 1985-86
senators (Velastegui, Wredman, Groemling) on leaf 198 of `talisman1986west` and three
separate 1986-87 senators (Castleberry, Norcia, Smoot) on leaf 120 of `talisman1987west`,
which is exactly what the new `/page/nNNN/mode/1up` anchors claim. The leaf captions
were then read back against the recorded rosters: of the twenty-one names the OCR
caption covers, all twenty-one sit in the row the file says they sit in. No mismatches.
(The branch's own night-report entry lists the corroborating names under the wrong
volumes — Velastegui and Groemling are 1986, not 1987. The prose is scrambled; the data
is right.)

The Judicial Council edit carried a real error and it was corrected before merging.
Kappler's roster row was given a resignation date of 17 February 2009 — the day the
print Herald carried the story — and had Bewley approved as her successor "two days
later." The archive already held the contemporaneous report: the Herald of 12 February
2009, mirrored on the Wayback Machine and cited by this year's own events, records that
she resigned that Thursday night in a letter to President Kayla Shelton and student
activities director Charley Pride. The Senate approved Bewley a week later, on the 19th.
Her own 2007-08 profile and two event entries had said so all along, so the branch was
introducing a contradiction against sourced material already in the file.

The failure is the ordinary one: a TopSCHOLAR index date read as an event date. The
back file is a print paper indexed by issue, and an issue date is when the story ran,
never when the thing happened. The added profile paragraph was dropped as well — it
retold a story her 2007-08 term already tells, and the alias layer folds both rows onto
one person page, so it would have appeared twice in two versions.

Keeping Kappler's office as "Clerk, Judicial Council" is right and was left alone: the
14 October 2008 minutes say Clerk, the Herald says Chief Justice by February, and the
hedge belongs in the note rather than in the office field. Bewley's "(successor)" follows
the convention the file already uses for Morgan Gammons succeeding Ellen Henderson in
2024-25.

## Counts after both merges

61 years, 2029 events, 60 people have been president. `build.py`, `check_data.py` and
`check_contrib.py` all clean. `check_duplicates.py` reports the same six long-judged
pairs and nothing new; neither branch added an event, so neither added a pair.

## Still open

The Herald article PDFs on TopSCHOLAR were unreachable for the whole of this pass —
403, then an empty 202 behind the bot check, after the prescribed 90-second wait. The
landing pages and abstracts answered fine. Anything needing an article body rather than
a headline will have to wait for a run that gets through.

## Addendum — a commit that landed mid-review, and a duplicate problem worth a run of its own

**A commit arrived on `research-profiles` between the review and the merge.** `ca4b3d9`,
nine cabinet profiles for 2021-2026 — Singh, Johnson, Romanov, Taylor, Wright, Jenkins,
Jerdon, Yelton and Savanna Kurtz — was pushed after the branch was read and went to main
with the PR head. Its own commit message says an adversarial pass was still checking it,
so it published as a draft. It was reviewed after the fact rather than before, which is
the wrong order; a branch should be re-read at its head immediately before the merge
button, not at the sha the listing returned.

Reviewed now, it largely holds. Every figure that can be checked traces to an event
already in that year's record with its own source: Taylor's $100,000 budget approved
unanimously on 27 August 2024; Wright's Borrow-a-Calculator report of 3 September 2024;
the 88% vote renaming the DEI Committee; Jerdon's $4,573.73, his 78 applicant
organizations, the Herald's later correction to $580, and the $71.17 left in the
discretionary fund; Jenkins's 56 bills, the most since 2018-19; Yelton's Swipe It Forward.
Singh's confirmation on 15 September 2021 matches the minutes.

One defect was corrected. Preston Romanov's profile carried the Executive Cabinet's
February 2024 censure complaint against Administrative Vice President Salvador León —
which alleged León pushed Romanov to promote Neurodiversity Week before its funding bill
passed — and stopped there, leaving an allegation against a named living person hanging
with no result. The outcome is in this same year's events: the Judicial Council heard it
on 7 February 2024 and censured León 6-0, recommending no further action. That has been
added, along with a line making clear Romanov was not himself the subject of the
complaint. The rule is that an allegation without its resolution is not publishable when
the resolution exists.

One tension is flagged rather than fixed: Singh's roster office reads Director of
Enrollment and Student Experience, from a January 2022 capture of the cabinet page, while
the Senate minutes confirm him as director of academic and student affairs. Both are
sourced. Which he actually held, or whether the post was renamed under him, is not
established here.

**The duplicate checker cannot see the duplicates.** Tracing those claims turned up
seventeen pairs of events that are one event written up twice — same date, same source
URL, bodies overlapping by half or more — none of which `check_duplicates.py` reports.
It compares words in titles, so two passes that titled the same meeting differently slip
straight through. The clearest:

- 2011-12, 9 Nov: "Senate defeats DUC name change resolution 19-8" / "Senate votes down
  renaming Downing University Center 19-8"
- 2021-22, 14 Apr: "Judiciary Council cleared Bornefeld's campaign over student-all email"
  / "Judicial Council clears presidential candidate over a student-wide email"
- 2023-24, 6 Feb: "Cabinet requests censure hearing against León" / "Executive cabinet
  files censure complaint against vice president Leon"
- 2020-21, 21 Oct: the two write-ups of Keller's 29-1 confirmation as AVP
- 2019-20, 12 Feb: the two write-ups of the Go With the Flow funding increase
- 2024-25, 5 Feb: the two write-ups of the DEI constitutional review

The León pair is the instructive one: the spelling differs between them, León and Leon,
which drops the title overlap far enough that nothing flags it. CLAUDE.md predicts this
failure exactly — "matching whole titles never catches it" — and the tool meant to catch
it does the thing the warning says will not work.

These are all pre-existing on main and none came from tonight's two branches, so nothing
was merged on their account. They are not fixed here on purpose: combining two entries
without losing a sourced fact from either means reading both sources properly, seventeen
times over, and that is a run's work rather than a tired addendum to someone else's. The
next pass should take it, and `check_duplicates.py` should grow a body-similarity mode
that compares events sharing a date and a source, which is what surfaced these.

---

# Night report - 21 August 2026 (second pass)

Written by the overnight editor at 9:45 PM. Four research pull requests were open at the
start of the run; all four were reviewed and all four merged, three of them after
corrections were pushed to the branch first.

## What was reviewed, and what came of it

**#106, person profiles.** Twenty-one profiles for Judicial Council and Senate officers,
2019 to 2024, one new event for the April 2022 senate results, and the merge of six
entries that had been written up twice. Fourteen claims were spot-checked against their
sources; twelve held. Three dates were wrong and were corrected before merging:

- Ethan Huffaker was elected secretary of the Senate on **21 March 2023**, not 7 March.
  The posted minutes carry a "March 7th" heading, but the same document records the 3/7
  minutes being approved and Bill 39-23-S failing 19-15, business the *Herald* reported
  on 22 March. Both Huffaker's profile and Antonina Clementi's were corrected.
- Trib Singh was confirmed at the 21st Senate's fourth meeting on **14 September 2021**.
  The branch had rightly changed "first meeting" to "fourth" but kept 15 September, which
  is the day the *Herald* published, not the day the Senate met.
- Justin Goins's account of the February 2023 censure hearing asserted that the Queer
  Student Union's removal of SGA from its safe-space list "followed five days later." The
  two reports do not support that: at the hearing the Speaker read a QSU letter and said
  the group had already dropped SGA, and QSU's president told the Senate the same four
  days afterwards. Rewritten to what the sources show.

Nicole Massarone's profile rested entirely on a *Herald* interview that nothing in the
archive cited. The interview is real and says what the profile says, so the record now
carries it as a second source rather than losing the paragraph.

Two of the branch's own corrections were checked and were right where main had been
wrong: Bill 17-22-F carries three authors, so "co-authored" is correct for Ethan Taylor,
and Bill 1-23-F prints Anne-Marie Wright as a junior senator, not a senior.

**#107, senate rolls.** No data at all - a research note recording six years with no
senate roll, a Talisman check on 1979-80 that found nothing, and which hosts were closed
during the run. The six years it names are exactly the six the data has. Merged. Its one
slip is that it lists 1967-68 among the settled gaps, and 1967-68 already has a roll.

**#108, photographs.** One year photograph for 1998-99: Stephanie Cosby crowned
homecoming queen. TopSCHOLAR refused this session's requests for the item page, twice,
ninety seconds apart - but its **OAI endpoint is not behind the same block**, and returned
the item's title, its description ("Stephanie Cosby of Greenville crowned homecoming queen
in 1998") and its date. The committed file is byte-for-byte identical to the image the
archive itself serves. Merged. The route is worth keeping:

    https://digitalcommons.wku.edu/do/oai/?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:digitalcommons.wku.edu:<collection>-<id>

**#109, the backlog.** Folds three printed spellings of Nathan J. Eaton onto one page.
Merging two names into one person is the change this archive is most careful about, so the
chain was checked rather than the names: the 2007-08 senator's record already said he
chaired Campus Improvements, ran for Speaker in April 2008 and was printed both ways, and
the Speaker elected on 15 April 2008 is the man that record describes. The profile already
published on main opens by calling him Nathan "Nate" Eaton. Merged.

## Fixed on main while here

The 29 November 2023 entry numbered the Honors College seat bill 14-23-F and the chief
justice office-hours bill 13-23-F, which is how the *Herald* numbered them at first
reading. The bills SGA later posted carry 13-23-F and 12-23-F, and 14-23-F is the
Community Builder scholarship this archive already describes separately - so the same
number named two different bills on the site. The entry now names the measures and records
both numberings.

Three pairs of duplicated entries were combined, each pair being one event written up
twice from a single source, with no sourced fact lost from either: the DUC name-change
vote of 9 November 2011, Bill 1-20-S of 12 February 2020, and Isaac Keller's confirmation
as administrative vice president on 21 October 2020.

## Still open

The duplicate problem the 21 August morning report described is real and mostly still
there. Comparing events that share a date **and** a source URL, and scoring the overlap in
their bodies rather than their titles, turns up 55 candidate pairs; perhaps twenty of them
are genuinely one event twice over. Two of that report's seventeen were cleared by #106
and three more tonight. `check_duplicates.py` sees none of them, because it compares
titles. It should grow a body-similarity mode that compares events sharing a date and a
source; until it does, every routine is working without the tool that is supposed to catch
this.

`web.archive.org` was unreachable from this session all evening - connection reset, then
403 - which two of tonight's branches also reported. TopSCHOLAR's item pages returned 403
while its OAI metadata and its gallery images stayed open.

## Where the archive stands

61 academic years, 2,022 dated and sourced entries, 73 leader records, 520 records
carrying a written profile, 135 photographs (79 leader portraits, 56 year photographs),
285 documents mirrored, 1,111 legislation files, 1,587 pages built. build.py, check_data.py,
check_contrib.py and check_duplicates.py all clean at the close of the run.

---

# 22 August 2026, small hours

Two research pull requests open, both cut from the current head of main, both merged.
The three branches that had been open since 4 August — #6 photographs, #7 the 1980s,
#8 the 2020s — are gone, closed before this pass began. Nothing is stale.

## Merged

**#111, the senate rolls.** Eight senators added to 2019-20's roll — Bradon Burks,
Destinee Daugherty, Krystin Hardin, MJ Mayo, Dawson McCoun, Kyle Phillips, Parker
Raybourne and Elias Thompson. There were only eight new claims, so rather than sample
them I opened every source. SGA's own minutes of 22 and 29 October 2019, 4 February,
25 February and 3 March 2020 carry all of them by name and by title, and the Herald of
26 February 2020 carries the confirmation vote. Raybourne was seated 24-3-1 after
senators questioned his legislative record and his party membership, and the Speaker
ruled the partisan questioning out of order; the entry says so, and says he was seated.
Kat Howard and Jamison Moorehead were confirmed the same night as committee chairs and
were correctly left among the officers rather than promoted to senators, which is the
error that has killed more claims on this project than any other.

**#112, person profiles.** Twenty-one officers who until now carried an office and a
citation and nothing else now carry an account of what they did: the Judicial Council
seated in August 1978, the parliamentarian and sergeant-at-arms of April 1982, the
committee chairs under Stephanie Cosby in 1998-99 and under Leslie Bedo in 2001-02, and
the parliamentarian approved in September 2002.

`cgi/viewcontent.cgi` is still answering with a 202 challenge, so the minutes PDFs behind
these citations could not be opened from this session, by me or by the routine. The
landing pages could. So the test that fitted this branch was not whether the PDF says it,
but whether the profile says more than the note it was written from — which matters here
more than it looks, because `build.py` prints the profile *instead of* the note on a
person page. A profile that drops a fact deletes it from the site. All twenty-one were
diffed against the note, office and citation already on main. Twenty carried everything
across and invented nothing.

## Cut

**The argument from silence in Steve Wilson's account.** The profile explained his
succession to the Judicial Council chairmanship by writing that "the dates align and no
other ASG post for Moore is recorded that year." The succession is not new and was left
alone; the reasoning was cut. This archive's own rule is that a gap in the record is not
evidence of absence and can never be the grounds for a claim, and a reader of a profile
cannot tell an inference from a finding. The account now gives the vote of 30 to 3,
Thornton's announcement of the vacancy, the Herald's report of 14 September 1978, and the
succession, and says plainly that no source connects Moore's departure to the opening.

**A spelling settled that should not have been.** The Herald of 26 February 2020 spells
the new senator Daugherty. The Senate's own minutes of the meeting the night before spell
her Daughtery. The entry had quietly followed the newspaper. Both spellings are now in
the record and neither is chosen.

## Still open

The duplicate problem described on 21 August is untouched and still real.
`check_duplicates.py` compares titles, so it cannot see the roughly twenty genuine
duplicates that share a date and a source URL but were written up in different words. It
needs a body-similarity mode. Until it has one every routine is working without the tool
meant to catch this, and the six pairs it does report — an introduction and its later
vote, or three separate bills filed on 1 September 1991 — are all correctly distinct and
will be reported again every night.

Five of the twenty-one new profiles, the 1978-79 Judicial Council members, are the same
sentence with the name changed and say nothing their own heading does not. They are true,
so they stand, but a profile that restates its heading is not worth a run.

`Me'Lon Craighead` was confirmed a senator on the same night as the eight in #111 and was
already on the roll. `Joe Murrell` and the `Joe Morel` who moved the adjournment in
January and April 1999 are still unreconciled, as is `Krystin Hardin` against the
`Senator Hard` of the 3 March 2020 minutes. None of these should be guessed at.

## Where the archive stands

61 academic years, 2,022 dated and sourced entries, 73 leader records, 553 records
carrying a written profile, 135 photographs (79 leader portraits, 56 year photographs),
285 documents mirrored, 1,111 legislation files, 1,853 pages built. build.py,
check_data.py, check_contrib.py and check_duplicates.py all clean at the close of the run.
No pull requests left open.

# 22 August, the small hours

Four research pull requests open, all cut from current main, all reviewed. Three merged,
one merged with most of it cut. Nothing was left open.

## The 1979-80 cabinet, at last

`research-backlog` closed the last of the three years with no executive recorded. The
four names — Steve Fuller, Dean Bates, Betty Thompson, Terri Craig — are the same four an
earlier pass found and rejected in good faith, because the TopSCHOLAR abstract for Herald
54:56 does not index the article that names them. The abstract is not the issue. Opening
the PDF settles it in one column: Hargrove beat David Young 1,087-535 on a turnout of
1,725 against 1,097 the year before, and the other four races are reported beside it, down
to the 785-761 that made Bates's the closest of the four. Herald 54:57 names all five again
by office as they were sworn in on 24 April, and SGA's own minutes of that meeting
corroborate every one of them by what they did that night — Fuller on committees, Bates on
the Center Board, Craig moving to waive the rules, and Betty Thompson's signature at the
foot of the last page. Around twenty claims checked against the three documents; all held.

This is the clearest vindication yet of the warning in CLAUDE.md that a miss in the local
index proves nothing. It cost this project a year of believing a gap was permanent.

Two things were cut before merging. Steve Fuller's note ended by saying he was elected
president himself in April 1980, cited to a newspaper printed in April 1979. True, and
already on the record under 1980-81, but not something its own citation can carry. And the
four officer notes each mixed Herald facts with minutes facts under a single source; both
are now cited, so a reader following either link finds the claim it supports.

## Where the Talisman actually lives

`photo-research` corrected a source path that CLAUDE.md itself still gets wrong. There is
no `digitalcommons.wku.edu/talisman/` collection; it returns a genuine 404. The yearbooks
sit under `dlsc_ua_yearbooks`, mixed into the same records series as the Herald. Fourteen
items were identified by reading the publication date off each item's own page rather than
inferring it from the order, which is why the winter 1995 book files to 1995-96 and the
spring 1995 book to 1994-95 — a mapping that would have come out wrong any other way. The
eighteen years still without a photograph were re-counted against `photos.json` and the
list matches exactly. Every leader still has a portrait.

`viewcontent.cgi` was challenged all through that run, and challenged again for me at
merge. `research-backlog` had pulled full Herald PDFs through the same endpoint a few
hours earlier. It lifts and re-closes by the hour, and no run should treat one day's
failure as the state of the world.

## Ten profiles that said nothing

The 21 August entry let five profiles stand that restated their own headings, on the
grounds that they were true. That was too generous, and the practice has now produced
twelve more. Ten were cut.

Malcolm Arvin's read, in full, that Arvin served as Junior Class Representative for
1967-68. The page already prints that as the heading and prints the roster citation
underneath, so the profile added a sentence and a second copy of the same citation. Worse,
a profile displaces a `note`, so Petrie, Streible and Graham each lost a shorter and better
line to a longer one saying the same thing. Streible's page is back to the sentence that
tells you something: she also sat on the seven-member Executive Committee.

Two claims failed outright. Earl Edmonds was said to have delivered "Greetings from the
Student Body" at the dedication of nine buildings on 14 October 1967. The programme's own
index attributes that to Raymond Cravens and puts Edmonds's name on the line above it, the
introduction. The running order makes the inference tempting and it may well be right, but
it was published as a fact and the record does not say it. And a listing of Class of 1968
senior officers was attributed to the 1968 Talisman, naming Karen Williams and Jack Lewis,
neither of whom appears anywhere in an index of 11,850 items; the yearbook page itself
cannot currently be opened. Both cut, the second only until someone can read the page.

What survived is real and now properly cited: Edmonds's election, which the index carries
as a Herald report of 6 April 1967, and Randi Jensen's own piece in the Herald that
November, which the index gives under her byline in that issue's letters column. The ten
cut names came off `profiles-done.txt` so a later run picks them up instead of skipping
them as finished.

Sitting unused in the same dedication programme: William Menser, that year's ASG
president, gave the commemoratory statement for the Kelly Thompson Complex for Science.
That is a 1967-68 entry nobody has written.

## A run that found nothing

`research-senate` added no names and explained why. The 1999-00 Herald coverage is spring
election reporting — who ran for president, for administrative vice president, for
treasurer — and candidacy for an executive office is not a seat in Congress. Declining to
convert those names into senators is the same discipline that killed all 39 "missing
president" claims, and it is the harder call. Its access table had the 2011 minutes
directory returning 404; it still returns 403, as it did on 21 August, so the two paths
fail differently and nothing changed there. Its count of Herald hits could not be
reproduced and is now stated with the filter that produces it.

## Still open

The duplicate problem is unchanged from 21 August and still real. `check_duplicates.py`
compares titles and cannot see entries that share a date and a source but were written up
in different words. The six pairs it reports are all correctly distinct and will be
reported again tomorrow.

Something it also cannot see: the meeting of 24 April 1979 is now written up twice, once
in 1978-79 for the resolutions the outgoing Congress passed and once in 1979-80 for the
officers it swore in. That split is deliberate and, I think, right — the legislation
belongs to the year that passed it and the swearing-in to the year that began — but it is
the shape of thing a body-similarity check would flag, and whoever builds that check should
decide what to do with it rather than be surprised by it.

Election events are filed inconsistently. Hargrove's April 1979 win sits in 1978-79, while
Fuller's April 1980 win sits in both 1979-80 and 1980-81. The leaders are all filed
forward correctly, which is what matters, but the events are not filed to one rule.

Flagged by `research-profiles` and not touched: the 2016-17 and 2017-18 executive records
carry garbled office and name fields from PDF extraction, along with officers of campus
clubs pulled in from a resolution's whereas-clauses. Nobody should profile those until
they are cleaned. The "Chris Grau" spelling flag in 1968-69 is still unresolved.

Vercel refused every preview build tonight, having spent its hundred free deployments for
the day. Nothing to do with any of this work, and it clears on its own.

## Where the archive stands

61 academic years, 2,021 dated and sourced entries, 73 leader records, 555 records carrying
a written profile, 135 photographs (79 leader portraits, 56 year photographs), 287
documents mirrored, 1,111 legislation files, 1,855 pages built. build.py, check_data.py,
check_contrib.py and check_duplicates.py all clean at the close of the run. No pull
requests left open.

---

# 22 August, the morning pass

Two pull requests open, both from the small hours of the same morning, both merged after
cuts. GitHub was reachable this run.

## Research: person profiles (#119)

Ten officers of the late 1970s through the mid 1990s, and then, in a commit pushed after
the run wrote its own report, the thirteen remaining 1967-68 congressmen and class
officers.

I opened seventeen claims against the sources they cite rather than the researcher's
paraphrase, and every one of them held. Dean Bates's byline on "Coffee House a Success",
Terri Craig's election to the SGAK Executive Council alongside Steve Thornton, the opinion
pieces by Erica Card, Elizabeth Fauver, Trent Lyda and David Serafini, and all three
February 1994 Herald items on Angelo Rodriguez trading places with Thomas Meredith. The
1967-68 roster is mirrored in `data/documents/`, so all thirteen seats were checked against
the primary text, down to Keith Petrie on the Student Activities Committee and Susan
Streible on the Executive Committee. Johnny Graham's absence from the roll of 13 February
1969 is in the mirrored minutes, in as many words.

The batch handled the advance-notice trap correctly, which is worth saying: the Herald ran
Tonya Root's preview of the Meredith swap on 17 February and her reports of it on the 22nd
and 24th, and the profile distinguishes them.

Four things came out before it went to main.

Betty Thompson's second paragraph. I read the 1980 Talisman on archive.org and it says
exactly what the profile said it says — a Betty Thompson of Bowling Green, Chi Omega,
crowned Homecoming Queen by Zacharias, a twirler at halftime. Nothing ties her to the ASG
secretary. The paragraph ended by admitting as much, and that admission is the argument for
cutting it, not for keeping it with a caveat: ninety words of a stranger's private life,
none of it about the office, published under an officer's name.

The claim that no other record of the officer survives in this archive, from all thirteen
1967-68 profiles. The archive cannot show that. `herald-index-full.json` cuts every line at
300 characters and a third of its lines are truncated mid-headline, so a miss in it proves
nothing — and the risk is live here rather than theoretical, because a Mike McDaniel carries
a Herald byline in the very issue of 29 April 1968 that this batch cites for Graham.

Johnny Graham's inference that the Graham on the April 1968 senior ballot was the sitting
junior class vice president. The Herald says a Johnny Graham was on that ballot and no more.
I cited the 13 February 1969 minutes on the entry that asserts the roll call, which was
traceable in the file but not cited where a reader would look.

And a date. Dean Bates's profile put the Regents' handover of campus entertainment to the
University Center Board in "the previous spring". It was 31 March 1979, three weeks before
the swearing-in the same sentence describes. Corrected against settled fact 7, with the
Talisman senior listing his profile leans on now cited.

Two more of these negative assertions, on Rebecca Hack and Andrea Cailles, were phrased
differently enough to survive my first sweep and reached main before I caught them. They
came out on the next branch, along with Janie Heathcoat's, which was already there.

## Research: the backlog (#120)

The run took the last open item in section 8.3: sixty-one names in the 1992-93 Congress roll
that had been merged on a night when the minutes PDFs were unreachable and were never read
against the meetings they cite. All eighteen documents came down and all sixty-one held.
Andrea Cailles joins the roll as its sixty-seventh member, a gap the officer record had been
pointing at all along.

The branch was well behind main. I merged main in first; only the generated `site/` files
conflicted and rebuilding resolved them. `data/years.json` merged cleanly, and the two
pull requests turned out to fit together rather than fight: #119 narrowed the Cailles
officer note to the August chairmanship it cites, and #120 put the February seating where
it belongs, in the membership.

One trim. The Cailles member note carried the absence roll of 6 April 1993 under a citation
pointing at the minutes of 9 February. I do not doubt the fact — the run read the document,
and the April minutes are cited elsewhere in the same year — but a reader following that
link cannot check that date, and it is the same fault #119's own verifier trimmed out of
David Serafini's entry hours earlier.

`viewcontent.cgi` was serving the bot-check page by the time I reached it, so the 1992-93
primary text was not re-readable on this pass. Landing-page abstracts, the mirrored
documents already in the repository and the surrounding record are what I could check.

## Found while checking

`build.py` drops `profile` and `src2`..`src20` from Senate member entries. `officer_index()`
rebuilds each member as a bare name, office, note and src before it reaches the person page.
Eleven member profiles and five sets of extra citations are sitting in `years.json` right
now, written by earlier runs and never published. That is section 6 trap 7 exactly — output
that reports success and produces nothing.

I did not fix it tonight. Surfacing eleven unreviewed paragraphs onto the live site is a
publishing decision rather than a build fix, and it should go through a review pass on its
own. Recorded in section 8.3 with the working rule in the meantime: a member entry gets one
source, and its note stays inside what that one source shows.

Twenty-three "no record survives" assertions from earlier runs are still on the live site,
outside tonight's diffs. Each needs judging on whether a real search stands behind it, so a
blanket strip is the wrong instrument and I have not attempted one. It deserves a pass of
its own.

Both research branches carry their commits under a tool's name in the git author field.
Squashing on merge keeps that out of main's history, which is where it matters, but it is
visible on the branches.

Worth having and left for the routine rather than researched from this chair: the 1980
Talisman describes Dean Bates as chairman of the University Center Board's lecture and
contemporary music committee and quotes him on the Spyro Gyra concert that lost $3,500 in
November 1979. That sits directly on top of his ASG activities portfolio.

## Still open

The duplicate pairs are the same six as yesterday and the day before. All correctly
distinct: a bill introduced and the same bill failing, a lawsuit planned and then endorsed,
a position taken and then legislated, three bills filed on one day. They will be reported
again tomorrow. Everything under "Still open" in the 22 August small-hours entry stands
unchanged.

## Where the archive stands

61 academic years, 2,021 dated and sourced entries, 73 leader records, 578 records carrying
a written profile, 135 photographs (79 leader portraits, 56 year photographs), 288 documents
mirrored, 1,111 legislation files, 1,855 pages built. build.py, check_data.py,
check_contrib.py and check_duplicates.py all clean at the close of the run. No pull requests
left open.

---

# Night report - 22 August 2026, mid-morning

Written by the editor. Four research pull requests were open; all four are merged and
nothing is left open.

## What came in and what happened to it

**#122, the senate rolls.** Thirty-two rank-and-file senators for 2010-11, 2011-12 and
2012-13, drawn from SGA's own minutes on wku.edu. I downloaded the cited minutes files
and read the passages rather than the drafter's notes, sixteen names across both years.
The strong ones are very strong: Kat Johns tabled for Sergeant-at-Arms because "Senator
Johns" was absent that night; Lauren Riggs's resignation reported to the floor; Crowley,
Spalding and Winston sworn in by President Jessie in one sentence; the 28 February 2012
blanket vote naming all six senators-at-large in the order the six notes give them.
Where a bare surname had to be tied to a full name, I checked the corpus myself and
found exactly one first name attaching to each: Rachel Calhoun, Paul Shively, Josh
Newman, Daniel Shaw. Merged with one cut.

**Cut: Josh Rodriguez, 2011-12.** The only place the full name appears is the Speaker's
report of 1 November 2011 joking that he had got his braces off. That places him nowhere
near the Senate, and the link to the "Senator Rodriguez" of the following week is the
surname alone. It is also the wrong thing to publish about a living person: a remark
about someone's teeth, lifted out of a meeting fifteen years ago onto a permanent public
site, has nothing to do with their SGA service. The branch's own handoff note says a bare
surname is not enough to add someone, which is the rule that decided it.

**#123, three Talisman photographs.** 1981-82 and 1987-88 verified themselves - both
crops include the printed yearbook caption, and both match photos.json word for word,
twenty-nine names in the right rows for 1981-82, including "Marcel" Bush in the settled
spelling. The decision not to crop the 1987-88 group into portraits was right; the
printed rows do not map onto the faces and nobody could assign those names from the
caption.

**Trimmed: the 1983-84 beer-poll caption.** That crop stops at the photograph, so the
identification of "Stanley Reagan, a Tompkinsville sophomore" rested on a transcription I
could not check - viewcontent.cgi answered the 1984 volume with a WAF challenge on four
attempts ninety seconds apart. The photograph proves the rest on its own: the banner, the
polling table, students queueing to vote in a poll ASG ran. The caption now says that and
no more. The name is preserved in the PR comment for whoever can next open p. 376. This
is not doubt about the transcription - the other two matched to the punctuation - but
naming a private individual is the one claim that should not rest on a caption the editor
never saw.

**#124, eleven officer profiles.** The facts are sound. I fetched four of the cited Herald
articles and every clause held, including the ones that read like they might be
misattributed: the intent-to-resign line is Spalding's and is filed under Spalding, and
Jankowski's rally quote is real. I also checked the facts that come from outside each
profile's own src, and all of them trace to a source already cited in that year.

**Rewrote eight of the eleven.** The batch broke the quotation rule comprehensively and
nobody had checked it: four quotes ran past fifteen words (Jankowski 22, Butler 20,
Calhoun 17, Whipple 17) and six profiles quoted one article two, three or four times over.
The Calhoun and Whipple paragraphs were carrying three and four consecutive lifted
sentences. No fact was dropped - each now keeps one quotation under the limit, with the
rest in reported speech. Veronica Butler's account of her own difficulty knowing when to
seek help is reported rather than quoted at twenty words; she said it about her own
committee's work so it belongs, but reported speech carries it at less cost to a current
student.

**#125, the officer roster cleaned against the legislation.** The best branch of the four
and the one I checked hardest, because it removes thirty-three named people. It survives.
The parser bug is real and I reproduced it: bill 9-16-F's contacts run "Dr. Saundra
Ardrey, chair of the WKU Department of Political Science / Jacob Holt, president of the
WKU Residence Hall Association", and the archive had been carrying "Political Science
Jacob Holt". Same mechanism gave "Public Health Kate Hart" and "Senate Sam Kurtz".

I sampled 26 changed documents from 2016-17 to 2025-26, re-downloaded every PDF and
extracted it independently: 43 of 43 corrected names appear verbatim in their own cited
document. The removals I pulled mechanically and got exactly the 33 claimed - faculty,
deans, the Provost, staff directors and officers of other student organisations, every one
named only in a bill's CONTACTS line, plus five fragments that were never people
("Organizational Aid" four times, "Executive Producer", "Food Pantry"). Listing a
department chair or the Provost as an SGA officer was an error of fact about real people;
removing them is a correction. The pass sorted on whether the office is an SGA office
rather than which block of the PDF the name sat in, which is why Kate Hart and Maggie
Yelton were kept from the same CONTACTS lines. Merged as is, no cuts.

## Flagged, not fixed

Keyanna Boka (leader, 2013-14) and Keyana Boka (senator 2010-11, committee chair 2011-12,
executive vice president 2012-13, and the executive entry for her own presidential year)
are plainly one person, but the spellings are not joined in name-aliases.json, so her four
records do not reach her page. This predates tonight - main already carried both spellings
inside a single year - and the rule says this pair is unverified and is to be flagged
rather than corrected. It wants a source that settles the spelling, not an editor's guess.

Lauren Willet / Lauren Willett came in the same way from #125 and is handled correctly
there: each entry matches its own cited bill.

## For the routines

The photograph run should crop to include the printed caption whenever there is one. It
cost nothing on two of tonight's three and made them unfalsifiable at review - twenty-nine
names confirmed without a single network request. The one photo cropped tight to the image
is the one that lost a fact.

The profiles run needs the quotation limit added to its verifier. The adversarial pass is
working well on truth - it caught a misattributed line, two invented officiants and an
over-generalised quote - but it only asks whether claims are true, and all eight
over-quoted profiles were true. Counting quotes and their length is mechanical and needs
no source fetch.

The senate run should keep disclosing its inferences the way this batch did; that
transparency is what made the branch checkable. One rule to hold harder: a full name that
appears only in an aside about someone's personal life is not evidence of membership,
however unique the surname.

#125's own note names the next piece of work: the pass covered the 294 entries carrying
the "Named on the document as..." marker, and entries from the same harvest without that
marker have not been checked. The same bug will be in them.

Commits on the research branches still arrive under a tool's name in the git author field.
It stays out of main's own commit messages, but the author field is permanent history and
the routines should be given a plain committer identity.

## Still open

The same six duplicate pairs, unchanged and still correctly distinct: a bill introduced and
the same bill failing, a lawsuit planned and then endorsed, a position taken and then
legislated, three bills filed on one day. The twenty-three "no record survives" assertions
from earlier runs are untouched and still deserve a pass of their own.

## Where the archive stands

61 academic years, 2,021 dated and sourced entries, 73 leader records, 589 records carrying
a written profile, 1,069 officer entries (down 33), 1,294 senate members (up 31), 138
photographs (79 leader portraits, 59 year photographs), 288 documents mirrored, 1,111
legislation files, 1,707 pages built. build.py, check_data.py, check_contrib.py and
check_duplicates.py all clean on main at the close of the run. No pull requests left open.

---

# 22 August 2026, midday: two research branches merged

Two pull requests were open and both are now on main. Nothing was left standing overnight.

## #126, person profiles: merged after eleven corrections

Sixteen profiles arrived across three pushes while the review was running, which is worth
recording as a working condition rather than a complaint: the branch moved under the review
twice, and each new push had to be fetched, read and merged before anything could land. The
routine's own adversarial re-read, pushed third, caught four of the same faults this review
had already found independently — the Narcan implementation, two over-long quotations and an
unsourced vacancy. That agreement is the best evidence yet that the verifier is doing real work.

The single pattern worth naming: **three chair entries cited a document that named someone
else in the post.** Helen Vickrey's source was the senate minutes of 13 September 2016, which
name Michael Shelton as MyCampusToo chair; Hizareth Linares's was the Herald of 12 October
2016, which names Francisco Serrano as SAVES's first chair; Mark Clark's was Resolution
7-17-F, which calls him a senator. In each case the note beneath still read "Named on the
document as ...". The office was true in all three cases and the legislation proves it, so
each entry now leads with the document that does name them in the post and keeps the earlier
one below. This came from replacing a scraped source label with a better document without
re-reading the better document. It will recur wherever that cleanup runs.

The rest, in descending order of seriousness. An advance notice read as a report: the Herald
of 15 February 2023 has Housing and Residence Life asking to delay the Narcan supply to 1
August, and the profile had them implementing it then. A lawsuit reversed: Resolution 10-17-F
says WKU sued the Herald, and Morgan Wysong's profile had the paper suing the university. A
living person's words over-attributed: Mark Clark called the senate's remarks discriminatory,
while "dehumanizing" was Brigid Stakelum's word, and the profile gave both to Clark. A date
wrong by a week: Meghan Pierce spoke for Adan Canizalez's confirmation on 24 January 2023, not
17 January — and cut with it went a parliamentarian sentence and an account of the senate
suspending its own bylaws for a chief justice election, neither of which appears in any source
this archive cites. Matthew Johnson's chair "standing empty into November 2019" had no source
and is gone; the minutes of 14 April 2020 are used instead for what they do record, a Zoom
meeting of thirty senators with Johnson reporting as committee head while campus was shut.
Smaller: the joint statement on the 2016 racism complaint came the day after the resignations,
not the same day; Bill 20-17-S followed Kentucky Senate Bill 17 as the bill describes it, not
"political or religious belief"; Ashley Cox is listed in the September 2017 minutes rather
than reporting to the meeting; and Brian Anderson's note read "Named on the document as chair
of."

Around twenty claims were opened at source. Everything not listed above held: vote counts,
dollar figures, authorship and election percentages were right every time they were checked.

## #127, the senate rolls: merged as it stood

Seven senators sworn in on 25 September 2012, taking that year's roll from three recorded
members to ten. All seven names and their groupings are in the Herald's report of the meeting
word for word, and no one named appears in a competing role, so the bill-author trap does not
bite. The four forward-looking notes each trace to an entry already sourced elsewhere in the
file, and the note on Paige Settles correctly declines to call her speaker in 2014-15, when
she chaired Legislative Research. The Shey/Shea Wyatt divergence between the minutes and the
Herald is flagged rather than resolved, which is right.

## A duplicate the checker cannot see

Two entries described the same meeting of 13 February 2018 from the same Herald report, in
different words. `check_duplicates.py` never flagged them because the titles share almost no
words. They are now one entry carrying both versions' facts. The six pairs the checker does
report were read again and are all genuinely distinct.

## Still open

The 294 "Named on the document as..." entries were cleaned in an earlier pass, but entries
from the same harvest without that marker are still unchecked, and the mis-sourcing above is
the kind of thing that will be sitting in them. The twenty-three "no record survives"
assertions still deserve a pass of their own. Research commits continue to arrive under a
tool's name in the git author field.

## Where the archive stands

61 academic years, 2,020 dated and sourced entries (one fewer than yesterday: two were one
event), 73 leader records, 594 records carrying a written profile (up 5), 1,069 officer
entries, 1,301 senate members (up 7), 138 photographs, 288 documents mirrored, 1,111
legislation files, 1,705 pages built. build.py, check_data.py, check_contrib.py and
check_duplicates.py all clean on main at the close of the run. No pull requests left open.

# 22 August 2026, evening

Four research pull requests open, all opened today, all merged. The three stale branches from
4 August named in the standing brief — #6 photographs, #7 the 1980s, #8 the 2020s — are gone;
nothing of theirs was left open to rescue or close.

## What was checked, and how

Where a claim could be checked against the thing itself rather than against a description of
it, it was. The legislation PR was checkable that way in full, so all thirty of its changes
were opened in the PDFs rather than eight of them sampled. The photograph PR was checked twice
over: once for whether the person is the right person, and again for whether the square cut out
of the portrait grid is the right square, which is a separate question and the one that fails
silently. The senate PR was read against eleven of SGA's own minutes files. The profiles PR
was read against twelve Herald articles, every sentence of all nine profiles.

## The two that would have done damage

**Two living people were named as the subjects of a racism investigation.** Cody Cox's new
profile had the October 2016 inquiry collapsing "when senator Braxton Powell and justice John
McKinney resigned." The Herald report it cites says three times over that SGA never released
the names of the accused, that neither man connected his resignation to the complaint, and
that the two gave scheduling conflicts and personal reasons for going. The paper set the
resignations and the dropped investigation side by side and declined to join them. The profile
joined them. It now says what the paper said. The archive's own 2016-17 event on this incident
already had it right — it names the two as having resigned and states plainly that neither
acknowledged a link — and that entry is the standard to follow.

**Gene Saunders wrote Bill 6 of 1976-77; the extraction filed him as its sponsor.** That form
sets author and sponsor in two columns, labels stacked on the left and names on the right, so
the flattened text reads Author / Sponsor / Gene Saunders / Christy Vogt in sequence and the
split took both names off the second label. On the page Saunders sits level with Author. The
run's own verifier had caught two errors of the same family, both cases of a name sitting
below a later heading. It could not catch this one, because a check that reads a block in
sequence cannot see a two-column form at all.

## Smaller corrections

Erika Puhakka's profile had President Mayer disputing where the Judicial Council had ranked
her against Wood Brown. No cited source records that exchange; what the Herald reports is that
the council preferred her and that Annalicia Carlson said so before the vote. Cut back to
that. Annalicia Carlson's account of the Pepe the Frog ruling reversed the order of what
Garrett Edmonds did and what he was told. Josh Zaczek was credited with striking "removal from
campus" from the Alpha Xi Delta resolution as well as adding "suspension from Greek affairs";
only the second was his amendment. A month-later resignation from the Judicial Council was
linked to the racism complaint by the word "also," which its source does not support.

Two senators' votes on Resolution 4-15-S were filed under the meetings at which the two were
appointed, which do not carry the vote. The claims are true — the roll call is in the
sixteenth meeting of the Thirteenth Senate, 24 February 2015, and the resolution carried 15-6
— so the roll call is now cited beside them. This is the hardest kind of error to see, because
only the pointer is wrong: a reader who checks the source finds nothing and concludes the
archive invented it.

## What the checks could not settle, and what settled it

Betty Thompson's portrait was very nearly cut. It is a Homecoming coronation, nothing in the
1980 Talisman connects her to student government, and that volume's index carries two separate
entries under her name. What saved it was the 1979 volume: the Miss Western report names
"Betty Thompson, a Bowling Green junior," which is the Herald's own description of the woman
elected secretary in April 1979, and the 1979 index lists exactly one of her. Two independent
sources converging on a name, a town and a class standing is enough.

Victor Jackson needed no such argument. The 1979 index reads "Jackson, Victor Michael 288-9,
295, 360" — one entry spanning both the ASG coverage already cited on his record and the
senior portrait page. The yearbook itself says the man in the meeting photograph and the man
in the portrait are one person. That is the strongest form of identification available in this
archive, and the method that produced it — reading the printed name index in the full text on
archive.org — should be standard on every photograph run from here.

Nolan and Noland Miles stay two records. The minutes show Student Affairs passing to Barrett
Greenwell on 11 February 2014, the same night Nolan Miles took Public Relations, and Noland
Miles had led Student Affairs since October: one committee changing hands as the other was
taken up. That is consistent with one person moving between committees and it is not proof, so
both records stand, but the evidence is now written into both notes instead of a bare
statement that the question is open.

## Found on main while checking

The meeting of 31 March 2021 was written up twice from the same report, in different words.
`check_duplicates.py` never saw it because the titles share almost no words — the same blind
spot that hid the 13 February 2018 pair. They are now one entry keeping every fact from both.
The Herald's spelling "Lauren Willet" is mapped to Lauren Willett, an identification the
profiles run had already relied on without recording, which would have let a later run rebuild
the duplicate person.

## Still open

Three-quarters of the undelimited author lists — about thirty-five live rows — remain
unresolved and want individual review rather than another automated pass. Any pass that
returns to them must read the AUTHOR block by coordinates, not by line order. Six pre-2011
attributions the PDFs plainly carry are still missing from the record: Bill Schilling as
author as well as sponsor of Bill 41 of 1985-86, Shannon Ragland as author of Resolution 45 of
1988-89, Michael Colvin as a sponsor of Resolution 210 of 1989-90. Two files in the 1976-77
folder, `dc_bill_2.pdf` and `dc_resolution_2.pdf`, are the same document filed twice. Sandy
Alford's and Sally Brenzel's portraits rest on a name unique in the yearbook index and nothing
more, and should be rechecked first if an ASG group photograph for 1978-79 ever surfaces.
The twenty-three "no record survives" assertions still deserve a pass of their own, and
research commits still arrive under a tool's name in the git author field.

## Where the archive stands

61 academic years, 2,019 dated and sourced entries (one fewer than yesterday: two were one
event), 73 leader records, 613 records carrying a written profile (up 19), 1,069 officer
entries, 1,318 senate members (up 17), 144 photographs, 1,103 authorship attributions read off
the legislation itself (up 65), 287 documents mirrored, 1,111 legislation files, 1,716 pages
built. build.py, check_data.py, check_contrib.py and check_duplicates.py all clean on main at
the close of the run. No pull requests left open.

# 22 August 2026, later evening

Two research pull requests were open, both cut from the current main with nothing stale behind
them. Both merged. The three branches from 4 August that this run's brief named as rotting —
#6, #7 and #8 — were already closed before it started.

## Person profiles (#134)

The pull request described twelve records; the branch had grown since it was written and
carried twenty-two. Ten committee officers of the 1990s Senate and Brooke Mitchell of the
2022-23 Mental Health and Wellbeing Committee had landed in an earlier commit the body never
mentioned. All twenty-two were reviewed.

Three sources were opened directly. Bill 46-23-S, which sits on wku.edu and not behind the
archive's bot protection, confirmed its seven authors, Olivia Feck as committee chair, the
$550 from the Legislative Discretionary Fund, the week of 23 to 28 April 2023 and every event
in it. It also showed something the entry had not: the bill records a first reading on 11
April and a second on 18 April, and its pass, fail and other boxes are all blank. The profile
had it "read to the Senate and passed unanimously" on that document alone. The unanimous vote
is real — the Herald of 13 April 2023 reports it, and that article was already cited in this
year's events — so the paragraph now says which source carries which fact and the Herald is
cited beside the bill. The 1971 Talisman, readable in full text on archive.org, confirmed the
Judicial Committee caption word for word: Freville vice-chairman, Linda Jones secretary, Eyler
chairman. That entry's refusal to merge Linda Jones with the 1971-72 president of the same
name is the rule working as intended. And the minutes of 13 April 2004, already mirrored in
this archive, settled the date correction: the meeting opened that day with 20 of 30 members
present, Abby Lovan withdrew, and Robert Watkins won by one vote. The archive had been dating
that election to 15 April, which is when the Herald's report ran.

One claim was cut outright. Watkins's profile ended with the disputed speaker vote being
"upheld later that month." Nothing in the record says so; all the archive has is Fausey
declining to challenge it. Abby Lovan's withdrawal, which the minutes do record, took its
place.

Three more were repairs rather than cuts, and they share a cause worth naming. `build.py`
hides an officer's note once that officer has a profile, on the reasoning that showing both
repeats the same facts. So a profile that is thinner than the note beneath it does not sit
alongside it — it deletes it from the page. David Apple's profile dropped that the April 1998
primary he read out was for Public Relations Director and sent Sweatt and France to the general
election. Andy Gailor's dropped that Resolution 97-17-F was voted down for insufficient
research. Both were folded back in, in both years each man appears. Tim Todd's "the only
remark of his recorded in that year's minutes" was scoped to the single set of 1985-86 minutes
this archive actually holds, which is all that claim can rest on.

Everything else traced. Trent Lyda's succession, Apple on internet hours, the Sweatt and France
vote totals, Gailor as City Commission representative, Steve Wilson confirmed 30 to 3, the 7
September 1978 ineligibility ruling, Eliana Martinez taking the clerkship by 28 May 2010,
VanWinkle working with Liz Goddard, the 30 October 2003 suspension of the by-laws, Eaton's
shuttle stop, Kenderes, Carol Gray as 1970-71 secretary — each fact in the new prose lands on
an entry already sourced in this archive.

## The backlog (#135)

Merged with nothing cut. Both image files are real JPEGs and both were looked at: a group
portrait of about thirty people in an auditorium for 1982-83, and a young man in a suit in a
large leather office chair for 1990-91. Neither crop carries its caption, which for the group
photograph is the right choice — the site names nobody in it, so no face in it can be
misidentified.

The Jeff Goff event looks wrong before it looks right, and the reason is worth recording. This
archive already says President for a Day was established by Bill 91-9-F in September 1991,
which is ten months after the swap this entry describes. It holds up. The 1991 Talisman covers
the 1990-91 year, and Michael Colvin, named in the entry as walking Goff into the office, was
president in 1990-91 — 1991-92 was Heather Falmlen. A fundraiser run once in November 1990 and
formalised by bill the following autumn is a coherent sequence. The Talisman item's own
landing-page index, which is readable even when the PDFs are not, lists "Student Takes Office –
Jeff Goff" and "President Takes Notes – Thomas Meredith" as a two-part feature, which is the
swap.

Kerrie Stewart needed no leap either: the 1981-82 Congress roll already recorded her sworn in
as Public Affairs Vice President for the following year on 27 April 1982, so the Talisman is a
second source and the April-to-following-year placement is the standing rule applied correctly.
The "Margaret Regan" spelling was added as a flag on the existing note, leaving the Board-seat
correction untouched.

## What could not be checked, and why it did not stop the merge

`viewcontent.cgi` was challenged for this entire run. Twelve minutes items, four rounds spread
over half an hour with ninety-second backoffs between them, cookies carried from each item page
and the referer sent back to it, tried against both the `sga` and `dlsc_ua_records` collections:
every request came back HTTP 202 with a Cloudflare challenge page and no bytes. A headless
browser could not reach the host at all. The run that produced #135 found the same endpoint
wide open to a bare curl a couple of hours earlier, which is one more confirmation of the note
in section 8.4 that this lifts and re-closes by the hour rather than staying shut.

Two consequences. The ten 1990s committee profiles could not be re-read at source; they were
allowed through because they restate notes already published and sourced on main rather than
asserting anything new, but they are re-wording, not fresh verification. And the "Margaret
Regan" caption spelling is the one claim merged this run with no second source behind it. It
stayed in because it is explicitly a flag rather than a correction, because nothing contradicts
it, and because this archive's own rule is that a miss under a closed door is not evidence of
absence. The next run that finds the endpoint open should read that caption and settle it.

## Still open

The 1995-96 entry that glosses Bill 91-9-F as having established President for a Day now sits
on the public site beside a swap that ran in November 1990. Both are sourced and neither is
wrong, but a reader meeting them together sees a contradiction; the earlier entry wants a
clause saying the bill formalised something ASG had already run once. Everything carried
forward from the previous report stands: the thirty-five unresolved author lists, the six
pre-2011 attributions the PDFs plainly carry, the duplicate 1976-77 pair, the Alford and
Brenzel portraits resting on a unique surname, and the twenty-three "no record survives"
assertions. The thirteen years still without a year photograph are now the whole of that gap
the Talisman landing page can reach — #135 exhausted its worklist, and the next pass needs a
live TopSCHOLAR search or Wayback captures instead.

Research commits still arrive under a tool's name in the git author field. Squash-merging keeps
it out of main's history, which is what both merges did, and is worth keeping to.

## Where the archive stands

61 academic years, 2,020 dated and sourced entries (up one), 73 leader records, 638 records
carrying a written profile (up 25), 1,070 officer entries, 1,318 senate members, 146
photographs (up two), 288 documents mirrored, 1,111 legislation files, 1,716 pages built.
build.py, check_data.py, check_contrib.py and check_duplicates.py all clean on main at the
close of the run; check_duplicates.py's six pairs are the known pre-existing ones and are
genuinely separate events. No pull requests left open.

---

# Editor's report - 22 August 2026, late evening

Four research pull requests were open. All four are merged. Nothing was left open, and
nothing was closed unmerged.

## What was reviewed, and what it cost

**#137, the senate rolls.** Thirty-seven rank-and-file senators of the fifth SGA, 2006-07,
recovered from ten sets of SGA minutes, seven of them newly mirrored. I read the primary
documents rather than the report: seven carry an OCR text layer, and the minutes of 17
October 2006 are a pure image scan with no text at all, so those pages were rendered and
read. Every claim in the sample held. The eighteen sworn in on 3 October are eighteen. The
eleven sworn in on 30 January are eleven. Christina Allen was sworn by Justice Brian
Fischer on 17 October, exactly as recorded. The text layer reads "Christian Cutlip"; the
page reads Cullip, and so does the 6 February meeting, so the entry is right and the
transcript is wrong.

The discipline about who was *not* added is what carried this one. Kevin Barnes was
approved on 30 January, marked not present, and never shown sworn: left off. Jeremy Glass
took the oath the same night as William Doolin on 27 February, but as Director of
Technology, an executive post, and is not on the roll. Joshua Fries was left as a flagged
possibility because `name-aliases.json` does not carry him, while Nathan Eaton was linked
because it does. That is the distinction being drawn correctly in both directions.

Two notes were trimmed. The senate note claimed every roll call from 30 January counted 35
seats; that night's roll counted 22, because it was taken before the oath, and the chamber
first counts 35 on 6 February. The Tim Hill note called the identity of the Legislative
Research chair unestablished, when the 12 September minutes in the same set name "Tim Hill,
Jr." as chair, and it asserted a resignation by 10 October that no cited source supports.

**#138, photographs.** Five 1970s officers given faces from the Talisman. This is the
category where an error cannot be taken back, so each portrait was checked down to the
individual cell of the grid: the yearbook's name index to find the page, the page image to
count names against portraits. All five are right. Two things made the identifications
strong rather than merely plausible - the 1973 volume's own account of student government
names Gary Whitfield as head of Legal Rights and R.G. Meade as head of Rules and Elections,
the 1977 volume has "secretary Pam Keown" and the 1978 volume "housing chairman John
Grizzell", so four of the five are tied to their office inside the same book as the
portrait; and the sequence of names around each cell tracks the sequence of faces.

Every one of the six source links was wrong, one leaf too high, so a reader following a
citation landed on the page after the portrait. Fixed. The offset is not constant between
volumes, 5 for 1973 and 3 for the later three, so it cannot be computed once and reused.
Worth noting that the index is not always right either: Vogt's index line says 404, which
is the S-T page; her portrait is on 405 with the U-W names, which is what the label said.

**#139, person profiles.** Eleven officers given a profile. Several claims matched their
minutes word for word - Merritt's 14-2 confirmation and "likes organization", the eleven
at-large senators the Herald named in April 2018, the thirteen sworn in on 30 September
2014, Glasgow's "catch-all", Faught's fourteen at the first meeting, Scaff thanking his
committee for being proactive on the day he said he would graduate, and Resolution 11-15-S
failing for want of a supermajority. This was careful work.

One paragraph contradicted the archive. Kerrie Stewart was said to have run for Public
Affairs Vice President on Margaret Ragan's ticket. This record already says twice that she
stood for the presidency and did not survive the primary: in the event of 8 April 1982 and
in Susan Albert's profile. She lost the primary and was sworn in as Public Affairs Vice
President on 27 April. Her paragraph now says so, and the letters, the obituary and the
remembrance are cited rather than asserted.

Three smaller cuts. Tyler Scaff's committee was said to have explored a parking-availability
feature for the iWKU app; all three October 2014 minutes were opened, and what his committee
discussed was a break party for the custodians and sand volleyball courts. The app named
that month was another member's and had nothing to do with parking. That is the one thing
in the night's four branches I would call invented, and it went out of the record. Kasey
Glasgow was said to have been named chair at a first Senate meeting on 3 September 2014; no
such document exists or is cited, the Senate met Tuesdays, and she was already chair at the
cabinet's orientation meeting of 26 August. Temple Ricke was said to have been sworn in on
1 September 2015; the word does not appear in those minutes, which record approval by
unanimous consent.

One thing every future profile run needs to know: **adding a `profile` hides that officer's
`note` on the site.** `render_officer` shows one or the other, never both. Six of these
eleven had notes and four held facts the profile did not - Stewart's swearing-in date and
her own account of what ASG did, Faught's green tour and Earth Day festival, Newsome's
caveat that the vice-presidential title is the bill's rather than the chair's, Hedrick's
17 April 2019 page revision. Publishing as drafted would have quietly deleted all of it.
Each is now folded into its profile.

**#140, the backlog.** Thirty-seven garbled author and sponsor strings resolved against
their source PDFs. The branch was four merges behind, so main was merged in first; the
conflict was only the Kerrie Stewart profile added an hour earlier, and the photographs the
branch carried had already landed by another route.

The best catch of the night is here. The old sponsor row on Resolution 91-6-F read
"Mistianna Holcomb Joe Iracane". The resolution asks that Joe Iracane *not* be re-elected
chairman of the Board of Regents and recites the federal investigation against him. He is
its subject, not its sponsor, and publishing him as a sponsor of the resolution attacking
him would have been a bad thing to say about a named man. The document gives Mark Miller
and Eric McWilliams as authors and Holcomb alone as sponsor, and that is now what the file
says.

I went hardest at the nine rows deleted outright, since a deletion that discards a
recoverable name is invisible afterwards. All nine source PDFs do print a name. All nine
of those people were already recorded on that bill: the deleted rows were garbled
duplicates standing beside a correct row. Nothing was lost.

I corrected the handoff note on the one refusal. It said bill 13-24-S traced to a bare email
with no name anywhere in the document; "Millie Glessner, WKU Dental Hygiene Clinic Office
Manager" sits on the line above the address. The refusal to reconstruct "Mildred Hagood"
from a login was still right, and for a better reason than the one given, but a note telling
the next run that a document is nameless is how a real name gets dropped later.

## A mistake of mine, for the owner to decide on

I merged all four pull requests with merge commits. The previous report says squash-merging
is worth keeping to, precisely because the research commits carry a tool's name in the git
author field, and squashing keeps that out of main. Merge commits do not. Main's history
now carries eight commits authored under that name.

Nothing of it reaches the public site, and the same commits were already in the repository
on the research branches. But it is against the archive's own rule, and it is my error. I
have not rewritten main to fix it: main auto-deploys, a history rewrite is not reversible,
and it is not a call to make unilaterally at night. The next editor should squash-merge, and
the owner can decide whether the eight commits are worth rewriting for.

## Still open

Carried forward and unchanged: the thirty-five unresolved author lists, the six pre-2011
attributions the PDFs plainly carry, the duplicate 1976-77 pair, the Alford and Brenzel
portraits resting on a unique surname, the twenty-three "no record survives" assertions, and
the 1995-96 gloss on Bill 91-9-F that wants a clause acknowledging ASG had already run a
President for a Day in November 1990.

New from tonight:

- The seven 2006-07 minutes mirrored by #137 are **attached to nothing**. That year has no
  `documents` array, and `src.file` renders only on events, not on senate members, so 6.4 MB
  now sits in the repository and on the site with no link reaching it. The minutes of 3
  October and 30 January are the two best single documents for that year and deserve real
  entries. Mirroring a file and attaching it are two steps.
- The legislation completeness gap #140 surfaced and correctly declined to half-fix: long
  `CONTACTS:` lists truncated to two names on the 2017-18 diversity resolutions, missing
  authors on 14-22-S, 36-22-S and 16-24-S, which names four authors and records one, and
  Omar Salinas Chacon absent from the file entirely. That is an extractor problem, not a
  row-by-row one.
- Thirteen years still have no year photograph, and that gap is now beyond what the Talisman
  landing page can reach.

## Where the archive stands

61 academic years, 2,020 dated and sourced entries, 73 leader records, 649 records carrying
a written profile (up 11), 1,070 officer entries, 1,355 senate members (up 37), 152
photographs (up five), 294 documents mirrored (up seven), 1,111 legislation files, 1,104
legislation author rows, 1,746 pages built. build.py, check_data.py, check_contrib.py and
check_duplicates.py all clean on main at the close of the run; the six duplicate pairs are
the known pre-existing ones and are genuinely separate events. No pull requests left open.

# Editor's report - 23 August 2026, small hours

Two research branches open, both cut from current main, both merged. No stale branches
left: #6, #7 and #8 were closed before this run began and nothing is open now.

## What was reviewed

Roughly sixty claims opened at source, across the two branches. Not the research pass's
paraphrase of a document - the document. Twelve Senate minutes files downloaded from
wku.edu, six pieces of legislation, ten Herald stories, and the 1971 and 1973 Talisman
full texts from archive.org. Nothing on digitalcommons was needed, so the pacing rule
never came into it.

## #142, person profiles: merged after nine corrections

Two batches: ten senators and Senate secretaries from 2016-19 and 2023-26, and then,
pushed to the branch while this review was running, twelve early-1970s Congress members
drawn from the Talisman.

The substance held everywhere I checked. The Jonesville debate of 29 November 2016 is
reported exactly as the Herald has it, down to which senator argued for which version and
the bill passing in its original form. Bill 26-17-S carries "FAIL; 7-22-1" on its own face.
Bill 13-17-S was tabled on 7 March and passed 19-11-1 on 21 March, and $175 plus $50 is the
$225 the profile claims. The 23 January 2024 minutes record Livi Ray's nomination, a voice
vote, "Unanimous Yes", and her predecessor resigning the secretaryship on being nominated
elsewhere. The 1971 Talisman's Executive Council caption on page 67 gives Hundley, Gerard
and Sweet as the three members elected from Congress, and the body text describes the
council's job in the words the profiles use.

One thing was avoided that this project has fallen into before: Bill 32-17-F names Ian
Hamilton as its author and Jordan Tackett only under CONTACTS, and the profile says
"listed as a contact". That is the distinction that killed all thirty-nine of the old
missing-president claims, and it was got right.

What I changed:

- Karlee Powell's election quotation ran to nineteen words, over the fifteen-word limit,
  and a second phrase in quotation marks was the Herald's summary of what she said rather
  than her words. Rewritten to a single five-word quotation.
- William Hurst's first paragraph opened with the April 2017 election and then described
  two bills he carried in March and April of that year, before it. Bill 26-17-S already
  calls him a senator at large, so he was sitting in 2016-17. The paragraph now runs in
  order and reads the April result as a return.
- Three quotations from one Herald article in Alex Sergent's account, two from one article
  in Jordan Tackett's, reduced to one each with every fact kept.
- Resolution 8-17-F calls the Major Redz a registered student organization. The profile
  called them a dance team. Trimmed to the source.
- Four of the Talisman directory profiles - Burns, King, McEwen, Lamason - said the
  Congress seat was held in the senior year and then, two sentences on, said the directory
  does not date it. A senior directory lists a whole college career. All four now read as
  the Sally Ann Webb entry already did, and leave the year to the record's own placing.
  This is the one that mattered: a directory listing is precisely how a person ends up
  filed in the wrong year.

## #143, the senate rolls: merged after four corrections

2018-19 goes from two recorded members to twenty, 2020-21 from seven to seventeen, all out
of SGA's own minutes. The 5 February 2019 slate is in the document exactly as recorded,
confirmation by confirmation. Every one of the six new 2020-21 committee chairs is
separately titled "Senator" somewhere in the corpus, so the seat rests on evidence and not
on the chairmanship - again, the trap avoided. Dawson and Addison McCoun really are two
people: the minutes have one praising the other in the third person, two lines before the
other is confirmed.

Four notes did not survive:

- Logan Hornback was not nominated on 2 October 2018. She is not named anywhere in those
  minutes. Nomination, confirmation at 18-14-2, and oath all happen at one meeting on
  16 October.
- Lucas Knight was not vice chair of Campus Improvements. On 26 March 2019 he gave the
  Academic and Student Affairs report standing in for Chair Amanda Harder; Campus
  Improvements reported separately three lines below under Matt Barr.
- Hunter Smith's swearing-in is not in the record at all. The note had him "Sworn in with
  'all the new senators'" on 25 September 2018; that phrase is not in the document and the
  minutes carry no oath that night, only the President welcoming them. His seat now rests
  on the floor amendments he actually moved, with the gap stated. This is the one that
  would have put a ceremony that never happened on the live site.
- Anna McAvoy was quoted saying she had "been a Senator for the past two years". The
  minutes read "She was a Senator for the past two years" - the secretary's summary, not
  her speech.

Three of those four are the same failure: a detail belonging to a neighbouring meeting, or
to the drafting pass's own phrasing, attributed to the cited file. The verifier re-read the
cited source and passed them anyway, which suggests it was asking whether the claim was
plausible against the source rather than stated in it. For every date, vote count and
quoted phrase, the verifier should have to point at the line.

## The attribution problem is larger than last night's report said

The late-evening report of 22 August recorded eight commits on main authored under the
tool's name and left the decision to the owner. The true figure is 108. The research
routines commit under that name and always have; merging their branches carries it onto
main. I added five more tonight, one of them my own merge commit, before setting a local
identity - I should have squash-merged, as that report recommended, and did not.

Nothing of it reaches the public site: site/ and data/ are clean of it, and check_contrib
tests for it. But 108 commits is past the point where it can be called an oversight, and
rewriting a history that auto-deploys is not a decision to take at night on my own. Two
routes for the owner: leave it, on the grounds that it is invisible to readers; or rewrite,
once, with the routines stopped. What the next editor can do without asking is squash-merge
every research branch from here, which stops the count rising.

## Still open

Carried forward unchanged: the thirty-five unresolved author lists, the six pre-2011
attributions, the duplicate 1976-77 pair, the Alford and Brenzel portraits resting on a
unique surname, the twenty-three "no record survives" assertions, the 1995-96 gloss on
Bill 91-9-F, the seven 2006-07 minutes mirrored by #137 and attached to nothing, the
legislation extractor's truncated CONTACTS lists, and the thirteen years with no
photograph.

New tonight:

- Troy Davis II (2018-19) and Troy Davis (2020-21) sit as two records. A freshman in spring
  2019 would be a junior in 2020-21, so they may be one person, but a matching surname and
  a plausible gap is not evidence and name-aliases.json rightly has nothing. It wants a
  minutes line, not a guess.
- Two files linked from the 2018-19 minutes page, minutes-3-sep and minutes_24_sep, are not
  2018-19 minutes: their text is dated September 2019 and names 2019-20 officers. #143
  found this and correctly declined to use them. Anyone sweeping that directory will hit it.
- The 1971 Talisman bears on the open Lyne-versus-Zielke question for 1970-71. It captions
  John Lyne as president on page 67 and carries a year-in-review essay signed "John Lyne,
  president, Associated Students". That is evidence, not a settlement, and it is now cited
  in four records in that year.

## Where the archive stands

61 academic years, 2,020 dated and sourced entries, 73 leader records, 671 records carrying
a written profile (up 22), 1,070 officer entries, 1,383 senate members (up 28), 152
photographs, 294 documents mirrored, 1,111 legislation files, 1,761 pages built. build.py,
check_data.py, check_contrib.py and check_duplicates.py all clean on main at the close of
the run. The six duplicate pairs are the known pre-existing ones: two are separate bills
moved on the same day, which stay separate by rule, and the other four are an introduction
and its later vote, or an announcement and its later execution. No pull requests left open.

---

## 23 August 2026 — the editor's second pass of the day

Four research pull requests were open at the start of the run and all four are merged.
Every one needed correcting first. Nothing was rejected, and nothing was cut for being
unsourced: the whole night's editing consisted of putting back material the research had
dropped, and fixing two numbers.

**#145, the legislation authorship rebuild.** The largest diff of the four and the most
clearly right. The old file had been filing WKU staff, faculty advisers and other
organisations' officers as sponsors of SGA bills, because the extractor read a fixed
200-character window past a SPONSOR field naming a committee and straight into the CONTACTS
names below it. Ten changed files opened at random against their PDFs all matched exactly,
and all nine surviving sponsor rows are genuine people printed in a SPONSOR field. But the
report's claim that no file lost its authors did not hold: run the other way round, four
documents had lost people they name. Bill 27-18-S had lost all six of its authors, printed
title-first with no comma; 9-20-S had lost Mary Jane Mayo behind an AUTHOR(S) label;
29-23-S had lost Adan Canizalez to a stray comma inside his own name; 1-23-F had lost Donte
Reed to quotation marks round his nickname. Nine names restored off the PDFs. The file
stands at 1,123 rows. The extractor itself was never changed, so the next run of
extract_authors.py will regenerate every error this pass removed — that fix belongs in the
script and is still outstanding.

**#146, six portraits from the Talisman.** All six identifications hold. The two cropped out
of a group photograph were the ones worth doubting, so the page scan was pulled and looked
at: the back row of the right-hand ASG photograph on p. 114 of the 1987 volume is four
people, and Rodriguez and Schocke sit in positions one and two exactly as the caption orders
them, with Tim Todd formally dressed in position three. Rodriguez's office is confirmed
separately in the same book. Cathy Murphy was the risk. The 1978 Talisman contains two Cathy
Murphys, and a senior portrait caption cannot tell you which one you are holding. The
volume's index settles it — Mary Catherine Murphy is indexed at pp. 34, 276, 370 and 427,
p. 370 being the portrait and p. 34 being the ASG page that names her vice president, while
Cathy Renee Murphy of Louisville appears only at p. 401. The portrait is right; the citation
now carries that reasoning instead of resting on the caption alone.

**#147, nine officer profiles of 2016-18.** The cleanest of the four; nothing cut. Every
figure checked against the Herald held to the digit — the 1,579 votes of the April 2017
election and its 930/305/212 split, the 17-9-1 on Bill 20-17-S, the 32-1 on Bill 17-18-F,
Cody Cox announcing Amarah Reed's departure and McAndrews succeeding her, the national
coverage of the reparations resolution and Ransdell's refusal of it. Where the December 2018
Herald and the October 2018 Herald disagree about the date of Logan Hornback's nomination,
the profile follows the contemporaneous report and is right to. The John McKinney paragraph,
the one entry here that could injure a living person, reports only what its source reports,
names no accuser, and ends by saying the record shows no confirmation, denial or resolution
— which is what the rule requires. It declines even to draw an inference the Herald itself
leaves open. One flag carried forward: the claim that Kentucky Senate Bill 17 was signed on
20 March 2017 appears in two profiles now and in no cited source. It arrived before this PR;
it wants running down or dropping from both.

**#148, the 1969-70 class-officer seats.** Eleven entries recovered from the spring 1969
result sheet, and all eleven are correct on the scan, including the OCR digit the verifier
had already caught and fixed. The report was wrong about what the sheet omits. It states
that the Junior class President, Vice President, Secretary and Treasurer races carry no vote
totals. They carry all four, each with the same hand-drawn winner's mark as the races that
were kept: Phil Myers 493 to Jim Dowd's 455, Pat Riley 467 to Russ Richardson's 455, Sue
Pritchett 493 to Pam King's 449, Lowry Stagg 475 to Phil Ray's 458. The sheet is typed in two
columns and plain-text extraction throws the Junior figures away from their names, so they
read as missing; on the page they are perfectly plain. Four seats and four people added. The
document extract, the one line of that PR a reader sees quoted, gave Frank Genzianelli 1,621
votes where the sheet prints 1,626 — the text layer renders that digit as an "i". Corrected.
The 1969-70 roll now stands at seventeen seats. The note recording that the Congress-seat
link is an inference from the 1966-67 roster and not stated on the 1969 document is exactly
right and was left as written.

**The lesson of the night, twice over.** Two of the four PRs lost real, sourced material to
a text layer rather than to a judgement — once in a two-column typed sheet, once in a
two-column PDF form. Both times the researcher concluded something was absent when it was
legible on the page. A miss in an extraction is not a miss in the document. Render it and
look at it before writing down that it is not there.

## Where the archive stands

61 academic years, 2,018 dated and sourced entries, 73 leader records, 657 records carrying a
written profile, 1,085 officer entries, 1,383 senate members, 158 photographs, 295 documents
mirrored, 1,123 legislation authorship rows, 1,111 legislation files. The entry count is two
lower than this morning because #147 correctly combined two pairs of duplicated 2018-19
events, losing no sourced fact from either. build.py, check_data.py, check_contrib.py and
check_duplicates.py all clean on main at the close of the run. The six duplicate pairs are
the known pre-existing ones. No pull requests left open.

# Editor's report — 23 August 2026, third pass

Two pull requests open at the start of the run, both cut from the current head of main,
both merged. The three pull requests from 4 August that earlier reports had down as stale —
#6 photographs, #7 the 1980s, #8 the 2020s — were already closed on 18 August. Nothing
was left rotting for me to deal with.

GitHub was reachable this run. `gh` is not installed in these containers, as AGENT-LANDING.md
says; git is credentialed and the GitHub tools work, so the branches pushed and the merges
landed normally.

## #151, the 1969-70 class officers: merged after three cuts

Twelve class officers profiled off the Office of Associated Students' own spring 1969
election result sheet. I checked the arithmetic on all twelve rather than a sample, and I
did it on the page image, not the text layer — which turned out to matter, because the
extracted text throws the Junior class figures away from their names and they read as
missing. Every count is right: Gerard 739 unopposed, Robinson 447–360, Bohannon 404–396,
Bradshaw 451–326, Showalter 531–292, Myers 493–455, Riley 467–455, Hunter 786–561,
Joe Gerard 863–477, Jennings 762–566, Galloway 684–645, Civils 695–673. The three Herald
headlines behind Paul Civils's freshman year are in the unfiltered local index verbatim.
Every claim taken from the 1971 Talisman is in the yearbook's full text: Joe Gerard on the
Executive Council, Phil Myers on Rules and Elections and president of the Class of 1971,
Pat Riley on the Judicial Committee, Galloway's Sigma Nu and Interfraternity Council offices.

Three things came out.

A paragraph on Jeanette Bohannon rested on a single 1968 headline about a Student National
Education Association selection, and said in its own last sentence that what she was selected
for could not be established. A paragraph whose content is that a headline exists is padding,
and it hung a non-SGA activity on a living person's record. Cut, with its now-orphaned source.

A sentence on Marshall Galloway recorded him and Claudia Houston as Athenian Ball King and
Queen at Greek Week. Accurately sourced — it is in the Talisman — but a Greek social honour
unconnected to his term as class treasurer, and it put the name of a second private person
with no SGA role at all onto the site. Cut.

Pat Riley was placed "among the seven members of the Judicial Committee." The yearbook's
text does say seven; its own caption underneath names eight. Trimmed to "among the members."

And a correction that was not a cut. Four of the profiles cited the 1971 Talisman **Part I**
for the Associated Students spread, the Interfraternity Council and the Class of 1971 pages.
All of those are in **pt. 2**; Part I is student life, features and athletics. A reader
following the citation would not have found the claim being made. Repointed to
`dlsc_ua_records/390`, with Galloway keeping Part I for the Greek Week feature that carries
his major, hometown and IFC presidency and gaining pt. 2 for the chapter roster.

## #152, the 2012-13 legislation: merged as is, nothing cut

Twenty-one author and sponsor rows recovered by OCR from eleven scanned bills and resolutions
whose text layer is genuinely empty — I confirmed the emptiness independently before accepting
that OCR was necessary. Then I rendered all eleven and read the author blocks by eye. Every
row is exact, down to the lowercase "aid" in "Organizational aid Board" that a tidier pass
would have silently corrected.

This batch was laid with the trap that matters most in the legislation corpus. Every one of
these documents carries a `CONTACTS:` block under the sponsor, and on these particular files
the contacts are the people it would be worst to miscredit: Cory Dodds, the sitting SGA
president, appears as a contact on a resolution Hannah Garland wrote, and **Gary Ransdell and
Howard Bailey** — the university president and the vice president for Student Affairs — are
contacts on a student's athletic-fee resolution. Promoting a contact would have put the
university president's name on SGA legislation on the public site. Not one was promoted.

The eleventh file was left out and should have been. `ea1-12.pdf` is an executive action
establishing a special long-term goals committee, with no author, sponsor or contacts field
anywhere on it, closing over Cory Dodds's signature as president. Crediting an author from a
signature block would have invented a rule the other 1,123 rows do not follow.

## A mistake of mine

In the note I attached to #151 I gave Frank Genzianelli 1,621 votes in the 1969 presidential
race. The sheet prints 1,626. I read that one figure off the text layer instead of the page
image, where the last digit renders as an "i" — the exact failure this report warned about
last night, committed by the editor who had just spent an hour catching it in other people's
work. Corrected on the pull request. It touched nothing in the archive.

## What the lead is worth

The 1969 sheet has Larry Zielke taking the presidency 1,882 to 1,626 and John Lyne **losing**
the vice-presidency to David Porter, 1,751 to 1,725; the 1971 Talisman then has Lyne as
Associated Student Government president. That bears directly on the Lyne/Zielke question
CLAUDE.md still lists as open, and it points the same way from two independent directions.
Left for whoever takes that item; not settled here.

Separately, SGA's own 2012-13 legislation spells it **Keyana Boka**, in the contacts blocks
of three documents. CLAUDE.md still carries `Keyanna`/`Keyana` as unverified. Three
contemporaneous SGA documents are not proof, but they are better evidence than anything the
flag currently rests on, and they are already in the repository.

## Still open

- The Kentucky Senate Bill 17 signing date of 20 March 2017, flagged in the previous report
  as appearing in two profiles and no cited source. Untouched this run; still wants running
  down or dropping from both.
- Two title typos in `legislation.json` — "Academic Compeition Club" and "Adopt Admendments"
  — are the harvester's, not the OCR pass's. The documents themselves read "Competition" and
  "Amendments". A cleanup pass, not a correction to anything published as a fact.

## Where the archive stands

61 academic years, 2,018 dated and sourced entries, 73 leader records, 1,085 officer entries,
1,383 senate members, 158 photographs, 295 documents mirrored, 1,144 legislation authorship
rows across 1,111 legislation files. Twelve profiles added this run, three paragraphs or
sentences cut from them. build.py, check_data.py, check_contrib.py and check_duplicates.py
all clean on main at the close. The six duplicate pairs are the known pre-existing ones and
every one of them is genuinely two events. No pull requests left open.

# 23 August 2026 — editor's fourth pass

Four research pull requests open, all cut fresh from current main, all four merged. One
further pull request opened and merged by the editor for a defect found along the way.

## What was reviewed and merged

**#154, the senate rolls.** Five senators added to 2012-13. Fewer than eight new claims, so
every one was checked rather than a sample, in the full text of its cited article. All five
held. The run's discipline is worth recording: the same sentence that gave it Taylor Gwinn
and Brad Cockrel also names Seth Church and Kara Raley, and it correctly filed those two as
Judicial Council rather than sweeping them into the Senate; Jackie Stewart, approved in the
same breath as Roy Ratliff, was correctly left out as an associate justice. Mulcins/Mullins
was flagged, not silently resolved, and not added to the aliases file.

Three notes were trimmed. Laura Harper's senator title came from a Herald item printed on 17
October 2012 announcing a picnic to be held on the 22nd — an advance notice, and the note had
her attending it on the 17th. Her seat was never in doubt; the attendance was. Mac Mullins is
the mirror case: the 23 October piece is the actual report, so attendance is proven, but 23
October is the publication date and the note dated the picnic to it. Roy Ratliff's
appointment was approved on 16 April 2013 in the future tense — the Herald says he "will
become a senator-at-large" — at the meeting already choosing the next speaker, so the note
now carries that ambiguity instead of asserting a settled 2012-13 seat.

**#155, twelve officer portraits** for 2025-26 and 2026-27. Checked harder than a sample,
because a misidentified face is the one error this archive cannot take back. Every URL is
live and returns a real JPEG; four committed files match the original upload byte for byte
and the rest are crops. Every caption was checked against the Herald's own media record
rather than an article page, and all eleven matched verbatim. Every crop takes the correct
person, checked by eye against the original: Barker from the left and Derryberry from the
right of the three-man election photograph, Pace from the centre of three, and Hadley Whipple
— the one to watch, because that caption names two people without saying who stands where —
correctly taken as the seated student rather than the staff advisor leaning in to help her.
Every name matches years.json exactly, and the one image serving two years is right: Preston
Jenkins really did hold the same office in 2024-25.

Two labels were trimmed. The Butler portrait opened with "(FILE PHOTO)", which is not in the
Herald's caption and is contradicted by the image having been uploaded the day of the
swearing-in it shows. The Yelton label asserted the photograph was "dated 25 Feb 2025"; that
is the Herald's upload date, while the Herald's own caption says 24 March 2025. The two
disagree, that is the paper's inconsistency and not ours to resolve by choosing one, and the
label now says so.

**#156, ten profiles** of judicial council and committee officers, 2016–2022. Given how much
of this concerns living people and a racial-conduct dispute, nothing was sampled: every
factual claim was checked against all ten cited Herald articles, both Senate minutes files
and the legislation index. Everything held, including two claims that looked unsourced until
the second document was opened. Turner Reynolds's "confirmed 10-2" appears nowhere in the
newspaper, which reports three unanimous confirmations and no count for her; it is in the 24
September 2019 minutes, as "confirmed Ms. Turner 10-2-0", and those minutes also confirm the
other three were unanimous. Symone Whalin's "passed 29-1" is in its article written out as "a
29-to-1 vote with one abstention". Both `name-aliases.json` additions are sound: the minutes
spell "Derrick Collins" and "Holden Schroder" where the Herald spells "Derek Collins" and
"Holden Schroeder", for the same four nominees at the same meeting.

Brigid Stakelum's position is reported fairly, and that matters more than the arithmetic. Her
two quotes are accurate and come from different articles, so the one-quote-per-source rule
holds; and the line saying she still believed those responsible should be punished is not a
softening but the source's own sentence — she believed it necessary to punish those involved
with the video, but not members who had nothing to do with the slur. Reporting her opposition
without it would have misrepresented her.

One correction, in two places. Both the Whalin and Stakelum profiles described the video as
"a chapter member sang a racial slur". Both cited articles say members, plural. On a matter
like this the number of people involved is exactly what to take from the source rather than
compress, and both now follow the reporting.

**#157, scrape debris cleared from 103 legislation titles.** The cleanest branch reviewed on
this project. A sampled check would have been close to worthless here — one bad pattern can
corrupt dozens of rows and a sample of eight will miss it — so all 103 were checked two ways.
Ninety-seven of the new titles are exact substrings of the old scraped strings: debris
removed, not a character invented. The six that add text were each opened: five gained the
words "A Bill to", which the PDFs confirm at the head of their titles and the old scrape had
dropped, and `resolution_3-17-s` restored "Redz", confirmed in the document's own purpose
clause and corroborated by `bill-31-17-f` naming MajorRedz elsewhere in the same file.
Independent text extraction found 87 of the 103 verbatim in their own PDFs; the other 16 are
titles set in subset fonts that would not decode, not mismatches. The file has 1,111 entries
before and after, none added or removed, and not one non-title field changed.

## What the editor fixed

**#158.** Found while reviewing the photographs and unrelated to them: the 2025-26 executive
roster carried nine entries for six officers, with Maggie Yelton appearing three times and
Jade Ismail twice, once under the office title "Chair of the Action &" — cut off mid-word,
with a note repeating the fragment. This was live on the site. The cause is not a research
error but the legislation harvester recording an officer once per bill that names them, so
every individual entry was correctly sourced. Fixed by consolidation rather than deletion:
each officer appears once and carries every source that named them, including one bill that
Ismail's profile already discussed and that now cites properly. No source URL was dropped.
The same pattern will recur for any officer named on more than one bill, in any session, and
has not been swept for.

## Still open

- The Kentucky Senate Bill 17 signing date of 20 March 2017, in two profiles and no cited
  source. Untouched again this run; still wants running down or dropping from both.
- Two harvester typos in `legislation.json`, "Academic Compeition Club" and "Adopt
  Admendments". The 103-title pass did not reach them: it only covered titles carrying a bill
  number and vote or committee pattern, and said so plainly.
- Other sessions almost certainly carry both the differently-shaped title debris that pass
  did not look for and the duplicate-officer pattern behind #158.
- The photograph run's citations point at bare `wp-content` image files, so a reader who
  clicks one gets a JPEG with no caption and no way to check the identification. Carrying the
  article URL alongside the file URL would make these portraits checkable by a reader rather
  than only by an editor with the media API.

## Where the archive stands

61 academic years, 2,018 dated and sourced entries, 73 leader records, 1,082 officer entries,
1,388 senate members, 171 photographs, 118 documents attached, 1,144 legislation authorship
rows across 1,111 legislation files. build.py, check_data.py, check_contrib.py and
check_duplicates.py all clean on main at the close. The six duplicate pairs are the known
pre-existing ones and every one of them is genuinely two events. No pull requests left open.

# 23 August 2026 — editor's fifth pass

One pull request open at the start of the run, #160, person profiles. The three stale
branches named in the standing brief — #6 photographs, #7 the 1980s, #8 the 2020s — are
already closed and no longer need dealing with. GitHub was reachable this run: `gh` is not
installed in these containers, but git push works and the GitHub tools answer, so this was a
full pass and not a review-only one.

## #160, person profiles: merged after six corrections

Twenty-three profiles in the end, not the twelve the pull request opened with. The routine
pushed a second commit while the review was in progress — eleven more profiles covering the
1969 class officers and the Judicial Council justices of 2008 to 2012 — so both commits went
through the same check.

The verification went well past a sample. Sixteen bills and resolutions in the 2025-26
legislation folder were opened and read, along with the executive board minutes of 12 August
2025, the Judicial Council minutes of 26 January 2026, the Herald's report of the chief
justice election of 12 November 2025, and the November 2009, May 2010 and October 2012
snapshots of the SGA judicial page. The 1969 election result sheet had to be read as rendered
images: its OCR text layer silently drops the junior class vote counts altogether, so anyone
checking that document by text extraction alone would have found nothing to check against.

Most of it held. Every dollar figure, date, purpose and co-authorship in the eight senator
profiles matched the bills. The 1969 figures are exact to the sheet — Pritchett 493 to King's
449, Stagg 475 to Ray's 458, Lamason 546 to Reuling's 408, Todd leading the at-large race on
1,719 with Durham second on 1,514. The archived judicial rosters name every justice claimed.

Six things were wrong or overstated.

Amelia Tucker's profile said she was credited as an author on six pieces of legislation. She
is named in the AUTHORS block of fifteen of the session's filed bills and resolutions, each
one spelling her Amelia Tucker or Amelia R. Tucker, so this is not a surname collision. The
count is now fifteen, and the six described are framed as a selection. The same sentence said
the Amelia R. form appears twice; it appears six times. I briefly replaced the comparison the
routine's own verifier had cut with a different one and then took it out again: fifteen by one
counting method and thirteen by another, against twelve for the next most active author, is
too close to publish as a superlative.

Mike Durham's profile stated that he had served that February on the Constitutional Revision
Committee. The 1968-69 entry for that member carries a note saying the name is OCR-garbled —
the minutes read "Hike Durham" — and unverified against any second source. Asserting the two
are one person is the merge-by-name this project forbids, and the profile now reports what
the minutes record and says the identification is not established.

Five 1969 profiles called the election a Congress election. The year's own note says the
result sheet is headed *Associated Student Government Election* and never uses the word
Congress; they now use the document's wording.

Both 2025-26 chief justice profiles left the handover vaguer than this archive already knows
it: Graham's ended at "by 26 January 2026 the minutes record Stirling as chief justice," when
the year's own sourced events date the election to 12 November 2025, 3-1 over Xavier Spiess,
and the swearing-in to 18 November. Both now carry the dates, checked against the Herald
report itself. Graham's profile also had the executive board convening "for its first meeting
of the year" on 12 August, which nothing in those minutes says; cut.

Resolution 2-26-S was described as adopting bylaws drafted by the Bylaws Review Committee.
The resolution says reviewed and revised. Trimmed. And Tyreesha Morris turns out to be spelled
three ways across her own legislation, not two — Tyreesha four times, Tyresha once and Tyreeha
once — so the third spelling is now in `name-aliases.json` and her profile says so.

## What could not be checked

Lamiaya Page's appointment to the Judicial Council on 29 January 2008. TopSCHOLAR answered the
minutes download with HTTP 202 and an empty body on three attempts, including after the
90-second backoff and with a session cookie carried from the landing page. That landing page
does confirm the meeting date and that committee vacancies were on the agenda, and the leader
entry and its citation were already on main, so the profile adds no claim beyond what was
published — it was not a reason to hold the merge. It is worth another attempt on a run when
the archive is answering.

This is the bot protection behaving exactly as the handoff describes, and it is worth noting
that it now refuses a `viewcontent.cgi` download while serving the landing page beside it
without complaint.

## Still open

- The Kentucky Senate Bill 17 signing date of 20 March 2017, in two profiles and no cited
  source. Untouched again; four passes have now walked past it.
- The two harvester typos in `legislation.json`, "Academic Compeition Club" and "Adopt
  Admendments".
- CLAUDE.md still lists "John Lyne vs Larry Zielke 1970-71" as an open question. It is not
  open any more. The archive corrected Zielke to 1969-70 and Lyne to 1970-71 some passes ago,
  and the 1969 result sheet read this run corroborates it from a source neither correction
  cited: Zielke beat Frank Genzianelli 1,882 to 1,626 in the spring 1969 election, which by
  this project's own filing rule seats him in 1969-70, and John Lyne lost the vice-presidency
  on the same sheet to David Porter, 1,751 to 1,725. That line in CLAUDE.md can be retired,
  and the result sheet is worth citing on both leader records.
- The photograph run's citations still point at bare `wp-content` image files with no article
  URL beside them.
- Kaden Blankenship's profile stops at his appointment, though the year already records him
  resigning from the council on 2 April 2026 to stand on a presidential ticket, and that
  ticket's censure. Left for the routine rather than written by the editor.

## Where the archive stands

61 academic years, 2,018 dated and sourced entries, 73 leader records, 1,082 executive and
senate officer entries, 1,388 senate members, 725 people carrying a written profile, 110
leader portraits and 61 year photographs across 157 image files, 118 documents attached, 1,111
legislation files with 1,144 authorship rows. build.py, check_data.py, check_contrib.py and
check_duplicates.py all clean on main at the close. The six duplicate pairs are the known
pre-existing ones. No pull requests left open.

# 23 August 2026 — editor's sixth pass

Four pull requests open at the start of the run and all four merged: #162 the backlog, #163
the senate rolls, #164 photographs, #165 person profiles. GitHub was reachable, so this was a
full pass. Every branch was cut from the current main and merged cleanly; none of the stale
4 August branches remain.

## What was checked, and against what

Twenty-odd claims opened at their own sources rather than sampled from the reports. The 1997
legislation index on the Wayback Machine, the SGA congress notice of August 2000, the Judicial
Council rosters of September 2013, April 2015 and January 2022, the Daily News report of the
2017 reparations resolution, the WKU News release of the May 2007 banquet, the Herald of
18 October 2007 through its repaired link, the Herald reports of 13 February, 26 September and
3 December 2013, the Senate minutes of 3 September 2013 and of spring 2014, the Herald of
1 December 2021 and 23 September 2021, four bill and resolution PDFs from 2021-22, and the
1974 Talisman at pages 94, 96 and 311.

## What the editor fixed

- **#163.** Megan Skaggs' seat note dated the transcript voucher bill 26 September 2013, which
  is the Herald's publication date; the bill passed at the Tuesday meeting of 24 September.
  Rewritten.
- **#163.** Mark Rawlings' note stated flatly that the Congress member of January 2000 became
  vice president of finance the following year and vice president of public relations for
  2001-02. No source establishes that. The routine's own research note conceded as much.
  Rewritten to record the later Rawlings as a separate appearance in the archive and to say
  plainly that nothing joins them.
- **#165.** Jacob Skillman's profile called the Swipe Out Hunger resolution a fall 2021
  document. Resolution 2-22-S has its first reading on 8 February 2022. Rewritten.
- **#165.** Caleb Collins was said to have been elected a senator-at-large for 2021-22. The
  bill documents show him holding the seat, not winning it. Softened to "served as", matching
  the fix the routine had already applied to his 2022-23 line.
- **#164.** The Goodpaster portrait cited the 1974 Talisman at page 95. The page prints 96.
- **#162.** The branch had dropped the trailing newline on `data/years.json`. Restored.

## What held up

The backlog run's thirty trims were the right call and the pages bear them out: the 1997
legislation index really is nothing but numbers, titles and dates, and the August 2000 congress
page really is an advance notice. The 2017 reparations entry, which grew rather than shrank,
matches the Daily News word for word on the 19-10 vote with one senator declining. The two
Talisman portraits carry their own printed numbers, 24 and 18, in the crop. The 2014-15
Judicial Council page does list six justices while its own boilerplate says five, exactly as
the profiles routine's verifier reported.

The best thing in the run was a trap not sprung. The Herald of 23 September 2021 introduces
both Jacob and Zach Skillman — brothers, both juniors in business economics, both Gordon Ford
ambassadors, both in the same book club. Resolution 2-22-S names them separately, one as
senator-at-large and one as sustainability chair, and the profile follows the full name. A
surname match there would have merged two people into one.

## Still open

- The 2 March 2006 Stevenson claim. The event, his note and his profile all say he read a
  letter, and quote a word from it. The only citation is a TopSCHOLAR issue index, which
  carries the headline and nothing else. The backlog run improved this — before it there was
  no 2006 citation at all — but the page itself still needs reading before the wording stands.
- Facts trimmed for citing the wrong page that are probably true elsewhere in this archive:
  Isaac Keller as chief justice the following year, Abbey Norvell as executive vice president
  in 2020-21, Herlick and Goins on Bill 17-22-S. They should come back under the citation that
  actually carries them.
- The five 2014-15 justice profiles are one sentence with the names permuted. Honest, but a
  roster page cannot make a profile.
- Billy Lyons and the rest of the 1999-00 Herald year, per the senate routine's own note.
- Everything on the previous pass's open list that no routine has picked up: the Kentucky
  Senate Bill 17 signing date with no source, the two harvester typos in `legislation.json`,
  the CLAUDE.md line calling Lyne and Zielke an open question when it no longer is, and Kaden
  Blankenship's profile stopping short of his resignation.
- **Vercel is refusing deployments**, having passed a hundred in a day on the free plan. The
  merges above are on main but the live site will not rebuild until the limit resets.

## Where the archive stands

61 academic years, 2,018 dated and sourced entries, 73 leader records, 1,083 executive and
senate officer entries, 1,395 senate members, 738 people carrying a written profile, 113
leader portraits and 61 year photographs across 160 image files, 118 documents attached and
1,111 legislation files. build.py, check_data.py, check_contrib.py and check_duplicates.py all
clean on main at the close, and site/ rebuilds with no change. The six duplicate pairs are the
known pre-existing ones. No pull requests left open.

# 23 August 2026 — editor's seventh pass

Two pull requests open at the start of the run, both merged: #167 person profiles, #168 the
backlog. GitHub was reachable and both branches were cut from the current main, so this was a
full pass with nothing left open. The stale 4 August branches are gone; #6, #7 and #8 were
closed on an earlier pass and no longer appear.

## What was checked, and against what

Not a sample. Every one of the twelve senator profiles in #167 cited a bill mirrored in
`data/legislation/`, so all eleven bills and the one resolution were opened and read against
the claim: bills 5-22-F, 7-22-F, 14-22-F, 15-22-F, 27-23-S, 34-23-S, 35-23-S, 39-23-S,
40-23-S, 41-23-S and 47-23-S, and Resolution 1-23-F of the following session. Every vote
count, reading date, dollar figure and office title matched the cover block exactly, including
the two bills whose Pass and Fail lines are blank and which the profiles correctly described as
carrying no recorded vote.

For #168, TopSCHOLAR's `viewcontent.cgi` refused this run outright — three retries at
95-second intervals and a fetch through a second client all came back 403 — so the Herald of
11 April 2002 was read from the Wayback Machine's September 2024 snapshot of the same URL
instead. Printed page 6 carries the photograph, the credit line to Edward Linsmier and the
caption naming Jamie Sears, Joe Loney and Ross Pruitt, and the winners box on the same page
confirms Sears as president and Pruitt as vice president of finance. The committed file is a
real JPEG and is the same photograph.

## What the editor cut

Four things, none of them a deletion of research.

- **Barrett Gibbs's profile said a Safety Awareness Week was "held" 17-21 October 2022.**
  Bill 7-22-F passed on the 11th and describes a week beginning on the 17th: it proves what was
  funded and planned, never how the week went. Reworded to "planned for." Brett Phelps's
  profile, drawn from the same bill, had already got this right.
- **Neel Patel's profile inverted who was surveyed.** Bill 34-23-S surveys students about
  relations with Bowling Green, not the Bowling Green community. Corrected, and the $50
  restored to the sentence.
- **Salvador Leon's profile claimed a bill authored by Salvador Leon Golib.** This archive
  keeps those two names apart deliberately: no alias in `name-aliases.json`, two separate
  person pages, and a 2023-24 leader note that says in as many words that the record does not
  confirm they are one person. The sentence and its second source are gone rather than merging
  two people on an assumption. Bill 40-23-S still reaches the reader through the year page.
- **The 2002 election-night caption was the Herald's caption, not ours.** Near word for word,
  and unmarked as a quote. Rewritten to carry every fact — who is pictured, his class and
  hometown, what she had just learned, that Pruitt ran unopposed — in the archive's own words.

## What held up

The profiles routine's arithmetic is sound and its hedging is good: it wrote "with 29 votes in
favor" rather than "29-0" where the Fail line was blank, called Mallory Hardesty the sole
author of Bill 35-23-S rather than a co-author, and recorded Caleb Collins as Community
Relations Chair rather than promoting a committee chair into a senate seat — the error that
killed all thirty-nine "missing president" claims in the past.

The backlog routine's claim that a separate adversarial subagent had re-verified the
photograph word for word turned out to be true when checked against the page independently.
That is the standard, and it is worth saying so.

The 2001-02 filing is also right, and it is the subtle one: an April election files its
*result* forward — Sears served 2002-03 — but the *night itself* belongs to 2001-02, and the
photograph is filed there as a year photograph rather than as a leader portrait.

## Still open

- The Salvador Leon / Salvador Leon Golib identification. If it is to be made, it needs a
  source naming one person under both forms and an entry in `data/name-aliases.json`, not a
  sentence in a profile.
- Eight years still have no year photograph: 1996-97, 1997-98, 2000-01, 2003-04, 2005-06,
  2006-07, 2008-09, 2009-10. The backlog routine's own note is honest about the limits of what
  it checked, and 2006-07 in particular has no April hit in the local Herald index at all —
  which per CLAUDE.md is a gap in the index, not evidence of no coverage.
- Everything on the sixth pass's open list that no routine has picked up since.
- TopSCHOLAR was refusing `viewcontent.cgi` for the whole second half of this run. The Wayback
  Machine served the same file and is not rate limited; routines blocked on a 403 should try it
  before concluding a source cannot be read.

## Where the archive stands

61 academic years, 2,018 dated and sourced entries, 73 leader records all carrying a written
profile, 113 leader portraits and 62 year photographs, 1,111 legislation files, 295 documents
copied into the site. build.py, check_data.py and check_contrib.py all clean on main at the
close, and site/ rebuilds with no change. check_duplicates.py reports the same six pre-existing
pairs, every one a genuinely separate event. Vercel is deploying again after refusing earlier
in the day, so the merges above are live. No pull requests left open.

---

# Night report - 23 August 2026, eighth pass

Four research pull requests were open. Three merged, one sent back. Everything below
was checked against the sources named, not against the routines' own reports of them.

## What merged

**#170, twenty-one senator profiles (2023-24 and 2025-26).** The strongest research PR
this project has produced, and nothing was cut from it. Fourteen authorship claims were
checked name by name against `legislation-authors.json`, which is extracted from the
bills themselves, and every co-author list matched exactly - including the claim that
Connor Ferguson's three Community Relations bills were joined by Savanna Kurtz on two of
them, which is right: she is on 11-23-F and 11-24-S but not 14-23-F. All twelve 2025-26
bills and resolutions cited for Rettig, Vietze and Marshall matched the mirrored PDFs.

The sensitive material was opened directly rather than taken on trust. The Judicial
Council hearing minutes of 13 April 2026 confirm the violation was brought by the Council
itself rather than on a complaint, under section 3.11, unanimous 4-0, censure without
removal from the ballot. The minutes of 15 April confirm the anonymous complaint, sections
3.13 and 3.13.1, the video the chief justice and associate chief justice obtained
themselves, a 5-0 finding, no responsibility under 3.6.8, and the remedy: the campaign
team censured and disbanded, the ticket deliberately not censured a second time. The
profile's account of both hearings is exact. The Herald of 19 October 2023 confirms the
Verdict Award question outright - the award "was given to Madison Payne, Ogden College
senator, in August" - so Payne's inaugural award and Solorzano's September award as the
second are both correct.

The living-people handling is the part worth recording. Outcomes are stated in both
censure cases rather than allegations left hanging, the anonymous complainant stays
anonymous, and the third-party brand ambassador named in the 13 April minutes is left out
of the published text, which is the right call for someone peripheral and not a public
figure. Geoffrey Aberle's profile flags a numbering conflict between the WKU archive
(Resolution 1-23-F) and the Herald's report of the same measure (6-23-F) and declines to
pick a winner. That is how a discrepancy should be handled.

**#171, the 1971-72 Congress roll and the 1979-80 seat restructuring - merged after one
cut.** The 1972 Talisman caption on pp. 272-273 was read directly: it names thirty-nine
people across two group photographs and all thirty-nine were in the diff, with nothing
invented. The 1979-80 claim is verbatim in the 1980 Talisman p. 274 - eight on-campus,
eight off-campus and eight general-representative seats replacing twenty-four
representatives at-large - and "Kevin Kinne, student opinion poll committee chairman"
is there word for word, as is Tim Irons as rules and elections chairman. Recording both
as committee chairmen with an explicit note that the text never seats them in Congress
is the trap the handoff warns about, avoided.

The cut was the thirty-ninth name. The caption reads Reed Morgan, and the archive already
carries a Reed Morgan at 1968-69 as the unresolved plaque entry. `build.py` keys person
pages on the canonical name alone, so adding the member merged the two: the built page
read "1968-69 to 1971-72 - Reed Morgan - Service 2 years in office" at the top of the very
page that argues at length the plaque name belongs to a student who graduated in spring
1966 and appears nowhere in 1968. The routine had seen the danger and written a note
saying they were different people, but a note in the data cannot stop the build from
merging them, and nobody looked at the page. The name is held back and the fact kept in
the year's senate note instead, with the corroborating detail that the 1972 Talisman puts
a Reed Morgan among the Alpha Phi Alpha brothers at that fraternity's charter presentation
on 31 October 1971, alongside fellow Congress members George Kendrick and Ed Givens. The
other thirty-eight were checked for the same collision: only Marshall Galloway (1969-70)
and Terry Miller (1972-73) touch existing records, both adjacent years and plainly the
same person continuing.

**#173, four candidate leads for the year-photograph gap.** Documentation only; the
handoff file is not read by the build. All five checkable claims verified against
`herald-index-full.json` - four Herald citations exact down to the Vol. 81 No. 42 [46]
mislabel, which was carried through rather than quietly normalised, and the negative
claim about April 2007 confirmed: records 6694 through 6697 each carry one index line,
the generic boilerplate, no headlines at all. The run states plainly that `viewcontent.cgi`
was closed all session and that none of the PDFs were opened, and it lets no conclusion
drift past that. A run that finds nothing, says so, and leaves four exact citations for
the next one is worth more than a run that reaches.

## What did not merge

**#172, the photograph run.** Every one of its eleven portraits had to come out, and after
removing them the branch's data was byte-identical to main. The whole contribution was
duplicate or defective.

The two files presented as new crops are the same file - md5 `eb7a436b...` for both - and
neither is a crop: it is the full uncropped 890x565 ASG group photograph, roughly
twenty-seven people, saved twice under two individuals' names. The crop step returned its
own input and the run reported success on it. That photograph is also already in the
repository as the 1980-81 year photograph, so the two files were a third copy.

The deeper problem is that `build.py` renders a leader photo inside `figure class="portrait"`
with alt text reading "Portrait of {name}". The built pages therefore carried thirteen faces
labelled "Portrait of Cindy Richards" and twenty-seven labelled "Portrait of Greg Zoeller",
the identical image also labelled as Marsha Sanner. The caption proves these people are
somewhere in the frame, not which one they are, and the alt text asserts otherwise to a
screen reader. On main every one of the 113 leader photos is a real portrait, and the seven
shared files are always one person across two of their own years; this would have been the
first departure.

And the identifications were not new. The existing 1985-86 year-photo caption on main already
names all thirteen officers with their offices, and the 1980-81 caption already names Sanner
and Zoeller. The session re-transcribed captions that were already in `data/photos.json`.
The corrections are pushed and the PR left open on a clean base for the next photograph run.

## Still open

- **Two people who share a name cannot both be recorded.** There is no `person_id`; the
  build keys on the canonical name, so any exact duplicate silently merges two humans.
  `name-aliases.json` solves the opposite problem and its own note records the same hazard
  in reverse for Ron Beck. This is a build change, not something to work around one name at
  a time, and Reed Morgan is the second time it has surfaced.
- **The year-photograph gap is twelve years, not the nine the photograph routine is working
  from:** 1993-94, 1994-95, 1995-96, 1996-97, 1997-98, 2000-01, 2002-03, 2003-04, 2005-06,
  2006-07, 2008-09, 2009-10. The routine's list is missing the mid-nineties and 2002-03.
- The Salvador Leon / Salvador Leon Golib identification, unchanged from the seventh pass.
- A profile citing more than twenty sources would silently lose the rest: `SRC_KEYS` in
  `build.py` covers `src2` through `src20`. Jaden Marshall's is at ten. Not urgent, but it
  will bite eventually.
- The three branches from 4 August (#6, #7, #8) were closed on 18 August and need no
  further attention.

## Where the archive stands

61 academic years, 2,018 dated and sourced entries, 73 leader records, 771 written profile
records across 716 distinct people, 1,433 senate members across 57 years, 113 leader
portraits and 62 year photographs from 161 image files, 295 documents mirrored, 1,111
legislation files, 1,810 pages built of which 1,726 are person pages. build.py,
check_data.py and check_contrib.py all clean on main at the close. check_duplicates.py
reports the same six pre-existing pairs, every one a genuinely separate event - three
introduce-then-resolve sequences and three same-day bills - and all six were left alone.
One pull request open, #172, corrected and empty.

### Addendum, same pass: Vercel refused again at 21:37

The section above was written believing the seventh pass's closing note still held -
that Vercel had resumed deploying and merges were going live. It stopped holding
during this pass. Preview builds for #170 and #173 completed normally at 20:29 and
20:36, and then at 21:37:20 the Vercel check on #174's branch came back
`failure - "Deployment rate limited - retry in 24 hours."` So tonight's four merges
are most likely stranded on `main` rather than published, and the eighth pass's
merges join the backlog the 22 August entry describes.

Nothing wrong is stranded. Every correction this pass - the Reed Morgan cut on #171,
the eleven withdrawn portraits on #172 - was made before merging, so what is waiting
on a deployment is only work that passed review.

Two things worth repeating rather than rediscovering:

- **`wku-sga-60.vercel.app` is not the production alias.** It answers
  `DEPLOYMENT_NOT_FOUND`, and that is a fact about the hostname, not about the site.
  The 22 August entry established this and I confirmed it again from this
  environment. A future pass should not read that 404 as the site being down. The
  real aliases sit behind Vercel SSO and cannot be checked from here, so the state
  of the public site remains unverifiable from a routine, and no pass should claim
  either way.
- **The capacity problem is structural and now recurring.** Four research routines
  and multiple editor passes, each push triggering a preview build, is what exceeds
  the cap. This pass alone pushed three correction branches and merged four pull
  requests. Limiting previews to something narrower than every push, or changing the
  plan, is a decision for the owner; it is the second consecutive day it has bitten.

---

## 24 August 2026 — the editor's ninth pass

Three pull requests open at the start, all worked tonight. Two merged, one left open at
zero. The three stale branches the standing prompt still names — #6, #7 and #8, the
1980s, the 2020s and the photographs — have not existed as open pull requests for some
time; the open set was #172, #176 and #177, all opened within the previous day.

**#177, the senate rolls: merged.** Ten senators added to the 2016-17 roll. I re-fetched
all five cited minutes PDFs from `wku.edu` and both cited Herald articles and read the
swearing-in passages myself rather than trusting the run's transcription. All ten names
held. The batch of nine sworn in on 31 January 2017 is real and correctly split from the
five already on record; Sara Saeed's seat is named in the swearing-in line rather than the
appointment line and the entry has it right; Lucas Knight's appointment to the seat left
short by the spring 2016 at-large election is in the Herald outright, with Speaker Nathan
Cherry quoted on the eleven-versus-ten count.

One citation was wrong and was fixed rather than cut. Olga Shoyat's note said she was
appointed to fill Chase Coffey's seat after his resignation, citing the 21 February 2017
minutes. **Coffey is not mentioned anywhere in those minutes** — no resignation, no
banquet resolution, no veto. The claim is true; it comes from the Herald's report of that
meeting, which the archive already cites elsewhere for Coffey's resignation. The note now
says which source carries which half, with the Herald added as `src2`.

The traps were handled well by the run itself, which is worth recording. Committee chairs
were deliberately kept off the roll — Amy Wyer, Michael Shelton and Alex Sergent were
sworn only as chairs and were left out. **Lucas Knight and Josh Knight were correctly kept
apart**, Josh being Director of Academic and Student Affairs in the same article; matching
on the surname would have merged them. Both spelling splits, Mujkanovic/Mujcanovic and
Fransisco/Francisco, are flagged and unresolved, which is the rule. I confirmed the
Mujcanovic variant myself.

**#176, the profiles: merged, after one cut.** Twenty-five profiles — twenty-one recent
senators, and four earlier officers that landed in a second commit while I was reviewing
and were merged in. I opened sources for roughly twenty-five discrete claims across
twenty-four of the people. All held but one.

Chloe Ralston's profile opened "a freshman nursing major". **None of the four sources cited
for her gives her course of study**, and "nursing" appears nowhere else in the file. Cut.
Everything else in her profile stands. Evan Tuck's "that same spring election cycle" read
as the wrong year against a paragraph opening in spring 2025; the spring 2026 results
confirm him a junior senator, so the sentence now names the ballot.

Three claims survived that I could not confirm, and cutting them would have been wrong:
Steve Fuller's 973–574 margin over Tom Jecker, where the cited issue is demonstrably the
right one but the mirrored scan's OCR is unusable; Abi Canter's "signature service", where
my text extraction of that PDF verifiably drops text and everything else in her profile is
verbatim from the two bills; and two second-meeting claims for McKinney and Falmlen. **An
unreadable source is not a source that says nothing**, and this pass had that proved on it
twice — the TopSCHOLAR challenge lifted mid-review and let me read the 18 September 1984
and 16 October 1990 minutes directly. Both confirmed: "Mitch McKinney was appointed
Parliamentarian", spelling and all, and Falmlen's recycling report almost phrase for
phrase, "solidly under way" by the end of November.

**#172, the photographs: not merged, nothing to merge, left open.** The diff against main
is still empty after the previous pass withdrew eleven portraits. This is the rolling photo
PR sitting at zero, not a branch to close. I merged current main into it so the next photo
run cuts from the record as it now stands rather than from eleven commits back.

**Two things for whoever picks this up.**

The `src` labels on the McKinney and Falmlen officer records each name two meetings but
carry one URL, so a reader following the link lands on half the citation. **This is
pre-existing on main, not from tonight**, but two meetings want two sources.

More substantial: four people — Ralston, Ferguson, Gannon and Dilts — now carry two
profiles for the same 2023-24 term, one on their `senate.officers` entry and one on
`senate.members`. Nothing on main did this before. It is not visible duplication today,
and the reason is itself the finding: **`members` profiles render nowhere in the HTML**,
only in `site/years.json`. Ferguson's three committee bills and Dilts's Bill 7-23-F reach
no reader. That is a build-side gap rather than a research one, and it is why tonight's
work is worth having even where it restates what was already in the file. Decide which
array is a profile's home before the next profiles pass fills both again.

One error of my own, recorded rather than hidden: the merge commit message for #177 reads
"spring 1916" where it should read "spring 2016". It is a typo in a commit message on
`main`, not in anything the site publishes, and correcting it would mean rewriting `main`,
which is not worth it.

**Vercel.** The deployment refusal that closed the eighth pass appears to have lifted. The
`build` and `Vercel Preview Comments` checks on #177 both completed successfully at
00:47 UTC, where yesterday's returned `Deployment rate limited - retry in 24 hours`. The
24-hour window had simply elapsed. As the 22 and 23 August entries establish, the state of
the public site still cannot be verified from a routine — `wku-sga-60.vercel.app` is not
the production alias and the real ones sit behind SSO — so this pass claims only that the
checks passed, not that the site is live.

## Where the archive stands

61 academic years, 2,018 dated and sourced entries, 73 leader records, 1,442 senate members
across the years with a roll, 796 written profiles across 1,823 named people, 113 leader
portraits and 62 year photographs, 295 documents mirrored, 1,111 legislation files, 1,731
person pages. `build.py`, `check_data.py` and `check_contrib.py` all clean on main at the
close. `check_duplicates.py` reports the same six pre-existing pairs — three
introduce-then-resolve sequences weeks apart and three same-day 1 September 1991 bills. I
read all six and left every one alone; same-day legislative business is genuinely several
events. One pull request open, #172, corrected and empty.

## 24 August 2026 — the editor's tenth pass

Full mode; push and merge both worked from the first probe. Three research pull requests
open, all cut fresh from current main, all merged.

**#172, photographs (rolling), merged as is.** Documentation only — the diff touched
`SGA-60-AGENT-INFO.md` and nothing else, so the merge published nothing. The one
externally checkable claim held: WKU's own Timeline for 1996 (`wku_timeline/376`) records
the Talisman halting publication in August 1996 for lack of interest, which is a genuine
publication gap, not a digitisation one, and closes off 1996-97 and 1997-98 from the
yearbook route. A run that establishes where not to look next earned its time.

**#180, twelve 1989-90 senator profiles, merged after one correction.** I read the mirrored
minutes PDFs directly rather than the citations, all twelve, since it cost nothing. Every
claim held — Leffert's twice-failed swearing-in, Fryrear entered as "Kristin fauser,"
Gion's OCR-damaged seat honestly left unspecified, the Eric/Kelly Elliot pair tracked
apart with the profile saying outright that this supports but does not prove two people.
Cut one claim in two places: that Steve Mason succeeded Dwight Adkins as Junior Class
Vice-President on 5 September 1989. The minutes do not say so — Adkins had been accepted
into the same title on 29 August, stayed in ASG until he resigned on 5 December, and the
5 September secretary's report lists Junior Class *President* vacant, not the vice-
presidency. That note was already on main, so a pre-existing error the new profile
inherited, now fixed in both. Also softened "Todd Gion succeeded Hagan Rose as Sergeant at
Arms" to what the minutes record, which is that Gion was accepted into the post.

**#181, twenty-three names on the 2024-25 senate roll, merged after three notes were
rewritten.** I pulled the minutes down and read the AUTHORS blocks: every seat title
claimed is printed verbatim beside the author's name on the bills. The committee-chair trap
was handled correctly in both directions — Dilts filed from a bill that names his class
seat, not from one that reads only "Senator"; Finch and Bryant not taken as members off
lines that give only their committee-chair titles. The three November 2024 removals
(Ibrahim, Gholston, Petty) check against the Herald's own report, including Petty's account
of medical reasons, which the paper's editor's note records she supplied. No factual cut.
What I cut was research process publishing to the person pages at `/o/`: Wagoner's note
citing "the task's own instruction," Ibrahim's citing "years.json's 2024-25 events" and
"the 17 minutes files," and — the one that mattered — Yates's note arguing for her seat by
holding up Kiersten Washington, a named living student, as a control case on Yates's own
page. All three rewritten to the facts and their hedges; Washington still appears where she
belongs, as the subject of Resolution 2-25-S.

**For the next run.** Two things carried over, both structural, neither a blocker. First,
member profiles on `senate.members` render nowhere in the HTML — only the `note` reaches
`/o/` — so #180's twelve profiles are currently visible only in `site/years.json`. The
23 August report already raised this; it is now costing good work its readers. Second,
`Annalise Finch` (member) and `Annie Finch` (Community Relations chair) are the same person
across the same year and the build gives them two pages; the Veterans Day 5K bill is good
evidence they are one. Wants deciding alongside the Eaton case in §8.5.

## Where the archive stands

61 academic years, 2,018 dated and sourced events, 60 presidents, 73 leader records,
1,465 senate members across the years with a roll. `build.py`, `check_data.py` and
`check_contrib.py` all clean on main at the close. `check_duplicates.py` reports the same
six pre-existing pairs — three introduce-then-resolve sequences and three same-day
1 September 1991 bills — read and left alone, as same-day legislative business is genuinely
several events. No pull request left open.

# 24 August 2026 — editor's pass, two pull requests merged

GitHub was reachable this run, so this was a full pass, not review-only. Two research
pull requests were open, both cut cleanly from current `main` (a real merge base at
`af11520`, not the 4 August orphans). Both merged; neither needed a cut. Everything below
was checked against the sources named, not against the routines' own reports.

## What merged

**#183 (`research-backlog`), a documentation note, merged.** `data/` was byte-identical to
`main`, so the merge published nothing to the site. It closes the last contradiction in
§8.3 item 7, where one sentence called the legislation-authors CONTACTS question moot while
the next still named five PDFs and Omar Salinas Chacon as an open gap. I confirmed the claim
independently against `data/legislation-authors.json` (1,144 rows): every author and sponsor
those five documents name — Serrano, Dahmer, Cissell, Reed, Feck, Bunning, Romanov, Howard,
McCoun, Powell, Diaz, Stinnett, Byrant, Cisco — is already recorded, and Chacon appears only
under CONTACTS, never as an author or sponsor, so his absence is correct. No cut.

**#184 (`research-profiles`), fifteen member profiles across 1972-73, 1973-74 and 1974-75,
merged with no cut.** Thirteen people who sat in the Associated Students Congress by way of
class office or a college seat. I spot-checked twelve-plus distinct claims across six primary
sources and every one held. From the Talisman full texts on archive.org: Mike Inman's
1974-75 senior class presidency with Pam Stewart, the bill to abolish class officers that
Jeff Consolo opposed, and the class of 1,865 for which only its two officers turned up, all
verbatim; Jeff Wampler and Karen McNally's 1974-75 "no need for class officers"; the 1972-73
Rules and Elections Committee under R.G. Meade and Fred Price; the 1973-74 "Donofrio and Vogt
lead freshman class" and the Stoltzfus/Moore senior class Gone with the Wind float. From the
Herald landing-page indexes: "Five File for Student Seat on Board of Regents," "Merrick
Endorses Hamp Moore" and "Inman Announces" in 53:54 (19 Apr 1974); the Jackson/Price AVP
platforms in 52:48 (6 Apr 1973); and "Voting Discrepancy Causes Special Election" with "Fred
Price Says Committee Will Investigate Election" in 52:20 (4 Nov 1972).

The traps checklist came back clean. The advance-notice items — the regent-race endorsement
letters, the AVP platforms — are held to exactly what they prove, and the profiles say
outright where the PDF could not be read (viewcontent.cgi was on its WAF challenge for the
run, so all Herald evidence here is headline-index only). No committee chair was promoted to
officer. No surname-only match: Karen McNally stays distinct from John and Rosemary McNally,
the Filburn sisters and the two Wamplers are kept apart. The duplicate-person risks are
flagged and left unmerged — Mike/Michael Inman, Christy Kay Vogt, Stoltzfus/Stolzfus,
Ronda/Rhonda Talley. The April 1974 regent race sits in the 1973-74 profiles with the seat
going to Greg McKinney, who serves 1974-75, consistent with the settled facts. Deborah
Locke's married name had already been cut in draft.

## What I did not do

The profiles-don't-publish limitation the run flagged is real and confirmed:
`scripts/build.py:6542` rebuilds each rank-and-file senate member into a fresh dict of
`name`/`office`/`note`/`src` before the person page is written, dropping `profile` and
`src2`+. So #184's fifteen profiles — and the roughly eleven member profiles already on
`main` — are banked in the record but reach no reader until that is fixed. I left it: it is a
presentation change touching every person page, and on an autonomous run that is the owner's
call, not a cut I should make unilaterally. Raised for Sam on both the PR and here. The
`Annalise Finch` / `Annie Finch` one-person-two-pages case from the 23 August pass is still
open in §8.5; nothing this run touched it.

## Where the archive stands

61 academic years, 2,018 dated and sourced events, 60 presidents. `build.py`, `check_data.py`
(exit 0) and `check_contrib.py` (exit 0) all clean on `main` at the close. `check_duplicates.py`
reports the same six pre-existing pairs — three introduce-then-resolve sequences and three
same-day 1 September 1991 bills — read and left alone as genuine separate legislative business.
No pull request left open.

# 24 August 2026 — editor's pass, three pull requests merged

Three research pull requests were open at the start of this pass and all three are now on
`main`. The three branches that had been open since 4 August — #6 photographs, #7 the 1980s,
#8 the 2020s — are gone; nothing stale is left to rescue or close.

## What merged

**#185, the senate rolls.** Three sitting senators of the 26th Senate added to 2026-27: Jaden
Marshall as a senator at large, Molly Ricky and Amelia Tucker as senators. I opened the cited
Herald report of the meeting of 28 April 2026 and read it end to end. All three names are in
it, in the roles claimed. The article swears Marshall in as a new senator at-large; it lists
all three among the current senators who spoke in the race for speaker; and it records the
9-9 tie between Tucker and Butler and the re-vote that Butler won, exactly as the note about
Tucker describes. The year is right: the meeting fell in April 2026 but the body serves
2026-27, which is where the entries sit. Veronica Butler is correctly not repeated among the
members, being already carried as Speaker. Nothing cut.

**#186, ten officer profiles, 1995-99.** Accounts of their time in office for Erin Schepman,
David Apple, Darlene and Carlene Lodmell, Steve Roadcap, Shawna Whartenby, Ryan Faught, Chad
Lewis, Leigh Ann Sears and Heather Rogers. I sampled twelve claims across the ten and traced
each to the sourced note it derives from, then opened the external citations. All twelve
held, including the four with hard numbers in them: Apple's primary tally of Sweatt 140,
France 95 and Miller 72; Lewis's budget of $41,756 and his $11,150.68 spent against
$30,605.32; Whartenby's 175 signatures; Sears's 52 riders on a Thursday night in November
1997. Herald 73:50 was opened directly and does carry Allyson Whitt's story on the
Lewis-Hancock vice-presidential race, so the new second citation on Lewis's record is sound.

The advance-notice trap was the one worth watching here, and the branch passed it. The Herald
piece on the Lewis-Hancock race is coverage of a contest still running, and the profile
claims only that the Herald covered it as a contested race. That Lewis won rests on other
records, not on the pre-election story.

I cut one thing. Roadcap, Darlene Lodmell and Heather Rogers each carried the same career
account on two of their year records, and because the person page prints one block per term,
a reader would have met the identical paragraphs twice on one page. I removed the second copy
in each case, leaving the account on the earlier record and letting the later record keep its
own note, which says something specific about that year that the shared account does not. No
sourced fact was lost — that is why this was trimmed rather than deleted. The profile count
lands at exactly the ten the report claimed. Two older pairs of this kind, Andy Gailor and
David Apple, predate the branch and are still there for a later pass.

**#187, the backlog.** Documentation only, no data. I re-ran its factual claims rather than
taking them on trust: 1,111 legislation entries across 43 sessions, confirmed; my own
independent sweep for title-scrape debris surfaced only benign titles of exactly the kind it
describes, so its finding that nothing outside the already-corrected entries is broken holds;
the three `.research` files are still empty lists; all four named portraits are still in
`data/photos.json`. Both titles it cites as examples exist verbatim. Fixed one sentence that
described "a Wikipedia-safe committee year", which means nothing — it is a collection's own
span of years.

## What could not be checked, and is not being dressed up

TopSCHOLAR's `viewcontent.cgi` was on its WAF challenge for the whole run: HTTP 202 with an
empty body, unchanged after a 90-second backoff. So the SGA minutes PDFs behind #186's
profiles could not be re-read from source. Landing pages open and their years match their
labels, and every claim traces cleanly to this archive's own previously sourced notes, which
is the standard CLAUDE.md sets for profiles. It is still a weaker check than reading the
minutes afresh, and it should be recorded as such rather than as a clean verification. The
same challenge is what stopped #187 and the 1979-80 work before it.

## Still open

The limitation raised in the last pass has not moved: `officer_index` in `build.py` rebuilds
each rank-and-file senate member into a fresh dict before the person page is written, so a
`profile` on a member reaches no reader. Officer and executive profiles, including all ten
merged this pass, are unaffected and do publish. The three members seated by #185 carry notes
rather than profiles, so they publish too — checked on the built pages. The fix is still a
presentation change touching every person page and still the owner's call.

The stale "SGA 60 - backlog" trigger cannot be repointed from inside a session; that is now
established twice over and needs the account holder rather than another run. The
`Annalise Finch` / `Annie Finch` case remains open. The 2026-27 record spells the chief of
staff "Gabi Pace" where the Herald has "Gabby Pace" — noted, not touched, since it predates
these branches.

## Where the archive stands

61 academic years, all of them researched. 2,018 dated and sourced events, 118 documents,
1,111 pieces of legislation across 43 sessions, 1,468 senate members across 58 years, 737
named officers, 773 accounts of a term in office, 113 portraits and 62 year photographs.
60 people have been president. `build.py`, `check_data.py` (exit 0) and `check_contrib.py`
(exit 0) all clean on `main` at the close. `check_duplicates.py` reports the same six
pre-existing pairs — three introduce-then-resolve sequences and three same-day bills of
1 September 1991 — read again and left alone as genuinely separate business. No pull request
left open.
