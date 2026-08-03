#!/usr/bin/env python3
"""
Harvest pre-2011 SGA legislation from TopSCHOLAR (digitalcommons.wku.edu).

Reads  digitalcommons.wku.edu/sga/Legislation/Bills/        (1976-2008)
       digitalcommons.wku.edu/sga/Legislation/Resolutions/
Writes data/legislation/<session>/dc_<type>_<id>.pdf
       merges entries into data/legislation.json

Each listing row carries an exact ISO date, so every document is filed to its
academic session from the date itself: August-December belongs to year-(year+1),
January-July to (year-1)-year.

Idempotent: entries whose source_url is already in legislation.json are skipped.
"""
import json, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "legislation"
META = ROOT / "data" / "legislation.json"

LISTINGS = [
    ("bill", "https://digitalcommons.wku.edu/sga/Legislation/Bills/"),
    ("resolution", "https://digitalcommons.wku.edu/sga/Legislation/Resolutions/"),
]

ROW = re.compile(
    r'<abbr title="(\d{4}-\d{2}-\d{2})T[^"]*" class="dtstart">.*?'
    r'<a href="(https?://digitalcommons\.wku\.edu/sga/Legislation/(?:Bills|Resolutions)/(\d+))" ?>([^<]+)</a>',
    re.S)


UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def fetch(url, binary=False):
    """One request at a time, 3s apart, with 90s backoff on a 403.

    TopSCHOLAR's bot protection triggers on burst volume, not identity - a
    parallel crawl gets every request refused, a slow polite one sails through.
    """
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            data = urllib.request.urlopen(req, timeout=60).read()
            time.sleep(3)
            return data if binary else data.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 403 and attempt < 3:
                time.sleep(90)
                continue
            raise
    raise RuntimeError("unreachable")


def session_from_date(iso):
    y, m = int(iso[:4]), int(iso[5:7])
    start = y if m >= 8 else y - 1
    return f"{start}-{str(start + 1)[2:]}"


def harvest_item(job):
    kind, iso, url, item_id, list_title = job
    session = session_from_date(iso)
    dest = OUT / session / f"dc_{kind}_{item_id}.pdf"
    try:
        page = fetch(url)
        m = re.search(r'citation_pdf_url" content="([^"]+)"', page)
        if not m:
            return None, f"{url}: no pdf link"
        pdf_url = m.group(1).replace("&amp;", "&")
        t = re.search(r'citation_title" content="([^"]+)"', page)
        title = (t.group(1) if t else list_title).strip()
        if not dest.exists():
            blob = fetch(pdf_url, binary=True)
            if not blob.startswith(b"%PDF"):
                return None, f"{url}: not a PDF"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(blob)
        return {"session": session, "type": kind, "title": title, "date": iso,
                "file": f"{session}/{dest.name}", "source_url": url}, None
    except Exception as e:
        return None, f"{url}: {e}"


def main():
    meta = json.loads(META.read_text()) if META.exists() else {"entries": []}
    known = {e["source_url"] for e in meta["entries"]}

    jobs, seen = [], set()
    for kind, listing in LISTINGS:
        text = fetch(listing)
        rows = ROW.findall(text)
        print(f"{listing}: {len(rows)} rows")
        for iso, url, item_id, title in rows:
            url = url.replace("http://", "https://")
            if url in seen or url in known:
                continue
            seen.add(url)
            jobs.append((kind, iso, url, item_id, title))

    print(f"{len(jobs)} new documents to fetch")
    added, failed = [], []
    for i, job in enumerate(jobs, 1):
        entry, err = harvest_item(job)
        if entry:
            added.append(entry)
        else:
            failed.append(err)
        if i % 25 == 0:
            print(f"{i}/{len(jobs)} done, {len(failed)} failed", flush=True)

    meta["entries"].extend(added)
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n")
    total = sum(f.stat().st_size for f in OUT.rglob("*.pdf"))
    print(f"added {len(added)}, {len(failed)} failed, "
          f"{len(meta['entries'])} total entries, {total // 1_000_000} MB on disk")
    if failed:
        print(*failed[:15], sep="\n", file=sys.stderr)


if __name__ == "__main__":
    main()
