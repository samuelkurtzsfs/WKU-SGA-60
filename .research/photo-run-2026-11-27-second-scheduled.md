# Photograph run, 27 November (second scheduled pass): baseline reconfirmed again, officer-gap list independently re-checked for anything untried, none found

## Baseline, checked fresh against the live data rather than taken from the last note

All 73 `leaders` records carry a portrait, including the four presidents the trigger's stored
brief still names (Nick Todd, Katie Dawson, Jeanne Johnson, Reagan Gilley). Every president and
student regent in `data/years.json` has one. All 61 years carry at least one photograph.
`portrait_gap.py` reports 187 cabinet/Senate-officer slots still without a portrait, held by 157
distinct people — unchanged from the first pass earlier today.

## What this pass did differently from the first pass today

Rather than re-walk the same handful of leads the morning run already named, pulled the full
157-name officer-gap list fresh off `portrait_gap.py --list` and checked, name by name, how many
times each one already appears in `.research/*.md` and `data/photo-finds/*.json` — looking
specifically for any name nobody has actually tried yet. There isn't one. The least-searched name
on the whole list, ShyAnte'e Williams, looked like an outlier at a single grep hit only because the
apostrophe in her name defeats a plain-text search; stripped to the stem "ShyAnte" she turns up in
29 prior notes, including the 20 September correction in `NIGHT-REPORT.md` that found her named
twice in the *Herald* under a stem a too-literal search had missed. Every other name on the list
returns between 5 and 31 prior hits. This confirms, by direct count rather than by memory, what the
last several weeks of this file have been saying in prose: the officer-gap list is not a backlog of
untried names, it is a backlog of names already tried on every open route and found wanting.

## Network gates, retested cold a second time this session

- `cgi/viewcontent.cgi`: still 403, full navigation headers sent, same as the morning check.
- `web.archive.org`: still `Recv failure: Connection reset by peer` at the egress proxy, same as
  the morning check.
- `archive.org/download/...`: still open (302 to the asset, confirmed reachable).
- `wkuherald.com` WP-JSON: still open.

Both routes that have produced every new portrait landed since early October are the same two
closed this morning. Nothing reopened in the hours between the two passes.

## Unchanged

`data/photos.json` and `data/photos/` are unchanged this pass; only this note was added. Build and
`check_data.py` both run clean (61 years, 73 leader portraits, 157-person officer gap unchanged).
The 13-person, 14-entry editor queue in `data/photo-finds/_for-the-editor.md` is unchanged and
still needs a human yes/no call that no further automated pass can supply.
