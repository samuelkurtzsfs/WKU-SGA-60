# Photograph run, 8 October (evening)

Reconfirmed the baseline by script before touching anything: all 73 `leaders` records carry a
portrait, including the four people this routine's brief still names (Nick Todd, Katie Dawson,
Jeanne Johnson, Reagan Gilley). `scripts/portrait_gap.py` reports 189 officer slots with no
portrait across 159 people, 157 of them with no portrait in any year — unchanged from the
afternoon run. The two year-photo gaps, 1994-95 and 2000-01, are also unchanged.

`research-photos` was already level with `main` (the afternoon run had fast-forwarded it); merged
`origin/main` again at the top of this session, which was a no-op.

## This session's access picture

- **`cgi/viewcontent.cgi` answered the Cloudflare "Just a moment..." 403 challenge** on every
  attempt, as it has for weeks. Worth noting separately this time: the **plain digitalcommons
  listing and collection pages are not behind the same wall** — `digitalcommons.wku.edu/sga/`
  and `digitalcommons.wku.edu/dlsc_ua_records/` both returned normal HTTP 200 pages. Only the PDF
  endpoint itself is challenged. That doesn't open a new route to an actual image (the item and
  listing pages carry no usable photographs, only metadata), but it's worth the next run knowing
  the two are not the same gate.
- **`web.archive.org` was closed all session**: a plain CDX query came back HTTP 403 once, then a
  retry timed out, then a second retry reset mid-exchange (`ws_closed_mid_exchange` at the proxy).
  Consistent with the intermittency this file has logged for weeks — not treated as a standing
  state, just not open tonight.
- **`archive.org` downloads (djvu text and single-page JPEGs) worked cleanly throughout**, as
  always — confirmed again by re-pulling a Talisman page image that had already been read.
- **`wkuherald.com`, including its WP-JSON API, was open and fast all session.**

## New this session: a wkuherald sweep of 30 officer-gap names

Rather than re-open the eight archive.org-era names (Pulman, Bass, Young, Wicks, Wilson,
Chesnut, Millay, Austin) — all eight were re-confirmed exhausted by the 7 October runs, Bass's
crop specifically withdrawn by the editor on 8 October for being unconfirmable, and nothing in
this session's access picture changes any of that — this run tried a route not logged as
systematically exhausted before: querying `wkuherald.com`'s `wp-json/wp/v2/posts` search
endpoint directly, with `_embed=1` to pull each hit's figures, and scanning every post's embedded
`<figure>`/`<figcaption>` pairs for the candidate's full name.

30 names were checked this way, spanning 2004-05 through 2021-22 and covering Chief Justice,
Speaker of the Senate, and director/committee-chair slots (the full list is in
`batch1.json`/`batch2.json`, not checked into the repo — it was scratch input, not a finding):
Nathan Cherry, Ryan Richardson, David Spalding, Stuart Kenderes, Art Scisney, Christopher
Jankowski, Kara Raley, Amber Daniel, Cody Cox, Erika Puhakka, Matt Holland, Mark Henry, Jenna
Haugen, Josh Fries, Liz Goddard, Mark Clark, Josh Zaczek, Cassidy Townsend, Brenna Mathews,
Tribhuwan Singh, Zachary Skillman, Elizabeth DeLozier, Turner Reynolds, Jillian Kenney, Hope
Wells, Helen Vickrey, Morgan Wysong, Sawyer Coffey, Rachel Keightley, Mallory Treece.

**Zero produced an individually-captioned photograph.** The one near-hit, during a spot check of
Justin Goins (Chief Justice, 2022-23, checked individually rather than in the 30-name batch): the
Herald's 17 Feb 2023 censure-hearing story (`wkuherald.com/70591/...`) carries three photographs,
one captioned as a group ("Judicial Council members view an Instagram post...", no names, no
left-to-right key — not usable, same rule as the withdrawn Bass crop) and two individually
captioned, but naming Speaker of the Senate Julie Mishchuk, not Goins. Mishchuk already carries a
portrait in `data/photos.json` (confirmed before writing this), so that is not a new find either
— it is why Goins' own search came up empty: the only solo-captioned face in his best-looking
lead belongs to someone else.

This is consistent with what the rest of this file already says about the shape of the gap: these
are Judicial Council justices, committee chairs and office staff, not candidates running in a
contested, photographed election. The Herald photographs the people giving quotes and standing at
podiums, which for routine SGA meeting coverage is usually the president, the Speaker or whoever
is contesting a motion — not a committee chair sitting in the gallery. The 157-people-with-no-
portrait-anywhere figure is not evenly distributed across roles; it is concentrated exactly where
a general-interest student newspaper has the least reason to single someone out for a caption.

## Nothing landed

No file in `data/photos.json` or `data/photos/` changed. `build.py` and `check_data.py` both
pass clean. This run's only change is this note; nothing in `SGA-60-AGENT-INFO.md` needed
correcting. Landed on `research-photos`.

## For the next run

- The wkuherald WP-JSON sweep is a real, repeatable method (`_embed=1`, scan figures for the
  candidate's full name in the caption) but has now been tried against 31 names (30 here plus
  Goins) with one near-hit and zero new portraits. It is not yet exhausted — only ~20% of the
  150-plus post-2003 gap list has been checked this way — but the hit rate so far suggests it
  will keep finding other people's captions before it finds the named candidate's, since minor
  officer roles are rarely the one quoted or photographed. Worth continuing in future runs, with
  expectations set accordingly, rather than treating one empty batch as proof there is nothing
  there.
- `cgi/viewcontent.cgi` and `web.archive.org` are both worth retrying cold at the top of the next
  run regardless of tonight's result — both have opened unpredictably between sessions for weeks
  and neither failure here should be read as a standing state.
- The eight archive.org-era names (Pulman, Bass, Young, Wicks, Wilson, Chesnut, Millay, Austin)
  do not need another look without a genuinely new lead; all eight are exhaustively documented in
  the 7-8 October notes in this file.
