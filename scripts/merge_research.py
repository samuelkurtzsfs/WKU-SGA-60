#!/usr/bin/env python3
"""
Merge verified workflow research into data/years.json.

Reads the journals of the two research workflows, pairs research results with
their fact-check verdicts, and merges: events and profile paragraphs whose
verdict is claim_not_found or contradicted are dropped; supported and (for now)
unverified items are merged; anything already present is skipped. Also PRUNES
previously merged items that a newly arrived verdict rejects. Statuses are
recomputed. Run scripts/build.py afterwards.

Usage: python3 scripts/merge_research.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WF = Path.home() / (".claude/projects/-Users-samkurtz/d305ae30-4294-46a3-abb0-409743beff17"
                    "/subagents/workflows")
JOURNALS = [WF / "wf_2cd5c72a-c1c/journal.jsonl", WF / "wf_ad3dd308-d04/journal.jsonl"]
BAD = ("claim_not_found", "contradicted")


def load(journal):
    research, verdicts, pre_verdicts = {}, {}, []
    if not journal.exists():
        return research, verdicts, pre_verdicts
    for line in journal.open():
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get("type") != "result":
            continue
        v = r.get("result")
        if isinstance(v, str):
            try:
                v = json.loads(v)
            except Exception:
                continue
        if not isinstance(v, dict):
            continue
        if "years" in v:                      # pre-2000 batch research
            for y in v["years"]:
                research[y["year"]] = y
        elif "items" in v:                    # pre-2000 batch verdicts
            pre_verdicts.extend(v["items"])
        elif "events" in v and "profiles" in v and "year" in v:
            research[v["year"]] = v
        elif "paragraphs" in v and "year" in v:
            verdicts[v["year"]] = v
    return research, verdicts, pre_verdicts


def main():
    research, verdicts, pre_items = {}, {}, []
    for j in JOURNALS:
        r, v, p = load(j)
        research.update(r)
        verdicts.update(v)
        pre_items.extend(p)
    # fold pre-2000 verdict items into the same per-year shape
    for it in pre_items:
        y = verdicts.setdefault(it["year"], {"events": [], "paragraphs": []})
        if it["kind"] == "event":
            y["events"].append({"title": it["key"], "verdict": it["verdict"]})
        else:
            name, _, idx = it["key"].rpartition("#")
            y["paragraphs"].append({"name": name, "index": int(idx or 0),
                                    "verdict": it["verdict"]})

    data = json.loads((ROOT / "data/years.json").read_text())
    by_id = {y["id"]: y for y in data["years"]}
    added = pruned = 0

    for yid, r in sorted(research.items()):
        y = by_id.get(yid)
        if not y:
            continue
        v = verdicts.get(yid)
        ev_v = {e["title"]: e["verdict"] for e in v["events"]} if v else {}
        par_v = {(p["name"], p["index"]): p["verdict"] for p in v["paragraphs"]} if v else {}

        # prune already-merged items that a verdict now rejects
        bad_titles = {t for t, vd in ev_v.items() if vd in BAD}
        before = len(y["events"])
        y["events"] = [e for e in y["events"] if e["title"] not in bad_titles]
        pruned += before - len(y["events"])

        existing = {e["title"].strip().lower() for e in y["events"]}
        for e in r.get("events", []):
            t = e["title"].strip()
            if t.lower() in existing or ev_v.get(t) in BAD:
                continue
            ne = {"date": e["date"], "title": t, "body": e["body"],
                  "src": {"label": e["src"]["label"], "url": e["src"]["url"]}}
            if e.get("campus"):
                ne["campus"] = True
            y["events"].append(ne)
            existing.add(t.lower())
            added += 1

        for prof in r.get("profiles", []):
            for l in y["leaders"]:
                if l["name"] != prof["name"]:
                    continue
                paras = l.get("profile") or []
                srcs = l.get("sources") or []
                have = {s.get("url") for s in srcs}
                for i, p in enumerate(prof["paragraphs"]):
                    if par_v.get((prof["name"], i)) in BAD:
                        if p["text"] in paras:
                            paras.remove(p["text"])
                            pruned += 1
                        continue
                    if p["text"] not in paras:
                        paras.append(p["text"])
                        added += 1
                    if p["src"]["url"] not in have:
                        srcs.append({"label": p["src"]["label"], "url": p["src"]["url"]})
                        have.add(p["src"]["url"])
                if paras:
                    l["profile"] = paras
                l["sources"] = srcs

        n = len(y["events"])
        y["status"] = "researched" if n >= 3 else ("partial" if n else "empty")

    (ROOT / "data/years.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    print(f"merged: +{added} items, pruned {pruned} rejected items")


if __name__ == "__main__":
    main()
