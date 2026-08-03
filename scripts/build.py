#!/usr/bin/env python3
"""
SGA 60 site generator — the lit wall.

Reads  data/years.json
Writes site/index.html   the board
       site/y/<year>.html one page per academic year

Pure Python. No AI, no API key, no network.
"""
import json, shutil, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "years.json"
SITE = ROOT / "site"
YDIR = SITE / "y"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700'
         '&family=Public+Sans:ital,wght@0,300;0,400;0,600;1,400'
         '&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">')

# ---------------------------------------------------------------- tokens
BASE = """
:root{
 --void:#08090B; --room:#101216; --room2:#171A20;
 --metal-hi:#D6D9D2; --metal:#B4B8B0; --metal-lo:#8B8F88; --metal-edge:#5E625C;
 --engrave:#22241F; --tungsten:#FFE6BC; --tungsten-dim:#C9A970;
 --red:#B01E24; --red-dim:#7A171C;
 --txt:#D9DBD5; --txt2:#9AA096; --txt3:#666B62;
 --inscribe:"Cinzel",Georgia,serif; --ui:"Public Sans",system-ui,sans-serif;
 --mono:"IBM Plex Mono",ui-monospace,monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--void);color:var(--txt);font-family:var(--ui);
 font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:var(--tungsten-dim);text-underline-offset:3px}
a:hover{color:var(--tungsten)}
:focus-visible{outline:2px solid var(--tungsten);outline-offset:3px;border-radius:2px}
.eyebrow{font-family:var(--mono);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--txt3)}
.wrap{max-width:1240px;margin:0 auto;padding:0 30px}
@media(max-width:640px){.wrap{padding:0 18px}}

/* engraved metal plate — shared by the board and the page headers */
.plate-face{
 background:linear-gradient(158deg,var(--metal-hi) 0%,var(--metal) 42%,var(--metal-lo) 100%);
 box-shadow:
   inset 0 1px 0 rgba(255,255,255,.65),
   inset 1px 0 0 rgba(255,255,255,.28),
   inset 0 -1px 0 rgba(0,0,0,.45),
   inset -1px 0 0 rgba(0,0,0,.3),
   0 2px 5px rgba(0,0,0,.55);
 position:relative;
}
.plate-face::before{ /* brushed grain */
 content:"";position:absolute;inset:0;pointer-events:none;opacity:.35;
 background:repeating-linear-gradient(96deg,rgba(255,255,255,.10) 0 1px,transparent 1px 3px);
}
.engraved{color:var(--engrave);text-shadow:0 1px 0 rgba(255,255,255,.5),0 -1px 0 rgba(0,0,0,.22)}
"""

# ---------------------------------------------------------------- index
INDEX_CSS = """
.room{position:fixed;inset:0;z-index:0;pointer-events:none;
 background:
  radial-gradient(140% 90% at 50% -12%, rgba(255,230,188,.13) 0%, rgba(255,230,188,.04) 26%, transparent 55%),
  radial-gradient(90% 60% at 50% 42%, rgba(255,230,188,.055) 0%, transparent 62%),
  linear-gradient(180deg,var(--room) 0%,var(--void) 62%);
}
.beam{position:fixed;top:-8vh;left:50%;transform:translateX(-50%);width:150vw;height:118vh;z-index:0;
 pointer-events:none;opacity:.5;
 background:linear-gradient(180deg,rgba(255,230,188,.20) 0%,rgba(255,230,188,.07) 34%,transparent 72%);
 clip-path:polygon(43% 0,57% 0,88% 100%,12% 100%);filter:blur(26px)}
.grain{position:fixed;inset:0;z-index:60;pointer-events:none;opacity:.05;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/></filter><rect width='140' height='140' filter='url(%23n)' opacity='.5'/></svg>")}

header.top{position:relative;z-index:2;padding:56px 0 30px;text-align:center}
header.top h1{font-family:var(--inscribe);font-weight:700;font-size:clamp(1.8rem,3.4vw,2.9rem);
 letter-spacing:.10em;margin:14px 0 0;color:var(--txt);
 text-shadow:0 0 34px rgba(255,230,188,.30),0 1px 0 rgba(0,0,0,.7)}
header.top .sub{color:var(--txt2);font-weight:300;max-width:56ch;margin:16px auto 0;font-size:1.02rem}

/* ---- the board ---- */
.stage{position:relative;z-index:2;perspective:1500px;perspective-origin:50% 32%;padding:14px 0 8px}
.board{
 position:relative;margin:0 auto;max-width:1180px;
 transform-style:preserve-3d;transition:transform .5s cubic-bezier(.2,.7,.3,1);
 padding:26px;border-radius:3px;
 background:linear-gradient(150deg,#4A4E48 0%,#33362F 40%,#232620 100%);
 box-shadow:
   inset 0 2px 0 rgba(255,255,255,.20), inset 0 -2px 0 rgba(0,0,0,.6),
   0 44px 90px rgba(0,0,0,.82), 0 12px 26px rgba(0,0,0,.6);
}
.board-inner{
 padding:22px;border-radius:2px;background:linear-gradient(170deg,#20231E 0%,#15170F 100%);
 box-shadow:inset 0 3px 14px rgba(0,0,0,.85), inset 0 0 0 1px rgba(255,255,255,.06);
}
.board::after{ /* light falloff toward the edges of the wall */
 content:"";position:absolute;inset:0;border-radius:3px;pointer-events:none;z-index:5;
 background:radial-gradient(78% 62% at 50% 26%, transparent 0%, rgba(0,0,0,.22) 58%, rgba(0,0,0,.46) 100%);
}
.board-head{display:flex;justify-content:center;padding-bottom:18px}
.board-head .sign{
 font-family:var(--inscribe);font-weight:600;font-size:clamp(.85rem,1.5vw,1.15rem);letter-spacing:.34em;
 padding:11px 30px;border-radius:2px;text-transform:uppercase}
.board-head .sign b{color:var(--red);font-weight:700}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(178px,1fr));gap:9px}
@media(max-width:520px){.grid{grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:7px}}

.plate{
 display:block;width:100%;border:0;text-align:center;cursor:pointer;font:inherit;
 padding:11px 9px 10px;border-radius:2px;
 transition:transform .22s cubic-bezier(.2,.8,.3,1),filter .22s,box-shadow .22s;
 transform:translateZ(0)}
.plate:hover,.plate:focus-visible{
 transform:translateY(-4px) scale(1.035);filter:brightness(1.18) saturate(1.05);z-index:6;
 box-shadow:
   inset 0 1px 0 rgba(255,255,255,.8), inset 0 -1px 0 rgba(0,0,0,.4),
   0 10px 22px rgba(0,0,0,.7), 0 0 26px rgba(255,230,188,.24)}
.plate .yr{display:block;font-family:var(--mono);font-size:10px;font-weight:600;letter-spacing:.13em;
 color:#5C6058;text-shadow:0 1px 0 rgba(255,255,255,.4)}
.plate .nm{display:block;font-family:var(--inscribe);font-weight:600;font-size:.82rem;line-height:1.24;
 letter-spacing:.035em;margin-top:5px;text-transform:uppercase}
.plate .nm.two{font-size:.68rem;letter-spacing:.01em}
.plate.now{box-shadow:inset 0 0 0 1.5px var(--red-dim),inset 0 1px 0 rgba(255,255,255,.6),0 2px 5px rgba(0,0,0,.55)}
.plate .dot{position:absolute;top:5px;right:6px;width:4px;height:4px;border-radius:50%;background:var(--red);opacity:.85}
.plate.hidden{display:none}
.plate .depth{display:block;height:2px;margin:8px 5px 0;background:rgba(0,0,0,.26);border-radius:2px;overflow:hidden}
.plate .depth i{display:block;height:100%;background:linear-gradient(90deg,var(--red-dim),var(--red));opacity:.75}

/* ---- controls ---- */
.bar{position:relative;z-index:2;display:flex;gap:7px;flex-wrap:wrap;justify-content:center;
 padding:26px 0 4px;max-width:1180px;margin:0 auto}
.chip{font-family:var(--mono);font-size:10px;letter-spacing:.13em;text-transform:uppercase;padding:6px 12px;
 border:1px solid rgba(255,255,255,.13);background:rgba(255,255,255,.03);color:var(--txt2);cursor:pointer;
 border-radius:2px;transition:.16s}
.chip:hover{border-color:rgba(255,230,188,.5);color:var(--tungsten)}
.chip[aria-pressed="true"]{background:var(--tungsten);border-color:var(--tungsten);color:#14161A;font-weight:600}
.readout{text-align:center;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;
 color:var(--txt3);padding:16px 0 60px;position:relative;z-index:2}

/* ---- the unlock panel ---- */
.scrim{position:fixed;inset:0;z-index:70;background:rgba(4,5,7,.86);backdrop-filter:blur(7px);
 opacity:0;pointer-events:none;transition:opacity .34s}
.scrim.open{opacity:1;pointer-events:auto}
.panel{position:fixed;z-index:71;inset:auto 0 0 0;max-height:88vh;overflow-y:auto;
 background:linear-gradient(180deg,#15181C 0%,#0C0E11 100%);
 border-top:1px solid rgba(255,230,188,.22);
 box-shadow:0 -30px 90px rgba(0,0,0,.9), 0 -1px 0 rgba(255,255,255,.06) inset;
 transform:translateY(102%);transition:transform .46s cubic-bezier(.16,.84,.28,1)}
.panel.open{transform:none}
@media(prefers-reduced-motion:reduce){.panel,.scrim{transition:none}}
.panel-in{max-width:1000px;margin:0 auto;padding:38px 30px 60px}
.panel .close{position:absolute;top:16px;right:20px;background:none;border:1px solid rgba(255,255,255,.16);
 color:var(--txt2);font-family:var(--mono);font-size:10px;letter-spacing:.16em;padding:7px 12px;cursor:pointer;border-radius:2px}
.panel .close:hover{border-color:var(--tungsten);color:var(--tungsten)}
.p-year{font-family:var(--inscribe);font-weight:700;font-size:clamp(2.4rem,6vw,4rem);letter-spacing:.03em;
 margin:0;line-height:1;text-shadow:0 0 40px rgba(255,230,188,.22)}
.p-org{margin-top:8px}
.p-leads{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 6px}
.p-lead{padding:12px 17px;border-radius:2px;min-width:190px}
.p-lead b{display:block;font-family:var(--inscribe);font-weight:600;font-size:1rem;letter-spacing:.03em;text-transform:uppercase}
.p-lead .role{font-family:var(--mono);font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;margin-top:4px;color:#4E524B}
.p-lead .role .w{color:var(--red-dim);font-weight:600}
.p-note{border-left:2px solid var(--tungsten-dim);padding:11px 15px;margin:16px 0 0;
 background:rgba(255,230,188,.05);font-size:.92rem;color:var(--txt2)}
.p-note b{color:var(--txt)}
.p-hr{border:0;border-top:1px solid rgba(255,255,255,.09);margin:30px 0 22px}
.ev{display:grid;grid-template-columns:96px 1fr;gap:20px;padding:17px 0;border-bottom:1px solid rgba(255,255,255,.06)}
@media(max-width:640px){.ev{grid-template-columns:1fr;gap:5px}}
.ev .d{font-family:var(--mono);font-size:11px;color:var(--tungsten-dim);padding-top:3px;letter-spacing:.04em}
.ev h4{font-family:var(--inscribe);font-weight:600;font-size:1.02rem;margin:0 0 7px;letter-spacing:.02em;color:var(--txt)}
.ev p{margin:0;color:var(--txt2);font-size:.94rem}
.ev .cite{display:inline-block;margin-top:9px;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;
 text-transform:uppercase;color:var(--tungsten-dim);border:1px solid rgba(255,230,188,.3);
 padding:3px 8px;text-decoration:none;border-radius:2px}
.ev .cite:hover{background:rgba(255,230,188,.14);color:var(--tungsten)}
.p-empty{border:1px dashed rgba(255,255,255,.16);padding:24px;color:var(--txt3);font-size:.94rem;border-radius:2px}
.p-foot{display:flex;gap:14px;flex-wrap:wrap;margin-top:26px}
.p-foot a{font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;
 text-decoration:none;border:1px solid rgba(255,230,188,.35);padding:10px 16px;border-radius:2px}
.p-foot a:hover{background:rgba(255,230,188,.12)}
"""

# ---------------------------------------------------------------- year page
PAGE_CSS = """
.room{position:fixed;inset:0;z-index:0;pointer-events:none;
 background:radial-gradient(120% 70% at 50% -10%, rgba(255,230,188,.10) 0%, transparent 55%),
 linear-gradient(180deg,var(--room) 0%,var(--void) 60%)}
.nav{position:relative;z-index:2;border-bottom:1px solid rgba(255,255,255,.07)}
.nav .wrap{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:15px 30px;flex-wrap:wrap}
.nav a{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;text-decoration:none;color:var(--txt2)}
.nav a:hover{color:var(--tungsten)}
.nav .brand{font-family:var(--inscribe);font-weight:700;letter-spacing:.14em;color:var(--txt);font-size:.9rem}
.nav .brand b{color:var(--red)}
.yhead{position:relative;z-index:2;padding:60px 0 34px}
.yhead h1{font-family:var(--inscribe);font-weight:700;font-size:clamp(3rem,8vw,5.2rem);letter-spacing:.02em;
 margin:8px 0 0;line-height:1;text-shadow:0 0 46px rgba(255,230,188,.24)}
.leads{display:flex;gap:11px;flex-wrap:wrap;margin-top:26px}
.lead{padding:13px 18px;border-radius:2px;min-width:200px}
.lead b{display:block;font-family:var(--inscribe);font-weight:600;font-size:1.02rem;letter-spacing:.03em;text-transform:uppercase}
.lead .role{font-family:var(--mono);font-size:9.5px;letter-spacing:.15em;text-transform:uppercase;margin-top:4px;color:#4E524B}
.lead .role .w{color:var(--red-dim);font-weight:600}
.cols{position:relative;z-index:2;display:grid;grid-template-columns:1.45fr .55fr;gap:48px;padding:34px 0 20px}
@media(max-width:900px){.cols{grid-template-columns:1fr;gap:30px}}
h2.sub{font-family:var(--inscribe);font-weight:600;font-size:1.1rem;letter-spacing:.13em;text-transform:uppercase;
 margin:0 0 18px;color:var(--txt2)}
.note{border-left:2px solid var(--tungsten-dim);background:rgba(255,230,188,.05);padding:12px 16px;margin:0 0 18px;
 font-size:.93rem;color:var(--txt2)}
.note b{color:var(--txt)}
.ev{display:grid;grid-template-columns:96px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.06)}
@media(max-width:640px){.ev{grid-template-columns:1fr;gap:5px}}
.ev .d{font-family:var(--mono);font-size:11px;color:var(--tungsten-dim);padding-top:3px}
.ev h3{font-family:var(--inscribe);font-weight:600;font-size:1.04rem;margin:0 0 7px;letter-spacing:.02em}
.ev p{margin:0;color:var(--txt2);font-size:.95rem}
.ev .cite{display:inline-block;margin-top:9px;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;
 text-transform:uppercase;color:var(--tungsten-dim);border:1px solid rgba(255,230,188,.3);padding:3px 8px;
 text-decoration:none;border-radius:2px}
.ev .cite:hover{background:rgba(255,230,188,.14);color:var(--tungsten)}
.empty{border:1px dashed rgba(255,255,255,.16);padding:24px;color:var(--txt3);font-size:.94rem;border-radius:2px}
.dig{border:1px solid rgba(255,255,255,.09);background:rgba(255,255,255,.02);padding:20px 18px;
 position:sticky;top:18px;max-height:88vh;overflow:auto;border-radius:2px}
.dig h2{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;margin:0 0 3px;color:var(--red)}
.dig h3{font-family:var(--mono);font-size:9.5px;letter-spacing:.15em;text-transform:uppercase;margin:18px 0 4px;color:var(--txt3)}
.dig .lede{font-size:.82rem;color:var(--txt3);margin:0 0 8px;line-height:1.45}
.dig a.q{display:block;text-decoration:none;padding:7px 0;border-top:1px solid rgba(255,255,255,.07);
 font-family:var(--mono);font-size:10.5px;color:var(--tungsten-dim);line-height:1.4}
.dig a.q:hover{color:var(--tungsten)}
.pager{position:relative;z-index:2;display:flex;justify-content:space-between;gap:18px;padding:26px 0 70px;
 border-top:1px solid rgba(255,255,255,.09);flex-wrap:wrap}
.pager a{font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-decoration:none;max-width:46%;color:var(--txt3)}
.pager a b{display:block;font-family:var(--inscribe);font-size:1.05rem;color:var(--txt);margin-top:4px;letter-spacing:.04em}
.pager a:hover b{color:var(--tungsten)}
.pager .r{text-align:right;margin-left:auto}
"""

ORG_TERMS = ['"student government association"', '"associated student government"',
             '"student government"', 'SGA', 'ASG', '"student regent"']
DQ = chr(34)


def q(s):
    return urllib.parse.quote_plus(s)


def year_searches(y):
    return [(f'{t} {cal}',
             f'https://www.google.com/search?q=site:digitalcommons.wku.edu+{q(t)}+{cal}')
            for cal in (y["start"], y["end"]) for t in ORG_TERMS]


def name_searches(name):
    org = " OR ".join(ORG_TERMS)
    return [
        (f'{name} + SGA terms',
         f'https://www.google.com/search?q=site:digitalcommons.wku.edu+{q(DQ+name+DQ)}+{q("("+org+")")}'),
        (f'{name} on TopSCHOLAR',
         f'https://www.google.com/search?q=site:digitalcommons.wku.edu+{q(DQ+name+DQ)}'),
        (f'{name} in WKU Timeline',
         f'https://www.google.com/search?q=site:digitalcommons.wku.edu/wku_timeline+{q(DQ+name+DQ)}'),
        (f'{name} in the Herald',
         f'https://wkuherald.com/?s={q(name)}'),
    ]


def role_flags(l):
    out = []
    if l["role"] == "regent":
        out.append('<span class="w">student regent</span>')
    elif l["role"] == "unresolved":
        out.append('<span class="w">role unresolved</span>')
    else:
        out.append("president")
    if l.get("year_confidence") == "ambiguous":
        out.append('<span class="w">year uncertain</span>')
    if l.get("missing_from_plaque"):
        out.append('<span class="w">not on the wall</span>')
    if l.get("current"):
        out.append("in office")
    out.append(f'plaque: {l["plaque_term"]}')
    return " &middot; ".join(out)


def shell(title, body, css, depth, extra_head=""):
    up = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#08090B">
<meta name="description" content="Sixty years of student government at Western Kentucky University, 1966-2026.">
<title>{title}</title>{FONTS}<style>{BASE}{css}</style>{extra_head}</head><body>
<div class="room"></div>
{body}
</body></html>"""


# ---------------------------------------------------------------- year page
def render_year(y, prev, nxt):
    leads = "".join(
        f'<div class="lead plate-face engraved"><b>{l["name"]}</b>'
        f'<div class="role">{role_flags(l)}</div></div>' for l in y["leaders"])

    notes = "".join(f'<div class="note"><b>{l["name"]}:</b> {l["note"]}</div>'
                    for l in y["leaders"] if l.get("note"))

    if y["events"]:
        evs = "".join(
            f'<article class="ev"><div class="d">{e["date"]}</div><div>'
            f'<h3>{e["title"]}</h3><p>{e["body"]}</p>'
            + (f'<a class="cite" href="{e["src"]["url"]}" target="_blank" rel="noopener">{e["src"]["label"]} &#8599;</a>'
               if e.get("src") else "") + '</div></article>'
            for e in sorted(y["events"], key=lambda e: e["date"]))
    else:
        evs = ('<div class="empty">Nothing logged for this year yet. Run the sweep on the right &mdash; six '
               'keywords against each calendar year &mdash; then add what you find to '
               '<code>data/years.json</code>.</div>')

    nq = "".join(f'<h3>Check: {l["name"]}</h3>' + "".join(
        f'<a class="q" href="{u}" target="_blank" rel="noopener">{lab} &#8599;</a>'
        for lab, u in name_searches(l["name"])) for l in y["leaders"])
    yq = "".join(f'<a class="q" href="{u}" target="_blank" rel="noopener">{lab} &#8599;</a>'
                 for lab, u in year_searches(y))

    pager = ""
    if prev:
        pager += f'<a href="{prev["id"]}.html">&larr; previous<b>{prev["id"]}</b></a>'
    if nxt:
        pager += f'<a class="r" href="{nxt["id"]}.html">next &rarr;<b>{nxt["id"]}</b></a>'

    body = f"""
<nav class="nav"><div class="wrap">
 <a class="brand" href="../index.html">SGA <b>60</b></a>
 <div style="display:flex;gap:20px"><a href="../index.html">The Board</a><a href="../history.html">Timeline</a></div>
</div></nav>
<header class="yhead"><div class="wrap">
 <div class="eyebrow">{y['org']}</div>
 <h1>{y['id']}</h1>
 <div class="leads">{leads}</div>
</div></header>
<div class="wrap"><div class="cols">
 <div>{notes}<h2 class="sub">What happened, in order</h2>{evs}</div>
 <aside><div class="dig">
  <h2>Dig here</h2>
  <p class="lede">Verify the name first &mdash; plaque years are disputed. Then sweep the year.</p>
  {nq}<h3>Year sweep &mdash; {y['start']} &amp; {y['end']}</h3>{yq}
 </div></aside>
</div><div class="pager">{pager}</div></div>"""
    return shell(f"{y['id']} · SGA 60", body, PAGE_CSS, depth=1)


# ---------------------------------------------------------------- index
def render_index(ys):
    tot = len(ys)
    evn = sum(len(y["events"]) for y in ys)
    done = sum(1 for y in ys if y["status"] == "researched")
    open_q = sum(1 for y in ys for l in y["leaders"]
                 if l["role"] == "unresolved" or l.get("year_confidence") == "ambiguous")

    plates = []
    for y in ys:
        names = [l["name"] for l in y["leaders"]]
        cls = ["plate", "plate-face", "engraved"]
        if any(l.get("current") for l in y["leaders"]):
            cls.append("now")
        flag = any(l["role"] == "unresolved" or l.get("year_confidence") == "ambiguous"
                   for l in y["leaders"])
        tags = f"d{(y['start']//10)*10} {y['status']} {'flagged' if flag else 'clean'}"
        pct = min(len(y["events"]), 5) * 20
        plates.append(
            f'<button class="{" ".join(cls)}" data-y="{y["id"]}" data-tags="{tags}" '
            f'style="position:relative" aria-label="Open the record for {y["id"]}">'
            + ('<span class="dot"></span>' if flag else '')
            + f'<span class="yr">{y["id"]}</span>'
            + f'<span class="nm{" two" if len(names) > 1 else ""}">{" · ".join(names)}</span>'
            + f'<span class="depth"><i style="width:{pct}%"></i></span></button>')

    # trimmed payload for the unlock panel
    payload = json.dumps({y["id"]: {
        "org": y["org"],
        "leaders": [{"name": l["name"], "flags": role_flags(l), "note": l.get("note", "")}
                    for l in y["leaders"]],
        "events": sorted(y["events"], key=lambda e: e["date"]),
    } for y in ys}, ensure_ascii=False, separators=(",", ":"))

    body = f"""
<div class="beam"></div><div class="grain"></div>

<header class="top"><div class="wrap">
 <div class="eyebrow">Western Kentucky University &middot; 1966&ndash;2026</div>
 <h1>Sixty Years on the Hill</h1>
 <p class="sub">Every student body president and student regent since the Associated Students were
 ratified in April 1966. Touch a plate to open that year.</p>
</div></header>

<div class="stage"><div class="board" id="board"><div class="board-inner">
 <div class="board-head"><div class="sign plate-face engraved">WKU Student <b>Government</b> Association</div></div>
 <div class="grid" id="grid">{''.join(plates)}</div>
</div></div></div>

<div class="bar" role="group" aria-label="Filter the wall">
 <button class="chip" data-f="all" aria-pressed="true">All</button>
 <button class="chip" data-f="d1960" aria-pressed="false">60s</button>
 <button class="chip" data-f="d1970" aria-pressed="false">70s</button>
 <button class="chip" data-f="d1980" aria-pressed="false">80s</button>
 <button class="chip" data-f="d1990" aria-pressed="false">90s</button>
 <button class="chip" data-f="d2000" aria-pressed="false">00s</button>
 <button class="chip" data-f="d2010" aria-pressed="false">10s</button>
 <button class="chip" data-f="d2020" aria-pressed="false">20s</button>
 <button class="chip" data-f="flagged" aria-pressed="false">Disputed</button>
 <button class="chip" data-f="empty" aria-pressed="false">Unresearched</button>
</div>
<p class="readout"><span id="readout"></span> &nbsp;&middot;&nbsp; {evn} events logged &nbsp;&middot;&nbsp;
 {done} of {tot} years complete &nbsp;&middot;&nbsp; {open_q} names still disputed &nbsp;&middot;&nbsp;
 <a href="history.html">the full timeline &#8599;</a></p>

<div class="scrim" id="scrim"></div>
<aside class="panel" id="panel" role="dialog" aria-modal="true" aria-labelledby="pYear">
 <button class="close" id="close">Close &times;</button>
 <div class="panel-in" id="panelIn"></div>
</aside>

<script>
const D={payload};
const board=document.getElementById('board'),grid=document.getElementById('grid'),
 scrim=document.getElementById('scrim'),panel=document.getElementById('panel'),
 pin=document.getElementById('panelIn'),readout=document.getElementById('readout');
const RM=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* the wall tilts with the mouse */
if(!RM){{
 let raf;
 window.addEventListener('mousemove',e=>{{
  if(raf)return;
  raf=requestAnimationFrame(()=>{{
   const x=(e.clientX/window.innerWidth-.5),y=(e.clientY/window.innerHeight-.5);
   board.style.transform=`rotateY(${{x*4.4}}deg) rotateX(${{-y*2.6}}deg)`;
   raf=null;
  }});
 }},{{passive:true}});
}}

function esc(s){{return String(s).replace(/[&<>]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c]));}}

function openYear(id){{
 const y=D[id]; if(!y)return;
 const leads=y.leaders.map(l=>`<div class="p-lead plate-face engraved"><b>${{esc(l.name)}}</b>
   <div class="role">${{l.flags}}</div></div>`).join('');
 const notes=y.leaders.filter(l=>l.note).map(l=>
   `<div class="p-note"><b>${{esc(l.name)}}:</b> ${{esc(l.note)}}</div>`).join('');
 const evs=y.events.length
  ? y.events.map(e=>`<article class="ev"><div class="d">${{esc(e.date)}}</div><div>
      <h4>${{esc(e.title)}}</h4><p>${{esc(e.body)}}</p>
      ${{e.src?`<a class="cite" href="${{e.src.url}}" target="_blank" rel="noopener">${{esc(e.src.label)}} &#8599;</a>`:''}}
      </div></article>`).join('')
  : `<div class="p-empty">This year has not been researched yet. Open the full page for the
     pre-built archive searches.</div>`;
 pin.innerHTML=`<div class="eyebrow">${{esc(y.org)}}</div>
  <h2 class="p-year" id="pYear">${{esc(id)}}</h2>
  <div class="p-leads">${{leads}}</div>${{notes}}
  <hr class="p-hr"><h3 class="eyebrow" style="margin-bottom:14px">What happened, in order</h3>${{evs}}
  <div class="p-foot"><a href="y/${{id}}.html">Full record &amp; archive searches &#8599;</a>
  <a href="history.html">The whole timeline &#8599;</a></div>`;
 scrim.classList.add('open');panel.classList.add('open');
 document.body.style.overflow='hidden';
 history.replaceState(null,'','#'+id);
 panel.scrollTop=0;document.getElementById('close').focus();
}}
function closeYear(){{
 scrim.classList.remove('open');panel.classList.remove('open');
 document.body.style.overflow='';history.replaceState(null,'',location.pathname);
}}
grid.addEventListener('click',e=>{{const b=e.target.closest('.plate');if(b)openYear(b.dataset.y);}});
scrim.addEventListener('click',closeYear);
document.getElementById('close').addEventListener('click',closeYear);
document.addEventListener('keydown',e=>{{if(e.key==='Escape')closeYear();}});

const chips=[...document.querySelectorAll('.chip')],plates=[...document.querySelectorAll('.plate')];
function apply(f){{
 let n=0;
 plates.forEach(el=>{{const ok=f==='all'||el.dataset.tags.split(' ').includes(f);
  el.classList.toggle('hidden',!ok);if(ok)n++;}});
 readout.textContent=n+' of '+plates.length+' plates lit';
 chips.forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.f===f)));
}}
chips.forEach(c=>c.addEventListener('click',()=>apply(c.dataset.f)));
apply('all');
if(location.hash && D[location.hash.slice(1)]) openYear(location.hash.slice(1));
</script>"""
    return shell("SGA 60 · Sixty Years on the Hill", body, INDEX_CSS, depth=0)


def main():
    ys = json.loads(DATA.read_text())["years"]
    YDIR.mkdir(parents=True, exist_ok=True)
    (SITE / "index.html").write_text(render_index(ys))
    for i, y in enumerate(ys):
        (YDIR / f'{y["id"]}.html').write_text(
            render_year(y, ys[i - 1] if i else None, ys[i + 1] if i < len(ys) - 1 else None))
    shutil.copy(DATA, SITE / "years.json")
    print(f'built the board + {len(ys)} year pages -> {SITE}')


if __name__ == "__main__":
    main()
