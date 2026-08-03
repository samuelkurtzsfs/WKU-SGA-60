#!/usr/bin/env python3
"""
One-time migration: presidents.json  ->  years.json

The plaque is person-keyed. The site needs to be year-keyed, because:
  - people report their plaque year is wrong, so the year has to be the stable spine
  - two names share a year in 18 places
  - a year page is the natural container for "everything SGA did that year"

Run once. After this, data/years.json is the only file anyone edits.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "presidents.json"
OUT = ROOT / "data" / "years.json"

FIRST, LAST = 1966, 2026  # academic years 1966-67 .. 2026-27


def yid(start):
    return f"{start}-{str(start + 1)[2:]}"


def parse_term(term):
    """Return (list_of_year_ids, confidence)."""
    t = term.strip()
    m = re.fullmatch(r"(\d{4})-(\d{2,4})", t)
    if m:
        a = int(m.group(1))
        b = m.group(2)
        b = int(b) if len(b) == 4 else int(str(a)[:2] + b)
        if b - a == 1:
            return [yid(a)], "stated"
        # multi-year plate, e.g. 1968-70, 1983-85, 1986-88
        return [yid(y) for y in range(a, b)], "stated"
    m = re.fullmatch(r"(\d{4})", t)
    if m:
        a = int(m.group(1))
        return [yid(a)], "ambiguous"
    return [], "unparsed"


# Events already researched, bucketed by year id. Sources are all open access.
EVENTS = {
 "1966-67": [
  {"date":"1966-04-01","title":"President Kelly Thompson approves the constitution",
   "body":"The proposed constitution of the Associated Students of Western Kentucky University was completed in late March and approved on 1 April. The copy held by WKU Archives is dated 7 April 1966.",
   "src":{"label":"TopSCHOLAR - SGA Constitution","url":"https://digitalcommons.wku.edu/sga/Constitution/Constitution"}},
  {"date":"1966-04-26","title":"Students ratify the constitution, 1,812 to 726",
   "body":"A four-day referendum. 2,538 students voted - a larger raw turnout than most SGA elections have managed since.",
   "src":{"label":"WKU SGA history","url":"https://www.wku.edu/sga/about/history.php"}},
  {"date":"1966-05-18","title":"Jim Haynes elected first president",
   "body":"Seven weeks from presidential approval to a seated student president. Western Kentucky State College became Western Kentucky University on 16 June, so the university and its student government are almost exactly the same age.",
   "src":{"label":"WKU SGA history","url":"https://www.wku.edu/sga/about/history.php"}}],
 "1967-68": [
  {"date":"1968-02-01","title":"WKU sends lobbyists to Frankfort for a student on the Board of Regents",
   "body":"The same Herald issue carries a tuition increase, a discussion group on major issues before the Associated Student Government and a committee investigating women's dormitory rules. This is the origin of the student regent seat.",
   "src":{"label":"Herald 47:20, 1968","url":"https://digitalcommons.wku.edu/dlsc_ua_records/9003/"}},
  {"date":"1968-05-09","title":"Bill Straeffer wins the presidency; the Herald calls the election a failure",
   "body":"The issue reporting Straeffer's win also carries an editorial headed 'Elections Illustrate Faults, Indifference'. Turnout anxiety shows up in the second contested election the organisation ever held.",
   "src":{"label":"Herald 47:30, 9 May 1968","url":"https://digitalcommons.wku.edu/dlsc_ua_records/9010"}}],
 "1969-70": [
  {"date":"1969-10-07","title":"Associated Student Congress endorses the Vietnam Moratorium",
   "body":"The Herald called it a bold step. The clearest early example of the body taking a position outside the campus fence - the same argument that returns in 2017 and 2023.",
   "src":{"label":"Herald 49:5, 7 Oct 1969","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4773"}},
  {"date":"1969-11-07","title":"Students start grading the faculty",
   "body":"An ASG committee compiled the results of Western's first student teacher-evaluation effort. The Herald had already editorialised demanding the tabulation move faster.",
   "src":{"label":"Herald 49:11, 7 Nov 1969","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4778"}}],
 "1970-71": [
  {"date":"1970-10-27","title":"A resolution on the women's curfew, five months after Kent State",
   "body":"The Associated Student Congress passed a curfew resolution; the Herald reported abolition was unlikely that year and editorialised that the curfew was obsolete. The letters page in the same issue is almost entirely students arguing about Kent State.",
   "src":{"label":"Herald 50:17, 27 Oct 1970","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4975"}}],
 "1971-72": [
  {"date":"1971-09-14","title":"Associated Students affiliates with a wider student association",
   "body":"An early attempt to gain leverage beyond the Hill. Which body it joined is not clear from the article index alone.",
   "src":{"label":"Herald 51:3, 14 Sep 1971","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4812"}},
  {"date":"1972-02-25","title":"'Chaos Reigns at Associated Students Meeting'",
   "body":"The same issue carries students planning a petition to force dorm visitation and a separate piece arguing student interest had collapsed and the Associated Students had followed it down.",
   "src":{"label":"Herald 51:39, 25 Feb 1972","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4850"}},
  {"date":"1972-04-28","title":"A strike threat over visitation, and six votes won on a university council",
   "body":"A Mass Action Committee called for a strike over dorm visitation while the Associated Students installed next year's officers. Buried in the same issue: students gained six votes on a university council. Linda Jones reflected on her term.",
   "src":{"label":"Herald 51:50, 28 Apr 1972","url":"https://digitalcommons.wku.edu/dlsc_ua_records/4868"}}],
 "1978-79": [
  {"date":"1979-04-12","title":"830 students vote in the primary; the Herald runs a defence of not voting",
   "body":"The Associated Student Government put the open-house policy on the ballot. The same issue carries a piece justifying student apathy in ASG voting - the paper had moved from scolding non-voters to explaining them.",
   "src":{"label":"Herald 54:54, 12 Apr 1979","url":"https://digitalcommons.wku.edu/dlsc_ua_records/3456"}}],
 "1984-85": [
  {"date":"1985-02-14","title":"Apathy as an editorial cartoon",
   "body":"'Voter Apathy Can be Solved' ran alongside a cartoon on election apathy and a report that a 24-hour open house was under discussion.",
   "src":{"label":"Herald 60:38, 14 Feb 1985","url":"https://digitalcommons.wku.edu/dlsc_ua_records/5721"}}],
 "1986-87": [
  {"date":"1986-08-04","title":"Twenty years of amendments consolidated into one document",
   "body":"The constitution of the WKU Associated Students with amendments - the only surviving snapshot of how the 1966 framework had been patched over two decades. A Judicial Council roster for 1986-87 survives alongside it.",
   "src":{"label":"TopSCHOLAR - SGA Constitution","url":"https://digitalcommons.wku.edu/sga/Constitution/Constitution"}}],
 "1987-88": [
  {"date":"1987-01-01","title":"Not enough candidates to fill the ballot",
   "body":"ASG races faced a candidate shortage; one report notes a candidate entered a race to help a rival rather than to win. The same issue has ASG tabling a phone bill after amendment.",
   "src":{"label":"Herald 62:48, 1987","url":"https://digitalcommons.wku.edu/dlsc_ua_records/5916/"}}],
 "1988-89": [
  {"date":"1988-01-01","title":"A formal reaction to the General Education Task Force",
   "body":"ASG filed a written response to a proposed overhaul of general education requirements - one of the earliest surviving examples of student government intervening in curriculum rather than campus life.",
   "src":{"label":"TopSCHOLAR - Documents/Reports/11","url":"https://digitalcommons.wku.edu/sga/Documents/Reports/11"}}],
 "1989-90": [
  {"date":"1989-11-09","title":"Extended library hours",
   "body":"Correspondence between President Amos Gott, Howard Bailey, Sally Ann Strickler and Michael Binder. Resolutions went out as letters to named administrators and answers came back.",
   "src":{"label":"TopSCHOLAR - Documents/Reports","url":"https://digitalcommons.wku.edu/sga/Documents/Reports"}},
  {"date":"1990-01-22","title":"The Downing University Center flagpole",
   "body":"One item in a working inventory of the job that year: the flagpole, the stadium press box, a dispute involving a local pizza vendor and a proposed budget for the Board of Student Body Presidents.",
   "src":{"label":"TopSCHOLAR - Documents/Reports","url":"https://digitalcommons.wku.edu/sga/Documents/Reports"}}],
 "1991-92": [
  {"date":"1992-04-07","title":"Associated Students votes to become the Student Government Association",
   "body":"The body voted to rename itself on 7 April and students ratified the change in a referendum on 14 April. It took effect that autumn.",
   "src":{"label":"WKU SGA history","url":"https://www.wku.edu/sga/about/history.php"}}],
 "1993-94": [
  {"date":"1993-11-01","title":"At least seventeen numbered resolutions in one semester",
   "body":"Resolutions 93-4-F through 93-20-F survive in the correspondence files - the fullest single-semester record in the collection, and the best available answer to how much a WKU student senate actually passes in a working term.",
   "src":{"label":"TopSCHOLAR - Documents/Reports","url":"https://digitalcommons.wku.edu/sga/Documents/Reports"}}],
 "1997-98": [
  {"date":"1997-10-22","title":"A crosswalk on Dogwood Drive",
   "body":"One of a run of outgoing letters in these years covering student seating at athletic events, ice machines in residence halls, campus safety, professors posting office hours, food court hours, housing scholarships for off-campus students and student health services.",
   "src":{"label":"TopSCHOLAR - Documents/Reports","url":"https://digitalcommons.wku.edu/sga/Documents/Reports"}}],
 "2003-04": [
  {"date":"2004-01-01","title":"The Constitutional Convention rebuilds the body",
   "body":"Three branches - Executive Cabinet, Senate and Judicial Council - drawn from the student body at large. The most consequential clause is the quietest: every enrolled student became a member of SGA with the right to vote in its elections.",
   "src":{"label":"WKU SGA history","url":"https://www.wku.edu/sga/about/history.php"}},
  {"date":"2004-04-20","title":"The president-elect is investigated before he takes office",
   "body":"The Herald reported an investigation into missing funds from an SGA dining account. Articles of impeachment were drafted against the president-elect's existing finance post but the judicial council found the two-week process could not finish before the term ended. Because state law governs the student regent seat, the new constitution required a separate special election to fill it.",
   "src":{"label":"Herald, April 2004","url":"https://wkuherald.com/55298/news/sga-president-elect-under-investigation/"}}],
 "2005-06": [
  {"date":"2005-01-01","title":"The plus/minus grading fight",
   "body":"An Institutional Research report on plus and minus grading, a protest broadside, a post-winter-term student survey and an SGA handbook all survive - one of the few academic-policy campaigns documented from research through to public agitation.",
   "src":{"label":"TopSCHOLAR - Documents/Reports","url":"https://digitalcommons.wku.edu/sga/Documents/Reports"}}],
 "2007-08": [
  {"date":"2008-02-20","title":"Fifty senators write down what a lobbying trip felt like",
   "body":"After a student rally at the Capitol in Frankfort, dozens of SGA members each filed an individual written reflection, archived one per person. The richest first-person source in the entire collection.",
   "src":{"label":"TopSCHOLAR - Frankfort rally reflections","url":"https://digitalcommons.wku.edu/sga/Documents/Reports"}}],
 "2014-15": [
  {"date":"2015-04-16","title":"An election result challenged and upheld",
   "body":"Anonymous accusations alleged Jay Todd Richey had breached election codes on poster placement. The judicial council warned him against future violations and confirmed he had rightfully won.",
   "src":{"label":"Herald, April 2015","url":"https://wkuherald.com/36017/uncategorized/sga/"}}],
 "2016-17": [
  {"date":"2017-04-18","title":"Resolution 6-17-S passes 19-10-1",
   "body":"Senators Andrea Ambam and Brian Anderson wrote a resolution supporting reparations for Black students, calling for full and free access to WKU for all Black people and asking for a task force on test-optional and geographically weighted admissions. Modelled on a resolution passed at Wisconsin-Madison earlier that year.",
   "src":{"label":"Bowling Green Daily News","url":"https://www.bgdailynews.com/news/sga-passes-resolution-supporting-reparations-for-black-students/article_8daeb133-844e-5052-a5ac-87189800ef25.html"}},
  {"date":"2017-04-21","title":"President Ransdell rejects the resolution",
   "body":"National wire coverage followed, along with a Tucker Carlson interview with Ambam and a wave of fabricated headlines claiming WKU had granted free tuition. Ransdell stated within days that it was not a university position. Both authors described it as a conversation starter.",
   "src":{"label":"FactCheck.org","url":"https://www.factcheck.org/2017/09/false-headline-free-tuition"}}],
 "2021-22": [
  {"date":"2021-08-06","title":"Northeast Hall renamed for Margaret Munday",
   "body":"Student Regent Matthew Wininger was sworn in at the Board of Regents meeting that renamed Northeast Hall for WKU's first African American student to enrol - the first building on campus named after an African American.",
   "src":{"label":"WKU News","url":"https://www.wku.edu/news/articles/index.php?view=article&articleid=9788"}},
  {"date":"2022-04-20","title":"Cole Bornefeld elected with 49% of 1,448 votes",
   "body":"Alexis Courtenay took 40% and Olivia Feck 11%. Sam Kurtz and Garrison Reed were elected to the two vice presidencies.",
   "src":{"label":"WKU News","url":"https://www.wku.edu/cebs/news/index.php?view=article&articleid=10479"}}],
 "2022-23": [
  {"date":"2023-02-17","title":"The Speaker takes the President to the Judicial Council",
   "body":"Speaker of the Senate Yulia 'Julie' Mishchuk requested a censure hearing against President Cole Bornefeld over anti-transgender posts he had liked on Instagram. Members of the Queer Student Union and both vice presidents attended. The Judicial Council voted unanimously against censure.",
   "src":{"label":"Herald, Feb 2023","url":"https://wkuherald.com/70591/news/sga-judicial-council-unanimously-votes-against-censure-of-president-bornefeld-regarding-use-of-social-media/"}},
  {"date":"2023-02-19","title":"A Title IX report seeks the President's removal",
   "body":"Filed with Student Conduct. Under the constitution, removing an executive who will not resign requires written endorsement from at least 20% of the Senate, a wait of at least fourteen days and a two-thirds vote of the full Senate sitting as a court.",
   "src":{"label":"Herald, March 2023","url":"https://wkuherald.com/70863/news/title-ix-compliant-filed-against-sga-president-over-social-media-posts-he-liked/"}},
  {"date":"2023-04-19","title":"Sam Kurtz elected on an unopposed ticket",
   "body":"With Salvador Leon as administrative vice president and Annalise Finch as executive vice president.",
   "src":{"label":"Herald, April 2023","url":"https://wkuherald.com/71533/news/sga-announces-election-results/"}}],
 "2023-24": [
  {"date":"2023-11-28","title":"The 23rd Senate corrects its own governing documents",
   "body":"Three bills from the Legislative Operations Committee: fix references to a 'University Senate' that had since split into separate Faculty and Staff senates, reconcile bylaws language about expelling senators with a constitution that only provides for impeachment, and update committee names that had drifted.",
   "src":{"label":"Herald, Nov 2023","url":"https://wkuherald.com/74058/news/sga-holds-final-meeting-of-semester/"}}],
 "2024-25": [
  {"date":"2025-02-11","title":"A mental health survey, and a warning about the election",
   "body":"The Senate passed Bill 4-25-S funding a DEI Committee tabling event to gather anonymous mental health survey responses. Dean of Students Martha Sales told the Senate 'you cannot isolate and educate at the same time'. Kurtz warned repeatedly that an unusually senior chamber made the spring election matter more than usual.",
   "src":{"label":"Herald, Feb 2025","url":"https://wkuherald.com/82037/news/sga-announces-spring-election-dates-passes-one-bill/"}},
  {"date":"2025-04-15","title":"Rush Robinson elected on a turnout of 966",
   "body":"Elected alongside class, college, transfer, first-generation, Intercultural Student Engagement Center and Honors College senators - constituencies the 1966 constitution had no concept of.",
   "src":{"label":"WKU News","url":"https://www.wku.edu/news/articles/index.php?view=article&articleid=12496"}}],
 "2025-26": [
  {"date":"2026-04-07","title":"Two tickets take questions in the DSU auditorium",
   "body":"Caden Lucas with Jakob Barker and Will Derryberry against Jaden Marshall with Kaden Blankenship and Miles VanRude. Chief Justice Sophie Stirling moderated questions submitted by the student body.",
   "src":{"label":"Herald, April 2026","url":"https://wkuherald.com/92534/news/sga-holds-town-hall-qa-for-executive-candidates-before-election/"}},
  {"date":"2026-04-15","title":"Turnout jumps 66% in a contested race",
   "body":"1,601 students voted, 635 more than the year before. Lucas won. The clearest evidence in the whole record that WKU turnout tracks whether there is an actual contest.",
   "src":{"label":"Herald, April 2026","url":"https://wkuherald.com/92808/news/lucas-wins-sga-presidential-election/"}},
  {"date":"2026-04-16","title":"Robinson tells the Faculty Senate to look at the dorms",
   "body":"Sitting next to Faculty Regent Shane Spiller during a discussion of WKU housing, Robinson told senators to 'take a field trip' and see the state of the residence halls.",
   "src":{"label":"Herald, April 2026","url":"https://wkuherald.com/92855/news/faculty-senate-holds-election-debates-senate-charter-changes/"}},
  {"date":"2026-04-28","title":"The red suit jacket changes hands",
   "body":"Lucas, Barker and Derryberry sworn in at the first meeting of the 26th Senate. Robinson handed Lucas the same red jacket his own predecessor had given him a year earlier.",
   "src":{"label":"Herald, April 2026","url":"https://wkuherald.com/93405/election/sga-holds-first-meeting-of-26th-senate-swears-in-new-senators-senate-speaker/"}}],
}


def main():
    src = json.loads(SRC.read_text())
    years = {yid(y): {"id": yid(y), "start": y, "end": y + 1,
                      "org": "Associated Students" if y < 1992 else "Student Government Association",
                      "leaders": [], "events": [], "status": "empty"}
             for y in range(FIRST, LAST + 1)}

    for p in src["presidents"]:
        ids, conf = parse_term(p["term"])
        for i in ids:
            if i not in years:
                print(f"  ! {p['name']} {p['term']} -> {i} outside range, skipped")
                continue
            years[i]["leaders"].append({
                "name": p["name"],
                "plaque_term": p["term"],
                "role": p["role"],
                "year_confidence": conf,
                "name_verified": bool(p.get("verified")),
                "missing_from_plaque": bool(p.get("missing_from_plaque")),
                "current": bool(p.get("current")),
                "note": p.get("note", ""),
                "sources": p.get("sources", []),
            })

    for i, evs in EVENTS.items():
        if i in years:
            years[i]["events"] = sorted(evs, key=lambda e: e["date"])

    for y in years.values():
        n = len(y["events"])
        y["status"] = "researched" if n >= 3 else ("partial" if n else "empty")

    out = {
        "_meta": {
            "spine": "academic year",
            "why": ("The plaque is person-keyed and several people report their year on it is wrong. "
                    "Years are the stable spine; people are attached to years and can be moved."),
            "coverage": f"{yid(FIRST)} through {yid(LAST)}",
            "generated_from": "data/presidents.json via scripts/migrate.py",
            "edit_this_file": True,
        },
        "years": [years[yid(y)] for y in range(FIRST, LAST + 1)],
    }
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))

    tot = len(out["years"])
    r = sum(1 for y in out["years"] if y["status"] == "researched")
    pa = sum(1 for y in out["years"] if y["status"] == "partial")
    amb = sum(1 for y in out["years"] for l in y["leaders"] if l["year_confidence"] == "ambiguous")
    noone = [y["id"] for y in out["years"] if not y["leaders"]]
    print(f"{tot} academic years written to {OUT}")
    print(f"  researched {r} | partial {pa} | empty {tot-r-pa}")
    print(f"  leaders with ambiguous plaque years: {amb}")
    print(f"  years with no name attached: {noone}")


if __name__ == "__main__":
    main()
