# Photograph run, 13 September (scheduled)

## State confirmed at the start of this run

All four presidents named in the standing brief already had verified portraits
from an earlier run — checked the magic bytes on each file, all real JPEGs
(`FF D8 FF E0`):

- Nick Todd (2004-05) — `data/photos/2004-05-nick-todd.jpg`
- Katie Dawson (2005-06) — `data/photos/2005-06-katie-dawson.jpg`
- Jeanne Johnson (2007-08) — `data/photos/2007-08-jeanne-johnson.jpg`
- Reagan Gilley (2008-09) — `data/photos/2008-09-reagan-gilley.jpg`

Wider check against `data/years.json`:

- **Every president and student regent (72 of 72 terms) has a portrait.**
  The one `role: "unresolved"` leader, Reed Morgan (1968-69), is excluded —
  CLAUDE.md settles that he never held either office, so there is nothing to
  photograph him *as*.
- **Every one of the 61 years has at least one photograph** attached
  (leader portrait or a year photo), so there is no year left with zero
  images.

So the only open item from the brief's priority list is priority 3:
executive cabinet and Senate officers without a portrait. Filtering the
218 raw misses down to named officer titles (cutting plain "Senator" /
"Senator At Large" / "Representative" seats, which are not the kind of
office the brief means) leaves **166 candidates**, spread 1977 to 2024.

## What I tried this run, and why it didn't produce a portrait

Nothing below cleared the bar. Recording it so the next run doesn't repeat
the same dead ends.

### Talisman via archive.org (free, not rate-limited)

archive.org only holds Talisman plain text for 1943-1981, 1986 and 1987 —
nothing for 1988-2015. That covers a handful of this run's candidates:

- **David Bass**, ASG activities vice president 1977-78 — found. Talisman
  1978, p. 34 (scan leaf 38 of `talisman1978west`). The caption describes
  *"a light moment in an ASG meeting"* and names four people without
  placing them: president Bob Moore, activities vice president David Bass,
  secretary Sharon May and vice president Cathy Murphy. The photo is a
  candid four-person group shot with no positional cue (no "left to
  right," no one facing the camera alone) — I could not tell which of the
  three visible faces is Bass. **Not used as a portrait** under the "never
  use a photo whose subject you cannot confirm" rule. It would be legitimate as a *year*
  photo (1977-78) captioned generically for the group, if a future pass
  wants it — 1977-78 already has other photos, so I left it out rather
  than add a caption that can't name a face.
- **David Young**, administrative vice president 1978-79 — found only as a
  text quote (Talisman 1979, scan p. 291/printed p. 289, an "ASG year in
  review" spread), no accompanying photo of him.
- **Steve Wilson** — the 1978-79 Judicial Council Chairman does not appear
  in `talisman1979west`. The "Steve Wilson" hits in that text are a
  different person (an SAE Spring Sing barbershop quartet member,
  agriculture major, senior portrait page).
- **Alice Wicks** (Secretary, 1978-79) — index-only, no page content found.
- **Mark Chesnut**, Treasurer 1980-81 — a "Mark Chesnut (Sigma Alpha
  Epsilon)" appears on the men's intramurals results page of Talisman 1981
  (printed p. 234, scan leaf 238), winning badminton and racquetball. The
  action photo on that page is an unlabeled football scrimmage shot; none
  of the men in it are identified by name, and there's no way to confirm
  this is even the same Mark Chesnut who was ASG treasurer (common name,
  Greek-life context different from ASG). **Not used.**
- **Chris Millay** and **Dwight Austin** (Parliamentarian / Sergeant-at-Arms,
  1986-87) — neither name appears anywhere in `talisman1987west`.

### digitalcommons PDF and search — blocked this session

`digitalcommons.wku.edu/dlsc_ua_records/<id>/` landing pages load fine
(200), but both `cgi/viewcontent.cgi` (the actual PDF) and `do/search/`
returned HTTP 403 with a Cloudflare **managed JS challenge** page
("Just a moment...") rather than the usual bot-check page. This is not the
ordinary rate-limit 403 the pacing rule is written for — waited the full
90 seconds, did unrelated work in between (ran `build.py` / `check_data.py`
to occupy real wall-clock time), retried once, same challenge. A JS
challenge cannot be passed by curl regardless of backoff; it needs an
actual browser. Checked: neither `playwright` (pip) nor a `playwright`
node package is installed in this container, only the bare Chromium
binary at `/opt/pw-browsers` with no automation library wired up to drive
it. I did not install anything (out of scope for a research run).

This blocked the one promising lead I had lined up: the 2003 Talisman
("About Face", `dlsc_ua_records/594`) for the 2001-03 committee chairs
(Shara Hammers, Michelle Woods, Andrea Lovell, Brooke Smith) — CLAUDE.md's
own guidance is that these yearbook SGA spreads are the best source, and
this one was never reached.

**For the next run:** retry `cgi/viewcontent.cgi` first thing — this may
be a session/IP-scoped challenge that clears on its own. If it's still
blocked, a real browser (Playwright) is the only way through it; that's an
environment/setup change outside a single research run's scope.

### wkuherald.com (2003-present, full text, not rate-limited)

Checked several recent Senate officers this way, since the WordPress API
exposes `featured_media` and I could check each photo's caption without
opening the article:

- **Nathan Cherry** (Speaker 2016-17) — found in text ("Speaker Nathan
  Cherry hopes the bill will help senators...") but the article carries no
  featured image.
- **Ryan Richardson** (Speaker 2017-18) — several matching articles, none
  with a photo of him specifically; SGA meeting-recap photos on this site
  are almost always an unlabeled wide shot of the chamber.
- **Justin Goins** (Chief Justice 2022-23 / Associate Chief Justice
  2021-22) — three matching articles; the one photo checked (a judicial
  hearing story) captions only President Cole Bornefeld, not Goins.
- Checked the "new Senate sworn in" article for four different years
  (2024, 2025, 2026 — the last is out of this project's 1966-2026 window
  going into 2026-27, noted only for completeness) — every one of these
  swearing-in photos is captioned generically ("newly-elected senators are
  sworn in...") or names only the president, never the individual
  officers being sworn in.

**Pattern worth recording:** the Herald's SGA coverage almost never
individually captions a Senate officer or judicial council member the way
it does the president. A search-by-name strategy across these 166
candidates is going to keep hitting this same wall unless the target
happens to have been separately profiled (an election-guide candidate
photo, a homecoming court appearance, etc. — the same categories that
worked for the four presidents already on file). **Worth trying next:**
searching each candidate name against the Herald's *election coverage*
specifically (search `"<name>" candidate` or `"<name>" senate election`)
rather than their in-office coverage, since that's where the four
priority presidents' portraits actually came from.

## Remaining 166 candidates (officer titles only, seats/at-large excluded)

See the filtered list this run generated — regenerate with:

```python
import json
data = json.load(open('data/years.json'))['years']
photos = json.load(open('data/photos.json'))
photo_names = {l['name'] for l in photos.get('leaders', [])}
skip = ['senator', 'representative']
for y in data:
    org = y.get('organization', {})
    for e in org.get('executive', []):
        n, office = e.get('name'), (e.get('office') or '')
        if n and n not in photo_names and n.lower() not in ('unknown', 'vacant', ''):
            print(y['id'], n, office, 'exec')
    for o in org.get('senate', {}).get('officers', []):
        n, office = o.get('name'), (o.get('office') or '')
        low = office.lower()
        if any(s in low for s in skip) and 'chair' not in low and 'speaker' not in low:
            continue
        if n and n not in photo_names:
            print(y['id'], n, office, 'senate')
```

No data files changed this run — nothing to commit to `data/years.json` or
`data/photos.json`. This note is the only new file.
