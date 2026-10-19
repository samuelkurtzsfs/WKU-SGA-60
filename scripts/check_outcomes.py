"""Flag events that state an outcome their bill sheet does not record.

An SGA bill sheet carries First Reading, Second Reading, then Pass / Fail /
Other. Entries have repeatedly taken a sheet whose outcome lines are empty and
written the measure up as though it had carried: six were corrected on
18 October 2026, four more the same day, and each was found by a random sample
landing on it rather than by anything mechanical.

This is the mechanical part. For every event citing a bill sheet the archive
holds, it reads the outcome lines off the page and compares them against the
voice the entry is written in. It decides nothing. A blank line in the text
layer is a lead and never a finding: a handwritten tick is not in the text
layer at all, and bills 03-04-F and 04-07-S read blank here while visibly
carrying one. Render the page and look at it before changing a word.

    python3 scripts/check_outcomes.py            # the leads
    python3 scripts/check_outcomes.py --all      # every matched event
"""

import json
import os
import re
import subprocess
import sys
from xml.etree import ElementTree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGISLATION = os.path.join(ROOT, "data", "legislation")

# The outcome labels, as the sheets print them.
LABELS = ("pass", "fail", "other")

# Words that are part of the furniture rather than a recorded outcome.
NOT_A_MARK = {"reading", "first", "second", "pass", "fail", "other", "date", "vote"}

# A lone bullet or comma sitting on an outcome line is a stray glyph, not a
# record of anything: bills 03-04-F and 04-07-S carry one each and both are
# blank sheets that visibly bear a handwritten tick. Counting them as marks
# suppressed the lead. A mark has to carry a letter or a digit.
def is_a_mark(text):
    token = text.strip().strip(":")
    if not token or token.lower() in NOT_A_MARK:
        return False
    return bool(re.search(r"[0-9A-Za-z]", token))

# Sheets whose outcome has been read off the page image, where the text layer
# cannot see it. A handwritten tick and a rubber stamp are both invisible to
# pdftotext, so without this list the same sound entries come back as leads
# every run and the real ones get lost among them. Only add a sheet here after
# looking at the rendered page, and say what you saw.
READ_BY_EYE = {
    "1994-95/dc_bill_77.pdf": "tick on the Pass line and a PASSED stamp (19 Oct 2026)",
    "2003-04/dc_bill_201.pdf": "handwritten tick on the Pass line (19 Oct 2026)",
    "2003-04/dc_bill_203.pdf": "handwritten tick on the Pass line (19 Oct 2026)",
    "2003-04/dc_bill_207.pdf": "handwritten tick on the Pass line, per the handoff",
}

# A finished verb over a sheet that records no outcome is the shape of the
# defect. These are the ones the corrected entries were using.
FINISHED = re.compile(
    r"\b("
    r"passed|carried|adopted|approved|enacted|ratified"
    r"|allocated|funded|appropriated|granted|awarded|paid|spent|bought|purchased"
    r"|put|raised|returned|created|established|installed|launched|held"
    r"|gave|sent|placed|added|set up|brought"
    r")\b",
    re.I,
)

# An entry already written to its record says so. These are the hedges the
# rewritten entries use, and a body carrying one is not a lead.
HEDGED = re.compile(
    r"\b("
    r"leaves? the (second reading|pass|outcome)"
    r"|outcome lines? (are |is )?blank"
    r"|blank"
    r"|no source .{0,40}records? the outcome"
    r"|does not record"
    r"|never recorded"
    r"|whether .{0,30}(went ahead|passed|carried)"
    r"|proposed (allocating|that)"
    r"|sought"
    r"|would (have )?(allocate|fund|pay|buy|create)"
    r")\b",
    re.I,
)


def words_on_page(pdf):
    """Every word on page one, as (text, yMin, yMax, xMin, xMax)."""
    try:
        out = subprocess.run(
            ["pdftotext", "-bbox-layout", "-f", "1", "-l", "1", pdf, "-"],
            capture_output=True, timeout=60,
        ).stdout
    except (subprocess.TimeoutExpired, OSError):
        return None
    if not out:
        return None
    try:
        tree = ElementTree.fromstring(out)
    except ElementTree.ParseError:
        return None
    ns = "{http://www.w3.org/1999/xhtml}"
    words = []
    for w in tree.iter(ns + "word"):
        text = (w.text or "").strip()
        if not text:
            continue
        words.append((
            text,
            float(w.get("yMin")), float(w.get("yMax")),
            float(w.get("xMin")), float(w.get("xMax")),
        ))
    return words


def rows_of(words):
    """Group words into visual rows, left to right.

    The sheets are scans, and the OCR breaks labels into fragments: 'Pass:'
    arrives as 'Pa' + 'ss:' and 'Fail:' as 'Fa' + 'il:'. Matching word by word
    found neither, so a sheet whose Pass line was filled in read as empty.
    Rows are grouped by vertical midpoint instead, and the label is matched
    against the row's joined text.
    """
    rows = []
    for word in sorted(words, key=lambda w: (w[1] + w[2]) / 2):
        text, ymin, ymax, xmin, xmax = word
        mid = (ymin + ymax) / 2
        height = max(ymax - ymin, 1.0)
        for row in rows:
            if abs(row["mid"] - mid) <= height * 0.6:
                row["words"].append(word)
                row["mid"] = sum((w[1] + w[2]) / 2 for w in row["words"]) / len(row["words"])
                break
        else:
            rows.append({"mid": mid, "words": [word]})
    for row in rows:
        row["words"].sort(key=lambda w: w[3])
    return rows


def outcome_of(pdf):
    """Read the Pass / Fail / Other lines.

    Returns (state, detail). state is 'marked' when something sits on one of
    those lines, 'blank' when all three are empty, 'no-lines' when the sheet
    has no such lines at all, and 'unreadable' when the page has no text layer.
    """
    words = words_on_page(pdf)
    if not words:
        return "unreadable", ""

    found, saw_label = [], False
    for row in rows_of(words):
        joined = "".join(w[0] for w in row["words"])
        squashed = re.sub(r"[^0-9a-z]", "", joined.lower())
        label = next((l for l in LABELS if squashed.startswith(l)), None)
        if not label:
            continue
        # 'Other' must not swallow a line of prose that merely opens with it.
        saw_label = True
        rest = squashed[len(label):]
        if not rest:
            continue
        # Rebuild the text after the label so the detail is readable.
        tail, consumed = [], 0
        for w in row["words"]:
            token = re.sub(r"[^0-9A-Za-z]", "", w[0])
            if consumed < len(label):
                consumed += len(token)
                continue
            tail.append(w[0])
        value = " ".join(tail).strip(" :_-")
        if is_a_mark(value):
            found.append("%s = %s" % (label, value))

    if not saw_label:
        return "no-lines", ""
    if found:
        return "marked", "; ".join(dict.fromkeys(found))
    return "blank", "all three lines empty in the text layer"


def main():
    show_all = "--all" in sys.argv

    years = json.load(open(os.path.join(ROOT, "data", "years.json")))["years"]
    entries = json.load(open(os.path.join(ROOT, "data", "legislation.json")))["entries"]
    by_url = {e["source_url"]: e for e in entries if e.get("source_url")}

    cache = {}
    leads, checked = [], 0

    for year in years:
        for event in year.get("events", []):
            sources = [event.get("src"), event.get("src2")] + (event.get("srcs") or [])
            sheet = None
            for source in sources:
                if source and by_url.get(source.get("url", "")):
                    sheet = by_url[source["url"]]
                    break
            if not sheet:
                continue
            pdf = os.path.join(LEGISLATION, sheet["file"])
            if not os.path.exists(pdf):
                continue
            if pdf not in cache:
                if sheet["file"] in READ_BY_EYE:
                    cache[pdf] = ("marked", READ_BY_EYE[sheet["file"]])
                else:
                    cache[pdf] = outcome_of(pdf)
            state, detail = cache[pdf]
            checked += 1

            prose = "%s %s" % (event.get("title", ""), event.get("body", ""))
            verb = FINISHED.search(prose)
            hedged = HEDGED.search(prose)

            flagged = state in ("blank", "unreadable") and verb and not hedged
            if flagged or show_all:
                leads.append({
                    "year": year.get("id"), "date": event.get("date"),
                    "title": event.get("title", ""), "sheet": sheet["file"],
                    "state": state, "detail": detail,
                    "verb": verb.group(0) if verb else "",
                    "hedged": bool(hedged), "flagged": flagged,
                })

    print("%d events cite a bill sheet this archive holds" % checked)
    states = {}
    for pdf, (state, _d) in cache.items():
        states[state] = states.get(state, 0) + 1
    print("  sheets read: " + ", ".join("%s %d" % (k, v) for k, v in sorted(states.items())))

    flagged = [l for l in leads if l["flagged"]]
    if show_all:
        for l in leads:
            mark = "FLAG" if l["flagged"] else "    "
            print("%s %s  %s  %s" % (mark, l["year"], l["date"], l["title"][:62]))
            print("       %s -> %s %s" % (l["sheet"], l["state"], l["detail"][:70]))
        print()

    if not flagged:
        print("\nno event states an outcome its sheet leaves blank")
        return 0

    print("\n%d lead(s). A blank text layer is not a blank page: a handwritten" % len(flagged))
    print("tick does not appear here. Render the sheet and look at it.\n")
    for l in flagged:
        print("%s  %s" % (l["year"], l["date"]))
        print("   %s" % l["title"])
        print("   sheet   data/legislation/%s" % l["sheet"])
        print("   outcome %s - %s" % (l["state"], l["detail"]))
        print("   voice   \"%s\"" % l["verb"])
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
