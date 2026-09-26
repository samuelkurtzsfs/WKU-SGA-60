# Photograph run, 26 September (third pass): baseline reconfirmed, both blocked routes still shut

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and 6.
`research-photos` was behind `origin/main` by one commit (`bf872754`, an unrelated 2003-04 dating
fix); merged cleanly, no conflicts. No pull request was open on this branch — the two earlier runs
today (the scheduled morning pass and a second pass) had already merged and landed without leaving
one open.

Re-verified programmatically rather than by trusting the prior reports: **0 of the 73 leader records
(every president and every student regent, including the four originally-named targets — Nick Todd,
Katie Dawson, Jeanne Johnson, Reagan Gilley) lack a portrait.** All four target files confirmed
present on disk and starting `FF D8 FF E0`. Priorities 1 and 2 are fully done. 217 executive/senate
officer records and 4 years (1994-95, 1995-96, 2000-01, 2008-09) still lack a photograph — the same
counts the second pass left. (217, counting by name and year, is the figure the second pass recorded
and the editor's earlier note settled; this log first read 216 and was corrected on review.)

## Both long-blocked access routes, tested fresh this session, both still shut

- **`digitalcommons.wku.edu/cgi/viewcontent.cgi`**, tested against article 6469 (David Bass's "New
  Vice President" article, Herald 27 Oct 1977) with the documented browser-navigation headers and,
  after the first 403, a full 90-second backoff and retry: both attempts returned `HTTP/2 403` with
  `cf-mitigated: challenge`, `server: cloudflare` and a Cloudflare Turnstile challenge page in the
  body — the same signature every run this week has logged, unaffected by pacing or retrying.
- **`web.archive.org`**, tested plain over HTTPS: connection reset by peer after the TLS handshake,
  consistent with the proxy-level `ws_closed_mid_exchange` the scheduled morning run recorded. Not
  retried a second time since the morning run had already established this is a standing block in
  this container, not a transient failure worth spending a retry on.

Net effect: nothing behind either route could be reached this run either, so the four-year
year-photograph gap and the David-Bass-adjacent pre-1990 officer leads that depend on a Talisman PDF
or a Herald PDF outside archive.org's held volumes remain untouched.

## Did not repeat this morning's or the second pass's searches

Both earlier runs today already swept, independently and thoroughly: the eight pre-1990 officer names
reachable through archive.org's Talisman text (Pulman, Bass, Young, Wicks, Wilson, Chesnut, Millay,
Austin — Bass already correctly handled via the existing 1977-78 group photograph, the other seven
genuine dead ends against that specific holding), and the current-decade wkuherald.com leads (ten
names, plus the five 2025-26/2026-27 freshman senators who are not yet due for a re-check). Re-running
either sweep a third time in the same day would spend requests without adding information; both are
recorded in `.research/photo-run-2026-09-26-scheduled.md` and `.research/photo-run-2026-09-26-second.md`
in enough detail for any future run to pick up from, and this run's own fresh tests of the two access
routes above reached the identical conclusion those two runs did.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean on the merged branch.
No file in `data/` changed — this run's entire diff is this log, for the same reason every prior one
gives: recording that the two access routes were retested and are still closed, so a fourth run today
does not spend a request finding that out again.

## For the next run

- Priorities 1 and 2 (every president and student regent) remain fully done.
- Both blocked routes are still worth a fresh one-shot test at the start of a new run — they have
  flipped open and shut across different container instances within the same week — but a third
  identical test within the same day adds nothing once two runs have already confirmed the same
  signature.
- Nothing else in the four-year year-photograph gap or the 217-record officer gap changed hands this
  run.
