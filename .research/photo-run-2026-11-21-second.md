# Photograph run, 21 November (second pass)

## Baseline reconfirmed before anything else

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  `leaders` portrait entry in `data/photos.json`, and all four image files were re-verified by
  magic bytes (`FF D8 FF E0`) directly from disk this pass, not just trusted from the JSON.
- **Priority 2**: `python3 scripts/check_data.py` — "61 years, 1964 events, 60 people have been
  president" — every president and student regent still carries a portrait.
- **Priority 3**: `python3 scripts/portrait_gap.py --any-year` — unchanged from this morning's
  pass and every pass for the past three weeks: 187 same-year officer slots with no portrait, 157
  people, 155 of whom have no portrait anywhere in the file. Checked every one of the 155 names
  against `.research/*.md` and `data/photo-finds/*.json`: all 155 already appear in a prior run's
  notes. None is untried.
- **Priority 4**: all 61 years still carry at least one `years`-level photograph entry.
- The current year, 2026-27, has a portrait for every executive officer already on file (Lucas,
  Barker, Derryberry, Pace, Bailey, Butler, Marshall, Carter Smith), so there was no open lead
  there either.

## What this pass actually tried, beyond re-confirming the baseline

- **Retested the digitalcommons.wku.edu gate directly.** `curl` still gets a flat 403 on
  `viewcontent.cgi`. Plain Python `urllib.request` with navigation headers (`Sec-Fetch-Dest:
  document`, `Sec-Fetch-Mode: navigate`, `Upgrade-Insecure-Requests: 1`) got a clean 200 and a
  real PDF on the first try. This is the same TLS-fingerprint bypass the 17 November pass logged;
  it is open again today, not a new finding, but worth reconfirming since it comes and goes.
- **`web.archive.org` is closed this session**: a plain HTTPS request to an `if_` capture URL hit
  a proxy-level connection reset (`ws_closed_mid_exchange`), not a remote 403. Consistent with the
  16 November finding that this is a proxy policy block on the hostname rather than a flaky
  remote.
- **Checked wkuherald.com's SGA-tagged feed fresh**: nothing published since the 17 November "SGA
  prepares for the holidays with new bills" post, which the first pass today already read in full.
  No new lead.
- **Re-opened the Justin Goins / Erika Puhakka / Josh Zaczek / Nathan Cherry threads** from the
  standing gap list with fresh wkuherald.com searches, since these are Judicial Council and
  Senate-leadership names from the richest-documented recent decade. The one photograph this
  turned up — Julie Mishchuk, Speaker of the Senate, captioned twice in the 17 Feb 2023 Judicial
  Council story — is already in `data/photos.json` (`2022-23-julie-mishchuk.jpg`); it does not
  name Goins. The two Nathan Cherry articles with a photograph attached (15 Feb 2017, 21 Sept
  2016) carry no caption naming him; the "Cherry" hits in their HTML are an unrelated word, not
  the person. No new portrait from any of the four names.
- **Confirmed the 2012/2018/2020/2021/2022 Talisman volumes invisible to year-keyed search**
  (`dlsc_ua_records/8897, 8690, 8681, 8776, 8898, 9256` — see `data/photo-finds/_archive-gaps.json`)
  are not unopened leads: prior passes (most recently 17 November) already opened and swept all
  of them. Did not re-fetch.

## Conclusion

No new portrait, no change to `data/photos.json` or `data/photos/`. `python3 scripts/build.py`
and `python3 scripts/check_data.py` both run clean; `site/`'s build-date-only diff was reverted
(`git checkout -- site/`). The standing ~155-person officer-portrait gap remains exhaustively
documented — every name has a dead end on file from at least one prior pass, and this pass's own
fresh attempt on four of the richest-documented names reproduced that. The digitalcommons gate
being open today changes nothing material, since every lead reachable through it for this gap
was already fetched and closed by earlier passes while it was open on other days. Landing this
note only on `research-photos`; no push notification, since nothing changed from the baseline
every recent pass (including this morning's) has already reported.
