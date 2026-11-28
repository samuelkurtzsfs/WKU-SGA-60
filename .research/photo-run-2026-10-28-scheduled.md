# Photograph run, 28 October (scheduled): four more pre-2001 officer-gap names checked at specific pages via a more reliable archive.org image route, no new portrait, two genuinely new negatives on record

## Priorities 1, 2 and 4, reconfirmed directly against the file before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait in `data/photos.json`. Unchanged — this trigger's stored brief is still the frozen one
  naming them as portraitless, and it still isn't true; see every run since 20 August.
- **Priority 2**: `python3 scripts/check_data.py` reports 61 years, 60 people have been president;
  every leader in `data/years.json` has a matching `data/photos.json` entry. No gap.
- **Priority 4**: every year still carries at least one photograph. The two standing near-misses
  (1994-95, 2000-01) were not reopened this pass — both already have several specific issues read
  with no usable frame, per the 7-8 October notes.
- **Priority 3** (officer/Senate gap): `python3 scripts/portrait_gap.py --any-year` reports 948
  officer slots, 188 with no portrait for that person in that year, 158 people, 156 with no
  portrait anywhere — unchanged from every pass this week.

## Network state, retested fresh

`digitalcommons.wku.edu/cgi/viewcontent.cgi`: still a Cloudflare 403 challenge, tested directly
with the navigation headers CLAUDE.md specifies. `web.archive.org`: still `curl: (35) Recv failure:
Connection reset by peer` on every plain request. Both unchanged from every pass logged this month.

`archive.org` itself is open, as it has been throughout, but this pass found that the standard
download redirect chain (`archive.org/download/<id>/<id>_djvu.txt`) needs `-L` followed all the way
through to a `dn*.ca.archive.org` or `dn*.eu.archive.org` edge — a bare `curl -o` without `-L`
silently writes an empty file from the 302 body, which could misread as "nothing there" rather
than "redirect not followed." Noting it because it would waste a future pass's time.

## A more reliable way to pull a specific Talisman page image, found this pass

Earlier passes have used `iiif.archive.org/iiif/<id>$<leaf>/full/pct:50/0/default.jpg` to render a
half-scale page. This pass found that specific leaf numbers can time out or 502/504 repeatedly at
that scale while the **same leaf at full resolution** (`full/full/0/default.jpg`, 3-4 MB rather than
400-600 KB) answers cleanly on the first or second try. Both sizes come from the same underlying
tile service, so the failure looks like a scale-dependent hiccup, not a dead leaf; worth trying
`full/full` first on a 502/504/timeout before concluding a leaf is unreachable.

Also used this pass, and worth recording for whoever next works a name against the Talisman:
`archive.org/metadata/<id>` returns `server` and `dir`, which construct a direct full-text search
hit: `https://<server>/fulltext/inside.php?item_id=<id>&doc=<id>&path=<dir>&q="<phrase>"`. This
returns the exact 1-indexed scan leaf and word-box coordinates for a phrase, which is faster and
far more precise than downloading the whole `_djvu.txt` and grepping it blind — especially useful
because the leaf-to-printed-page offset is **not constant through a volume** (this book ran -2 in
one section and -4 in another, apparently around unnumbered section-divider spreads), so the only
reliable way to find a page is to search for it, not to guess an offset.

## Four more pre-2001 officer-gap names, each checked at a specific, located page

- **David Young, Administrative Vice President 1978-79** (the one name on the gap list from a
  Talisman year not yet individually checked this way). Found on 1979 Talisman p. 289
  (`talisman1979west$291`, in the "Making news about entertainment" ASG wrap-up): "David Young,
  administrative vice president, said this was done to 'force some heads-up competition' between
  candidates," on the new ASG congress election structure. This is a direct, named quote confirming
  his office and year, matching the existing record exactly — but it is running text, not a photo
  caption, and the facing spread (pp. 288-289, the volume's whole ASG section this year) carries no
  photograph captioned with his name. No portrait exists to find at this location.
- **Mark Chesnut, Treasurer 1980-81**. The volume's own index carries exactly one page for him,
  "Chesnut, Mark Cameron 234," distinct from the senior-portraits entry for "Chesnut, William George
  II 371." Page 234 (`talisman1981west$238`) turned out to be the intramural champions list, not a
  photograph: "Mark Chestnut (Sigma Alpha Epsilon)" won men's Badminton (singles) and, with Mitch
  Gum, Racquetball (doubles) for Sigma Alpha Epsilon. A real, specific fact (confirms his fraternity
  and that this is the right Mark Chesnut, a different spelling of the surname than the ASG record
  uses), but a results list, not an image — no face to crop. The volume's own ASG group photograph,
  p. 282, was already checked exhaustively by an earlier pass (every one of its ~26 captioned
  figures already has a portrait in `data/photos.json`); Chesnut is not among the names in that
  caption, so he was never in this photograph to begin with.
- **Chris Millay and Dwight Austin, Parliamentarian and Sergeant-at-Arms 1986-87**. Full-text search
  of the 1987 Talisman for "Millay" and "Dwight" returns zero matches for either person anywhere in
  the volume — only a same-surname sophomore (Lori Ann Millay, Beth Ann Millay, unrelated) and a
  same-first-name senior (Dwight Scott, unrelated). This is a stronger negative than "no photograph
  found": neither person is named anywhere in this yearbook's text layer at all, index included.
- **Vern Pulman, Representative-at-Large 1974-75**. Full-text search of the 1975 Talisman for
  "Pulman" returns zero matches; a search for "Vern" alone turns up only a same-middle-name index
  entry (Kenneth Vern Anderson). Same conclusion as Millay/Austin: not named anywhere in this
  volume.

All four results are consistent with the project's long-standing finding that the officer gap below
president/regent level is covered by Talisman group photographs when the person appears in one, and
not at all when they don't — committee-chair and single-term officer names that never made a
captioned photograph are not recoverable from this source, whatever page the index sends you to.

## Conclusion

No new portrait landed this pass. Both standing network blocks (`viewcontent.cgi`, `web.archive.org`)
are confirmed still closed by direct test, unchanged from every pass this month. Four more
pre-2001 officer-gap names were checked at the specific pages the volumes' own indexes or
full-text search pointed to, rather than by a blind per-name sweep; two (Young, Chesnut) turned up
real text confirming the existing record but no photograph, and two (Millay, Austin, plus Pulman in
a different year) are not in their volume at all. `python3 scripts/build.py` and
`python3 scripts/check_data.py` both exit clean; `site/`'s build-date-only diff was reverted.
`data/photos.json` and `data/photos/` are unchanged from `origin/research-photos`. No push
notification sent: the blocked-route state was already reported to the owner on 23 October and
nothing has changed since, and no new portrait was found to report. Landed on `research-photos`.
