# Profile-writing run, 24 August 2026 (scheduled)

## What this run found

The standing prompt for this routine still frames the job around a stale count
("806 people, 73 profiled"). The real count on `research-profiles` at the start
of this run was already 773 profile records (per-office; more than one office
per person is why it beats the 806 name count) covering every one of the
archive's 73 leader (president/regent) records, and effectively every named
executive-cabinet and Senate officer.

A full audit before writing anything, done in this order:

1. Every `leaders` entry (president/regent): 0 without a `profile`.
2. Every `organization.executive` and `organization.senate.officers` entry
   without a `profile`, name not already in `.research/profiles-done.txt`,
   excluding the year's own duplicate "President" listing (which merges onto
   the leader's page automatically since `build.py` keys pages by exact name
   string): 13 unique names. Checked every one against the full `leaders`
   list — **all 13 already carry a profile under a later year, as the
   president they eventually became** (Kevin Smiley, Jay Todd Richey, Andi
   Dahmer, Stephen Mayer, Will Harris, Garrett Edmonds, Cole Bornefeld, Sam
   Kurtz, Rush Robinson, Caden Lucas, plus Sandra Norfleet, William Menser and
   Bill Straeffer as regents/early presidents). None of the 13 is a genuine
   gap.
3. Re-ran the same check without excluding "President"-office duplicates, to
   catch cases where the executive-tier record and the leader record use
   *different spellings* of the same person's name and so would not merge
   automatically. This caught one real case: **Tara Higdon** (Administrative
   Vice President, 1994-95, and President, 1995-96, in `organization.executive`)
   never linked to her leader record, filed as **Tara (Higdon) Howard** for the
   same 1995-96 term. The leader entry's own note already documents the
   connection ("the 1994-95 organization record independently names her as
   that year's Administrative Vice President, noting she would succeed Evans
   as president and student regent the following year"), so this was a data
   bug, not new research: her 1994-95 and 1995-96 executive terms were on a
   separate, profile-less page from her real, fully profiled leader page.
   Fixed by adding `"Tara Higdon": "Tara (Higdon) Howard"` to
   `data/name-aliases.json`. Checked every other `leaders` entry for the same
   parenthetical-name pattern (the archive's convention for a maiden/former
   name) — she is the only one. Rebuilt and confirmed: `site/o/tara-higdon.html`
   no longer exists; both her terms now render on `site/o/tara-higdon-howard.html`
   alongside her profile.

**Conclusion: there are no remaining un-profiled people in the leader,
executive-cabinet, or Senate-officer tiers.** That is the entire scope this
routine's standing prompt asks it to work through (tiers 1-4 of its priority
order). Tier 5, "everyone else," is `organization.senate.members` — 1,468
rank-and-file entries, 1,396 without a `profile`.

## Why tier 5 is not a place to write profiles yet

Checked `scripts/build.py`'s `officer_index()` (~line 6533) directly. For
`organization.executive` and `organization.senate.officers` entries, the
per-term dict it builds copies `profile`, `photo`, and the numbered `src2`..
fields straight off the source object. For `organization.senate.members`
entries it does not: it builds a fresh dict with only `name`, `office` (from
`seat`), `note`, and `src` (lines ~6542-6545), so a `profile` field written on
a member record is silently dropped before it ever reaches the render step.
This matches, and confirms with a direct code read, the concern already
recorded in `SGA-60-AGENT-INFO.md` §8.3 item 5 ("build.py drops `profile` and
`src2`..`src20` when it builds a member's page"). Writing profiles onto member
records right now would be real research work that never appears on the
published site. That is a `scripts/build.py` fix, outside this routine's
"edit `data/` only" scope — flagging it for whoever next touches `build.py`,
not attempting it here.

Beyond the code gap, most of the 1,396 thin member records are a single
roll-call or committee-vote mention with no further material in
`herald-index-full.json` (spot-checked a contiguous sample, 1966-67 through
1968-69, the founding Congress) — genuinely too thin for the kind of
"how they got in, what they did, how it ended" narrative this project's
`profile` field is meant to hold. A few names in that sample (Doug Alexander,
Paul Gerard, Phil Myers, Kent Gildersleeve) turned out to have real further
Herald coverage; Doug Alexander's case (elected Associated Students vice
president for 1970-71, beating Steve Tichenor) already has a full profile
under his executive-officer record for that later year, so no work was
needed there. The others were not written up, since doing so would be a
`organization.senate.members` profile and be dropped by the bug above.

## What this run changed

- `data/name-aliases.json`: added the Tara Higdon / Tara (Higdon) Howard
  alias, described above.
- No new `profile` content — there was no genuine gap left to fill within
  the tiers this routine is scoped to.
- `.research/profiles-done.txt` unchanged; nothing new to append.

Ran `python3 scripts/build.py`, `python3 scripts/check_data.py` (clean, "the
archive checks out against its own rules") and `python3
scripts/check_duplicates.py` (the same six known pairs as before, unchanged)
before landing.

## For whoever reads this next

The standing prompt for this routine should be updated (or the routine
retired) — it is now asking for work that does not exist under the current
data. If new officers get added to `organization.executive` or
`organization.senate.officers` in a future research pass, run the same
13-candidate cross-check against `leaders` before assuming they need a fresh
profile; a fair number of officers went on to be president and already have
one. If the `build.py` member-profile bug above gets fixed, tier 5 (Senate
members) is where the next real batch of profile-writing work is.
