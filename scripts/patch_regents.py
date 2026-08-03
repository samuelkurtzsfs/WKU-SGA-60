#!/usr/bin/env python3
"""Applies the president-vs-regent findings from the Herald article index."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "years.json"
d = json.loads(P.read_text())
Y = {y["id"]: y for y in d["years"]}

# name -> (year id, role, confidence, note)
ROLES = {
 "William Menser": ("1967-68","president","confirmed",
   "ASG president 1967-68. On 4 April 1968 the Herald reported he 'assumes duties as Regent Board Member' "
   "- making him WKU's first student regent, two months after the enabling bill was reported in committee. "
   "The seat was non-voting at first."),
 "Michael Fiorella": ("1972-73","regent","confirmed",
   "Student regent, not president. Sworn in 26 September 1972 alongside gubernatorial appointees Gerald Edds "
   "and Chalmer Embry, who Gov. Wendell Ford had named the previous month."),
 "Edward Jordan, Jr.": ("1972-73","president","likely",
   "Paired on the plaque with Michael Fiorella, who is confirmed as the student regent that year - so Jordan "
   "is the president by elimination. Confirm with April 1972 Herald election coverage."),
 "Gregory McKinney": ("1974-75","regent","confirmed",
   "Student regent, not president. Sworn in 19 June 1974 as WKU's first African American student regent."),
 "Jeffrey Consolo": ("1974-75","president","confirmed",
   "ASG president. The Herald of 1974 reports 'Jeff Consolo Tabs Eight for Congress' - a president making "
   "appointments to the Associated Student Congress."),
 "Sandra Norfleet": ("1982-83","regent","confirmed",
   "Student regent, not president. Election reported in the Herald, 18 February 1982."),
 "Paul Gerard, III": ("1968-69","regent","likely",
   "Two-year plate reading 1968-70, immediately after William Menser took the first student regent seat in "
   "April 1968. Almost certainly the second student regent. Early student regents were non-voting "
   "'associate regents', which may explain the longer term. Not yet confirmed."),
 "Robert Moore": ("1977-78","president","confirmed",
   "Elected ASG president by a 26-vote margin, reported 15 April 1977."),
 "Christy Mollozzi": ("1976-77","president","likely",
   "The outgoing president who 'congratulates voters' in the 15 April 1977 Herald is Christy Vogt, and a "
   "Christy Vogt letter dated 26 April 1977 sits in the SGA document series. Vogt and Mollozzi are very "
   "likely the same person under maiden and married names. Confirm before merging."),
}

moved = 0
for y in d["years"]:
    for l in y["leaders"]:
        if l["name"] in ROLES:
            tgt, role, conf, note = ROLES[l["name"]]
            l["role"] = role
            l["year_confidence"] = conf
            l["name_verified"] = (conf == "confirmed")
            l["note"] = note
            if y["id"] != tgt and tgt in Y:
                Y[tgt]["leaders"].append(l); y["leaders"].remove(l); moved += 1
                print(f"  moved {l['name']}: {y['id']} -> {tgt}")

NEW = {
 "1967-68": [
  {"date":"1968-02-08","title":"A bill to put a student on the Board of Regents reaches committee",
   "body":"Reported by Ron Lawrence. Western had sent lobbyists to Frankfort for it earlier that month. The same issue carries students berating dorm rules and a letter headed 'Wanted: Work for Judicial Council'.",
   "src":{"label":"Herald 47:18, 8 Feb 1968","url":"https://digitalcommons.wku.edu/dlsc_ua_records/9006"}},
  {"date":"1968-04-04","title":"William Menser becomes WKU's first student regent",
   "body":"Two months after the bill was in committee, the Herald reported that Menser 'assumes duties as Regent Board Member'. The seat carried no vote at first. The same issue opens candidate declarations for the next student government election.",
   "src":{"label":"Herald 47:26, 4 Apr 1968","url":"https://digitalcommons.wku.edu/dlsc_ua_records/8998"}}],
 "1969-70": [
  {"date":"1970-02-10","title":"'Associate' regents want voting power",
   "body":"Two pieces in one issue: Associated Students seeking voting rights for the student regent, and student and faculty 'associate' regents pressing for a vote. An editorial calls for broad support of Senate Bill 75. Two years in, the seat was still symbolic.",
   "src":{"label":"Herald 49:26, 10 Feb 1970","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4927"}}],
 "1970-71": [
  {"date":"1970-08-28","title":"Regents seat eight students on the Academic Council",
   "body":"An editorial framed it as the Regents opening doors to student expression in academics. Representation was arriving faster in the curriculum committees than on the board itself.",
   "src":{"label":"Herald 50:1, 28 Aug 1970","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4968"}}],
 "1971-72": [
  {"date":"1972-02-01","title":"'Student Regent May Get Vote'",
   "body":"Four years after the seat was created it was still non-voting. The same issue has the Academic Council clarifying grievance procedure and an Associated Students open session scheduled for 12 February.",
   "src":{"label":"Herald 51:32, 1 Feb 1972","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4845"}}],
 "1972-73": [
  {"date":"1972-08-29","title":"Gov. Wendell Ford names two regents",
   "body":"Gerald Edds and Chalmer Embry. The same issue reports the best ASG course evaluation yet, students questioning the $5 car registration fee, and filing opening for ASG offices.",
   "src":{"label":"Herald 52:2, 29 Aug 1972","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4872"}},
  {"date":"1972-09-26","title":"Three new regents sworn in, one of them a student",
   "body":"Michael Fiorella took the student seat alongside Edds and Embry. The same issue reports 'Slack Time at Associated Student Government Congress', an ASG bankruptcy plan and the open-dorm visitation fight continuing.",
   "src":{"label":"Herald 52:6, 26 Sep 1972","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4876"}}],
 "1973-74": [
  {"date":"1974-06-19","title":"Gregory McKinney sworn in as WKU's first African American student regent",
   "body":"Seven years before Julius Price became the first Black gubernatorial appointee to the board in 1981. The student seat integrated the Board of Regents first.",
   "src":{"label":"WKU Timeline, 19 Jun 1974","url":"https://digitalcommons.wku.edu/wku_timeline/354/"}}],
 "1976-77": [
  {"date":"1977-04-15","title":"Bob Moore elected ASG president by 26 votes",
   "body":"One of the narrowest margins in the record. The same issue carries the outgoing president congratulating voters, the faculty asking for a say in hiring, and Western fighting a beer licence for a local pizzeria.",
   "src":{"label":"Herald 52:53, 15 Apr 1977","url":"https://digitalcommons.wku.edu/dlsc_ua_records/5370"}}],
 "1981-82": [
  {"date":"1982-02-18","title":"Sandra Norfleet elected student regent",
   "body":"Reported by Kevin Francke. The same issue has a group set to speak on the Associated Student Government's behalf and Western's 1982 budget coming off hold.",
   "src":{"label":"Herald 57:41, 18 Feb 1982","url":"https://digitalcommons.wku.edu/dlsc_ua_records/2447"}}],
}

added = 0
for yid, evs in NEW.items():
    have = {e["title"] for e in Y[yid]["events"]}
    for e in evs:
        if e["title"] not in have:
            Y[yid]["events"].append(e); added += 1

for y in d["years"]:
    y["events"].sort(key=lambda e: e["date"])
    n = len(y["events"])
    y["status"] = "researched" if n >= 3 else ("partial" if n else "empty")

d["_meta"]["role_values"] = {
 "president": "Led the student government that year",
 "regent": "Held the student seat on the WKU Board of Regents - a separately elected office from 1968 until the two merged",
 "unresolved": "Shares a year with another name and the split is not yet established"}
d["_meta"]["student_regent_history"] = (
 "The student regent seat was created by state legislation reported in committee in February 1968 and "
 "filled in April 1968 by William Menser. It carried no vote for at least four years - students were "
 "campaigning for voting power in February 1970 and the Herald was still reporting 'Student Regent May Get "
 "Vote' in February 1972. Because it was separately elected, several plaque years carry two names: one "
 "president and one regent.")

P.write_text(json.dumps(d, indent=1, ensure_ascii=False))
print(f"moved {moved} leaders, added {added} events")
ur = sum(1 for y in d["years"] for l in y["leaders"] if l["role"]=="unresolved")
rg = sum(1 for y in d["years"] for l in y["leaders"] if l["role"]=="regent")
print(f"still unresolved: {ur} | identified as regents: {rg} | events total: {sum(len(y['events']) for y in d['years'])}")
