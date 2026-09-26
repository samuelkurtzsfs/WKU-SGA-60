# Photograph run, 26 September (scheduled): a near-duplicate caught, two access checks re-confirmed blocked

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4 and 6.
`research-photos` was behind `origin/main` by several commits; merged main in cleanly except for one
conflict in this file's own directory (`.research/NIGHT-REPORT.md`, an append-only log — resolved by
keeping both sides' additions in date order, nothing dropped). No pull request was open on this
branch or any other; the prior rolling PR had already been merged (most recently #601-#604, all
editor passes, none photograph work).

Re-checked the four originally-named presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan
Gilley) before anything else, as every prior run has: all four still carry a portrait. Went further
and checked programmatically rather than by name: **0 of the 73 leader records (every president and
every student regent) lack a portrait.** Priorities 1 and 2 from the task brief are both fully done
and have been for some time.

## Two long-blocked access routes, tested again and still blocked this session

- **`digitalcommons.wku.edu/cgi/viewcontent.cgi`**, tested directly with the recommended browser
  navigation headers against article 9903 (the standing 2000-01 year-photograph lead): `HTTP/2 403`,
  `cf-mitigated: challenge`, a Cloudflare interactive-challenge page, not a plain rate limit. Same
  result every prior run has logged for months.
- **The `web.archive.org` mirror bypass** that worked for the 25 September evening run failed this
  session on both protocols: plain `http://web.archive.org/` returned `403` from this container's own
  egress proxy with `x-block-reason: hostname_blocked` (a policy denial, not to be retried per
  `/root/.ccr/README.md`), and `https://` to the same host reset the connection after ~11 seconds on
  three separate attempts, 5 seconds apart (`recentRelayFailures` on the proxy status endpoint records
  it as `ws_closed_mid_exchange` against `web.archive.org:443`). This matches `SGA-60-AGENT-INFO.md`'s
  own caveat that this route "may vary by container" — it is closed in this one. Confirmed the item
  landing page (not the PDF endpoint) loads fine over plain HTTPS regardless (`dlsc_ua_records/8919`,
  200 OK), so only the download path is blocked, not the domain generally.

Net effect: the four-year year-photograph gap (1994-95, 1995-96, 2000-01, 2008-09) is untouched this
run. 1994-95 and 1995-96 were already ruled out on other grounds (no Talisman was published either
year; the four "Xposure" mini-yearbooks that stood in for it were confirmed by full abstract to carry
no organizational content). 2000-01 and 2008-09 still have Herald leads on file (articles 9903 and
7740) that neither access route above could reach this session.

## Officer portraits searched, priority 3

Worked outward from the missing-officer list (216 executive/senate records across every year still
lack a portrait; computed directly against `photos.json`, not estimated) into the most recent decade
first, on the theory that wkuherald.com coverage is thickest there. Searched, via wkuherald.com and
WKU-adjacent web results: Erika Puhakka, Turner Reynolds, Brenna Mathews, Tribhuwan Singh, Livi Ray,
Elizabeth Gannon, Miles Harvey, Zoe Martin, Nolan Rongey, Carter Smith. Every one of these was already
on record as searched-and-not-found in earlier PRs (#353, #426, #449, #461, #597); this run's searches
independently reached the same articles and the same conclusion — group photos or no photo at all,
nothing that individually captions the person. Confirmed rather than assumed: opened the specific
articles (SGA swearing-in and election-result stories most likely to carry individual headshots) and
read every caption on the page. None of the ten is a new dead end; all were already closed.

One genuine near-miss, caught before it became a mistake. A Herald story on the SGA Judicial Council's
February 2023 censure hearing of President Bornefeld captions a photograph "Speaker of the Senate
Julie Mischuck" — a real, individually-identified officer photograph, for **Julie Mishchuk** (both of
the story's photograph captions spell the surname "Mischuck", where its own body text spells it
"Mishchuk" throughout, as SGA's Senate minutes do; the two spellings run to eight letters each, so
they differ in the letters and not in the length; the archive already follows the minutes' spelling).
This looked like a new find until
`check_data.py`-equivalent duplicate checking (the build's own consistency check) caught it: **this
exact photograph, same article, same crop rationale, was already added to `photos.json` earlier the
same day** (line ~10823, crediting the identical source with a note about the caption's spelling
already on file). The 39,524-byte file already in `data/photos/2022-23-julie-mishchuk.jpg` was
independently confirmed and briefly, accidentally overwritten with a 95,014-byte re-crop of the same
photo during this run; caught by `git status` before committing and reverted with `git checkout --`
on both the `data/` file and the `site/` copy `build.py` had regenerated from it. No duplicate landed;
no file was net-changed. Worth recording so no future run mistakes this closed case for an open one
purely because a stale search index (this one included) hasn't caught up to the same-day merge yet.

## What is not open any more, checked directly rather than assumed

Every executive and senate officer for 2025-26 and 2026-27 already carries a portrait except five:
Miles Harvey, Zoe Martin, Tyreesha Morris, Nolan Rongey and Carter Smith, all senators-at-large or
freshman senators elected in the most recent two cycles. All five were searched this run (see above)
and none has an individually captioned photograph on wkuherald.com yet — plausible, since freshman
senators rarely get individual coverage until they chair something or run for a higher office. Not
closed as a dead end, just not yet found; a future run should re-check these five once they have had
another semester to appear in a headline of their own, rather than re-searching the many already-closed
names above.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both run clean on the merged branch
(61 years, 73 leader records, 0 without a portrait, 70 year-level photograph entries, the one
pre-existing `_do-not-use.json` withdrawal noted by the build as routine and unrelated to this run).
No `data/` file differs from what `research-photos` already held before this run's merge from `main`.

## For the next run

- The two blocked routes above are worth a fresh one-shot test each time a run starts, cheaply, before
  assuming either is open — both have flipped open and shut across different container instances
  within the same week.
- The five 2025-26/2026-27 senators named above are the only current-year gap; nothing else in the
  organization tables for those two years is missing a portrait.
- Nothing else in the four-year year-photograph gap or the wider 216-record officer gap changed hands
  this run. Both remain exactly where the 25 September reports left them.
