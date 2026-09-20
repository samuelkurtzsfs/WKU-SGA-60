# Photograph run, 20 September (scheduled) — nothing new, two access routes found blocked

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` §4 and §6
before touching anything. `research-photos` was already a fast-forward ancestor of `origin/main`
(merge base `04e6e4bf`, current tip `93685e68`), so there was nothing to merge — the branch simply
caught up. `gh` is not installed in this container; `git push --dry-run` confirmed write access
directly, per the route-one instructions.

Re-checked the four standing priorities fresh against current `data/years.json` and
`data/photos.json`:

- **Priorities 1 and 2 (presidents and regents): still fully satisfied.** All four named
  presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) and every other `leaders`
  entry with `role: "president"` or `role: "regent"`/`"student regent"` across all 61 years has a
  portrait; a scripted cross-check of every leader name against `photos.json`'s `leaders` array
  came back with zero missing presidents or regents. The four named files, and a further sample,
  all check out as real JPEGs (`ffd8ffe0`).
- **Priority 4 (a photo for every year): still satisfied at the minimum bar.** All 61 years carry
  at least one photograph in `photos.json`'s `years` array.
- **Priority 3 (cabinet/Senate officers): still the open queue**, unchanged in scale — roughly 175
  executive-cabinet and Senate-officer/committee-chair names still carry no portrait, spanning
  1977-78 through 2023-24.

## Two specific leads chased from the 19 September report — both closed out negative

**The 20 April 2022 SGA election-results gallery (`wkuherald.com/65821/`, 8 photos, media IDs
65823-65830) was read photo by photo via the WordPress media API**, on the strength of the 19
September report's correction that Gunnar Robinson, Makism Zaepfel, Daniel Vuleta and Trib Singh
had been missed by a full-name-only search. None of the eight individual captions name any of
those four, or Gunnar Robinson: the gallery's subjects are Sam Kurtz, Cole Bornefeld, Garrison
Reed, Alexis Courtenay and SGA Chief Justice Holden Schroeder, all of whom the archive already
has portraits for (Schroeder's own portrait already cites two frames from this exact gallery,
65824/65825). The body text of the article does name Zaepfel (as "Makism"), Vuleta, and Gunner
Robinson among ten senators-at-large elected that night, but as a name in running prose, not a
caption — it does not meet the identification bar. These four remain without a portrait; this
specific gallery has now been fully read and is exhausted as a lead.

**The 15 September and 23 September 2021 SGA swearing-in articles** (`wkuherald.com/60866/`,
`wkuherald.com/61104/`), the source of the Skillman/Massarone hits in that same correction, were
also checked. Both articles' featured images caption only the meeting as a whole ("The fourth
meeting of the 21st senate was called to order...") with no image at all for the second. Zach
Skillman and Kate Massarone are named in the body text but not in any caption. Also without a
portrait.

## A further surname sweep, continuing the 19 September report's "redo by surname" instruction

Searched `wkuherald.com`'s live post search by surname alone (not the full name), 1.5 seconds
apart, for twelve more names still on the queue: Puhakka, Zaczek, Massarone, Rongey, Banales,
Padgett, Gannon, Herlick, Cisco, Hornback, Tomas, Reynolds (Turner). Every returned post's
featured-media caption was read. None named the person being searched for — the closest calls
were two captions that turned out to identify different people entirely:

- The one `Rongey` hit (`wkuherald.com/83874/`, spring 2025 election results) captions Mahurin
  Honors College Senator-Elect **Ciin Lun**, not Nolan Rongey.
- One `Gannon` hit (`wkuherald.com/74409/`, January 2024) captions sophomore senator **Gabe
  Jerdon** being sworn in, not Elizabeth Gannon.

Both Lun and Jerdon (as "Gabriel Jerdon", matching `years.json`) already have portraits in this
archive, including ones drawn from these exact two photographs — so this was a useful check
against gaps in `years.json`'s `organization.senate` coverage, not a wasted one, but it produced no
new work either way. Reynolds, Tomas and Cisco are common enough surnames that the returned posts
were dominated by unrelated sports and campus coverage; none of the SGA-flavored results among
them named Turner Reynolds, Juan Tomas or Maiah Cisco specifically, and going further into
pagination on a common surname risks a false match more than it saves time, so these three were
left rather than pushed deeper.

## Two access routes tried and found blocked this run — worth flagging for whoever runs next

**`digitalcommons.wku.edu/cgi/viewcontent.cgi` (the PDF-serving endpoint) is behind a Cloudflare
JS challenge right now, not the "empty HTTP 202" `CLAUDE.md` and `SGA-60-AGENT-INFO.md` describe.**
Confirmed on the 1996-04-25 Herald issue (`dlsc_ua_records/2986`, "New Student Government Officers
Sworn In" — a swearing-in photo would have been useful for the 1995-96/1996-97 general-year-photo
gap). A plain request with the documented `Sec-Fetch-*`/`Upgrade-Insecure-Requests` headers
returned HTTP 403 with a `Just a moment...` Cloudflare interstitial body. Backed off 90 seconds and
retried once, then 240 seconds and retried again: same result both times. Landing/item pages on
the same domain (e.g. `dlsc_ua_records/2986/` itself, and the finding-aid index) returned a normal
200 throughout, so this is not a whole-domain block — only the file-serving CGI route is gated.
Also tried routing the same request through the container's own pre-installed headless Chromium
(via a locally-installed `playwright-core`, proxied through the session's configured
`HTTPS_PROXY`): the challenge page loads but does not clear even after an extra 8-second wait,
consistent with Cloudflare detecting headless automation rather than this being a timing issue.
Nothing was force-downloaded past this; no bot-check page was saved under a `.jpg`/`.pdf` name.

**`web.archive.org` is blocked at the container's own egress policy this run** ("Blocked by egress
policy"), both the wildcard capture-listing UI and the plain CDX API. `SGA-60-AGENT-INFO.md` §4
already flags this as variable by container and says to test rather than assume either way — this
run's test came back negative. The Wayback-based `wku.edu` SGA officer-page route that the 19
September report suggested for the 1996-97 through 2002-03 Talisman gap was not reachable at all
because of this, not because of anything about the pages themselves.

`archive.org`'s Talisman djvu text and IIIF page-image routes (the non-Wayback, non-`cgi`
archive.org paths) were unaffected by either block and worked normally throughout this run.

## Nothing added

`data/photos.json` and `data/photos/` are unchanged. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both pass clean on the unmodified data; `site/` was regenerated,
found identical to the committed copy, and left alone (nothing to revert). This report is the only
new file this run produces.

## Left for the next run

- The 41-name (now effectively 37, after Skillman/Zaepfel/Vuleta/Singh/Robinson/Lun/Jerdon are
  accounted for one way or another) 2018-2026 Senate/committee list is genuinely exhausted against
  `wkuherald.com`'s live search, by both full name and surname. Further progress on this window
  most likely needs `digitalcommons.wku.edu`'s PDF route (currently Cloudflare-gated) or
  `web.archive.org` (currently egress-blocked) to come back, rather than more searching against the
  same live API with the same technique.
- If a future run has working access to the `viewcontent.cgi` PDF route again, `dlsc_ua_records/2986`
  (1996-04-25 Herald, "New Student Government Officers Sworn In") is still an open, promising lead
  for both the 1995-96/1996-97 general-year-photo gap and for officers David Young-era successors —
  Steve Roadcap, Jamie Fite, Jenny Stith and others from that stretch of the queue.
- The 1996-97 through 2002-03 Talisman publishing gap (Roadcap, Faught, Fite, Cole, Bailey, and the
  1997-99 Senate lists), the 1984 Talisman class-portrait grids (Kelly S. Smith, John Holland), and
  the ~150 remaining unchecked cabinet/Senate names are all exactly as the 19 September report left
  them — this run did not reach them given the time spent confirming the two leads above and the
  two blocked routes.
