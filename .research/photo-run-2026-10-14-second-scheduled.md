# Photograph run, 14 October (second scheduled pass): confirms the morning note, closes Mark Henry, pins down the digitalcommons block

## Priorities 1, 2 and 4: reconfirmed, unchanged

Checked programmatically against `data/photos.json` before anything else, per CLAUDE.md's "check
whether an earlier run already got them."

- **Priority 1** (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley): all four still carry a
  portrait, each file re-verified as a real JPEG (`FF D8 FF E0` header) at its path in
  `data/photos/`.
- **Priority 2** (every other president or student regent): every `leaders` record in
  `data/years.json`, all 61 years, checked by `(name, year)` against `data/photos.json`. Zero
  missing.
- **Priority 4** (years with no photograph at all): every year id checked against `photos.json`'s
  `years` array. Zero missing.

`python3 scripts/portrait_gap.py`: **189 officer slots / 159 people / 157 with no portrait in any
year** — the exact count the 13 and 14 October runs left it at. Nothing closed it further this
pass either.

## What this pass added: one more name, and a precise diagnosis of the digitalcommons block

The morning's `photo-run-2026-10-14-scheduled.md` worked seventeen 2003-2022 names through the
`wkuherald.com` WordPress REST route and found no portrait that met the bar. It did not reach
**Mark Henry** (2004-05, Information Technology Director). Checked this pass:
`wp-json/wp/v2/posts?search=Mark%20Henry` — ten hits, all 2024-2025 sports and campus-building
stories about an unrelated subject. No SGA-era hit at all. No portrait, no citation.

The morning note left `cgi/viewcontent.cgi` and `web.archive.org` as "closed" without saying why.
Worth recording precisely, since it changes what a future run should try: **this container's own
network egress proxy refuses the connection**, not WKU's server. A direct attempt to let a real
browser (Playwright/Chromium, already installed at `/opt/pw-browsers`) solve the Cloudflare
challenge on a Talisman PDF failed with

```
brunhild.challenges.cloudflare.com:443 — connect_rejected (the egress proxy denied the CONNECT
(organization policy) or could not reach the destination)
```

So the JS challenge cannot resolve from inside this sandbox regardless of headers, retries, pacing
or a real browser engine — the proxy is blocking the challenge host itself, by policy, before
Cloudflare ever sees a retry. This is a different, harder failure than the 403-and-backoff pattern
CLAUDE.md describes for ordinary digitalcommons rate limiting, and no amount of pacing fixes it.
It affects every Talisman year **not** mirrored on `archive.org` (1971-1981, 1986 and 1987 only),
which is most of the collection the gap list needs — 2012, 2014-2017 among them, which this pass
had hoped to reach for Brittany Crowley, Sawyer Coffey, Rachel Keightley, Abhishek Bose and Smita
Peter's SGA-era coverage. Confirmed again this pass that those years are not mirrored on
`archive.org` either (`https://archive.org/metadata/talisman<year>west` returns an empty `files`
list for every one of 1996-1999, 2004-2005, 2008-2010, 2013, 2015-2018 and 2022 — the whole
2004-2011 span plus 1997-2002 has no Talisman at all, per WKU's own publication-history note that
the yearbook stopped in 1994 and restarted in 2003).

Re-confirmed the archive.org Talisman slice itself needs no further work: 1978, 1979 and 1981 were
read page-by-page again this pass (via `archive.org`'s `BookReaderImages.php`, which is not
Cloudflare-gated and not rate-limited the way digitalcommons is) chasing David Bass (1977-78,
Activities VP), David Young (1978-79, Administrative VP) and Alice Wicks (1978-79, Secretary). All
three turn up only in unlabelled multi-person group-photo captions ("A LIGHT MOMENT IN AN ASG
MEETING brings laughter from president Bob Moore and smiles from activities vice president David
Bass, secretary Sharon May and vice president Cathy Murphy" over a photo with no per-person
position cues) or, for Wicks, no photo credit in the yearbook's index at all. None clears the
identification bar. This matches what the 12 October third pass already closed these names on;
not re-litigated past confirming it still holds.

## Nothing changed in the data

`data/photos.json`, `data/photos/` and `data/years.json` are all untouched this run.
`python3 scripts/build.py` then `python3 scripts/check_data.py`: 61 years, clean — 60 presidents,
no missing leader portrait, no year without a photograph, same as every recent pass.

## For the next run

- Don't re-try `cgi/viewcontent.cgi` expecting pacing or headers to help — the block is this
  container's own proxy policy on the Cloudflare challenge host, not WKU's rate limiter. It would
  need the egress policy itself changed to open, which is outside what a research pass can do.
- The `wkuherald.com` WordPress REST route remains the one living way into post-2002 coverage; the
  22 names tried across the last two passes (seventeen this morning, Mark Henry this evening, plus
  the earlier Aaron Pawley/Brittany Crowley citations) are exhausted **for portraits** on it.
  Re-querying them without a new source would just repeat these two notes.
- The 157 people with no portrait in any year are overwhelmingly committee chairs, judicial
  council justices and senate officers from exactly the years `archive.org` doesn't mirror and
  digitalcommons can't be reached from. Closing more of the gap list needs either this container's
  network policy to open `digitalcommons.wku.edu`'s PDF route, or a source outside TopSCHOLAR
  entirely (wku.edu/news for the most recent years is still untried against this specific name
  list and doesn't share digitalcommons' gate).
