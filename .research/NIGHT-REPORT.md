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
