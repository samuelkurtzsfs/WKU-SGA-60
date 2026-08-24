# Senate rolls, 24 August (scheduled run, later pass)

## The stored prompt is stale, again

This run's stored prompt describes the same premise every "senate rolls" run
since 21 August has already found stale: it claims the archive holds zero
rank-and-file senate members and that `.research/senators-unverified.json`
still holds 105 unreconciled draft names. Neither is true. Re-checked before
doing anything else:

- `.research/senators-unverified.json` is `[]` — already reconciled.
- 58 of 61 academic years already carry `organization.senate.members`. The
  three without it (1966-67, 1969-70, 1979-80) are documented permanent gaps:
  no surviving TopSCHOLAR minutes for the first two, and a re-researched,
  re-confirmed negative finding for 1979-80 (no Congress roster survives that
  year, only two committee chairmen who are never called seated members).
- PR #190, "Research: the senate rolls," is already open from an earlier run
  today and is current with this branch's head (`research-senate` has a real
  merge base with `main`, not an orphan). That run reconfirmed the same
  staleness and then did real work: 1983-84 went from 11 to 25 recorded
  members plus one officer, adversarially verified, five names corrected.

## What this run tried

With the reconciliation and the survey both already done, I looked for the
next real gap rather than re-confirming the same staleness a further time.
1976-77 was flagged (alongside 1983-84, already worked) as under-mined: 25
surviving SGA minutes on TopSCHOLAR, only 2 ever read into the archive
(22 Feb and 19 Apr 1977).

- `digitalcommons.wku.edu/cgi/viewcontent.cgi` was closed for this entire
  session — every attempt returned HTTP 202 with the WAF challenge, landing
  page and PDF alike (tested against SGA minutes item 10, article 1046, and
  Herald issue 5153, article 6155, with the browser-navigation headers and
  cookie/Referer chain that has worked on other days; five attempts spread
  over roughly 20 minutes with the documented 3s/90s pacing). Per the
  project's own notes this challenge opens and closes by the hour, so this is
  a closed window, not a permanent block — a future run should just try
  again.
- The 1977 Talisman (`archive.org/download/talisman1977west/...`, reachable
  and used) turned out to already be fully mined for 1976-77: its ASG feature
  (pp. 50-51) is the cited source for Vogt, Blair, Payne, Keown and Kelley
  already in the record, and the one uncited name in it — Don Augenstein,
  named only as a co-organizer of the Rules and Elections committee alongside
  Bob Moore and Georgiana Carlson (both already recorded, from Congress
  minutes, not the yearbook) — is exactly the "committee chair is not a
  member" trap CLAUDE.md warns about and was correctly left out by whichever
  earlier pass mined this page. Not added.

## Two real leads for whoever gets `viewcontent.cgi` open next

Found via the local Herald index (`data/herald-index-full.json`), not yet
opened because both are Herald issue PDFs and the endpoint was closed all
session:

- **`dlsc_ua_records/5153`** (Herald 51:57, 23 Apr 1976, article id 6155) —
  headlined "New Associated Student Government Congressmen, Officers Are
  Sworn In." This is exactly the shape of article that has yielded full
  rosters elsewhere in this project (see the 1979-80 find in
  `SGA-60-AGENT-INFO.md` §8.3 item 1) and would name the incoming 1976-77
  Congress — the year this run was trying to work.
- **`dlsc_ua_records/5357`** (Herald 52:39, 28 Jan 1977) — headlined
  "Associated Student Government Expels 3 – Alice Pannier, Paul Stamp, Mary
  Smith." Three named former Congress members, not currently in the record.
  Read the article itself before adding anything: an expulsion is exactly
  the kind of living-person-adjacent claim CLAUDE.md's rules on outcomes
  apply to, and the abstract index only gives the headline, not what the
  article actually says happened or why.

Neither was added to `data/years.json` — no PDF text was reachable this
session to source them from. Flagging rather than guessing, per the
project's own rule that a source you could not open is not one that says
nothing.

## Nothing changed in `data/`

No commits to `data/years.json` this run. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both still pass clean against the branch as
left by the earlier 24 August run.
