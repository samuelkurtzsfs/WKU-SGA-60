# 1995-96 Senate/Congress roll — research notes

All 18 SGA minutes items listed for 1995-96 were fetched and read in full. No 403s,
no blocked PDFs — every item's landing page and PDF loaded on the first attempt at
the standard pace (one request at a time, 3s apart). PyMuPDF (`fitz`) extracted
usable, if noisy, OCR text from every PDF. All 18 PDFs verified as starting `%PDF`
and mirrored into `data/documents/` as `1995-96-minutes-YYYY-MM-DD.pdf`.

**55 candidate rank-and-file members** were drafted to
`.research/senators-1995-96-draft.json`, matching `scripts/merge_senators.py`'s
schema (`year`, `name`, `seat`, `note`, `src`).

## Item-date correction

The task's index gives item **128** as **1995-09-09**. The document at that item
is headed "MINUTES OF THE STUDENT GOVERNMENT ASSOCIATION ... **SEPTEMBER 19,
1995**" throughout, and its content sits correctly between the 12 Sep and 26 Sep
meetings (open positions lists, committee reports, roll call absences all follow
in sequence). The other 17 items' internal dates all matched the index exactly.
This is very likely a data-entry slip in `minutes-index.json` (09-09 for
09-19), not a wrong item number — WKU SGA met on Tuesdays that fall, and 9 Sep
1995 was a Saturday, while 19 Sep 1995 was a Tuesday, consistent with every other
meeting date in the run. **The draft file and the mirrored PDF both use the
document's own date, 1995-09-19**, not the index's 1995-09-09. Flagging this for
whoever reconciles `minutes-index.json` against the archive.

## What each item actually contains

Every 1995-96 meeting's minutes follow the same template: Call to Order, Roll
Call (which lists only the **absentees** by name, never a full attendance list),
Reading of the Minutes, Officer Reports (President, Vice-President, PR Director,
Secretary, Treasurer), Committee Reports (one line per standing committee plus
four "Academic Council" college slots and a Council on Organizational Affairs
line), Unfinished/New Business, Announcements, Adjournment. There is no
membership roster or seating chart in any of the 18 documents — the roll call's
absentee list, and the explicit "accepted by acclamation" / "elected" / "voted"
seat-filling language in New Business, are the only two ways the minutes name a
person as a seated member. I built the draft strictly from those two kinds of
evidence, per the task's own membership rule.

## Officers found (for `organization.executive`, not `senate.members`)

- **President:** Tara Higdon (elected before the record starts; presided all
  year except 19 Sep 1995 and 13 Feb 1996, when she is herself listed absent).
- **Vice-President:** Jeff(ery) Yan — OCR renders the surname as "Yan" in most
  documents and "Van" in a handful of others (130, 126, 127) within the same
  documents that elsewhere spell it "Yan"; "Yan" is very likely correct (it is
  also how the flag-design credit line spells it, 14 Nov 1995 minutes) but flag
  the "Van" spelling as unresolved OCR noise, not a second person.
- **Public Relations Director:** Kristen Miller, retitled "Director of Public
  Relations" in the minutes from 13 Feb 1996 on.
- **Secretary:** Erin A. Schepman (signs every set of minutes).
- **Treasurer:** Brandon Rucker.
- **Coordinator of Committees:** Stephanie McCarty — this reads as a distinct
  executive-level role coordinating the committee chairs (collects their
  reports, calls chair meetings), separate from her repeated appearance as
  "Potter College representative" in the Academic Council committee-report
  slot. She never appears on a roll-call absentee list, so I did not add her to
  the members draft; she is a candidate for `organization.executive` instead,
  if a source elsewhere confirms the title.

## Committee chairs (for `organization.senate.committees`)

Academic Affairs (Terra Swanson through Aug, then David Apple from 2 Oct),
Student Affairs (Darlene Lodmell all year, with a single appearance by
Stephanie Cosby chairing on 13 Feb 1996 that does not recur), Legislative
Research (Carlene Lodmell all year), Campus Improvements (Steve Roadcap all
year), Public Relations (Cindy Chiapetta at the very start, then "Co-Chair"
Shawna Whartenby from 19 Sep on), Programming (Jason Loehr all year), Cultural
Diversity (Valerie Hadnot through 14 Nov 1995, then Margaret Carter from 23 Jan
1996). All of the above except Valerie Hadnot are independently confirmed as
seated Congress members (roll call or an elected/accepted seat) and are in the
draft with their committee role noted. **Valerie Hadnot is deliberately left
out of the members draft** — she chairs Cultural Diversity in every report from
29 Aug through 14 Nov 1995, but never once appears on a roll-call absentee list
or in a seat-acceptance vote across all 18 documents, and per this project's
own rule a committee chairmanship alone does not establish Senate/Congress
membership.

## Size

No document states a total membership size or Congress roster count. The
Secretary's weekly "open positions" announcements (a running list of vacant
Hall, Off-Campus, Non-Traditional, Freshman Council and Graduate School seats)
imply a much larger nominal roster than the 55 names recovered here, but I did
not attempt to back into a total from the vacancy counts — that would be
inference, not a stated figure.

## Ambiguous names left out or flagged rather than merged silently

- **Charles Carneal / Brad Carneal** — absent under "Charles Carneal" in the
  fall (10, 24 Oct; 14 Nov 1995) and under "Brad Carneal" in every spring
  document (16, 23 Jan; 13 Feb 1996). Kept as **one** draft entry (per this
  project's rule against inventing two people from one surname) but the note
  flags the inconsistency explicitly rather than asserting they're the same
  person.
- **Lance Barnhouse / William Barnhouse** — "Lance Barnhouse" is accepted as a
  Senior Off-Campus representative 24 Oct 1995; "William Barnhouse" is absent
  28 Nov 1995 and 23 Jan 1996. Same treatment: one entry, flagged, not merged
  as fact.
- **Mary Farrar** — announced as Ogden College representative to Academic
  Council 29 Aug 1995, and never appears again in any of the 18 documents (no
  roll-call absence, no seat vote). Left out entirely: a single appointment
  announcement with zero later corroboration is exactly the kind of role the
  task's own rules say not to infer membership from.
- **Stephanie McCarty** — see Officers above; left out of the members draft on
  the same reasoning as Mary Farrar (never on a roll call), and because her
  role reads as executive/coordinator rather than a Congress seat.
- **Heather Rogers** — named Committee Member of the Month 5 Mar 1996. Left out
  entirely: committee membership, even an award for it, is explicitly not
  Congress/Senate membership per this project's trap rules, and she does not
  appear on any roll call.
- **Rob Evans** — named in the President's report 14 Nov 1995 as "the Student
  Representative of CHE" (the state Council on Higher Education, a different,
  state-wide body). Excluded: not a WKU SGA Congress seat.
- **Jason Martin** — "Judicial Council Foreman," thanked for Homecoming work 2
  Oct 1995. Excluded: the Judicial Council is a separate branch from Congress.
- **Matt Hall, Charbonnee LaBelle, Eva Farrar** — named only as contest
  entrants/winners ("SGA Free Parking Spot," "President for a Day"). Excluded:
  not officeholders.

## Spelling doubts flagged in individual notes (not resolved)

Rob Carothers/Crouthers/Carouthers, Joel Banashak/Banshek, Julie Gott/Gatt,
John Yeric/Yenc, Andrew Gailer/Gaitor, Andy/Andi Spears, Samuel/Sam/Smauel
Faught, Joni/Jorn Flowers — all read as OCR noise on one real person across
badly-scanned photocopies, each flagged in that person's own `note` field with
every spelling seen, per this project's "flag, do not fix, spelling doubts"
rule. None of these matched any entry in `data/name-aliases.json`.

## Cross-check against name-aliases.json

None of the 55 candidate names, nor any of the flagged variant spellings, match
an entry in `data/name-aliases.json`. No changed-surname or known-alias case
applies to this batch.

## What I did not do

- I did not write anything into `data/years.json` — that's for the merge step
  (`scripts/merge_senators.py .research/senators-1995-96-draft.json`) and the
  verifier that should run over this draft first.
- I did not attempt `organization.senate.officers` or
  `organization.executive` entries myself; the officer/committee-chair
  findings above are handed off as candidates for whoever builds those
  buckets, since this task was scoped to rank-and-file members.
- I did not chase the Academic Council or Council on Organizational Affairs
  structures beyond noting who occupied them, since neither reliably
  demonstrates Congress/Senate membership on its own.
