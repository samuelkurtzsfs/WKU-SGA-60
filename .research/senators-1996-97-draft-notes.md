# 1996-97 Senate/Congress roll — research notes

All 29 SGA minutes items listed for 1996-97 were fetched and read in full. No 403s
at all across 58 requests (29 landing pages + 29 PDFs), one request at a time, 3
seconds apart. PyMuPDF (`fitz`) extracted usable, if noisy, OCR text from every
PDF. All 29 PDFs verified as starting `%PDF` and mirrored into `data/documents/`
as `1996-97-minutes-YYYY-MM-DD.pdf`; the two dates that carry two indexed items
each (4 Feb and 11 Feb 1997) turned out to be a Congress meeting plus a separate
Executive Council meeting on the same evening — the Executive Council file is
disambiguated as `1996-97-minutes-YYYY-MM-DD-executive-council.pdf`.

**81 candidate rank-and-file members** were drafted to
`.research/senators-1996-97-draft.json`, matching `scripts/merge_senators.py`'s
schema (`year`, `name`, `seat`, `note`, `src` with `label`/`url`/`file`).

## Roll-call format, confirmed

The task's premise — that WKU Congress roll calls this era name only the
*absent* members, so an absence is itself proof of membership — holds for
1996-97, with one wrinkle: the very first meeting of the year (27 Aug 1996) says
"Roll was taken through an attendance sheet signed by those who attended," not a
spoken roll call, so that meeting names no members at all through its roll-call
line. From 3 Sep 1996 on, every one of the remaining 27 Congress meetings uses
the standard "Absences included ..." formula, naming only those missing. The two
Executive Council minutes (4 and 11 Feb 1997) are different in kind: they record
no names at all beyond "all officers were present."

Because the first meeting has no absentee list, its membership evidence comes
entirely from explicit motions, seconds, and the swearing-in language in New
Business — the same category of evidence the task's own trap rules require
regardless of roll-call format.

## What each item actually contains

The template matches 1995-96: Call to Order, Roll Call, Reading of the Minutes,
Officer Reports (President, Vice-President, PR Director, Secretary, Treasurer),
Committee Reports (one line per standing committee, an Academic Council block,
a Council on Organizational Affairs line), Old/Unfinished Business, New
Business, Announcements, Adjournment. From 4 Feb 1997 a few meetings add a
"Special Orders" section for end-of-year award nominations.

Evidence used for membership, in this order of strength: (1) a formal roll-call
*vote* naming who voted for/against/abstained — the strongest evidence in this
run, since several documents explicitly name people by both first and last name
recorded as voting; (2) election/acceptance to a named open seat by unanimous
consent or a Congress vote; (3) the standard roll-call absentee list; (4) a
member moving or seconding a motion by name. A **new caution this year that
1995-96 did not surface**: the 15 October 1996 minutes record President Miller
saying the Marriot Food Service Committee "was looking for one *non-congress*
member," which is direct proof that at least some standing committees in this
Congress accepted volunteers who were not Congress members. That finding raised
the bar for two people whose only apparent evidence was a committee Vice Chair
appointment (Amy Braden, Jason Cole, both accepted as Vice Chairs of Student
Affairs 21 Oct 1996) — both are in the draft anyway, but on the strength of an
independent roll-call *vote* eight days later, not the Vice Chair appointment
itself, which by itself I no longer treat as sufficient.

## Officers found (for `organization.executive`, not `senate.members`)

- **President:** Kristen (Kristen L.) Miller, elected in spring 1996 (she was
  the 1995-96 Public Relations Director per that year's own notes) — presided
  every meeting she is not herself recorded absent.
- **Vice-President:** Carlene Lodmell — presided most meetings in Miller's
  absence.
- **Secretary:** Darlene Lodmell (signs every set of minutes; a different
  person from Carlene Lodmell, both real, both recorded separately throughout).
- **Public Relations Director:** Shawna Whartenby — continuity with 1995-96,
  where she was recorded as PR Co-Chair from 19 Sep 1995.
- **Treasurer:** Steve Roadcap — continuity with 1995-96, where he chaired
  Campus Improvements all year.
- **Coordinator of Committees:** Erin Schepman, elected 27 Aug 1996, replaced
  by Ryan Faught around 21 Jan 1997.
- **Judicial Council Foreman** (judiciary branch, not Congress, so not in the
  members draft): Jeff Yan, serving from the executive retreat over summer
  1996 (confirmed by Rick Malek's question about when Congress approved him,
  24 Sep 1996 — the executive council explained they had approved him at the
  summer retreat since Congress was not in session); succeeded by Erin
  Schepman (nominated 28 Jan 1997, confirmed by a 22-0-5 roll-call vote), who
  was in turn succeeded by Henry White (nominated 11 Feb 1997).
- **Parliamentarian:** Josh Detre, appointed 10 Sep 1996.
- **Sergeant of Arms:** Chad Lewis, appointed 10 Sep 1996.

**1997-98 executive officers, elected 22 Apr 1997 and explicitly belonging to
the following academic year, not this one** (spring elections file forward,
per the project's own rule): President Keith Coffman, Vice President Leigh Ann
Sears, Director of Public Relations Heather Rogers, Secretary Jamie Fite,
Treasurer Chad Lewis. None of these officer titles are recorded against
1996-97; each of these five people is in the 1996-97 members draft only for
their confirmed 1996-97 Congress service, never for the office they were about
to take up.

## Committee chairs (for `organization.senate.committees`)

Fall 1996, announced 27 Aug and confirmed weekly: **Academic Affairs** (David
Apple, all year), **Student Affairs** (Stephanie Cosby, all year; Vice Chair
Jason Cole reported for her when absent from Nov 1996), **Legislative
Research** (Ryan Faught through the fall, then Andy Gailor from ~21 Jan 1997;
Vice Chair Callie Varner from ~18 Feb 1997), **Campus Improvements** (Leigh Ann
Sears, all year), **Public Relations** (Heather Rogers, all year), **Technology**
(Kip Carr, all year — a new committee this year, first reported 24 Sep 1996).
Two further, apparently sub-committee bodies: **By-Laws** (Kip Carr, chaired
from the fall, reporting through the spring) and a **Constitutional
sub-committee** spun out of Legislative Research (Rick Malek, chair from
~18 Feb 1997, rewriting the constitution's Preamble and Article I). Andy Gailor
also served as SGA's representative to the **Bowling Green City Commission**
all year, reported alongside the committees but not itself a standing
committee.

All of the above except Kip Carr are independently confirmed as seated Congress
members by a roll call, an election, or a moved/seconded motion, and are in the
draft with their committee role noted. **Kip Carr's inclusion rests on weaker
ground** than everyone else in the draft: he is repeatedly listed among
meeting "Visitors/Others" rather than the roll call, yet is also repeatedly
nominated for, and on 19 Nov 1996 wins, the "Congress Member of the Month"
award — a title the minutes use in explicit contrast to a separate "Committee
Member of the Month" award for non-Congress committee volunteers. That contrast
is the reasoning for including him; it is a different kind of evidence from
everyone else in this draft and is flagged plainly in his note for the
verifier to weigh.

## Size

No document states a total Congress roster size or seat count. The weekly list
of open positions read into the Secretary's report is long and changes
constantly (it ran to 19 named seats on 25 Feb 1997 alone), implying a nominal
roster well beyond the 81 names recovered here, but backing into a total from
the vacancy list would be inference, not a stated figure, so none is recorded.

## Ambiguous names — kept as separate people, flagged in their own notes

- **Garrett Blincoe / Lance Blincoe** — kept as two different people, not one
  split by OCR: both are named in the *same* absentee sentence on 21 Oct 1996
  ("...Garrett Blincoe, Jeff Oliver, Lance Blincoe, Devon Moore..."), which
  would be impossible if they were the same person misread twice in one line.
- **Leigh Bakken / Luke Bakken** — kept separate for the same reason: both
  vote, on *opposite* sides, in the same 29 Oct 1996 roll-call vote.
- **Matt Bastin / David Bastin** — the harder case. Each first name recurs
  under its own spelling across *multiple, separate* documents (Matt Bastin
  in at least six meetings spanning Aug 1996-Apr 1997; David Bastin in two
  meetings, 3 Dec 1996 and 28 Jan 1997, each time in a formal roll-call vote).
  That repetition across different documents argues against a single-document
  OCR slip, so both are kept as separate people per this project's rule
  against merging by surname alone — but unlike the two cases above, the two
  spellings never appear in the *same* document, so a transcription error
  spanning several weeks' typing cannot be fully ruled out either. Flagged
  explicitly in both entries' notes. The name-aliases.json entry for
  "Matthew D. Bastin" -> "Matthew Bastin" may or may not be either of these
  two people or from this year at all; noted for the editor to check, not
  applied.
- **B.J. Stith** — a single absentee list (23 Nov 1996) spells this "R.J.
  Stith" where every other appearance across the year, including a formal
  roll-call vote, reads "B.J. Stith." Treated as one person with an OCR slip
  on one bad scan (a "B" misread as "R" is far more plausible on this
  document's quality than a second sibling who is never independently
  attested), not merged silently — the variant spelling is recorded in the
  note.
- **Kara Wallace / Kani Wallace** — both spellings appear within the *same*
  single document (29 Oct 1996), a much stronger signal of one typist's
  inconsistency for one person than the Blincoe/Bakken cases above. Kept as
  one entry, both spellings noted.
- **Shawn Wallace / Kara Wallace** — kept as two different people despite the
  shared surname: "Shawn Wallace" appears only on absentee lists in September
  1996, "Kara Wallace" only from 29 Oct 1996 on, the two spellings share no
  letters that would suggest an OCR confusion, and this project's rule against
  surname-only matching applies squarely here. Flagged in both notes as a
  caution, not a claim either way.
- **Julie Gott / Julie Robinson** — two different people (different surnames
  entirely); noted only because both are frequently absent in the same
  meetings and it would be easy to conflate them while skimming.

## Spelling doubts flagged in individual notes (not resolved)

Leigh Ann Sears/"Scars" (a very consistent OCR mis-scan, not a spelling
question), Julie Gott/Gatt, Michael/Micheal Croley, Kirk "FHeeman"/Freeman,
Doug Mory/Mary, Atul/Awl/Alul Patel, Carlton/Carleton Rumienier, Robert
Oslakovic/Oslakovie, Theresa/Teresa Criss, Rachel/Rachael Hendricks, Anne/Ann
Guillory, Curtis Street/Strout/Streut, Aaron Galloway/Gallowy — all read as OCR
noise on one real person, each flagged in that person's own `note` field per
this project's "flag, do not fix" rule. None of these, nor any of the ambiguous
names above, matched an entry in `data/name-aliases.json` (checked
programmatically against every alias key and value).

## Excluded, and why

- **Jeff Yan, Erin Schepman (as Judicial Council Foreman), Henry White (as
  Judicial Council Foreman nominee)** — the Judicial Council is a separate
  branch from Congress, per this project's own trap rules and the 1995-96
  precedent (Jason Martin excluded on the same grounds). Erin Schepman and
  Henry White are still in the members draft, but only on the strength of
  their *other*, independent Congress-member evidence (a moved motion and an
  absentee listing respectively), never their judiciary role.
- **Kit/Kip Tolbert** (Housing staff, mentioned repeatedly as a contact, never
  a Congress member), **Steven Graham's Public Relations award alone**
  (superseded by his later roll-call vote, which is the evidence actually
  used), **Drew Harrell and Kristin Willis's By-Laws sub-committee
  appointment alone** (both are in the draft anyway, but on their later
  independent roll-call absences, not the committee appointment, per the
  Marriot Committee finding above), **Kern [Faye?] Stewart** (an end-of-year
  award nominee whose name is too badly OCR-garbled on 25 Mar 1997 to use
  confidently), **Rick Kempa/Kempe/Kemps** (a repeat visitor and losing
  At-Large candidate, never elected), **Kyle Shrewsbury before 11 Feb 1997**
  and **April Pierce/Curtis Street/Leigh Bakken before their respective
  elections** (all repeat visitors before being elected, counted only from
  their election date), **Donna Key, Kathy Mattingly, Karen White, Tara
  Beard, Rick Kempa, Curtis Strout [as a visitor], Barry Westerman, Magdalena
  Ball, Jason Newland, Charles Lanter, Calitos R., Nicole Laster, Paul
  Thomas, Rob Marty, Rachel Hendrick [as a visitor, before her Feb 1997
  election]** and other named visitors — never elected, never on a roll call,
  never moved/seconded a motion as a member. **Matt Bachelor** (the incoming
  Herald reporter, introduced by name, not a member). **Rob Evans**-style
  outside-body appointments do not recur this year, but the equivalent trap
  is Andy Gailor's City Commission seat, which is an SGA appointment *to* an
  external body, not itself evidence of anything beyond what his own
  independent Congress election already establishes.

## Cross-check against name-aliases.json

Checked programmatically: none of the 81 candidate names match an entry (as
either key or value) in `data/name-aliases.json`. No changed-surname or known
alias case applies to this batch, though the "Matthew D. Bastin"/"Matthew
Bastin" alias pair is flagged above as worth a manual look given the surname
match to this year's Matt Bastin/David Bastin ambiguity.

## What I did not do

- Did not write anything into `data/years.json` — that is for the merge step
  (`scripts/merge_senators.py .research/senators-1996-97-draft.json`) and a
  verifier pass over this draft first.
- Did not build `organization.executive` or `organization.senate.officers`
  entries myself; the officer and committee-chair findings above are handed
  off as candidates for whoever builds those buckets, since this task was
  scoped to rank-and-file members. The two Executive Council minutes (4 and
  11 Feb 1997) are mirrored into `data/documents/` but carry no names beyond
  "all officers were present," so they were not useful for the members draft.
- Did not attempt to resolve the Matt Bastin/David Bastin question further,
  or chase down whether "Matthew D. Bastin" in name-aliases.json is connected
  to either — flagged for a future pass with fresh eyes on the primary
  documents, or for whoever maintains that person's profile elsewhere in the
  archive.
