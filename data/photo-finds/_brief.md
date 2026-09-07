# The portrait hunt: how this is done

Everyone recorded in office in this archive should have a face. This is the
standing brief for that work, reconstructed after the original was lost with
`/tmp`. It lives in the repository now, because a brief that only exists in a
temporary directory is one reboot from being nobody's knowledge.

Read this, then read `_archive-gaps.json`. That file is the accumulated result
of the runs so far — what has been tried, what is closed, and which routes are
dead. It is longer than this brief and more valuable.

## The rules that do not bend

**Identification is absolute.** Never put a name on a face you cannot prove is
that person. A caption, a class-grid label, a numbered key or a printed
nameplate proves it; a resemblance, a surname and a plausible year do not. A
wrong face is worse than no face, because a reader has no way of knowing.

When you can prove the *face* but not the *person* — the grid position is
certain but nothing ties that man to this office — do not discard the work and
do not guess. Put this in the entry:

    "identification": "FACE PROVED, PERSON NOT PROVED - FOR THE EDITOR"

and write out what you established and what you could not. The merge refuses
those automatically and routes them to the editor with your reasoning intact.
Several people have been kept off the site that way and each time it was right.

**WKU sources only.** The College Heights Herald, the Talisman, TopSCHOLAR,
wku.edu. Not LinkedIn, not employer pages, not social profiles, not obituaries,
not Ancestry, not newspapers.com. This holds for recent students especially,
where the temptation is greatest because they are the easiest to find. The
owner ruled on this explicitly.

**The quality floor is low.** A soft, small or cropped face beats an empty
frame. Mark it `"quality": "soft"` / `"small"` / `"group crop"` and the merge
adds a short note to the citation. Do not discard a usable face for being
imperfect; do discard one you cannot identify.

**No source, no entry.** Every finding needs `src` with a label and a URL.

## The two directories

- `data/photos/` is what the site serves. Your finished crop goes here, and the
  `file` field in your findings must name a file that exists here.
- `~/Desktop/SGA60 photo hunt/` is for bulky working material only — whole
  yearbook pages, PDFs, scratch. Ten good portraits were once filed into it by
  mistake and refused on every run until somebody moved them by hand.

Use your own scratch directory under `/tmp/hunt-<block>/`. Agents sharing one
path have overwritten each other's helper scripts.

## Write after every single person

Not in batches, not at the end. The machine sleeps, a watchdog kills agents
after ten minutes of no progress, and the account's spend limit has cut runs
off mid-sentence. Whole fleets have died and only what was already on disk
survived. One agent's twelve finds survived a stall for exactly this reason.

## Filter before you cut

If you are given an officers list, load it into a set at the start and check
every candidate against it before cutting. A volume-wide sweep lands on
whoever it happens to hit; two agents drifted onto rank-and-file senators
without noticing, and the one that filtered had all twelve of its finds land
where they were wanted.

## A documented dead end is worth as much as a find

Write into `<block>-notes.json` every person you could not find and why: which
volumes and issues you checked, whether they appear in text but never in a
photograph, whether a frame exists that cannot be identified. There are now 327
such reasons on file across nine blocks, and they are what turns "nobody has
looked" into "this person is not there".

The same applies to whole sources. Establishing that the People Poll did not
exist before 1993, or that the Xposure magazines hold no portraits, saved four
agents from being sent after them. When you close a source, say so in
`_archive-gaps.json` so the next run does not reopen it.

## What has been learned about the sources

Read `_archive-gaps.json` for the full list. The essentials:

- **The Wayback route into TopSCHOLAR.** Its `/cgi/viewcontent.cgi` returns 403
  to every script and to headless Chrome; the block is on the TLS fingerprint.
  The Internet Archive mirrors the same PDFs and serves them to plain curl:
  `http://web.archive.org/web/2024id_/https://digitalcommons.wku.edu/cgi/viewcontent.cgi?article=<N>&context=<collection>`
  **Use `curl -L`** or you get a bare 302 and an empty file. Where there is no
  snapshot, try
  `.../context/<collection>/article/<N>/type/native/viewcontent`.
  About four concurrent connections; a fifth fails in a way that looks like a
  missing snapshot. Parallel Range requests are far faster on big volumes.

- **Test the embedded PDF text layer before OCRing.** On the 2002-2009 Heralds
  it is good and better than OCR. On 1990s and older scans it is close to
  unreadable — render at 300 dpi with PyMuPDF and use `ocrmac`.

- **The Herald is OCR-indexed continuously from 1993 to 2019** across four
  indexes on the Desktop. Grep them before fetching anything.

- **Talisman grids, volume at a time.** Read the volume once, OCR every name
  label, build one name-to-cell map, then match your whole list in a single
  pass. Prove each row against the rows above and below on sex and alphabetical
  order before cutting. Searching the index name by name fails, because the
  leaf an OCR hit lands on is only a pointer: the text pools captions from
  pages several leaves away.

- **Always read the printed folio.** Leaf offsets vary by volume and sometimes
  within one, and at least one of our own tools computes a leaf three too high.

## What you must not touch

`data/photos.json`, `data/years.json` and `site/` are the editor's. Write only
your findings file, your notes file, and your crops.
