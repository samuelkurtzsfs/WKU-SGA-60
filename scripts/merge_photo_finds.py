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

# Said plainly, for a reader rather than a researcher.
QUALITY = {
    "soft": "the only surviving frame of them, and it is not a sharp one",
    "small": "the only surviving frame of them, and it is a small one",
    "group crop": "cropped from a group photograph, the only one of them known",
    "group": "cropped from a group photograph, the only one of them known",
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
    return out


def load_finds():
    rows = []
    for f in sorted(FINDS.glob("*.json")):
        # _worklist files are the job, not the result. -notes files are the
        # sourced facts that fell out of the hunt, a different shape entirely,
        # and reading them here reported thirty-four researcher errors that
        # were nothing of the kind.
        if f.name.startswith("_worklist") or f.name.endswith("-notes.json"):
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


def check(rec, known):
    """Return the reason to refuse this finding, or None to accept it."""
    year, name, fn = rec.get("year"), rec.get("name"), rec.get("file")
    if not (year and name and fn):
        return "missing year, name or file"
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
        near = [n for n in known[year] if fold(n) == fold(name)]
        if near:
            return f"name is spelled {near[0]!r} in {year}, not {name!r}"
        return f"nobody called {name!r} is recorded in {year}"
    return None


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
    overlay = json.loads(OVERLAY.read_text())
    have = {(p["year"], p["name"]): p for p in overlay.get("leaders", [])}

    added, improved, refused = [], [], []
    for origin, rec in finds:
        why = check(rec, known)
        if why:
            refused.append((origin, rec.get("name", "?"), why))
            continue
        key = (rec["year"], rec["name"])
        # A researcher who had to settle marks the finding "soft", "small" or
        # "group crop". The owner would rather have the face than an empty
        # frame, but a reader looking at a poor photograph should be told it
        # is the only one there is, not left wondering. So it goes in the
        # citation the site already prints, and nowhere new.
        label = rec["src"]["label"]
        q = str(rec.get("quality") or "").strip()
        if q and q.lower() not in label.lower():
            label = f"{label} ({QUALITY.get(q.lower(), q)})"
        entry = {"year": rec["year"], "name": rec["name"], "file": rec["file"],
                 "src": {"label": label, "url": rec["src"]["url"]}}
        old = have.get(key)
        if old:
            if old["file"] == rec["file"] and old["src"] == entry["src"]:
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

    overlay["leaders"] = sorted(have.values(),
                                key=lambda p: (p["year"], p["name"]))
    OVERLAY.write_text(json.dumps(overlay, indent=1, ensure_ascii=False) + "\n")
    print(f"\nwrote {OVERLAY}, now {len(overlay['leaders'])} portraits")
    print("now run: python3 scripts/build.py && python3 scripts/check_data.py")


if __name__ == "__main__":
    main()
