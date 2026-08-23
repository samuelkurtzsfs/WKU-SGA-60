# Senate rolls, 23 August 2026 (scheduled run, second pass this run): six names for 2013-14

Picked up from the run earlier today that closed 1999-00 and 2012-13 and flagged
"2013-14 and other post-2003 years likely have the same kind of headroom" as the
next thing to try. Went straight at 2013-14 rather than the wkuherald.com method,
since AGENT-INFO's own worklist named it directly: "2013-14 (10 members, more
files available under the same trick)" via `wku.edu/sga/legislative/minutes.php`.

## What was pulled

`wku.edu/sga/legislative/minutes.php` links every individual minutes file back to
2009-10 with a plain `<a href>`. Fetched 52 of 53 linked files from
`/sga/uploads/minutes/2013/` and `/sga/uploads/minutes/2014/` (one, `2-10.docx`,
never came back after five attempts spread over several minutes — `curl: (35)
Recv failure: Connection reset by peer` every time; not fatal, just one meeting's
minutes never read). All fetched as `.docx`, text pulled from `word/document.xml`
with no external dependency.

## The trap this run had to work around

The `/2013/` and `/2014/` upload folders are **not** the same thing as the
2013-14 academic year. They are calendar-year folders, and each one straddles
two academic years: the `/2013/` folder holds meetings from January-April 2013
(the tail of 2012-13, Cory Dodds's Senate) as well as August-December 2013 (the
start of 2013-14, Keyana Boka's), and the `/2014/` folder holds January-May 2014
(the rest of Boka's term) as well as September-October 2014 (the start of
2014-15, under Nicki Seay, who by some of these same files is already going by
"Nicki Taylor" — the married-name change CLAUDE.md already documents as a known
case). Filenames give no reliable signal either: `min4-26.docx`, sitting in the
2013 folder, is actually the 24th meeting of the 11th Senate on 16 April
**2013**, not April 2014.

Sorted every file by content instead of filename or folder: extracted the
president's name and the "Nth meeting of the Mth Senate" line from each, and
kept only the ones naming Keyana Boka and the 12th Senate. This is also how
`min4-26.docx`, `min4-2.docx`, `min4-9.docx`, `min3-5/19/26.docx`,
`min2-19/26.docx` and `minutes01-29/2-12/2-15/11-27/12-4.docx` were correctly
excluded as 2012-13 documents parked in the wrong-looking folder, and how the
bare-numeral files in the 2014 folder (`1-27`, `2-3`, `2-18minutes`, `3-3`
through `5-5`, `10-14` through `11-18`, all five `sep*` files) were excluded as
2014-15 documents — every one of them names "Nicki Taylor" or "Nicki Seay" as
president, never Boka.

## What this run found and added

Six names, each checked against the traps this project has been burned by
before (committee chair ≠ officer but IS an established member-record pattern
for this exact year; bill author ≠ member; Org Aid ≠ Senate; "present, but not
on roster" is an explicit negative; don't merge two people sharing a surname).
A separate adversarial verifier subagent, given only the raw excerpts and no
access to this reasoning, was asked to try to refute all seven then-candidates.
It returned 2 clean accepts, 1 thin-but-valid accept, 3 trims, and 1 reject:

- **Chris Costa**, Senator — the verifier accepted straight off two explicit
  "Senator Costa" mentions in floor debate/motions (3 and 10 Sept 2013 minutes).
  Landed instead on the site's own already-published Herald citation (3 Dec
  2013, "senator Chris Costa moved... to revoke SGA's support for a $9 Talisman
  student fee"), since it is the same fact, already vetted, and a cleaner
  permanent URL than the wku.edu docx.
- **Megan Skaggs**, Chair of the Academic Affairs Committee — seven consecutive
  committee-report bylines under her name, Sept-Nov 2013, plus the already-
  published Herald citation calling her "Academic Affairs committee head Megan
  Skaggs." Used that Herald citation as the source.
- **Ashlee Manley**, Chair of the Legislative Research Committee, fall 2013 —
  six consecutive bylines plus a spot filling in as Speaker of the Senate on 8
  Oct 2013. The verifier's one substantive catch on this run: the drafted claim
  said she was "succeeded by Jay Todd Richey on 11 February 2014," but the 11
  Feb minutes only say Richey was appointed to that chair that day — they never
  say Manley left, resigned, or was removed. Trimmed to state only what the
  cited document (3 Sept 2013 minutes) itself shows. She is a different person
  from the already-recorded "Alyson Manley" — both names appear as separate
  lines on the same absence roll, which settles it rather than leaving it to
  guesswork.
- **Mallory Treece**, Chair of the Public Relations Committee, fall 2013 — same
  shape and same trim as Manley: the "succeeded by Nolan Miles" framing was cut
  for the same reason (the 11 Feb minutes name his appointment, not her exit).
- **Mallory Chaney**, Chair of the Campus Improvements Committee, early fall
  2013 only — the verifier's sharpest catch. Only the 3 September 2013 minutes
  actually print her name; a later "this will be my last week" committee report
  (15 Oct) is unattributed in the source and the draft had assumed it was still
  her without textual support. Trimmed to claim only the one dated, named fact.
- **Ashley Presnell**, Senator — a single citation, the same spring 2014
  absence roll as five other senators already on record for this year. The
  verifier flagged it as thin but valid: an absence-roll listing is one of the
  accepted evidence types on its own, and Presnell is not among the roll's
  explicit "present, but not on roster" names (the actual negative signal on
  that same document).
- **Rejected: Taylor Ruby.** The only 2013-14-dated mention has him personally
  moving to suspend the bylaws, with no "Senator" title attached — unlike
  Costa's parallel motion, which did carry the title. Accepting it would also
  require assuming this is the same Taylor Ruby sworn in as a freshman senator
  in September 2012, which the excerpt does not establish either way. Two
  unsupported inferences stacked on one citation was judged too thin.

2013-14 now has 27 members, up from 21. `build.py`, `check_data.py` and
`check_duplicates.py` all pass clean; the six known duplicate pairs are
unchanged and none involve 2013-14.

## What's left

- `2-10.docx` (the 2014 folder) was never successfully fetched this run —
  worth another try, since `wku.edu` has been intermittently flaky on this pass
  the way `viewcontent.cgi` is on TopSCHOLAR, not a fixed block.
- The same content-sorting method (check the actual president's name and
  meeting ordinal in the text, never trust the calendar-year folder or the
  filename) applies directly to 2014-15 and 2015-16, both of which are mixed
  into the same `/2014/` folder under "Nicki Taylor"/"Nicki Seay" and have not
  been swept by this method yet.
- The wkuherald.com full-text method that worked for 1999-00 and 2012-13 was
  not tried against 2013-14 in this run, since the wku.edu minutes gave enough
  headroom on their own; a future pass could still cross-check it for anyone
  the minutes missed.
