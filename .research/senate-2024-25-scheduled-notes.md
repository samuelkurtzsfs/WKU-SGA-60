# 24th Senate (2024-25) roster extraction - method and findings

## Method

Read all 17 available Senate meeting minutes files in full, front to back (agenda, officer
and committee reports, university committee reports, bill/resolution debate transcripts, and
the attached bill text with AUTHORS/SPONSORS/CONTACTS blocks). Cross-checked every name found
against:

- the current `organization.senate` record for 2024-25 in `data/years.json` (11 members, 5
  officers, 5 executive, 6 known committee chairs), pulled directly from the file rather than
  from the task's summary, to see exactly how each name is currently recorded;
- `data/name-aliases.json` (no entries matched any name found in this corpus);
- the task's list of traps, applied name by name.

For each candidate, I required one of: (a) a bill/resolution AUTHORS line giving full name and
seat, matching this project's established practice for the 11 already-recorded members; (b) a
nomination-and-confirmation-and-swearing-in sequence naming them in full; or (c) direct,
repeated address as "Senator [Surname]" in floor proceedings where the full name was
independently established elsewhere in the same corpus. Two names (Caroline Yates and Malick
Ibrahim) fall short of a clean version of any of those three and are included but explicitly
flagged as weaker, for the verification pass to accept or reject.

## What I found

**21 candidates**, all newly confirmed to hold Senate seats and not already in the "Members"
array of `organization.senate` for 2024-25. Six of them - Sophia Bryant, Hannah Evans, Megan
Farmer, Ryan Dilts, Savanna Kurtz, and Annalise/Annie Finch - were already in the record, but
only as *committee chairs*; per the project's own trap #1, chairing a committee does not by
itself prove a Senate seat, so finding their bill-authorship credits (which name their Senate
seat directly, e.g. "Megan Farmer, Senior Senator") is the news here, not their existence.
Fifteen are genuinely new names: Caden Lucas, Van Zing, Jade Ismail, Jakob Barker, Maggie
Yelton, Thomas Pabin, John King, Guan Zhou Sim, Bradley Wagoner, Sydney Rettig, Emaun Riley,
Hermes Olmos, and Cayden Bailey are confirmed at the same authorship-or-swearing-in standard
the existing 11 members use; Caroline Yates and Malick Ibrahim are flagged as weaker.

The **richest single meeting** by far was **29 October 2024** (Bill 13-24-F, funding the
Veterans Day 5K). Its AUTHORS block alone named five senators in one shot with full name and
seat - Annalise Finch, Savanna Kurtz, Hannah Evans, Maggie Yelton, and Thomas Pabin - plus
Bill 12-24-F's authors gave Caden Lucas and Jakob Barker their seats the same day, and Bill
14-24-F gave John King his. Second richest was **11 February 2025** (Bill 3-25-F, the SGA
March Madness bill), whose authors gave Ryan Dilts, Hermes Olmos, and Emaun Riley their seats
in one block, alongside two already-known senators (Hadley Whipple, Jax Price). The project's
established practice of treating bill authorship as adequate evidence of Senate membership did
almost all of the real work here; the floor-debate prose mostly confirmed people rather than
introducing them, because the transcripts nearly always use bare surnames ("Senator Bryant,"
"Senator Lucas") once someone's full name has appeared once in a bill's author line.

## The Wagner/Wagoner question

Resolved, tentatively, in favor of one person. "Bradley Wagoner" is named in full, with his
seat ("First Generation Senator"), as a bill author twice (Bill 18-24-F, 19 Nov 2024; Bill
17-25-S, 25 Mar 2025), and "Senator Wagoner" (not "Wagner") is the spelling used in every
absence list and committee-liaison mention across the whole 2024-25 corpus *except* the very
first file, 10 September 2024, which reads "Senator Wagner" in the absence list and gives him
a birthday shoutout the same week. Given sixteen consistent "Wagoner" spellings against one
"Wagner," and no second person of either name ever appearing, I treated this as one senator and
used the fuller/dominant spelling, Bradley Wagoner - but did not silently merge it; the note on
his entry flags the single outlier explicitly, as the task asked.

## Other ambiguous or borderline cases, deliberately left out

- **Garrett Price / "Senator G. Price."** "Garrett Price" is named every single week as the
  Senate's liaison to the Master Plan Committee - a university-committee-report credit, which
  per the task's trap #3 is not proof of a Senate seat on its own. Separately, "Senator G.
  Price" (an initial, not a full first name) appears in two absence lists (17 Sep, 22 Oct 2024)
  and once asking a question in debate (28 Jan 2025). I never found a bill authorship or a
  direct "Senator Garrett Price" statement. The task's rule is explicit that an initial does
  not satisfy "full name attached to Senator," so he is left out, though he is very likely a
  genuine senator and is a strong candidate for a follow-up pass that can find a swearing-in
  or authorship record I missed (or that simply isn't in these 17 files).
- **Sawyer Edmunds.** Named alongside Kaison Barton on the University Athletic Committee for
  several weeks in the fall, then drops out of the reports entirely by mid-October. Pure
  committee-liaison credit, no "Senator Edmunds" anywhere. Left out.
- **"Senator Norman."** Asks questions in debate repeatedly (10/1, 10/22, 11/19, 2/18) but
  never once appears with a first name or initial anywhere in the corpus. Left out per trap #4.
- **Bare-surname absentees never expanded anywhere in this corpus:** Diltz, Gholston, Petty,
  Young. These appear only in absence lists, exactly the pattern the task told me to distrust.
  Left out.
- **"Senator Zim" (19 Nov 2024 absence list) and "Senator Lynn" (same list).** Both appear
  exactly once, in the same absence list, in a file with an unusually high density of
  transcription slips that meeting (e.g. "Morgan Ammons" for the already-confirmed Morgan
  Gammons; "Sentor" for Senator throughout). "Zim" is very plausibly a mis-transcription of
  "Zing" (Van Zing, confirmed elsewhere) and "Lynn" of "Lun" (Ciin Lun, already a recorded
  member) - both surnames are one keystroke off and no other trace of either "Zim" or "Lynn"
  exists anywhere else in the 17 files. I did not add them as new people, and did not silently
  fold them into Zing/Lun either; flagging the likely typo here for whoever reviews this.
- **Kiersten Washington.** Authored Resolution 2-25-S (Gordon Wilson Hall elevators) but is
  never given a "Senator" title or a seat anywhere - reads as an outside student advocate for
  the issue, not an SGA senator. Left out.

## The two flagged-as-weaker entries

**Caroline Yates** and **Malick Ibrahim** are in the draft JSON but explicitly marked weaker
than the other 19, because neither has a bill-authorship line or an unambiguous "Senator [Full
Name]" sentence naming them - see the `note` field on each entry for the specific reasoning.
Both rest on combining a full name from a non-Senate-proving credit (a university committee
appointment for Yates, an Organizational Aid Board membership for Ibrahim) with repeated
direct "Senator [Surname]" usage elsewhere in the same corpus, where no other person of that
surname exists anywhere in the 17 files. I think both are very likely real senators, but they
do not meet the same bar as the other 19 and should get extra scrutiny (or a search of files
outside this set) before being added to `years.json`.

## Resignations noted in passing

The Speaker's report on 28 January 2025 states that Senators Finch (Annalise/Annie Finch),
Reddig (Sydney Rettig), and Evans (Hannah Evans) all resigned. This is useful context for
whoever writes these three up for the record - all three have solid evidence of having held
seats earlier in the year - but I did not attempt to source a reason, date, or successor for
any of the three resignations; nothing in these 17 files says more than the bare fact.

## Files not used for anything beyond corroboration

9/10/24, 9/24/24, 2/4/25, and 2/25/25 mostly confirmed names already established from other
meetings' bill-authorship blocks rather than introducing new ones.
