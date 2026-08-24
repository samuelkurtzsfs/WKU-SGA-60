# Verification of the 24th Senate (2024-25) draft roster: 21 candidates

Every claim in the draft was re-derived directly from the 17 primary-source minutes text
files (not taken on the researcher's word), and cross-checked against `data/years.json`
and `data/name-aliases.json` for name collisions with anyone else in the 60-year archive.

## Result: 19 accept, 2 trim, 0 reject

**Accept (19):** Sophia Bryant, Hannah Evans, Megan Farmer, Ryan Dilts, Savanna Kurtz,
Annalise Finch, Caden Lucas, Van Zing, Jade Ismail, Jakob Barker, Maggie Yelton, Thomas
Pabin, John King, Guan Zhou Sim, Bradley Wagoner, Sydney Rettig, Emaun Riley, Hermes
Olmos, Cayden Bailey.

**Trim (2):** Caroline Yates, Malick Ibrahim.

**Reject (0).**

## Why the 19 hold up

Every bill-authorship citation the draft made was checked against the actual AUTHORS
block printed at the bottom of the relevant minutes file, and every one matched the
seat title claimed, word for word: Bryant ("PCAL Senator"), Evans ("Senator At-Large"),
Farmer ("Senior Senator"), Dilts ("Junior Senator," on Bill 3-25-F only — the earlier
Bill 7-24-F citation correctly carries no seat), Kurtz ("Sophomore Senator," including
the "Savannah" double-h variant), Finch ("Senior Senator"), Lucas ("Mahurin Honors
College Senator," plus a real nomination-and-confirmation record as parliamentarian),
Zing ("Gordon Ford College of Business Senator"), Ismail ("Sophomore Senator" — the
bill's own agenda label and its own printed text disagree on the bill number, 15-24-F
vs 15-22-S, a source-side inconsistency, not a researcher error), Barker ("Freshman
Senator"), Yelton ("Junior Senator," confirmed three separate times), Pabin ("Senator
At-Large"), King ("CEBS Senator," twice), Sim ("Senator At-Large"), Wagoner ("First
Generation Senator," twice, plus the Wagner/Wagoner outlier confirmed exactly where the
draft said it was), Rettig (nomination and swearing-in confirmed verbatim, plus the
Redig/Reddig spelling variants), Riley (nomination and swearing-in confirmed, plus an
already-published Herald article in years.json independently confirming the same fact),
Olmos ("International Senator"), and Bailey ("Freshman Senator").

Three of the resignations the draft flagged in passing — Finch, Rettig ("Reddig"), and
Evans — are confirmed verbatim in the Speaker's 28 January 2025 report: "Senator Finch,
Senator Reddig and Senator Evans all resigned."

No collisions turned up in `data/years.json` or `data/name-aliases.json`. Several
surnames (Kurtz, Farmer, Evans, King) belong to other, clearly different people
elsewhere in the 60-year archive (President Sam Kurtz vs. Senator Savanna Kurtz; a
1981-82 Congress member Tom Farmer; a 1966-67 executive Catlette "Tom" Evans, Jr.; a
1970s election candidate Pam King) — different eras, different first names, no risk of
merging. Several of the 21 candidates turned out to already have independent
corroboration sitting in years.json's existing, Herald-sourced event entries for
2023-24 through 2025-26 (Zing's flag resolution, Riley's ISEC appointment, Lucas's
parliamentarian role, Ismail's fundraising resolutions, Ibrahim's 2023-24 election and
2024-25 removal, Yates's 2025-26 continuation) — none of which the draft researcher had
used, since they worked only from the 17 minutes files.

## The two trims

**Caroline Yates** — real evidence, correctly flagged by the draft as weaker than the
other 19, and I am not downgrading it further. The draft's chain (a full name from a
Graduate Advisory Council appointment, combined with repeated direct "Senator Yates"
address in floor debate with no other Yates in the corpus) holds up, and I found a
fourth instance of direct address the draft missed (2/11/25). More importantly, an
internal-pattern check the task asked for turned up real supporting evidence: Kiersten
Washington, a confirmed non-senator who authored two resolutions in these same minutes,
is never once called "Senator Washington" — showing the corpus reserves "Senator" for
actual members, not as a loose courtesy title. Best of all, an already-published Herald
article already sitting in years.json's 2025-26 events independently calls her "Senator
Caroline Yates," confirming she was a genuine continuing Senate member in a year outside
this research window. The note was rewritten to include this corroboration; the seat
stays unset, since no 2024-25 source states one directly (the Graduate Advisory Council
report reads "No Graduate Senator" the week after her name stops appearing, which hints
at the seat's title without proving she held it).

**Malick Ibrahim** — real evidence, but the draft's note contains a factual error that
needed fixing, not just softening. It claims "Senator Ibrahim" appears in absence lists
"from 24 September 2024 through 4 March 2025." Checking every one of the 17 files, he
does not appear in any absence list after 29 October 2024. The reason is decisive and
was sitting in years.json the whole time: an already-published Herald article, already
cited under 2024-25, reports the Judicial Council voted 7-0 on 6 November 2024 to remove
"Senators Malick Ibrahim, Myricle Gholston and Karisha Petty" for excessive unexcused
absences — naming him "Senator Malick Ibrahim" directly, in full, independently of
anything in the 17 minutes files. A second Herald article already in years.json's
2023-24 events shows he was originally elected a freshman senator in the fall 2023
special election. Net effect: the evidence for Ibrahim holding a Senate seat is
actually stronger than the draft realized, but the note needed the removal fact added
and the inaccurate "through 4 March 2025" claim removed.

## What I did not do

I did not edit `data/years.json`. These verdicts are for the editor who merges this
draft into the record.
