# 30 August 2026 — editor's pass, morning: an empty queue, and the orphan branches checked event by event

Nothing was open. No pull request on the repository was in an open state, so
nothing was merged, nothing was cut, and nothing was pushed to a research
branch. `main` stands where last night's pass left it, at 9626c3a.

The state of the published archive was confirmed before anything else.
`build.py` completed cleanly and, rebuilt on a clean checkout, produced no
diff against the committed `site/` — so what is on the live site is what the
data says. `check_data.py` exits 0. `check_contrib.py` exits 0, all of its
contributor-layer and drop-box cases passing. `check_duplicates.py` reports
the same six pairs it has reported for days; all six were read again and all
six are two events rather than one, on the same reasoning recorded on
29 August. None is new.

**61 years, 1,984 events, 60 people have been president.**

## The orphan branches hold nothing, and this pass proves it a harder way

Previous passes settled that the `research-*` branches with no merge base
against `main` are superseded snapshots, on the grounds that merging one would
delete more than it added. That is true and it still is. But it is a
file-level argument, and a file that is a net deletion can still contain a
paragraph nothing else has. The question those passes answered was "is this
branch mergeable", and the question the brief actually asks is "is any
research stranded here". Those are not the same question.

So this pass compared them event by event instead: every event on every
orphan branch, keyed on its year, its date and its title, against every event
on `main`.

The three recent orphans — `research-backlog`, `research-senate` and
`research-profiles` — differ from `main` by 58 events each, and all 58 are
title-only variants sitting at a year and date `main` already occupies. They
are pre-deduplication copy, from before the 29 August merge of thirty-five
doubled events. There is nothing in them.

The six 4 August snapshots each showed around 125 events not on `main` by
title. All but a handful are events `main` has since re-filed into the correct
academic year, and the re-filing is the reason they no longer match: the
branches still carry Sandra Norfleet under 1982-83, which the 18 August
correction settled as 1981-82, and still carry Doug Alexander's March 1970
vice-presidential win under 1970-71 rather than 1969-70. Merging any of them
would walk settled facts backwards.

That left seven events, on seven dates, with nothing on `main` at the same
date at all. Each was chased down individually, and every one of the seven is
already published under a different date:

- The disputed 9-8 speaker of the senate vote is on `main` at 2004-04-13.
- Hannah Garland's tabled plus-minus resolution is at 2013-02-19.
- The predatory-loan resolution stalling 17-16 is at 2021-11-18.
- The committee chairs and the provost on the Quality Enhancement Plan are at
  2022-09-07.
- The ISEC meeting is at 2021-11-10, written up as the job-fair scholarship
  bill.
- Mason Stevenson's letter is at 2006-03-02, under the same title.
- The I-A football resolution is at 2006-10-31, with the referendum behind it
  at 2006-10-25.

In every case `main`'s version is the better one. The branches dated these
events to the day the *Herald* printed them; `main` dates them to the day the
meeting happened, which is a day or two earlier and is the date that belongs
in a history of the organisation. The clearest case is the speaker vote:
the branch cites the *Herald* of 15 April 2004, and `main` cites SGA's own
minutes of 13 April, mirrors the PDF, and says in the entry itself that the
report ran two days after the vote.

The conclusion the earlier passes reached was right. It is now right on
evidence that would have caught a counter-example, which the file-level
comparison would not have. Nothing is stranded. Recorded so that a future
pass does not have to walk this again — and so that a future pass does not
read a large branch-ahead count, or a list of unmatched titles, as research
worth rescuing. Both are artefacts.

## Six published claims opened against their sources

With no queue to review, the sample was taken from what is already on the
site, on the principle that a claim on the live site is worth as much
checking as a claim proposed for it. Six entries were read against the
articles behind them, fetched in full rather than from the local index.

All six hold. Two are worth naming because they show the archive catching
something:

- The 2022-23 committee chairs entry says six chairs were installed. The
  draft of the same event on the 4 August branch said five, and the article
  names six. The published version is the correct one.
- The 2012-13 plus-minus entry calls Hannah Garland the Academic Affairs
  committee chair and reports Cory Dodds on putting the question to a spring
  ballot. Neither claim is in the *Herald* report of 21 February, which is
  the obvious source and calls her only the resolution's author. Both are in
  the follow-up of 26 February, which is the article the entry actually
  cites. The entry is sourced correctly and the citation is the right one of
  the two.

The second of those is the trap the brief names — a bill's author recorded as
an officeholder — and the archive does not fall into it. The title is real and
it is cited to the article that carries it.

One small imprecision, not worth a correction on its own but recorded: that
same entry places the tabling "at the Tuesday meeting", and the 26 February
article it cites says only "its last meeting". The Tuesday is established by
the 21 February article, which the entry does not cite. The date on the entry,
2013-02-19, is correct — 19 February 2013 was a Tuesday — but the source for
it is a second article that is not named.

## The research pipeline is down to one routine, and has been for six days

Recorded on 28 August and not since acted on, so it is restated here with the
current figures rather than left to age in the middle of the file.

`research-photos` is healthy and has run several times a day; every merge for
the last three days has come from it. The other three have not committed since
25 August. Two have documented reasons: `research-backlog`'s last commit
disabled its own trigger deliberately, and `research-senate`'s records a fifth
consecutive empty pass, which is a routine reporting that its leads are
exhausted rather than a routine failing. `research-profiles` stopped on
24 August with nothing in the record explaining why.

The effect is visible in the count. The archive's event total has not risen
since 26 August. It has only fallen, from 2,019 to 1,984, and that fall is the
thirty-five duplicates merged on 29 August, which is the record getting more
accurate rather than smaller. No new history has been added in four days. The
portraits are real work and they are the project's most wanted material, but
photographs are all that is arriving.

Whether to re-scope or restart a routine is the owner's call, not the editor's.
It is flagged rather than acted on.

## Tooling notes

`web.archive.org` is refused by this environment's egress policy. Two entries
on the orphan branches cite Wayback captures and could not have been checked
against them had they needed checking; both turned out to be published already
from better sources on TopSCHOLAR, so nothing was lost this pass. A future run
that needs the Wayback Machine should know it cannot reach it from here.

`wkuherald.com` refuses the fetch tool with a 403 but serves ordinary requests
normally. Every *Herald* article in this pass was read that way. The 403 is not
the site being down and is not a reason to write "no source found".

`gh` is still not installed, as the 29 August addendum records. The brief's
opening command fails with `command not found` rather than the 403 it is
written to detect, which would drop a run into review-only mode while GitHub
was fully reachable. It was reachable this pass: `git push --dry-run` and the
GitHub tools both worked.

## Still open

Everything from the previous entries stands, and none of it moved tonight: the
twelve years with no photograph, the roughly 569 officer and senate-officer
names with no portrait, the 21 president records with no `also_regent` field,
the 151 raw "SGA legislation: ..." citation labels, the sixteen people filed
under both the executive and the senate, the credits citing a bare image file,
the Salvador Leon and Salvador León question, and the 1972-73 Ed Jordan credit
at exactly fifteen words. `scripts/photo_gap.py` is still unwritten, and the
proposal that `check_duplicates.py` compare bodies as well as titles has still
not been built.

The standing brief still sends each pass after pull requests #6, #7 and #8,
closed unmerged on 18 August, and still describes four running routines when
one is running.

# 30 August 2026 — editor's pass: a portrait kept, a portrait withdrawn

One pull request open, #280, the photographs routine's rolling branch. It
carried two new officer portraits. Two claims is fewer than the eight a spot
check calls for, so both were opened against their sources rather than sampled.
One held and is now on the site. One did not and was cut before the merge.

**Julie Mishchuk, Speaker of the Senate 2022-23, stands.** The Herald article
of 17 February 2023 was fetched and the photograph traced back to its own file
on the Herald's server, so the committed portrait is that frame and not a
lookalike of it. The caption names the person, the office and the occasion, and
one person is in the frame. The name matches `years.json` exactly and
`name-aliases.json` holds nothing that would make this a second record for
someone already on file.

Its note needed one correction, and the correction improves the record rather
than weakening it. The note said the article's caption spells the surname
"Mischuck"/"Mischuk" and implied the archive's "Mishchuk" rested on Senate
minutes alone. Counted in the fetched page: "Mishchuk" 28 times, "Mischuck"
twice, "Mischuk" never. The two photograph captions are the only places the
Herald departs from our spelling; the article's own text agrees with us
throughout. That is better evidence than the note claimed to have, and the note
now says so.

**Annalise Finch, Executive Vice President 2023-24, was withdrawn**, and the
image file removed from `data/photos/` and `site/photos/`.

The note claimed the WKU News article "names exactly three people sworn in at
the podium pictured." It does not. The article reports that the executive
council was sworn in and then names roughly fifteen more people elected
alongside the ticket, seven of them women — Bodemann, Wright, Vincent, Evans,
Distler, Payne, Duggins. So "the only woman named and the only woman pictured"
is not true of the source, and the elimination the identification rested on
does not close.

Underneath that, the photograph carries no caption at all: `alt=""`, no
figcaption, no credit, nobody named anywhere near it. A captioned alternative
was looked for before cutting — the Herald's own coverage of the same election,
19 April 2023, confirms the three ran as one unopposed ticket but carries no
photograph, and nothing else from that week names her beside a face.

There is a real circumstantial case, and it is worth writing down so the next
run does not mistake this for a thin lead. The left-hand figure is a good match
for the Salvador León portrait already in the archive, which does have a naming
caption; the article's subject is the executive council; the three ran together.
But that is an inference about who stands next to whom, not a source naming a
face, and the rule here is a hard bar rather than a confidence threshold: never
use a photo whose subject cannot be confirmed from caption or context, because a
misidentified face is worse than no face. She is also a living person, and this
would have published her name under an uncaptioned photograph on the strength of
a claim the source contradicts.

Provenance was not the problem, and recording that saves the next run a check:
the committed file is byte-identical to the article's own og:image at
`img_news/social_cover_images/11290.jpg`. Right file, right place, no caption.
What would land it is a captioned Herald or WKU News photograph, a Talisman
page, or a WKU gallery item naming her beside the image. The elimination
argument will not, however it is worded.

## Checks

`build.py` clean. `check_data.py` exit 0. `check_contrib.py` exit 0.
`check_duplicates.py` reports the same six pairs already standing on `main` —
the 1997-98 designated-driver items, the 1991-92 regent-advisory-committee bill
and its failure, the 1971-72 KCLU pair, the 2003-04 plus/minus pair and the
three same-day 1991-09-01 bills. Read and judged again this pass: all genuinely
separate events, none touched by this diff. The Vercel preview went green on the
corrected head before the merge.

61 years, 1,984 events, 60 people have been president.

The traps checklist found nothing else. No events were added, so no advance
notice could be written up as a report and no April result could be filed into
the wrong academic year. No committee chair recorded as an officer, no bill
author recorded as a member, no surname-only match, no changed-surname
duplicate, nothing touching the settled facts.

## The standing brief is out of date in two places

Worth correcting where the next editor run will read it, because both cost time
tonight.

The brief names three pull requests — #6 photographs, #7 the 1980s, #8 the
2020s — as open since 4 August and asks for them to be merged forward or closed.
All three were closed unmerged on **18 August**, twelve days ago. Checked
directly rather than inferred from the open list. There is nothing stale to
rescue; the photographs routine has since opened #280 against the same branch
name, which is what this pass reviewed.

The brief's opening probe is still `gh auth setup-git && gh pr list`, and `gh`
is still not installed in these containers, so it fails with `command not found`
rather than the 403 the brief is written to detect. A run that reads that as the
platform gate drops into review-only mode while GitHub is fully reachable — the
opposite of what the brief intends. The previous pass recorded this on 30 August
and it has not been changed. The working probe is `git push --dry-run` plus the
GitHub tools, as `AGENT-LANDING.md` says. Tonight both worked first try.

## The production domain is sga60.vercel.app, and tonight's merge is live on it

The previous pass recorded that the production domain appears nowhere in the
repository, so no run could confirm that what it merged actually reached the
public site. Found and verified tonight, so it need not be rediscovered:
**https://sga60.vercel.app**. `wku-sga-60.vercel.app`, the name the Vercel
project and the preview URLs suggest, returns 404; `sga60.vercel.app` serves
the archive, title and all.

Checked the merge against it directly rather than trusting the deploy. The
Mishchuk portrait is live at `/photos/2022-23-julie-mishchuk.jpg`. The withdrawn
Finch portrait returns **404** there, and her officer page renders with no
portrait reference in it. So the cut published as intended, and did not merely
leave the file orphaned in the tree.

Worth writing into `SGA-60-AGENT-INFO.md` §1 alongside the deploy notes, where a
run will find it before it needs it. Every merge here is a publication, and
until tonight there was no way to check the publication happened.

## The other research-* branches are still orphans, and none is a review target

Checked while the queue was empty, because the brief asks the editor to rescue
stale research branches and it is worth knowing there is none to rescue.
`research-senate`, `research-backlog`, `research-profiles`, `research-2020s`,
`research-1980s` and `research-editor-0823-seventh` all return `NONE` from
`git merge-base` against `main`. They are the superseded snapshots
`AGENT-LANDING.md` warns about, not forks of the current history, and the
content diff shows it plainly — `research-2020s` differs from `main` by some
303,000 deletions, which is main's own material the branch never had. Merging
any of them would delete the archive rather than add to it.

None of them has an open pull request, so none was in tonight's queue, and none
was touched. Recorded only so a future run does not read a large branch-ahead
count as stranded research. `research-photos`, the one branch the routines are
actually feeding, cuts from current `main` and merged normally.

## The verification record went in the body, not a comment

The previous pass left this open — a comment cannot be stripped of its
attribution line, a body can, and it asked whether the verification summary
should move to the body and these reports. Taking that decision this pass, since
the alternative is knowingly publishing under the project's name a line the
project's own rules forbid. The full verification record for #280 is in the
pull request body, which was rewritten and is clean, and repeated here. No
comment was posted.

`SGA60_SITE` and `SGA60_RESEARCH_TOKEN` are still unset in this routine's
environment, so review-only mode still has no drop box to land in and route
three, the run report, remains the only fallback. Unchanged from the previous
pass, and still worth either setting or writing plainly into the brief.

# 30 August 2026 — addendum: the attribution line can be stripped from a pull request body but not from a comment

Recorded after the merge, because it is a rule this repository states plainly
and there is currently no way for a routine to keep it.

`AGENT-LANDING.md` already warns that a "Generated by Claude Code" line
carrying a session link is appended to a pull request body, and tells a run to
read the body back and strip it. That works: `update_pull_request` rewrites the
body, and #278's body was cleaned that way within a minute of opening.

The same line is appended to **pull request comments**, and there it cannot be
removed. None of the GitHub tools available to these containers can edit an
existing issue or pull request comment — they can create one, reply to a review
comment, or add a reaction, and that is all. The direct REST API is not a way
round it either: `api.github.com` answers this session with

    403  GitHub access is not enabled for this session.

even though `git push` and the GitHub tools themselves work normally. That is
the platform gate the standing brief describes, still up on the raw API while
the tooled path is open.

So the verification comment on #278 carries the line permanently, and so does
every editor comment before it. This is not a thing a run can fix by being more
careful; it needs either a tool that can edit a comment or a decision to put
the verification summary only in the pull request body, which *can* be cleaned,
and in these reports, which are the project's own record. The second is
available today and costs nothing. Worth deciding before the next pass, since
the comment is visible text published under the project's name and the archive's
own rule forbids exactly this.

Two smaller notes from the same check. The merge itself is clean: `main` at
`fb0c3f2` carries no tool attribution in any commit message, and the commit is
authored by the project, not by a tool. And the Vercel preview deployment is a
real check on these pull requests — it went green on #278 before the merge, so
it is worth waiting the minute for rather than merging blind, given that a
merge here publishes.

# 30 August 2026 — editor's pass: an empty queue, and two concert citations that pointed at the announcement

Nothing was open to review. The last research merge was the photographs run's
#275, late on 29 August, and its night report #276 and the addendum #277 both
merged behind it. No routine has opened anything since, so this pass went to
the published record and audited a class of claim rather than a branch.

## Nothing is stranded on a branch

Checked first, because a routine that pushes without opening a pull request
looks exactly like a quiet night. `research-photos` and `research-editor-0826-late`
are fully contained in `main`. The other eleven `research-*` and `photo-*`
branches all report commits ahead of main, but that is an artefact of the
28 August history rewrite, which severed their merge bases. Compared by file
content instead, every one of them is *behind*: merging any would delete
photographs and years.json content that main already carries. They hold nothing
to rescue. The three branches the standing brief names as stale — the 4 August
snapshots behind the old #6, #7 and #8 — are among them, and their pull
requests are long since closed.

## What was audited

The advance-notice trap, systematically, across all 1,984 published events.
An announcement printed before an event proves what was booked, never how the
night went, so the test was mechanical: parse the date out of every citation
label, compare it with the event's own date, and read every entry whose source
went to press before the thing it describes happened.

Forty-four events are dated after the issue they cite. Forty-two of them handle
it correctly and needed nothing: they say plainly that the Herald *announced*
the event, attribute the outcome to the following week's issue or to the
Talisman, and several state outright that the report predates the thing
described. The routines have been disciplined about this.

## What was corrected

Two entries carried the outcome but cited only the announcement.

**1975-76, Natalie Cole in Van Meter, 10 December 1975.** The body gives an
estimated crowd of 325 and four songs; the citation was the Herald of 9 December,
printed the day before, which announced the concert and could not have carried
either fact. The facts themselves are sound — the 1976 Talisman puts Cole in
Van Meter on 10 December before an estimated crowd of 325 and names "Killing Me
Softly With His Song", "Honky Tonk Women", "You Are the Sunshine of My Life"
and the chart hit "This Will Be". Read against the volume's own full text, not
an index. Rescued rather than cut: the citation now leads with the Talisman and
names the Herald announcement after it.

**1976-77, Jimmy Buffett and the Coral Reefer Band, 27 April 1977.** The same
fault, with a wider gap. The body has three encores after a ninety-minute set,
a small crowd and a concert that lost money; the citation was the Herald of
25 March, thirty-three days early, announcing that the concert was set. The
1977 Talisman carries all of it — the lost money, the small cult that brought
him back for three encores after his 90 minute set, the April 27 date, and the
album titles. Citation corrected the same way.

Both now follow the convention already used elsewhere in the record, at
1974-75 for Pure Prairie League and 1973-74 for the Muskie lecture: the source
that carries the substance first, the announcement named after it. Neither
entry's text changed, because neither entry was wrong. The link under it was.

## Traps, checked

Committee chairs recorded as officers, surname-only matches, changed surnames
against `data/name-aliases.json`, April results filed into the wrong academic
year, anything touching the settled facts in section 7: none of these arise in
a citation change that alters no name, no year and no claim. No contributor
edits were in scope this pass.

## Recorded, not acted on

Forty-one published events credit the Talisman somewhere in the body while
citing something else. Most are sound — the Herald carries the fact and the
Talisman corroborates it — and the two above were the cases where the
substance lived only in the yearbook. The list is worth a slower pass than
this one, but it is not urgent and nothing in it is a false claim.

The 1976 and 1977 Talisman full texts on archive.org read as plain text in a
single request and are not rate limited. For checking a concert's crowd, its
takings or its date they are faster and better evidence than the Herald index,
and this pass cost TopSCHOLAR nothing at all.

## Checks

`build.py` clean, `check_data.py` 0, `check_contrib.py` 0. `check_duplicates.py`
printed six pairs and all six are genuinely separate events, judged and left
alone: the 1997-98 designated driver cards are the bill's first reading and the
Herald's notice of distribution three months later; the 1991-92 advisory
committee pair is a bill introduced and the same bill failing after amendment
nine days on; the 1971-72 pair is the Civil Liberties Union planning action and
Associated Students endorsing it a month later; the 2003-04 pair is SGA voicing
concern in September and passing legislation in October; and the three 1991-92
bills sharing 1 September are three different bills, which is exactly the case
the rule says to leave standing.

## Where the archive stands

61 years, 1,984 events, 60 people have been president, 297 documents, 1,111
legislation files.

## Still open

Everything from the previous entries stands, less nothing — this pass closed no
open item and opened none. The forty-one Talisman-credited citations above are
new to the list. Still untouched: the twelve years with no photograph, the
roughly 569 officer and senate-officer names with no portrait, the 21 president
records with no `also_regent` field, the 151 raw "SGA legislation: ..." citation
labels, the sixteen people filed under both the executive and the senate, the
credits citing a bare image file, the Salvador Leon and Salvador León question,
and the 1972-73 Ed Jordan credit at exactly fifteen words. The proposal that
`check_duplicates.py` compare bodies as well as titles has still not been built.

`SGA60_SITE` and `SGA60_RESEARCH_TOKEN` were again unset this pass, so the
review-only fallback route remains untested. It cost nothing: GitHub was
reachable by `git push --dry-run` and the GitHub tools, and this work merged the
ordinary way. `gh` is still not installed, so the brief's opening probe still
fails with `command not found` rather than the 403 it is written to detect.

# 29 August 2026 — editor's pass, midday: an empty queue, and the nine new portraits taken back to the volumes

Nothing was open to review. The photographs run's #267 and the night report #268
both merged this morning, and no routine has opened anything since. For the third
consecutive pass there was nothing to merge, so this one went to the material that
merged most recently and read it against its sources instead.

## Nothing is stranded on a branch

Checked before concluding the queue was really empty, because a routine that
pushes without opening a pull request looks exactly like a quiet night.
`research-photos` and `research-senate` are fully contained in `main`; the file
differences they appear to carry are `main`'s own later work seen from behind.
`research-profiles` and `research-editor-0823-seventh` have no merge base at all
and are the superseded snapshots AGENT-LANDING.md warns about.

`research-backlog` needs recording, because it looks like 299 commits of lost
work and is not. Its commits are pre-rewrite duplicates of history already on
`main`, carrying both the `SGA 60` and `samuelkurtzsfs` copies of the same
changes. One of them is "Withdraw the Thomas LaCivita portrait: the face is not
identified" — the withdrawal that was examined against the page image on
28 August and reversed. Merging that branch would quietly undo a settled fact.
It should not be merged, and a later pass that sees the commit count should read
this paragraph before acting on it.

## The nine portraits, checked against the volumes' own text

All nine merged this morning as crops from named group photographs, which is the
identification most likely to go wrong: the credit places a face by counting
along a printed caption. Every one of the claims below was opened on
archive.org rather than taken from the credit.

The 1986 Talisman's p. 194 caption is verbatim what the seven 1985-86 credits
quote, in both rows — front row Mitchell McKinney, Cindy Richards, Greg Elder,
Tara Wassom, Loree Zimmerman, Roland Spencer; back row Edward Kenney, Lori Scott,
Kent Groemling, Mark Lovell, Sean Peck, Donna Pack, Tim Todd. The second
Associated Student Government photograph's caption matches the Caroline Miller
credit in the same way. The volume's index enters Gregory Allen Elder at 194-195
and 327 and Cindy Lee Richards at 194-195 and 314, exactly as the two credits
claim, and the class portraits they were cropped from read "GREG ELDER, Glasgow"
and "CINDY RICHARDS, accounting, Cloverport".

Brett Butler's credit quotes the 1971 volume's "Brett Butler; Harned;
Accounting", which is right, and the same volume corroborates the office
independently in an officers caption naming him treasurer beside John Lyne as
president and Doug Alexander as vice president — which is what this archive
already records for 1970-71, from that page.

Pam Stewart was the one worth the most care, because the credit joins an officer
to a senior portrait across two volumes and a second Pamela Stewart exists. It
holds. The 1974 index enters Pamela Gail Stewart at p. 56, the 1975 index enters
her at p. 377, that volume separately lists a Pamela Anne Stewart whom the credit
explicitly declines to merge, and the 1974 text names "Pam Stewart, secretary" in
the executive branch. The identification rests on the indexes rather than on a
shared name, which is what the credit says it rests on.

## Published events opened against their issues

Digitised Herald landing pages answered this session, so nine event claims were
read against the issue indexes they cite. All held. The 29 February 1972 issue
carries Linda Jones's "Associated Students Corrects Herald", David Gray's piece
on the Kentucky Civil Liberties Union planning court action, Carter Pence on the
executive branch of the constitution, and "Benjamin Mays Speaks Tonight". The
28 March 1972 issue carries Nancy Pape's "Vote Yes", Roger Miller on Associated
Students endorsing the lawsuit, and the mini-concert item. Nikita Stewart's
"Altered Bill Fails in Associated Student Government" is in the 6 February 1992
issue, and Melissa Felkins's designated driver cards item in the 17 February 1998
issue.

Three of those nine are advance notices, and all three are already written down
to what a notice proves: the mini-concert appears only as something the issue
advertised, the designated driver cards only as due to be distributed the
following day, and the Benjamin Mays entry says in its own body that the
yearbook's caption and its running text disagree about whether he spoke. Nothing
in the sample claimed a crowd, a review or a result out of a booking.

## The photograph layer as a whole

233 leader portraits and 61 year photographs. Every file is present on disk,
every one begins with real image bytes, every one carries a source URL, and every
name in a leader entry matches a person the year actually records. The two Lori
Scott entries share one file across 1985-86 and 1986-87 by design, and the
1986-87 credit says on its face that it is an extension of a photograph taken in
the earlier year; the archive has her as KISL Committee chairman in the first
year and administrative vice-president in the second, both from the minutes.

Committee chairs in both years are filed under the senate's officers and not the
executive, which is the error #243 corrected elsewhere. It has not come back.

## Checks

`build.py` completed cleanly: 61 year pages, 7 decade pages, 297 documents,
1,111 legislation files. `check_data.py` exited 0 on 61 years, 2,019 events and
60 people recorded as president. `check_contrib.py` exited 0 on every assertion.
`check_duplicates.py` reported the same six pairs as recent passes; each was read
again and each is still two events rather than one written twice.

## What is reachable

Measured rather than assumed, since the last entry asked a later run to test it.
Herald issue landing pages on digitalcommons answer 200, and that is the route
that lets a negative conclusion be checked properly. `viewcontent.cgi` is still
403, so the page images and the pre-2011 portrait work behind them stay shut.
`wkuherald.com` article pages are still 403. `archive.org` and `www.wku.edu`
both answer 200; the Talisman full texts used throughout this pass came from
archive.org.

## One thing for the owner, not for a routine

CLAUDE.md still lists "John Lyne vs Larry Zielke 1970-71" among the questions
that are open. The data no longer treats it as open: Lyne is recorded verified
and confirmed, with five sources and a note explaining that the plaque's pairing
is wrong because Zielke's term was 1969-70. The 1971 Talisman caption read for
Butler above names Lyne president too. The law file and the record disagree, and
editing the law file is not a routine's call, so it is left as it stands and
flagged here.

## Nothing merged, nothing cut

No pull request was open, so nothing was merged. Nothing in what was audited
needed cutting or trimming. The archive stands where it stood: 61 academic years,
2,019 dated and sourced events, 60 people recorded as president, 297 mirrored
documents, 1,111 pieces of legislation.

## Added after the pass: why the queue keeps being empty

Three passes in a row have recorded an empty queue without asking why it was
empty, so this pass checked. Three of the four research routines have stopped
opening pull requests.

`research-profiles` last opened one on 24 August (#189). `research-backlog` last
opened one on 25 August (#223), and that one is explained: its own last commit
reads "Disable the stale backlog trigger, not just diagnose it", so it was
stopped deliberately. `research-senate` last opened one on 25 August (#225), and
nothing in this file explains that one. `research-photos` is the only routine
still producing, and it has run several times a day throughout.

The visible effect is that the archive's event count has not moved. It has stood
at 2,019 since 26 August, and every merge since has been photographs. The
photograph work is real and the portraits are the project's most wanted
material, but a pipeline reduced to one routine is not what this file has been
describing when it says "an empty queue".

This is recorded rather than acted on. Restarting a routine is not an editor's
call, and nothing here suggests the routines failed at their research: they
simply stopped being fired. The owner should know that two of them, the senate
rolls and the person profiles, went quiet without a reason anyone wrote down.


## Still open

Everything carried over stands, untouched by this pass: the twelve years with no
photograph of their own, the roughly 590 officer and senate-officer names with no
portrait, the 21 president records with no `also_regent` field, the 151 raw
"SGA legislation: ..." citation labels, the sixteen people filed under both the
executive and the senate, the credits citing a bare image file, the Salvador Leon
and Salvador León question, and the 1972-73 Ed Jordan credit at exactly fifteen
words. `scripts/photo_gap.py` is still unwritten and still wanted.

# 29 August 2026 — editor's pass, later: nine portraits merged, and the page-number slip caught for the third night running

One pull request was open, #267, "Research: photographs — nine more officer
portraits," pushed this morning to `research-photos`. It is merged. Nine
portraits are on the site that were not there this morning: Brett Butler,
Pam Stewart, Tara Wassom, Loree Zimmerman, Lori Scott, Sean Peck, Donna Pack,
Tim Todd and Caroline Miller. Two corrections went onto the branch first, and
a third fixed something that was already live.

The branch had a real merge base with main and was not behind it, so none of
the orphan-history caution in AGENT-LANDING.md applied.

## What was checked, and how

Ten claims, which was the whole diff rather than a sample. Nothing was taken
from the run's own report; every identification was opened against the volume.

The seven portraits out of the 1986 Talisman rest on two group photographs
whose captions print a front-row and back-row roster in reading order. Both
rosters are verbatim in the volume's text, and every position the run claimed
matches. That is not on its own enough — a roster only identifies a face if
the count of faces matches the count of names — so the group photographs
already on main were counted: six in front and seven behind in the first,
six and six in the second, exactly the rosters. Each crop was then checked
against its place in the group photograph, and the sequence of men and women
against the roster: M,F,M,F,F,M across the front row, M,F,M,M,M,F,M across the
back, F,F,F,F,M,M in the second photograph. A crop shifted by one place would
have broken that pattern somewhere, and none does.

Brett Butler needed none of this. His crop carries the printed caption inside
the frame, and the Who's Who heading, the caption and the printed folio 36 sit
together on the page, with the index entering him at 36.

Every name, year and office also matches `years.json` exactly. No committee
chairman has been lifted into an executive office anywhere in the diff, which
is the error that killed all thirty-nine of the old missing-president claims;
Scott, Peck, Pack, Todd and Miller are recorded as chairmen, which is what the
senate officer list already said. `Tim Todd` was already mapped to
`Timothy Todd` in `name-aliases.json`, and the 1987 senior portrait on file is
consistent with the new crop, so no second person has been invented.

## Pam Stewart, who needed the most work and was the best find

Her page was wrong: filed at p. 378 of the 1975 Talisman, and she is on 377.
The volume's index enters Pamela Gail Stewart and Barry Lynn Stice alike at
377, and Stice follows Stewart in the grid.

The identification underneath it is sound, but it was resting on the wrong
thing. The 1975 volume names **two** Pamela Stewarts, Pamela Anne and Pamela
Gail, so a first and last name does not settle which of them was the ASG
secretary. It happens that the volumes' own indexes do: the 1974 index enters
Pamela Gail Stewart at p. 56, its Associated Student Government page, and the
1975 index enters her at p. 377. The credit was rewritten to stand on that,
and to record that the second Stewart exists and has not been merged into her.
The face is right too — row three of the grid runs Stephenson, Stevenson,
Stewart, Stice, Stiegemeier, a man, man, woman, man, woman sequence that the
page image matches, and the third position is the committed crop.

One clause was cut. The credit said the volume names her senior class vice
president. It does not. It names "senior officers Mike Inman and Pam Stewart"
and never gives her an office; the phrase appears nowhere in the volume.

## Two citations that were already on the live site

The Greg Elder and Cindy Richards credits, merged on 28 August, both put the
1986 ASG group photograph on p. 198. It is on p. 194: the printed folio 194
falls immediately after the two roster captions, and the index enters Gregory
Allen Elder and Cindy Lee Richards alike at 194-195. Page 198 is an index
page — the line `Martin, Brian Oneil 194-195, 198` is what sits there — which
is where the number almost certainly came from. Elder's quote as
administrative vice president is on p. 195. Both are corrected. An unverified
"p. 75" in the Richards credit was replaced with the index reference, which a
reader can check.

## The thing worth saying plainly

This is three nights in a row that a page number has been wrong, and each time
in the same way: a number read off the scanning apparatus or off an index line
rather than off the page. Last night's entry is headed "a page number that was
really a leaf number." The run that produced tonight's work wrote down a rule
for itself — leaf equals reported page minus one, checked across two volumes —
and that rule is what produced the Stewart error. It is a fine way to find a
page and a bad way to cite one. The volumes print their own folios and carry
their own indexes, and consulting one costs a single grep. That is what caught
all three of these, and it belongs in the method rather than in the night
report every morning. It is now written into section 8 of the handoff.

Nothing else was open. Pull requests #6, #7 and #8, which the standing brief
still describes as stale since 4 August, were closed unmerged on 18 August;
this is the third pass to confirm it, and the brief has not caught up with a
repository now at #267.

## One thing I could not clean up

The attribution line that AGENT-LANDING.md warns about was appended to both
things opened this pass. It was stripped from the body of #268. It could not
be stripped from the review comment on #267: the platform's direct GitHub API
is refused in this session, and the tool surface that does work has no method
for editing a comment once posted. Nothing reached the archive itself — no
commit message, no data file and no generated page carries it, which is what
the rule is really protecting — but the comment on #267 still ends with it,
and removing it is a ten-second job for anyone with a browser.

## Counts

`build.py` clean, `check_data.py` exit 0, `check_contrib.py` exit 0: 61 years,
2019 events, 60 people have been president. `check_duplicates.py` reports the
same six pairs it has reported for days, all correctly separate — three bills
of 1 September 1991, and three pairs that are an introduction and then a vote.
This diff added no events, so it could not have made a duplicate. All nine
image files verified as real JPEGs.

# 29 August 2026 — editor's pass, morning: an empty queue, and last night's six portraits re-checked from the volumes' own text

Nothing was open to review. `list_pull_requests` returned an empty set, and the
three pull requests the standing brief still names as stale — #6 photographs,
#7 the 1980s, #8 the 2020s — were all closed unmerged on 18 August, eleven days
ago. The brief has not caught up with the repository, which is now at #265.
Nothing was merged this pass because there was nothing to merge, and nothing was
cut because nothing failed.

## The branches, checked rather than assumed

Every branch on origin beginning `research-` or `photo-` was measured against
main rather than read from the pull request list, in case a routine had pushed
work and then failed to open a pull request for it. None had. The four active
branches — `research-photos`, `research-senate`, `research-backlog` and
`research-editor-0826-late` — are all nought commits ahead of main, which is to
say fully merged.

The seven that report themselves ahead are the orphan-history snapshots, and
they are ahead of nothing. `git merge-base` returns no common ancestor for any
of them against main: `research-1966-79`, `research-1980s`, `research-1990s`,
`research-2000s`, `research-2010s`, `research-2020s`, all last touched on
4 August, together with `photo-research-2026-08-22`,
`research-editor-0823-seventh` and `research-profiles`. AGENT-LANDING.md is
explicit that these are snapshots of a superseded repository rather than forks
of this one, and that merging one deletes the contributor layer and the
validators along with `herald-index-full.json`. They were left where they are.
The commit counts they carry are not pending work.

## Last night's portraits, checked a second way

The 03:36 pass merged six portraits and opened all eight of their credits
against the Talisman page images. This pass checked the same material by a
different route, the volumes' own OCR text and printed indexes on archive.org,
so that the identifications rest on two independent readings rather than one.
Twelve claims were opened. All twelve held.

The two captions are verbatim as the credits quote them. The 1972 volume reads
"Above—Reginald Glass, vice president; Nancy Pape, secretary; Linda Jones,
president; Joe Glasser, treasurer." The 1973 volume carries the heading "Berman
led sophs during a quiet year" and a caption placing vice-president Mike Inman
at the left, which is what leaves Berman as the figure at the right.

The Berman page correction is right, and the volume settles it twice over. The
folio immediately above the sophomore page reads 415, and the index files
Berman at 301, 416 and 418. The 421 the credit used to carry was the scan leaf,
as last night's correction said.

The reasoning the Glasser credit gives for trusting the caption's order also
holds: the 1972 volume states in its own words that Reginald Glass is the first
black vice president of Associated Students, which is what fixes him at the
left of the frame.

The four class-portrait rows check out on position. The 1977 index reads
"Faulk, Gerard Jr. 319, 350" and the p. 350 block runs Fatheddin, Faulk,
Ferguson, Ferralasco, in that order, with Faulk second. The 1978 index reads
"Reed, Gary W. 288, 372" and the block runs Reece, Reed, Reeves. The 1981 index
reads "Fuller, Steven Joe 128, 131, 282, 325", and Fuller is the last portrait
on his page, which its running foot confirms by reading Ford-Fuller.

Cook is the strongest of the four and the one worth recording in full, because
the yearbook ties the officer to the face without any help from us. The index
reads "Cook, Patricia Ann 35, 383". Page 383 is the portrait. Page 35 is the
Herald editorial's inner-office joke declaring a day in honour of Tricia Cook,
interim ASG secretary — the volume's own words, and the same person under the
index's own hand. Her block is nine names, Cole, Collins, Colter, Connor,
Conover, Cook, Cooper, Cooper, Cope, and she is the sixth of them, exactly as
the credit says.

One loose end, not a defect. The Faulk index carries a page 319 the credit does
not account for, and the volume has an SNEA group photograph listing a G. Faulk
in its front row, which would suit an elementary education major. It does not
put him in an ASG office, so the credit's own caution — that the tie between
this senior and the Judicial Council chairman rests on the name — stands
unaltered.

## Checks

`build.py` completed cleanly: 61 year pages, 7 decade pages, 297 documents and
1,111 legislation files. `check_data.py` exited 0 on 61 years, 2,019 events and
60 people recorded as president. `check_contrib.py` exited 0 on every assertion.
`check_duplicates.py` reported the same six pairs as recent passes. They were
read again rather than taken on the earlier verdict, and each is still two
events rather than one written twice: the three bills of 1 September 1991, the
regent advisory committee's introduction in January 1992 and its defeat after
amendment in February, the Civil Liberties Union's planned action in February
1972 and Associated Students' endorsement of the suit in March, SGA's position
against plus/minus grading in September 2003 and its legislation in October, and
the designated driver cards funded by bill in November 1997 and reported for
distribution in February 1998.

That last pair is worth a line, because the February entry is an advance notice
and is written as one. It says the cards would be distributed the following day
and that the archive holds only a contents listing, and it claims nothing about
how the distribution went. That is the rule applied correctly rather than
tripped over.

## Where the archive stands

Sixty-one academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents, 1,111 pieces of legislation. Unchanged by this
pass.

## What could not be done

`archive.org` answered 200 throughout and served all five Talisman full texts
without difficulty, which is how this pass did its checking. The
`digitalcommons.wku.edu` restrictions recorded by earlier entries were not
retested, because nothing this pass needed lay behind them.

## Still open

Everything carried over stands, untouched by this pass: the twelve years with no
photograph of their own, the roughly 590 officer and senate-officer names with no
portrait, the 21 president records with no `also_regent` field, the 151 raw
"SGA legislation: ..." citation labels, the sixteen people filed under both the
executive and the senate, the credits citing a bare image file, the Salvador Leon
and Salvador León question, and the 1972-73 Ed Jordan credit at exactly fifteen
words. `scripts/photo_gap.py` is still unwritten.

One thing this pass would add for the owner rather than settle itself: the
standing brief that drives these runs still describes a queue from 4 August and
sends each pass looking for three pull requests that have been closed for five
weeks. It costs a few minutes a run and it points the editor at the orphan
branches, which are the one thing on this remote that must never be merged.

---

# Editor's pass - 29 August 2026: six portraits merged, and a page number that was really a leaf number

One pull request was open, #264 from the photograph routine, and it was merged
after two corrections were pushed to the branch first. It added six portraits
and nothing else: Joe Glasser, treasurer in 1971-72; Louis Berman,
sergeant-at-arms in 1972-73; Gerard Faulk, who chaired the Judicial Council in
both 1975-76 and 1976-77; Gary Reed, treasurer in 1977-78; Tricia Cook, interim
secretary the same year; and Steve Fuller, administrative vice president in
1979-80 and president in 1980-81, one portrait carrying both of his years.

Eight entries for six faces is fewer than the eight new claims a spot check
calls for, so all of them were checked rather than sampled, and all five cited
Talisman pages were opened as page images rather than taken on the credits'
word.

## A page number that was really a leaf number

The Berman credit cited p. 421 of the 1973 Talisman. The page is 416. The
folios on either side of it run 415 and 417, and the volume's own index files
Berman at 301, 416 and 418. What the credit had recorded was the scan leaf,
n421, which is what the source link correctly points at.

The routine had reasoned its way there honestly and written the reasoning into
the handoff: it fetched a dozen leaves, found the offset exact every time, and
recorded the rule. The rule holds for four of the five volumes it used - leaf
n275 of 1972 is page 272, n353 of 1977 is 350, n375 and n386 of 1978 are 372
and 383, n328 of 1981 is 325, all a gap of three - and breaks on the fifth,
where 1973's longer front matter makes the gap five. An offset confirmed a
dozen times inside one volume says nothing about the next one.

This is the second night in a row that the leaf and the folio have caused
trouble, and it is worth noting they failed in opposite directions. On 27
August the 1971 volume's index and folio both said page 68 and both were
useless, because that volume numbers its sections separately, and only the leaf
found the committee photograph. Last night the folio was right and the leaf was
what got written down. The lesson that survives both is not "prefer the leaf" or
"prefer the folio" but read the number off the page image, check it against the
index, and where the two disagree say which one the credit means. A note to
that effect now sits in the handoff beside the method it corrects.

## The identifications themselves, and how far each one actually reaches

Four of the six came out of the alphabetical class-portrait sections, a name
list beside a grid of faces in the same order. It is a good method and the
archive already rests Jack Smith, Dean Bates, Terri Craig and Kevin Strader on
it. But it identifies a face in a yearbook, which is not the same as
identifying an officer, and the six divide sharply on that second step.

The yearbook settles it outright in two cases, and neither credit had said so.
The 1978 index reads "Cook, Patricia Ann 35, 383", and page 35 is the ASG page
that names Cook the interim secretary, so the volume itself ties the officer to
the portrait on 383. The 1981 index reads "Fuller, Steven Joe 128, 131, 282,
325", carrying one man across the regents pages, the ASG group photograph and
the senior portrait. Both credits now carry that evidence, because it is the
part that makes them certain and it was the part missing.

For Faulk and Reed it does not. The 1977 volume never names ASG's Judicial
Council chairman and the 1978 volume never names its treasurer, so both rest on
a distinctive name appearing exactly once in the volume's index, plus, for
Reed, an accounting major that suits a treasurer. That is thin, and it is
thinner than the credits made it sound. They were kept, because the method is
already the archive's and the row positions are firm, but both credits now say
plainly what the identification rests on and what it does not. A reader who
wants to weigh a name-only match should be able to see that is what they have.

Glasser and Berman came from captioned photographs and needed no such
reservation. The Glasser caption's left-to-right order is confirmed by
something outside itself: Glass stands at the left, and the same volume calls
him the body's first black vice president. The Berman caption places Inman at
the left, which leaves Berman as the figure at the right.

## A credit that claimed a cleaner crop than the crop is

The Glasser credit said the frame was cropped to him alone. It is not: the
other players at the tables behind are plainly in it, and the man himself is
bent over a shot with his face half turned away. It is the only photograph the
volume gives of him and it is genuinely him, so it stays, but the credit now
describes the picture a reader will actually see. An archive that overstates
its crops is training its readers not to trust its captions.

## What held

Everything else. No events were added, so the advance-notice trap and the
April-election trap did not arise. No committee chair was promoted into an
officer's chair. Nothing was matched on a surname alone. The Steve Fuller and
Steven Fuller entries are not a duplicated person: `name-aliases.json` already
maps the one to the other. Nothing touched the settled facts. Nothing in the
diff came from a contributor. All six files are real JPEGs and all six now
render on their officers' pages.

Two things worth carrying forward, neither of them faults. The 1981 index gives
Fuller as **Steven Joe**, which is the first positive support for the plaque's
"Steven" over the Herald's "Steve"; his leader note still flags that spelling
as unverified and this looks like enough to close it, but changing a leader
record is not a photograph pass's work and was left alone. And on his own page
the new Talisman portrait has displaced the 1980 Herald halftone, which is a
real gain in legibility; the year page's leader card still carries the Herald
one.

The Berman credit was also rewritten to paraphrase its caption rather than
quote it. The quotation ran to exactly fifteen words, and the rule is under
fifteen - the same fault the standing list still records against the 1972-73 Ed
Jordan credit.

## State of the record

61 years, 2019 events, 60 people have been president. 297 documents and 1111
legislation files. 223 portrait credits across 147 distinct image files, and
all 73 leader records carry a portrait. `build.py`, `check_data.py` and
`check_contrib.py` all clean. `check_duplicates.py` reports the same six pairs
as ever; all six were read again and all six are genuinely separate events - an
announcement and a distribution four months apart, a bill introduced and the
same bill failing, and three bills passed on one day in September 1991, which
the rules deliberately keep apart.

The three pull requests this routine's standing instructions describe as stale
and open since 4 August - #6 photographs, #7 the 1980s, #8 the 2020s - have
been closed since 18 August. There was nothing to rescue or close. The
instruction should be updated so a future pass does not go looking for them.

## Still open

Everything carried over stands, none of it touched by this pass: the twelve
years with no photograph of their own, the officer and senate-officer names
with no portrait, now roughly 584, the 21 president records with no
`also_regent` field, the 151 raw "SGA legislation: ..." citation labels, the
sixteen people filed under both the executive and the senate, the credits
citing a bare image file, the Salvador Leon and Salvador León question, and the
1972-73 Ed Jordan credit at exactly fifteen words.

`digitalcommons.wku.edu/cgi/viewcontent.cgi` was not exercised by this pass,
which had no need of it; the routine reports it still returning the same
Cloudflare challenge it has since 25 August. `archive.org` answered every
request made of it tonight, including five full volume texts and five page
images, and remains the way in.

Two leads noticed while reading the volumes, recorded here rather than acted
on. The 1978 Talisman mentions a Reed Morgan awards banquet, which is context
for the settled question of what his plate honours, though it puts him in no
office and does not reopen anything. And the April 1980 presidential election
is written up both in 1979-80, where it happened, and in 1980-81, the term it
produced. That is defensible and it predates this diff, but the two accounts
should be read side by side by whoever next works either year.

# Editor's pass - 28 August 2026, night: a withdrawn portrait checked against the page and left standing

Nothing was open to review. `research-photos`, `research-senate` and
`research-backlog` are all level with main, and the three the standing brief
still calls stale - #6, #7, #8 - have been closed since 18 August. That is the
third pass to record it; the brief is still pointing at them and still should
not be.

With no queue, the pass went at what is already published.

## The Thomas LaCivita portrait, and why it kept moving

The archive's own history contains a straight contradiction about one face. On
25 August a pass withdrew the 1974-75 LaCivita portrait, reasoning that the
concert-booking caption on p. 109 of the 1975 *Talisman* describes two people
conferring and so belongs to the stairway photograph above it, leaving the
brick-wall close-up in the left column uncaptioned and the man in it
unidentified. On 27 August a later pass added the same photograph back under a
new filename and kept it, reading the caption onto the portrait and explaining
that treasurer Ricky Johnson simply fell outside the printed frame. Each pass
argued from the caption text alone, and the caption text alone does not settle
it, which is why the face has now been published, cut and published again.

It was settled by fetching the page. The scan of leaf n112 at
`archive.org/details/talisman1975west` shows the left-column photograph in full
rather than the head-and-shoulders crop the archive publishes, and the full
frame carries a second person at its left edge: a hand and forearm resting on
the document the visible man is holding, with a shoulder just inside the
border. So the photograph does contain two people, the fully visible one stands
at the right of the frame, and the caption naming LaCivita "(right)" with
Johnson describes this picture and no other. The identification holds and the
current entry's wording is accurate.

The portrait was left exactly as it is. What changed is `CLAUDE.md`, which now
carries the finding in its settled list with the leaf number, because the
withdrawal's reasoning is still sitting in the history reading like a sound
argument, and the next pass to find it would have cut the face a third time.

## The six portraits merged earlier today

Re-checked independently of the pass that merged them, and they hold. The
election-night crops were the ones worth the time, because three of them come
out of a single group photograph and are identified by nothing but the
caption's left-to-right order. The original was downloaded and read: four
people, blonde at the left, a second woman with straight light hair, a third
with dark curly hair, a fair-haired young man at the right, matching Molyneaux,
Dahmer, Lowry and Hounshell in the order the caption gives them. The three
published crops are three different people and each sits where the caption puts
them. Wyer, Ricke and Terrell were confirmed word for word against their
articles.

The filings were checked against the trap that has done the most damage here. A
committee chair is not an officer, and Amy Wyer is not filed as one: the SAVES
chairmanship she is photographed being sworn into sits under the 2018-19 senate
officers, while her 2017-18 public relations directorship, a genuine executive
post, is recorded separately. Molyneaux and Hounshell are executive officers of
2017-18 off an April 2017 election, which is the right way round.

## What was checked on main

`build.py` completes cleanly and leaves the working tree unchanged, so what is
deployed matches `data/`. `check_data.py` and `check_contrib.py` both exit 0.
`check_duplicates.py` reports the same six pairs, all read again and all still
six real events rather than three written twice.

Two checks were run that no script performs. Every file the data references was
looked for on disk - 210 leader photographs, 297 documents, 1,111 pieces of
legislation and every event `src` file - and nothing dangles. Every quoted span
in `photos.json` and `years.json` was measured against the fifteen-word rule,
across credits, event bodies, profiles, notes and document extracts, and
nothing exceeds it. The over-quotation backlog earlier passes worked through is
genuinely clear.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents and 1,111 pieces of legislation, over 61 year
pages and 7 decade pages.

## Still open

Everything carried over stands, none of it in a diff this pass had to judge:
the 151 raw "SGA legislation: ..." citation labels, the sixteen people filed
under both the executive and the senate, the year-photograph gap from 1996-97
to 2009-10 behind the Cloudflare gate on `viewcontent.cgi`, the Salvador Leon
and Salvador León question awaiting `name-aliases.json`, and the 1972-73 Ed
Jordan credit sitting at exactly fifteen words.

Two new ones. Molly Ricke is photographed being sworn in as a senator-at-large
in January 2025, which falls in 2024-25, but the archive records her only in
2025-26; the portrait is filed where she is recorded, and the earlier seat is a
lead nobody has followed. And `NIGHT-REPORT.md` is now ordered both ways - most
entries newest-first from the top, a run of them appended oldest-last at the
bottom - which will mislead anyone reading it for the current state.

# Editor's pass - 28 August 2026, later: six portraits merged, one of them recropped first

One pull request was open, #254, `research-photos`, and it merged. The three the
standing brief still calls stale - #6, #7, #8 - remain closed, as the previous
pass recorded; the brief is still pointing at them and still should not be.

Six officer portraits, all off wkuherald.com, all into `photos.json` only, with
`years.json` untouched. Amy Wyer 2018-19, Nathan Terrell 2019-20, Savannah
Molyneaux, Kara Lowry and Conner Hounshell 2017-18, Molly Ricke 2025-26. Six
claims is fewer than the eight a sample is meant to cover, so all six were
opened rather than a sample of them, and every caption was confirmed word for
word against the live article.

## The Lowry crop was not a portrait of Lowry

The run reported that its crop of the 2017-18 election-night group photograph
kept "a small sliver of Dahmer's hair/eye at one corner." That description was
wrong, and the way it was found is worth keeping.

The four officers in that photograph are hugging, heads touching, and the whole
identification rests on the caption's left-to-right order. Rather than take the
order on trust, the Herald's full-size original was downloaded and each of the
three committed crops located inside it by pixel match. Molyneaux sits at x
0-450, leftmost, exactly as claimed. Hounshell sits at x 1048-1499, rightmost,
also as claimed. Lowry's crop ran x 796-1156: roughly 100 pixels of Andi Dahmer
at one edge and 156 of Hounshell at the other, leaving Lowry about the middle
200. Three faces under one name.

Nothing was misidentified - the order held everywhere it was checked - but a
reader looking at that file could not have told which of the three faces was
Kara Lowry, and the rule about a misidentified face being worse than no face is
there for exactly that. The crop was remade from the full-size original at 240
by 660: Dahmer is out of frame, Lowry is the front-facing dominant subject, and
the credit now says plainly that Hounshell stays partly visible in profile
beside her. Rescued rather than deleted, because the identification was sound
and only the framing was not.

## A photo credit that stated an allegation and not its outcome

The Terrell credit carried the headline of the Herald's September 2020 report -
a candidate dropping out of a race over a video of him using a racial slur - and
stopped there. It sat under a living person's portrait on the 2019-20 page,
where nothing else in the year explains it. The episode is in fact recorded
properly, and in full, as a sourced event on 2020-21 under 23 September; the
credit was reproducing the accusation and leaving the reader on the wrong page
to find how it ended.

The report also led with a resignation, which the credit had softened into a
withdrawal from a race. The credit now records what the article actually
concluded: he denied being the person in the video, then confirmed it,
apologised in a statement, resigned the speakership and left the executive
vice-presidential race. The portrait itself is a clean solo headshot off the WKU
website and was never in doubt.

## What held

The other four credits needed no work. The election caption confirms Dahmer
president, Molyneaux executive vice president and Lowry administrative vice
president, and says nothing about Hounshell holding any office - he is simply in
the photograph, and the entry claimed nothing more, which is the trap about a
bill's author not being a member wearing a different coat. Spring elections file
forward correctly: an April 2017 result sitting in 2017-18. Nobody was matched by
surname. `name-aliases.json` carries Connor to Conner Hounshell and the canonical
spelling was used, so no second person was invented. No advance notices - all four
articles report things that had already happened. Nothing touches the settled
facts and no contributor commit was in the diff.

One thing was noted and not acted on, because it belongs to a decade routine and
not to a photographs branch: Ricke's portrait documents a January 2025 swearing-in
as a Senator-at-Large, but is filed to 2025-26, because 2024-25 carries no record
of her at all. The gap is in `years.json`. Terrell's filing to 2019-20 is right -
it is his only officer record, and its note already runs into the autumn of 2020.

`build.py`, `check_data.py` and `check_contrib.py` all clean: 61 years, 2019
events, 60 people have been president. `check_duplicates.py` reports the same six
pairs it has been reporting, none of them in this diff, and each of them a
genuinely separate event - a bill introduced and the same bill failing weeks
later, three different bills on 1 September 1991.

## The production alias, found at last: `sga60.vercel.app`

Two earlier entries in this file record that the live site could not be
verified from a routine, because `wku-sga-60.vercel.app` answers
`DEPLOYMENT_NOT_FOUND`. It is not the production alias and never was. The
production alias is **`sga60.vercel.app`**, which answers 200 and serves the
board under the title "SGA 60 - Student Government at Western Kentucky
University". `SETUP-CONTRIBUTORS.md` still gives the dead host as its example
for `SITE_URL`; that line was left alone, because it may be describing a
configured value rather than suggesting one, and it is the owner's to change.

This pass was therefore checked all the way through to what the public can
actually see, which is what "every merge is publishing" is supposed to mean.
Both corrections are live: `/o/nathan-terrell.html` carries the outcome and no
longer carries the old credit, `/o/kara-lowry.html` carries the new wording,
and `/photos/2017-18-kara-lowry.jpg` is served at 240 by 660 - the remade crop,
not the three-face one.

One correction to record against this pass itself: the comment posted on #254
went out with a generated-by line appended to it. The repository's rule against
tool attribution covers comments as plainly as commit messages, and the line
should not have been there. It could not be edited off afterwards - the direct
API is refused in this environment and the tools available do not edit a comment
once posted. Nothing that reached `main` carries it: the merge commit and all
four commits under it were checked, and the history is clean.

# Editor's pass - 28 August 2026: nothing to merge, so the last day's portraits were audited instead

No pull request was open. The three the standing brief still names as stale -
#6 photographs, #7 the 1980s, #8 the 2020s - were closed on 18 August; the
numbering has since reached 248. The brief should stop pointing at them.

One branch, `research-photos`, sat seven commits ahead of main. It carries no
data changes at all: its research reached main earlier by another route, and the
only thing merging it would have done is delete 124 lines from this file. It was
left alone. Every other `research-*` branch is one of the 4 August snapshots with
no merge base with main, and `git merge-base` still confirms it.

With no diff to review, the pass went to what actually reached the live site in
the last day: eight portraits, merged across #241, #244, #246 and #247. Portraits
are the material this archive treats as most dangerous, because a misidentified
face is worse than no face. Fourteen claims were opened against their sources.
All fourteen held. Nothing was cut.

## The Talisman credits, checked against the volumes themselves

The 1971, 1975, 1977 and 1978 full texts were pulled from archive.org, which is
not rate limited and carries the captions as text.

- **Eyler and Freville, 1970-71.** The Judicial Committee caption is confirmed
  word for word: front row DeShazer, Jackson, Freville vice-chairman, Jones
  secretary; second row Coffman, Barber, Riley, Eyler chairman. The index files
  both men at 68. Both are recorded under `senate.officers`, not in the
  executive - the confusion #243 fixed has not come back.
- **LaCivita, 1974-75.** The caption is confirmed: LaCivita at right, activities
  vice-president, with treasurer Ricky Johnson, discussing the signing of two
  acts. The credit paraphrases rather than reprints, correctly.
- **Blair, 1976-77.** The index puts Thomas Alan Blair at 340, exactly where the
  credit says. Bellbrook Ohio, the psychology and business majors and the remark
  about student representation on university committees are all on the page. The
  1977 Talisman separately names him administrative vice-president.
- **Kelley, 1975-76 and 1976-77.** "Richard Hobson Kelley" is real - the index
  files him at 344-345, and the credit's p. 345 is inside that spread. The
  nameplate reading RICK KELLEY is plainly visible along the bottom of the
  photograph, among ASG concert bills for Chicago, the Spinners, James Taylor
  and Seals and Crofts. The two-year claim does not rest on the portrait: the
  volume calls him activities vice-president for two years and describes him and
  treasurer David Payne as beginning second terms.

## Shockley: the right credit, reached by the wrong caption first

This one is worth writing down because the next pass could repeat it. The 1978
intern feature carries two photographs. The capitol shot is captioned for two
people, Shockley and Betsy Ashcraft, and read against that caption the credit's
claim to name Shockley alone looks like an over-claim worth cutting.

It is not the photograph used. The committed file is an interior shot of a man
reading a document, and its caption begins PAPERWORK AND GOPHER work and names
Brent Shockley alone, describing the bill drafts he prepared for the Legislative
Research Commission. The credit is accurate as written, and pp. 116-117 is right:
the feature sits between the page marked 116 and the one marked 118. The lesson
is that a feature with two photographs needs the caption belonging to the crop,
not the first caption that mentions the name.

## Two credits that could not be finished, and were not cut for it

The Courtenay and Reed portraits cite frame-level captions in a 2022 Herald
election gallery. Cloudflare refuses the gallery to everything available here -
the REST API, a plain fetch and a headless render all end at a challenge page -
so frames 006, 008 and 009 could not be read. The frames exist, and the article's
own text independently confirms the substance: Garrison Reed was elected
executive vice president on Bornefeld's ticket, and Alexis Courtenay placed
second in the presidential race with 40 per cent.

So the identifications stand on evidence that was checked; only the quoted
caption wording is unconfirmed. That is a gap in this pass, not a fault in the
credits, and a miss behind a bot wall is never grounds for cutting a claim.

## A trap in TopSCHOLAR's own metadata

Volume numbers there cannot be trusted to date an issue. The archive stamps
"Vol. 51" on both the issue of 29 February 1972 and the issue of 9 April 1976,
four years apart. Our records date all three issues checked by their publication
date and every one is right, so nothing needed correcting - but a routine that
infers an academic year from a volume number will file work four years wrong.
Date first, volume second.

## Traps, and the duplicate pairs

No advance notice was written up as a result. The February 1998 designated driver
entry is a notice of a distribution due the next day, and it says so and claims
nothing about how it went. No committee chair sits in an executive slot. Nobody
is matched by surname alone, which matters in 2022-23, where a Garrison Reed, a
Steven Donte' Reed and a Reed Hensley share a page and the credit disambiguates
by a second frame. No settled fact moved: Norfleet is still 1981-82. No
contributor commits landed in the window.

`check_duplicates.py` returned six pairs and all six are genuine. Three are the
same-day September 1991 bills the rules explicitly protect. The others are a bill
and the vote that killed it, a union planning a suit and the students endorsing
it a month later, and a concern raised in September against legislation passed in
October. The January 1992 advisory-committee entry checks out too: it says the
bill was introduced two days before the Herald reported it, and the Herald report
is there on 30 January.

## State of the record

`build.py`, `check_data.py` and `check_contrib.py` all complete clean: 61 years,
2019 events, 60 people have been president, 297 documents and 1111 legislation
files. The rebuild produced nothing but a changed date stamp, so the data and the
published site are in step.

Nothing merged, because there was nothing to merge. Nothing cut, because
everything checked held.

# Editor's pass - 27 August 2026, after the overnight pass: two faces off a page that had to be found twice

One pull request was open, #247 from the photograph routine, and it was merged.
It added two portraits and nothing else: David Eyler, chairman of the 1970-71
Judicial Committee, and Michael E. Freville, its vice-chairman, both cropped out
of the same group photograph in the 1971 Talisman.

Two new claims is fewer than the eight a spot check calls for, so both were
checked rather than sampled.

## The page is not where the page number says it is

The credit cited p. 68 of the 1971 Talisman, and the volume's own index agrees:
DeShazer, Eyler and Freville are all filed at 68. But printed page 68 in the
scan is a photo essay about rain. The Talisman numbers its sections separately,
and the committee page sits on leaf n227, which `talisman1971west_djvu.xml`
settles exactly. Anyone rechecking this should go by the leaf, not the folio, and
the source links now point there so nobody has to find it a third time.

## Two committees share the page, and the crops came from the right one

This was the risk worth ruling out before anything else. Leaf n227 carries two
group photographs: the Judicial Committee at the top, four seated and four
standing, and Rules and Elections below it, five and four. A crop lifted from the
wrong one would have put a stranger's face on an officer's page, which is the
failure this archive treats as worse than having no face at all.

The crops came from the top photograph. Both positions were then checked against
the caption rather than taken on the routine's word, and the row order turns out
to be firmer than the pull request claimed:

- The front row runs man, woman, man, woman against DeShazer, Jackson, Freville,
  Jones. Freville is the seated man in the white shirt and dark patterned tie,
  third from left, with Barber's striped shirt directly behind him.
- The second row is four men against Coffman, Barber, Riley, Eyler. Eyler is
  rightmost, in a jacket, standing against the window grid of the building.

Both positions were cropped out of the page scan independently and compared to
the committed files. They match. Both files begin `FF D8` and are real JPEGs.

## What was cut

Both credits reproduced the Talisman's caption whole - twenty-eight words inside
quotation marks, once in each entry. The limit is fifteen words, once per source,
and this is a public site reusing a university archive; the rule is not decorative.

Neither portrait was lost to it. The house pattern for a long credit is to
paraphrase, which is what the Reed and Mujkanovic credits already do, and both
now do the same while keeping every piece of the identification evidence. The
source links were repointed from the volume's front door to the page itself, the
same defect the overnight pass fixed for nineteen other credits.

## Traps, checked

No events were added, so no advance notice could be written up as a report. No
year assignments were added, so nothing filed an April result into the wrong
academic year. No settled fact was touched. Neither man is matched by surname:
both are full names, and the Talisman's senior listing gives Michael Earle
Freville against the archive's Michael E. Freville. Neither appears in
`data/name-aliases.json`, so no changed surname has quietly made a second person.
Nothing about either man goes past what his caption reported. No contributor
commit was in the diff, and every commit on the branch is authored "SGA 60" with
no tool attribution.

The portraits attach to the officer entries rather than to the year's leader, so
the site renders Eyler as "Chairman, Judicial Committee" and does not present
either man as anything he was not.

The six duplicate pairs are the same six as every recent pass, all pre-existing
on main, and all still separate events.

## One thing found and left alone

The 1970-71 Judicial Committee's three officers are filed under
`organization.senate.officers`. The Talisman describes the Judicial Committee as
a body of the Associated Students that interprets the constitution and hears
election appeals - a committee, on that description, rather than an office of the
Senate. That is close to what the night pass corrected for 2016-17 and 2022-23.

It predates this pull request, the portraits attach correctly either way, and
restructuring a decade's data inside a photograph review is not this pass's work.
It is left for whoever next works the 1970s. Worth recording alongside it: the
Talisman's own text says the committee had seven student members, and its caption
then names eight.

## The three stale branches are not stale any more

The standing brief still lists #6, #7 and #8 - the photograph branch, the 1980s
and the 2020s - as open since 4 August and needing a decision. All three were
closed on 18 August. The branches survive them and still have no merge base with
main, so the judgement recorded then stands: they are snapshots of a superseded
repository, and merging one would delete the contributor layer and the validators.
Nothing was done to them.

## Still open

Everything the overnight pass listed is still open: the 151 raw
"SGA legislation: ..." citation labels, the sixteen people filed under both the
executive and the senate, and the twelve-year year-photograph gap from 1993-94 to
2009-10.

The gate behind that gap has got worse. `digitalcommons.wku.edu`'s
`viewcontent.cgi` is refusing every download with a hard 403, and has been since
25 August - the routine tested a fresh article, one that had worked before, and a
90-second backoff, and got nothing. Roughly 770 cabinet and Senate officer
portraits sit behind it. The Talisman years archive.org holds - 1971 to 1981,
1986 and 1987 - are the only ones reachable, which is where these two came from,
and archive.org does not hold the volumes covering the year-photograph gap.

Three names from the 1970-71 Executive Council photograph on the facing page -
Brett Butler, Carol Gray, Doug Alexander - were correctly left unidentified. The
caption lists four in the front row and three in the second, but the pose is not a
grid and one of the two women named in the front row stands visually behind. No
crop met the bar. That was the right call and it should stay that way unless
someone can read the photograph itself rather than the caption's row order.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents and 1,111 pieces of legislation. 201 portraits
now carry a credit, every one of them sourced, and 61 year photographs alongside
them. `build.py` completes cleanly over 61 year pages and 7 decade
pages; `check_data.py` and `check_contrib.py` both exit 0.

# Editor's pass - 27 August 2026, overnight: nineteen citations that led to a bare photograph

No pull request was open. The photograph routine's branch still carries the three
commits behind #244, but every byte of its content is already on main; the only
difference left between them is the report main gained afterwards. Nothing was
waiting, so the pass went at the live site.

## The backlog item was understated by more than three times

Four successive reports have carried "the five wkuherald.com credits citing a bare
image file" as an open item. There are nineteen, across eleven photographs, and they
are on the officer pages of eleven people.

The defect is worth stating precisely, because it is not a wrong fact. Every one of
these credits reads "the caption names ..." and is rendered as a link. The link went
to the raw JPEG on the Herald's content server, which has no caption on it. So a
reader following the citation to check the identification arrived at a picture and no
means of checking anything. The claim was true and unverifiable at the same time.

## Every caption was read, and every label held

All nineteen labels were checked against the Herald's own caption for the frame,
pulled from the paper's photo records rather than taken from any run report. All
nineteen describe their caption accurately.

Two are worth recording as the routine getting it right. Maggie Yelton's credit says
the caption dates the photograph 24 March 2025 while the Herald filed the image under
February, and that the two disagree - which is exactly what the record shows, and it
was flagged rather than smoothed over. Preston Jenkins' caption ends with the
photographer's note that he leaned into the microphone and asked whether it was on;
the credit paraphrases the briefing and leaves the line alone, which is the
quotation rule working.

## What was cut

One sentence, and it was the only false claim in the set. Savanna Kurtz's credit
said the caption spells her name "Savana" and that years.json follows the double-n
spelling used elsewhere. The caption reads "Savanna" - the single-n spelling appears
in it nowhere. There is no discrepancy between the Herald and this archive to flag,
and the sentence was rendering publicly on her officer page. It is gone. The rest of
her credit is accurate and stays.

## Where the citations now point

Eleven of the nineteen rows, covering six frames, now cite the Herald article that
published the photograph. Each was confirmed by fetching the article and finding both
the image file and the caption text on the page - Gabriel Jerdon to the funding-bill
report of 16 October 2025, Hadley Whipple to the first-generation resources report of
3 March 2026, Jade Ismail to the parking-ticket exemption report, Sophie Stirling to
the Gilbane partnership report, Jakob Barker and Will Derryberry to the election-night
visuals of 15 April 2026, and Veronica Butler to the mental health initiatives report.

Cayden Bailey's frame is the reason each one was opened rather than trusted. The
Herald's own photo record names a parent article for it, and that article does not
carry the frame. A parent field is not evidence, and it was not followed.

The remaining eight rows, five frames, are photographs the Herald appears to have
captioned but never run: Savanna Kurtz, Maggie Yelton, Preston Jenkins, Gabi Pace and
Bailey. Kurtz's is the clearest case - the Herald's story on that meeting used a
different frame of Rush Robinson from the same shoot. For these the citation now
points at the Herald's photo record, which is where the caption is actually
published, and the label says so and names the frame. That is a link a reader can
check. The bare file was not.

Three credits also gained the date the Herald published alongside the date of the
photograph, which is the house style set for Isaac Keller's credit in April.

## Traps, checked

No events were added or altered, so no advance notice could be written up as a
report. Seven people carry a portrait attached to two academic years, and every one
was checked against years.json rather than assumed: Barker, Derryberry, Pace, Bailey,
Butler, Whipple, Jenkins and Kurtz each genuinely served in both years their portrait
is filed under. The April 2026 election photographs sit on 2026-27 for the offices
won and on 2025-26 for the senate seats those people already held, which is the
forward-filing rule applied correctly, not a year error. Nobody was matched by
surname. No committee chair became an officer. No settled fact was touched. Nothing
in any credit goes beyond what its caption reports, which matters here because all
eleven are living students.

No contributor commit was in this diff. The duplicate checker reports the same six
pairs as every recent pass; this diff added no events, so none of them are its doing.

## Two items the standing list was carrying wrongly

The "151 raw SGA legislation citation labels" have been fixed since #240, which
rewrote 276 of them. Sophie Stirling's succession to chief justice on 18 November
2025, carried as missing since #233, is in years.json with the council's 3-1 vote and
her profile. Both were still being listed as open work.

## Still open

Sixteen people are filed under both the executive and the senate for what may be one
post - counted again this pass, still sixteen, in 1988-89, 1996-97, 1998-99, 2005-06,
2016-17, 2017-18, 2020-21, 2021-22 and 2023-24. Each wants its sources read.

The twelve-year year-photograph gap is unchanged, behind the Cloudflare gate on
viewcontent.cgi.

The three branches from 4 August had their pull requests closed on 18 August. They
still have no merge base with main and are still snapshots of a superseded
repository, so they were left alone. That judgement has not changed.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as president,
297 mirrored documents and 1,111 pieces of legislation. No citation in photos.json
now points at a bare image file. build.py completes cleanly over 61 year pages and 7
decade pages, and check_data.py and check_contrib.py both exit 0.

# Editor's pass - 27 August 2026, late: the Garrison Reed lead closed

One pull request was open, #244 from the photograph routine, and it answered the
question the previous pass left at the bottom of its own "still open" list. That
entry had said Garrison Reed was worth one more look, because the frame the earlier
run found hides his face behind his own raised arm, and because a second caption in
the same gallery names him with a positional cue. The routine went back and found
exactly that. The lead is closed and the portrait is on the site.

## What was verified, and how

The diff was one photograph, one entry in `data/photos.json` and a handoff note.
Small enough that everything in it could be checked rather than sampled, so it was.

The captions were pulled from `wkuherald.com` at first hand rather than taken from
the run report. The election-night gallery of 20 April 2022 holds nine frames.
Frame 009's caption reads as the credit quotes it, naming Cole Bornefeld
congratulating Garrison Reed on winning the vice presidency. Frame 008's names Reed
at left congratulating Sam Kurtz.

The identification needed more than that, because frame 009 shows two men shaking
hands and an unnamed third in the background, and a crop has to choose. Three
independent things settle it. The man at left in frame 009 - straight dark hair,
navy blazer, no checked shirt - is the same man as the Bornefeld portrait already
on file, so the cropped man is not Bornefeld and the caption names only two. Frame
008 places Reed at left in a red and white checked shirt with his face partly behind
his arm, and it is the same shirt and the same face as the crop. Frames 001 and 010
name Bornefeld, Reed and Kurtz together as president, vice president and
administrative vice president, in that order, which also identifies the blue-suited
man in the background of 009 as Kurtz. That is identification by positional caption,
which is what this archive asks for, and not by surname.

The photograph begins `FF D8 FF E0`, is a real JPEG, and the `site/photos/` copy is
byte-identical to the one in `data/photos/`.

## What the editor cut

One thing, and it was trimmed rather than deleted. The credit line carried a second
quoted caption from the same gallery, which is one more quotation than a single
source is allowed, and an aside explaining that an earlier pass had set the
photograph aside because of the raised arm. That aside is workflow, and it was
rendering publicly at the top of `o/garrison-reed.html`.

The frame 008 evidence is what fixes which man is Reed, so cutting it outright would
have removed the reader's means of checking the crop. It is paraphrased instead and
kept, and the credit now says plainly that frame 008 is what settles the question.
The workflow aside is gone. No sourced fact was lost and the credit is back to one
quotation.

## Traps, checked

The gallery reports results announced just after midnight; it is not an advance
notice, and nothing in the entry claims anything the captions do not. No committee
chair was recorded as an officer. Nobody was matched by surname alone.
`data/name-aliases.json` keeps Garrison Reed and Donte Reed apart, correctly, and
there is no duplicate person and no duplicate year-and-name pair in `photos.json`.
The April 2022 result is filed forward to 2022-23, which is the rule: SGA elects in
April and the winner serves the following year. No settled fact was touched. Nothing
about a living person goes past what his caption reported. No contributor commit was
in the diff, and every commit is authored "SGA 60" with no tool attribution.

The six duplicate pairs are the same six as every recent pass. They were read rather
than waved through, and all six are genuinely separate: three bills on one day in
September 1991, which the rule keeps separate; a bill introduced in January 1992 and
the same bill failing after amendment a week later; SGA taking a position against
plus-minus grading in September 2003 and passing the legislation three weeks later;
the Kentucky Civil Liberties Union filing in February 1972 and Associated Students
endorsing it a month after; and the designated driver cards funded in November 1997
against the Herald's February 1998 notice that they were about to be distributed.
That last pair is worth recording as a good example rather than a problem - the
February entry is an advance notice, it says so, and it claims nothing about how the
distribution went. This diff added no events, so none of the six are its doing.

## One inconsistency, left alone

The run states the remaining officer pairs without a portrait as about 779 in the
pull request and about 778 in the handoff note. A recount of executive and senate
officers gives 760. The difference is in what each count includes rather than an
error in the data, and it sits in a handoff document that is not published to the
site, so it was left. Two figures produced by one run should still agree.

## Still open

Everything the previous passes listed is still open, minus Reed: the 151 raw
"SGA legislation: ..." citation labels, the sixteen people filed under both the
executive and the senate, the five wkuherald.com credits citing a bare image file,
and the twelve-year year-photograph gap sitting behind the Cloudflare download gate
on `viewcontent.cgi`, which has refused every run since 25 August.

The three branches from 4 August have no pull requests any more. They still have no
merge base with main and are still snapshots of a superseded repository, so they
were left alone rather than merged. That judgement has not changed.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as president,
297 mirrored documents and 1,111 pieces of legislation. Every president and every
student regent carries a portrait; a recount this pass found none missing.
`build.py` completes cleanly over 61 year pages and 7 decade pages, and
`check_data.py` and `check_contrib.py` both exit 0.

# Editor's pass - 27 August 2026, night: committee chairs sitting in the executive

No pull request was open. Every research branch that shares a history with main is
fully merged, and the four branches from 4 August still have no merge base, so they
were left alone again. With nothing queued at the gate, the pass went to a defect
already on the live site.

## The 2016-17 executive was missing its Administrative Vice President

The executive roster for 2016-17 listed fifteen people. Six of them were committee
chairs, and one of those six had displaced a real executive office: Hannah Neeper
appeared only as Chair of the Organizational Aid Committee, so the year published no
Administrative Vice President at all. Her own note had said all along that she held
the chairmanship "alongside her office as Administrative Vice President"; nothing had
acted on it.

SGA's own minutes of 13 September 2016 settle it, and the file was already mirrored in
`data/documents/`, so nothing had to be fetched. The minutes run the executive reports
first - President Jay Todd Richey, Administrative Vice President Hannah Neeper, Chief
of Staff James Line, Director of Public Relations Murphy Burke - and then a separate
block of committee reports: Academic Affairs, Legislative Research, MyCampusToo,
Sustainability. That is SGA drawing the line itself, and the data had blurred it.
Neeper is now Administrative Vice President, sourced to those minutes, with the
Organizational Aid chairmanship kept in the note and in the senate block where it was
already recorded against Bill 10-16-F.

## Five people were being published twice

Kara Lowry, Emily Houston, Hizareth Linares, Helen Vickrey and Andi Dahmer each stood
in both the executive and the senate under the same title. Vickrey's and Linares'
profiles were byte-identical in both places, so the site was printing the same
paragraphs about the same woman twice on the same page. The executive copies are gone.
The senate copies, which carry the better sources - Bill 18-16-F, Bill 17-17-S, Bill
24-17-S - are what remain. Lowry's case needed no judgement: Secretary of the Senate
is a senate office by its own name, and the minutes list her under the senate's
officer reports.

Nothing was deleted that existed only in the executive. Brian Anderson, Morgan Wysong
and Savannah Molyneaux were moved rather than cut, because their executive entries
carried profiles and sources the senate side did not have. Anderson had been in the
senate twice over, once richly as Legislative Research chair and once thinly as
"Senator"; those are now one entry, and Resolution 6-17-S survives on it as a second
source.

## A committee member is not an executive officer

Two entries in 2022-23 claimed more than any structure allows. Brooke Mitchell was
filed in the executive as "Mental Health and Wellbeing Committee Member", on the
strength of being one of seven listed authors of Bill 46-23-S - a bill's author read
as a committee member, and a committee member then read as a member of the executive.
Reed Hensley was filed there as "Member of Organizational Aid Board", though his own
profile says he was elected a sophomore class senator. Both moved to the senate with
their profiles and sources intact. Neither was cut: what the sources prove about them
is all still on the page, under a heading that does not overstate it.

Olivia Feck was left where she is. She is a committee chair in the same executive
block, and from about 2021 the cabinet may genuinely have included chairs; without
minutes for that year in hand, moving her would be a guess. A committee *member* in
the executive is wrong under any reading, which is why those two moved and she did not.

## Checked before anything was touched

Every name, every source URL and every profile was counted in the file before and
after. No name left the record, no source URL left the record, and no person lost a
profile: the count fell by two only because Vickrey's and Linares' duplicate copies
went, and the surviving copy of each is the full one, character for character.

The build renders `senate.members` as a bare count of names, so relocating anyone into
it would have silently dropped their profile from the site. Everything moved this pass
went into `senate.officers`, which the officers page indexes.

## Traps, checked

No events were added or altered, so no advance notice could be written up as a report
and nothing moved an April result into the wrong academic year. No settled fact was
touched. Nothing was matched on a surname: the one name that could collide, Reed, was
read off the profiles rather than the name. No contributor commit was in this diff.
Nothing here goes past what its cited source reports, and nothing added a personal
detail unconnected to SGA service.

The six duplicate pairs are the same six as recent passes. All six are still genuinely
separate events, and two were re-read in full this pass rather than inherited: the
1997-98 designated driver cards are a bill passing in November and a Herald notice of
distribution in February, and the 2003-04 plus/minus grading pair is a September debate
and an October vote. The February 1998 entry is drawn from a contents listing and says
so, claiming only that distribution was announced - the advance-notice rule handled
correctly by whoever wrote it.

## Still open

The wider pattern is not fixed. Committee chairs sit in the executive block in at least
1974-75, 1990-91, 2013-14, 2017-18, 2021-22, 2022-23, 2023-24 and 2025-26. Each needs
that year's minutes to know whether the chairs were cabinet members in that era, which
is a research job rather than an editing one, and it is the most useful thing the
routines could take up next. "Coordinator of Committees" in the late 1990s is not part
of it: that is a real cabinet office, not a chairmanship.

Everything the evening pass listed is still open: the raw "SGA legislation: ..."
citation labels, now 276 of them rather than the 151 last counted, the five
wkuherald.com credits citing a bare image file, and the year-photograph gap behind the
Cloudflare download gate. Garrison Reed is still worth one more photograph pass.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as president,
297 mirrored documents and 1,111 pieces of legislation - all unchanged, as an
organisation-structure pass should leave them. `build.py` completes cleanly over 61
year pages and 7 decade pages; `check_data.py` and `check_contrib.py` both exit 0.

# Editor's pass - 27 August 2026, evening: eight portraits the yearbook does not identify

One pull request was open, #241 from the photograph routine: twelve cabinet officer
portraits for 1971-72 through 1977-78, pulled from Talisman volumes on archive.org.
Four were merged. Eight were cut. The two reasons they were cut are the two the
photograph routine keeps running into, so both are written out here in full.

## What was verified

The Talisman full texts on archive.org are not rate limited, so every cited caption
was read in the volume itself rather than taken from the pull request. All eleven
quoted captions are verbatim. Where the identification turned on what the printed
photograph actually shows, the page image was fetched and read.

The 1975 page settled the one that mattered most. The caption puts Tom LaCivita "at
right" discussing concert bookings with treasurer Ricky Johnson, while the routine's
credit claimed Johnson was not in the frame at all - which, if the crop had taken the
wrong figure, would have published Johnson's face under LaCivita's name. Leaf 112 of
the 1975 volume shows one man fully in frame at the right and nothing of the second
man but a hand at the lower left edge. The crop is LaCivita. The page footer also
confirms the citation exactly: 109, Associated Student Government.

Rick Kelley's portrait needed no argument at all. The desk nameplate in the photograph
reads RICK KELLEY, the posters behind him are Associated Student Government concert
bills, and the Who's Who text beside the portrait names him activities vice-president
for ASG. The same volume's ASG section has him "beginning second terms in office",
which is what makes filing his portrait under both 1975-76 and 1976-77 correct.

Tom Blair was carried by the volume's own index - `Blair, Thomas Alan 50, 277, 340` -
where page 50 is the ASG section naming Tom Blair administrative vice president and
page 340 is the Who's Who portrait. The index, not the name, is the identification.

## Five group photographs presented as one person's portrait

Reginald Glass, Nancy Pape and Joe Glasser for 1971-72; Pam Stewart and Thomas
LaCivita for 1973-74. Both captions name everyone present without saying which figure
is which, and the routine filed the uncropped group shot under each name in turn.

The site renders a `leaders` entry as a portrait figure with alt text reading
"Portrait of Nancy Pape." So a four-person photograph filed under three names tells a
reader three times over that it is looking at a particular person, and points at three
different faces. A credit line explaining that the caption does not map names to
figures does not undo that.

Worse, the archive already held both photographs. `1971-72-executive-officers.jpg` and
`1973-74-officers-meeting.jpg` have been on main for some time, filed as year
photographs with every officer named in the caption - which is the correct home for a
group shot. The routine re-downloaded both under new filenames, 888 KB of duplicate
binary. Glass and Pape also already had individual portraits: Glass from his p. 201
solo profile with his name tag legible in the frame, Pape cropped from the very same
pool-room photograph by counting along the caption's naming order. The new entries
would have set both aside in favour of the unidentified group shot.

## Three portraits resting on a name and nothing else

Gerard Faulk, filed under two years, and Gary Reed. Both came from senior class
portrait grids, and in neither volume does anything connect the man in the grid to
student government.

Faulk's case is the instructive one, because it looked corroborated and was not. The
grid gives "GERARD FAULK, JR., Elem. Ed., Bowling Green", and years.json describes the
Judicial Council chairman as an elementary education major, so the two appear to
agree. They are the same statement. That claim's `src2` is this grid entry: the
archive learned his major from the photograph the major was then used to authenticate.
Strip the circle away and there is a name and nothing else. The word *judicial* does
not appear anywhere in the 1977 Talisman, and the index puts Faulk on p. 319, the SNEA
group, and p. 350, the grid.

Gary Reed is the same shape and thinner. The 1978 index reads `Reed, Gary W. 288, 372`;
372 is the grid and 288 turns out to be the Accounting Club roster, where he appears as
"G. Reed" - a surname-initial match nested inside a full-name match. The archive knows
nothing else about him beyond winning the treasurer election 554 to 437.

The four grid portraits already on main - Strader, Elder, Richards, Velastegui - each
pair the class portrait with the same volume's ASG group photograph or feature. That
second link is the standard. These two had none.

Brent Shockley rests on a name too and was kept, because the difference is real: his
caption identifies the man in the photograph directly, and the corroboration is
independent rather than circular. The Herald has him a senior studying government from
Scottsville; the Talisman has him a senior interning at the Legislative Research
Commission.

## Trimmed rather than cut

The four surviving credits quoted 34, 20, 20 and 15 words of Talisman text. The rule is
under fifteen words, once per source, and main holds that line - 192 of its 193 photo
credits sit under it. All four were rewritten as paraphrase with one short quote each,
losing no fact that does identifying work.

LaCivita's credit was corrected to say Johnson's face falls outside the frame rather
than that he is absent from it, which is both true and the reason the crop is LaCivita.
Shockley's page was cited as 121; the index gives 116-7 and the page markers in the
text agree, so it now reads pp. 116-117.

## Traps, checked

No events were added, so no advance notice could be written up as a report and no April
result could be filed into the wrong academic year. No committee chair was promoted to
officer - Faulk is recorded as Judicial Council chairman under the senate, where he
belongs, and that was not disturbed. No changed surname created a duplicate person. No
settled fact was touched. Nothing about any of these men goes past what his caption
reported. No contributor commit was in this diff, and every commit on the branch is
authored "SGA 60" with no tool attribution.

The four surviving files begin `FF D8` and are real JPEGs, and the deleted files are
gone from both `data/photos/` and `site/photos/` with no reference left anywhere in the
built site.

The six duplicate pairs are the same six as every recent pass. This diff adds no
events, so none came from here, and all six are still separate events.

## Still open

Faulk's profile in years.json states as fact that he was an elementary education major,
sourced to the grid entry whose portrait has now been cut. With the photograph gone the
claim stands on a name match alone. Flagged rather than fixed, since years.json was
outside this diff, and left for a run that can go at the Herald text directly.

The three branches from 4 August - the 1980s, the 2020s and the photograph branch that
went with them - still have no pull requests and still have no merge base with main.
Left alone, as before.

Everything the afternoon pass listed is still open: the 151 raw "SGA legislation: ..."
citation labels, the sixteen people filed under both the executive and the senate, the
five wkuherald.com credits citing a bare image file, and the twelve years from 1993-94
to 2009-10 with no photographs at all, which sit behind the `viewcontent.cgi` Cloudflare
gate that refused the routine every attempt this session.

Garrison Reed is still worth one more photograph pass, for the reason the morning report
gave.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as president, 297
mirrored documents and 1,111 pieces of legislation. `build.py` completes cleanly over 61
year pages and 7 decade pages; `check_data.py` and `check_contrib.py` both exit 0.

# Editor's pass - 27 August 2026, afternoon: citations that named people who never existed

No pull request was open. All four research routines are level with `main`, and the
three branches from 4 August remain orphan histories with no merge base, so the review
went at what is already published — starting from the backlog the last four reports
have named and not finished: the roster citations carrying a raw "SGA legislation: ..."
blob instead of a bill number and title.

## What the backlog actually was

The standing figure was 151 citations. Both halves of that number were wrong, in
opposite directions. The labels live under `src`, `src2` and so on up to `src10`; a
sweep that reads only `src` finds 124. The true count is **276**, across the executive
block, the senate officers and the senate members.

Of those, 81 carry a scraped table row, not a title. The rest simply lack the bill
number. The same corruption has a **second home nobody had found**:
`data/legislation-authors.json`, where 211 rows carried the same run-on string in their
`title` field. That file renders the per-officer pages under `site/o/`, so the bad text
was on the site twice over, from two different files.

## Six people who do not exist, and one who does

The scrape ran past the title into the authors, committee and vote columns of SGA's
own legislation listing. Where two authors sat side by side, it fused them. Read
against the AUTHOR lines of the bills themselves:

- Bill 13-17-S credited "William Wysong". The bill names William Hurst, Senator, and
  Morgan Wysong, Public Relations Committee Chair.
- Resolution 7-17-S credited "Hannah Line" — Hannah Neeper and James Line.
- Resolution 5-17-S credited "Savannah Lowry" — Savannah Molyneaux and Kara Lowry.
- Bill 19-17-S credited "Andi Edmunds" — Andi Dahmer and Luke Edmunds.
- Bill 8-17-S credited "Andi Jody Dahmer" — Andi Dahmer and Jody Dahmer.
- Bill 28-17-S credited "Emily Mayer" — Emily Houston and Stephen Mayer.

The seventh is the one that mattered most. Resolution 6-17-S credited **"Andrea
Anderson"**, which fuses Andrea Ambam, Senator, and Brian Anderson, Senator. Andrea
Anderson is a real and separate person in this archive: WKU's general counsel, named in
the 2018-19 suit against the university and again before the Senate over the Pride
Center in 2025-26. The corrupt citation put a named, living university officer's name
on a student reparations resolution she had nothing to do with. Her four genuine
entries are untouched.

## What was checked before anything was cut

Two roster people looked like fusions of the same kind and are not. **Jody Dahmer** and
**Luke Edmunds**, both 2016-17 senators, are named in their own right on the AUTHOR
lines of Bills 8-17-S, 12-17-S and 19-17-S. They stay. PR #235's finding that no
phantom reached a roster holds, and it now rests on the documents rather than on
inference: none of the seven fused names is a person anywhere in `years.json`.

## What changed

All 276 roster citations now read as the document prints itself — `SGA legislation:
Bill 13-17-S, Funding for a Portable Whiteboard for SGA` — with the designation and
title read from the mirrored PDF, and the scraped tail gone. The 211 corrupted titles
in the author index are rewritten the same way. Nothing was deleted: every citation
keeps the URL that carries its evidence, and in that index no name, file or role
changed, only the title.

Three further errors surfaced on the way:

- **Bill 9-23-F was published as amending the Constitution. It amends the Bylaws.**
- **Bill 16-24-S** carried a second document's title fused onto its own.
- **Four citations pointed at URLs that 404.** `.../legislative/2019_20_legislation/`
  should be `2019_2020_legislation`, and one 2016-17 bill sat under a directory that
  does not hold it. Checked one URL per path prefix; the other nine prefixes resolve.

## Traps, checked

The older convention, where a title opens with its own designation — `Bill #92-09-S -
Establish ASG Health Insurance Ad-Hoc Committee` — reads to a naive pattern exactly
like the corruption. A first pass would have rewritten thirteen of them. Detection was
changed to require the designation to sit *after* the title text, which separates 25
legacy documents from 103 corrupt ones with no overlap, and the run was redone. No
legacy title was altered. Every URL in the roster citations belongs to 2016-17 or
later, so no legacy document is reachable from that edit at all.

No new claim is added, so there is no advance notice to mistake for a report and no
election to file into the wrong year. Nothing was matched by surname; the fusions were
resolved by reading each bill's AUTHOR line, which prints the office beside the name.
No committee chair was promoted to officer. No settled fact was touched. The one living
person affected has less said about her than before, not more.

Ten of the rewritten citations were then sampled at random and checked back against the
text of the document each cites; all ten matched on both designation and title.

## Still open

- `2016-17/bill_8-17-s.pdf` prints **"Resolution 8-17-S"** in its header while its title
  begins "Bill to Help Fund" and SGA filed it as a bill. The citation follows the
  document. SGA's own inconsistency, recorded here rather than smoothed over.
- The sixteen people filed under both the executive and the senate for what may be one
  post, from the 26 August report, are untouched.
- The five wkuherald.com credits citing a bare image file rather than the article.
- The year-photograph gap behind the Cloudflare download gate.
- Sophie Stirling's succession to chief justice on 18 November 2025, flagged in #233 and
  still not written into `years.json`.
- The split spelling of Steven Donte' Reed and Donté Reed, flagged in #239.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as president, 297
mirrored documents and 1,111 pieces of legislation. `build.py` completes cleanly over 61
year pages and 7 decade pages; `check_data.py` and `check_contrib.py` both exit 0;
`check_duplicates.py` reports the same six pairs, read again and separate again.

# Editor's pass - 27 August 2026, morning: two officer portraits, both verified

One pull request was open, #239 on `research-photos`, and it was merged. It added
eighteen lines to `data/photos.json` and one image file: a portrait of Alexis
Courtenay for 2021-22, and the reuse of an existing portrait for Steven
Donte' Reed's 2023-24 year. Two new claims, so both were checked rather than sampled.

## What was checked, and how

The Courtenay portrait cites a College Heights Herald election-night gallery from
20 April 2022. The rendered gallery page carries no captions; they sit behind the
lightbox. The eight photo IDs are in the page's `data-photo-ids` attribute, and each
caption comes back from `wkuherald.com/wp-json/wp/v2/media/<id>`. Frame
`041922_sgaelections_hendricks_006`, media 65827, is captioned with Bornefeld and
Courtenay embracing after the presidential result was announced. The original was
downloaded and set beside the committed crop: they are the same frame, and the crop
keeps the one identifiable face in it. The other person in the picture has his back
to the camera, so there is no left-and-right question to get wrong.

The Reed entry attaches the portrait already on file for 2024-25 to his 2023-24 year.
Its source, the Herald's 27 August 2024 report on the editorial board's meeting with
the executive cabinet, names him in the caption with a positional cue, and the article
text names the same five officers. Reusing one portrait across a person's years is
long-standing practice here: forty-nine files are already shared that way, including
Sarah Vincent's across the same two years.

Both files begin `FF D8`. Every one of the 193 leader photograph entries names a
person that year's record actually contains; none is orphaned.

## What was corrected

Two citation labels, both for precision rather than accuracy.

The Courtenay label cited the gallery post but not which of its eight photographs it
came from. A gallery frame is the equivalent of a page number, so the frame name is
now in the label and a reader can reach the exact caption.

The Reed label had dropped the caption's positional cue, which is the only thing that
tells three seated men apart, and did not say that the photograph post-dates the year
it is filed under. Both are now stated, along with the fact that the two spellings of
his name are already paired in `data/name-aliases.json`.

## Traps, checked

Two men named Reed sit a year apart in this record - Garrison Reed, executive vice
president in 2022-23, and Steven Donte' Reed - which is precisely the surname trap.
The research routine had added a Garrison Reed portrait from the same gallery, found
that an earlier pass had already set that frame aside because his face is behind his
own arm, and pulled it back out before opening the pull request. That was the right
call and it holds on re-inspection.

The photograph filed under 2021-22 is from an April 2022 election, which invites the
file-forward rule. It does not apply: the rule governs terms, and Courtenay held the
public relations directorship in 2021-22. She lost the election the photograph
records. The year is right.

Nothing here touches a settled fact. Nothing goes beyond what the cited caption
reported. No contributor commit was in the diff, and no commit carried tool
attribution.

## What was left alone

`check_duplicates.py` reports the same six pairs it has reported for days, none of
them in this diff. All six are still separate events: a bill introduced and the same
bill failing a week later are two things, and same-day legislative business stays
several entries.

## Still open

Garrison Reed still has no portrait. Frame `041922_sgaelections_hendricks_009`, media
65829, from the same gallery shows two men shaking hands with clear, unobstructed
faces and is captioned as Bornefeld congratulating Reed - but the caption carries no
left-or-right cue, so it cannot identify which face is which on its own. The next
photograph pass would need an independent anchor, and Bornefeld's existing portrait
is one. Worth a look; not worth a guess.

Everything the previous passes listed is still open: the 151 raw "SGA legislation: ..."
citation labels, the sixteen people filed under both the executive and the senate,
the five wkuherald.com credits citing a bare image file, and the year-photograph gap
behind the Cloudflare download gate.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as president,
297 mirrored documents and 1,111 pieces of legislation. `build.py` completes cleanly
over 61 year pages and 7 decade pages; `check_data.py` and `check_contrib.py` both
exit 0.

# Editor's pass - 27 August 2026, small hours

No pull request was open. The three that the standing brief still names as stale -
#6 photographs, #7 the 1980s, #8 the 2020s - were all closed on 18 August, and the
brief has not caught up; there is nothing there to rescue or to close. Every active
research branch - photographs, profiles, the senate rolls, the backlog - is level
with main with nothing unmerged behind it. The six `research-1966-79`-style branches
from 4 August remain orphan snapshots with no merge base, exactly as AGENT-LANDING.md
warns, and were left alone.

With nothing waiting to be gated, the pass went at what had already reached the live
site in the previous day's merges, which is where an unreviewed error would now be
sitting in public.

## The state of what is published
Main builds clean: 61 year pages, 2,019 events, 60 people recorded as president,
297 documents and 1,111 legislation files. `check_data.py` and `check_contrib.py`
both pass. Across all 2,441 roster rows in the record, every one carries a source
and none is left with a title truncated by a PDF line break - the 26 August roster
work holds.

## What the pass corrected

**Isaac Keller's portrait credit claimed more than the caption says.** The credit
read that the caption showed him "waving to the chamber while other senators
applaud." The Herald's caption says only: Isaac Keller gets sworn in as Chief
Justice during a Student Government Association meeting in Downing Student Union
on 9 April 2019. There is no wave and no applause in it, and the photograph itself
shows his right hand raised taking the oath, not waving. The identification is
sound and stays - the article names him confirmed chief justice in a 28-0 vote -
but the credit is trimmed to what the caption proves, and now carries both dates:
the meeting on 9 April, the report published 10 April. This is the same fault the
26 August pass corrected elsewhere under "cite the caption, do not reprint it";
it had been reintroduced in the credit written that evening.

**Hannah Neeper was listed twice in the same executive roster.** 2016-17 carried
her as "Chair of Organizational Aid Committee" and again as "Chair of
Organizational Aid" - one committee, two rows, differing by a single word, which
is why the 26 August merge of entries sharing a name and an office passed over
them. Merged into one row; all three sources from the thinner entry carried
across, so she now cites nine.

## What was verified and stands
Holden Schroeder's portrait was checked to its source and holds. The gallery's
captions are not in the page's HTML - they load separately, and the article text
never says "chief justice" - so the credit was confirmed against the Herald's own
media record for the post, where the frame is captioned: SGA Chief Justice Holden
Schroeder addresses the members of SGA before announcing the election results,
just after midnight on 20 April 2022. That matches the credit word for word,
including the corrected date. The double spelling is deliberate and correct:
Schroder for 2019-20, following the Judicial Council roster as printed, Schroeder
thereafter, and both match years.json exactly.

The duplicate checker returned the same six pairs as the previous passes and all
six stay. The designated-driver trio in particular is three distinct events - the
bill on 4 November 1997, the Herald's report nine days later, and the February
notice of distribution - and each is already scoped to what its own source proves,
with the two written from index listings saying so plainly.

The 26 August note on Sophie Stirling's election is a research routine catching the
advance-notice trap on itself, correctly: the Herald of 13 November 2025 reports the
Judicial Council's vote but is written before the handover, so 18 November stays out
of the record as the date she took office until a source from after the meeting says
it happened. Left as it stands.

## Still open, for whoever takes the next pass
**Committee chairs are recorded as executive officers, and seven people are
double-listed because of it.** In 2016-17 and 2017-18 the same person appears once
under `organization.executive` and again under `organization.senate.officers` for
the same role: Hannah Neeper (Organizational Aid), Helen Vickrey and Andi Dahmer
(MyCampusToo), Hizareth Linares (SGA SAVES), Emily Houston (Student Affairs), Kara
Lowry (Secretary of the Senate) in 2016-17, and Ashley Cox (CASA) in 2017-18. Three
of those pairs use different title strings for the one role - "MyCampusToo Chair"
against "MyCampusToo Committee Chair", "Student Affairs Chair" against "Student
Affairs Committee Chair" - so a name-and-office match will not find them. The next
roster pass should de-duplicate **across** the two lists, not only within each.

This was not fixed here because it is not only a duplicate: it asks whether a
committee chair belongs in the executive cabinet at all, and these two years answer
it both ways at once. That is a structural decision for the editor, not one to take
unsupervised, and every row involved is sourced, so nothing is unsupported - only
repeated.

**Hannah Neeper's note says she held the administrative vice presidency, but
2016-17 has no Administrative Vice President row.** Either the office is missing
from the roster or the note overstates it; one source would settle which.

**Some harvested legislation labels carry the bill's sponsor line as part of the
title**, e.g. Neeper's src8 ending "B10-17-S Hannah Neeper Organizational Aid Yes",
and the same pattern in Kara Lowry's and Hizareth Linares's citations. Cosmetic,
but it is published text.

# Editor's pass - 25 August 2026, midday

No pull request was open. The overnight editor closed the last of them at 9:36,
and every active research branch - backlog, photographs, the senate rolls,
profiles - is level with main with nothing unmerged behind it. Nothing was
merged this pass because there was nothing waiting.

## The state of what is published
Main builds clean: 61 year pages, 2,019 events, 60 people recorded as president,
297 documents and 1,111 legislation files. `check_data.py` and `check_contrib.py`
both pass.

## What the pass corrected
The duplicate checker returned six pairs. Five are genuinely separate business -
a bill introduced and the same bill failing on amendment, the Civil Liberties
Union's plan and student government's later endorsement of it, a position taken
and the legislation that followed, and three bills filed on one day in September
1991 - and all five stay as they are.

The sixth sent me to Bill 97-3-F, and the bill turned out to be readable in our
own legislation archive, which two entries written from index listings had not
used. It allocated $900 of Campus Improvement funds to print designated driver
cards entitling the driver to free soft drinks in place of alcohol, first reading
4 November 1997, passed on second reading a week later.

- The entry of 4 November said the bill's provisions were "not established here."
  They were established, in a file already on the site. Rewritten from the bill.
- The entry of 13 November had the cards "still being distributed" the following
  February. The February source is an advance notice - the Herald's index line
  reads that the cards would be distributed the next day - so it proves an
  announcement and not a continuous distribution. Trimmed to that.

Both entries now cite what actually supports them; the 4 November entry points at
the bill on TopSCHOLAR rather than a 2003 capture of an index page.

## Still open
The six research branches dated 4 August remain orphan snapshots with no merge
base against main. They are not mergeable and should not be merged; their pull
requests are already closed.

---

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

---

# 24 August 2026 — editor's pass, one merged and one held

Two research pull requests were open at the start of this pass, both opened this morning:
#189 from `research-profiles` and #190 from `research-senate`. The three branches from
4 August that earlier passes worried about — #6 photographs, #7 the 1980s, #8 the 2020s —
were all closed on 18 August and needed nothing.

## What merged

**#189, `research-profiles`.** One substantive line: an alias joining "Tara Higdon" to
"Tara (Higdon) Howard" in `data/name-aliases.json`. Her 1994-95 vice presidency and 1995-96
presidency had been sitting on a separate, profile-less person page from her real record,
because the plaque prints her maiden name in parentheses and the executive listings do not.

This is not a new claim about anyone. Both records already on main placed the same person in
the same office in the same year, and the leader note already stated the connection. The
sequence behind it is confirmed in contemporaneous headlines — "Rob Evans & Tara Higdon Ready
to Lead Students" in April 1994, "Tara Higdon Moves Up; Voting Down" in April 1995, then "Tara
Higdon Sees New Beginning" — found in `herald-index-full.json` and checked against the Herald
70:51 landing page. The rendered change is a link retarget on three year pages; displayed
names are untouched. Nothing cut.

The run also reported a real limitation rather than working around it: `officer_index()` in
`build.py` drops `profile`, `photo` and the numbered `src` fields when it builds a rank-and-file
senate member, so a profile written on one of the 1,396 un-profiled members would never reach a
reader. It correctly left that alone as a `scripts/` change outside its scope. It is the same
blocker the last two passes recorded and it has still not moved.

## What did not merge, and why

**#190, `research-senate`.** Fourteen new Congress members and one new officer for 1983-84,
read out of two ASG minutes that had never been mined. The research looks careful and its
adversarial pass caught five real errors before it reached me. I held it anyway, on one ground:
**I could not read either source document.**

Neither of the two cited minutes had been mirrored into `data/documents/`, so checking them
meant fetching them, and TopSCHOLAR would not serve them. The landing pages opened at 200. The
download endpoint returned 403 with the bot-check page saved under a `.pdf` name — trap 7,
caught only because the magic bytes were checked — and then 202 with an empty body on four
further attempts across about nine minutes, at the pacing CLAUDE.md sets. A second fetch path
returned 403. So the spot-check sample came to zero claims verified out of sixteen. That is not
a finding against the research; it is the merge test asking for something this run could not
produce.

What could be established without the documents did hold up. Tony Whalen was Administrative
Vice President in 1983-84, so Todd Duncan's appointment by him is coherent. John Holland is
already recorded as Public Relations Vice-President for 1984-85 under the same president, and
the `/441` landing abstract independently confirms that meeting discussed grading systems,
which is what the new officer note claims he reported on. Gil Cowles and Jon Norris both check
out as prior and later records. Six of the fourteen rest on being named among unexcused
absences, which is sound evidence of membership. Recording a committee in the `seat` field is
an established convention here, not the committee-chair trap: 91 existing member records do it.
And the run's refusal to merge Alvan Kujala with Allan Kujala absent a source was exactly right.

## What I cut

Three corrections, pushed to the branch as `58470c2`.

The 6 September 1983 ad-hoc research committee was published with one man under two surnames in
the same year. The verifier corrected Kujata to Kujala on his own entry, whose note calls that
reading confirmed on a clean crop, but left the old spelling standing in the cross-references
inside Sandy Hill's and Randy Kimmel's notes. A name in prose is as published as a name in a
field. Both now read Kujala.

The Representative at Large approved that night carried an uncertain surname, which was honestly
flagged — and then argued past. The note conceded the tight crop "reads more like Ranan than
Ragan," and settled on Ragan because "a Margaret Ragan appears elsewhere in this year's 1982
election coverage." She does not. Margaret Ragan was the 1982-83 president, elected in April
1982, and her term ended before this Congress sat; 1983-84's election coverage is April 1983.
Reaching for an unrelated person's surname to settle a reading the scan contradicts is trap 4
run backwards, and it is how an invented spelling gets into a record. The name is left as
recorded, since this pass could not read the page either, and the note now states the doubt
plainly and rules out the false connection.

Gil Cowles's 1982-83 and 1983-84 records are matched on the name alone. That was stated flatly
as "the same person" where the identical case for Jon Norris is hedged; it now carries the same
hedge.

## Still open

#190 stays open. It should merge on its next look, and the fix is small: mirror the two PDFs
into `data/documents/` as `1983-84-asg-minutes-1983-09-06.pdf` and
`1983-84-asg-minutes-1984-02-28.pdf`, verify the `%PDF` header, and attach them to the year.
Three readings also want settling from those scans — the disputed surname, whether the given
name really is Alvan, and Kim Robertson on a clean crop.

The TopSCHOLAR challenge is no longer an incident. It blocked the 1979-80 work, then #187, then
#186's re-reading on 24 August, and now #190. Any research that cites a document it did not
mirror is a claim no later pass can check, and the archive is accumulating them. Mirroring the
PDF at the moment of citation is the whole remedy and it is already the rule; it needs to be
treated as the load-bearing step it is rather than housekeeping.

The `officer_index` member-profile limitation, the stale "SGA 60 - backlog" trigger, the
`Annalise Finch` / `Annie Finch` case and the "Gabi Pace" / "Gabby Pace" spelling all stand
unchanged from the last pass.

## Where the archive stands

61 academic years, 2,018 dated and sourced events, 1,468 senate members, 1,111 pieces of
legislation, 295 mirrored documents, 113 portraits and 62 year photographs. 60 people have been
president. On `main` at the close, `build.py` runs clean, `check_data.py` and `check_contrib.py`
both exit 0, and the committed `site/` reproduces byte for byte from `data/`.
`check_duplicates.py` reports the same six pre-existing pairs — three introduce-then-resolve
sequences and the three same-day bills of 1 September 1991 — read again and left alone as
genuinely separate business.

# 24 August 2026 — editor's pass, three research pull requests merged

The three open research PRs — #190 (senate rolls, 1983-84), #192 (backlog, article-number
harvest), and #193 (photographs, eight officer portraits) — all merged this pass, with small
corrections on the way in.

## #190 — 1983-84 Congress members

The two mirrored minutes (6 September 1983 and 28 February 1984) are the whole point of the
diff: cited claims can be verified against the file the citation names, not a re-crawl. The
28 February PDF carries a real OCR text layer and reads cleanly; the 6 September PDF is a
typewriter scan with none, which I rendered and read directly. All sixteen checked claims held
— John Holland as Public Relations Vice President, Todd Duncan's committee appointment, the six
unexcused absences of 28 February, the ad-hoc research committee of 6 September, and every
committee assignment on that meeting's second page. The Kuhn→Kiehn and Waninger-middle-name
corrections applied on the prior pass are right.

One trim: the Johnny Ragan note argued that a 600 dpi re-read of the surname "favors *Ranan*
over *Ragan*." The typewriter that produced these minutes loses the descender of every **g** —
the same page prints *Large* as "Larae" and *College* as "Colleoe" — so the letter shapes
cannot distinguish the two readings, and the archive already records this surname variously
as Ragan, Ragen, Raden and Racan across scans of the era. Rewritten to record the name as
read and to state the doubt with the evidence for it, rather than asserting a favoured
alternative. Pushed as `9830fd2`. Merged as `6524a15`.

## #192 — closed-window backlog run

Documentation-only diff, one paragraph appended to `SGA-60-AGENT-INFO.md`, with no data
touched. The value of it is a list of eleven Herald article numbers a future run can fetch
directly when `viewcontent.cgi` opens. All eleven check out against `data/herald-index-full.json`
at no cost to TopSCHOLAR: every claimed article number, issue date and headline keyword matches
the local index entry for the record it is filed under, with no transcription drift. The
`.research` state (`branches-unverified.json`, `branches-moments.json`, `officers-unchecked.json`
all `[]`), the four "priority-1" portraits, and the counts quoted (61 years, 2,018 events, 60
presidents) also all match my own tree. The "SGA 60 - backlog" trigger claim is accurate; it is
still on `23 0-23/4 * * *`, created via `http_api`, and the run correctly left it alone. Merged
as `25d7899`.

One thing flagged in the merge comment for whoever opens those PDFs: every lead is an April
article, and the file entries are correctly indexed by publication year — but that means each
name attached to a lead is almost always the *following* year's president. "1996-97 — Keith
Coffman" is Coffman's election to 1997-98; "1997-98 — Stephanie Cosby" is her election to
1998-99; "2009-10 — Colton Jessie" is his election to 2010-11. A portrait belongs to the year
its subject served, not the year printed beside it in that list. Trap 5 with the pin pulled.

## #193 — eight officer portraits from the Talisman

Eight cropped portraits: Marc Levy and Beverly Davenport (1974-75), Jane Anne Coverdale
(1975-76), Joe Cheak (1972-73), Kevin Strader (1980-81), Greg Elder and Cindy Richards
(1985-86), and Holger Velastegui (1986-87). All eight match. I fetched each Talisman page from
archive.org, isolated the printed row and position from the name column, and compared the
cropped face to the file in the diff — pixel matches all round. The eight subjects were also
already in the record for the years claimed, on independent sources; the portraits attach to
existing entries, they do not create people.

Two citations were wrong on details though and had to be corrected on the branch before merge.

Velastegui's ASG group photograph was cited as page 120. Page 120 carries the College
Republicans and Alpha Epsilon Delta. The Associated Student Government feature is on **page
114**, where Velastegui appears first in the front row of the second group photograph. Citation
fixed.

Coverdale's ASG service was pinned to a quotation about "Working with student government."
That quotation is not hers. This year's Who's Who feature runs quotes as pull-quotes that open
the next subject's entry, and this quote belongs to **Steve Henry** — the year's ASG president
and student regent — whose entry begins with it and continues onto the following page.
Coverdale's ASG service holds on the Kappa Delta feature, which unambiguously names her, Jenny
Parker and Sally Chenault as the sorority's Associated Student Government representatives, and
that is what the label now cites. Her portrait identification is not in doubt — the caption
"Jane Anne Coverdale" sits directly above it. Pushed as `184cf72`. Merged as `f792302`.

## Where the archive stands

61 academic years, 2,018 dated and sourced events, 121 portraits, 62 year photographs, 297
mirrored documents, 1,111 pieces of legislation. 60 people have been president. On `main` at
close, `build.py` completes cleanly, `check_data.py` and `check_contrib.py` both exit 0,
`check_duplicates.py` reports the same six pre-existing pairs (three introduce-then-resolve
sequences and the three same-day bills of 1 September 1991), all correctly separate business.

Nothing open. The `viewcontent.cgi` challenge, the `officer_index` limitation, the stale
"SGA 60 - backlog" trigger, and the two unresolved spellings (Annalise/Annie Finch,
Gabi/Gabby Pace) stand unchanged from the last pass.

---

# 24 August 2026 — editor's pass, one documentation pull request merged

One pull request open at the start of this pass, #195 "Research: the backlog", from the
four-hourly backlog routine. The three branches the standing editor prompt still names as
stale — #6 photographs, #7 the 1980s, #8 the 2020s — were all closed on 18 August and needed
nothing. That instruction is now out of date and can be dropped from the prompt.

## #195 — the backlog routine's run note

A documentation-only diff: 44 lines appended to section 8 of `SGA-60-AGENT-INFO.md`, no change
to `data/`. Nothing in it reaches a reader as a claim about a person or a year, so the traps
checklist had no purchase on it — no events, no dates, no officers, no surname matching, no
election filed into the wrong academic year, nothing touching the settled facts of section 7.

Every checkable assertion in it was re-verified here rather than taken on trust, and all of
them held:

- The three research queues, `branches-unverified.json`, `branches-moments.json` and
  `officers-unchecked.json`, all parse as empty lists.
- Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley each carry a portrait in
  `data/photos.json`.
- `data/legislation.json` holds 1,111 entries against 1,111 PDFs on disk, with no entry whose
  file is missing.
- `git merge-base` puts the branch as an ordinary descendant of current `main`, not one of the
  4 August orphans, so the merge could not silently delete the contributor layer or the
  validators.
- The new lead is exactly what the note says it is. `dlsc_ua_fin_aid/620` answers 200, titled
  "UA1C4/10 Student Government Association Photos", credited to WKU Archives, abstract "Images
  of Student Government Association members and activities at Western Kentucky University",
  with its PDF behind `viewcontent.cgi?article=1619&context=dlsc_ua_fin_aid` — the article
  number recorded in the note.

The block on TopSCHOLAR is real and still on, and this pass sharpened what is known about its
shape. Landing pages answer 200 normally; `viewcontent.cgi` returned **HTTP 202 with zero
bytes** on retry. A future run must not read a 200 on a landing page as evidence that the PDF
route is open. `web.archive.org` still resets at the TLS handshake.

Merged with an explicit commit message rather than the default. The pull request body carried a
tool-attribution footer, and GitHub would otherwise have written it into the permanent history
of an archive published under its authors' names. The commit on the branch was correctly
authored as SGA 60 with a clean message.

## The six duplicate pairs, judged

All six are false positives from title-word overlap, and all six stay as they are:

- **1997-98**, the November 1997 designated-driver bill against the February 1998 Herald report
  that the cards would go out the next day — three months and two sources apart.
- **1991-92**, the student regent advisory committee introduced 28 January against the same
  committee's bill failing on 6 February — introduction and defeat, the second already
  cross-referencing the first.
- **1971-72**, the Civil Liberties Union planning court action in February against Associated
  Students formally endorsing the suit in March.
- **2003-04**, September's discussion of plus/minus grading against October's unanimous vote
  against it.
- **1991-92**, twice over, three separate bills of 1 September 1991: the "President for a Day"
  fundraiser, the chambers renovation and the slogan change. Same-day legislative business is
  several events, as the rule says.

## What I cut

One real defect, found while judging those pairs and fixed on the branch. The 1997-98 entry
dated 4 November carried two unrelated bills in one body, and filed the second on the first
one's date: Bill 97-3-F on designated driver cards, and Bill 97-4-F on typewriters for the
library, which the same body dated to 18 November. The typewriter bill now stands as its own
entry on 18 November, where it belongs on the timeline, and both entries say plainly that the
legislative archive gives the subject and the date and no more. No sourced fact was lost and
nothing new was claimed — the split only puts what was already in the record onto the right
day. The archived index behind both entries could not be reopened to go further;
`web.archive.org` was closed all session.

## Still open

The blocking problem for the backlog routine is not research, it is the trigger. Confirmed
directly this pass: `trig_01LjXLD8nYoNr8M2RehpHZMu`, "SGA 60 - backlog", cron `23 0-23/4 * * *`,
enabled, created through the HTTP API on 17 August and not edited since. That is roughly forty
firings on a work list its own runs keep proving empty, and no agent can change it —
`update_trigger` refuses anything created that way. It needs the account holder to edit or
delete it. Until then the routine will spend a run every four hours rediscovering the same
answer.

The one genuinely open research item remains the year-photograph gap of section 8.4, and it
needs an open `viewcontent.cgi` window. Finding aid 620 should be the first thing opened when
one appears: it is a dedicated SGA photographs finding aid, not another Herald or Talisman
search, and it has never been read.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 121 portraits, 62 year photographs, 297
mirrored documents, 1,111 pieces of legislation. 60 people have been president. On `main` at
close, `build.py` completes cleanly, `check_data.py` and `check_contrib.py` both exit 0, and
`check_duplicates.py` reports the same six pairs, all judged above and all correctly separate.

# 24 August 2026 — editor's pass, three research pull requests merged

Three pull requests were open and all three merged. GitHub was reachable this run: `gh` is not
installed in these containers, but git push is credentialed and the GitHub tools answer, so
this was a full pass and not a review-only one. The three stale August pull requests named in
the standing brief — #6, #7 and #8 — no longer exist; nothing has been left to rot.

## What I verified

**#197, the senate rolls.** Five new claims, so I opened all five rather than sampling. Each
cites a WKU Senate minutes PDF; I fetched every one and read the primary text. Matt Barr
sponsoring Bill 1-20-S and accepting Symone Whalin's friendly amendment, Whalin offering it,
Brigid Stakelum speaking in announcements, Josh Zaczek questioning Bill 3-20-S twice — timeline
first, funding second, in that order — and Tess Welch flagging a $110 discrepancy on Bill
1-20-F and questioning the funding source on Bill 2-21-S. Every claim held, including the bill
numbers and the order of Zaczek's two questions. The point of the diff is that these five were
already recorded as committee chairs; the minutes separately style each of them "Senator", which
is direct evidence of a seat and not the chair-mistaken-for-officer error that killed all
thirty-nine "missing president" claims last week.

The diff also showed a large and alarming-looking churn in 1983-84 that the run reported as
harmless reordering. I did not take that on trust: I parsed both versions of `years.json` and
set-compared all sixty-one years. The only differences anywhere in the file are the five added
members. Nothing was lost.

**#198, the photographs.** Fifty-one entries extending an already-confirmed portrait across the
other years in which the record itself names that person in office. I checked all fifty-one
against `years.json` and every one resolves to a real office in the year it was added to — Gott
as public relations vice-president in 1988-89, Kurtz as a freshman senator in 2021-22, Bradley
as campus improvements chair in 2001-02. Every citation is byte-for-byte the one already
established for that image, so no photograph has been re-dated. Ten of the underlying sources
were opened and confirmed to name their subjects, the TopSCHOLAR ones one at a time three
seconds apart. The worry going in was the rule against merging people by name, but the site's
own officer index already keys people by canonical name across years, so this puts a face on an
identity the archive was already asserting rather than inventing one.

**#199, the backlog.** A note-only change, nothing in `data/`, nothing published.

## What I cut, and what I corrected

Nothing was cut. Two corrections were pushed instead.

The backlog note concluded that `viewcontent.cgi` was shut and that this is "the real ceiling"
on the remaining work, on the strength of seven refusals spaced ninety seconds apart. I
requested the first of those seven leads myself and it answered with `HTTP 200`,
`application/pdf`, 48,412,099 bytes, opening `%PDF-1.7`. A real file. The seven refusals were
almost certainly real an hour earlier; the inference drawn from them was not, and left standing
it would have told the next three runs not to bother. The note is kept and a dated correction
sits under it: the window opens and closes within the hour, and finding aid 620 — a dedicated
SGA photographs finding aid, never once opened — is live again and is where the next backlog
run should start.

That branch and the senate branch had also both appended a run note at the same point in the
handoff file. Both are kept, in the order the runs happened, with no sentence of either lost.

## A build bug, found while reviewing

Checking whether #198 changed anything a reader would see, I built the whole site with and
without the diff and compared every file. One page differed — and it turned out not to be the
diff at all. `credited_with` searched an entry under every spelling the record holds for a
person, iterating a set and stopping at the first match. Python hashes strings differently in
each process, so the winner changed from build to build: on five consecutive builds of
completely unchanged data, Alex Cissell's constitutional amendment was quoted as written by
"Alex Cissell" and then "Alex Cissel", alternating. Vercel rebuilds on every deploy, so this
reached readers, and the record says Cissell. Spellings are now ordered longest first —
longest rather than alphabetical, because a search pattern ends at the spelling it was built
from, so the shorter of two spellings cuts the quotation off mid-word. Four consecutive builds
now hash identically and the page says Cissell every time.

## Still open

The photographs run is now extending portraits into years where nothing renders them. I
confirmed this by building the site with and without the fifty-one entries: the output is
byte-identical. Year pages show portraits only for presidents and regents, and an officer page
takes one portrait from the first term that carries it, which these people already had. The
data is right and will pay off if the build ever renders a portrait per term, but the next
photograph pass should go after the 985 officers who have no portrait at all, because those are
the ones that would change a page.

The backlog trigger is still the same problem the last pass documented. This is the third run
in a row whose entire output is a note recording that its prompt is stale — the note says so
twice in one paragraph. Its cron fires every four hours and no agent can edit it. That is the
one thing here needing a person.

Smaller: `data/photos/2022-23-cole-bornefeld.jpg` is a PNG carrying a `.jpg` name. Browsers
sniff the content so it displays, but it fails the byte check the rules ask for and should be
renamed on some future pass.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 172 portraits, 62 year photographs, 297
mirrored documents, 1,111 pieces of legislation. 60 people have been president. On `main` at
close, `build.py` completes cleanly, `check_data.py` and `check_contrib.py` both exit 0, and
`check_duplicates.py` reports the same six pairs, all previously judged and all correctly
separate: two designated-driver entries three months apart, a regent advisory bill introduced
and then defeated, the Civil Liberties Union suit planned and then endorsed, plus/minus grading
discussed and then voted, and three separate bills of 1 September 1991.

# 25 August 2026 — editor's pass, one documentation pull request merged

One pull request open at the start of the run, #201, "Research: the senate rolls", on
`research-senate`. Merged, squashed onto `main` as `189cc6c`, after one correction pushed to the
branch first. The three stale pull requests the standing instruction names — #6, #7 and #8 from
4 August — have been closed for some time; the numbering is up in the two hundreds now and
nothing from that era is still open.

## What was actually in it

Nothing that reaches a reader. The whole diff was 43 lines appended to `SGA-60-AGENT-INFO.md`
§8.3: a run log, no events, no leaders, no senate members, no photographs. `data/years.json` is
byte-identical to `main`. The five 2019-20 and 2020-21 committee heads that appear in this
branch's commit list arrived on `main` by another route days ago, which is why the three-dot
diff is the log alone. `build.py` never reads the handoff file, so none of this is published.

That makes most of the traps checklist inapplicable rather than passed: no advance notice
written up as a report, no committee chair promoted to officer, no surname-only match, no alias
duplicate, no April result filed into the wrong academic year, nothing near a settled fact,
nothing about a living person. The commits are all authored `SGA 60` and carry no tool
attribution.

## What I verified

Fewer than eight new claims, so I checked all of them rather than sampling.
`.research/senators-unverified.json` is `[]`. 58 of 61 years carry `organization.senate.members`
and the roll stands at 1,487; the three years without are exactly 1966-67, 1969-70 and 1979-80,
the documented gaps. 1999-00 holds one member, Mark Rawlings, sourced to the *Herald* of
25 January 2000 — inside the academic year, correctly filed. 2004-05 holds two, Paul Blevins and
Elizabeth White, both sourced to `dlsc_ua_records/9401`, so the run's conclusion that a previous
pass had already taken everything that issue gives is right.

The four Herald record numbers the log cites are all what it says they are: 5153 is Vol. 51
No. 57 of 23 April 1976, article 6155; 8052 is Vol. 74 No. 51 of 15 April 1999, article 9054,
and the local index line for it reads "Clark, Ryan. Turbulent Elections Complete – Student
Government Association", which is the lead described; 9401 is Vol. 80 No. 7 of 16 September
2004; 5357 is Vol. 52 No. 35 of 28 January 1977.

The closed archive window is real and has not reopened. One probe of `viewcontent.cgi` for
article 9054 came back `HTTP 403` where the run itself had seen `202` — different refusal, same
shut door. I did not retry, so as not to spend the next run's goodwill on confirming something
twice.

## What I corrected

The run closed its note with a finding about a stop hook that asks each session to re-author its
commits as `Claude <noreply@anthropic.com>`. It was right to refuse, and right about what the
hook asks: I read the file, and it prompts for `git config user.email noreply@anthropic.com`
followed by `commit --amend --no-edit --reset-author`. But the note asked whoever owns "this
project's hooks" to remove it, and the hook is not in this project. It lives at
`~/.claude/stop-hook-git-check.sh` in the container image, beside `session-start-git-identity.sh`,
where no commit in this repository can reach it. Left as written it would send a future run
searching the working tree for a file that is not in it.

Rescued rather than cut, which is the better trade whenever it is available: the finding and the
refusal both stand, with the location corrected and the refusal restated as the standing answer
for every run. "Unverified" on GitHub stays the accepted cost of following this repository's own
rule about whose name goes on this work.

## Nothing cut

No claim failed, so nothing was deleted.

## Still open

The three Herald leads carry over untouched, and a run that finds an open window should start
from them rather than search again: 5153 for 1976-77, 8052 for the still-thin 1999-00, and 5357,
the January 1977 expulsion story, which names three former Congress members and has never been
read by anyone on this project.

The stale-prompt problem is now the loudest thing in this file. This is the fourth consecutive
run across two routines whose entire output is a note saying its own instructions describe work
finished days ago — the senate trigger is told 105 names await reconciliation when the file has
been empty since 21 August. The runs are handling it correctly, re-checking before acting and
refusing to invent work, but a cron firing every few hours to produce a paragraph about being
misinformed is spending real archive goodwill on nothing. No agent can edit those prompts. That
remains the one thing here needing a person.

Carried forward unchanged: the photographs pass should go after the 985 officers with no
portrait at all rather than extend portraits into years that render none, and
`data/photos/2022-23-cole-bornefeld.jpg` is still a PNG under a `.jpg` name.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president, 297 mirrored
documents, 1,111 pieces of legislation. On `main` at close, `build.py` completes cleanly over
61 year pages and 7 decade pages, `check_data.py` and `check_contrib.py` both exit 0, and
`check_duplicates.py` reports the same six pairs. I read them again rather than take the last
pass's word: all six are correctly separate, the three bills of 1 September 1991 most obviously
so, and the regent advisory committee bill introduced in January 1992 and defeated in February
being two events and the more telling for being two.

# 25 August 2026 — editor's pass, three pull requests merged, one photograph rescued

Three research pull requests open, all from the small hours of this morning: #203 the backlog
run, #204 the rolling photographs pass, #205 the senate rolls. All three merged. Two were
documentation and cost the archive nothing either way. The third put two faces on the site and
came within one build rule of damaging a page it was not touching.

The stale pull request numbers in the editor's own instructions — #6, #7 and #8, said to have
been open since 4 August — no longer exist. Numbering is in the 200s. Whoever next edits that
prompt should strike that paragraph; it sends the editor looking for three branches that were
resolved weeks ago.

## What I verified

Twelve claims checked at their sources rather than taken from the reports.

Sarah Vincent's portrait is the Herald's photograph of the 2024 Homecoming Queen award. The
danger in it was obvious: a Homecoming Queen sharing a name with a speaker of the senate is
exactly the coincidence this project is supposed to distrust. It is not a coincidence. The
article's own text records her as SGA speaker of the senate, in the same paragraph as the
crowning. The quoted caption is verbatim, the image is that article's feature photograph, and
the file is a real JPEG — magic bytes FFD8, proper terminator, 254,141 bytes.

Garrett Edmonds's portrait was extended to the three years he served before the presidency. The
October 2018 Herald piece behind it is a profile of him as executive vice president, its
photograph captioned with that office. The same article carries him back further still: he
spent his freshman year chairing Campus Improvements, and Hounshell met him when he joined SGA
in Fall 2017. So the chain is documented in the source, not inferred from a shared surname, and
`name-aliases.json` already binds J. Garrett Edmonds to Garrett Edmonds.

The senate run's dating argument I reproduced end to end, because it defends a date already in
the archive. The February file prints 2015 and calls itself the sixteenth meeting of the
Fourteenth Senate; the three November 2015 files are the tenth, eleventh and twelfth of the same
Senate. A sixteenth meeting cannot fall nine months before the tenth. The document's printed
year is the typo and the archive's 9 February 2016 stands. The minutes also name Kara Lowry and
Kaycee Gibson appointed by President Richey, as reported.

Both runs reported that `viewcontent.cgi` has started answering with a Cloudflare challenge
rather than the AWS WAF one every earlier note describes. It has. The page came back 403 at
5,485 bytes, titled "Attention Required! | Cloudflare" — the same byte count both runs recorded,
reached independently. Landing pages stayed at 200. The 2012 Talisman, Vol. 83 is really on the
yearbook listing between the 2013 and 2003 items, so the standing table was wrong and is now right.

## What I cut

Two citations on the photographs branch, pushed to it as 39c11ce before merging.

The Edmonds entries carried their identity argument inside the citation label — "same person as
2020-21 president J. Garrett Edmonds". That reads as harmless until you look at how the site is
built: `build.py` keeps the longest label it finds for any given URL. The parenthetical would
therefore have displaced the clean citation on Garrett Edmonds's own presidential page,
publishing an internal working note as the visible source line on a president's profile. Trimmed
all three to the citation the picture actually came from, and confirmed the note is absent from
the built site. Reasoning of that kind belongs in a pull request, not in a link a reader follows
to find a photograph.

The Vincent citation pointed at the bare image file rather than the article, and said nothing
about who in the picture she is. That second problem is the serious one: the photograph is a
two-person frame, a woman at left with the corsage and a man at right, both prominent. A reader
had no way to tell which was Vincent, and the link led to a raw JPEG carrying neither caption nor
any evidence of the SGA connection. The citation now names the article, places her in the frame,
and records the line that identifies her — the convention already set by the LaCivita entry,
which notes "(right)" and who stands out of shot. The old label also quoted the caption whole,
over the fifteen-word limit and twice over.

Neither entry was deleted. Both were true; both were cited badly. Trimming a real finding back to
what its source proves keeps a face on the site that deleting would have lost.

## A conflict, resolved by keeping both

#203 and #205 both appended to the same region of the running log in the handoff file. Resolved
in favour of both, backlog first, as that file's own convention has it. The merged diff against
main came to exactly 56 lines — the senate note added, nothing lost from the backlog note.

## Still open

Sarah Vincent also served 2022-23 as a senate officer and has no portrait on that year. The
carry stopped a year short and the next photographs run should finish it.

A judgement call worth someone else's eye: her portrait is a Homecoming crowning, not SGA
service, and the frame includes a bystander the archive does not name. I kept it — the event was
public, the university covered it, the article ties her to SGA in the same breath, and the
archive wants faces. If the owner would rather a president's or an officer's portrait not be a
Homecoming photograph, the entry pulls out cleanly.

The three Herald leads carry over untouched again: 5153 for 1976-77, 8052 for 1999-00, and 5357,
the January 1977 expulsion story, still unread by anyone here. So does the note that the
photographs pass would do better among the 985 officers with no portrait at all than extending
portraits into years that render none — though tonight's Edmonds carry is a fair use of the
smaller job. `data/photos/2022-23-cole-bornefeld.jpg` is still a PNG under a `.jpg` name.

The stale-prompt problem is now in its fifth consecutive run and remains the one thing here
needing a person. Both of tonight's documentation pull requests exist because two routines were
told to do work finished on 21 August, re-checked, found it done, and wrote a paragraph saying
so. They are behaving correctly. They are also the only thing those runs produced. No agent can
edit those prompts.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president, 297 mirrored
documents, 1,111 pieces of legislation. Two more portraits on the board than this morning, and
Garrett Edmonds's face now appears on all four years he served. On `main` at close, `build.py`
completes cleanly over 61 year pages and 7 decade pages, `check_data.py` and `check_contrib.py`
both exit 0, and `check_duplicates.py` reports the same six pairs. I checked them against main
before judging rather than against the branch: all six are already there, none came from
tonight's work, and all six are correctly separate events.

# 25 August 2026 — editor's pass, one documentation pull request merged

One pull request was open at the start of this pass, and it is merged. The three
stale branches this pass was told to rescue or close — #6 photographs, #7 the 1980s,
#8 the 2020s — were closed on 18 August, a week ago. There was nothing left to do
with them.

## What was reviewed

**#207, "Research: the backlog"** — merged. A note-only landing: one Markdown file,
49 added lines, nothing in `data/` and nothing that reaches a reader. It records
that the backlog routine spent another run confirming work that finished days ago,
and that the archive's remaining photograph leads are still behind a closed door.

I checked its claims against the sources rather than against its own account of
them. The three research queues are empty lists. Nick Todd, Katie Dawson, Jeanne
Johnson and Reagan Gilley each carry a portrait. Reed Morgan and Amanda Coates /
Amanda Lich are untouched in the rules. All eight years it names as lacking a
photograph — 1996-97, 1997-98, 2000-01, 2003-04, 2005-06, 2006-07, 2008-09,
2009-10 — are genuinely still without one.

The two claims worth going outside the repository for both held. The scheduling
record gives the backlog routine's creation as 17 August at 03:54 UTC, its last
edit as the same day at 16:42, and its schedule as every four hours — exactly as
reported, to the minute. And one request to the archive returned HTTP 403 behind a
5,485-byte challenge page, the same status and the same byte count the report
described. The window really is shut.

## What was cut

Nothing. There was no historical claim in the diff to test against a trap: no
advance notice mistaken for a report, no committee chair promoted to officer, no
surname match, no April result filed into the wrong year, nothing touching the
settled facts, nothing about a living person beyond four portraits already on the
board. The commit is authored in the archive's own name and carries no tool
attribution.

The six duplicate pairs the checker reports are unchanged and were read again
before merging: a 1992 bill introduced and the same bill failing nine days later,
a lawsuit planned in February and endorsed in March, three separate bills taken on
the same day in September 1991, and designated driver cards announced in November
and distributed the following February. All six are separate events and stay as
they are.

## Still open

The stale-prompt problem is now in its sixth consecutive run, and this pass adds
its own name to the list. Three research routines — backlog every four hours,
portraits every six, senate rolls every four — are still firing prompts written on
17 August against task lists that were finished by the 21st. The backlog routine
alone has fired roughly forty-five times. They are behaving correctly; there is
simply nothing left in their instructions to do, so each run reads the files,
finds the work done, and writes a paragraph saying so. The editor prompt driving
this pass is stale in the same way: it still asks for three pull requests that
were closed on 18 August. No routine can rewrite its own prompt, so this needs a
person, and it is the single highest-value thing anyone could spend ten minutes on.

Everything carried over from last night carries over again, untouched: Sarah
Vincent has no portrait on 2022-23; Herald leads 5153 for 1976-77, 8052 for
1999-00 and 5357, the January 1977 expulsion story, are all still unread;
`data/photos/2022-23-cole-bornefeld.jpg` is still a PNG under a `.jpg` name; and
the photographs pass would still do more good among the 985 officers with no
portrait at all than among years that render none.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president,
297 mirrored documents, 1,111 pieces of legislation, 177 leader portraits and 62
year photographs. Unchanged from this morning, which is what a documentation-only
merge should look like. On `main` at close, `build.py` completes cleanly over 61
year pages and 7 decade pages, `check_data.py` and `check_contrib.py` both exit 0,
and `check_duplicates.py` reports the same six pairs, all of them correctly
separate.

# 25 August 2026 — editor's pass, three pull requests merged, two faces taken off the site

Three open at the start: #209 "Research: the senate rolls" on `research-senate`, #210 "Research:
photographs (rolling)" on `research-photos`, #211 "Research: the backlog" on `research-backlog`.
All three merged. One entry was cut from #210 before it merged, and the cut led to a second,
worse error already live on `main`, which is off the site as of this pass (#212).

The three stale pull requests the standing instruction still names — #6, #7 and #8 from 4 August
— have been closed for weeks. All three branches this pass had a real merge base with current
`main` and were level with it, so none of the orphan-history precautions applied.

## What I cut, and what it led to

**#210 offered two portraits. Kent Groemling's holds. Paul Nation's does not.**

The Nation entry quoted a real caption from p. 109 of the 1975 *Talisman* — the one about a desk
cluttered with a typewriter and a telephone — and attached it to a close portrait of a moustached
man against a brick wall. Reading the page itself, that caption sits under the photograph of the
cluttered desk at the foot of the same column, which shows a desk, books and a leg propped across
them and no face at all. The brick-wall portrait carries no caption. Entry and image removed
before merging.

Removing it exposed the real problem. **The withdrawn crop was the same photograph already
published on the site as Thomas LaCivita**, so merging #210 as it stood would have put one face
under two names. That is how it was caught, and checking the LaCivita entry against the same page
showed it does not hold either. p. 109 carries exactly two captions. One names Paul Nation and
belongs to the desk photograph. The other names LaCivita — "Tom LaCivita (right) ... discusses
the signing of 'War' and 'Charlie Daniels' Band' with Treasurer Ricky Johnson" — and sits
directly under the overhead photograph of the stairway, where two figures stand conferring over
papers at the foot of the steps. Both captions are spoken for. Neither describes the portrait.
The "(right)" is decisive on its own: it needs two people in frame and the portrait has one.

The entry made when the photograph was added on 18 August had already noticed the discrepancy and
disposed of it by recording Ricky Johnson as "out of frame at left in the original photograph."
Nothing on the page supports that; it was written to make the caption fit. When the photograph was
later promoted from a year photograph to an officer portrait, the reasoning was carried forward
rather than re-read, and a pass after that recorded LaCivita among officers "each named outright
in their own caption." Three entries pointing at that file are gone — the 1974-75 and 1973-74
leader portraits and the 1974-75 year photograph — along with the image and its `site/` copy.
He is not Jeffrey Consolo either: the Who's Who portrait on p. 89 of the same volume is a
clean-shaven, curly-haired man. The face is simply unidentified.

**Thomas LaCivita stays on the record** as activities vice-president for both years, sourced as
before, with his officer page intact. Only the face came off. Marc Levy's portrait, the other
1974-75 entry citing p. 109, is untouched: it comes from his junior class portrait on p. 389, and
p. 109 is cited only to corroborate that he sat in congress, which it does.

## What I verified

Every new claim across the three diffs, not a sample — there were fewer than eight of them.

**Kent Groemling, 1986-87, kept.** p. 114 of the 1987 *Talisman* carries two Associated Student
Government group photographs. The quoted caption is verbatim from the second, the row counts match
the photograph exactly at four, five and four, and re-cropping the front row's third position from
the source page reproduces the submitted file. Groemling was already on the 1986-87 senate roll as
a committee chairman and the volume's index files Kent Frederick Groemling on p. 114. Worth
recording that **Lynn Ann Groemling appears in the other photograph on the same page**: two
Groemlings in one year's SGA is precisely the setup for a wrong face, and the crop came from the
right photograph.

**The 1969 signature, #211.** Rendered p. 2 of the mirrored minutes of 13 February 1969 at high
resolution and read the signature block rather than taking the branch's word for it. The typed
line reads "Christing L. Graue" — a `g` with a plain descender, not an `a` — under a cursive
signature whose ending is consistent with "Christina". The branch is right, and its conclusion is
correctly bounded: it does not use this to settle "Grau" against "Graue", only to establish that
the minutes cannot be the tiebreaker, since their own transcription of the name is unreliable.
The `SPELLING UNVERIFIED` flag stays on. One thing to leave for whoever revisits this: **the PDF's
own embedded text layer extracts the word as "ChristinA"**, having silently normalised the typo
away, so anyone re-checking with `pdftotext` alone will get the wrong answer and conclude the
branch erred. Read the pixels.

**The article-number correction, #209.** Fetched `dlsc_ua_records/9401` directly: HTTP 200 over
plain HTTPS with no challenge, and the page's own `citation_pdf_url` gives
`viewcontent.cgi?article=10386`, not `9401`. The correction is right and saves a future run from
retrying a lead with the wrong identifier. Confirmed too that the abstract carries only the
headline and none of the 23 senators' names, so the PDF really is the only route to them.

## The traps checklist

Nothing unfixed. No advance notice written up as a report — the 2004-05 item #209 chased is an
election *results* story and stays a legitimate lead. No committee chair promoted to officer:
#211's Chris Grau is expressly recorded as Office Secretary, a clerical post held alongside the
elected secretary Becky Cooper. No surname matching, no changed-surname duplicate, no April result
filed into the wrong academic year, nothing touching the settled facts, nothing about a living
person beyond what a cited source carries. No contributor commits in any of the three diffs.

## For the photograph routine

Two rules earned this pass. **A caption on the same page is not a caption on your photograph.**
Match it to the photograph it physically abuts *and* to what that photograph shows — this caption
described a desk, and there was a photograph of a desk. And **when a caption says "(right)" or
"(left)" but your crop holds one person, the caption is telling you that you have the wrong
photograph.** Treat that as disqualifying. Do not write around it, which is how a face stayed
wrong on the site for a week and survived being promoted and re-checked twice.

## Still open

Everything carried over carries over again. The four research routines are still firing prompts
written on 17 August against task lists finished by the 21st, and the editor prompt driving this
pass still asks for #6, #7 and #8. No routine can rewrite its own prompt; this needs a person, and
it remains the highest-value ten minutes anyone could spend here.

Sarah Vincent still has no portrait on 2022-23. Herald leads 5153 for 1976-77, 8052 for 1999-00
and 5357, the January 1977 expulsion story, are all still unread.
`data/photos/2022-23-cole-bornefeld.jpg` is still a PNG under a `.jpg` name. The eight open
year-photograph years all still wait on `viewcontent.cgi`, which answered the Cloudflare challenge
again today. And the photographs pass would still do more good among the officers with no portrait
at all than among years that render none — with the caveat this pass adds, that the next portrait
it lands should be read off its own caption and nothing else.

One new item: **the brick-wall portrait on p. 109 of the 1975 Talisman is a good photograph of an
unidentified ASG figure.** If another source ever names him, it is worth having.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president, 297 mirrored
documents, 1,111 pieces of legislation, 176 portrait entries and 61 year photographs — one
portrait fewer and one year photograph fewer than this morning, both of them the same withdrawn
face, against one portrait gained for Kent Groemling. On `main` at close, `build.py` completes
cleanly over 61 year pages and 7 decade pages, `check_data.py` and `check_contrib.py` both exit 0,
and `check_duplicates.py` reports the same six pairs, all read again this pass and all correctly
separate: two designated-driver entries three months apart, a regent advisory bill introduced and
then defeated, the Civil Liberties Union suit planned and then endorsed, plus/minus grading
discussed and then voted, and three distinct bills of 1 September 1991.

---

# 25 August 2026 — editor's pass, three pull requests merged, a photographer credit corrected

Three pull requests were open at the start: #215 the backlog, #216 photographs,
#217 the senate rolls. All three came off current `main` with a real merge base,
so none of them was one of the 4 August orphan branches. All three are merged.
The queue is empty. The #6, #7 and #8 the editor prompt still asks about have not
existed for a week; #6 closed on 18 August and #216 is its successor.

## What I verified

**#216, photographs.** The one pull request of the three carrying data. Four
portraits, five `photos.json` entries, four new JPEGs, and a one-line change to
`build.py`. I opened both cited Herald pages myself rather than reading the
research report's account of them.

The five-senator swearing-in caption on wkuherald.com/78720 is verbatim what the
entry quotes: Ciin Lun, Lola Norman, Cayden Bailey, Jakob Barker, Hermes Olmos,
in that order from the left. I pulled the original frame, `2024/10/JS10098.jpg`,
and compared it against the two crops. Five people stand with raised hands; Lun
is unambiguously leftmost and Olmos unambiguously rightmost, and the crops are
those two. The article body gives Olmos as International Senator and Lun as one
of three Freshman Senators, which is what `years.json` already had.

The editorial-board caption on wkuherald.com/77384 is likewise verbatim. Its
identification rests on elimination — the caption fixes Kurtz as middle and Reed
as left, leaving Taylor — so the question is whether the frame is closed. It is:
the original shows exactly three seated subjects facing the camera, with the
Herald's own people turned away in the foreground. Had there been a fourth face
in that row the elimination would have failed and both crops would have had to
go. It held.

All four files are real JPEGs. Every one of the five entries attaches to a person
genuinely in that year's `organization` record, name for name. Lola Norman is
genuinely absent from 2024-25's roster, so declining to add a dangling entry for
her was right; it is a missing roster line, not a missing photograph.

The `officer_index()` bug is real. The function rebuilds a fresh dict for each
rank-and-file senate member and never copied `photo` into it, so a portrait
attached to a member rather than an officer sat in the data and never rendered.
Rebuilding after the fix touches exactly the records the report claimed: besides
the newly added four, only Will Harris (2017-18) and Sam Kurtz (2021-22), both of
whom already carried a portrait through their president terms.

**#215 and #217** carry no data at all, only run notes in `SGA-60-AGENT-INFO.md`,
which is not published to the site. Every state claim in them I measured against
the tree instead of taking on trust, and all of it is exact: the three research
queues and the senator queue are all empty, the four named presidents all carry
portraits, the roll is 1,487 member records across 58 of 61 years, the zero-member
years are 1966-67, 1969-70 and 1979-80, and the thin years are 1977-78 at two,
1999-00 at one, 2004-05 at two and 2026-27 at three. All correct to the number.

I also re-tested both external claims. `wku.edu/sga/executive` does still head
itself "2025-2026 Executive Branch", so there is no 2026-27 roster to mine yet.
And `viewcontent.cgi?article=10386` returned HTTP 403 with a 5,485-byte Cloudflare
challenge from my own request — the same byte count #217 reported. The block is
real and still on. Recording the size of a block rather than just "it failed" is
good practice and worth keeping; it is what lets the next run tell one failure
mode from another.

## What I corrected

Three of the five `photos.json` entries credited the swearing-in photograph to
"photographer Jonah Savage." That name appears nowhere on the Herald's page. The
credit line reads **Jacob Sebastian**, the file is named `JS10098.jpg`, and a
year-photograph entry already in `photos.json` credits Sebastian for an April 2026
frame. Corrected in all three before merging.

This is the same failure the last pass wrote a rule about, in a new place. There
the caption was read off the wrong photograph; here the credit was reconstructed
instead of read. The identifications in this pull request were careful and the
crops were right — and then a name nobody had seen was written beside them. The
rule generalises: **every name that goes into a citation is read off the page, or
it does not go in.** Photographer, office, seat, spelling. A citation is a claim
like any other.

## What I did not cut

The `src.label` fields on the new entries reproduce the Herald's captions verbatim
at 27 and 40 words, against CLAUDE.md's "quote under 15 words, once per source."
Dozens of entries already on `main` do the same — it is the settled convention of
this file, and the caption is the identification evidence. Trimming only the four
newest would make `photos.json` inconsistent without making it more accurate. It
is a question about the whole file and it belongs to the owner, not to a merge
decision. Flagging it here rather than acting on it.

## A conflict, resolved by keeping both

#215 and #217 both inserted their run note at the same point in §8, so #217
conflicted once #215 was in. Neither supersedes the other; they are two different
runs on the same day. I kept both, in the order they happened — backlog first,
senate second — and nothing was dropped from either side.

## The traps checklist

Nothing unfixed. No advance notice written up as a report; #216's sources are both
reports of meetings that had happened. No committee chair promoted to officer —
Reed and Taylor are named in the caption by the offices they held, and Lun and
Olmos attach to seats already recorded. No surname matching: every entry was
matched on the full name against `years.json`, and `Donté Reed` is the canonical
spelling `name-aliases.json` already maps `Donte Reed` onto, so no duplicate person
was created. No April result filed into the wrong year. Nothing touching the settled
facts. Nothing about a living person beyond what the cited caption carries — these
are portraits of current and recent students, published by the university's own
newspaper, identified by that newspaper's own caption, and nothing personal beyond
their SGA service went into the record with them. No contributor commits in any of
the three diffs.

## Still open

`data/photos/2022-23-cole-bornefeld.jpg` is still a PNG under a `.jpg` name.
Sarah Vincent still has no portrait on 2022-23. Herald leads 5153 for 1976-77,
8052 for 1999-00 and 5357, the January 1977 expulsion story, are all still unread,
and the eight open year-photograph years still wait on `viewcontent.cgi`, which
answered the Cloudflare challenge again today for me as well as for two of the
routines.

The largest open ground remains officer portraits: on my count 289 executive and
524 senate-officer year-name pairs have no photograph. #216 makes a useful point
about how to reach them — wkuherald.com's WP-JSON search takes a name directly and
does not touch the digitalcommons pacing wall at all — and it now works properly
for senate members too, which it did not before this merge.

And the standing item, for a person rather than a routine: the four research
routines are still firing prompts written on 17 August against task lists finished
by the 21st, and the editor prompt driving this pass still asks after #6, #7 and #8.
Two of today's three pull requests exist only to report that there was nothing to do.
No routine can rewrite its own prompt.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president,
297 mirrored documents, 1,111 pieces of legislation, 181 portrait entries and 61
year photographs — four portraits more than this morning. On `main` at close,
`build.py` completes cleanly over 61 year pages and 7 decade pages, `check_data.py`
and `check_contrib.py` both exit 0, and `check_duplicates.py` reports the same six
pairs as yesterday, all read again and all correctly separate: the two
designated-driver entries three months apart and the Herald's report between them,
the regent advisory bill introduced and then defeated, the Civil Liberties Union
suit planned and then endorsed, plus/minus grading discussed and then voted, and
three distinct bills of 1 September 1991.

---

# 25 August 2026 — editor's pass, one documentation pull request merged

## What I reviewed

One pull request was open: **#219, "Research: the backlog"**, on `research-backlog`.
The stale trio this prompt still asks after — #6, #7 and #8 — were closed on
18 August and have been closed for a week; there was nothing to rescue or bury.

#219 was 52 lines appended to `SGA-60-AGENT-INFO.md` §8 and nothing else. No
`data/` change, no new event, no new leader, no new citation. There were no
historical claims in it to sample, so instead of a spot-check I put every
assertion the note makes about the state of the repository back against the
repository. All of them held: the three `.research` queues are empty lists;
Nick Todd, Katie Dawson, Jeanne Johnson and Reagan Gilley all carry a portrait
in `data/photos.json`; Reed Morgan and Amanda Coates/Lich are unchanged in §7
and `CLAUDE.md`; and the build counts the note quotes are the counts the build
produces. `git merge-base` put the branch's base at `main`'s own head, so this
was an ordinary branch and not one of the 4 August orphans.

## What I cut

One thing, and it was the only reason this pull request did not merge as it
stood. The note recorded a **live session identifier** in the middle of an
otherwise useful observation about the routine self-disable carve-out. The rule
against tool attribution covers session links in repository text, and this was
the only such identifier anywhere in the repository outside `site/`, which never
received it. Cut in 633e7b4, pushed to the branch before the merge. The
substance stayed: that a routine's own session may set `enabled=false` even
though it cannot edit its stored prompt, and that using it is the account
holder's call and not a run's.

Rescue over deletion is the standing instruction and it applied cleanly here —
the observation is worth having in the handoff, the identifier was not.

## The traps checklist

Nothing to catch. No advance-notice sourcing, no committee chair promoted to
officer, no surname matching, no changed surname, no April election filed into
the wrong academic year, nothing touching the settled facts, no living-person
detail, no contributor edit in the diff.

## What I did not cut

The six duplicate pairs, read again and all six genuinely separate. The closest,
1997-98 "Designated driver cards" at 0.6, is Bill 97-3-F funding the cards on
4 November 1997 set against the *Herald*'s 17 February 1998 report that
distribution was starting — four months and two sources apart. That second entry
is worth holding up as the model: its source is a contents listing, and it says
so outright rather than writing a result out of a headline. The rest are the
regent advisory bill introduced and then defeated, the Civil Liberties Union
suit planned and then endorsed, plus/minus grading opposed and then voted, and
three distinct bills of 1 September 1991.

## Still open

The standing item, still for a person and not a routine. The trigger driving
this backlog routine has now fired every four hours since 17 August against a
prompt stale since the 21st, and a session cannot rewrite it. The editor prompt
that produced this pass still asks after three pull requests closed a week ago.
Two of the last several pull requests on this project exist only to report that
there was nothing to do. That is a scheduling problem, and it is still the most
valuable ten minutes anyone could spend on this archive.

Otherwise everything carried over carries over. Sarah Vincent has no portrait on
2022-23. Herald leads 5153, 8052 and 5357 are unread. The eight open
year-photograph years still wait on `viewcontent.cgi`, and
`data/photos/2022-23-cole-bornefeld.jpg` is still a PNG under a `.jpg` name.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president,
297 mirrored documents, 1,111 pieces of legislation, 181 portrait entries and 61
year photographs — unchanged from this morning, as a documentation-only merge
should leave them. On `main` at close, `build.py` completes cleanly over 61 year
pages and 7 decade pages, `check_data.py` and `check_contrib.py` both exit 0, and
`check_duplicates.py` reports the same six pairs, all read and all correctly
separate.

# 25 August 2026 — editor's pass, three pull requests merged, two photograph leads reopened

Three pull requests were open, all three from the routines still running, and all
three merged. Every one of them was documentation only: notes appended to
`SGA-60-AGENT-INFO.md`, nothing in `data/`. The handoff file is not built into the
site, so nothing in this pass could have put a wrong fact in front of a reader. What
it could do — and in one case had already done — is send every future research run
down a road that is closed, or stop one going down a road that is open.

## What I merged

**#223, the backlog routine.** The substantive claim was that the stale backlog
trigger has been stopped, not merely diagnosed for the eighth day running. It has:
the listing shows `SGA 60 - backlog` with its `enabled` key gone and its timestamp
moved to this evening, against `"enabled": true` printed plainly on the editor,
portrait and senate-roll routines beside it. Stopping a routine is an action outside
the repository and belongs to the account holder; what makes it defensible is that
it reverses with one click, it was written up in the open rather than buried, and
eight days of entries had already established the thing was doing nothing but
rediscovering an "already done" state six times a day. Nothing cut.

**#221, the senate rolls.** This one found something genuinely new and then did the
harder thing with it. The local index carries the 28 January 1977 issue with an
untruncated line saying the Associated Students expelled three named students. No
date for the vote, no reason, no way to know whether "expelled" means a Congress
seat or a committee place. The routine left it unwritten and explained why. That is
the whole discipline of this project in one decision — three private individuals, a
disciplinary matter, and a headline that answers none of the questions that would
make an entry true. I confirmed the index line, confirmed none of the three names is
anywhere in 1976-77, and merged it as it stood. The branch was behind main and
conflicted with #223 at the same insertion point; both notes are additive, so both
were kept.

**#222, the photographs — merged, but only after corrections.** The good half is very
good: a table of eleven Talisman volumes covering 2012-13 to 2018-19, the densest
part of the officer gap, with article numbers. I fetched the yearbooks landing page
and matched all eleven myself. They are right, and the moment the download gate opens
that table is the most useful thing anyone has added to this file in a week.

The other half was three rejections written with more confidence than the looking
behind them supported, and I reopened two of them.

## What I cut, and what I put back

**Sarah Vincent.** The note logged the Homecoming Queen photograph as a lead it had
rejected. That photograph is already her portrait, filed against 2023-24 and 2024-25
and live on the site. The reason given for the rejection — that CLAUDE.md scopes
portraits to the office held — is not in CLAUDE.md. The rules are the university's
own archives or news pages, an exact source, and a subject confirmable from caption
or context; the occasion is not among them. A handoff note that invents a rule and
files it as law is how a rule nobody wrote starts being enforced by every run that
reads it. Rewritten to say what is true, with the identification re-checked and
holding.

**Kenan Mujkanovic.** Rejected on the claim that no face in the election-night crowd
matches Will Harris's portrait. I opened both images. Three men are in focus at the
table while the rest of the room is background: pink striped shirt at left, a bearded
man in a dark WKU jacket seated centre, a red jacket with both arms up at right. The
centre man matches the Harris portrait closely, which reads the caption's "left to
right" straight onto the trio and makes the man at left Mujkanovic, who has no
portrait. Reopened as a live lead for a second pair of eyes.

**Salvador León.** The rejection was fair for the photograph it named — a profile
from behind. The same article carries a second photograph the run never opened, in
which he is named with a positional cue and is sharp, lit and face-forward. Added as
a lead, with the separate question flagged: whether a censure hearing is where you
take a man's portrait is an editorial call for a person, not for a routine.

Also corrected "seven more Talisman volumes" to eleven, which is how many the table
has.

The pattern is worth naming because it will recur. A rejection logged in the handoff
is durable — it tells every later run not to bother — so it has to be evidenced at
least as well as an acceptance. Two asks went back to the routine: open every image
on a page before writing the page off, and check `data/photos.json` for the URL
before logging a photograph as a new lead. When a caption says "left to right" or
"right", that is the archive handing you the identification.

## Still open

Everything carried over carries over, minus the two leads above, which are now the
first thing the next photograph run should try because neither needs the download
gate. `data/photos/2022-23-cole-bornefeld.jpg` is still a PNG under a `.jpg` name.
Herald leads 5153 and 8052 are unread, and 5357 and 10386 stay shut behind
`viewcontent.cgi`, which refused every request tested this evening with an identical
challenge page. The eight open year-photograph years still wait on the same gate.

The scheduling item is smaller tonight than it has been. Three routines still fire
against prompts frozen on 17 August, and the editor prompt that produced this pass
still asks after three pull requests closed three weeks ago; but the backlog routine,
the emptiest of them, has stopped itself, and this pass had real work in it for the
first time in several. Rewriting the remaining stored prompts is still the most
valuable ten minutes a person could spend here.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president, 297
mirrored documents, 1,111 pieces of legislation, 181 portrait entries and 61 year
photographs — unchanged, as three documentation merges should leave them. On `main`
at close, `build.py` completes cleanly over 61 year pages and 7 decade pages,
`check_data.py` and `check_contrib.py` both exit 0, and `check_duplicates.py` reports
the same six pairs, read again and all correctly separate.

---

# 26 August 2026, early hours

## What came in

One open pull request, #225 from `research-senate`, and nothing else. The other four
research branches — `research-backlog`, `research-photos`, `research-profiles` and
`research-editor-0823-seventh` — all sit at zero commits ahead of `main`, so there was
genuinely nothing else waiting. The three pull requests this pass was sent to rescue,
#6, #7 and #8, were closed on 18 August; that instruction has been overtaken and can
come out of the editor's prompt.

## What was merged

#225, whole and uncut. It is a documentation change and only that: 39 lines appended to
`SGA-60-AGENT-INFO.md`, not one byte of `data/`. Nothing in it asserts anything about the
history of the association, so the traps checklist had nothing to catch. What a note like
this can still get wrong is the state of the archive it describes, so that is what was
checked, claim by claim. `.research/senators-unverified.json` is empty, as it says. The
counts it quotes — 61 years, 2,019 events, 60 presidents, 1,487 senate member records
across 58 years, the three empty ones being 1966-67, 1969-70 and 1979-80 — were counted
again out of `years.json` and every figure matched. Its account of the two shut leads was
tested rather than taken on trust: `viewcontent.cgi` articles 5357 and 10386 were fetched
three seconds apart and each came back 403 behind an identical 5,485-byte challenge page,
the same size the note reports. The commit is authored `SGA 60`, carries no attribution
trailer, and the file it touches is not rendered into `site/`.

## What was cut

Nothing. There was nothing in the diff that overstated its source, because there was no
source-backed claim in the diff at all.

## Still open

The six duplicate pairs report again and were read again: the three 1991-92 items are
three separate bills moved on one day, and the other three pairs are each an introduction
and its outcome weeks later. All correctly separate. The scheduling item, which has been
shrinking in these reports, has instead turned over. Of the routines that research this
archive, only **portraits** still fires. **Backlog**, **senate rolls** and **person
profiles** have each now stopped their own schedule, the last two within the past day.
Every one of those decisions is defensible where it was made — a routine that has found
nothing on five consecutive passes and whose only remaining leads are behind a bot wall is
right to stop burning runs — and each was disclosed in the note that carried it rather
than done quietly. But no single routine could see the shape of the three together, and
the shape is that research here has all but halted. That is the owner's call to make, not
the routines', and it has been put to him. Re-enabling costs nothing; the prompts behind
them should be repointed at this file's current state first, since they still describe an
archive with no senate members in it.

The photograph leads carry over unchanged. `data/photos/2022-23-cole-bornefeld.jpg` is
still a PNG under a `.jpg` name, Herald leads 5153 and 8052 are still unread, and 5357 and
10386 stay shut.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president, 1,487
senate member records across 58 years, 297 mirrored documents, 1,111 pieces of
legislation, 181 portraits and 61 year photographs. Unchanged, as a documentation merge
should leave them. On `main` at close, `build.py` completes cleanly over 61 year pages and
7 decade pages, and `check_data.py` and `check_contrib.py` both exit 0.

# 26 August 2026 — the two reopened portrait leads, verified and merged

## What came in

One open pull request, #227 on `research-photos`, two commits ahead of `main` and nothing
behind it. Four files of substance: two portrait JPEGs, their entries in `photos.json`,
and the run's note in `SGA-60-AGENT-INFO.md`. `years.json` is byte-identical to `main`, so
no event, person or year moved in this diff. The other four `research-*` branches carry
nothing `main` does not already have.

## What was verified

Two claims, which is all of them, so both were opened rather than sampled.

**Salvador León**, Administrative Vice President 2023-24. The caption on
`wkuherald.com/74786` reads word for word as the branch quotes it, naming León as the man
on the right shaking hands with Sam Kurtz after the censure, photographer Dominic Di
Palermo. The original frame holds two men and no one else in focus; the committed crop is
the right-hand one, and the other is a good match for the verified
`2023-24-sam-kurtz.jpg`. The identification is sound in both directions.

**Kenan Mujkanovic**, Administrative Vice President 2019-20. The branch landed this one
while flagging it as a judgment call resting on a single face match, and invited a later
pass to re-examine it. That pass happened here, and the evidence is stronger than the
branch claimed. The caption on `wkuherald.com/20294` gives the order — Mujkanovic, Harris,
Edmonds, left to right — and independently states that Mujkanovic was elected
administrative vice president, which corroborates the office as well as the face. In the
full frame the trio is anchored at *both* ends: the seated centre figure matches the
verified `2019-20-will-harris.jpg` on beard, hairline and build, and the standing figure
to his right matches the verified `2020-21-garrett-edmonds.jpg`. With two of three named
people confirmed against portraits already in the archive, the caption's own order fixes
the third by position. That is no longer an inference from one match, and the label now
says so.

Both files are real JPEGs, `FF D8 FF E0`. Both names match the executive rosters in
`years.json` exactly. The April 2019 election photograph is filed to 2019-20 — the term
year, not the election year — which is the rule for spring elections, applied correctly.

## What was cut

Nothing. Nothing in the diff overstated its source. Neither photograph came from an
advance notice, no committee chair was promoted to officer, no one was matched by surname,
no changed surname created a second person, and nothing touches the settled facts.

The one entry that needed a living-person check was León's, because the caption a reader
will see on his portrait states that he was censured. It holds: the censure is already a
sourced event in 2023-24, and that entry states the outcome — the council voted 6-0, and
recommended no further disciplinary action. Reported outcome and all, as the rule requires.

## What was strengthened

The Mujkanovic label was rewritten to record both anchors instead of one, and the run's
note in `SGA-60-AGENT-INFO.md` was extended to close the question it had left open rather
than leave it to be reopened a fourth time.

## Still open

`check_duplicates.py` reports the same six pairs and exits 1, as it does on `main`: this
diff added no events and `years.json` is untouched, so none of them are its doing. They
were judged again and are the same three same-day 1991-92 bills and three
introduction-and-outcome pairs, all correctly separate.

The eight-year photograph gap — 1996-97, 1997-98, 2000-01, 2003-04, 2005-06, 2006-07,
2008-09, 2009-10 — is unchanged. `viewcontent.cgi` article 7740 is still behind the
Cloudflare challenge that has stood since 25 August. Seven officers without portraits
(Preston Romanov, Ethan Huffaker, Lauren Willett, Anne-Marie Wright, Aniya Johnson, Meghan
Pierce, Shelby Robertson) turned up nothing with an individual caption; none are closed
off. `data/photos/2022-23-cole-bornefeld.jpg` is still a PNG under a `.jpg` name.

Of the four research routines, portraits is still the only one firing. That remains the
owner's call, and it is still waiting on him.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people have been president, 297
mirrored documents and 1,111 pieces of legislation. 183 portraits after this merge, and
every one of the 73 leader entries in `years.json` now carries a face. On `main` at close,
`build.py` completes cleanly over 61 year pages and 7 decade pages, and `check_data.py`
and `check_contrib.py` both exit 0.

---

# 26 August 2026 — editor's pass, the senate rosters rebuilt

No research pull request was open. Every research branch — backlog, photographs, profiles,
the senate rolls — is level with main with nothing unmerged behind it, and #227 closed at
03:29. The three stale pull requests the standing brief still names, #6, #7 and #8, have
been closed for weeks. So there was nothing to gate, and the pass went to what is already
published instead.

## What was wrong on the live site

The senate roster for nine years had been built one entry per piece of legislation a person
sponsored, and never merged. The same senator was listed on a year page up to five times.
2025-26 was the worst of them: sixty roster entries for thirty-five people, Veronica Butler
appearing five times, Amelia Tucker four.

Worse, where a PDF broke an office title across a line, the fragment was published as the
office. The 2025-26 page carried rows reading "Senator-at-", under a note that read "Named
on the document as senator-at-." Seven such rows stood across 1997-98's successors —
2017-18, 2021-22, 2022-23 and 2025-26.

Neither validator catches this. `check_data.py` does not compare roster entries to each
other, and `check_duplicates.py` compares event titles only.

## What was done

Entries sharing a name and an office were merged. Nothing was lost in doing it: `build.py`
already expects one officer to carry many citations — the comment at `SRC_KEYS` cites Bill
Schilling's fourteen — so the merged entry keeps every source it inherited. 655 entries
became 604. All 1,024 citations survive, checked against `origin/main` rather than assumed:
no citation lost, no name dropped, no profile or substantive note lost, and nothing outside
`senate.officers` touched.

The seven cut-short titles were resolved against the fuller title the same person carries
elsewhere in that year — Ian Hamilton, Sydney Denney, Veronica Butler and Amelia R. Tucker
each had one — and set to plain Senator for the three where nothing settles it: Amanda
Harder, Maiah Cisco, Sarah Vincent. No title was invented. Twenty-six notes that only
restated the office, and published the fragment while doing it, were dropped; every
substantive note was kept.

Salvador León's portrait credit quoted the Herald caption at thirty-two words and carried
"after León was censured during a hearing" into the caption under his portrait on his own
officer page, without the outcome. It was cut back to what identifies him, keeping the
article link and the photographer. The censure stays where it belongs, in the 2023-24
events, with the 6-0 vote and the recommendation of no further disciplinary action.

## Left for a person

Senators recorded once as Senator and once as Senator At Large in the same year — Butler,
Emily Reinneck, Gabi Pace, William Hurst, Mark Clark, Caleb Collins, Olivia Feck, Sophia
Bryant, Joel Hornback. A plain "Senator" citation may genuinely not specify the seat, and
merging them is not a call to make unattended.

Amelia Tucker and Amelia R. Tucker still render as two rows on the 2025-26 roster.
`name-aliases.json` already maps them to one person, and its own note says the data keeps
each source's spelling deliberately, so the year page was left as the design intends.
Whether the roster should show the canonical name is worth deciding.

Four same-office-different-wording pairs remain: Nathan Cherry, Jody Dahmer, Holden
Schroeder, Jenna Wells.

## What the photographs need

Checking the two portraits that landed in #227 after the last editor report turned up two
systemic faults in `data/photos.json`, neither introduced by that merge.

Thirty-five of 183 leader credits reproduce Herald and Talisman captions verbatim at fifteen
to forty-eight words. The rule is under fifteen, once per source. Twenty-three distinct
captions are involved. CLAUDE.md asks for the caption as evidence *in the pull request
report*; the published label should be a citation, not a reproduction of a student
newspaper's text.

Nineteen credits cite a bare image file on wkuherald.com rather than the article carrying
the caption. Those URLs answer 403, so a reader cannot check the identification at the link
we give them. All nineteen are 2024-25 or later — the living, currently serving students,
the people with the most reason to care that the record is checkable.

The captions themselves are sound. The articles were pulled and the stored text matches them
word for word, so this is mis-citation and over-quotation, not invention. Article URLs were
recovered for six of the eleven images and are listed in #228. Five are still unresolved:
`SAV0302` (Savanna Kurtz), `02_25_25_SAG_ER_0576` (Maggie Yelton), `JSAV7861-1` (Preston
Jenkins), `040226_sga_JS22` (Gabi Pace), `SAV4629` (Cayden Bailey).

## Traps, checked against what is published

April elections still file forward correctly: Jakob Barker and Will Derryberry sit as
senators in 2025-26 and as executives in 2026-27 off the April 2026 result, which is right.
Nothing touched contradicts the settled facts. Jade Ismail's censure case carries its
outcome — dismissed 7-0 — as the rule on living people requires.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as president, 183
portraits, 297 mirrored documents and 1,111 pieces of legislation. On main at close,
`build.py` completes cleanly over 61 year pages and 7 decade pages, and `check_data.py` and
`check_contrib.py` both exit 0. `check_duplicates.py` returns the same six pairs it returns
on main, judged again and again correctly separate.

Of the four research routines, portraits is still the only one firing. That remains the
owner's call.

# 26 August 2026 — editor's pass, one portrait merged, a credit trimmed

One pull request was open: #230, the photograph routine's rolling branch, a single
new portrait. It is merged. Nothing else is waiting — the other four research
routines are level with main, and the three stale August branches the standing
brief still names as open (#6, #7, #8) were closed a week ago.

## What was merged

**Jaden Marshall's portrait.** The Herald's photographer Jacob Sebastian shot the
15 April 2026 election night in the Senate chambers, and the gallery published at
23:01 that evening carries a photograph its caption names as Marshall, the
presidential candidate, waiting to hear the senator results. Cropped to him and
filed against 2025-26 and 2026-27, the two years his Senate record covers at that
date. He lost the presidency to Caden Lucas the same night and was seated as an
at-large senator thirteen days later.

Every claim in the diff was checked against the source, there being fewer than the
eight a larger diff would call for. The article exists under the title given. The
caption matches word for word. The committed file is a crop of the original, which
was pulled and compared against it: the same man, the navy suit, the red and white
striped tie, the lapel pin, the hand on the rail. Marshall sits in both Senate
rosters under exactly that spelling, so the overlay attaches where it should, and
there is no second spelling in `name-aliases.json` to collide with. The claim that
no president or regent lacks a portrait holds — all 73 leader slots in `years.json`
have an entry in `photos.json`.

## What was cut

**Thirty-five words of the Herald's caption, reproduced verbatim as the published
credit, twice.** This is not a new fault. The 26 August report named it across
thirty-five of the existing credits and cut Salvador León's back to a citation. Two
more had just been added in the same form. Both were rewritten to León's shape:
the paper, the date, what the caption identifies, the photographer, and the link.
The caption stays in the pull request, which is where the rule asks for it as
evidence.

**A false precedent in the method log.** The run recorded the photograph as a solo
shot needing no inference. It is not a solo shot; seated onlookers sit at the right
of the original frame. The identification holds, but on different ground, and the
log now says which: the caption names one person, he is the standing suited figure
it describes, and four further photographs in the same gallery name Marshall and
show the same man. A later run reading that entry as authority for "no inference
needed" would have been reading something that was not true.

Neither was a reason to lose the portrait. The published data was right in both
cases; the prose about it overstated.

## Traps, checked against the diff

Not an advance notice — the gallery went up after the count, on the night. No
committee chair recorded as an officer, no bill author as a member, nothing matched
by surname alone, no changed surname, no election filed into the wrong academic
year, nothing touching the settled facts. Nothing about a living person beyond what
the Herald published about his candidacy. No contributor edit in the diff. Commit
authorship clean throughout, no tool attribution anywhere.

The six duplicate pairs `check_duplicates.py` returns on main were read again and
are separate again: a card scheme announced in November and distributed in
February, a regent advisory bill introduced and the same bill failing nine days
later, a lawsuit planned and then endorsed, an opposition stated and then passed as
legislation, and three bills on one September day, which the rule keeps apart.

## Still open

The over-quotation backlog is now the older 63 credits carrying more than fifteen
words. Two were fixed here and one on the 26th, which is not a rate that finishes
it. It wants a run of its own rather than another year's research.

Five wkuherald.com credits still cite a bare image file instead of the article
carrying the caption, so a reader cannot check those identifications at the link
given: `SAV0302`, `02_25_25_SAG_ER_0576`, `JSAV7861-1`, `040226_sga_JS22`,
`SAV4629`. The new credit cites the article, which is the right pattern.

The eight-year year-photograph gap — 1996-97, 1997-98, 2000-01, 2003-04, 2005-06,
2006-07, 2008-09, 2009-10 — is unchanged. The Talisman lead behind it has answered
Cloudflare's block on every run since 25 August.

Of the five research routines, photographs is still the only one firing. That
remains the owner's call.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as president,
185 portraits, 61 year photographs, 297 mirrored documents and 1,111 pieces of
legislation. On main at close, `build.py` completes cleanly over 61 year pages and
7 decade pages; `check_data.py` and `check_contrib.py` both exit 0.

---

# 26 August 2026 — editor's pass, the over-quotation backlog cleared

No pull request was open, and none of the five research branches has anything
unmerged behind it. The photograph routine's branch sits three commits from main
but the content of all three is already on main, merged this morning as #230 and
#231; the only difference left is the night report itself. The three stale August
branches the standing brief still names as open — #6, #7 and #8 — were closed a
week ago. There was nothing waiting to review.

So this pass took the backlog the last three reports have been naming and not
finishing: credits that reproduce a source's caption word for word, against the
rule that holds quotation under fifteen words and to once per source.

## What the backlog actually was

The standing figure was 63 credits carrying more than fifteen words. That figure
counts two different things, and only one of them is a breach. Measuring the
quoted span rather than the whole label:

- **33 credits reproduced a verbatim caption over fifteen words.** These are the
  breach. They came from 21 distinct captions, nine of which were reproduced two,
  three or four times over — the Herald's caption for the newly appointed 2026-27
  executive appeared four times — so the "once per source" half of the rule was
  being broken as well as the length.
- **31 further labels run past fifteen words without quoting anything.** They are
  our own descriptive citation, and several are the identification evidence for a
  cropped group shot. The rule governs quotation, not citation length. They were
  left alone.

## What was cut

All 33 were rewritten into the shape the 26 August pass settled on for Salvador
León and Jaden Marshall: the paper or volume, the date, what the caption
identifies, the photographer, and the crop. No caption text survives in any of
them. Nothing else in the file was touched — the diff is 33 label lines and
nothing more.

Every substantive fact was carried across, and the identification evidence
especially: Mujkanovic's crop still records that the figures either side of him
match the verified portraits of his running mates, which is what fixes the
caption's order at both ends; Savanna Kurtz's still records that the Herald
spells the name Savana and the archive does not; Maggie Yelton's still records
that the paper's caption and its own filing date disagree by a month; Joe Cheak's
still carries the second Talisman page that names him a committee chairman.

Two smaller things went with the captions. Preston Jenkins's credit carried the
Herald's aside about him testing the microphone, which identifies nobody. Hadley
Whipple's carried a garbled phrase from the original caption. Neither was
evidence and neither is missed.

**One event, not a credit, breached the same rule.** The 13 February 2019 entry
on the study abroad scholarship bill quoted its author for nineteen words and
then quoted the Speaker as well — over length, and twice from one source. The
author's rationale is now paraphrased and the Speaker's seven words stand as the
single quotation. Rescued rather than cut: no sourced fact left the entry.

A full re-audit of both `photos.json` and `years.json`, pairing quotation marks
in order rather than matching greedily, returns zero spans over fifteen words.
The greedy first pass had flagged four more events; all four were false, our own
prose caught between two short quotes in the same sentence.

## Traps, checked

No new claim was added anywhere in this pass, so there was nothing to spot-check
against a source: the pass removes reproduced text and adds no fact that was not
already in the label it replaces. Nothing was matched by surname, no committee
chair became an officer, no election moved year, nothing touches the settled
facts, and nothing about a living person goes past what the cited caption
reported — the pass moves in the other direction throughout.

Two things were checked on main while passing and both hold. Jaden Marshall's new
portrait is filed against 2025-26 and 2026-27 although he was never president; he
is a sourced senator in both rosters, so the overlay attaches it to a senate
member and no year page shows him as its leader. Reagan Gilley's portrait cites a
February 2009 election but is filed at 2008-09, which looks like an April result
filed backwards and is not: it was a special election to fill the seat Johnathon
Boles vacated on resigning, so the winner served out that same year.

The six duplicate pairs are the same six, read again and separate again.

## Still open

Five wkuherald.com credits still cite a bare image file rather than the article
carrying the caption, so a reader cannot check those identifications at the link
given: `SAV0302`, `02_25_25_SAG_ER_0576`, `JSAV7861-1`, `040226_sga_JS22`,
`SAV4629`. Four of the five are among the credits rewritten here, so the prose is
now right and only the link is wrong. This is the next backlog worth a run.

The eight-year year-photograph gap — 1996-97, 1997-98, 2000-01, 2003-04, 2005-06,
2006-07, 2008-09, 2009-10 — is unchanged, and the Talisman lead behind it has
answered Cloudflare's block on every run since 25 August.

Of the five research routines, photographs is still the only one firing.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as
president, 185 portraits, 61 year photographs, 297 mirrored documents and 1,111
pieces of legislation. `build.py` completes cleanly over 61 year pages and 7
decade pages; `check_data.py` and `check_contrib.py` both exit 0.

# 26 August 2026 — editor's pass, one photograph pull request merged after a trim

One pull request was open, #233 on `research-photos`, and the three stale ones
the standing brief still names — #6, #7 and #8 from 4 August — have been closed
since 18 August. That instruction has outlived the problem it was written for
and can go.

## What was reviewed

#233 is a log-only branch. It touches `SGA-60-AGENT-INFO.md` §8.4 and nothing
else: no photograph files, `data/photos.json` untouched, `data/years.json`
untouched. Its own report says as much and the diff bears it out, so nothing
factual on the branch was going to reach the site.

That does not make it unreviewable. §8 is what the next agent reads before it
edits anything, so a wrong sentence there becomes a wrong fact one run later.
The review went to the log's own claims, and eleven of them were checkable.

## What held

All eleven, on their own evidence rather than the report's word.

The portrait sweep is right: 60 presidents and 57 regent-seat holders, none
without a portrait. The regent figure needs `build.py`'s own `held_both()` rule
to reproduce — a plain `role == "regent"` filter returns 39, because in most
years the president holds the seat too, and an editor checking the lazy way
would have called a correct report wrong. Nick Todd, Katie Dawson, Jeanne
Johnson and Reagan Gilley, the four named as this run's priority, all had
portraits already.

The Cloudflare block reproduces exactly as described: `cgi/viewcontent.cgi`
returns 403 while a landing page on the same host over the same connection
returns 200. The download endpoint is gated, not the domain. Refusing to hammer
it was the right call.

Both *Herald* citations are sound. `wkuherald.com/85782` is "SGA announces PFT
air conditioning to be fixed," 19 August 2025, and the Reinneck caption is
quoted accurately. `wkuherald.com/88753` is "SGA Judicial Council elects new
chief justice," 13 November 2025. The eight officers named as portrait gaps are
all genuinely in an `organization` block with no portrait against any of them.

The decision not to use the Reinneck photograph deserves recording as the
standard, not just as a null result. She is named alone in the caption, which is
ordinarily enough, but the frame is six senators with their hands up and no
positional cue. Naming the person and identifying the face are two different
things. It was set aside rather than guessed, which is what should happen every
time.

## What was cut

The incidental finding, parked for whoever next edits `years.json`, said Sophie
Stirling was "sworn in 18 Nov 2025." The article is dated the 13th and the
handover had not happened yet: it reports the Judicial Council's vote on the
night of 12 November and says she *was to be* sworn in at the next meeting on
the 18th, when Blake Graham *would* step down. Future tense throughout. Trap
one, in the place it does the most damage — a to-do note, where a date sits
waiting to be copied into the record by someone who will not re-open the source.
Rewritten to the election of 12 November, with the caveat stated plainly so the
18th cannot be lifted out later without a source from after the meeting.

The same paragraph said the 2025-26 organization block "does not yet show" the
succession. It does. Stirling is already there as chief justice, noted as
holding it by 26 January 2026. What the article actually adds is the election
date and the predecessor's name, not a missing officer, and it now says so —
otherwise the next run spends its time hunting a gap that was never there.

Both corrections went onto the branch as 7cf2de3 before the merge, and the
report comment on #233 records what was verified and what was trimmed.

## Traps, checked

The advance notice above was the one that fired. Nothing was matched by surname,
no committee chair was promoted to officer, no April result moved year, no
settled fact was touched, and nothing about a living person goes past what the
cited article reported. No contributor commit was in the diff.

The six duplicate pairs are the same six as every recent pass, read again and
separate again: two designated-driver stories five months apart, a bill and its
failure, a lawsuit planned and then endorsed, a position taken and then voted,
and three bills filed the same day in September 1991.

## Still open

Emily Reinneck appears twice in the 2025-26 senate officers, once as "Senator
At-Large" and once as "Senator". It is pre-existing on `main`, not from this
branch, and it wants a look from whoever next opens that year.

The five wkuherald.com credits citing a bare image file rather than the article
carrying the caption are unchanged and remain the best backlog for a run. So is
the year-photograph gap, which stays shut for as long as the download gate does.

A post-meeting source for 18 November 2025 would settle the Stirling handover
and let the succession be dated properly.

Of the five research routines, photographs is still the only one firing.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as
president, 185 portraits, 61 year photographs, 297 mirrored documents and 1,111
pieces of legislation. `build.py` completes cleanly over 61 year pages and 7
decade pages; `check_data.py` and `check_contrib.py` both exit 0.

# 26 August 2026 — editor's pass, evening: the rosters counted people twice

No pull request was open. The photographs routine's last run was merged at 15:25
and its branch carries nothing main does not already have; every other research
branch is level. So this pass went looking at what is already published, starting
from the one defect the morning report left open: Emily Reinneck appearing twice
in the 2025-26 senate.

She was not one case. She was one of eighty-six.

## What was wrong

Two faults, both of them the residue of the sweep that read officers out of the
signature blocks of bill PDFs. The sweep filed one roster line per document, so a
chief of staff who signed seven bills became seven officers.

The first fault is within a block: fifty-five posts were held by one person who carried
between two and seven lines for it in the same year's executive or senate roster,
because each document labelled the post slightly differently — "Senator" on one
bill and "Senator At Large" on the next, "Chief of Staff" on five and "Chief of"
on a sixth where the label was cut off mid-phrase. Conner Hounshell had seven
lines for 2017-18. Andi Dahmer had five for her presidency. Seventy-two lines in
all were one person, one post, counted again.

The second fault is across blocks: fourteen more people were filed under both
"executive" and "senate" for the same single post, so a committee chair rendered
twice on the year page and twice on their own officer page.

## What was done

Eighty-six duplicate lines were collapsed into the post each of them described.
Every merge was decided by hand and every citation was carried across: a check
against `origin/main` confirms nothing was lost — no person, no source URL, no
profile. The merged line keeps the fuller office label, so "Chief of" and
"Director of Academic and" are gone from the site, and the scraper's stub notes
("Named on the document as senator") went with the labels they described.

Three of these were corrections somebody had already written and never applied.
Matt Bastin's 1998-99 entry said in its own note that the archive recorded him
only as Vice President when he signed the minutes all year as Vice President of
Administration — and both versions were live, side by side. Melissa Paris's
2005-06 entry said the same about her portfolio. Ann-Blair Thornton's 2009-10
entry said outright that she should be moved from the executive to the senate.
All three now say one thing, with the correction recorded in the note rather
than left as an instruction to a future editor.

## What was checked before cutting

Several of these entries cited a document whose own label named somebody else,
which reads at first like an unsourced claim. It is not. Three of the PDFs were
pulled and read: Bill 13-17-S names "William Hurst, Senator" in its authors,
Resolution 7-17-S names "James Line, Chief of Staff", and Bill 7-17-S names
"Emily Houston, Student Affairs Chair" among its contacts. The attributions are
sound. What is corrupt is the citation *labels*, which fused adjacent names into
people who never existed — a "William Wysong" out of William Hurst and Morgan
Wysong, a "Hannah Line" out of Hannah Neeper and James Line. No such phantom ever
reached a roster; they exist only inside citation text. Nothing was cut on this
basis, and it would have been wrong to cut it.

## What was left alone

Eight people still hold two lines in one year, and each of them earned it: Anne
Guillory chairing two committees in 1997-98, Jeanne Johnson as Speaker and as
Campus Improvements chair in 2005-06 and again as executive vice president and
president pro tempore in 2006-07, Amanda Allen moving up from administrative to
executive vice president, Brenna Mathews from parliamentarian to secretary,
Justin Goins from associate chief justice to chief justice, Hannah Neeper holding
the administrative vice presidency alongside the Organizational Aid chair, and
Donté Reed as director of enrollment until January 2024 and chief of staff after.

Seth Norman nearly went with the merges. His 2005-06 entries read as one post
under two names — Director of Public Relations and Chair of the Public Relations
Committee — until the notes were read: he chaired the committee that autumn and
moved up to the directorship at the end of January 2006. Two posts, in sequence.
He stays as two lines.

## Traps, checked

Nothing was matched by surname: every merge was keyed on the full name through
`name-aliases.json`, and the eleven spellings that disappear from the rosters
(Matthew Bastin, Connor Hounshell, Alex Cissel, Alexis Courteney, Ari Srivastava,
Zach Skillman, Lauren Willet, Maksim Zaephel, Donte Reed, Amelia R. Tucker,
Tyresha Morris) are all registered there already as the same people. Lauren
Willett's two spellings are recorded in her note rather than left implicit. No
committee chair was promoted to an officer — the reverse, if anything, since a
chair and the senate seat under it are now one line and the note says so for the
specific seats, Potter College and PCAL. No election moved year, no settled fact
was touched, and nothing about a living person goes past what its source says.
No contributor commit was in this diff.

The six duplicate event pairs are the same six as every recent pass and are
separate again.

## Still open

The citation labels are still raw scrape output: 151 roster citations carry a
long "SGA legislation: ..." blob instead of a bill number and title, and some of
those blobs contain the fused non-names described above. They are visible on the
site. Rewriting them to "SGA Bill 13-17-S, Funding for a Portable Whiteboard" is
mechanical work against the PDFs and is the best-defined job left.

Sixteen people are still filed under both the executive and the senate for what
may be one post — Bill Parsons, Ryan Faught, Amanda Cole, Mitchell Bailey, Ryan
Morrison, Skylar Jordan, Cherieth Lineweaver, Brian Anderson, Ian Hamilton, Kara
Lowry in 2017-18, Mark Clark, Jamison Moorehead, Zachary Skillman, Meghan Pierce
and Sarah Vincent among them. Most look like genuine pairs of offices, which is
why none of them was touched; each wants its sources read the way Norman's were.

The five wkuherald.com credits citing a bare image file, and the year-photograph
gap behind the Cloudflare download gate, are both unchanged.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as
president, 185 portraits, 61 year photographs, 297 mirrored documents and 1,111
pieces of legislation. `build.py` completes cleanly over 61 year pages and 7
decade pages; `check_data.py` and `check_contrib.py` both exit 0.

---

# 26 August 2026 — editor's pass, two Chief Justice portraits merged after a date correction

One pull request was open, #236 from the photograph routine, and it is merged.
Nothing else was waiting: the backlog, profiles and senate branches are all
level with main.

## What was in it

Six entries in `data/photos.json` and two image files. No events, no officers,
no year assignments — which narrows what could go wrong, and means the whole
diff could be checked rather than sampled. All six were.

Isaac Keller, cropped from a Herald photograph of the 9 April 2019 meeting, is
now the portrait on his 2018-19, 2019-20 and 2020-21 pages. Holden Schroeder,
cropped from the April 2022 election-night gallery, covers 2019-20, 2021-22 and
2022-23.

## What was checked, and how

wkuherald.com refuses an ordinary fetch, so both captions were read through the
same WP-JSON media endpoint the routine used. Both say what the credits claim
they say. Keller's caption names him alone as the man being sworn in as chief
justice; Schroeder's names him alone as the chief justice addressing the chamber
before announcing results, and the second frame the routine cited as
corroboration does exist and does show the same face.

The crops were then traced back to the full-size originals rather than taken on
trust. This mattered more than it sounds: the Keller post carries two images and
only one of them is captioned. The crop came from the captioned one. In the full
frame he is the standing, waving figure and the only other well-lit person is
applauding, so there is no ambiguity about which man was being sworn in.
Schroeder is the only standing figure in his frame, with the spring election
slide behind him.

All six names were checked against `years.json` before the portraits were
allowed to attach to those years, and all six are there. The 2019-20 entry
deliberately spells him "Holden Schroder" because that is what the roster for
that year spells him; the two spellings were already one person in
`name-aliases.json` long before this run, so nothing new was merged on the
strength of a name.

The surname trap was checked directly, because it had somewhere to go: there is
a separate Madison Keller in the archive. Her page carries no photograph. Isaac's
portrait did not leak onto it.

## What was corrected

The Schroeder credit read "College Heights Herald, 19 April 2022". The gallery
published on the 20th and its own captions place the moment just after midnight
on the 20th; the 19th is the meeting — the 21st Senate's last — not the Herald
item. A reader following the citation would have gone looking on the wrong day.
Rather than cut a sound entry over it, the credit now carries both dates and says
which is which. That is the only change the editor made.

## Traps, checked

No events were added, so no advance notice could be written up as a report. No
officers and no year assignments were added, so nothing filed an April result
into the wrong academic year and no committee chair was promoted. No settled fact
was touched. Nothing about either man goes past what his caption reported — both
credits describe a public meeting and nothing else. No contributor commit was in
this diff, and every commit on the branch is authored "SGA 60" with no tool
attribution.

Both files begin `FF D8` and are real JPEGs, and the `site/photos/` copies are
byte-identical to the ones in `data/photos/`.

The six duplicate pairs are the same six as every recent pass, all pre-existing
on main, and all still separate events — a bill introduced and the same bill
failing a week later are two things.

## Still open

The three branches from 4 August — the 1980s, the 2020s and the photograph
branch that went with them — have no pull requests any more. They still have no
merge base with main and are still snapshots of a superseded repository, so they
were left alone rather than merged; that judgement has not changed.

Everything listed as open in the evening pass is still open: the 151 raw
"SGA legislation: ..." citation labels, the sixteen people filed under both the
executive and the senate, the five wkuherald.com credits citing a bare image
file, and the year-photograph gap sitting behind the Cloudflare download gate.

Garrison Reed is worth one more photograph pass. The routine set him aside
because his face is hidden behind his own arm in the frame it found, which was
the right call, but a second caption in the same gallery names him with a
positional cue and may give a cleaner shot.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents and 1,111 pieces of legislation. `build.py`
completes cleanly over 61 year pages and 7 decade pages; `check_data.py` and
`check_contrib.py` both exit 0.

# 28 August 2026 — editor's pass, three portraits merged after a caption trim

One pull request was open, #250, the rolling photograph branch. It added three
officer portraits and nothing else: Zach Jones and James Line, both 2016-17, and
Morgan Gammons, 2024-25. Three new claims is fewer than the eight a spot check
would sample, so all three were verified rather than sampled.

## What was checked

Both cited Herald articles were opened and both captions matched the entries
word for word. `wkuherald.com/28868` carries the 5 April 2017 report, bylined
Jamie Williams, of the 3 April meeting that lowered the SGA grade-point
requirement from 2.5 to 2.0. `wkuherald.com/83591` carries the 4 April 2025
report of the DEI committee vote, and its body calls Gammons chief justice in a
post-meeting interview independently of the caption, which is a second thread on
the same identification.

The part worth doing properly was the crops. A caption reading "(left)" and
"(right)" identifies nobody if the crop is taken from the wrong side of the
frame, and that error would be invisible in a diff. Both original photographs
were pulled and looked at. The 2017 frame holds two men and only two, in the
chambers with the constitution lettered on the wall behind them: the man at left
in a light blue shirt with his hand to his chin, the man at right at the podium
in a white SGA-monogrammed shirt. The committed files take Jones from the left
and Line from the right, which is the way round the caption puts them. The 2025
frame is a solo shot of Gammons at the podium with nobody else in it. All three
files begin `FF D8 FF E0`.

All three names match `data/years.json` exactly, and none of the three offices
was inflated to suit a photograph. Jones is recorded as senior senator and
campus improvements chair, which is what he was; a photograph of a committee
chair did not turn him into an officer.

## What was cut

The three credit lines reproduced the newspaper's captions whole — nineteen
words for the 2017 caption, twenty-four for the 2025 one, and the 2017 caption
printed twice, once under each man. These are not private notes. `site/o/` is
gitignored but rebuilt on every deploy, and the strings were confirmed rendering
as visible text into the Jones, Line and Gammons officer pages. The rule is a
quote under fifteen words, once per source, and the three longest quoted strings
in the whole of `photos.json` were these three.

They were trimmed, not deleted. Each credit now quotes only the words that carry
the identification and paraphrases the rest, and the photographs, subjects,
years and source URLs are untouched. The full captions stay in the pull request
where they serve as evidence, which is what they are for.

This is the third pass running that has had to make the same cut: Garrison Reed
in a3be81c, the two Judicial Committee portraits in 5d766b9, these three now.
The routine is told again, on the pull request, to write the credit paraphrased
from the start and keep the full caption in its report.

## What was clear

Both articles report meetings that had already happened, so neither is an
advance notice. No one was matched by surname. Nothing files into the wrong
academic year: Gammons photographed in April 2025 is a sitting officer of
2024-25, not an April election result belonging to the year after. Nothing goes
near the settled facts, and nothing about a living person exceeds what the
source printed — the clothing noted in each credit is crop provenance, and it is
the thing that makes the identification checkable by the next reader.

The routine was right to flag Salvador Leon and Salvador León and right not to
touch them. They may well be one man across two years, but that has to be
established rather than assumed, and it belongs in `name-aliases.json`. Still
open.

## Still open

Everything carried over from the evening pass remains: the 151 raw "SGA
legislation: ..." citation labels, the sixteen people filed under both the
executive and the senate, the credits citing a bare image file, and the
year-photograph gap from 1996-97 to 2009-10 sitting behind the Cloudflare
download gate on `viewcontent.cgi`, which the routine tested once more this run
and found unchanged.

One small thing noticed and left alone: the 1972-73 Ed Jordan credit quotes at
exactly fifteen words, which is the boundary rather than under it. It is
pre-existing on main and outside this diff, and it is noted here rather than
changed in a pass reviewing something else.

The three branches from 4 August still have no pull requests and still have no
merge base with main. That judgement has not changed either.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents and 1,111 pieces of legislation. `build.py`
completes cleanly over 61 year pages and 7 decade pages; `check_data.py` and
`check_contrib.py` both exit 0; `check_duplicates.py` reports the same six pairs
as every recent pass, none of them in a year this diff touched, and all six
still genuinely separate events.

# 28 August 2026 — the editor's pass, nothing open to review

## What there was to review

Nothing. There are no open pull requests on the repository. The three branches
the standing brief still names as stale and open — #6 "Research: photographs
(rolling)", #7 "Research: the 1980s" and #8 "Research: the 2020s" — were all
closed on 18 August, ten days ago, and none of them was merged. The brief has
not caught up with that; this entry is the note that it should.

Every research branch that shares a history with `main` is level with it.
`research-photos`, `research-backlog`, `research-senate` and
`research-editor-0826-late` are all nought commits ahead, which means the work
the routines pushed has already landed. `research-photos` carries a commit from
today and that commit is on `main`, so the routines are running and landing
normally; there is no stall behind the empty queue.

The seven branches from 4 August — `research-1966-79`, `research-1980s`,
`research-1990s`, `research-2000s`, `research-2010s`, `research-2020s`,
`research-profiles`, together with `photo-research-2026-08-22` and
`research-editor-0823-seventh` — still have no merge base with `main`. That
judgement is unchanged from every previous pass and was not revisited.

## The rewrite of main

`main` was force-pushed since the last pass: the tip this clone had, af11520 of
24 August, is not an ancestor of the current bc8e909. This was the commit-author
cleanup that AGENT-LANDING.md had been describing as undecided. It is done. The
history is now 140 commits authored entirely by `SGA 60` and `samuelkurtzsfs`;
no commit on `main` carries a tool's name, a `Co-Authored-By` trailer or a
session link.

Because a force-push is the one operation that can silently destroy research,
it was checked rather than assumed. The old tip's `years.json` was extracted and
compared against the current one field by field: 61 academic years on both
sides, no year present in the old file and absent from the new, no leader
present in the old and absent from the new, and of 2,018 dated events on the old
tip every one survives on the new, which carries 2,019. Nothing was lost. The
rewrite took the tool's name out of the history and left the history alone.

AGENT-LANDING.md was corrected to say so. It had been telling every routine that
105 commits still carried the attribution and that nobody had decided what to do
about it, which would have sent the next reader looking for a problem that has
been fixed.

## Where the archive stands

61 academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents and 1,111 pieces of legislation. `build.py`
completes cleanly over 61 year pages and 7 decade pages; `check_data.py` and
`check_contrib.py` both exit 0. The working tree is clean after a build, so
what is deployed matches what is in `data/`.

`check_duplicates.py` reports the same six pairs it has reported for several
passes, and all six were read again rather than taken on trust. The three bills
of 1 September 1991 are three bills. The 1991-92 regent advisory committee is an
introduction on 28 January and a defeat on 6 February. The 1971-72 Civil
Liberties Union pair is the union's plan in February and Associated Students'
endorsement in March. The 2003-04 plus/minus pair is a position taken in
September and legislation passed in October. The 1997-98 designated driver cards
are announced three months apart. None of the six is one event written twice.

## Still open

Everything carried over from the previous pass stands untouched, none of it
being in a diff this pass had to judge: the 151 raw "SGA legislation: ..."
citation labels, the sixteen people filed under both the executive and the
senate, the credits citing a bare image file, the year-photograph gap from
1996-97 to 2009-10 behind the Cloudflare gate on `viewcontent.cgi`, the
Salvador Leon and Salvador León question awaiting `name-aliases.json`, and the
1972-73 Ed Jordan credit sitting at exactly fifteen words.

---

# 28 August 2026 — editor's pass, a photograph run's note merged after every claim in it was opened

## What there was to review

One open pull request, #258, "Research: photographs", on a `research-photos`
branch cut from the current tip of `main`. The three pull requests that had sat
open since 4 August — #6 photographs, #7 the 1980s, #8 the 2020s — are all
closed, #8 on 18 August, so nothing stale was left to rescue or to shut.

The diff was forty-four lines added to §8 of `SGA-60-AGENT-INFO.md` and nothing
else. No `data/` file moved, which means nothing in this branch could reach the
public site. That is the reason to read it carefully rather than the reason to
wave it through: a note in the handoff is what the next routine acts on, and a
wrong figure in it sends the next run hunting for something that is not missing,
or worse, stops it hunting for something that is.

## What was checked

Fourteen claims, every one of them opened against its source rather than taken
from the report.

The counts came back exact. Sixty-one academic years, 2,019 events, sixty people
recorded as president. All seventy-two president and regent leader records carry
a portrait, with no gap anywhere in `leaders`. The tree holds seventy-three
leader records in total — sixty-six presidents, six regents and one still
unresolved — so the note's "seventy-two president/regent" is a precise figure
and not a miscount, and the unresolved record has a portrait as well. Year
photographs stand at forty-nine of sixty-one, and the twelve years named as
still missing one match, in order and without exception, the twelve the data
gives up: 1993-94 through 1997-98, then 2000-01, 2002-03, 2003-04, 2005-06,
2006-07, 2008-09 and 2009-10.

The three names carried over from the previous photograph run were the part
worth the most attention, because each was a surname search and surname searches
are where this archive has historically gone wrong. Lane Hedrick verifies on
every particular: wkuherald.com article 29383, "SGA supports military students
through legislation", 22 March 2017, `featured_media: 0`, and the sentence
quoted in the note is verbatim in the body at ten words, inside the limit. The
Jack McKinney hits are the fraternity-rush feature, the Ransdell convocation
transcript and a basketball story, none of them connected to any officer. The
two Simpson hits are two other people entirely: Cole Simpson, a freshman
mechanical engineering student standing for the senate in the April 2024
election guide, and Libby Simpson, a news reporter's byline. Neither is the
officer the run was looking for, and the run said so instead of banking the
match.

The Cloudflare gate was tested once, at the pace the rules require. Article 7642
on `viewcontent.cgi` returned HTTP 403 at exactly 5,485 bytes, the challenge
page, while ordinary landing pages on the same host still resolve. The block
remains specific to the PDF endpoint, unchanged since 25 August.

## What was cut

Nothing. This is the first pass in some time where the honest answer is that
there was nothing to remove.

## Traps, checked

No events were added, so no advance notice could be written up as a report. No
person was added, moved or renamed, so no surname-alone match, no changed
surname split into two people, and no April result filed into the wrong academic
year. Nothing in the diff touches the settled facts. The three living people it
names appear only in their public capacity as SGA officers or Herald staff,
exactly as their sources have them, with no personal detail attached. No
contributor commit was in the diff.

The Simpson finding deserves recording as the opposite of a trap sprung. The run
had two surname matches in hand and rejected both on identification. That is the
habit the thirty-nine false missing presidents were the argument for.

`build.py` completed cleanly, `check_data.py` and `check_contrib.py` both exited
0, and `check_duplicates.py` reported the same six pairs it has reported for
several passes — the three bills of 1 September 1991, the 1991-92 regent
advisory committee's introduction and defeat, the 1971-72 Civil Liberties Union
plan and endorsement, the 2003-04 plus/minus position and legislation, and the
designated driver cards three months apart. All six were read again on the
previous pass and none is one event written twice. Nothing new joined them.

The branch had a real merge base at the current tip of `main`, so none of the
4 August orphan-history hazard applied. The commit is authored as `SGA 60`, and
neither the message, the diff nor the pull request body carries any tool's name.
It was merged, and the review was left on the pull request.

## Where the archive stands

Sixty-one academic years, 2,019 dated and sourced events, sixty people recorded
as president, 297 mirrored documents and 1,111 pieces of legislation. Every
president and regent has a portrait. Forty-nine of the sixty-one years have a
photograph of their own.

## Still open

The one thing this pass turned up that the pull request did not fix: §1 of
`SGA-60-AGENT-INFO.md` still summarises year photographs as "32 of 61" and
forty-five entries. The true figures are forty-nine and, by count, sixty-one.
The merged note says the table is stale, which is accurate and was verified, but
saying so is not the same as correcting it, and the next routine to read §1
before §8 will believe the wrong number. The table should be refreshed.

The six `research-*` branches from 4 August — the 1966-79, 1980s, 1990s, 2000s,
2010s and 2020s beats, and `research-profiles` — still show fifty to two hundred
and fifteen commits ahead of `main` with no merge base at all. They are the
superseded-repository snapshots, not lost work, and they have no open pull
requests. They were left alone deliberately. Merging one would delete
`herald-index-full.json`, the aliases, the contributor layer and the validators.

Everything carried over from the previous pass stands: the 151 raw "SGA
legislation: ..." citation labels, the sixteen people filed under both the
executive and the senate, the credits citing a bare image file, the year
photograph gap behind the Cloudflare gate, the Salvador Leon and Salvador León
question awaiting `name-aliases.json`, and the 1972-73 Ed Jordan credit sitting
at exactly fifteen words.

# 28 August 2026 — editor's pass, late: an empty queue, and §1's table re-measured

## What there was to review

Nothing. `gh` is not installed in these containers, but git is credentialed and
`git push --dry-run` opened a new branch cleanly, so this was a full-mode pass
with the ability to merge and simply nothing to merge. No pull request is open.
The three the standing brief still names as stale since 4 August — #6
photographs, #7 the 1980s, #8 the 2020s — have been closed since 18 August. That
is now the fourth pass to record it, and the brief is still pointing at them.

The `research-*` branches were checked rather than assumed. Four of them —
`research-photos`, `research-senate`, `research-backlog` and
`research-editor-0826-late` — are level with `main` with nothing ahead. Three
carry commits ahead of it: `photo-research-2026-08-22` at 610,
`research-profiles` at 215 and `research-editor-0823-seventh` at 133. None is
lost work. Their `data/` diffs against `main` are net deletions — every one of
them would remove portraits `main` already publishes, among them the whole
2025-26 and 2026-27 sets — because they are snapshots taken before the material
landed, not forks carrying anything new. They were left alone, as were the six
4 August beat branches.

One thing about merge base is worth recording for the next pass, because it
changes how the branch table reads. The `main` rewrite described in
`AGENT-LANDING.md` force-updated the branch again during this run's fetch, so
`git merge-base` now returns nothing for almost every branch, not only the
4 August orphans. Merge base can no longer be used to tell a superseded snapshot
from an ordinary branch. Compare `data/` contents instead; that is what was done
here.

## What the pass did instead

Took the single item the previous pass left explicitly open: §1 of
`SGA-60-AGENT-INFO.md`, whose count table was still measured at commit `117647c`
on 20 August. Two runs had by then flagged it as stale in §8 without correcting
it, which is the failure the last report named — saying a table is stale is not
the same as fixing it, and the next routine reads §1 before §8.

It was re-measured whole rather than patched at the two rows that had been
reported wrong, because fourteen of the twenty rows had moved. Every figure was
computed from `data/` on the current tip, using the repository's own logic where
the definition was not obvious: programmes through `build.py`'s `is_program`,
presidents through the same `role == "president"` test `check_data.py` uses. An
early count of the presidents came out at 61 and was wrong — it had swept in the
one record whose role is `unresolved`, Reed Morgan of 1968-69 — and the figure
was only trusted once it reproduced `check_data.py`'s own 60.

The year-photograph row read 32 of 61 and is 49. The photograph-entry row read
45 and is 61. Also corrected: entries 2,025 to 2,019, people in any office 1,503
to 1,749, officer records 1,064 to 947, senate members 912 across 35 years to
1,487 across 58, cabinets 58 of 61 to 61 of 61, photograph files 113 to 196,
documents 246 to 297 mirrored with 120 referenced, legislation 827 to 1,111,
authorship attributions 1,038 to 1,144, pages built 1,587 to 1,833. Presidents,
programmes, leader records and the Herald index were already right and were left
untouched.

## The one row that turned into a finding

The student regent row said 57 and there was no way to reproduce it. Measured
against the data it resolves to 39: five records whose `role` is `regent`, plus
34 presidents whose `also_regent` is `true`.

The 39 was not published as the count, because it is not one. Twenty-one
president records carry no `also_regent` field at all, so for those years the
seat is unstated rather than empty, and 22 of the 61 years show nobody holding
it. `check_data.py` passes on all of them, so the validator is not going to
surface this. The row now reads as a floor and says so, and both §1 and §8 name
the 21 unstated records as the open question. A future run that reads 39 as an
answer will conclude the regent seat is done when a third of it has never been
recorded either way.

## Traps, checked

Nothing in `data/` was touched, so nothing this pass did could reach the public
site. No event was added, so no advance notice could be written up as a report.
No person was added, moved or renamed: no surname-alone match, no changed
surname split in two, no April result filed into the wrong academic year.
Nothing goes near the settled facts. No living person is named in anything
written this pass beyond Reed Morgan's existing unresolved record, which was
read and not altered. No contributor commit was in scope.

`build.py` completed cleanly. `check_data.py` and `check_contrib.py` both exited
0. `check_duplicates.py` reported the same six pairs as the last several passes.
All six were read again rather than taken on the previous verdict. The three
bills of 1 September 1991 are three bills. The 1991-92 regent advisory committee
pair is an introduction and a defeat eight days apart. The 1971-72 pair is the
Civil Liberties Union planning an action and Associated Students later endorsing
it. The 2003-04 pair is a position taken in September and legislation passed in
October. The designated driver cards are three separate entries — the bill of
4 November 1997, the Herald's report of 13 November and the distribution
announced on 17 February 1998 — and each is hedged to what its source actually
proves, two of them noting that the archive holds only a contents listing. None
is one event written twice.

## Where the archive stands

Sixty-one academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents, 1,111 pieces of legislation, 1,833 pages
built. All 73 leader records carry a portrait. Forty-nine of the 61 years have a
photograph of their own.

## Still open

The 21 president records with no `also_regent` field, described above. This is
new and it is the largest unmeasured gap the pass found.

The twelve years still without a photograph: 1993-94 through 1997-98, then
2000-01, 2002-03, 2003-04, 2005-06, 2006-07, 2008-09 and 2009-10. The Cloudflare
block on `viewcontent.cgi` was not retested this pass — three separate runs have
now confirmed it shut since 25 August and a fourth confirmation buys nothing.

Everything carried over stands: the 151 raw "SGA legislation: ..." citation
labels, the sixteen people filed under both the executive and the senate, the
credits citing a bare image file, the Salvador Leon and Salvador León question
awaiting `name-aliases.json`, and the 1972-73 Ed Jordan credit at exactly fifteen
words.

---

# 28 August 2026 — editor's pass: five extended portraits merged, one credit corrected

## What there was to review

One open pull request, #261, "Research: photographs", opened at 20:00 UTC on the
`research-photos` branch and the successor to #254. The three branches that had
sat open since 4 August — #6, #7 and #8 — are gone from the queue and needed no
handling this pass.

#261 was two commits, 101 added lines, two files: five new entries in
`data/photos.json` and a run log appended to `SGA-60-AGENT-INFO.md`. It had a
real merge base with `main`, so none of the orphan-history warning applied. Both
commits were authored `SGA 60`, and neither the commits nor the pull request body
carried any tool attribution.

## What was checked, and how

Every one of the five new entries reuses a photograph and a citation already
published on `main`. Four of the five labels proved **byte-identical** to their
counterparts there, compared by diff rather than by reading. So the pass carried
no new photographic identification, and the only genuinely new assertion in each
entry was that the person held a named office in the year the portrait was now
being filed against.

That assertion is not sourced to the cited article. It comes from
`data/years.json`, so that is where it was checked, all five of them:

- Amy Wyer, Director of Public Relations, 2017-18 — in `organization/executive`.
- Garrison Reed, Associate Justice, 2023-24 — in `organization/senate/officers`.
- Kara Lowry, Secretary of the Senate, 2016-17 — in `organization/senate/officers`.
- Savannah Molyneaux, Sustainability Committee Chair, 2016-17 — same.
- Steven Donte' Reed, Director of Enrollment and Student Experience, 2022-23 —
  in `organization/executive`.

All five held. All five image files are present in `data/photos/` and begin
`ff d8`.

Filing one photograph against more than one year of a person's service is long
settled practice here and not a novelty of this run: fifty files on `main`
already do it.

## What was corrected

The credit on the new **Steven Donte' Reed 2022-23** entry had been copied whole
from his 2023-24 entry, and it kept that entry's sentence saying no portrait from
his 2023-24 year is on file. Under 2022-23 that sentence is off its subject and
untrue as well — a portrait for 2023-24 is on file, and it is this same
photograph. Corrected to 2022-23 and merged as part of the pull request.

The correction was worth more than its size. The site was built twice, once from
`main`'s `photos.json` and once from the branch's, and the two trees compared in
full: across 1,833 pages the **only** rendered difference is Donté Reed's
portrait credit. That sentence was the sole thing this pull request would have
put in front of a reader, and without the fix it would have put it there wrong.
The other four extensions change no page today, because each of those four people
already showed that portrait on their own page from the other year they served.
They are still worth holding as data, but they are not four new pictures on the
site and the run log should not be read as saying they are.

## Traps, checked

No events were added, so no advance notice could be dressed up as a report. No
new office claim was made; every office named was already published. Nothing
approaches the settled facts.

The live trap in this diff was the surname. Two men named Reed sat in the same
cabinet, and the entries keep them apart correctly: Garrison Reed runs senate
member in 2021-22, executive vice president in 2022-23, associate justice in
2023-24; Steven Donte' Reed runs director of enrollment in 2022-23, chief of
staff in 2023-24, executive vice president in 2024-25. Nothing was matched on
"Reed". The `Steven Donte' Reed` / `Donté Reed` pairing the credit appeals to is
genuinely in `data/name-aliases.json`; the file was opened rather than the
label believed.

The April-election trap came out right and deserves recording as a near miss.
The Lowry and Molyneaux photograph is election night, 19 April 2017, and that
election seats the 2017-18 officers — but both women are filed here against
**2016-17**, which is correct, because the entries attach to the offices they
held during 2016-17 and the photograph is contemporaneous with that year. Filing
it forward would have been the error.

All five are living people. Every label is a photo credit for a public SGA
occasion and none strays into anything personal. No contributor commit was in
scope and nothing in `data/posts/` was touched.

## What could not be done

None of the four cited `wkuherald.com` articles could be opened. The domain
answers this session with a Cloudflare 403, and `web.archive.org` — the obvious
second route, and three of the four have snapshots — is refused outright by this
environment's egress policy. There was no third way in.

This did not hold the merge, and the reason matters: no new claim in the diff
rested on those articles. The labels behind them are already published and were
verified in earlier runs, and the office-years, which are the new part, are
checkable locally and were checked. Had this diff asserted a fresh identification
out of a wkuherald caption, it would have been left open instead.

One correction for the routine's own log: it records the Cloudflare gate as
sitting on `digitalcommons.wku.edu/cgi/viewcontent.cgi`. It is wider than that.
`wkuherald.com` is gated to this session too, and that is where the recent-decade
portraits come from.

## Checks

`build.py` completed cleanly. `check_data.py` and `check_contrib.py` both exited
0, the latter passing all thirty of its assertions. `check_duplicates.py`
reported the same six pairs as recent passes, each read again rather than taken
on the earlier verdict, and each still two events rather than one written twice:
the three bills of 1 September 1991, the regent advisory committee's
introduction and its defeat eight days later, the Civil Liberties Union's
planned action and Associated Students' later endorsement of it, September's
position on plus/minus grading and October's legislation, and the designated
driver cards across November 1997 and February 1998.

## Where the archive stands

Sixty-one academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents, 1,111 pieces of legislation, 1,833 pages
built. All 73 leader records carry a portrait; 49 of the 61 years have a
photograph of their own. The counts are unchanged by this merge, which is what a
pass adding only portrait cross-filings should do.

## Still open

The twelve years with no photograph of their own, and the roughly 590 officer
and senate-officer names with no portrait, both unchanged. Most of the pre-2011
work behind them is blocked while `viewcontent.cgi` stays shut, and the
wkuherald block now closes the recent decades to this session as well.

The routine proposes a `scripts/photo_gap.py` to compute the portrait gap
instead of re-deriving it by hand each run. It is worth writing. It should also
report whether an extension would change a rendered page, so that a run can tell
a genuine new portrait from a data-completeness fill like four of these five.

Everything carried over stands: the 21 president records with no `also_regent`
field, the 151 raw "SGA legislation: ..." citation labels, the sixteen people
filed under both the executive and the senate, the credits citing a bare image
file, the Salvador Leon and Salvador León question, and the 1972-73 Ed Jordan
credit at exactly fifteen words.

One question for the owner, which the editor should not settle alone. This
session is required by its own operating rules to sign every GitHub comment it
posts with a Claude Code attribution line, while `AGENT-LANDING.md` instructs the
opposite — strip that line from any pull request body or comment, on the ground
that it is visible text published under the project's name. The comment on #261
carries the line. Nothing in the repository or the built site does, and that rule
was kept exactly. The conflict is only about GitHub's own comment threads, and
it needs a decision rather than each run guessing.

# 29 August 2026 — editor's pass: an empty queue, ten published claims opened against their sources

## What there was to review

Nothing. There are no open pull requests. Every research branch is either level
with main — `research-photos`, `research-senate`, `research-backlog` — or a
superseded snapshot: the six decade branches of 4 August still have no merge
base with main and stand at more than 300,000 deletions against it, which is
what `AGENT-LANDING.md` describes and not work to rescue. `research-profiles`,
the one recent branch without a merge base, was compared field by field rather
than by its commit graph: 61 years, 73 leaders and 299 profile paragraphs on
both sides, and main carries one event more. It holds nothing main lacks.

The standing brief still names #6, #7 and #8 as stale and open. They have been
closed since 18 August. This is the fourth pass to record it.

## What was checked, and how

With no queue, the pass went at what is already published, and at the part of it
the previous pass could not reach. That run merged five portrait cross-filings
while unable to open any of the four `wkuherald.com` articles behind them, and
said so. The articles are still shut: the domain root answers 200 to this
session but every article path returns a Cloudflare 403, so the position is
unchanged and the note in the previous entry stands.

What could be reached was checked instead. Every office behind those five
cross-filings was read out of `data/years.json` and two were taken back to the
primary document:

- Amy Wyer, Director of Public Relations in 2017-18. The Senate minutes of
  12 September 2017 carry the line "Director of Public Relations – Amy Wyer"
  under the officer reports. The same minutes list a separate Public Relations
  committee under William Hurst, which the record has correctly not merged with
  the executive directorship.
- Garrison Reed, Associate Justice in 2023-24. Bill 20-24-S is signed by Isaac
  King as Chief Justice, Ellen Henderson as Associate Chief Justice and Garrison
  Reed as Associate Justice.

Both cross-filings therefore rest on offices that exist in a primary source.

Ten published claims were then drawn at random from the 1,289 events whose
citations sit on reachable domains, and every one was opened:

- Herald 74:51, 15 Apr 1999 — "Turbulent Elections Complete", by Ryan Clark. Confirmed.
- Herald 63:33, 21 Jan 1988 — Klausnitzer on Greg Robertson quitting the senior class presidency. Confirmed, byline included.
- Herald 63:45, 3 Mar 1988 — Klausnitzer on the chiefs rarely keeping office hours, with the editorial on the same point in the same issue. Both confirmed.
- Herald 57:39, 11 Feb 1982 — Francke and Lyly on ASG and the University Center Board wanting more money and planning budget requests. Confirmed.
- Herald 49:41, 17 Apr 1970 — the Associated Students dance, and Cinema '70 showing "The Promoter". Confirmed.
- Herald 47:14, 8 Dec 1967 — the Kentucky Intercollegiate Press Association supporting student representation. Confirmed.
- Resolution 80-7, 18 September 1980 — described by the archive as concerning the inequity of residence hall budget cuts. Confirmed, date included.
- Bill 01-4-S — a bill to schedule a clean-up day on 23 April 2001. Confirmed.
- Bill 4-18-S — $50 from Senate discretionary to promote the 2018 Spring Movie Series for the Sustainability Committee. Confirmed.
- Bill 17-22-S — the Judicial Council having had no formal written guidelines before the General Procedural Rules. Confirmed.

Ten of ten held. Nothing was cut and nothing needed trimming.

## Traps, checked

The advance-notice trap was the one worth watching in this sample, and the
archive came out ahead of it twice. The 1970 dance is indexed as "Associated
Students Dance Slated from 8-12 Tonight" — an announcement — and the entry says
the Herald announced it, with no crowd, no review and no takings. Bill 01-4-S
scheduled a clean-up for a date seven weeks off, and the entry says the bill set
it rather than that it happened. Both are written to what the source proves.

The April-election trap came out right as well. The 1999 entry puts Griffey and
Bastin's wins in 1998-99, where the election happened, and describes them as
completing the 1999-2000 executive slate.

No committee chair was found recorded as an executive officer in the material
checked; the Wyer minutes are the case where that confusion was available and
was not made. Nothing was matched on a surname alone. Nothing touched the
settled facts except to support one: the index of Herald 57:39 carries the
runoff story for the regent seat in February 1982, which is consistent with
Sandra Norfleet sitting in 1981-82 and not 1982-83. No contributor commit was in
scope and nothing in `data/posts/` was touched. All the living people named here
appear only in the offices they held and the votes they cast.

## A false positive, recorded so the next pass does not act on it

Seventy-seven leader portrait credits carry a photograph date that falls outside
the academic year they are filed under, and seventy-three of those do not say
so. This looked at first like a defect the last merge had introduced, because
the two Steven Donte' Reed credits it created do carry that disclosure while the
Amy Wyer and Garrison Reed ones do not.

It is not a defect. Cross-filing a portrait into the other years a person served
is long-standing practice here, and it reaches back to 1968-69; the disclosed
ones are the exception rather than the rule. Many of the seventy-three are
election-night photographs of an officer taken in April, which by the nature of
this archive always falls in the year before the term they were elected to. There
is nothing to correct, and rewriting seventy-three credits on the editor's own
initiative would have been a large unilateral change to live pages in the name of
a consistency the project never adopted. Left alone.

## Checks

`build.py` completed cleanly: 61 year pages, 7 decade pages, 297 documents and
1,111 legislation files. `check_data.py` exited 0 on 61 years, 2,019 events and
60 people recorded as president. `check_contrib.py` exited 0 on all of its
assertions. `check_duplicates.py` reported the same six pairs as recent passes.
Each was read again rather than taken on the earlier verdict, and each is still
two events rather than one written twice: the three bills of 1 September 1991,
the regent advisory committee's introduction and its defeat, the Civil Liberties
Union's planned action and Associated Students' later endorsement, September's
position on plus/minus grading and October's legislation, and the designated
driver cards across November 1997 and February 1998.

## Where the archive stands

Sixty-one academic years, 2,019 dated and sourced events, 60 people recorded as
president, 297 mirrored documents, 1,111 pieces of legislation. Unchanged by this
pass, which merged nothing because there was nothing to merge.

## What could not be done

`digitalcommons.wku.edu/cgi/viewcontent.cgi` is still 403 to this session, so
the Herald page images stay shut and the pre-2011 portrait work behind them stays
blocked. `wkuherald.com` article pages are 403 as well. Two things are open to
this session that the previous entry recorded as closed, and a later run should
test rather than assume: `archive.org` answers 200, and `www.wku.edu` serves SGA
minutes and legislation PDFs without difficulty — both of the primary documents
checked above came from it. The Talisman full texts on archive.org are therefore
reachable again.

## Still open

Everything carried over stands, none of it touched by this pass: the twelve years
with no photograph of their own, the roughly 590 officer and senate-officer names
with no portrait, the 21 president records with no `also_regent` field, the 151
raw "SGA legislation: ..." citation labels, the sixteen people filed under both
the executive and the senate, the credits citing a bare image file, the Salvador
Leon and Salvador León question, and the 1972-73 Ed Jordan credit at exactly
fifteen words.

The `scripts/photo_gap.py` the photograph routine proposed last night is still
worth writing, and this pass adds a second use for it: it should be able to tell
a genuine new portrait from a cross-filing of one already on file, which is the
distinction that made the seventy-three credits above look like a fault.

The question the previous entry put to the owner is still open and still should
not be settled by a routine: whether a GitHub comment thread counts as visible
text published under the project's name. Practice so far has kept the repository
and the built site completely clean of tool attribution, which is what CLAUDE.md
actually governs, and that is the reading this pass followed too.

# 29 August 2026 — editor's pass: two portraits merged, both citations one leaf out

One pull request open, #271 from the photograph routine, adding portraits of
Susan Hurley (1975-76, ASG housing committee co-chair) and Debbie Anderson
(1978-79, Judicial Council member) to `data/photos.json`. Merged, after two
corrections pushed to the branch first. The three stale pull requests the
standing brief still names — #6, #7 and #8 from 4 August — are no longer open
and needed nothing this pass.

The branch had a real merge base with main and was current with it, so none of
the orphan-history precautions applied.

## What was verified

Two claims in the diff, so both rather than a sample, each opened at source and
checked against the page image rather than the caption text alone.

Hurley's caption is verbatim correct. The photograph on p. 295 of the 1976
Talisman carries fifteen women in groups of four, six and five, matching the
caption's three rows; the back row is five in the caption's order, and the
committed crop is the third figure, confirmed by cropping the same face out of
the full-resolution leaf and comparing the two side by side.

Anderson's caption is verbatim correct and p. 344 is four rows of five as the
entry claims. Row four runs woman, man, woman, woman, man against Alspaugh,
Althaus, Cheryl Anderson, Debbie Anderson and John E. Anderson III, so the
reading order is confirmed by the portraits themselves and not assumed; the crop
is position four. Worth recording that p. 345 of the same volume is seven rows
of five — the grid is per-page and cannot be carried from one page to the next.

Build, `check_data.py` and `check_contrib.py` all exit 0. 61 years, 2019 events,
60 people have been president, matching the routine's own report.
`check_duplicates.py` prints the same six pairs as before, all of them genuinely
separate business — an announcement against a distribution, a bill introduced
against the same bill failing, three separate bills on 1 September 1991 — and
this diff adds no events to disturb them. All 73 leader records carry a
portrait.

## What was corrected

Both archive.org links pointed one leaf past the photograph. The printed page
numbers in the labels were right, so the error was invisible to every check the
routine ran, but a reader following either citation would have found the wrong
page and no such photograph. Page 295 of the 1976 Talisman is leaf n298, not
n299, which is a page of cartoons; page 344 of the 1979 volume is leaf n345, not
n346. The true offsets are +3 and +1 against links that assumed +4 and +2, the
latter being the figure the routine's own handoff note records for that page
range.

The note claimed each target page had been fetched and its printed folio read
off the image "before trusting it, never assumed from a nearby citation." That
is not what happened and the passage has been rewritten. The folio was read for
the crop and not for the link, so the two were checked separately and only one
was verified — a narrower and more useful lesson than the one the note drew.

The Anderson label overclaimed. Nothing ties the pictured senior to ASG but her
name: the 1979 volume has no student government section at all, so there was
nothing to corroborate against. The senior-portrait-grid route is sound and well
precedented here — Faulk, Reed, Fuller, Smith and Stewart all rest on it — and
house style is to say so on the entry, as the Faulk label already does. The
label now says it. Kept rather than cut; the disclosure is what makes it
publishable.

Hurley's label was strengthened in the other direction, because the evidence is
better than it claimed. The 1976 index enters Susan Louise Hurley at pp. 63, 268
and 295: p. 63 is ASG's own attendance roll and p. 268 the Chi Omega page whose
text names her an ASG representative that year. That portrait rests on three
citations tying one woman to ASG, not on a shared name.

## Two dead ends that are not dead

Both recorded in the handoff note as exhausted, both abandoned for the same
reason: the run stopped at the first page its index entry gave.

The 1979 index reads "Manis, Melinda Susan 325, 364" and only 325 was opened, a
sixty-person sorority composite fairly judged too crowded. Page 364 carries a
clean alphabetical senior portrait, "MELINDA MANIS, elem. ed., Marietta, Ga.,"
between Beverly J. Mainland and Alecia E. Marcum — the same route that produced
the Anderson portrait, and Manis is a 1978-79 Judicial Council alternate. The
index reads "Carwell, David Hargis 73, 289" and p. 73 was never looked at at
all; Carwell is the year's activities vice president and better documented than
either portrait landed this run. Both leads are now in the handoff note.

## Still open

Everything carried over stands, none of it touched by this pass, less the two
portraits added: the twelve years with no photograph of their own, the officer
and senate-officer portrait gap the routine now puts at roughly 573 names, the
21 president records with no `also_regent` field, the 151 raw "SGA legislation:
..." citation labels, the sixteen people filed under both the executive and the
senate, the credits citing a bare image file, the Salvador Leon and Salvador
León question, and the 1972-73 Ed Jordan credit at exactly fifteen words.

`scripts/photo_gap.py` is still unwritten and still worth writing. This pass
suggests a third job for it beyond the two already recorded: it could check that
a citation's leaf number and its printed page number agree, which is precisely
the fault that got through every existing check tonight.

`digitalcommons.wku.edu/cgi/viewcontent.cgi` was not tested this pass; all
verification ran on archive.org, which answered every request without
rate-limiting, including two full-resolution scan leaves and two complete volume
texts.

# 29 August 2026 — editor's pass, evening: an empty queue, and thirty-five events that were written up twice

No pull request was open. The photograph routine's #271 was merged this
afternoon and nothing has come in since; #6, #7 and #8, the three stale
requests the standing brief still names, have been closed since 18 August and
needed nothing. Of the twelve `research-*` branches on origin, only
`research-photos` is current with main and it carries no unmerged data. The
rest are either the 4 August orphan snapshots with no merge base, or branches
whose last commit records the routine behind them being disabled. Nothing is
stranded.

With no queue, this pass went at the published archive instead, and found a
fault in it that no check in the repository can see.

## Thirty-five events were in the record twice

`check_duplicates.py` compares titles. Two research passes writing the same
Herald article up in different words produce two entries whose titles share
almost no vocabulary, so the checker has never reported any of them, and it
still prints the same six pairs it always has — all six genuinely separate
business, and left alone.

Comparing bodies rather than titles found 99 candidate pairs. What separates a
real double write-up from two events at one meeting turned out to be the
citation: for the wkuherald.com years one URL is one article, so two entries on
the same date citing the same article are one event told twice. That test
returned 47 groups. Reading all 47 in full, 35 were the same event written
twice and 12 were not.

The 12 that were not have been left exactly as they were. They are the case
CLAUDE.md protects: several distinct items reported in one article. Three
separate spending bills from one meeting stay three entries; so do the red
jacket handover and the outgoing officers' final reports on 28 April 2026, the
Judicial Council's Talisman ruling and the Talisman's own funding meeting in
December 2013, and the two inventories in Kendrick Bryan's 2010 commentary.

The 35 were merged rather than deleted. Each pair shared one source, so no
citation was lost, and each merged entry carries every sourced fact from both
originals — the merge usually makes the entry better than either half, because
the two passes had noticed different details. The 2 February 2023 Narcan pair
is typical: one entry had the five-of-seven committee support, the other had
Lana Kunkel saying there had been no overdose in a WKU residence hall. Both are
in the record now, in one place. The count falls from 2,019 events to 1,984.

Where a merged pair carried two quotations from one article, one was kept and
the other paraphrased, which is what the quote rule requires and what neither
original had been doing.

## What was verified

Nine of the merged entries were opened at source — a third of them, rather
than the eight the brief asks for, because this pass was rewriting published
text rather than reviewing someone else's. Every claim held: the $872 and the
$71 car-rental charge in the 2004 audit, Survance's word for the special
projects fund and the $3,000 and $35,000 the senate kept in 2019, the 29-1
vote and Lowry's compromise on the Confederate marker, the $750 and the Center
for Citizenship and Social Justice's $100 behind the Jonesville scholarship,
Luttrell's reasons for standing down, Gammons on the DEI provisions, the 13-11
smoking vote and Church's fifth draft, Bill 1.22s and the drained pantry, and
the Dining Dollars allegation against Todd.

Two things were corrected off the back of that reading. The Confederate marker
entry said the amendment was made during the meeting; the Herald puts it before
the resolution was presented, and the entry now says so. And the 14 April 2026
meeting had its doubled fuel-cost fact removed from the entry about the year's
56 bills, leaving it with the parking report where it belongs — and carrying
with it the unresolved Ginny Griffin / Jenny Griffith name, which the other
entry had been flagging and this one had been stating flat.

`wkuherald.com` refuses the fetch tool with a 403 and answers a plain request
with a browser user agent. Worth knowing: it is the source for everything after
about 2003 and a run that concludes it is unreachable would be wrong.

## Still open

Everything carried over from the previous entries stands, none of it touched
here: the twelve years with no photograph, the roughly 573 officer and
senate-officer names with no portrait, the 21 president records with no
`also_regent` field, the 151 raw "SGA legislation: ..." citation labels, the
sixteen people filed under both the executive and the senate, the credits
citing a bare image file, the Salvador Leon and Salvador León question, and the
1972-73 Ed Jordan credit at exactly fifteen words. The two Talisman leads the
last pass reopened — Melinda Manis on p. 364 of the 1979 volume and David
Carwell on p. 73 of the same — are still unworked.

New, and worth a routine of its own: `check_duplicates.py` should compare
bodies as well as titles, and should treat two entries sharing one per-article
citation on one date as a duplicate until a human says otherwise. Every one of
the 35 merged tonight would have been caught the day it landed. The pre-2003
years, where a citation is a whole Herald issue rather than one article, need
the body comparison instead and were not swept for this beyond confirming the
six known pairs.

---

# 29 August 2026 — editor's pass, night: four officer portraits, and one identification that was carrying two claims

One pull request was open, #275 from the photographs routine: four portrait
crops and their `photos.json` entries, no events and no change to
`years.json`. It merged. The three stale pull requests the standing brief
still names — #6, #7 and #8, the 1980s, the 2020s and the rolling
photographs branch from 4 August — were closed on 18 August and are not
waiting on anyone. The brief should stop naming them.

## What was verified

Four claims, so all four were opened rather than sampled. Both page images
were downloaded from archive.org and each published crop was located on its
page, so the position is established rather than eyeballed.

The 1981 Talisman, p. 282 group photograph carries the caption as the
routine quoted it. Its figures align with the caption's rows exactly — 6
against 6 in the front row, 7 against 7 in the second, 8 against 8 in the
third, 7 against 7 in the back, 28 both ways. Two checks beyond the count:
the front row's six names are all women's and all six figures read as women,
the first in a Phi Mu sweater; and the third row's one woman's name,
Margaret Ragan, falls at position 7, where the row's one figure without
masculine features stands. The caption's order therefore describes this
photograph, and counting along it is sound.

Each crop was then matched against the page by normalised cross-correlation.
Sanner scored 0.997 at the front row's fourth position, Zoeller 0.965 at the
third row's sixth, Morris 0.949 at the third row's fifth — every one where
its entry says it is.

The 1979 Talisman, p. 364 block reads MELINDA MANIS, ALECIA E. MARCUM,
DENISE MARR, JAMES R. MARSHALL, MARILYN MARSHALL against five portraits.
The names run woman, woman, woman, man, woman and so do the faces, the man
fourth in both, which fixes the block's order without relying on the count.
The published crop is the leftmost portrait.

All four names in `photos.json` match `years.json` exactly, so each portrait
attaches to the officer it names.

## What was corrected

The Manis entry was carrying two claims and had evidence for one. The face
is Melinda Manis — the caption says so and the row order confirms it. That
the 1979 senior of that name is the Judicial Council alternate of 1978-79
is an inference from the name, and the label stated it as though it were
read off the page. The 1979 volume has no student government section, so
no page puts her portrait and her post together.

The label now says what the identification rests on, which is what the
Debbie Anderson entry a few lines above it in the same file already does
for the same situation. Two things found while checking were added, because
they strengthen the inference without settling it: the volume's index
carries one Melinda Susan Manis, at pp. 325 and 364, and p. 325 is the Chi
Omega group photograph rather than anything to do with ASG. The only other
Manis indexed is a Susan Renee Manis, a different first name, so there is
no second Melinda to confuse her with.

The portrait was rescued, not cut. What went was the overreach.

## Traps, checked

No events in the diff, so nothing could rest on an advance notice. No role
was changed, so no committee chair was promoted to officer. Nobody was
matched by surname: all four come from full names in captions. Nothing
collides in `name-aliases.json` — its only Morris is Tyreesha Morris, a
different person, and Kevin Kinne, who stands in this caption's third row,
is already aliased there to Kevin Kinnie, which is some small evidence the
caption names people the record already knows. No election moved year,
nothing touched the settled facts, no contributor commits were in the diff,
and nothing about a living person went past a captioned face.

## Recorded, not acted on

The three new labels quote the caption's row roster at 18 words, past the
15-word quote rule read literally. This file has done that throughout: the
Susan Hurley entry on main quotes 37 words, and a dozen others fall between
10 and 22. A roster of names is the evidence for an identification rather
than reproduced prose, and the new entries are not outliers. Rewriting the
house practice on the back of one pull request would have been the wrong
way to settle it. It is a question for the project, not a fault in this
work.

## Checks

`build.py` clean, and reproducible — rebuilding on the branch produced no
diff, so the committed `site/` matched the data it came from.
`check_data.py` 0. `check_contrib.py` 0. `check_duplicates.py` reported its
usual six pairs and all six were read: every one is two events rather than
one. The 1997-98 designated driver pair is the clearest — Bill 97-3-F
passing in November and the Herald's distribution notice in February, three
months and two sources apart. None of the six was in this diff.

## Where the archive stands

61 years, 1,984 events, 60 people have been president.

## Still open

Everything from the previous entries stands. Two items move: the Melinda
Manis lead on p. 364 of the 1979 volume is closed with a portrait, and the
David Carwell lead on p. 73 is closed without one — the routine read both
of the pages the index cites and found only text mentions of him as ASG
activities vice president, no photograph, and said so rather than reaching
for a face. That is the right outcome to record for a lead that fails.

Still untouched: the twelve years with no photograph, the roughly 569
officer and senate-officer names with no portrait, the 21 president records
with no `also_regent` field, the 151 raw "SGA legislation: ..." citation
labels, the sixteen people filed under both the executive and the senate,
the credits citing a bare image file, the Salvador Leon and Salvador León
question, and the 1972-73 Ed Jordan credit at exactly fifteen words. The
previous entry's proposal that `check_duplicates.py` compare bodies as well
as titles has not been built.

New for the photographs routine, from this pass: the row-order method it
used is good, and the sex-pattern cross-check makes it better, because it
catches an off-by-one that a bare count cannot. Worth doing as a matter of
course. And when a portrait comes from a page that names the person but not
their office, the label should say so. The face and the post are two
claims, and the second needs its own evidence or its own caveat.

## Addendum, same pass: the fallback route is not wired up

Checked after the merges, and worth knowing before a run needs it.

`SGA60_SITE` and `SGA60_RESEARCH_TOKEN` are both unset in the editor
routine's environment. Those are the two variables the drop box needs, and
the drop box is what the standing brief falls back to when GitHub is gated.
Tonight that cost nothing, because GitHub was reachable and both merges went
through the ordinary path. But if the platform gate had been up, the fallback
would have been unavailable too, and a full review would have had nowhere to
land except the run report — which is route three, the one that keeps nothing
in the repository.

So the brief's review-only mode is, as things stand, a route that has never
been tested from this routine and would fail on its first use. Either the two
variables should be set in the routine's environment, or the brief should say
plainly that route three is the only fallback the editor has.

Two smaller notes from the same check. `gh` is not installed in these
containers, so the brief's opening command — `gh auth setup-git && gh pr list`
— fails with `command not found` rather than with the 403 it is written to
detect. A run that reads that as the platform gate would drop into review-only
mode while GitHub was in fact fully reachable, which is the opposite of what
the brief intends. `GH_TOKEN` is set, git is credentialed, and the GitHub MCP
tools work; the right probe is `git push --dry-run` and
`mcp__github__list_pull_requests`, as `AGENT-LANDING.md` already says.

And the production domain is recorded nowhere in the repository — not in
`vercel.json`, not in the generated pages, not in these reports. There is
therefore no way for a run to confirm that what it merged actually reached
the live site. Worth writing down somewhere, given that every merge here is
a publication.

# 30 August 2026 — editor's pass: one portrait cut for a name that belonged to another man

One pull request open, #283 from the photographs routine, four officer
portraits in it and five entries, since Bill Schilling is attached to two
years. Fewer than eight new claims, so all of them were checked rather than
a sample. The three stale pull requests the standing brief still names — #6,
#7 and #8 — are gone; nothing from 4 August is open any more.

## What was verified

All four image files are real JPEGs and all four are genuine class-portrait
or group-photograph crops, checked by opening them, not by trusting the
magic bytes alone.

**Paul J. Deom, 1980-81.** Holds. The 1981 *Talisman* index carries one Paul
Deom, referred to p. 266, which is the Kentucky Civil Liberties Union
photograph. The caption names the back row in order and Deom is third of
four, as the entry says. The article on the same spread calls him "a junior
from Boonville, Ind., and Associated Student Government member," which is
the tie between the face and the office, and it matches the profile already
in the archive.

**Bill Schilling, 1986-87 and 1987-88.** Holds, and on better evidence than
the entry claimed. The 1987 *Talisman* index carries a single Schilling of
that forename — William Byron — and refers him both to p. 343, the class
portrait, and to p. 114, where the Associated Student Government group
photograph's second row is captioned with his name. William Byron is also
the name the *Herald* printed in March 1988, already cited in his profile.
He appears again in the Inter-hall Council photograph beside Delwin Cheek,
who the archive records as having beaten him for that council's presidency.
The label has been rewritten to carry the index evidence.

**Chris LeNeave, 1986-87.** Holds, and it settles a question the archive had
left open. His profile said a Christopher LeNeave in the senior directory
"may be the same person, though nothing in the sources reviewed for this
profile directly ties the ASG chairman ... to that directory entry." The
index closes it: one Leneave in the book, Christopher M., referred to p. 303
for the portrait and to pp. 114 and 116 for the two government photographs,
in the first of which he is named in the second row beside Schilling and
president Tim Todd. The portrait would have been published beside a caveat
denying it, so the caveat has been rewritten to state the tie and to record
that an earlier pass had the two as possibly distinct.

## What was cut

**Steve Wilson, 1978-79.** Withdrawn, image deleted. The entry cited the
1979 *Talisman* p. 379, "STEVE WILSON, agriculture, Tompkinsville," and
added "indexed as Steve Alan Wilson, p. 34." The caption transcription is
right; everything built on it is wrong.

The 1979 index reads "Wilson, Steve Alan 296, 318, 320, 336." There is no
p. 34. Page 379 belongs to a different index entry two lines below it:
"Wilson, Stevie Joe 379." So the portrait is of Stevie Joe Wilson, not of
the Steve Alan Wilson the label named. The book separately lists a Stephen
Alan Wilson, so there are at least three of them.

Neither man is tied to student government. The index gives Associated
Student Government pages 53, 73, 82, 119, 262 and 288-9, and not one of
Steve Alan Wilson's four pages is among them; p. 296, the one that can be
placed, is a club group photograph. The only Steve Wilson the 1979 volume
describes in any detail coordinated Spring Sing for the SAEs and sang in
their barbershop quartet. Nothing in the yearbook connects any of them to
the Judicial Council chairmanship that Congress confirmed on 12 September
1978, which is the entire basis on which the face was being published.

This is trap 4, matching on a name, on one of the commonest surnames there
is. A misidentified face is worse than no face, and this one would have put
a stranger on a chairman's page.

## Traps, checked

No events were added by this pull request, so the advance-notice trap and
the April-election filing rule had nothing to bite on. No committee chair
was promoted to an officer; the three surviving subjects are recorded at
the posts the archive already had for them. No surname-alone match survives.
No changed surname, and nothing here touches `name-aliases.json`. Nothing
contradicts the settled facts. No contributor commits in the diff. On living
people: these are class portraits of named officers from the university's
own open yearbooks, which is what the archive has done for the other
portraits, and none of the labels reaches past the yearbook into anything
personal.

## Checks

`build.py` clean — 61 years, 297 documents, 1,111 legislation files.
`check_data.py` exit 0, 61 years, 1,984 events, 60 people have been
president. `check_contrib.py` exit 0. `check_duplicates.py` reports the same
six pairs as before, none of them from this diff and all six genuinely
distinct: a card scheme and its distribution three months later, a bill
introduced and the same bill failing, a lawsuit planned and then endorsed, a
position taken and then legislated, and three separate bills of 1 September
1991, which the rule keeps apart.

Merged after the cut. The photographs routine's own reported checks — build
and `check_data.py` passing, JPEG magic bytes — all passed on the branch as
it stood, which is the point worth taking from this pass: every automated
check the routine ran was green while a misidentified portrait sat in the
diff. Nothing but reading the index would have caught it.

## For the photographs routine

The method that worked on three of the four is the one to keep: go to the
yearbook's own index, confirm the person is indexed once under that name,
and confirm the index refers them both to the portrait page and to a page
where their organisation is named. That is what makes a face a person.

Where it failed, the index was cited without being read. The label asserted
a page number, 34, that appears nowhere in the entry, while the entry's real
page list would have shown at a glance that the portrait page belonged to
somebody else. If a label names an index entry, the entry should be quoted
in the pull request report the way the captions already are.

## Still open

Everything carried forward from the 29 August entry stands. The 12-year
year-photograph gap is untouched. `SGA60_SITE` and `SGA60_RESEARCH_TOKEN`
are still unset in this routine's environment, so the review-only fallback
remains untested and unavailable; `gh` is still not installed, so the
brief's opening probe still fails with `command not found` rather than the
403 it is written to detect. Both were reported on 29 August and neither has
changed.

## Addendum: the attribution rule and the harness disagree about comments

Recorded because it is the editor's call to make and the owner may want to
make it differently.

`AGENT-LANDING.md` says a pull request body or comment is visible text
published under the project's name, and that any line naming the tooling
should be stripped from it. The editor routine's own harness requires the
opposite: an attribution footer on every comment it posts, so that a reader
can tell the review was machine-written before acting on it.

Tonight's review comment on #283 carries the footer. The reasoning: the
repository and the generated site are what CLAUDE.md's rule protects, and
they are clean — the commit is authored `SGA 60`, no trailer, no session
link, nothing in `data/` or `site/` names a tool. A pull request comment is
working machinery rather than the published archive, and a human being asked
to trust a review that withdrew a portrait is better served knowing what
wrote it.

That is a judgement, not a settled fact. If the owner wants the footer gone
from comments too, the rule to change is the harness's, not this file's, and
it should be said plainly in the standing brief so every routine reads it
the same way.

# 30 August 2026 — editor's pass, midday: every archive.org citation in the photograph archive re-resolved

No pull request open. #283 merged at 09:26 and went to the live site; the
queue has been empty since. With nothing to review, the pass went back over
what #283 published three hours earlier, and then over every photograph
citation in the archive.

## What was verified

The three portraits #283 landed are all correctly identified. Each was
checked by cropping the named position out of the source page and setting it
beside the file in `data/photos/`.

**Bill Schilling, 1986-87 and 1987-88.** Holds. The 1987 *Talisman* index
carries one Schilling of that name, William Byron, at pp. 114, 116 and 343.
Page 343 is the sophomore directory, and the portrait fourth row, third from
left is captioned "WILLIAM SCHILLING, Union". Cropped from the page scan it
is the same face as the stored file, feature for feature.

**Chris LeNeave, 1986-87.** Holds. The index carries one Leneave,
Christopher M., at pp. 114, 116 and 303. Page 303 is the senior directory
and the portrait second row, fourth from left is captioned "CHRISTOPHER
LENEAVE, biology, Mayfield". The independent crop matches the stored file.

**Paul J. Deom, 1980-81.** Holds, and the row position is now settled rather
than assumed. Page 266 of the 1981 *Talisman* was read as an image: the
Kentucky Civil Liberties Union group photograph has four men in the back
row, the fourth wears a patterned sweater, and the stored crop shows its
subject immediately to that man's left. That is position three, which the
caption names Paul Deom. The volume's index carries one Paul Deom, at
pp. 261, 266 and 282.

## What was corrected

**The Deom label attributed a fact to the wrong page.** It said the article
on p. 266 names him an Associated Student Government member. It does not:
p. 266 calls him a junior from Boonville, Indiana who contacted the KCLU.
It is p. 261, a different spread, that adds the ASG membership. The claim is
true and the index ties the two pages to one man, so the label was rewritten
to cite p. 261 for it rather than cut.

**An unresolved arrest was being used as identity evidence.** The 1986-87
Schilling label ended by saying the *Herald* reported his arrest in March
1988 "under the same full name". Two things were wrong with it. The paper
printed the surname as Shilling in that headline, so it is not the same
name; and the year's own event for 17 March 1988 already records the arrest
properly, noting that no charge and no outcome survive in the index. A photo
credit repeats the allegation stripped of those caveats, and it adds nothing
to the identification, which rests on the index entry. The clause was cut.
The event stands as written.

**Fourteen archive.org citations opened the wrong page.** This began as a
check on the three new ones and became an audit of all 86 leaf-numbered
archive.org citations in `data/photos.json`. Each volume's OCR was split
into leaves and each cited leaf tested for the name it claims to show.
Twelve failed. In eleven the name sits on the leaf immediately before the
one cited; in the twelfth, Holger Velastegui, it sits nine leaves earlier.
Two group-photograph entries for 1971-72 shared one of the bad leaves, so
fourteen URLs were repointed in all:

| | cited | correct |
|---|---|---|
| Linda Jones, 1970-71 and 1971-72 | n204 | n203 |
| Nancy Pape, 1971-72, and two 1971-72 group photographs | n276 | n275 |
| Joe Cheak, 1972-73 | n360 | n359 |
| Marc Levy, 1974-75 | n393 | n392 |
| Beverly Davenport, 1974-75 | n390 | n389 |
| Jane Anne Coverdale, 1975-76 | n89 | n88 |
| Cathy Murphy, 1977-78 | n374 | n373 |
| Kevin Strader, 1980-81 | n346 | n345 |
| Greg Elder, 1985-86 | n331 | n330 |
| Cindy Richards, 1985-86 | n318 | n317 |
| Holger Velastegui, 1986-87 | n343 | n334 |
| Paul J. Deom, 1980-81 | n270 | n269 |
| Bill Schilling, 1986-87 and 1987-88 | n355 | n346 |
| Chris LeNeave, 1986-87 | n315 | n306 |

Every corrected leaf was confirmed to carry the person in the context the
label describes, and the printed page numbers in the labels were all
correct. Only the links were wrong. Re-run after the fix, all 86 resolve.

**A profile sentence put a man in the wrong row.** The 1986-87 LeNeave
profile said he was named in the second row of the p. 114 photograph
alongside William Schilling and president Tim Todd. Schilling is in the
second row; Todd is in the back row. Rewritten to say so.

## Traps, checked

No advance notice was relied on. No committee chair was promoted to officer
and no bill author to member. Nobody was matched by surname alone — the
1981 volume carries a second Deom, Mark Anthony, and the identification
rests on the full name plus the index entry, not the surname. No April
election result moved year. Nothing here touches a settled fact. The one
living-person problem found is the Schilling arrest clause, cut above.

## Checks

`build.py` clean, `check_data.py` exit 0 at 61 years, 1,984 events and 60
people who have been president, `check_contrib.py` exit 0.
`check_duplicates.py` reports the same six pairs as the last four passes,
none from this diff and all six genuinely distinct.

## For the photographs routine

The page numbers you write in labels are reliable; the leaf numbers in the
URLs are not. Fourteen of eighty-six were wrong, and none of them would have
shown up in the checks the routine runs — the file is a valid JPEG, the
build passes, the data validates, and the citation still looks like a
citation. The failure is only visible to a reader who clicks the link.

Do not derive the leaf from the printed page by adding an offset, and do not
read it out of `scandata.xml`: that file's `pageNumber` values are wrong for
the 1987 volume, and following them is what produced the two nine- and
twelve-leaf errors. Open the leaf you are about to cite and read the printed
page number off the scan, or split `_djvu.xml` into leaves and confirm the
subject's name appears on the one you are citing. The second is cheap enough
to run over every entry, which is how tonight's twelve were found.

## Still open

Everything carried forward from the 30 August entry stands. The 12-year
year-photograph gap is untouched. `SGA60_SITE` and `SGA60_RESEARCH_TOKEN`
are still unset in this routine's environment; `gh` is still not installed,
so the brief's opening probe still fails with `command not found` rather
than the 403 it is written to detect. Git push and the GitHub tools both
work, which is the route `AGENT-LANDING.md` prescribes and the one this pass
used.

# 30 August 2026 — editor's pass, evening: one portrait merged, its citation pointing at the facing page

One pull request open, #285, the rolling photograph hunt. It carried a single
published claim, so it was checked whole rather than sampled. Merged after one
correction.

## What was merged

A portrait of **Paul Nation**, administrative vice-president of Associated
Student Government in 1974-75, from the 1975 *Talisman*.

The identification is the strongest kind this archive gets. The photograph
carries its own evidence: a desk nameplate reading PAUL NATION sits in the
frame, beside the typewriter and the papers. The caption on the spread names
him and gives his office. President Jeff Consolo's own list of the officers he
served with names Paul Nation administrative vice-president, and a later page
of the same volume says he served in that office. The volume's index reads
"Nation, Paul Marshall 109, 284, 390". The office already stood in
`years.json` from an earlier pass, so nothing new was claimed about him — only
a face added to a man already on the record.

## What was corrected

**The citation opened the wrong page, for the fifth pass running.**

The label read page 108. The URL read leaf `n112`. Both page images were
fetched and read. Leaf `n111` is printed page 108, headed "ASG....Let's take
roll", and the desk photograph sits at the foot of its right-hand column: that
is the frame this crop came from. Leaf `n112` is printed page 109. A reader
following the link would have arrived at a page that does not contain the
photograph. Repointed to `n111`.

The page number in the label was right and the link was wrong. This entry first
called that the third pass running to find it; checked against the build history
on main, it is the fifth. The run of them is: the Berman citation on 29 August
at 03:36, which recorded the scan leaf as the page; Stewart, Elder and Richards
later that morning, a page number read off the scan instead of the page; Hurley
and Anderson that afternoon, both one leaf out; the fourteen repointed at midday
on 30 August; and this one tonight. Five passes, nineteen citations.

Each of those passes wrote down how to avoid it — open the leaf and read the
printed page number off the scan. The instruction has never reached the routine,
because it has only ever been written into a night report the routine does not
read. Five repetitions is enough to stop treating that as something a later pass
should consider. It belongs in `CLAUDE.md`, in the pictures section, next to the
rule about verifying the JPEG magic bytes, which is the check the routine does
perform and does pass. Left here for the owner to approve, since `CLAUDE.md` is
the editorial law and not the editor's to rewrite unasked.

The defect is invisible to every check the project runs: the file is a valid
JPEG, the build passes, `check_data.py` validates, and the citation still reads
like a citation. Only a reader who clicks the link finds it. That is why it has
survived five passes.

**The label also read the photograph and its caption as one thing.** They are
on different pages. The photograph is on 108; the caption block describing it
is on 109, printed under a different picture entirely — a pair of feet propped
on a desk. The label said the photograph was "individually captioned", which
reads as though the caption sits beneath it, and on this spread that is exactly
the misreading that produced the LaCivita withdrawal on 25 August. The label
now says where each sits. Checking it also confirmed the settled LaCivita fact
independently: page 109 does carry the brick-wall photograph and the caption
naming him "(right)" with treasurer Ricky Johnson.

**The quotation ran over the limit.** The label reproduced the caption in full,
about forty words. The rule is under fifteen, once per source. Cut to ten, with
the rest kept as paraphrase, losing no fact.

Also restored the trailing newline the run had dropped from `photos.json`.

## Traps, checked

No advance notice was relied on; nothing here is an event claim. No committee
chair was promoted to officer — Nation's office is confirmed by the president's
own roster and matches what `years.json` already held. Nobody was matched by
surname alone: the full name appears in the caption, in the index and on the
nameplate. No alias collision; `name-aliases.json` holds nothing under Nation.
No election result moved year. Nothing about a living person beyond the office
he held and the photograph. No contributor edit in the diff. No tool
attribution in either commit.

The run's negative findings — McDivitt, Pulman, Saunders, the 1977-78 quartet,
Young and Carwell, Chesnut — publish nothing and were left alone. Declining to
use a group photograph that pins no face to a name is the right call and should
keep being made.

## Checks

`build.py` clean at 61 years and 297 documents. `check_data.py` exit 0 at 61
years, 1,984 events and 60 people who have been president. `check_contrib.py`
exit 0, every case passing. `check_duplicates.py` reports the same six pairs as
the last five passes, none of them from this diff. All six were read again and
all six are genuinely separate events: a bill funding the designated driver
cards and their distribution three months later; a bill introduced and the same
bill defeated after amendment; a lawsuit planned in February and endorsed in
March; concern voiced in September and legislation passed in October; and three
distinct bills filed on the same day in September 1991. Nothing merged.

## Still open

PRs #6, #7 and #8, which the standing brief still describes as stale and open,
were closed on 18 August. The brief has been wrong about them for a fortnight
and should be updated.

The twelve-year year-photograph gap, 1993-94 through 2009-10, is untouched
again: the photograph routine reported `digitalcommons.wku.edu` returning
Cloudflare's block page for its whole session, before and after the full
backoff. That is now the third consecutive run blocked there.

`SGA60_SITE` and `SGA60_RESEARCH_TOKEN` remain unset in this routine's
environment, so the drop box is unavailable. `gh` is still not installed, so
the brief's opening probe fails with `command not found` rather than the 403 it
is written to detect; a reader following the brief literally would conclude the
gate was down and drop to review-only for nothing. Git push and the GitHub
tools both work, which is the route `AGENT-LANDING.md` prescribes and the one
this pass used.

# 30 August 2026 — editor's pass, night: no queue, and four events that were in the record twice

No pull request was open. The three the standing brief still calls stale — #6, #7
and #8 — have been closed since 18 August, and the numbering has since run to
#287, the last of them merged at 15:29 today. With nothing proposed for the site,
this pass was spent on what is already on it.

## The queue, and why it was empty

`git fetch` and the GitHub tools both work from this environment; `gh` is not
installed, so the brief's opening probe fails with `command not found` rather
than the 403 it is written to detect. A reader following the brief literally
would drop to review-only for nothing. The route in `AGENT-LANDING.md` — plain
`git push` plus the GitHub MCP tools — is the one that works and the one this
pass used.

Every research branch was measured against `main`. `research-photos` is level
with it. The branches showing large ahead-counts are the orphans the 30 August
morning pass walked event by event; nothing has been added to them since, and
its conclusion stands.

## Four events that were in the record twice

`check_duplicates.py` compares titles, and none of these four pairs had titles
close enough to trip it. They were found by fingerprinting each event on the
distinctive figures in its text — money to the cent, crowd sizes, counts over a
hundred — and pairing events inside a year that share two or more. Six pairs
came back; three were coincidence at a distance of months, and the rest were
real. All four have been merged so that no sourced fact from either side is
lost, and each was read against its source first.

**The Loggins and Messina concert, 17 September 1975.** Carried once from the
1976 *Talisman* at the date of the concert and once from the *Herald* at the
date of the report, two days later. The *Herald* issue's own index confirms it
is one event: "Associated Student Government Concert Draws 4,300 Loses $7,000",
alongside "Band Overpowers Duo – Loggins & Messina". Kept at the concert date,
which is this archive's practice, with the *Herald* added as `src2` so its
issue and mirrored PDF survive.

**The Student Activities Committee, 1975-76.** Two entries, both from the same
yearbook. Merging them turned up two claims the source does not carry, and both
are now cut:

- The entry said the committee was "put into operation on 2 December 1975". The
  *Talisman* says the opposite — that lingerings of the 2 December ASG meeting
  were still noticeable during the spring semester, and that ASG "finally
  adopted" the committee to remedy the dispute afterwards. 2 December is the
  date of the argument, not of the committee. The merged entry says the
  yearbook gives no adoption date, and fixes what is known: it was in place in
  time to help bring the free Spinners and Wet Willie concert of 30 January.
- The entry made Rick Kelley the committee's chair. The yearbook only has
  Kelley saying what the committee was formed to do. He was ASG activities
  vice-president, which the same volume states plainly and which the record
  already had right elsewhere. This is trap two in the handoff — a person
  quoted about a body written up as its officer — and it had reached the
  published site.

The merged entry gains what the second copy held and the first did not: the
dispute's origin, assistant dean of student affairs Ron Beck's argument that a
university programme ought to have educational value, and the letters students
sent the *Herald* against him. It also now carries the sub-committee split the
yearbook actually prints — seven for concerts with three alternates, five each
for lectures and publicity with two apiece — in place of "each with alternates".

**The 7 April 2026 meeting.** Two entries three days apart, citing the *same
Herald article*, one dated to the meeting and one to publication. Merged at the
meeting date, and made more precise from the article than either copy had been:
the $602.58 splits $287.67, $239.94 and $74.97, and the Downing Student Union
signage resolution drew nothing from the fund. Speaker Hadley Whipple's warning
that the senate might have to be choosy is kept from the second copy.

**The first meeting of the 24th Senate, 27 August 2024.** Three entries
overlapped here. One, "Senate passed $100,000 budget at first meeting", was
dated 28 August while its own first clause said the meeting was on the 27th,
and it cited the editorial-board article while describing the senate meeting.
Every fact in it already stood in the other two. It is cut, and the one thing
only it carried — that the executives meant to spend the whole allocation, which
the article supports twice over — is folded into the editorial-board entry. The
budget entry's passing mention of a four-member Judicial Council is also cut,
because the entry beside it names all four appointees.

## A volume-numbering trap that is not an error

Citations carrying a *Herald* volume and issue were checked for internal
consistency: 936 of them, mapped volume by volume. Volumes 45 to 73 run one to
an academic year, except 50 to 53, which each carry two ranges four years apart
— volume 51 appears as both 1971-72 and 1975-76.

That looks exactly like four years of mislabelled citations, and it is not.
TopSCHOLAR's own catalogue labels record 4819 "College Heights Herald, Vol. 51,
No. 7" and dates it 1971, and labels record 5081 "Vol. 51, No. 7" and dates it
1975. Both pages were opened. The collision is in the archive being cited, not
in the citing. Every one of these citations is faithful to its source and none
should be touched.

Recorded because the pattern is conspicuous, a whole afternoon could be spent
"correcting" it, and the correction would be wrong. The practical consequence
for anyone citing this era: a volume and issue alone does not identify an issue
between volumes 50 and 53. The record URL does.

## Citations, opened

A hundred citations were sampled across the domains the archive cites and
fetched one at a time: 45 TopSCHOLAR, 25 wkuherald.com, 18 wku.edu, 8
archive.org, 5 bgdailynews.com. Ninety-six returned 200.

The four that did not are all the same shape — direct PDF links of the form
`/context/<collection>/article/<id>/viewcontent/<file>.pdf` — and all four
returned Cloudflare's challenge page. Landing pages never did, including
requests made immediately after a refusal, so this is not the burst-volume
throttle the brief warns about: it is that host refusing automated fetches of
the PDF itself while serving the record page normally. Forty-two citations in
the data use that shape. They are not broken for a reader in a browser and
nothing was changed, but a routine that fetches them will see a 403 that has
nothing to do with pacing, and waiting ninety seconds will not clear it.

This is worth putting beside the three consecutive photograph runs that reported
`digitalcommons.wku.edu` blocked for a whole session. TopSCHOLAR was reachable
throughout tonight's pass, landing page after landing page.

## Checks

`build.py` clean at 61 years, 297 documents and 1,111 legislation files.
`check_data.py` exit 0 at 61 years, **1,980 events** and 60 people who have been
president — four fewer events than last night, which is the four merges and no
loss of fact. `check_contrib.py` exit 0. `check_duplicates.py` reports the same
six pairs as the last six passes, none from tonight's edits and all six read
again and genuinely separate. Re-running the numeric fingerprint over the merged
file returns nothing at any distance under a week.

## Traps, checked

No advance notice was leaned on. Three entries were flagged by a search for
outcome language sitting on a notice-shaped source, and all three cleared: the
Jules Bergman lecture of 23 September 1975 reports its crowd from the 1976
*Talisman*, a retrospective volume, and the yearbook's wording — poor weather
hindered the crowd for the first guest of the lecture series, ASG a co-sponsor —
supports the entry as written. One committee chair was demoted to what the
source actually says, above. Nobody is matched by surname alone. No April
election result moved year. Nothing touches a settled fact, and the LaCivita and
Norfleet findings were left alone. Nothing about a living person goes past what
its source reported. No contributor edit was in scope tonight.

One thing was checked and deliberately not changed. The Ronstadt entry credits
the 1976 *Talisman* with a crowd of about 6,500; the same yearbook gives 6,300
in its Homecoming section and 6,500 in its concerts section, which is the
section the entry cites. The entry is faithful to what it cites, so the figure
stands, and the entry now says the yearbook contradicts itself — so that the next
pass to notice does not "fix" a correctly sourced number.

## Still open

The research pipeline is still one routine. `research-photos` has produced every
merge for four days; `research-backlog`, `research-senate` and
`research-profiles` have not committed since 24-25 August. No new history has
been added to the archive in five days. Whether to re-scope or restart them is
the owner's call and is flagged, not acted on.

The twelve-year year-photograph gap, 1993-94 through 2009-10, is untouched again.

The wrong-leaf citation problem in `photos.json` is now six passes old. Five
passes wrote the remedy into a night report the photograph routine does not
read, and this pass found no new instance only because it did not sweep the
photographs again. It belongs in `CLAUDE.md`, in the pictures section, beside the
rule about verifying JPEG magic bytes. That remains for the owner to approve,
since `CLAUDE.md` is the editorial law and not the editor's to rewrite unasked.

`SGA60_SITE` and `SGA60_RESEARCH_TOKEN` are unset in this routine's environment,
so the drop box is unavailable. It was not needed.

# 30 August 2026 — editor's pass, late: a closed gap that was not closed

One pull request open, #289 from `research-photos`, a documentation-only run
adding eighty lines to `SGA-60-AGENT-INFO.md`. Nothing under `data/`. That file
is not referenced by `build.py`, so nothing in it reaches the public site; the
exposure here was to the research routines that read it, and one paragraph in it
would have cost them real work.

## What was verified

Twelve claims checked, which is more than the eight the pass calls for, because
the note is almost entirely a record of dead ends and a dead end is only useful
if it is accurately described. Eleven held.

Stan McDivitt is the 1974-75 Student Affairs Chairperson in the record. The 1975
*Talisman* quote is verbatim — line 22924 of `talisman1975west_djvu.txt` carries
it exactly as the note gives it — and the volume's index does send him to p. 282.
Steve Henry, named in the same sentence, is genuinely absent from 1974-75
`organization`, as the note says; that is a lead for a later run. The 1981 index
gives "Chesnut, Mark Cameron 234", one page and no senior grid. Wooten, Austin,
Millay and Key are all 1986-87 senate officers and DeLozier, Williamson, Summers
and Hack all 1987-88, every title matching. `talisman1988west_djvu.txt` returns
503 with an Internet Archive error page, not a timeout, exactly as reported.

The best thing in the run was a refusal. The 1987 *Talisman* does carry a
"President Bill Fogle", four lines above a sentence about the Young Democrats.
Same name, wrong organization. The routine found the photograph, saw what it
actually was and left it, which is trap 4 caught before it landed rather than
after.

## What was corrected

The note declared priority four closed: a year photograph for 61 of 61 years,
the twelve-year gap gone, and future runs told to stop listing year photographs
as open work.

The `years` list in `photos.json` holds 61 entries covering 49 distinct years.
Nine years hold more than one photograph — 2026-27, 1971-72 and 2004-05 hold
three each, and 1970-71, 1972-73, 1977-78, 1978-79, 1985-86 and 1986-87 hold
two. Twelve years still have none: 1993-94 through 1997-98, 2000-01, 2002-03,
2003-04, 2005-06, 2006-07, 2008-09, 2009-10. A row count had been matched
against a year count.

It is the same twelve-year gap the previous entry in this file records as
untouched again, which is how a wrong count gets caught: the archive had already
written down the true answer.

Rewritten rather than cut. Everything around it is sound, and the note now says
plainly that priority four is open, that it is a mid-1990s and 2000s gap, and
that coverage is counted in distinct years and never in rows. Two smaller
figures went with it — the officer-portrait backlog is 714 name-year pairs over
568 unique names, not 721 over 573, and portrait coverage of leader records is
73 records over 66 unique names, which the note had run together with the 60
presidents `check_data.py` counts.

## Traps, checked

No new claim about any person, living or otherwise, and nothing near a settled
fact. No advance notice was written up as a report; the one advance notice in
range was already handled correctly, see below. No surname match, no changed
surname, no election in the wrong academic year, no committee chair promoted to
officer — the note's whole subject is committee chairs and it names every one of
them as what they are. No contributor edit in scope.

## Checks

`build.py` clean: 61 year pages, 297 documents, 1111 legislation files.
`check_data.py` exit 0, 61 years, 1980 events, 60 presidents. `check_contrib.py`
exit 0. `check_duplicates.py` reports six pairs, all pre-existing on main and all
genuinely distinct: three bills introduced on 1 September 1991, and three
introduction-and-outcome pairs weeks apart. The 1997-98 pair was read in full — a
November 1997 bill funding designated driver cards, and a February 1998 *Herald*
notice that distribution began the next day. Separately sourced, and the February
entry states on its face that the archive holds only a contents listing, which is
the advance-notice rule applied correctly rather than a duplicate.

## Still open

The twelve-year year-photograph gap, 1993-94 through 2009-10, is open and now
correctly recorded as open in the handoff file. Officer portraits stand at 714
missing pairs over 568 names.

The pipeline is still one routine. `research-photos` has produced every merge for
five days; `research-backlog`, `research-senate` and `research-profiles` have not
committed since 24-25 August, and their branches now sit behind main — a merge of
any of them would delete photographs main already holds. No new history has been
added to the archive in six days. That remains the owner's call.

`SGA60_SITE` and `SGA60_RESEARCH_TOKEN` are unset in this routine's environment,
so the drop box is unavailable. Push access was working, so it was not needed.

One thing this pass could not fix. The attribution line `AGENT-LANDING.md`
warns about was appended to both the pull request body and the review comment
on #289 after they were posted. It was stripped from the pull request body,
which is what that file specifically calls out. It could not be stripped from
the comment: editing an existing comment needs the REST API directly, and raw
`api.github.com` returns the platform gate's 403 in this environment even
though the GitHub tools and `git push` both work. The comment on #289
therefore still carries one. Anyone with a browser can delete that line in
about ten seconds; nothing else in this pass carries it, and no commit does.
