# Photograph run, 28 November (second pass this session): John Holland checked, both network gates retested cold, no new portrait

## Baseline, reconfirmed before anything else

Same as this morning's pass: the four presidents once missing a portrait (Nick Todd, Katie
Dawson, Jeanne Johnson, Reagan Gilley) all still carry one, every president and student regent
has a portrait, all 61 years carry at least one photograph, and `scripts/portrait_gap.py`
reports the same 187 cabinet/Senate-officer slots without a portrait, held by 157 people, 155 of
whom have no portrait in any year — unchanged since 22 November.

## What this pass tried

Cross-checked the archive.org-era slice of the officer gap (years archive.org actually holds
Talisman text for: 1971-1981, 1986, 1987) against `data/photo-finds/_do-not-use.json`. Of the
names in that slice — Vern Pulman (1974-75), David Young and Alice Wicks (1978-79), Mark Chesnut
(1980-81), John Holland (1983-84 and 1984-85), Chris Millay and Dwight Austin (1986-87) — every
one has already been closed out and barred except John Holland, who had never been searched.

John Holland turned out not to be checkable the way the others were: his two years, 1983-84 and
1984-85, are inside the gap archive.org does not cover (it holds 1971-1981, 1986 and 1987 only,
not 1982-1985), so `talisman1984west_djvu.txt` and the 1985 equivalent do not exist on
archive.org — confirmed by fetching both URLs directly; both return the site's own HTML error
page, not a yearbook. No other open route reaches these two years: `wkuherald.com` only goes
back to roughly 2003, and `digitalcommons.wku.edu/cgi/viewcontent.cgi` (the only way to the 1984
or 1985 Talisman PDF) is the gate below, still closed. John Holland is not added to
`_do-not-use.json` as a closed lead, since nothing was found to rule in or out — there is simply
no open source for his two years right now.

## Network gates, retested cold

- `digitalcommons.wku.edu/cgi/viewcontent.cgi`: still answers 403 on a plain GET with full
  navigation headers (`Sec-Fetch-Dest: document`, `Sec-Fetch-Mode: navigate`,
  `Upgrade-Insecure-Requests: 1`) and a real browser user agent. Unchanged from every pass since
  this gate closed.
- `web.archive.org`: the agent egress proxy now closes the tunnel mid-exchange
  (`ws_closed_mid_exchange`) rather than returning any HTTP status at all. This is a step beyond
  the plain connection reset earlier passes reported — worth a later pass checking whether it is
  the same block or a new one, since the error text is different this time.

## Unchanged

`data/photos.json` and `data/photos/` are unchanged this pass; only this note was added. Build
and `check_data.py` both run clean.
