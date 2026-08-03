#!/usr/bin/env python3
"""
SGA 60 site generator — the lit wall.

Reads  data/years.json
Writes site/index.html   the board
       site/y/<year>.html one page per academic year

Pure Python. No AI, no API key, no network.
"""
import html as html_mod
import json, shutil, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "years.json"
DOCS = ROOT / "data" / "documents"
PHOTOS = ROOT / "data" / "photos"
LEG = ROOT / "data" / "legislation"
LEGMETA = ROOT / "data" / "legislation.json"
SITE = ROOT / "site"
YDIR = SITE / "y"

def h(s):
    return html_mod.escape(str(s), quote=True)

# San Francisco on Apple devices via the system font stack; graceful fallbacks
# elsewhere. No webfont downloads, no external requests, instant rendering.
FONTS = ""

# ---------------------------------------------------------------- tokens
BASE = """
:root{
 --red:#B01E24; --red-dark:#8E1218; --black:#0B0B0C;
 --ink:#151517; --ink2:#4C4C4F; --ink3:#8A8A8E;
 --paper:#FFFFFF; --paper2:#F7F6F3; --line:#E7E4DF;
 --inscribe:-apple-system,BlinkMacSystemFont,"SF Pro Display","Segoe UI",Roboto,Helvetica,sans-serif;
 --ui:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,sans-serif;
 --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--ui);
 font-size:clamp(15px,0.35vw + 13.8px,18px);line-height:1.65;
 -webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:var(--red);text-underline-offset:3px;text-decoration-thickness:1px}
a:hover{color:var(--red-dark)}
:focus-visible{outline:2px solid var(--red);outline-offset:3px;border-radius:3px}
.eyebrow{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--red)}
.wrap{max-width:1200px;margin:0 auto;padding:0 30px}
@media(max-width:640px){.wrap{padding:0 18px}}

/* plaque plates: clean white cards on the black wall */
.plate-face{background:var(--paper);border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,.25);position:relative}
.engraved{color:var(--ink)}

/* ---- Big Red ---- */
.bigred{position:fixed;right:18px;bottom:10px;z-index:80;cursor:pointer;user-select:none;-webkit-user-select:none;line-height:0}
.bigred svg{display:block;filter:drop-shadow(0 8px 14px rgba(0,0,0,.28));image-rendering:pixelated}
.bigred .close{position:absolute;top:-12px;right:-6px;width:22px;height:22px;border-radius:50%;
 border:1px solid var(--line);background:var(--paper);color:var(--ink2);font-size:13px;line-height:19px;
 text-align:center;cursor:pointer;padding:0;font-family:var(--ui)}
.bigred .close:hover{color:var(--red);border-color:var(--red)}
.bigred .say{position:absolute;bottom:100%;right:8%;margin-bottom:12px;background:var(--black);color:#fff;
 font-family:var(--mono);font-size:11px;letter-spacing:.06em;padding:8px 12px;border-radius:8px;white-space:nowrap;
 opacity:0;transform:translateY(6px);transition:.25s;pointer-events:none;line-height:1.4}
.bigred .say:after{content:"";position:absolute;top:100%;right:22px;border:6px solid transparent;border-top-color:var(--black)}
.bigred.talk .say{opacity:1;transform:none}
.bigred .gavel{transform-origin:122px 70px}
@keyframes br-bounce{0%,100%{transform:none}30%{transform:translateY(-28px) rotate(-5deg)}60%{transform:translateY(0) rotate(3deg)}80%{transform:translateY(-10px)}}
@keyframes br-spin{to{transform:rotate(360deg)}}
@keyframes br-bang{0%,100%{transform:rotate(0)}35%{transform:rotate(-60deg)}55%{transform:rotate(16deg)}75%{transform:rotate(-8deg)}}
.bigred.bounce{animation:br-bounce .9s cubic-bezier(.3,.7,.3,1)}
.bigred.spin{animation:br-spin .8s ease}
.bigred.bang .gavel{animation:br-bang .7s ease}
@media(prefers-reduced-motion:reduce){.bigred,.bigred .gavel{animation:none!important}}
"""

# ---------------------------------------------------------------- index
INDEX_CSS = """
.room,.beam,.grain{display:none}
header.top{padding:64px 0 30px;text-align:center}
header.top h1{font-family:var(--inscribe);font-weight:800;font-size:clamp(2rem,3.8vw,3.2rem);
 letter-spacing:-.015em;margin:14px 0 0;color:var(--ink)}
header.top .sub{color:var(--ink2);max-width:58ch;margin:16px auto 0;font-size:1.04rem}

/* ---- the board ---- */
.stage{padding:26px 0 8px}
.board{position:relative;margin:0 auto;max-width:1180px;padding:26px;border-radius:16px;
 background:var(--black);box-shadow:0 24px 60px rgba(0,0,0,.28)}
.board-inner{padding:2px}
.board-head{display:flex;justify-content:center;padding-bottom:20px}
.board-head .sign{font-family:var(--inscribe);font-weight:700;font-size:clamp(.9rem,1.5vw,1.12rem);
 letter-spacing:.12em;padding:11px 28px;border-radius:10px;text-transform:uppercase;
 background:var(--red);color:#fff;box-shadow:none;border:0}
.board-head .sign b{color:#fff;font-weight:800}
.board-head .sign::before{display:none}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(178px,1fr));gap:10px}
@media(max-width:520px){.grid{grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px}}
.plate{display:block;width:100%;border:0;text-align:center;cursor:pointer;font:inherit;
 padding:14px 10px 12px;border-radius:8px;transition:transform .18s,box-shadow .18s}
.plate::before{display:none}
.plate:hover,.plate:focus-visible{transform:translateY(-3px);box-shadow:0 10px 22px rgba(0,0,0,.4)}
.plate .yr{display:block;font-family:var(--mono);font-size:10.5px;font-weight:600;letter-spacing:.12em;color:var(--red)}
.plate .nm{display:block;font-family:var(--inscribe);font-weight:700;font-size:.86rem;line-height:1.3;
 letter-spacing:0;margin-top:5px;color:var(--ink);text-transform:none}
.plate .nm.two{font-size:.72rem}
.plate.now{box-shadow:inset 0 0 0 2px var(--red)}
.plate .dot{position:absolute;top:7px;right:8px;width:5px;height:5px;border-radius:50%;background:var(--red)}
.plate.hidden{display:none}
.plate .depth{display:block;height:3px;margin:9px 6px 0;background:#EFEDE9;border-radius:3px;overflow:hidden}
.plate .depth i{display:block;height:100%;background:var(--red)}

/* ---- controls ---- */
.bar{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;padding:26px 0 4px;max-width:1180px;margin:0 auto}
.chip{font-family:var(--ui);font-size:13px;font-weight:500;padding:6px 15px;border:1px solid var(--line);
 background:var(--paper);color:var(--ink2);cursor:pointer;border-radius:999px;transition:.16s}
.chip:hover{border-color:var(--red);color:var(--red)}
.chip[aria-pressed="true"]{background:var(--red);border-color:var(--red);color:#fff;font-weight:600}
.readout{text-align:center;font-size:.85rem;color:var(--ink3);padding:16px 0 80px}

.search{display:block;width:100%;max-width:520px;margin:26px auto 0;background:var(--paper);
 border:1px solid var(--line);color:var(--ink);font-family:var(--ui);font-size:16px;
 padding:12px 18px;border-radius:999px;box-shadow:0 2px 8px rgba(0,0,0,.05)}
.search:focus{outline:2px solid var(--red);outline-offset:2px}

/* ---- the panel ---- */
.scrim{position:fixed;inset:0;z-index:70;background:rgba(11,11,12,.5);opacity:0;pointer-events:none;transition:opacity .3s}
.scrim.open{opacity:1;pointer-events:auto}
.panel{position:fixed;z-index:71;inset:auto 0 0 0;max-height:88vh;overflow-y:auto;background:var(--paper);
 border-top:4px solid var(--red);border-radius:18px 18px 0 0;box-shadow:0 -20px 60px rgba(0,0,0,.3);
 transform:translateY(102%);transition:transform .42s cubic-bezier(.16,.84,.28,1)}
.panel.open{transform:none}
@media(prefers-reduced-motion:reduce){.panel,.scrim{transition:none}}
.panel-in{max-width:1000px;margin:0 auto;padding:40px 30px 70px}
.panel .close{position:absolute;top:16px;right:20px;background:none;border:1px solid var(--line);
 color:var(--ink2);font-family:var(--ui);font-size:13px;padding:7px 14px;cursor:pointer;border-radius:999px}
.panel .close:hover{border-color:var(--red);color:var(--red)}
.p-year{font-family:var(--inscribe);font-weight:800;font-size:clamp(2.3rem,6vw,3.6rem);letter-spacing:-.02em;margin:0;line-height:1;color:var(--ink)}
.p-org{margin-top:8px}
.p-leads{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 6px}
.p-lead{padding:13px 18px;border-radius:10px;min-width:190px;border:1px solid var(--line);box-shadow:none}
.p-lead b{display:block;font-family:var(--inscribe);font-weight:700;font-size:1.02rem;text-transform:none;letter-spacing:0}
.p-lead .role{font-size:.78rem;margin-top:4px;color:var(--ink3);font-family:var(--ui);letter-spacing:.02em;text-transform:none}
.p-lead .role .w{color:var(--red);font-weight:600}
.p-note{border-left:3px solid var(--red);padding:12px 16px;margin:16px 0 0;background:var(--paper2);
 border-radius:0 8px 8px 0;font-size:.94rem;color:var(--ink2)}
.p-note b{color:var(--ink)}
.p-hr{border:0;border-top:1px solid var(--line);margin:30px 0 22px}
.ev{display:grid;grid-template-columns:96px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid var(--line)}
@media(max-width:640px){.ev{grid-template-columns:1fr;gap:5px}}
.ev .d{font-family:var(--mono);font-size:12px;color:var(--red);padding-top:4px;font-weight:600}
.ev .ctx{display:block;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);margin-top:5px;font-family:var(--ui)}
.ev h4{font-family:var(--inscribe);font-weight:700;font-size:1.05rem;margin:0 0 7px;color:var(--ink)}
.ev p{margin:0;color:var(--ink2);font-size:.95rem}
.ev .cite{display:inline-block;margin-top:8px;margin-right:14px;font-size:.85rem;color:var(--red);
 border:0;padding:0;text-decoration:underline;text-underline-offset:3px;text-transform:none;font-family:var(--ui);letter-spacing:0}
.ev .cite:hover{background:none;color:var(--red-dark)}
.p-empty{border:1px dashed var(--line);padding:24px;color:var(--ink3);font-size:.94rem;border-radius:10px}
.p-foot{display:flex;gap:20px;flex-wrap:wrap;margin-top:28px}
.p-foot a{font-size:.92rem;font-weight:600;text-decoration:underline;text-underline-offset:3px;border:0;padding:0;
 font-family:var(--ui);letter-spacing:0;text-transform:none}
.p-foot a:hover{background:none}
"""

# ---------------------------------------------------------------- year page
PAGE_CSS = """
.room{display:none}
.nav{background:var(--black)}
.nav .wrap{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:15px 30px;flex-wrap:wrap}
.nav a{font-size:.85rem;font-weight:500;text-decoration:none;color:rgba(255,255,255,.75);
 font-family:var(--ui);letter-spacing:.02em;text-transform:none}
.nav a:hover{color:#fff}
.nav .brand{font-family:var(--inscribe);font-weight:800;letter-spacing:.06em;color:#fff;font-size:1rem}
.nav .brand b{color:var(--red)}
.yhead{padding:56px 0 30px;border-bottom:1px solid var(--line)}
.yhead h1{font-family:var(--inscribe);font-weight:800;font-size:clamp(2.8rem,7vw,4.6rem);letter-spacing:-.02em;
 margin:8px 0 0;line-height:1;color:var(--ink)}
.leads{display:flex;gap:11px;flex-wrap:wrap;margin-top:24px}
.lead{padding:13px 18px;border-radius:10px;min-width:200px;border:1px solid var(--line);box-shadow:none}
.lead b{display:block;font-family:var(--inscribe);font-weight:700;font-size:1.02rem;text-transform:none;letter-spacing:0}
.lead .role{font-size:.78rem;margin-top:4px;color:var(--ink3);font-family:var(--ui);letter-spacing:.02em;text-transform:none}
.lead .role .w{color:var(--red);font-weight:600}
.cols{display:grid;grid-template-columns:1.45fr .55fr;gap:48px;padding:34px 0 20px}
@media(max-width:900px){.cols{grid-template-columns:1fr;gap:30px}}
h2.sub{font-family:var(--inscribe);font-weight:700;font-size:1.05rem;letter-spacing:.01em;margin:34px 0 14px;
 color:var(--ink);text-transform:none;border-bottom:2px solid var(--red);display:inline-block;padding-bottom:4px}
.note{border-left:3px solid var(--red);background:var(--paper2);border-radius:0 8px 8px 0;
 padding:12px 16px;margin:0 0 18px;font-size:.93rem;color:var(--ink2)}
.note b{color:var(--ink)}
.ev{display:grid;grid-template-columns:96px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid var(--line)}
@media(max-width:640px){.ev{grid-template-columns:1fr;gap:5px}}
.ev .d{font-family:var(--mono);font-size:12px;color:var(--red);padding-top:4px;font-weight:600}
.ev .ctx{display:block;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);margin-top:5px;font-family:var(--ui)}
.ev h3{font-family:var(--inscribe);font-weight:700;font-size:1.06rem;margin:0 0 7px;color:var(--ink)}
.ev p{margin:0;color:var(--ink2);font-size:.95rem}
.ev .cite{display:inline-block;margin-top:8px;margin-right:14px;font-size:.85rem;color:var(--red);border:0;padding:0;
 text-decoration:underline;text-underline-offset:3px;text-transform:none;font-family:var(--ui);letter-spacing:0}
.ev .cite:hover{background:none;color:var(--red-dark)}
.empty{border:1px dashed var(--line);padding:24px;color:var(--ink3);font-size:.94rem;border-radius:10px}
.dig{border:1px solid var(--line);background:var(--paper2);padding:20px 18px;position:sticky;top:18px;
 max-height:88vh;overflow:auto;border-radius:12px}
.dig h2{font-size:.8rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin:0 0 3px;color:var(--red);font-family:var(--ui)}
.dig h3{font-size:.72rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin:18px 0 4px;color:var(--ink3);font-family:var(--ui)}
.dig .lede{font-size:.84rem;color:var(--ink3);margin:0 0 8px;line-height:1.5}
.dig a.q{display:block;text-decoration:none;padding:7px 0;border-top:1px solid var(--line);
 font-size:.84rem;color:var(--ink2);line-height:1.4;font-family:var(--ui)}
.dig a.q:hover{color:var(--red)}
.pager{display:flex;justify-content:space-between;gap:18px;padding:26px 0 90px;border-top:1px solid var(--line);flex-wrap:wrap}
.pager a{font-size:.8rem;letter-spacing:.04em;text-decoration:none;max-width:46%;color:var(--ink3);font-family:var(--ui)}
.pager a b{display:block;font-family:var(--inscribe);font-size:1.1rem;font-weight:700;color:var(--ink);margin-top:4px}
.pager a:hover b{color:var(--red)}
.pager .r{text-align:right;margin-left:auto}

/* ---- president profiles ---- */
.profile{margin:0 0 26px}
.profile p{color:var(--ink2);font-size:.96rem;margin:0 0 12px}

/* ---- photographs ---- */
.portraits{display:flex;gap:16px;flex-wrap:wrap;margin:26px 0 4px}
.portrait{margin:0;width:160px}
.portrait img{width:100%;height:190px;object-fit:cover;object-position:top;border-radius:10px;
 box-shadow:0 6px 18px rgba(0,0,0,.18)}
.portrait figcaption{font-size:.78rem;color:var(--ink3);margin-top:7px;line-height:1.5}
.portrait figcaption b{display:block;font-family:var(--inscribe);font-size:.92rem;font-weight:700;color:var(--ink)}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px;margin:0 0 28px}
.gallery figure{margin:0}
.gallery img{width:100%;border-radius:10px;box-shadow:0 6px 18px rgba(0,0,0,.18)}
.gallery figcaption{font-size:.84rem;color:var(--ink3);margin-top:7px;line-height:1.5}

/* ---- the organization ---- */
.org{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin:0 0 30px}
@media(max-width:640px){.org{grid-template-columns:1fr}}
.org h3{font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin:0 0 10px;color:var(--red);font-family:var(--ui)}
.off{display:grid;grid-template-columns:auto 1fr;gap:14px;padding:9px 0;border-bottom:1px solid var(--line);font-size:.93rem}
.off .o{font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3);padding-top:4px;min-width:110px;font-family:var(--ui)}
.off b{font-family:var(--inscribe);font-weight:700;color:var(--ink)}
.off p{margin:3px 0 0;color:var(--ink2);font-size:.88rem}
.org .meta{font-size:.88rem;color:var(--ink2);margin:10px 0 0}

/* ---- the archive shelf ---- */
.doc{border:1px solid var(--line);border-radius:12px;margin:0 0 24px;overflow:hidden;background:var(--paper)}
.doc-head{padding:17px 19px 14px}
.doc-head h3{font-family:var(--inscribe);font-weight:700;font-size:1.05rem;margin:0 0 7px;color:var(--ink)}
.doc-head p{margin:0;color:var(--ink2);font-size:.93rem}
.doc-extract{border-left:3px solid var(--red);background:var(--paper2);margin:0 19px 15px;border-radius:0 8px 8px 0;
 padding:12px 16px;font-size:.93rem;color:var(--ink2)}
.doc-extract .from{display:block;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);margin-bottom:6px;font-family:var(--ui)}
.doc-view{display:block;width:100%;height:480px;border:0;border-top:1px solid var(--line);background:var(--paper2)}
.doc-foot{display:flex;gap:18px;flex-wrap:wrap;padding:13px 19px}
.doc-foot a{font-size:.85rem;color:var(--red);border:0;padding:0;text-decoration:underline;text-underline-offset:3px;
 text-transform:none;font-family:var(--ui);letter-spacing:0}
.doc-foot a:hover{background:none;color:var(--red-dark)}

/* ---- legislation ---- */
.lrow{display:grid;grid-template-columns:110px 1fr auto;gap:14px;align-items:baseline;
 padding:11px 0;border-bottom:1px solid var(--line);font-size:.93rem}
@media(max-width:640px){.lrow{grid-template-columns:1fr;gap:4px}}
.ltype{font-family:var(--mono);font-size:11px;letter-spacing:.04em;color:var(--red);font-weight:600}
.lt{color:var(--ink)}
.lls{display:flex;gap:14px;white-space:nowrap}
.lls a{font-size:.85rem;color:var(--red);border:0;padding:0;text-decoration:underline;text-underline-offset:3px;
 text-transform:none;font-family:var(--ui);letter-spacing:0}
.lls a:hover{background:none;color:var(--red-dark)}
.lsec{margin:0 0 34px}
.lcount{font-size:.78rem;color:var(--ink3);font-family:var(--ui);letter-spacing:.02em}
.lfilter{width:100%;max-width:420px;background:var(--paper);border:1px solid var(--line);color:var(--ink);
 font-family:var(--ui);font-size:15px;padding:11px 16px;border-radius:10px;margin:6px 0 26px}
.lfilter:focus{outline:2px solid var(--red);outline-offset:2px}
.ljump{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 22px}
.ljump .chip{font-family:var(--ui);font-size:13px;padding:5px 13px;border:1px solid var(--line);border-radius:999px;
 color:var(--ink2);text-decoration:none}
.ljump .chip:hover{border-color:var(--red);color:var(--red)}
"""



# ---------------------------------------------------------------- big red
_PX = {"R": "#B01E24", "D": "#7E1014", "W": "#FFFFFF", "B": "#1A1A1C", "O": "#8B5A2B"}
_BODY = [
    "......RRRRRRRR........",
    ".....RRRRRRRRRR.......",
    "....RRRRRRRRRRRR......",
    "....RRWWRRRRWWRR......",
    "....RWBWRRRRWBWR......",
    "....RRWWRRRRWWRR......",
    "....RRRRRRRRRRRR......",
    "....RDDDDDDDDDDR......",
    "...RRDBBBBBBBBDRR.....",
    "...RRDDDDDDDDDDRR.....",
    "...RRRRRRRRRRRRRRRR...",
    "...RRRRRRRRRRRRRR.....",
    "...RRR.RRRRRR.RRR.....",
    "...RR...RRRR...RR.....",
    "....R...RRRR...R......",
    "........RRRR..........",
    ".......RRR.RRR........",
    "......RRR...RRR.......",
    "......RR.....RR.......",
]
_GAVEL = [
    "......................",
    "......................",
    "......................",
    "......................",
    "................BBBB..",
    "................BBBB..",
    "................BBBB..",
    ".................OO...",
    ".................OO...",
    ".................OO...",
    ".................OO...",
]


def _pixels(rows):
    out = []
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != ".":
                out.append(f'<rect x="{x*7}" y="{y*7}" width="7.4" height="7.4" fill="{_PX[c]}"/>')
    return "".join(out)


BIGRED = (
    '<div class="bigred" id="bigred" role="img" aria-label="Big Red holding the SGA gavel. Click to play.">'
    '<button class="close" id="brx" aria-label="Dismiss Big Red">&times;</button>'
    '<div class="say" id="brsay">Order, order!</div>'
    f'<svg width="154" height="133" viewBox="0 0 154 133">{_pixels(_BODY)}'
    f'<g class="gavel">{_pixels(_GAVEL)}</g></svg></div>'
    '<script>(function(){var br=document.getElementById("bigred");if(!br)return;'
    'try{if(localStorage.getItem("bigred")==="hidden"){br.remove();return}}catch(e){}'
    'document.getElementById("brx").addEventListener("click",function(e){e.stopPropagation();br.remove();'
    'try{localStorage.setItem("bigred","hidden")}catch(e){}});'
    'var says=["Order, order!","Go Tops!","Sixty years on the Hill.","Motion carries.","The Spirit Makes the Master."],i=0,m=-1;'
    'br.addEventListener("click",function(){br.classList.remove("bounce","spin","bang","talk");void br.offsetWidth;'
    'm=(m+1)%3;if(m===0){br.classList.add("bang","talk");document.getElementById("brsay").textContent=says[i++%says.length];}'
    'else if(m===1){br.classList.add("bounce")}else{br.classList.add("spin")}'
    'clearTimeout(br._t);br._t=setTimeout(function(){br.classList.remove("talk")},1600)});})();</script>'
)

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
""" + BIGRED + """
</body></html>"""


def render_office(o):
    return (f'<div class="off"><span class="o">{o.get("office", "")}</span><span>'
            f'<b>{o.get("name", "")}</b>'
            + (f'<p>{o["note"]}</p>' if o.get("note") else "")
            + (f' <a class="cite" href="{o["src"]["url"]}" target="_blank" rel="noopener">'
               f'{o["src"]["label"]} &#8599;</a>' if o.get("src") else "")
            + '</span></div>')


def render_org(y):
    org = y.get("organization")
    if not org:
        return ""
    exec_rows = "".join(render_office(o) for o in org.get("executive", []))
    sen = org.get("senate", {})
    sen_rows = "".join(render_office(o) for o in sen.get("officers", []))
    sen_rows += "".join(
        f'<div class="off"><span class="o">committee</span><span><b>{c.get("name", "")}</b>'
        + (f'<p>chair: {c["chair"]}</p>' if c.get("chair") else "")
        + (f'<p>{c["note"]}</p>' if c.get("note") else "")
        + '</span></div>' for c in sen.get("committees", []))
    sen_meta = ""
    if sen.get("size"):
        sen_meta += f'<p class="meta">{sen["size"]} senators this year.</p>'
    if sen.get("note"):
        sen_meta += f'<p class="meta">{sen["note"]}</p>'
    if not (exec_rows or sen_rows or sen_meta):
        return ""
    return (f'<h2 class="sub">The organization</h2><div class="org">'
            f'<div><h3>The Executive</h3>{exec_rows or "<p class=meta>Not yet researched.</p>"}</div>'
            f'<div><h3>The Senate</h3>{sen_rows}{sen_meta or ""}'
            + ("<p class=meta>Not yet researched.</p>" if not (sen_rows or sen_meta) else "")
            + '</div></div>')


def render_docs(y):
    docs = y.get("documents")
    if not docs:
        return ""
    out = ['<h2 class="sub">From the archive</h2>']
    for d in docs:
        page = f'#page={d["page"]}' if d.get("page") else ""
        extract = ""
        if d.get("extract"):
            extract = (f'<div class="doc-extract"><span class="from">the part about SGA'
                       + (f' &middot; pages {d["sga_pages"]}' if d.get("sga_pages") else "")
                       + f'</span>{d["extract"]}</div>')
        viewer = (f'<iframe class="doc-view" src="../docs/{d["file"]}{page}" loading="lazy" '
                  f'title="{d.get("title", d["file"])}"></iframe>') if d.get("file") else ""
        links = []
        if d.get("file"):
            links.append(f'<a href="../docs/{d["file"]}" target="_blank" rel="noopener">Open the full file &#8599;</a>')
        if d.get("src"):
            links.append(f'<a href="{d["src"]["url"]}" target="_blank" rel="noopener">{d["src"]["label"]} &#8599;</a>')
        out.append(
            f'<article class="doc"><div class="doc-head"><h3>{d.get("title", d.get("file", ""))}</h3>'
            + (f'<p>{d["summary"]}</p>' if d.get("summary") else "")
            + f'</div>{extract}{viewer}<div class="doc-foot">{"".join(links)}</div></article>')
    return "".join(out)


def render_portraits(y):
    ports = [(l, l["photo"]) for l in y["leaders"] if l.get("photo")]
    if not ports:
        return ""
    figs = "".join(
        f'<figure class="portrait"><img src="../photos/{p["file"]}" alt="{h(l["name"])}" loading="lazy">'
        f'<figcaption><b>{h(l["name"])}</b>'
        + (f'<a class="cite" style="margin-top:5px" href="{h(p["src"]["url"])}" target="_blank" '
           f'rel="noopener">{h(p["src"]["label"])} &#8599;</a>' if p.get("src") else "")
        + '</figcaption></figure>' for l, p in ports)
    return f'<div class="portraits">{figs}</div>'


def render_gallery(y):
    photos = y.get("photos")
    if not photos:
        return ""
    figs = "".join(
        f'<figure><img src="../photos/{p["file"]}" alt="{h(p.get("caption", ""))}" loading="lazy">'
        f'<figcaption>{p.get("caption", "")}'
        + (f' <a class="cite" style="margin-top:5px" href="{h(p["src"]["url"])}" target="_blank" '
           f'rel="noopener">{h(p["src"]["label"])} &#8599;</a>' if p.get("src") else "")
        + '</figcaption></figure>' for p in photos)
    return f'<h2 class="sub">The year in pictures</h2><div class="gallery">{figs}</div>'


def leg_sorted(entries):
    return sorted(entries, key=lambda e: (e.get("date") or "9999-99-99", e["title"]))


def leg_row(e, depth):
    up = "../" * depth
    when = f'<br>{e["date"]}' if e.get("date") else ""
    return (f'<div class="lrow" data-t="{h(e["title"].lower())} {h(e["type"])}">'
            f'<span class="ltype">{h(e["type"])}{when}</span><span class="lt">{h(e["title"])}</span>'
            f'<span class="lls"><a href="{up}legislation/{e["file"]}" target="_blank" rel="noopener">read &#8599;</a>'
            f'<a href="{h(e["source_url"])}" target="_blank" rel="noopener">original &#8599;</a></span></div>')


def render_legislation(entries):
    groups = {}
    for e in entries:
        groups.setdefault(e["session"], []).append(e)
    sessions = sorted((k for k in groups if k not in ("governing", "undated")), reverse=True)
    order = ([("governing", "Governing documents")] if "governing" in groups else []) \
        + [(s, s) for s in sessions] \
        + ([("undated", "Undated")] if "undated" in groups else [])
    jump = "".join(f'<a class="chip" href="#s{k}">{lab}</a>' for k, lab in order)
    secs = "".join(
        f'<section class="lsec" id="s{k}"><h2 class="sub">{lab} '
        f'<span class="lcount">{len(groups[k])} documents</span></h2>'
        + "".join(leg_row(e, 0) for e in leg_sorted(groups[k])) + '</section>'
        for k, lab in order)
    body = f"""
<nav class="nav"><div class="wrap">
 <a class="brand" href="index.html">SGA <b>60</b></a>
 <div style="display:flex;gap:20px"><a href="index.html">The Board</a><a href="history.html">Timeline</a></div>
</div></nav>
<header class="yhead"><div class="wrap">
 <div class="eyebrow">The paper trail &middot; every document readable on this site</div>
 <h1 style="font-size:clamp(2.2rem,6vw,3.6rem)">Legislation</h1>
</div></header>
<div class="wrap" style="position:relative;z-index:2;padding-bottom:70px">
 <input class="lfilter" id="lf" type="search" placeholder="filter by title, type, keyword&hellip;"
  aria-label="Filter legislation">
 <div class="ljump">{jump}</div>
 {secs}
</div>
<script>
const lf=document.getElementById('lf');
lf.addEventListener('input',()=>{{
 const q=lf.value.toLowerCase().trim();
 document.querySelectorAll('.lrow').forEach(r=>{{r.style.display=!q||r.dataset.t.includes(q)?'':'none';}});
 document.querySelectorAll('.lsec').forEach(s=>{{
  s.style.display=[...s.querySelectorAll('.lrow')].some(r=>r.style.display!=='none')?'':'none';}});
}});
</script>"""
    return shell("Legislation · SGA 60", body, PAGE_CSS, depth=0)


def render_leg_year(leg):
    if not leg:
        return ""
    return (f'<h2 class="sub">Legislation &mdash; {len(leg)} documents on file</h2>'
            + "".join(leg_row(e, 1) for e in leg_sorted(leg)))


# ---------------------------------------------------------------- year page
def render_year(y, prev, nxt, leg=()):
    leads = "".join(
        f'<div class="lead plate-face engraved"><b>{l["name"]}</b>'
        f'<div class="role">{role_flags(l)}</div></div>' for l in y["leaders"])

    notes = "".join(f'<div class="note"><b>{l["name"]}:</b> {l["note"]}</div>'
                    for l in y["leaders"] if l.get("note"))

    profs = "".join(
        f'<section class="profile"><h2 class="sub">{l["name"]} &mdash; the term</h2>'
        + "".join(f'<p>{p}</p>' for p in
                  (l["profile"] if isinstance(l["profile"], list) else [l["profile"]]))
        + '</section>'
        for l in y["leaders"] if l.get("profile"))

    if y["events"]:
        evs = "".join(
            f'<article class="ev"><div class="d">{e["date"]}'
            + ('<span class="ctx">campus</span>' if e.get("campus") else '') + '</div><div>'
            f'<h3>{e["title"]}</h3><p>{e["body"]}</p>'
            + (f'<a class="cite" href="{e["src"]["url"]}" target="_blank" rel="noopener">{e["src"]["label"]} &#8599;</a>'
               if e.get("src") else "")
            + (f' <a class="cite" href="../docs/{e["src"]["file"]}" target="_blank" rel="noopener">read it on this site &#8599;</a>'
               if e.get("src", {}).get("file") else "") + '</div></article>'
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
 <div style="display:flex;gap:20px"><a href="../index.html">The Board</a><a href="../history.html">Timeline</a><a href="../legislation.html">Legislation</a></div>
</div></nav>
<header class="yhead"><div class="wrap">
 <div class="eyebrow">{y['org']}</div>
 <h1>{y['id']}</h1>
 <div class="leads">{leads}</div>
</div></header>
<div class="wrap"><div class="cols">
 <div>{render_portraits(y)}{notes}{profs}{render_org(y)}<h2 class="sub">What happened, in order</h2>{evs}{render_gallery(y)}{render_docs(y)}{render_leg_year(leg)}</div>
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

<input class="search" id="q" type="search" aria-label="Search sixty years"
 placeholder="Search sixty years &mdash; names, events, dates&hellip;">

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
 <a href="history.html">the full timeline &#8599;</a> &nbsp;&middot;&nbsp;
 <a href="legislation.html">the legislation archive &#8599;</a></p>

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
  ? y.events.map(e=>`<article class="ev"><div class="d">${{esc(e.date)}}${{e.campus?'<span class="ctx">campus</span>':''}}</div><div>
      <h4>${{esc(e.title)}}</h4><p>${{esc(e.body)}}</p>
      ${{e.src?`<a class="cite" href="${{e.src.url}}" target="_blank" rel="noopener">${{esc(e.src.label)}} &#8599;</a>`:''}}
      ${{e.src&&e.src.file?` <a class="cite" href="docs/${{e.src.file}}" target="_blank" rel="noopener">read it on this site &#8599;</a>`:''}}
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
const q=document.getElementById('q');
q.addEventListener('input',()=>{{
 const s=q.value.toLowerCase().trim();let n=0;
 plates.forEach(el=>{{
  const y=D[el.dataset.y];
  const hay=(el.dataset.y+' '+y.leaders.map(l=>l.name).join(' ')+' '
   +y.events.map(e=>e.date+' '+e.title+' '+e.body).join(' ')).toLowerCase();
  const ok=!s||hay.includes(s);
  el.classList.toggle('hidden',!ok);if(ok)n++;
 }});
 readout.textContent=s?n+' years match "'+q.value+'"':n+' of '+plates.length+' plates lit';
}});
if(location.hash && D[location.hash.slice(1)]) openYear(location.hash.slice(1));
</script>"""
    return shell("SGA 60 · Sixty Years on the Hill", body, INDEX_CSS, depth=0)


def apply_photo_overlay(ys):
    """Merge data/photos.json onto the years. Photos live in their own file so the
    photograph agent and the six decade agents never edit the same file."""
    overlay_path = ROOT / "data" / "photos.json"
    if not overlay_path.exists():
        return
    overlay = json.loads(overlay_path.read_text())
    by_id = {y["id"]: y for y in ys}
    for p in overlay.get("leaders", []):
        y = by_id.get(p["year"])
        for l in (y["leaders"] if y else []):
            if l["name"] == p["name"]:
                l["photo"] = {"file": p["file"], "src": p.get("src")}
    for p in overlay.get("years", []):
        y = by_id.get(p["year"])
        if y:
            y.setdefault("photos", []).append(
                {"file": p["file"], "caption": p.get("caption", ""), "src": p.get("src")})


def main():
    ys = json.loads(DATA.read_text())["years"]
    apply_photo_overlay(ys)
    leg = json.loads(LEGMETA.read_text())["entries"] if LEGMETA.exists() else []
    by_session = {}
    for e in leg:
        by_session.setdefault(e["session"], []).append(e)
    YDIR.mkdir(parents=True, exist_ok=True)
    (SITE / "index.html").write_text(render_index(ys))
    for i, y in enumerate(ys):
        (YDIR / f'{y["id"]}.html').write_text(
            render_year(y, ys[i - 1] if i else None, ys[i + 1] if i < len(ys) - 1 else None,
                        by_session.get(y["id"], ())))
    (SITE / "legislation.html").write_text(render_legislation(leg))
    if LEG.is_dir():
        shutil.copytree(LEG, SITE / "legislation", dirs_exist_ok=True)
    shutil.copy(DATA, SITE / "years.json")
    ndocs = 0
    if DOCS.is_dir():
        (SITE / "docs").mkdir(exist_ok=True)
        for f in DOCS.iterdir():
            if f.is_file() and not f.name.startswith(".") and f.suffix != ".md":
                shutil.copy(f, SITE / "docs" / f.name)
                ndocs += 1
    if PHOTOS.is_dir():
        shutil.copytree(PHOTOS, SITE / "photos", dirs_exist_ok=True)
    print(f'built the board + {len(ys)} year pages + {ndocs} archive documents '
          f'+ {len(leg)} legislation files -> {SITE}')


if __name__ == "__main__":
    main()
