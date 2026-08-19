# 1995-96 Senate/Congress roll — adversarial verification

All 18 mirrored PDFs (`data/documents/1995-96-minutes-YYYY-MM-DD.pdf`) were opened with
PyMuPDF and read in full — not sampled, not spot-checked. Every one of the 55 candidate
entries in `senators-1995-96-draft.json` was checked line-by-line against the actual text
of the specific minutes its `src` cites. No digitalcommons.wku.edu access was needed or used.

## Verdict counts

- **Accepted unchanged: 52**
- **Trimmed: 3** (Carlene Lodmell, Julie Gott, Chad Lewis — see below)
- **Rejected: 0**

Every one of the 55 names is a genuine, textually confirmed Congress/Senate member for
1995-96. Nothing in this batch turned out to be a committee chair mistaken for a member, a
bill author mistaken for a seated senator, a guest, or a duplicate. This is a clean batch —
the researcher's stated method (only roll-call absentee lists and explicit "accepted by
acclamation" / "elected" / "voted" seat-filling language count as membership evidence) was
applied consistently and correctly everywhere I checked it.

## The roll-call-format conclusion

All 18 documents follow an identical template: Call to Order, **Roll Call**, Reading of the
Minutes, Officer Reports, Committee Reports, Unfinished/New Business, Announcements,
Adjournment. The Roll Call section never lists a full attendance roster — it lists only
**absentees**, introduced every time by the fixed phrase "Absences included..." or
"Absences include...". I read all 18 roll-call sections (not just the 3-4 the task asked
for a minimum of), and the format never varies.

This is corroborated as a genuine *membership* record, not a generic sign-in sheet, by
several pieces of internal evidence read directly in the text:
- The 29 Aug 1995 minutes state the attendance policy explicitly: "If a Congress member has
  3 unexcused absences they will be sent before Judicial Council," and 10 minutes late
  without notifying Executive Council also counts as an absence — i.e., the roll call is
  tracked against a known roster with real consequences, which only makes sense for seated
  members.
- The minutes several times name someone "Congress member" or "Congress Member" directly
  in Business/Announcements text independent of the roll call (e.g., "Congress Member Joel
  Banashak was voted committee Member of the Month," "Congress member Steve Roadcap was
  voted Congress Member of the Month," "Congress member Rob Carothers drew..."), and every
  one of those people also appears on a roll-call absentee list elsewhere — the two kinds of
  evidence agree with each other everywhere they overlap.
- 19 Sep 1995's roll call lists President Tara Higdon herself as absent, confirming the
  roll call covers seated officers as well as rank-and-file members, i.e., it is a genuine
  membership attendance mechanism, not a list restricted to some other population.
- Guests and non-members are handled with different language entirely and never appear on
  the roll call: Rob Evans ("the Student Representative of CHE," a separate statewide body),
  Jason Martin ("Judicial Council Foreman"), Stephanie McCarty ("Coordinator of Committees"
  and repeatedly "Potter College representative" to Academic Council, a distinct body), and
  Valerie Hadnot (Cultural Diversity chair) are all named repeatedly in the minutes but never
  once appear on a roll-call absentee list across all 18 documents — which is exactly why
  the researcher correctly excluded all four from the draft.

**Conclusion: the roll call is a bona fide record of Congress/Senate seat-holders being
checked for attendance. A person named absent on it is a confirmed member.** The
researcher's core method holds up under scrutiny.

## The two flagged surname-ambiguity pairs

- **Charles Carneal / Brad Carneal.** Grepped every occurrence across all 18 files:
  "Charles Carneal" is absent 10 Oct, 24 Oct, and 14 Nov 1995 (all fall); "Brad Carneal" is
  absent 16 Jan, 23 Jan, and 13 Feb 1996 (all spring). The split between the two names is
  perfectly clean along the fall/spring line, and no document ever gives a class year, hall,
  or any other identifying detail that would let a reader tell whether this is one person
  whose first name got mis-transcribed at the semester break or two different people who
  happen to share a surname. **The researcher's call — one draft entry, explicitly flagged
  as unresolved rather than silently merged or split — is the correct one.** I could not
  resolve it either, and neither should a reader be told it's settled.
- **Lance Barnhouse / William Barnhouse.** Same check: "Lance Barnhouse" is accepted as a
  Senior Off-Campus representative once, 24 Oct 1995; "William Barnhouse" is separately
  listed absent 28 Nov 1995 and 23 Jan 1996. No overlap, no distinguishing detail either way.
  **Same treatment is correct: one entry, flagged, not resolved.**

## OCR/spelling-variant clusters — resolved spelling per the document

| Name | Draft's chosen spelling | Verdict | Evidence |
|---|---|---|---|
| Rob Carothers | Carothers | **Confirmed correct** | "Carothers" appears 5 times (2 Oct x2, 28 Nov, 30 Jan, 13 Feb) vs. "Crouthers" once (29 Aug, original seating) and "Carouthers" once (10 Oct). Majority and clearest spelling. |
| Joel Banashak | Banashak | **Confirmed correct** | "Banashak" appears in 2 Oct (x2) and 10 Oct, all clean; only the 5 Sep original announcement has the OCR-garbled "Banshek." |
| Julie Gott | Gott | **Confirmed correct as primary**, note corrected | Original 29 Aug seating and 30 Jan roll call both read "Gott" cleanly; 31 Oct and 27 Feb read "Gatt." The draft's note wrongly attributed the "Gatt" misspelling to 30 Jan as well as 31 Oct/27 Feb — 30 Jan actually reads "Gott." Trimmed. |
| John Yeric | Yeric | **Confirmed correct** | Original 29 Aug seating reads "Yeric" cleanly; only 19 Sep reads "Yenc." |
| Andrew Gailer | Gailer | **Confirmed correct** | Original 13 Feb acceptance reads "Gailer" cleanly; only 5 Mar reads "Gaitor." |
| Samuel/Sam/Smauel Faught | Samuel Faught | **Confirmed correct** | Original 16 Jan acceptance reads "Samuel Faught" cleanly; "Smauel" (27 Feb) is a transposition typo, "Sam" (5 Mar) an informal short form. |
| Joni/Jorn Flowers | Joni Flowers | **Confirmed correct** | Three of four appearances (14 Nov, 28 Nov, 27 Feb) read "Joni"; only 5 Mar reads "Jorn" (OCR). |
| Andy/Andi Spears | Andy Spears | **Reasonable, unresolvable further** | First appearance (23 Jan) reads "Andy"; second (13 Feb) reads "Andi." No anchor exists to call one definitively correct; draft's choice of the first-seen spelling is a defensible default and is left as is. |

None of the eight clusters, nor any flagged variant, matches an entry in
`data/name-aliases.json` — confirmed by direct inspection of that file's 32 pairs, none of
which involve any 1995-96 name.

## Trims — what was cut and why

1. **Carlene Lodmell** — note claimed she was "reported as Education College representative
   14 Nov 1995 **and 16/30 Jan 1996**." The 16 Jan 1996 minutes' Academic Council section
   reads "Education College--No report," with no name attached at all. Only 14 Nov and 30
   Jan actually name her in that role. Trimmed the 16 Jan claim out of the note; the
   membership finding itself (Sophomore Off-Campus seat, LRC chair, 2 Oct absence) is
   untouched and fully supported.
2. **Julie Gott** — note claimed the 30 Jan 1996 roll call recorded her as "Julie Gatt." It
   does not; the 30 Jan document reads "Julie Gott" correctly. The misspelling "Gatt" only
   actually occurs on 31 Oct 1995 and 27 Feb 1996. Corrected the note accordingly.
3. **Chad Lewis** — note claimed "does not reappear in any later minutes read." He does: the
   10 Oct 1995 roll call lists him absent by name. This is not an overclaim to cut but an
   undercount to fix — the correction actually strengthens the entry (two independent
   confirmations of membership instead of one) rather than weakening it, so it is filed as
   a trim (note corrected) rather than a rejection.

I also verified, and did not change, one adjacent case that could have looked like the same
kind of error: Jason Loehr's note lists him absent "19 Sep and 24 Oct 1995" but omits a
third confirmed absence on 10 Oct 1995 visible in that day's roll call. This is a strict
undercount, not a false claim — everything stated is true — so it did not need a trim under
this project's rule (narrow overclaims; an incomplete-but-true note is not an overclaim).
Left as accepted, unchanged, per the letter of the verification task.

## Why zero rejections

Every one of the 55 names is independently confirmable as a seated Congress/Senate member
by at least one of: an explicit "accepted by acclamation" / "elected" / "voted... by
unanimous consent" seat-filling vote, or a roll-call absentee listing (itself established
above as a genuine membership record). Where a person's note also mentions a committee
chairmanship or an award, that fact is always additional to — never the sole basis for —
their inclusion, matching this project's own trap rule that a committee chair is not
automatically an officer or member. The researcher's exclusions (Mary Farrar, Stephanie
McCarty, Heather Rogers, Rob Evans, Jason Martin, Valerie Hadnot, and the contest
entrants/winners Matt Hall, Charbonnee LaBelle, Eva Farrar) were all independently checked
against the same 18 documents and are correctly excluded — none of them appears on a roll
call or in a seat-filling vote anywhere in the record.

## What remains open

The Carlene/Darlene Lodmell "twin sisters both reported as Education College representative"
conflict (14 Nov 1995 and 30 Jan 1996 name Carlene; the 10 Oct 1995 election explicitly
elected Darlene) is a genuine documentary contradiction, not a research error, and neither
the draft nor this check attempts to resolve it — it is left flagged in both leaders' notes,
as the draft already had it, which is the right editorial call per this project's rule
against silently reconciling sources that disagree.

The Charles/Brad Carneal and Lance/William Barnhouse pairs remain genuinely unresolved for
the same reason: nothing in any of the 18 documents supplies the detail that would settle
either one, and no future re-read of these same 18 minutes will change that — resolving them
would require a different source entirely (a photo caption, a yearbook roster, or similar).
