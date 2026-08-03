#!/usr/bin/env python3
"""
SGA 60 site generator.

Reads  data/years.json
Writes site/index.html  and  site/y/<year>.html

Pure Python. No AI, no API key, no network. Runs in about a second.
"""
import json, shutil, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "years.json"
SITE = ROOT / "site"
YDIR = SITE / "y"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Zilla+Slab:ital,wght@0,400;0,600;0,700;1,400'
         '&family=Public+Sans:ital,wght@0,300;0,400;0,600;0,800;1,400'
         '&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">')

CSS = """
:root{--paper:#E7E9E0;--card:#F3F4EE;--ink:#15171A;--ink2:#53595C;--ink3:#7C8285;
 --ditto:#57429A;--ditto-soft:#EDE8F8;--red:#A0181F;--rule:#C4C7B9;--rule-soft:#D8DACE;
 --display:"Zilla Slab",Georgia,serif;--body:"Public Sans",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}
*{box-sizing:border-box}
html{scroll-behavior:smooth}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.62;
 -webkit-font-smoothing:antialiased;background-image:repeating-linear-gradient(90deg,rgba(21,23,26,.018) 0 1px,transparent 1px 3px)}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
@media(max-width:640px){.wrap{padding:0 18px}}
a{color:var(--ditto);text-underline-offset:3px}a:hover{color:var(--red)}
:focus-visible{outline:2.5px solid var(--ditto);outline-offset:3px;border-radius:2px}
.eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink3);font-weight:500}
.topbar{border-bottom:1.5px solid var(--ink);background:var(--paper)}
.topbar .wrap{display:flex;justify-content:space-between;align-items:center;gap:18px;padding:13px 28px;flex-wrap:wrap}
.brand{font-family:var(--display);font-weight:700;font-size:1.05rem;text-decoration:none;color:var(--ink)}
.brand span{color:var(--red)}
.navlinks{display:flex;gap:18px}
.navlinks a{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;color:var(--ink2)}
.navlinks a:hover,.navlinks a[aria-current]{color:var(--red)}
footer{border-top:1.5px solid var(--ink);margin-top:70px;padding:34px 0 60px;font-size:.88rem;color:var(--ink2)}
footer p{max-width:72ch;margin:0 0 10px}
"""

INDEX_CSS = """
.hero{padding:64px 0 34px}
.hero h1{font-family:var(--display);font-weight:700;font-size:clamp(2.6rem,7vw,4.6rem);line-height:1;letter-spacing:-.02em;margin:14px 0 0}
.hero h1 em{font-style:italic;font-weight:400;color:var(--ditto)}
.hero p{max-width:54ch;color:var(--ink2);font-weight:300;font-size:1.1rem;margin:22px 0 0}
.stats{display:flex;gap:34px;flex-wrap:wrap;margin-top:30px;padding-top:22px;border-top:1px solid var(--rule)}
.stat b{display:block;font-family:var(--display);font-size:2.1rem;font-weight:700;line-height:1}
.stat span{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3)}
.controls{display:flex;gap:8px;flex-wrap:wrap;padding:15px 0;position:sticky;top:0;background:var(--paper);
 border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);z-index:20}
.chip{font-family:var(--mono);font-size:11px;letter-spacing:.07em;text-transform:uppercase;padding:6px 11px;
 border:1.25px solid var(--rule);background:transparent;color:var(--ink2);cursor:pointer;font-weight:500}
.chip:hover{border-color:var(--ink);color:var(--ink)}
.chip[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:var(--card)}
.tally{font-family:var(--mono);font-size:11px;color:var(--ink3);align-self:center;margin-left:auto}
.wall{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:11px;padding:32px 0 8px}
.plate{display:block;text-decoration:none;background:var(--card);border:1px solid var(--rule);padding:13px 13px 12px;transition:.14s;position:relative}
.plate:hover{border-color:var(--ink);transform:translateY(-2px);box-shadow:3px 3px 0 rgba(87,66,154,.18)}
.plate .yr{font-family:var(--mono);font-size:12px;font-weight:600;color:var(--red);letter-spacing:.06em}
.plate .nm{display:block;font-family:var(--display);font-size:1rem;font-weight:600;color:var(--ink);line-height:1.22;margin-top:4px;text-transform:uppercase}
.plate .nm.two{font-size:.86rem}
.plate .meter{display:flex;gap:2px;margin-top:9px}
.plate .meter i{height:3px;flex:1;background:var(--rule-soft)}
.plate .meter i.on{background:var(--ditto)}
.plate.hidden{display:none}
.plate.now{border-width:2px;border-color:var(--red)}
.plate .q{position:absolute;top:7px;right:8px;font-family:var(--mono);font-size:11px;color:var(--red);font-weight:600}
.legend{display:flex;gap:22px;flex-wrap:wrap;font-family:var(--mono);font-size:10.5px;color:var(--ink3);padding:14px 0 0}
.block{margin-top:56px;padding:32px 0;border-top:1.5px solid var(--ink)}
.block h2{font-family:var(--display);font-size:1.85rem;font-weight:700;margin:0 0 10px}
.block p{max-width:68ch;color:var(--ink2);margin:0 0 14px}
"""

PAGE_CSS = """
.yhead{padding:52px 0 30px;border-bottom:1.5px solid var(--ink)}
.yhead .eyebrow{margin-bottom:8px}
.yhead h1{font-family:var(--display);font-weight:700;font-size:clamp(3rem,9vw,5.4rem);line-height:.95;letter-spacing:-.03em;margin:0}
.leaders{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
.lead{background:var(--card);border:1px solid var(--rule);padding:13px 16px;min-width:210px}
.lead b{display:block;font-family:var(--display);font-size:1.12rem;font-weight:600;text-transform:uppercase;letter-spacing:.01em}
.lead .r{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3);margin-top:3px}
.lead .warn{color:var(--red)}
.lead .ok{color:var(--ditto)}
.cols{display:grid;grid-template-columns:1.4fr .6fr;gap:50px;padding:40px 0}
@media(max-width:880px){.cols{grid-template-columns:1fr;gap:32px}}
h2.sub{font-family:var(--display);font-size:1.3rem;font-weight:600;margin:0 0 16px}
.ev{display:grid;grid-template-columns:104px 1fr;gap:22px;padding:20px 0;border-bottom:1px solid var(--rule-soft)}
@media(max-width:700px){.ev{grid-template-columns:1fr;gap:6px}}
.ev .d{font-family:var(--mono);font-size:11.5px;font-weight:600;color:var(--ink);padding-top:3px}
.ev h3{font-family:var(--display);font-size:1.1rem;font-weight:600;margin:0 0 7px;line-height:1.28}
.ev p{margin:0;color:var(--ink2);font-size:.97rem}
.ev a.cite{display:inline-block;margin-top:10px;font-family:var(--mono);font-size:10.5px;color:var(--ditto);
 border:1px solid var(--ditto);background:var(--ditto-soft);padding:2.5px 7px;text-decoration:none}
.ev a.cite:hover{background:var(--ditto);color:var(--card)}
.empty{background:var(--card);border:1px dashed var(--rule);padding:22px;color:var(--ink3);font-size:.95rem}
.note{background:var(--card);border-left:3px solid var(--ditto);padding:14px 16px;margin:0 0 20px;font-size:.94rem;color:var(--ink2)}
.dig{background:var(--card);border:1px solid var(--rule);padding:20px 18px;position:sticky;top:18px;max-height:88vh;overflow:auto}
.dig h2{font-family:var(--mono);font-size:11px;letter-spacing:.13em;text-transform:uppercase;margin:0 0 3px;color:var(--red);font-weight:600}
.dig h3{font-family:var(--mono);font-size:10px;letter-spacing:.13em;text-transform:uppercase;margin:18px 0 4px;color:var(--ink3)}
.dig .lede{font-size:.85rem;color:var(--ink3);margin:0 0 6px;line-height:1.45}
.dig a.q{display:block;text-decoration:none;padding:7px 0;border-top:1px solid var(--rule-soft);
 font-family:var(--mono);font-size:11px;color:var(--ditto);line-height:1.4}
.dig a.q:hover{color:var(--red)}
.pager{display:flex;justify-content:space-between;gap:18px;padding:24px 0;border-top:1.5px solid var(--ink);flex-wrap:wrap}
.pager a{font-family:var(--mono);font-size:11.5px;text-decoration:none;max-width:46%}
.pager a b{display:block;font-family:var(--body);font-size:1rem;font-weight:600;color:var(--ink);margin-top:3px}
.pager a:hover b{color:var(--red)}
.pager .r{text-align:right;margin-left:auto}
"""


def shell(title, body, css_extra, depth):
    up = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>{FONTS}<style>{CSS}{css_extra}</style></head><body>
<nav class="topbar"><div class="wrap">
 <a class="brand" href="{up}index.html">SGA<span>60</span> &middot; The Record</a>
 <div class="navlinks"><a href="{up}index.html">Years</a><a href="{up}history.html">Timeline</a></div>
</div></nav>
{body}
<footer><div class="wrap">
<p>Names transcribed from the plaque in the SGA Chambers, Downing Student Union 2081. Plaque years are treated as
a claim, not a fact &mdash; several are disputed. Everything is checked against the archive before it is confirmed.</p>
<p>Built for SGA 60 &mdash; sixty years of student government at Western Kentucky University, 1966&ndash;2026.</p>
</div></footer></body></html>"""


ORG_TERMS = ['"student government association"', '"associated student government"',
             '"student government"', 'SGA', 'ASG', '"student regent"']
DQ = chr(34)


def q(s):
    return urllib.parse.quote_plus(s)


def year_searches(y):
    """The year sweep: every SGA keyword crossed with both calendar years."""
    out = []
    for cal in (y["start"], y["end"]):
        for t in ORG_TERMS:
            out.append((f'{t} {cal}',
                        f'https://www.google.com/search?q=site:digitalcommons.wku.edu+{q(t)}+{cal}'))
    return out


def name_searches(name):
    """Name check: is this person real, and is the plaque year right?"""
    org = " OR ".join(ORG_TERMS)
    return [
        (f'{name} + SGA terms',
         f'https://www.google.com/search?q=site:digitalcommons.wku.edu+{q(DQ + name + DQ)}+{q("(" + org + ")")}'),
        (f'{name} anywhere on TopSCHOLAR',
         f'https://www.google.com/search?q=site:digitalcommons.wku.edu+{q(DQ + name + DQ)}'),
        (f'{name} in the Herald',
         f'https://wkuherald.com/?s={q(name)}'),
    ]


def render_year(y, prev, nxt):
    leads = ""
    for l in y["leaders"]:
        flags = []
        if l["role"] == "unresolved":
            flags.append('<span class="warn">role unresolved</span>')
        if l["year_confidence"] == "ambiguous":
            flags.append('<span class="warn">year ambiguous</span>')
        if l["missing_from_plaque"]:
            flags.append('<span class="warn">not on the wall</span>')
        if l["name_verified"]:
            flags.append('<span class="ok">confirmed</span>')
        if l["current"]:
            flags.append('<span class="ok">in office</span>')
        flags.append(f'plaque reads {l["plaque_term"]}')
        leads += (f'<div class="lead"><b>{l["name"]}</b>'
                  f'<div class="r">{" &middot; ".join(flags)}</div></div>')

    notes = "".join(f'<div class="note"><b>{l["name"]}:</b> {l["note"]}</div>'
                    for l in y["leaders"] if l.get("note"))

    if y["events"]:
        evs = "".join(
            f'<article class="ev"><div class="d">{e["date"]}</div><div>'
            f'<h3>{e["title"]}</h3><p>{e["body"]}</p>'
            + (f'<a class="cite" href="{e["src"]["url"]}" target="_blank" rel="noopener">{e["src"]["label"]} &#8599;</a>'
               if e.get("src") else "")
            + '</div></article>'
            for e in sorted(y["events"], key=lambda e: e["date"]))
    else:
        evs = ('<div class="empty">No events recorded for this year yet. Run the year sweep on the right &mdash; '
               'twelve searches, one per keyword per calendar year &mdash; and add what you find to '
               '<code>data/years.json</code> under this year&rsquo;s <code>events</code> array.</div>')

    nq = ""
    for l in y["leaders"]:
        nq += f'<h3>Check: {l["name"]}</h3>'
        nq += "".join(f'<a class="q" href="{u}" target="_blank" rel="noopener">{lab} &#8599;</a>'
                      for lab, u in name_searches(l["name"]))
    yq = "".join(f'<a class="q" href="{u}" target="_blank" rel="noopener">{lab} &#8599;</a>'
                 for lab, u in year_searches(y))

    pager = ""
    if prev:
        pager += f'<a href="{prev["id"]}.html">&larr; previous year<b>{prev["id"]}</b></a>'
    if nxt:
        pager += f'<a class="r" href="{nxt["id"]}.html">next year &rarr;<b>{nxt["id"]}</b></a>'

    body = f"""
<header class="yhead"><div class="wrap">
 <div class="eyebrow">{y['org']} &middot; academic year</div>
 <h1>{y['id']}</h1>
 <div class="leaders">{leads}</div>
</div></header>
<div class="wrap"><div class="cols">
 <div>
  {notes}
  <h2 class="sub">What happened, in order</h2>
  {evs}
 </div>
 <aside><div class="dig">
  <h2>Dig here</h2>
  <p class="lede">Check the name first &mdash; plaque years are disputed. Then sweep the year.</p>
  {nq}
  <h3>Year sweep &mdash; {y['start']} and {y['end']}</h3>
  {yq}
 </div></aside>
</div>
<div class="pager">{pager}</div></div>"""
    return shell(f"{y['id']} &middot; SGA 60", body, PAGE_CSS, depth=1)


def render_index(ys):
    tot = len(ys)
    done = sum(1 for y in ys if y["status"] == "researched")
    part = sum(1 for y in ys if y["status"] == "partial")
    evn = sum(len(y["events"]) for y in ys)
    amb = sum(1 for y in ys for l in y["leaders"]
              if l["year_confidence"] == "ambiguous" or l["role"] == "unresolved")

    plates = []
    for y in ys:
        names = [l["name"] for l in y["leaders"]]
        cls = ["plate"]
        if any(l["current"] for l in y["leaders"]):
            cls.append("now")
        flagged = any(l["role"] == "unresolved" or l["year_confidence"] == "ambiguous" for l in y["leaders"])
        tags = f"d{(y['start']//10)*10} {y['status']} {'flagged' if flagged else 'clean'}"
        filled = min(len(y["events"]), 5)
        meter = "".join(f'<i class="{"on" if k < filled else ""}"></i>' for k in range(5))
        plates.append(
            f'<a class="{" ".join(cls)}" data-tags="{tags}" href="y/{y["id"]}.html">'
            + ('<span class="q">?</span>' if flagged else '')
            + f'<span class="yr">{y["id"]}</span>'
            + f'<span class="nm{" two" if len(names) > 1 else ""}">{" &middot; ".join(names)}</span>'
            + f'<span class="meter">{meter}</span></a>')

    body = f"""
<div class="wrap">
 <section class="hero">
  <div class="eyebrow">Sixty-one academic years &middot; 1966&ndash;2027</div>
  <h1>Every year of it,<br><em>as far as the record</em><br>will take us.</h1>
  <p>One page per academic year. Who led it, and everything the archive holds about what student
  government at Western actually did that year, in order. Most of these pages are still empty. That is the job.</p>
  <div class="stats">
   <div class="stat"><b>{tot}</b><span>Years</span></div>
   <div class="stat"><b>{evn}</b><span>Events logged</span></div>
   <div class="stat"><b>{done}</b><span>Years researched</span></div>
   <div class="stat"><b>{part}</b><span>Started</span></div>
   <div class="stat"><b>{amb}</b><span>Name or year disputed</span></div>
  </div>
 </section>

 <div class="controls" role="group" aria-label="Filter years">
  <button class="chip" data-f="all" aria-pressed="true">All</button>
  <button class="chip" data-f="d1960" aria-pressed="false">60s</button>
  <button class="chip" data-f="d1970" aria-pressed="false">70s</button>
  <button class="chip" data-f="d1980" aria-pressed="false">80s</button>
  <button class="chip" data-f="d1990" aria-pressed="false">90s</button>
  <button class="chip" data-f="d2000" aria-pressed="false">00s</button>
  <button class="chip" data-f="d2010" aria-pressed="false">10s</button>
  <button class="chip" data-f="d2020" aria-pressed="false">20s</button>
  <button class="chip" data-f="empty" aria-pressed="false">Not started</button>
  <button class="chip" data-f="flagged" aria-pressed="false">Disputed</button>
  <span class="tally" id="tally"></span>
 </div>

 <div class="wall" id="wall">{''.join(plates)}</div>
 <div class="legend">
  <span>Bar under each year = events logged, out of five</span>
  <span style="color:var(--red)">? = name or plaque year not yet confirmed</span>
 </div>

 <section class="block">
  <h2>Why years, not people</h2>
  <p>The wall in the SGA Chambers is organised by person, and people who served have said their year on it is
  wrong. So the plaque is treated here as a claim to be checked, not a source to be copied. The academic year is
  the spine; names hang off it and can be moved when the archive says otherwise.</p>
  <p>It also fixes a problem the person-keyed version could not. Eighteen plates share a year with another name.
  On a year page they simply both appear, and the question of which one was president and which was student
  regent becomes a caption to resolve rather than a structural contradiction.</p>
 </section>
</div>
<script>
const chips=[...document.querySelectorAll('.chip')],plates=[...document.querySelectorAll('.plate')],t=document.getElementById('tally');
function apply(f){{let n=0;plates.forEach(el=>{{const ok=f==='all'||el.dataset.tags.split(' ').includes(f);
el.classList.toggle('hidden',!ok);if(ok)n++;}});t.textContent=n+' of '+plates.length+' shown';
chips.forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.f===f)));}}
chips.forEach(c=>c.addEventListener('click',()=>apply(c.dataset.f)));apply('all');
</script>"""
    return shell("SGA 60 &middot; Sixty years of student government at WKU", body, INDEX_CSS, depth=0)


def main():
    ys = json.loads(DATA.read_text())["years"]
    YDIR.mkdir(parents=True, exist_ok=True)
    if (SITE / "p").exists():
        shutil.rmtree(SITE / "p")          # retire the old person-keyed pages
    (SITE / "index.html").write_text(render_index(ys))
    for i, y in enumerate(ys):
        (YDIR / f'{y["id"]}.html').write_text(
            render_year(y, ys[i - 1] if i else None, ys[i + 1] if i < len(ys) - 1 else None))
    shutil.copy(DATA, SITE / "years.json")
    print(f'built index + {len(ys)} year pages -> {SITE}')


if __name__ == "__main__":
    main()
