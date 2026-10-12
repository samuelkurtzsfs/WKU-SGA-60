# Photograph run, 12 October (third pass): the `archive.org` Talisman route checked on its own, found open, and found to add nothing the 7-10 October runs had not already closed

## Priorities 1, 2 and 4: reconfirmed programmatically, unchanged

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): checked against
`data/photos.json` before anything else. All four still carry a portrait.

**Priority 2** (any other president or student regent without a portrait): every `leaders`
record in `data/years.json`, across all 61 years, checked by name against `data/photos.json`.
Zero missing.

**Priority 4** (years with no photograph at all): checked which year ids in `data/years.json`
have no entry in `photos.json`'s `years` array. Only **1994-95**, unchanged since 11 October.

## Access this session: `archive.org`'s Talisman route specifically, not just the three routes the last two runs logged

The two prior passes today (afternoon/editor review, second pass) tested `wkuherald.com`,
`digitalcommons.wku.edu/cgi/viewcontent.cgi` and `web.archive.org`, but neither logged a direct
test of plain `archive.org` (the Talisman djvu-text and page-image route `scripts/talisman.py`
uses, which is a separate host and route from `web.archive.org`'s Wayback Machine and has gone
down independently of it before). Tested directly this pass:

- `archive.org/download/talisman1975west/talisman1975west_djvu.txt` — HTTP 302 to an `ia*.us.archive.org`
  mirror, then 200, full text downloaded.
- `archive.org/download/talisman1975west/page/n112_w2400.jpg` (via `scripts/talisman.py 1975 --page 112`) —
  real JPEG, FF D8 header confirmed. **Open.**
- `web.archive.org` — `curl: (35) Recv failure: Connection reset by peer`, matching the standing
  egress-policy denial. **Closed**, independently of `archive.org` being open — the two hosts are
  not the same gate.
- `digitalcommons.wku.edu/cgi/viewcontent.cgi` — HTTP 403 against article 8989 (the standing
  1994-95 lead). **Closed.**
- `wkuherald.com/` — HTTP 403 (no managed-challenge page fetched to inspect, just the bare code).
  **Closed** this pass, where the second pass this afternoon had found it open — consistent with
  the intermittency both prior notes already flagged, not a new finding.

## Priority 3: the one route open this pass checked against the one slice it can reach, and closed again

`portrait_gap.py --list` filtered to the academic years archive.org's 19 Talisman volumes cover
(1970-71 through 1980-81, plus 1985-86 and 1986-87 — `talisman1982west` through
`talisman1985west` are not on archive.org) returns exactly eight names:

Vern Pulman (1974-75), David Bass (1977-78), David Young (1978-79), Steve Wilson (1978-79),
Alice Wicks (1978-79), Mark Chesnut (1980-81), Chris Millay (1986-87), Dwight Austin (1986-87).

All eight were checked individually against this exact route across the 13 September through
10 October runs (see `photo-run-2026-10-09-third.md` for Bass, Young and Wilson in detail). The
findings stand: Bass appears in a group photograph already filed as a `years` entry for 1977-78
because no face can be matched to his name in it; Young is quoted in text but neither photograph
on his page shows him; the rest returned no photograph at all. Re-querying the djvu text and
`BookReaderImages.php` for these eight names this pass (same search terms, same volumes) returned
the identical hits already on record — nothing new, because nothing in the archive.org scans has
changed since the last check. Not re-litigated past that confirmation; CLAUDE.md's bar (a
caption that names the subject, alone or clearly) is still not met for any of the eight.

## Nothing changed

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run.
`python3 scripts/build.py` and `python3 scripts/check_data.py` both exit clean (61 years, 1968
events, 60 presidents). This run's only output is this note.

## For the next run

- **`archive.org` (plain, Talisman) and `web.archive.org` (Wayback) are different gates and must
  be tested separately.** This pass found the first open and the second closed at the same time;
  a note that only tries one must not be read as having tried the other.
- The reachable Talisman slice (the eight names above) is now individually exhausted across at
  least four separate passes (13 Sept, 7 Oct, 9 Oct, 12 Oct). A future run should not re-spend
  time on these eight without a new source turning up; they are closed, not merely unchecked.
- Priority 3's wider gap (159 people, 157 with no portrait anywhere) is otherwise all pre-2011
  names behind the still-closed `cgi/viewcontent.cgi`, or names already exhausted on
  `wkuherald.com` per the 11-12 October notes. There is no untried slice reachable from any route
  open this pass.
- The 1994-95 year-photo gap's next step is unchanged: `cgi/viewcontent.cgi` against article 8989
  (Herald 69:51, pp. 6-9) and the unread tail of article 8933 (Herald 70:56, pp. 8-29), the moment
  that route opens — `archive.org` cannot help here, since no Talisman was published for 1994-95.
- No open pull request exists for `research-photos` (`gh api repos/.../pulls?state=open` confirms
  empty); opening a fresh one with this note as its body, per standing practice when none is open.
