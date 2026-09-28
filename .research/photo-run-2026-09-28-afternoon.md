# Photograph run, 28 September (afternoon): six TopSCHOLAR-wanted articles retrieved via the
web.archive.org bypass and read in full; all close negative

## Starting state

Read `CLAUDE.md`'s Pictures section, `AGENT-LANDING.md` and `SGA-60-AGENT-INFO.md` sections 4
and 6. A scheduled run earlier today (`a9649d53`/`33aa0255`, merged to `main` as `6816a852`)
already reconfirmed priorities 1 and 2 fully done and the 8-name archive.org-Talisman officer gap
exhausted, so this run checked out `research-photos` fresh from `origin/research-photos` and
merged `origin/main` forward (clean, no conflicts) rather than repeat that work.

Independently reconfirmed the baseline: all 73 `leaders` records carry a portrait, all four named
presidents (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley) among them; every president and
student regent in `data/years.json` resolves to a portrait; 33 executive and 184 senate-officer
records still lack one. `python3 scripts/merge_photo_finds.py` (dry run) agrees: 0 to add, 0 to
replace, the same 18 standing refusals.

## digitalcommons.wku.edu remains blocked; the web.archive.org id_ bypass worked today

`viewcontent.cgi` still returns Cloudflare's interactive challenge (HTTP 403) on a direct request,
full browser headers included - unchanged from every recent entry in this file. The
`web.archive.org/web/<timestamp>id_/<viewcontent.cgi URL>` bypass documented in `_brief.md` and
used successfully on 19 and 25 September worked again today, though the Internet Archive itself
was visibly unstable throughout the session: the CDX API returned a genuine site-wide
"Temporarily Offline" page on several attempts and the proxy logged repeated
`ws_closed_mid_exchange` resets on the PDF fetches themselves. Every article eventually came
through whole on a retry a few seconds later; none needed more than two attempts.

**Confirmed again: the landing-page URL number (`dlsc_ua_records/<N>`) and the `viewcontent.cgi`
article id are different numbering systems.** Resolved the real article id for six wanted items by
fetching each landing page directly over plain HTTPS (this always works; only `viewcontent.cgi`
itself is blocked) and reading its own `viewcontent.cgi?article=` link out of the HTML, rather than
guessing the landing-page number is the same value.

## Six wanted articles retrieved and read in full; all close as dead ends

Working from `data/photo-finds/_topscholar-wanted.json`, six not-yet-attempted entries were
resolved and fetched (mapping: 3695->article 4692, 9223->10212, 9224->10211, 6720->7725,
6238->7243; the seventh CDX lookup, for 5160/6164, again returned the same 356 MB capture logged
as impractical on 25 September and was not re-attempted). Notes added to each entry in
`_topscholar-wanted.json`; summary:

- **3695/4692** (Herald 81:39, 4 Apr 2006) - wanted for the 2006-07 senate cohort (Bishop, Humble,
  Holland, Eaton, Hill). Its only SGA content is the presidential/administrative-VP debate story,
  with a captioned photograph of Ratliff, Watkins and Allen - all three already on file. No
  senate-candidate grid anywhere in the 15-page issue (checked visually, not just by text search,
  since the OCR layer is badly garbled). None of the five wanted names appear.
- **6720/7725** (Herald 84:33, 19 Feb 2009) - wanted for Corey Bewley. The full story of his
  nomination as chief justice is there and reads exactly as expected, but the page carries no
  photograph at all.
- **6238/7243** (Herald 85:20, 17 Nov 2009) - wanted for Timothy Gilliam. "Western students work
  for politicians" names and quotes him as expected; it is a pure text feature, no photograph
  anywhere on the page.
- **9223/10212** and **9224/10211** (Herald 78:46 and 78:47, 18 and 20 March 2003) - wanted for
  Kelly Johnson, Brooke Smith, Kristin Hartley (both issues) and Stacey Adkisson, Natalie Croney
  (9223 only; both already covered elsewhere). 10211's "SGA Candidates" series individually
  captions Jessica Martin, Shawn Peavie, Nick Todd and Abby Lovan - all four already on file - and
  names none of the three wanted. 10212 (11 pages, almost no text layer, read entirely as rendered
  images) carries two more candidate profiles with captioned photographs, "Johnson supports
  one-stop billing" and "Lockhart wants comfortable atmosphere" - but the Johnson pictured is
  **Patti Johnson**, running for 2003-04 executive vice president, not Kelly Johnson; Patti Johnson
  already has a portrait in `photos.json` (Herald 80:5, 9 Sept 2004, carried back to 2003-04), so
  this is independent corroboration, not a new find. Dana Lockhart is not a name this archive is
  missing. Neither issue names Kelly Johnson, Brooke Smith or Kristin Hartley anywhere. Both halves
  of the spring 2003 election coverage this pair of entries pointed at are now exhausted for those
  three names.

No new portrait or year-scene photograph resulted from any of the six. All six are marked closed
in `_topscholar-wanted.json` with the article id, what was actually on the page, and why it does
not serve the wanted name, so a future run does not refetch them.

## Checks

`python3 scripts/build.py` and `python3 scripts/check_data.py` both ran clean (61 years, 60
presidents, all portrayed; 1,968 events; the archive checks out against its own rules).
`data/photos.json` and `data/photos/` are unchanged this run; only `_topscholar-wanted.json` and
this file changed.

## For the next run

- Priorities 1 and 2 remain fully done.
- Six more `_topscholar-wanted.json` entries are now closed with the actual page content recorded.
  Two remain genuinely open: `5160` (Mallory Treece, blocked by a 356 MB capture, impractical in
  this container) and `8633` (Katherine Smith, a common-name lead never yet attempted) and the two
  large Talisman-spread entries (`talisman/` x2, for 2014-15 and 2016-17 cohorts) — not touched
  this run.
- Kelly Johnson, Brooke Smith and Kristin Hartley (spring 2003) have no photograph in either
  Herald issue this project ever proposed for them. If a face exists for any of the three, it is in
  an issue neither entry anticipated - worth a fresh TopSCHOLAR index search rather than refetching
  9223/9224.
- The web.archive.org id_ bypass is intermittently reachable again; retry rather than assume it is
  closed, but expect to need one or two retries per fetch while archive.org's own infrastructure is
  unstable.
