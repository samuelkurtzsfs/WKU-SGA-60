#!/usr/bin/env python3
"""Fold the photograph agents' findings into data/photos.json.

    python3 scripts/merge_photo_finds.py            # show what would change
    python3 scripts/merge_photo_finds.py --write    # write it

Twelve agents hunt portraits, one per five-year block, and none of them may
touch photos.json: they drop a findings file in data/photo-finds/ and put the
image in data/photos/. This merges those drops.

The check that matters is the last one. The build attaches a portrait by exact
year and exact name, and when either is wrong it attaches the photograph to
nobody, silently, and the year looks the same as before. So every finding is
tested against the people actually recorded in that year before it is written.
"""

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FINDS = ROOT / "data" / "photo-finds"
PHOTOS = ROOT / "data" / "photos"
YEARS = ROOT / "data" / "years.json"
OVERLAY = ROOT / "data" / "photos.json"

MAGIC = {b"\xff\xd8": "jpeg", b"\x89P": "png"}

# Short. A citation is not the place for an apology about the picture, and a
# sentence explaining that this is the only surviving frame reads like padding.
QUALITY = {
    "soft": "only picture found",
    "small": "only picture found",
    "masked": "only picture found",
    "group crop": "cropped from a group photo",
    "group": "cropped from a group photo",
}


def fold(s):
    """For telling a near miss from a real one when a name does not match."""
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s.lower())


def people_by_year(doc):
    """Everyone the archive records in each year, however they served."""
    out = defaultdict(set)
    for y in doc["years"]:
        for l in y.get("leaders", []):
            out[y["id"]].add(l["name"])
        org = y.get("organization") or {}
        sen = org.get("senate") or {}
        for lst in ((org.get("executive") or []), (sen.get("officers") or []),
                    (sen.get("members") or [])):
            for e in lst:
                if e.get("name"):
                    out[y["id"]].add(e["name"])
        # A committee record names the committee; its chair is a separate
        # field. The site draws chairs into the roster and shows their faces,
        # so a portrait of somebody whose only office that year was a
        # chairmanship has to be allowed to attach.
        for c in (sen.get("committees") or []):
            if c.get("chair"):
                out[y["id"]].add(c["chair"])
    return out


def load_finds():
    rows = []
    for f in sorted(FINDS.glob("*.json")):
        # Only the findings files are findings. A leading underscore marks the
        # drop box's own bookkeeping, the worklists and the record of archive
        # gaps; -notes files hold sourced facts that fell out of the hunt.
        # Both are shaped differently, and reading them as portraits once
        # reported thirty-four researcher errors that were nothing of the kind.
        if f.name.startswith("_") or f.name.endswith("-notes.json"):
            continue
        try:
            got = json.loads(f.read_text())
        except (json.JSONDecodeError, OSError) as e:
            print(f"  !! {f.name}: unreadable, skipped ({e})")
            continue
        if not isinstance(got, list):
            print(f"  !! {f.name}: not a list, skipped")
            continue
        rows.extend((f.name, r) for r in got if isinstance(r, dict))
        print(f"  {f.name}: {len(got)}")
    return rows


def barred():
    """Photographs an editor has withdrawn, keyed by the frame, not the person.

    The register was advisory: researchers were told to read it and mostly did,
    but nothing stopped a later pass re-finding the same frame and offering it
    again. Two withdrawn faces were back this morning.

    It has to key on the URL rather than the name. Almost every entry rejects a
    particular photograph, not a person: Kaison Barton is barred from a track
    and field frame and is published from a good one taken at the lectern, and
    barring him by name would quietly delete the portrait he has. Only a URL
    can tell those apart. Entries that describe a frame in prose with no link
    stay advisory, which is what the brief tells researchers to read them as.
    """
    p = FINDS / "_do-not-use.json"
    if not p.is_file():
        return {}
    try:
        rows = json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    out = {}
    for r in rows:
        if not isinstance(r, dict):
            continue
        for field in ("url", "file"):
            v = str(r.get(field) or "")
            if v.startswith("http"):
                out[v.strip()] = (r.get("name", "?"),
                                  r.get("reason") or "withdrawn by an editor")
    return out


def check(rec, known, no=None):
    """Return the reason to refuse this finding, or None to accept it."""
    year, name, fn = rec.get("year"), rec.get("name"), rec.get("file")
    if not (year and name and fn):
        return "missing year, name or file"
    url = str((rec.get("src") or {}).get("url") or "").strip()
    if no and url in no:
        return f"withdrawn frame: {no[url][1][:88]}"
    src = rec.get("src") or {}
    if not str(src.get("url", "")).startswith("http") or not src.get("label"):
        return "no usable source"

    path = PHOTOS / fn
    if not path.is_file():
        return f"{fn} is not in data/photos/"
    head = path.open("rb").read(2)
    if head not in MAGIC:
        return f"{fn} is not an image (starts {head!r})"

    if year not in known:
        return f"{year} is not a year in the archive"
    if name not in known[year]:
        if resolve(name, year, known):
            return None
        near = [n for n in known[year] if fold(n) == fold(name)]
        if near:
            return f"name is spelled {near[0]!r} in {year}, not {name!r}"
        return f"nobody called {name!r} is recorded in {year}"
    return None


def resolve(name, year, known):
    """The archive's own spelling of this person, or None if it cannot tell.

    A researcher writes Carmen Willoughby; the archive files her as Carmen Ann
    Willoughby in the year she was secretary. Refusing that helps nobody, and
    correcting it by hand does not stick, because the researcher rewrites the
    findings file after every person and puts their spelling back.

    So it is resolved here, and only when there is no room to be wrong: the
    given name and the surname must both match, and exactly one person in that
    year may match. Two Deborah Clarks in one year resolve to nothing, which is
    the right answer.
    """
    if name in known.get(year, ()):
        return name
    # fold() drops spaces along with the punctuation, so the words have to be
    # separated before it runs or every name collapses to a single token
    words = lambda s: [fold(w) for w in str(s).split() if fold(w)]
    a = words(name)
    if len(a) < 2:
        return None
    hits = []
    for other in known.get(year, ()):
        b = words(other)
        if len(b) >= 2 and a[0] == b[0] and a[-1] == b[-1]:
            hits.append(other)
    return hits[0] if len(hits) == 1 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    print("reading findings")
    finds = load_finds()
    if not finds:
        print("nothing dropped yet")
        return

    known = people_by_year(json.loads(YEARS.read_text()))
    no = barred()
    if no:
        print(f"{len(no)} withdrawn photographs on record, matched by url")
    overlay = json.loads(OVERLAY.read_text())
    have = {(p["year"], p["name"]): p for p in overlay.get("leaders", [])}

    # Two researchers working neighbouring decades can both find a portrait of
    # the same person, from different photographs, and both be right. Whichever
    # was read last used to win, so the file flipped back and forth on every
    # run. Settle it once, on the rule the owner gave: the bigger frame.
    def pixels(rec):
        w, h = rec.get("width") or 0, rec.get("height") or 0
        if w and h:
            return int(w) * int(h)
        p = PHOTOS / str(rec.get("file") or "")
        return p.stat().st_size if p.is_file() else 0

    best = {}
    for origin, rec in finds:
        k = (rec.get("year"), rec.get("name"))
        if k not in best or pixels(rec) > pixels(best[k][1]):
            best[k] = (origin, rec)
    if len(best) < len(finds):
        print(f"{len(finds) - len(best)} findings were duplicates; kept the "
              f"largest frame of each")
    finds = list(best.values())

    added, improved, refused = [], [], []
    for origin, rec in finds:
        why = check(rec, known, no)
        if why:
            refused.append((origin, rec.get("name", "?"), why))
            continue
        # write it under the name the archive knows, or the
        # build attaches the face to nobody
        recorded = resolve(rec["name"], rec["year"], known) or rec["name"]
        key = (rec["year"], recorded)
        # A researcher who had to settle marks the finding "soft", "small" or
        # "group crop". The owner would rather have the face than an empty
        # frame, but a reader looking at a poor photograph should be told it
        # is the only one there is, not left wondering. So it goes in the
        # citation the site already prints, and nowhere new.
        label = rec["src"]["label"]
        q = str(rec.get("quality") or "").strip()
        if q and q.lower() not in label.lower():
            label = f"{label} ({QUALITY.get(q.lower(), q)})"
        entry = {"year": rec["year"], "name": recorded, "file": rec["file"],
                 "src": {"label": label, "url": rec["src"]["url"]}}
        old = have.get(key)
        if old:
            if old["file"] == rec["file"] and old["src"] == entry["src"]:
                continue
            # An editor working after the researcher writes the identifying
            # reasoning into the citation: which row of the group photograph,
            # how the count was done. The finding still holds the short label
            # it was filed with, so re-merging the same finding would truncate
            # all that back off. If the label on file already contains the
            # finding's own, it has been enriched, and it stays.
            if (old["file"] == rec["file"]
                    and old["src"].get("url") == entry["src"]["url"]
                    and label in old["src"].get("label", "")):
                continue
            improved.append((key, old["file"], rec["file"],
                             rec.get("why", "")))
        else:
            added.append((key, rec["file"], rec.get("why", "")))
        have[key] = entry

    print()
    print(f"{len(added)} portraits would be added")
    for (yr, name), fn, why in sorted(added):
        print(f"  {yr}  {name:26s} {fn}")
        if why:
            print(f"              {why[:96]}")
    print()
    print(f"{len(improved)} would be replaced with a better frame")
    for (yr, name), oldf, newf, why in sorted(improved):
        print(f"  {yr}  {name:26s} {oldf} -> {newf}")
        if why:
            print(f"              {why[:96]}")
    if refused:
        print()
        print(f"{len(refused)} refused")
        for origin, name, why in sorted(refused):
            print(f"  {origin}: {name} - {why}")

    if not args.write:
        print("\nthis was a dry run. add --write to apply it.")
        return
    if not (added or improved):
        print("\nnothing to write")
        return

    # A researcher who finds a better frame files it under a new name and
    # deletes the old file, which leaves the overlay pointing at something
    # that is no longer there and the site rendering a broken image. Worse
    # than no portrait, and invisible until someone looks at the page.
    missing = [p for p in have.values() if not (PHOTOS / p["file"]).is_file()]
    for p in missing:
        print(f"  dropped {p['name']} ({p['year']}): {p['file']} is gone")
        del have[(p["year"], p["name"])]
    if missing:
        print(f"{len(missing)} entries pointed at files that no longer exist")

    overlay["leaders"] = sorted(have.values(),
                                key=lambda p: (p["year"], p["name"]))
    OVERLAY.write_text(json.dumps(overlay, indent=1, ensure_ascii=False) + "\n")
    print(f"\nwrote {OVERLAY}, now {len(overlay['leaders'])} portraits")
    print("now run: python3 scripts/build.py && python3 scripts/check_data.py")


if __name__ == "__main__":
    main()
