#!/usr/bin/env python3
"""
Check data/years.json against the rules this archive says it keeps.

The failure this guards against is not a crash. It is a script that reports
success while quietly producing something wrong: a harvest that wrote an empty
file and printed "done", a merge that dropped a field nobody was reading, an
edit that left two entries describing one event. Those survive because nothing
looks. This looks.

Exit status is 1 if anything is wrong, so it can gate a deploy.

    python3 scripts/check_data.py            everything
    python3 scripts/check_data.py --quiet    only the failures
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROLES = {"president", "regent", "unresolved"}
KINDS = {"concert", "speaker", "film", "festival", "tradition",
         "service", "program", "other"}
DATE = re.compile(r"\d{4}-\d{2}-\d{2}$")
YEAR_ID = re.compile(r"\d{4}-\d{2}$")

problems = []
notes = []


def bad(msg):
    problems.append(msg)


def note(msg):
    notes.append(msg)


def check_years(ys):
    ids = [y["id"] for y in ys]
    for yid in ids:
        if not YEAR_ID.match(yid):
            bad(f"year id is not YYYY-YY: {yid}")
    for a, b in zip(ys, ys[1:]):
        if b["start"] != a["start"] + 1:
            bad(f"a year is missing between {a['id']} and {b['id']}")
    if len(set(ids)) != len(ids):
        bad("two years share an id: "
            + ", ".join(k for k, v in Counter(ids).items() if v > 1))


def check_events(ys):
    for y in ys:
        seen = Counter()
        for e in y["events"]:
            where = f"{y['id']} \"{e.get('title', '')[:48]}\""
            if not str(e.get("title", "")).strip():
                bad(f"{y['id']}: an event has no title")
            if not str(e.get("body", "")).strip():
                bad(f"{where}: no body")
            d = str(e.get("date", ""))
            if not DATE.match(d):
                bad(f"{where}: date {d!r} is not YYYY-MM-DD")
            elif not (y["start"] <= int(d[:4]) <= y["start"] + 2):
                bad(f"{where}: dated {d}, outside {y['id']}")
            src = e.get("src") or {}
            if not src.get("url") or not src.get("label"):
                bad(f"{where}: no source. The rule is no source, no entry")
            if e.get("kind") and e["kind"] not in KINDS:
                bad(f"{where}: kind {e['kind']!r} is not one of {sorted(KINDS)}")
            if e.get("campus") and e.get("kind"):
                bad(f"{where}: tagged campus context and also a programme SGA put on")
            seen[e.get("title", "").strip().lower()] += 1
        for t, n in seen.items():
            if n > 1:
                bad(f"{y['id']}: {n} events share the title \"{t[:52]}\"")


def check_leaders(ys):
    for y in ys:
        for l in y["leaders"]:
            who = f"{y['id']} {l.get('name', '?')}"
            if not str(l.get("name", "")).strip():
                bad(f"{y['id']}: a leader has no name")
            if l.get("role") not in ROLES:
                bad(f"{who}: role {l.get('role')!r} is not one of {sorted(ROLES)}")
            if "also_regent" in l and l["role"] != "president":
                bad(f"{who}: also_regent is only meaningful on a president")
            if l.get("acting") and l["role"] != "president":
                bad(f"{who}: acting is only meaningful on a president")
            for s in l.get("sources") or []:
                if not s.get("url") or not s.get("label"):
                    bad(f"{who}: a source is missing its label or url")
        # a year with more than one name cannot infer who held the Board seat
        pres = [l for l in y["leaders"] if l["role"] == "president"]
        if len(y["leaders"]) > 1 and y["start"] >= 1967:
            for l in pres:
                if "also_regent" not in l:
                    bad(f"{y['id']} {l['name']}: more than one name this year, so "
                        f"also_regent has to be stated, not guessed")


def check_seat(ys):
    def held_both(l, y):
        if l["role"] != "president":
            return False
        if "also_regent" in l:
            return bool(l["also_regent"])
        return len(y["leaders"]) == 1 and y["start"] >= 1967
    for y in ys:
        if y["start"] < 1967:
            continue
        if not any(l["role"] == "regent" or held_both(l, y) for l in y["leaders"]):
            note(f"{y['id']}: nobody is recorded in the student seat on the Board")


def is_pdf(path):
    try:
        with open(path, "rb") as fh:
            return fh.read(4) == b"%PDF"
    except OSError:
        return False


def is_image(path):
    try:
        with open(path, "rb") as fh:
            head = fh.read(8)
        return head[:2] == b"\xff\xd8" or head[:8] == b"\x89PNG\r\n\x1a\n"
    except OSError:
        return False


def check_files(ys):
    """A file that is present is not the same as a file that is what it claims.
    TopSCHOLAR answers a blocked download with an HTML page and HTTP 202, which
    lands on disk named .pdf and reads as a successful mirror until someone
    opens it."""
    docs = ROOT / "data" / "documents"
    photos = ROOT / "data" / "photos"

    def want_pdf(where, f):
        path = docs / f
        if not path.exists():
            bad(f"{where}: file missing: {f}")
        elif not is_pdf(path):
            bad(f"{where}: {f} is not a PDF. A blocked download saves the "
                f"bot-check page under the right name")

    for y in ys:
        for d in y.get("documents") or []:
            if d.get("file"):
                want_pdf(y["id"], d["file"])
        for e in y["events"]:
            f = (e.get("src") or {}).get("file")
            if f:
                want_pdf(f"{y['id']} \"{e.get('title','')[:40]}\"", f)
        for p in y.get("photos") or []:
            if not p.get("file"):
                continue
            path = photos / p["file"]
            if not path.exists():
                bad(f"{y['id']}: photograph missing: {p['file']}")
            elif not is_image(path):
                bad(f"{y['id']}: {p['file']} is not a JPEG or PNG")
        for l in y["leaders"]:
            ph = (l.get("photo") or {}).get("file")
            if ph and not (photos / ph).exists():
                bad(f"{y['id']} {l['name']}: portrait missing: {ph}")
            elif ph and not is_image(photos / ph):
                bad(f"{y['id']} {l['name']}: portrait {ph} is not a JPEG or PNG")


def check_photos(ys):
    """The photo overlay in data/photos.json is keyed by name and year, so
    correcting a name or moving a term silently detaches the portrait. That has
    happened, so it is checked: an entry naming somebody the archive no longer
    has is almost always a rename nobody followed through."""
    path = ROOT / "data" / "photos.json"
    if not path.exists():
        return
    overlay = json.loads(path.read_text())
    live = {(l["name"], y["id"]) for y in ys for l in y["leaders"]}
    names = {l["name"] for y in ys for l in y["leaders"]}
    for y in ys:
        org = y.get("organization") or {}
        for o in (org.get("executive") or []):
            live.add((o.get("name"), y["id"]))
            names.add(o.get("name"))
        senate = org.get("senate") or {}
        for o in (senate.get("officers") or []):
            live.add((o.get("name"), y["id"]))
            names.add(o.get("name"))
        for m in (senate.get("members") or []):
            live.add((m.get("name"), y["id"]))
            names.add(m.get("name"))
        # A committee record names the committee; the person is in `chair`.
        # They hold an office and the roster gives them a page, so a portrait
        # of them is legitimate and must not be reported as attaching to
        # nobody.
        for c in (senate.get("committees") or []):
            if c.get("chair"):
                live.add((c["chair"], y["id"]))
                names.add(c["chair"])
    photos = ROOT / "data" / "photos"
    for e in overlay.get("leaders", []):
        who, when = e.get("name"), e.get("year")
        if e.get("file") and not (photos / e["file"]).exists():
            bad(f"photos.json: image missing for {who}: {e['file']}")
        if who not in names:
            bad(f"photos.json names {who!r}, who is not in the archive. If a name "
                f"was corrected, the overlay has to be corrected with it or the "
                f"portrait detaches")
        elif (who, when) not in live:
            bad(f"photos.json puts {who!r} in {when}, where the archive does not "
                f"have them; the portrait will not attach")
    # The same name in the same year twice. The build renders such a pair once,
    # so nothing shows on the site, which is exactly why it goes unnoticed: what
    # it corrupts is the count of how many portraits the archive holds, and a
    # run that trusts that count reports progress it did not make. It happens
    # when a research branch adds a portrait that has already landed on main by
    # another route: merging main in does not dedupe an entry the branch is
    # about to write. Caught by hand on 4 September, when
    # a second copy of Carmen Ann Willoughby's 1966-67 portrait reached a pull
    # request. Compared on the exact name and not through name-aliases.json,
    # because one image deliberately carries an entry under each name form the
    # archive uses for the person — Jim Haynes and James P. Haynes both need one
    # in 1966-67 or the portrait detaches from the roster or from the year page.
    seen = {}
    for e in overlay.get("leaders", []):
        key = (e.get("name"), e.get("year"))
        if key in seen:
            bad(f"photos.json attaches two portraits to {key[0]!r} in {key[1]} "
                f"({seen[key]} and {e.get('file')}). One name, one year, one "
                f"entry: check photos.json for the year and name before adding, "
                f"not just the worklist")
        seen[key] = e.get("file")

    # The Spirit Masters scrapbooks are catalogued UA12/2/16. UA68 is SGA's own
    # record group, and portrait passes have written it over the correction
    # three times now (settled 3 September, put back by a rebuild, restored,
    # put back again on 4 September). The archive's own titles decide it: every
    # scanned volume on TopSCHOLAR is titled "UA12/2/16 Spirit Masters
    # Scrapbook" and none carries UA68 anywhere.
    for sec in ("leaders", "years"):
        for e in overlay.get(sec, []):
            src = e.get("src") or {}
            if "UA68" in (src.get("label") or "") and "stu_org" in (src.get("url") or ""):
                bad(f"photos.json credits a Student Organizations volume to UA68 "
                    f"({e.get('name') or e.get('file')}, {e.get('year')}). The "
                    f"Spirit Masters scrapbooks are UA12/2/16; UA68 is SGA's own "
                    f"record group and has been written over this correction "
                    f"three times")

    withpic = {(e.get("name"), e.get("year")) for e in overlay.get("leaders", [])}
    missing = [f"{y['id']} {l['name']}" for y in ys for l in y["leaders"]
               if (l["name"], y["id"]) not in withpic]
    if missing:
        note(f"{len(missing)} leaders have no portrait: " + ", ".join(missing[:8])
             + (" ..." if len(missing) > 8 else ""))


def check_counts(ys):
    n_ev = sum(len(y["events"]) for y in ys)
    pres = {l["name"] for y in ys for l in y["leaders"] if l["role"] == "president"}
    note(f"{len(ys)} years, {n_ev} events, {len(pres)} people have been president")
    for y in ys:
        n = len(y["events"])
        want = "researched" if n >= 3 else ("partial" if n else "empty")
        if y.get("status") != want:
            bad(f"{y['id']}: status is {y.get('status')!r} but it has {n} events "
                f"so it should be {want!r}")


def main(argv):
    quiet = "--quiet" in argv
    data = json.loads((ROOT / "data" / "years.json").read_text())
    ys = data["years"]
    for fn in (check_years, check_events, check_leaders, check_seat,
               check_files, check_photos, check_counts):
        fn(ys)

    if not quiet:
        for n in notes:
            print(f"  {n}")
    if problems:
        print(f"\n{len(problems)} problems:")
        for p in problems:
            print(f"  ! {p}")
        return 1
    print("\nthe archive checks out against its own rules")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
