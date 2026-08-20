#!/usr/bin/env python3
"""
One-off companion to harvest_topscholar_legislation.py.

That script's ROW regex only matches listing rows whose date carries
class="dtstart" exactly. Many rows carry class="dtstart visually-hidden"
instead and were silently skipped, so 284 dated documents on the SGA
Legislation listings never got harvested. This parses the listings by
<tr class="vevent"> block, which catches both forms, and fetches only the
documents legislation.json does not already have. Same pacing and headers as
the original: one request at a time, 3s apart, 90s backoff on 403, item page
first then the PDF with a Referer.
"""
import json, re, sys, time, http.cookiejar, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "legislation"
META = ROOT / "data" / "legislation.json"

LISTINGS = [
    ("bill", "https://digitalcommons.wku.edu/sga/Legislation/Bills/"),
    ("resolution", "https://digitalcommons.wku.edu/sga/Legislation/Resolutions/"),
]

VEVENT = re.compile(r'<tr[^>]*class="vevent"[^>]*>(.*?)</tr>', re.S)
DTSTART = re.compile(r'class="dtstart[^"]*"\s+title="(\d{4}-\d{2}-\d{2})T')
LINK = re.compile(
    r'<a href="(https?://digitalcommons\.wku\.edu/sga/Legislation/'
    r'(?:Bills|Resolutions)/(\d+))"\s*>([^<]+)</a>')

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

_cj = http.cookiejar.CookieJar()
_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(_cj))


def fetch(url, binary=False, referer=None):
    headers = {"User-Agent": UA}
    if binary:
        headers.update({
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
        })
        if referer:
            headers["Referer"] = referer
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers)
            data = _opener.open(req, timeout=60).read()
            time.sleep(3)
            return data if binary else data.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 403 and attempt < 3:
                time.sleep(90)
                continue
            raise
    raise RuntimeError("unreachable")


def session_from_date(iso):
    """Academic year containing a dated item.

    Beware: TopSCHOLAR gives some items a year and no month, which arrives here
    as YYYY-01-01 and files a fall document into the *previous* academic year.
    Twenty-three items came through that way on the first run and had to be
    refiled by hand off the -F in their own numbers. If the listing date is
    year-only, read the semester letter out of the title before trusting this.
    """
    y, m = int(iso[:4]), int(iso[5:7])
    start = y if m >= 8 else y - 1
    return f"{start}-{str(start + 1)[2:]}"


def harvest_item(kind, iso, url, item_id, list_title):
    session = session_from_date(iso)
    dest = OUT / session / f"dc_{kind}_{item_id}.pdf"
    page = fetch(url)
    m = re.search(r'citation_pdf_url" content="([^"]+)"', page)
    if not m:
        return None, f"{url}: no pdf link"
    pdf_url = m.group(1).replace("&amp;", "&")
    t = re.search(r'citation_title" content="([^"]+)"', page)
    title = (t.group(1) if t else list_title).strip()
    if not dest.exists():
        blob = fetch(pdf_url, binary=True, referer=url)
        if not blob.startswith(b"%PDF"):
            return None, f"{url}: not a PDF ({len(blob)} bytes)"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(blob)
    return {"session": session, "type": kind, "title": title, "date": iso,
            "file": f"{session}/{dest.name}", "source_url": url}, None


def main():
    meta = json.loads(META.read_text())
    known = {e["source_url"].rstrip("/") for e in meta["entries"]}

    jobs, seen = [], set()
    for kind, listing in LISTINGS:
        text = fetch(listing)
        for block in VEVENT.findall(text):
            d = DTSTART.search(block)
            a = LINK.search(block)
            if not d or not a:
                continue
            iso = d.group(1)
            url = a.group(1).replace("http://", "https://")
            item_id, title = a.group(2), a.group(3)
            key = url.rstrip("/")
            if key in known or key in seen:
                continue
            seen.add(key)
            jobs.append((kind, iso, url, item_id, title))
        print(f"{listing}: {len(jobs)} cumulative new jobs", flush=True)

    print(f"{len(jobs)} new documents to fetch", flush=True)
    added, failed = [], []
    for i, job in enumerate(jobs, 1):
        try:
            entry, err = harvest_item(*job)
        except Exception as e:
            entry, err = None, f"{job[2]}: {e}"
        if entry:
            added.append(entry)
        else:
            failed.append(err)
        if i % 20 == 0:
            print(f"{i}/{len(jobs)} done, {len(added)} added, {len(failed)} failed",
                  flush=True)

    meta["entries"].extend(added)
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n")
    total = sum(f.stat().st_size for f in OUT.rglob("*.pdf"))
    print(f"added {len(added)}, {len(failed)} failed, "
          f"{len(meta['entries'])} total entries, {total // 1_000_000} MB on disk")
    if failed:
        print(*failed[:20], sep="\n", file=sys.stderr)


if __name__ == "__main__":
    main()
