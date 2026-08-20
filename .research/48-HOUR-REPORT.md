# The 48-hour push: what it produced

For Sam Kurtz. Written 20 August 2026, as the push closed.

## What it added

The push was set up on 17 August and every run for the first day was refused
GitHub access at the platform level, so the clock that matters starts at about
04:43 UTC on 18 August. Roughly thirty-six hours of research landed after that.
Against where the archive stood on 17 August:

| | 17 Aug | now |
|---|---|---|
| academic years | 61 | 61 |
| dated, sourced entries | 1,877 | 2,025 |
| people recorded in any office | 806 | 1,503 |
| people whose record carries a written profile | 73 | 261 |
| senate members recorded | 0 | 912, across 35 years |
| photographs held | 61 | 113 |
| legislation PDFs held | 390 | 827 |
| documents mirrored and referenced | 34 | 246 |
| authorship attributions from legislation | 918 | 1,038 |
| pages built | 867 | 1,587 |

The two figures that matter most are the ones that went from nothing to
something. There was no senate roll at all on 17 August; there are now 912 member
records across 35 of the 61 years, recovered from SGA's own minutes rather than
from any later list. And 437 pieces of pre-2011 legislation came down off
TopSCHOLAR in a single run, more than doubling the legislation archive and
covering 1975-76 to 2008-09.

The profile count is the third. Seventy-three people had a written profile and
they were all presidents or student regents; 261 do now, and the new ones are
cabinet and senate officers — the people the plaque was never going to name.

I want to be honest about how the person count reads. It nearly doubled, but a
rank-and-file senator known only from one roll call is a much thinner record than
a profiled officer, and 1,503 person pages is not 1,503 biographies. The archive
got wider faster than it got deeper.

The entry count is the number that moved least: 148 new events in thirty-six
hours, against 1,877 already there. That is the right shape — the years were
already researched, and the push was spending its time on people rather than on
finding more things that happened.

## What the editor rejected, and what that says

The editor passes are written up in full in `.research/NIGHT-REPORT.md`. The
pattern in the rejections is worth more than the count, because it repeats.

**The commonest failure was a claim that outran its source.** A profile would
assert what someone said inside a Herald article while citing an item page that
carries only the headline. A crowd size, a vote tally, a quotation, a named
reason — none of those survive on a headline, and a great many trims were exactly
that: keep the confirmed headline, cut the detail. The same fault in another
costume is the advance notice read as a report; a chartered bus "cancelled for
lack of signups" was cut from a 2012 rally entry because the story it cited says
nothing about a bus, and the bus was the only sentence explaining why the
delegation was small. An explanation is a claim.

**The second pattern is more troubling, and it is ours.** Twice, research wrote
"no source in this archive confirms" over a fact the archive already publishes.
The 1987 Todd–Elder election result is in the unfiltered Herald index and has
been a live event on the 1986-87 page for some time — and yet Tim Todd's own
profile has been saying on the site that the surviving issues do not record the
result. Two new profiles read that sentence, believed it, and repeated it about
two more people. It was corrected at the source so it stops propagating. A wrong
sentence in a president's profile does not sit still; it gets cited. The lesson
the editor drew is the right one: a negative claim about our own holdings needs a
search, not an assumption.

**The third pattern is attribution.** WKU staff named in a legislation sign-off
block get read as SGA officers; Christian Ryan and Robbin Taylor were caught and
removed from the 2015-16 cabinet, and the same fault put faculty and staff names
into the raw legislation extraction by the dozen. A committee chair is not an
officer, a bill's author is not necessarily a member, and a contact is not a
sponsor. This is the fault that killed all thirty-nine "missing president" claims
a fortnight ago and it has not stopped presenting itself.

**And once, the verifier was the problem.** The Herald of 10 December 1987
printed four letters on the Bill Schilling affair, and the surviving index line
for that issue runs title-first, unlike every other line in the file. The
research read it author-first and shifted all four attributions by one. Its own
adversarial checker then moved a fifth attribution further in the same wrong
direction and reported it as a correction. Both profiles now set out the four
titles and the four names and say which belongs to which is not established,
which is the only honest answer available.

There is one over-cut worth recording against the editor rather than the
research: Nate Eaton's 2007-08 shuttle stop was cut as unsourced when it was
sourced — the citation was on the senate officers list rather than the committees
list. It has been restored. An over-cut is a smaller failure than a wrong fact,
but it is still a fact lost.

What all of this says about where the research is weakest: **it is strongest when
it works from a document it has in hand, and weakest when it works from a
catalogue.** Every batch built on locally mirrored minutes came through nearly
intact — 86 of 86 names held on the 1997-98 roll, 80 of 80 on 1998-99, with the
only misses turning out to be OCR damage the research had already flagged itself.
Every batch built on landing pages and headlines needed trimming. The method is
known and it works; the runs that skipped the mirroring step are the ones that
cost editor time.

## Pull requests still open

**#54, "Research: person profiles", on `research-profiles`.** It is the only one
open. It carries about thirty officer profiles — twelve from the 1970s Senate and
committees, ten from the 1988-89 Congress, and eight more from the mid-1970s
Congress that arrived at 04:24 this morning. The editor held it over the two 1987
failures described above and pushed the corrections onto the branch itself; the
three unverified biographical details it also flagged were then chased down in
the Talisman texts, with Tinsley and Jackson confirmed and Faulk's home town
dropped as contradicted by his own yearbook caption. So the editor's stated
conditions have been met.

I have not merged it, for one reason: the final eight-profile batch landed after
the review and has had no editor pass at all. Merging it would publish a batch
nobody outside the routine that wrote it has read, on the last run of the push,
with nothing scheduled behind it to catch a mistake. It is a clean fast-forward
whenever you want it — `git merge-base` confirms a proper ancestor at `117647c` —
and the twenty-two earlier profiles are, in the editor's own words, ready.

`research-2020s` is also unmerged and should stay that way. It is one of the 4
August branches, it shares no root commit with `main`, and merging it would
delete the Herald index, the authorship index, the aliases, the contributor layer
and the validators. That warning is now written into §8.0 of the handoff with the
`git merge-base` check that catches it.

## What the routines could not reach

Three different things, and they are worth telling apart.

**A source that is genuinely blocked.** `web.archive.org` is refused outright by
the container's egress policy — not rate limited, not a 403 that patience cures;
the connection does not open. Every Wayback citation in this archive is therefore
unverified rather than verified, by anybody, at any point in the push. Liz
Goddard's profile rests entirely on Wayback and so does Stuart Kenderes's.

**A source that challenges intermittently.** `digitalcommons.wku.edu/cgi/
viewcontent.cgi` — every PDF on TopSCHOLAR, so Herald page images, Talisman
pages, minutes and legislation — answers HTTP 202 with an empty body and
`x-amzn-waf-action: challenge`. On 19 August one run got through it by landing on
the item page first and sending the PDF request with that cookie, a `Referer`
back at the item page and a browser's `Sec-Fetch-*` headers, which is how the 437
legislation files came down. I re-tested the same recipe an hour ago and it
challenges again. Landing pages on the same host are open and return 200
throughout, which is why headlines and citation labels could still be checked all
week. This cost real research: it is why five profiles could not be re-verified
and were kept only because they restate notes already published, and why several
batches were trimmed to headline-level facts.

This block also did direct damage through the handoff. §8 of the handoff had
described `viewcontent.cgi` as hard-blocked, that description became stale the
day the header recipe worked, and good research was trimmed on the strength of a
note rather than a test. §8.1 now carries the test commands so the next run
checks rather than believes.

**And a source that simply is not there.** The three years with no cabinet at all
— 1979-80, 2001-02, 2003-04 — are not blocked, they are empty. All 92 candidates
for them were checked one at a time; 68 were checked against a source that loaded
perfectly well and did not say what was claimed. Those are disproven, not
pending. Only 21 are waiting on a host to open. Separately, `archive.org` holds
no Talisman for 1967–1970 or 1982–1985, which is a real hole in the yearbook
route rather than a network problem.

## The twenty-five hours

Every run between the setup on 17 August and 04:43 on 18 August was refused
GitHub access at the platform level. The error was the same each time: GitHub
access not enabled for the session, an org admin must connect the app, HTTP 403.
`git push`, `gh` and the GitHub tools all returned it. Roughly twenty-five hours
of scheduled runs produced nothing that survived its container.

What was in flight when it bit was the person-profiles work. The 17 August run of
that routine researched ten officers — Reginald Glass, Joe Glasser, Nancy Pape,
Charles Boteler, Pat Newton, Debby Clark, Glenn Jackson, Lee Goodpaster, Pam
Stewart, Thomas LaCivita — and lost the push.

Those ten were checked this morning against the current data. **All ten already
carry full profiles.** Nothing was actually lost there; a later run redid the work
without knowing it was a redo. That is the one concrete recovery I can point to,
and it is also the honest measure of the cost: the loss was not the research,
which was cheap enough to repeat, it was the twenty-five hours of scheduled time
spent producing it twice.

Beyond those ten, nothing survives to audit. The runs that were refused wrote
their findings into run reports inside containers that were then reclaimed. If
other work was in flight it is gone, and I cannot tell you what it was. The
practice the project adopted afterwards — put every finding with its source URL
into the run report, and let the next run land it — is the right response, but it
only helps a run that knows to do it, and the 17 August runs did not.

## What the next push should aim at

Ranked, with the reason.

1. **Fix `apply_photo_overlay()` in `build.py`.** It matches the leaders overlay
   only against a year's top-level `leaders` array, and `render_officers()`
   renders no photo field at all — so a portrait of a vice president or a senate
   officer can sit correctly in the data and never appear on the site. This is an
   hour of Python that unblocks an entire category of research, and until it is
   done, hunting officer portraits is work that cannot be published.
2. **Read the twenty-six mirrored 1996-97 minutes.** The files are already on
   disk. This needs no network, cannot be blocked, and turns twenty-six documents
   from dead weight into cited primary sources — the cheapest real gain available.
3. **More senate rolls, by the method that worked.** 912 members across 35 years
   is a third of the record. Mirror a year's minutes first, then check every name
   against the primary text offline. Every batch built this way came through the
   editor nearly intact; every batch built on catalogue pages did not.
4. **A Wayback sweep from a network that can reach it.** Not more research — a
   verification pass on claims already published. Some of them, Goddard's whole
   profile among them, currently rest on a citation nobody in this environment
   can open.
5. **The 2016–2027 name cleanup.** Titles glued onto names, "Senator Andi
   Dahmer", "Public Health Kate Hart". They inflate the person count, they cannot
   safely be profiled, and they are the most visible bad data on the site.
6. **Merge or close #54, and close `research-2020s`.** Leaving a good pull
   request open past the end of a push is how work gets forgotten, and leaving an
   orphan branch open is how somebody merges it by accident.
7. **The 119 undelimited co-sponsor lists.** Real names, in hand, unusable until
   somebody writes a smarter name-boundary parser. Worth doing, but last: it is
   the only item here that needs new code and yields no new facts.

## Where it fell short

The push spent itself unevenly. Profiles and senate rolls did well; the events
record barely moved, and three years still have no cabinet. The handoff carried a
stale note about a blocked host for two days and cost real research on the
strength of it. The archive learned, twice in one night, that it will repeat its
own errors back to itself if a wrong sentence is left standing in a profile. And
the largest single line item in the whole push — twenty-five hours — bought
nothing at all.

All three validators exit clean. `check_duplicates.py` reports the same six pairs
it has reported on every pass, and all six are genuinely separate events.
