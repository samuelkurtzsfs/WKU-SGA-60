# Photograph run, 26 November (second pass)

## Baseline reconfirmed, unchanged from this morning's pass

- Priority 1 (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four already carry a
  `leaders` portrait in `data/photos.json`.
- Priority 2: every president and student regent in the record carries a portrait.
  `check_data.py` runs clean.
- Priority 3: `scripts/portrait_gap.py --any-year` is unchanged since this morning's Amelia
  Tucker addition — 157 people, 155 with no portrait anywhere in the file, almost all
  2018-2026 and concentrated in Judicial Council, Senate secretary/parliamentarian seats and
  college senators.
- Priority 4: all 61 years already carry at least one `years`-level photograph.

## What this pass checked

- **wkuherald.com's WordPress API**, by date: the ten most recent posts matching "SGA" are
  unchanged since this morning. Nothing has been published since 17 November's "SGA prepares
  for the holidays with new bills," already read and ruled out on 23 November's second pass.
- **Network gates, retested cold:**
  - `digitalcommons.wku.edu` item/landing pages answered 200 directly (tested against
    `dlsc_ua_records/1619`).
  - `cgi/viewcontent.cgi` (the actual PDF route) returned HTTP 403 with full browser
    navigation headers, tried via plain Python `urllib` rather than `curl` in case of a
    TLS-fingerprint difference. Closed.
  - `digitalcommons.wku.edu/do/search/` returned HTTP 403. Closed.
  - `web.archive.org` reset at the TLS layer (`ws_closed_mid_exchange` at the egress proxy).
    Closed, consistent with every pass since mid-September.
  - `archive.org/download/...` (the Talisman plain-text route, ordinarily not rate-limited)
    returned HTTP 503. Not the usual bot-block shape; may be a transient service issue on
    archive.org's side rather than a gate. Worth a fresh try next pass, though the 2018-2025
    cohort that makes up most of the standing gap is in the Talisman's post-2011 magazine
    format anyway, which prior passes already closed out as a dead end for this purpose.
- Confirmed no new names have entered `data/years.json`'s `organization` block for 2026-27
  beyond what the morning pass already checked (Veronica Butler, Jaden Marshall, Molly Ricky,
  Amelia Tucker, Carter Smith) — all five already carry a portrait.

## Conclusion

No new portrait. Every open route was retested rather than assumed, and none produced
anything the standing record did not already have. `data/photos.json` and `data/photos/` are
unchanged; this note is the only new file. `python3 scripts/build.py` and `python3
scripts/check_data.py` both run clean against unchanged data.

Two items unchanged from every recent pass, still needing the account holder rather than a
further automated run:

1. `data/photo-finds/_for-the-editor.md` — 13 people, 14 entries, open since 8 September 2026,
   each a proved photograph whose tie to the named officeholder needs a yes/no editorial call
   that automated research cannot make.
2. The photograph trigger's cadence against a 155-person Senate/officer gap that has now been
   checked, repeatedly, through every reachable source. `update_trigger` was refused in an
   earlier run ("created via http_api, not by an agent"); only the account holder can change it.
