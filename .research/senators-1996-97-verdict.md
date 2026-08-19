# 1996-97 Senate/Congress roll — adversarial verification

All 29 mirrored PDFs in `data/documents/1996-97-minutes-*.pdf` were opened directly with
PyMuPDF and read in full (not skimmed from the researcher's summary). Every one of the 81
candidate entries in `.research/senators-1996-97-draft.json` was checked against the specific
document its own `src` cites; where a note made a claim about a second document (an OCR
variant, a later committee change, a seat move), that second document was opened too.

**Result: 76 accepted as drafted, 4 accepted with a trimmed `note`/`seat` (one name change
touched two entries), 1 rejected. 80 of 81 entries survive**, written to
`.research/senators-1996-97-checked.json` in the original schema
(`year`/`name`/`seat`/`note`/`src`), `src.file` still pointing at the local mirror.

## Rejected (1)

**Kip Carr.** The draft included him on the strength of a committee chairmanship (Technology),
a bill sponsorship (Resolution 96-6-F), an unusual amount of floor activity, and above all his
19 Nov 1996 "Congress Member of the Month" award — a title the researcher's own notes flagged
as the strongest evidence available, "since several documents explicitly name people ... voting."

Reading every meeting he appears in overturns that: the roll-call header of every single
Congress minutes he is named in — 24 Sep, 1 Oct, 8 Oct, 15 Oct, 21 Oct 1996, 28 Jan, 4 Feb,
18 Feb, 11 Mar, 1 Apr, 8 Apr, 15 Apr 1997 — lists him under **"Visitors"** or **"Others,"**
never once on the absentee roll among seated members. This is not one bad week; it is the
consistent, year-long classification the minutes themselves apply to him, including weeks
*after* other people who started as visitors (Leigh Bakken, April Pierce, Tracy Guthrie, Amy
Wilson) had already won seats and moved onto the absentee list — Carr never makes that move.
The "Congress Member of the Month" title turns out not to be decisive either: a 1995-96 minutes
document (`data/documents/1995-96-minutes-1995-10-10.pdf`, read for comparison) records the
*parallel* "Committee Member of the Month" award going to a person the same sentence calls
"Congress Member Joel Banashak" — so the two award names do not reliably separate members from
non-member committee volunteers the way the draft's note assumed. Weighed against his direct
and repeated "Visitor"/"Other" classification, the award is not enough. This is exactly the
trap the task brief named: a committee chair (and here, a committee chair who was also a bill
sponsor and an award winner) is not automatically a seated member, and the minutes' own
attendance bookkeeping says he was not one.

## Trimmed (4 entries, 5 notes touched)

1. **Rick Malek** (27 Aug 1996) — the note said he "seconded" a motion that evening. He did
   not: the minutes show he **moved** the motion to table the budget vote (Andy Spears
   seconded it). Corrected the verb. The membership evidence itself — a named mover of a
   motion — is unaffected.

2. **Leigh Bakken** and **Luke Bakken** — the draft's notes on both entries claimed the two
   "vote on opposite sides of the same 29 Oct 1996 roll-call vote," offered as the proof they
   are two different people. Rereading that vote: both names are listed in the **same**
   ("against") column, not opposite ones — the claim is simply wrong. The underlying
   two-person conclusion still holds, just not for that reason: both names appear separately,
   as two distinct absentees, in the 23 Nov 1996 roll call, which is real and sufficient
   evidence against an OCR split of one person into two. Both notes were rewritten to drop the
   false claim and cite the real evidence.

3. **Amy Braden** — the note said she was "nominated and accepted as Vice Chair of the Student
   Affairs committee" on 21 Oct 1996. The minutes for that date nominate **Jason Cole** as Vice
   Chair and **Amy Braden as Secretary** of Student Affairs, in the same paragraph — a
   conflation between the two committee posts. Corrected her title to Secretary. Her Congress
   membership is unaffected: it rests on the independent 29 Oct 1996 roll-call vote (she is in
   the "against" column), which was read and confirmed directly.

4. **Keith Coffman** — the note said he was "appointed Sergeant of Arms 10 Sep 1996." The 10
   Sep 1996 minutes appoint **Chad Lewis**, not Coffman, to that post ("the appointed positions
   of Parliamentarian and Sergeant of Arms to be filled by Joshua Detre, and Chad Lewis
   respectively"). Coffman does have a real, later Sergeant of Arms nomination — 11 Feb 1997 —
   but the retrieved text of that meeting states only that Vice President Lodmell nominated him
   and that it "will be approved in New Business"; the New Business paragraph itself does not
   contain an explicit confirming vote in the copy read here. Rather than re-date an unconfirmed
   claim, it was dropped; his entry now carries only the solidly confirmed 3 Sep 1996 Junior
   Off-Campus election.

## The 27 August 1996 attendance-sheet meeting

Confirmed as the researcher described. The minutes read: "Roll was taken through an attendance
sheet signed by those who attended," not a spoken roll call — so the meeting names no absent
members at all. Membership evidence for that date comes only from the New Business record of
motions and seconds (Heather Rogers, Stephanie Cosby, Erin Schepman, Rick Malek, David Apple,
Ryan Faught, Andy Spears, Gina Raffaelli named individually moving or seconding) and the
swearing-in language ("The Congress members that were elected last year were sworn in by
Judicial Council Foreman, Jeff Yan"). All four entries citing this date (Rick Malek, Gina
Raffaelli, Heather Rogers, Erin Schepman) check out against that record (Malek's note corrected
above). Every other meeting from 3 Sep 1996 onward uses the standard "Absences included ..."
formula naming only those missing, confirming the absentee-equals-membership convention holds
for all 27 remaining Congress meetings this year, not just a subset. Spot-checked directly
(full text read, not summary) at 09-03, 09-10, 09-17, 09-24, 10-01, 10-08, 10-15, 10-21, 10-29,
11-13, 11-19, 11-23, 12-03, 1997-01-21, 02-04, 02-11, 02-18, 02-25, 03-04, 03-11 — twenty
separate meetings, well past the requested 4-5.

## Ambiguous-pair resolutions

- **Garrett Blincoe vs Lance Blincoe** — kept as two people. Confirmed twice: the 21 Oct 1996
  absentee list reads "...Garrett Blincoe, Jeff Oliver, Lance Blincoe, Devon Moore..." and the
  29 Oct 1996 list repeats the same pattern ("...Garret Blincoe, Jeff Oliver, Lance Blincoe,
  Devon Moore..."), each time with a third name (Jeff Oliver) sitting between the two Blincoes.
  A single name misread twice by OCR would not produce that separation twice on two different
  dates. Garrett Blincoe is also independently absent alone on 17 Sep 1996; Lance Blincoe is
  independently elected Junior Off-Campus representative alone on 1 Oct 1996. Two real people.

- **Leigh Bakken vs Luke Bakken** — kept as two people, but not for the reason originally
  given (see Trims, above). Real evidence: both are named separately in the 23 Nov 1996
  absentee list ("...Luke Bakken, Garret Blincoe, Lance Blincoe, Devon Moore, Henry White, Kara
  Wallace, Julie Robinson, Sarah Cox, Brice Boyer, Kristin Willis, Josh Detre, Stephen Barnett,
  Leigh Bakken, B. J. Stith and Jason Wong"), with eleven other distinct names between them.
  Leigh Bakken is also independently a visitor-then-At-Large-representative from 8 Oct 1996;
  Luke Bakken is independently absent alone on 21 Oct 1996 before that date. Two real people.

- **Matt Bastin vs David Bastin** — kept as two people, matching the researcher's hedged call.
  "Matt Bastin" recurs constantly across the *entire* year (at least eleven separate documents,
  Aug 1996 through Apr 1997, moving motions, seconding, and voting). "David Bastin" appears in
  exactly two documents, each a formal roll-call vote naming him individually alongside many
  independently-confirmed people: 3 Dec 1996 ("Those voting in favor were: ... David Bastin,
  Josh Detre, Steven Graham...") and 28 Jan 1997 ("Those voting in favor were: ... David Apple,
  Jason Cole, David Bastin, Jeffrey Porter, Steven Graham...") — eight weeks apart, in two
  independently-typed sets of minutes, with "Matt Bastin" never appearing in either of those
  same two documents. Two formal roll-call appearances eight weeks apart is weak evidence for
  a random OCR slip (image-level misreads do not usually repeat identically on different scans
  eight weeks apart); it is at least as consistent with a real second person. Kept apart, both
  notes' hedged uncertainty left as drafted. Incidental finding for the editor, not applied
  here: `data/years.json` already carries a "Matthew Bastin" as **1998-99 vice president**, two
  years after this year's Matt Bastin — a plausible continuity (rank-and-file member becomes
  VP) worth checking on a future pass, but out of scope for a rank-and-file roll and not
  asserted in either entry.

- **B.J. Stith vs "R.J. Stith"** — treated as one person, an OCR slip. "B.J. Stith" is the
  spelling on his 21 Oct 1996 election to the Barnes-Campbell seat ("The new representative is
  BJ Stith") and on the 29 Oct 1996 roll-call vote ("...Curtis Street, and B.J. Stith" voting in
  favor). Exactly one document, the 23 Nov 1996 absentee list, reads "R.J. Stith" instead, and
  no second "R.J. Stith" ever recurs anywhere else in the run. Confirmed as drafted.

- **Kara Wallace vs "Kani Wallace"** — treated as one person, an OCR slip. Both spellings
  appear within the *same* 29 Oct 1996 document: "Kani Wallace seconded the motion" earlier in
  New Business, and "Kara Wallace" later in that evening's roll-call vote. One typist,
  inconsistent within a single sitting, is far more plausible than two people who happen to
  share a document. Confirmed as drafted.

- **Shawn Wallace vs Kara Wallace** — kept as two people. "Shawn Wallace" appears only on
  September 1996 absentee lists (10 Sep, 17 Sep, 24 Sep); "Kara Wallace" first appears 29 Oct
  1996 and continues into 1996-97's Perfect Attendance list (3 Dec 1996, "Kara Wallace" named
  alongside Ryan Faught, Jamie Fite, Jason Cole, David Bastin, Steven Graham). The two spellings
  share no letters that would suggest a single OCR confusion, and the project's rule against
  surname-only matching applies. Confirmed as drafted.

## Other things checked and confirmed, not previously flagged

- No entry in this batch matches any key or value in `data/name-aliases.json` — verified
  directly against the file's contents, not just the researcher's own claim of having checked.
- No one in the surviving 80 is a 1997-98 officer-elect wrongly credited with 1996-97
  membership: the 22 Apr 1997 election minutes were not used as a source for any entry in the
  draft, and the five people who do go on to 1997-98 executive office (Keith Coffman, Leigh Ann
  Sears, Heather Rogers, Jamie Fite, Chad Lewis) are each sourced here only to their confirmed
  1996-97 Congress activity, exactly as the researcher's notes describe.
- Josh Detre (Parliamentarian) and Chad Lewis (Sergeant of Arms) were double-checked because
  the researcher's own notes list them under "officers... for `organization.executive`, not
  `senate.members`," which reads as an internal contradiction with their presence in this
  members draft. Reading the record resolves it: both are independently named on multiple
  Congress absentee/roll-call lists across the year on top of their appointed titles (Detre
  absent 13 Nov and 23 Nov 1996, voting 3 Dec 1996 and 28 Jan 1997; Lewis absent 17 Sep and 29
  Oct 1996, voting 3 Dec 1996 against) — so their Congress membership is independently
  supported and their inclusion here stands, unchanged.
- Julie Gott vs Julie Robinson: confirmed as two distinct people with stronger evidence than
  the draft's note stated — both names appear together, separately, in the same 29 Oct 1996
  absentee list ("Julie Gatt... Julie Robinson"), which the original note did not cite.
- All seat/committee/election claims tied to a specific date in the surviving 80 entries were
  matched word-for-word against that date's document: Amy France/Anne Guillory/Robert
  Martin/Randall McGraw/Jeffrey Porter's shared 21 Jan 1997 unanimous-consent seating; Theresa
  Criss/Tara Logsdon/Kyle Shrewsbury/Robert Oslakovic's 11 Feb 1997 seating; Tracy Guthrie/Rachel
  Hendricks' 4 Feb 1997 seating; Carlton Rumienier's 3 Dec 1996 seating; Scott Self's 13 Nov 1996
  introduction and unanimous approval; Amy Wilson's 25 Feb 1997 acclamation; Laura Hancock's
  4 Mar 1997 At-Large seating; Callie Varner's 18 Feb 1997 LRC Vice Chair post; Andy Gailor's
  15 Oct 1996 LRC Vice Chair post and 21 Jan 1997 Chair promotion; Ryan Faught's 21 Jan 1997
  Coordinator of Committees move; Kristin Willis's and Drew Harrell's 15 Oct 1996 By-Laws
  sub-committee appointment. All matched.

## Files

- `.research/senators-1996-97-checked.json` — 80 surviving entries, original schema, `src.file`
  pointing at the local PDF mirror.
- `data/years.json` was not touched. Merging is a separate step.
