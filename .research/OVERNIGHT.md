# SGA 60 overnight pipeline — runbook

Repo: /Users/samkurtz/Downloads/sga60. Editor rule: publish only what verification
supports; prune anything a verdict rejects. Never leave findings unmerged if they
passed. Push to main publishes the live site.

## Each wave, in order

1. `git pull` (cloud agents may have merged work).

2. **Cloud check**: `git ls-remote --heads origin` and `~/bin/gh pr list --repo
   samuelkurtzsfs/WKU-SGA-60 --state open`. For each research PR with new commits:
   fetch the branch, diff against main, spot-verify new claims by opening their
   cited source URLs (respect the digitalcommons pacing rule in CLAUDE.md), delete
   anything unsupported, run `python3 scripts/build.py`, merge the PR, comment
   what was verified and cut.

3. **Resume the local workflows from cache** (finished agents replay free; only
   failed/missing ones run):
   - Modern (mostly missing fact-checks):
     Workflow scriptPath
     `/Users/samkurtz/.claude/projects/-Users-samkurtz-Downloads-sga60/d305ae30-4294-46a3-abb0-409743beff17/workflows/scripts/sga60-year-sweep-wf_0d1c308a-3f3.js`
     resumeFromRunId `wf_2cd5c72a-c1c`, args = the JSON object in
     `.research/modern-args.json` (pass the parsed object, not a string).
   - Pre-2000 (research batches 2-4 and all verifies still outstanding):
     Workflow scriptPath
     `/Users/samkurtz/.claude/projects/-Users-samkurtz-Downloads-sga60/d305ae30-4294-46a3-abb0-409743beff17/workflows/scripts/sga60-pre2000-sweep-wf_ad3dd308-d04.js`
     resumeFromRunId `wf_ad3dd308-d04`, args = the object in
     `.research/pre2000-args.json`.
   Stop a stale still-running handle first with TaskStop if resume complains.

4. **When workflows land**: `python3 scripts/merge_research.py` (reads both
   journals, merges supported material, prunes rejected items), then
   `python3 scripts/build.py`, commit with a message naming the years, push.

5. **Spend-limit failures** ("monthly spend limit" / "usage limit" in agent
   errors): stop launching agents, merge and publish whatever verified material
   already exists, and stand down until the next scheduled wave.

## Standing facts
- 7 cloud research routines + 1 legislation harvester fire hourly at :51 on
  their own; they need no launching, only their PRs need editing and merging.
- The 4 modern years still awaiting fact-check: 2005-06, 2007-08, 2009-10
  (2008-09's verdict landed and was applied).
- Photos merge via data/photos.json; legislation via data/legislation.json.
- Rotate the GH_TOKEN environment secret once cloud pushes are confirmed working.
