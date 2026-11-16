# Photograph run, 16 November (fourth scheduled pass): web.archive.org's block identified precisely, no new portrait

## Baseline reconfirmed

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`.
- **Priority 2**: `python3 scripts/check_data.py` exits clean — 61 years, 1964 events, 60
  presidents, every president and student regent portrayed.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` still reports the same ~155-157
  person no-portrait-anywhere gap logged by every pass since early November. Checked a further
  sample of officer names across 1996-2012 (judicial council members, committee chairs, IT/PR
  directors) against `data/photo-finds/*-notes.json`: every one already carries a prior search
  record. No new name resolved this pass.
- **Priority 4**: all 61 years still carry at least one photograph.

## What this pass actually settled: the `web.archive.org` block is a proxy policy block, not a flaky remote reset

Every report since mid-September has logged `web.archive.org` as "connection reset" or
"unchanged," with a standing note (`SGA-60-AGENT-INFO.md` §4) that it varies by container and
should be tested fresh each time rather than assumed. This pass tested it properly rather than
repeating the same one-line probe:

- `archive.org/wayback/available` (a different hostname from `web.archive.org`) answers cleanly —
  confirmed snapshots exist for `wku.edu/sga` across 2017, 2019, 2021 and 2023, each with a
  `web.archive.org/web/<timestamp>/...` replay URL.
- Fetching that replay URL directly returns, immediately and consistently: `HTTP 403`, body
  `Blocked by egress policy`, header `x-block-reason: hostname_blocked`. This is this session's
  own egress proxy refusing the hostname outright, not a timeout, not a mid-transfer reset from
  the remote end, and not the Claude Code Remote environment's network policy (`get_environment`
  reports this environment as `unrestricted`, so the block sits below that layer, in the
  proxy itself).

This resolves the ambiguity every prior report flagged: `web.archive.org` is not intermittently
reachable depending on luck, and the `archive.org/wayback/available` API being reachable is not
evidence the content host is too — they are different hostnames with different proxy treatment.
The yearbook/officer-page leads this would have unlocked (archived `wku.edu/sga` senate and
judicial roster pages for 2012-2024, which is exactly the era carrying most of the standing
no-portrait gap) stay closed on this route, in this container, as a policy block rather than a
network fault — worth recording so a future pass spends its one probe elsewhere rather than
retrying the same hostname on the same proxy.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `build.py` and
`check_data.py` both pass clean: 61 years, 1964 events, 60 presidents, every one portrayed. One
diagnostic fact recorded — `web.archive.org` is proxy-blocked by hostname in this container,
distinct from the `archive.org` API host, which is open — to stop a future pass re-probing the
same dead end. The standing ~155-person officer-portrait gap remains exhaustively documented as
closed or text-only rather than unsearched; nothing in today's four passes moved it. Landed on
`research-photos`.
