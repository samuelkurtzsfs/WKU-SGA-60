# Photograph run, 11 October (later scheduled) — the 2000-01 scene-photograph gap closed; the 1994-95 gap is still open, and a chunked-download corruption hazard is logged for the next run that tries the same workaround

## Priorities 1 and 2, reconfirmed before anything else

**Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
portrait in `data/photos.json`. Nothing to do.

**Priority 2** (any other president or student regent without a portrait): checked every
`leaders` record in `data/years.json` against `data/photos.json` by name, programmatically. Zero
missing.

## Priority 4: 2000-01's scene-photograph gap is closed

`data/photos.json`'s `years` array carried no entry for 2000-01 (confirmed by every run since
9-10 October). Found one this pass: the front page of Herald 75:52, 13 April 2000 ("A Friendly
Debate") carries a photograph of the SGA presidential candidates debating at a Meet Your
Candidates session, each standing behind a lectern printed with their own name —
**Cassie Martin** and **Duan Wright** — with two other candidates seated between them. The
nameplates are the identification; this is a stronger basis than a caption alone, since the
photograph itself labels each standing figure. Cassie Martin went on to win the presidency and
already carries her own portrait (`2000-01-cassie-martin.jpg`); this is a scene photograph for
the year, not a new leader portrait, and was added to the `years` array as
`2000-01-sga-debate.jpg`.

The same page also carries a second photograph, captioned "Vice presidential candidates Dwight
Campbell and Leslie Bedo share a friendly conversation after Tuesday's debates" — cropped and
reviewed this pass but not added, since the nameplate photograph is the stronger identification
and the `years` array wants one representative scene, not every frame on a page already otherwise
well covered (every 2000-01 executive officer, Bedo included, already carries a portrait).

**Route to the PDF:** the live `digitalcommons.wku.edu/cgi/viewcontent.cgi` endpoint is still
Cloudflare-gated (confirmed 403 this run, same as every pass since the gate closed). The Wayback
`id_` bypass worked, consistent with the two 11 October runs before this one.

## Priority 4: 1994-95's scene-photograph gap is still open

Three leads chased this pass, none landed:

- **Article 7936** ("A new beginning," Herald 70:56, 27 Apr 1995, viewcontent article 8933) —
  downloaded whole (15.1 MB, 29 pages) via the Wayback `id_` bypass, no corruption. Pages 1, 2, 3,
  5, 6 and 7 rendered and read directly: front page (Ole Miss chancellor search, Herald-apology
  protests, mayoral-election turnout piece), p.2 (campus briefs, an Oklahoma City vigil photo),
  p.3 (jump continuations), p.5–7 (Your View/editorial page, voting-rights-group story, a
  full-page ad). **No SGA content and no photograph relevant to this project on any of the six
  pages read.** The transition story this citation is logged against was not found in the pages
  checked; it may run later in the issue (pp. 8–29, mostly unchecked this pass) or may be a short
  item with no photograph at all. Not exhausted — a future pass should read the remaining pages
  rather than re-read these six.
- **Article 7984** ("Evans defeats Sivley for the SGA presidency," Herald 69:51, 19 Apr 1994,
  viewcontent article 8989) — the single most promising lead, an election-result story for the
  1994-95 president. The front page (printed p.1) carries only the pre-election "Sivley vs. Evans
  at polls today" preview, with a photograph unrelated to SGA (a Physical Plant employee
  sweeping Van Meter Hall). The jump line sends the story to printed page 6, which — along with
  pages 7 and 8 — rendered blank in this pass's copy of the PDF. **That blankness should not be
  read as the pages being empty.** See the corruption note below: this file could not be fetched
  in one piece and was reassembled from five byte-range chunks, and page 9's render came back with
  a grey corruption block across its lower third, proving the reassembly was not clean throughout.
  Pages 6–8 rendering as pure white, immediately after a 5 MB chunk boundary, is exactly the
  failure mode that kind of corruption produces, not good evidence the pages are genuinely blank.
  **This lead is not closed.** The next run should fetch this same file again — ideally in one
  shot if the connection allows it that session, or in differently-sized chunks if not — and
  specifically re-render printed pages 6 through 9, which is where the election result and any
  candidate photograph would run.
- **Article 8114** ("Martin and Wright discussed the issues," Herald 75:52, 13 Apr 2000,
  viewcontent article 9118) — this is the 2000-01 lead, included here only to record the download
  hazard it exposed: a first attempt via the Wayback `id_` bypass returned exactly 1,048,576 bytes
  (2^20, a suspiciously round number) for two separate snapshot timestamps, and PyMuPDF could open
  only 9 of the file's 17 pages before erroring "cannot find page 10 in page tree." A **different,
  larger snapshot of the same article** (10.9 MB instead of ~1 MB) fetched whole and opened clean.
  **When a Wayback `id_` fetch comes back at exactly a power-of-two byte count, treat it as
  truncated and look for a different snapshot timestamp of the same article before trusting the
  page count it reports.**

## A real finding: large PDFs (roughly 15+ MB) do not reliably complete through this session's
## egress proxy as a single request, but byte-range chunking works around it

`curl` against the two large Wayback PDFs this pass needed (8933 at 15.1 MB, 8989 at 23.9 MB)
failed outright on the first one (`Recv failure: Connection reset by peer`, reproduced on retry)
and succeeded on the second only after being split into five 5 MB range requests
(`curl -r start-end`) and concatenated with `cat`. The agent proxy's own error surfaced during the
single-shot attempts: `ws_closed_mid_exchange — the tunnel to the egress proxy closed before the
exchange completed`. **Chunked range-fetching is a working workaround for this session**, but the
reassembled file is not guaranteed byte-perfect — page 9 of the chunked 8989 download rendered
with a visible corruption artifact even though the overall byte count matched the CDX record
exactly and PyMuPDF opened all 21 pages without raising an error. A page that opens without error
and renders as blank or part-corrupted near a chunk boundary is not a trustworthy negative. Prefer
a single-shot fetch when the file size allows it (this session moved under ~11 MB cleanly); fall
back to range-chunking only when single-shot fails, and treat anything within a few hundred KB of
a chunk boundary as unverified until re-fetched a different way.

## Nothing else changed

`data/years.json` is untouched. `python3 scripts/build.py` and `python3 scripts/check_data.py`
both exit clean (61 years, 1,968 events, 60 presidents; "the archive checks out against its own
rules"). One file added to `data/photos/` (`2000-01-sga-debate.jpg`, JPEG-magic-byte verified) and
one entry added to `data/photos.json`'s `years` array.

## For the next run

- Priority 3 (officer portraits) is unchanged from the last several passes: `scripts/portrait_gap.py`
  reported 189 officer slots / 159 people / 157 with no portrait anywhere before this run started;
  this pass did not touch it.
- 1994-95's scene-photograph gap is still open. Re-fetch viewcontent article 8989 (Herald 69:51,
  19 Apr 1994) and read printed pages 6-9 specifically — this pass's copy of those pages is
  suspect, not a clean negative. Article 8933 (Herald 70:56, 27 Apr 1995) has pages 8 through 29
  still unread and came through with no corruption, so a direct read of the rest of it is the
  cheaper next step.
- Treat any Wayback `id_` download that lands on an exact power-of-two byte count as truncated;
  pick a different snapshot timestamp from the CDX listing rather than trusting the short file.
- For any future large (15+ MB) Wayback fetch: try single-shot first, fall back to 5 MB
  byte-range chunks via `curl -r`, and re-verify any page within roughly 500 KB of a chunk seam
  by an independent fetch before treating a blank or odd render as a real negative.
