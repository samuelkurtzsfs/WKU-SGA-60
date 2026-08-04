#!/usr/bin/env python3
"""
SGA 60 site generator.

Reads  data/years.json, data/photos.json, data/legislation.json,
       data/herald-index.json
Writes site/index.html          the plaque board
       site/y/<year>.html       one record per academic year
       site/history.html        the complete timeline
       site/history/<dec>s.html one decade of the timeline at a time
       site/legislation.html    the legislation archive
       site/corrections.html    what the plaque gets wrong, and what is still open
       site/about.html          scope, method, sources, conditions of use
"""
import html as html_mod
import json
import re
import shutil
import urllib.parse
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "years.json"
DOCS = ROOT / "data" / "documents"
PHOTOS = ROOT / "data" / "photos"
LEG = ROOT / "data" / "legislation"
LEGMETA = ROOT / "data" / "legislation.json"
SITE = ROOT / "site"
YDIR = SITE / "y"
HDIR = SITE / "history"

TODAY = date.today()
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")


def h(s):
    return html_mod.escape(str(s), quote=True)


def long_date(d):
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


BUILT = long_date(TODAY)


# ---------------------------------------------------------------- dates
def fmt_date(iso):
    """Return (display, machine, precision).

    The house convention in this archive is that a day of 01 means the day is
    unknown and 01-01 means only the year is known. A date is never displayed
    with more precision than the source gives it.
    """
    s = str(iso)
    parts = s.split("-")
    try:
        y = int(parts[0])
        m = int(parts[1]) if len(parts) > 1 else 1
        d = int(parts[2]) if len(parts) > 2 else 1
    except (ValueError, IndexError):
        return h(s), s, "unknown"
    if m == 1 and d == 1:
        return str(y), f"{y:04d}", "year"
    if d == 1:
        return f"{MONTHS[m - 1]} {y}", f"{y:04d}-{m:02d}", "month"
    return f"{d} {MONTHS[m - 1]} {y}", f"{y:04d}-{m:02d}-{d:02d}", "day"


def time_tag(iso, cls=""):
    disp, mach, _ = fmt_date(iso)
    c = f' class="{cls}"' if cls else ""
    return f'<time{c} datetime="{mach}">{h(disp)}</time>'


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


# ---------------------------------------------------------------- links
def ext(url, label, cls="", extra=""):
    """An external link. The arrow means the reader is leaving the site, so it
    appears here and nowhere else."""
    c = ("ext " + cls).strip()
    return (f'<a class="{c}" href="{h(url)}" rel="noopener"{extra}>{label}</a>')


def src_link(src, cls=""):
    if not src or not src.get("url"):
        return h(src.get("label", "")) if src else ""
    return ext(src["url"], h(src.get("label", src["url"])), cls)


# ---------------------------------------------------------------- style
CORE = """
:root{
 --red:#B01E24; --red-dark:#8A171C; --black:#0B0B0C;
 --ink:#141416; --ink2:#44444B; --ink3:#76767D;
 --paper:#FFFFFF; --paper2:#F6F5F2; --line:#DCD9D3; --line2:#EBE8E3;
 --display:-apple-system,BlinkMacSystemFont,"SF Pro Display","Segoe UI",Roboto,Helvetica,sans-serif;
 --ui:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,sans-serif;
 --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
 --measure:35rem;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--ui);
 font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
@media(max-width:640px){body{font-size:16px}}
h1,h2,h3,h4{font-family:var(--display);font-weight:700;letter-spacing:-.012em;
 text-wrap:balance;margin:0}
p{margin:0 0 1em;text-wrap:pretty}
a{color:var(--red);text-underline-offset:3px;text-decoration-thickness:1px}
a:hover{color:var(--red-dark)}
a.ext::after{content:"\\00A0\\2197";color:var(--ink3);font-size:.82em;text-decoration:none}
:focus-visible{outline:2px solid var(--red);outline-offset:2px}
.wrap{max-width:1120px;margin:0 auto;padding:0 34px}
@media(max-width:640px){.wrap{padding:0 18px}}
.prose{max-width:var(--measure)}
.num{font-variant-numeric:tabular-nums}
.lab{font-family:var(--ui);font-size:11px;font-weight:600;letter-spacing:.12em;
 text-transform:uppercase;color:var(--ink3);margin:0}
.skip{position:absolute;left:-9999px}
.skip:focus{position:static;display:inline-block;padding:8px}

/* ---- masthead nav ---- */
.nav{background:var(--black);color:#fff}
.nav .wrap{display:flex;justify-content:space-between;align-items:baseline;gap:14px;
 padding:13px 34px;flex-wrap:wrap}
@media(max-width:640px){.nav .wrap{padding:11px 18px}}
.nav a{color:rgba(255,255,255,.72);text-decoration:none;font-size:.86rem}
.nav a:hover,.nav a[aria-current]{color:#fff}
.nav a[aria-current]{box-shadow:inset 0 -2px 0 var(--red)}
.nav .brand{font-family:var(--display);font-weight:800;letter-spacing:.05em;color:#fff;font-size:1rem}
.nav .brand b{color:var(--red);font-weight:800}
.nav ul{display:flex;gap:20px;margin:0;padding:0;list-style:none;flex-wrap:wrap}

/* ---- page head ---- */
.head{padding:56px 0 26px;border-bottom:1px solid var(--line)}
@media(max-width:640px){.head{padding:34px 0 20px}}
.head .kicker{font-family:var(--ui);font-size:12px;font-weight:600;letter-spacing:.12em;
 text-transform:uppercase;color:var(--ink3);margin:0 0 12px}
.head h1{font-size:clamp(2.1rem,5vw,3.1rem);line-height:1.04}
.head .lede{font-size:1.12rem;color:var(--ink);max-width:var(--measure);margin:18px 0 0}
.head .scope{color:var(--ink2);max-width:var(--measure);margin:14px 0 0;font-size:.97rem}

/* ---- record head ---- */
.rec-head{padding:48px 0 22px}
.rec-head h1{font-size:clamp(2.6rem,6.5vw,4rem);line-height:.98;letter-spacing:-.03em;
 font-variant-numeric:tabular-nums}
.glance{display:grid;grid-template-columns:max-content 1fr;gap:0 28px;margin:26px 0 0;
 border-top:1px solid var(--line);max-width:46rem}
.glance dt{font-family:var(--ui);font-size:11px;font-weight:600;letter-spacing:.11em;
 text-transform:uppercase;color:var(--ink3);padding:9px 0 0}
.glance dd{margin:0;padding:7px 0 0;font-variant-numeric:tabular-nums}
.glance dd a{text-decoration:none;border-bottom:1px solid rgba(176,30,36,.3)}
@media(max-width:520px){.glance{grid-template-columns:1fr;gap:0}
 .glance dt{padding-top:12px}.glance dd{padding-top:2px}}

/* ---- sections ---- */
section{margin:0}
h2.sec{font-size:1.16rem;margin:52px 0 4px;padding-top:15px;border-top:1px solid var(--line)}
h2.sec .n{font-family:var(--ui);font-size:12px;font-weight:600;letter-spacing:.02em;
 color:var(--ink3);margin-left:10px;font-variant-numeric:tabular-nums}
.secnote{color:var(--ink3);font-size:.88rem;margin:0 0 18px}
.body{padding-bottom:40px}

/* ---- leaders ---- */
.leader{padding:34px 0 0}
.leader h2{font-size:1.5rem;letter-spacing:-.02em}
.leader h2 .r{font-family:var(--ui);font-weight:400;font-size:1rem;color:var(--ink2);
 letter-spacing:0;white-space:nowrap}
.facts{display:grid;grid-template-columns:max-content 1fr;gap:0 26px;margin:14px 0 20px;
 max-width:46rem;font-size:.95rem}
.facts dt{font-family:var(--ui);font-size:11px;font-weight:600;letter-spacing:.11em;
 text-transform:uppercase;color:var(--ink3);padding:7px 0 0}
.facts dd{margin:0;padding:5px 0 0;color:var(--ink)}
@media(max-width:520px){.facts{grid-template-columns:1fr}.facts dt{padding-top:11px}.facts dd{padding-top:1px}}
.editorial{max-width:var(--measure);color:var(--ink);border-left:2px solid var(--line);
 padding-left:18px;margin:0 0 22px}
.editorial p{margin:0 0 .8em}
.editorial p:last-child{margin-bottom:0}
.editorial.flagged{border-left-color:var(--red)}
.profile{max-width:var(--measure)}
.profile p{font-size:1.02rem;margin:0 0 1.05em}
.profile sup{font-size:.66em;line-height:0}
.profile sup a{text-decoration:none;padding:0 1px}
.srclist{max-width:46rem;margin:6px 0 0;padding:0 0 0 1.4em;font-size:.88rem;color:var(--ink3)}
.srclist li{margin:0 0 5px}
.srclist a{color:var(--red)}

/* ---- portraits and photographs ---- */
.plates-photo{display:flex;gap:26px;flex-wrap:wrap;margin:30px 0 6px}
.portrait{margin:0;width:190px}
.portrait img{display:block;width:100%;height:auto;border:1px solid var(--line)}
.portrait figcaption{font-size:.82rem;color:var(--ink2);margin-top:9px;line-height:1.45}
.portrait figcaption b{display:block;font-family:var(--display);font-size:.95rem;
 font-weight:700;color:var(--ink);margin-bottom:2px}
.portrait figcaption .who{display:block}
.credit{display:block;color:var(--ink3);font-size:.78rem;margin-top:3px}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:24px;margin:16px 0 0}
.gallery figure{margin:0}
.gallery img{display:block;width:100%;height:auto;border:1px solid var(--line)}
.gallery figcaption{font-size:.87rem;color:var(--ink2);margin-top:9px;line-height:1.5}

/* ---- the organization ---- */
.org{display:grid;grid-template-columns:1fr 1fr;gap:34px;margin:16px 0 0}
@media(max-width:700px){.org{grid-template-columns:1fr;gap:24px}}
.org h3{font-family:var(--ui);font-size:11px;font-weight:600;letter-spacing:.11em;
 text-transform:uppercase;color:var(--ink3);margin:0 0 6px}
.off{display:grid;grid-template-columns:9rem 1fr;gap:0 16px;padding:9px 0;
 border-top:1px solid var(--line2);font-size:.94rem}
@media(max-width:520px){.off{grid-template-columns:1fr;gap:1px}}
.off .o{font-size:.8rem;color:var(--ink3);padding-top:3px}
.off b{font-weight:600}
.off p{margin:2px 0 0;color:var(--ink2);font-size:.88rem}
.org .meta{font-size:.92rem;color:var(--ink2);margin:12px 0 0;max-width:var(--measure)}

/* ---- entries ---- */
.ev{display:grid;grid-template-columns:9rem 1fr;gap:0 26px;padding:17px 0;
 border-top:1px solid var(--line2)}
@media(max-width:640px){.ev{grid-template-columns:1fr;gap:3px;padding:15px 0}}
.ev .when{font-size:.83rem;color:var(--ink3);padding-top:5px;font-variant-numeric:tabular-nums}
.ev .when .ctx{display:block;font-size:10px;letter-spacing:.1em;text-transform:uppercase;margin-top:4px}
.ev h3{font-size:1.04rem;margin:0 0 6px}
.ev p{margin:0;max-width:var(--measure)}
.srcline{font-size:.84rem;color:var(--ink3);margin-top:9px}
.srcline a{margin-right:14px}
.pl{float:right;font-family:var(--mono);font-size:.78rem;color:var(--ink3);
 text-decoration:none;opacity:0;margin-left:12px}
.ev:hover .pl,.ev:focus-within .pl{opacity:1}
.ev:target{background:var(--paper2);box-shadow:-14px 0 0 var(--paper2),14px 0 0 var(--paper2)}
.empty{max-width:var(--measure);color:var(--ink2)}
.searchlist{columns:2;column-gap:30px;padding:0;margin:10px 0 0;list-style:none;font-size:.86rem}
@media(max-width:640px){.searchlist{columns:1}}
.searchlist li{margin:0 0 4px;break-inside:avoid}

/* ---- documents ---- */
.doc{border-top:1px solid var(--line2);padding:22px 0 6px}
.doc h3{font-size:1.05rem;margin:0 0 7px}
.doc p{color:var(--ink);max-width:var(--measure);margin:0 0 12px}
.doc-extract{border-left:2px solid var(--red);padding:2px 0 2px 16px;margin:0 0 14px;
 max-width:var(--measure);color:var(--ink2);font-size:.95rem}
.doc-extract .lab{margin-bottom:4px}
.doc-view{display:block;width:100%;height:460px;border:1px solid var(--line);background:var(--paper2)}
.doc-foot{font-size:.86rem;color:var(--ink3);margin:10px 0 0}
.doc-foot a{margin-right:18px}

/* ---- legislation rows ---- */
.lrow{display:grid;grid-template-columns:7.5rem 1fr auto;gap:0 18px;align-items:baseline;
 padding:10px 0;border-top:1px solid var(--line2);font-size:.95rem}
@media(max-width:700px){.lrow{grid-template-columns:1fr;gap:2px}}
.lrow .lt{color:var(--ink3);font-size:.82rem;font-variant-numeric:tabular-nums}
.lrow .ll{font-size:.85rem;white-space:nowrap}
.lrow .ll a{margin-left:16px}
@media(max-width:700px){.lrow .ll a{margin:0 16px 0 0}}
.lsec{margin:0 0 26px}

/* ---- timeline ---- */
.hx{display:grid;grid-template-columns:8rem 1fr;gap:0 24px;padding:6px 0;
 border-top:1px solid var(--line2);font-size:.92rem;line-height:1.45}
@media(max-width:640px){.hx{grid-template-columns:1fr;gap:0;padding:8px 0}}
.hx .when{color:var(--ink3);font-size:.8rem;padding-top:3px;font-variant-numeric:tabular-nums}
.hx .t{color:var(--ink2);max-width:52rem}
.hx .t b{color:var(--ink);font-weight:600}
.hx .t a{font-size:.84rem;margin-left:8px;white-space:nowrap}
.hyear{font-size:1.35rem;margin:38px 0 2px;padding-top:14px;border-top:1px solid var(--line)}
.hyear .who{font-family:var(--ui);font-weight:400;font-size:.9rem;color:var(--ink3);
 display:block;margin-top:5px;letter-spacing:0}
.hyear .who a{text-decoration:none;border-bottom:1px solid rgba(176,30,36,.3)}
details.hidx{margin:14px 0 0;font-size:.9rem}
details.hidx summary{cursor:pointer;color:var(--ink3);font-size:.84rem}
details.hidx summary:hover{color:var(--red)}
.decnav{display:flex;flex-wrap:wrap;gap:0 18px;margin:0 0 24px;font-size:.92rem}
.decnav a{text-decoration:none;border-bottom:1px solid rgba(176,30,36,.35);padding-bottom:1px}
.decnav span{color:var(--ink3)}

/* ---- filters and search ---- */
.tools{padding:26px 0 0;border-bottom:1px solid var(--line);padding-bottom:18px}
.field{display:block;max-width:26rem}
.field .lab{margin-bottom:6px}
.field input{width:100%;background:var(--paper);border:1px solid var(--line);color:var(--ink);
 font-family:var(--ui);font-size:16px;padding:10px 12px;border-radius:2px}
.field input:focus{outline:2px solid var(--red);outline-offset:-1px;border-color:var(--red)}
.facets{display:flex;flex-wrap:wrap;gap:0 20px;margin:20px 0 0}
.facets button{background:none;border:0;border-bottom:2px solid transparent;padding:4px 0 5px;
 font-family:var(--ui);font-size:.92rem;color:var(--ink2);cursor:pointer}
.facets button:hover{color:var(--red)}
.facets button[aria-pressed="true"]{color:var(--ink);font-weight:600;border-bottom-color:var(--red)}
.facets button .c{color:var(--ink3);font-weight:400;font-variant-numeric:tabular-nums}
.readout{font-size:.9rem;color:var(--ink2);margin:16px 0 0;font-variant-numeric:tabular-nums}

/* ---- citation ---- */
.citebox{border-top:1px solid var(--line);border-bottom:1px solid var(--line);
 padding:16px 0;margin:46px 0 0;max-width:46rem}
.citestr{font-size:.92rem;color:var(--ink);margin:8px 0 0;line-height:1.55}
.copy{background:none;border:1px solid var(--line);border-radius:2px;color:var(--ink2);
 font-family:var(--ui);font-size:.8rem;padding:5px 11px;margin-top:12px;cursor:pointer}
.copy:hover{border-color:var(--red);color:var(--red)}
.revised{font-size:.84rem;color:var(--ink3);margin:12px 0 0}

/* ---- pager ---- */
.pager{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;
 border-top:1px solid var(--line);padding:20px 0 0;margin-top:44px}
.pager a{font-size:.82rem;color:var(--ink3);text-decoration:none;max-width:46%}
.pager a b{display:block;font-family:var(--display);font-size:1.15rem;color:var(--ink);
 margin-top:3px;font-variant-numeric:tabular-nums}
.pager a:hover b{color:var(--red)}
.pager .r{text-align:right;margin-left:auto}

/* ---- footer ---- */
.foot{border-top:1px solid var(--line);background:var(--paper2);margin-top:70px;
 padding:36px 0 54px;font-size:.88rem;color:var(--ink2)}
.foot .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:30px}
.foot p{max-width:34rem;margin:0 0 .9em}
.foot h2{font-family:var(--ui);font-size:11px;font-weight:600;letter-spacing:.12em;
 text-transform:uppercase;color:var(--ink3);margin:0 0 10px}
.foot .fine{color:var(--ink3);font-size:.82rem;margin-top:26px;
 border-top:1px solid var(--line);padding-top:16px}

/* ---- print ---- */
@media print{
 .nav,.tools,.pager,.bigred,.board,.legend,.starthere,.foot .cols,.copy,.decnav{display:none!important}
 body{font-size:11pt;color:#000}
 a{color:#000;text-decoration:none}
 a.ext::after{content:""}
 .body a[href^="http"]::after{content:" (" attr(href) ")";font-size:8pt;color:#444;word-break:break-all}
 .citebox{margin:0 0 18px;border-top:0}
 .doc-view{display:none}
 h2.sec{break-after:avoid}
 .ev,.doc,.leader{break-inside:avoid}
}
"""

BOARD_CSS = """
.board{background:var(--black);padding:26px 22px 30px;margin:26px 0 0}
@media(max-width:640px){.board{padding:18px 14px 22px;margin-left:-18px;margin-right:-18px}}
.decade{margin:0 0 26px}
.decade:last-child{margin-bottom:0}
.dechead{display:flex;justify-content:space-between;align-items:baseline;gap:14px;
 border-bottom:1px solid rgba(255,255,255,.22);padding-bottom:7px;margin:0 0 12px}
.dechead h2{font-family:var(--ui);font-size:11px;font-weight:600;letter-spacing:.14em;
 text-transform:uppercase;color:rgba(255,255,255,.82)}
.dechead .c{font-size:11px;color:rgba(255,255,255,.45);font-variant-numeric:tabular-nums}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:7px}
@media(max-width:520px){.grid{grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:6px}}
.plate{display:block;background:var(--paper);color:var(--ink);text-decoration:none;
 padding:11px 12px 12px;border:1px solid transparent}
.plate:hover,.plate:focus-visible{border-color:var(--red);color:var(--ink)}
.plate .yr{display:block;font-family:var(--mono);font-size:11.5px;color:var(--ink3);
 font-variant-numeric:tabular-nums;letter-spacing:.01em}
.plate .nm{display:block;font-family:var(--display);font-weight:650;font-size:.92rem;
 line-height:1.25;margin-top:6px}
.plate .nm.two{font-size:.82rem}
.plate .ct{display:block;font-size:11px;color:var(--ink3);margin-top:7px;
 font-variant-numeric:tabular-nums}
.plate .q{display:block;font-size:11px;color:var(--red);margin-top:3px}
.plate.now{border-color:var(--red);box-shadow:inset 0 0 0 1px var(--red)}
.plate.hidden{display:none}
.decade.hidden{display:none}
.legend{margin:18px 0 0;font-size:.85rem;color:var(--ink3);max-width:44rem}
.legend p{margin:0 0 .5em}
.starthere{margin:56px 0 0;padding-top:16px;border-top:1px solid var(--line)}
.starthere ol{list-style:none;margin:14px 0 0;padding:0;
 display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:0 34px}
.starthere li{padding:12px 0;border-top:1px solid var(--line2);max-width:32rem}
.starthere a{font-family:var(--display);font-weight:650;text-decoration:none;
 border-bottom:1px solid rgba(176,30,36,.35)}
.starthere span{display:block;color:var(--ink2);font-size:.92rem;margin-top:4px}

/* ---- Big Red ---- */
.bigred{position:fixed;right:16px;bottom:8px;z-index:20;width:150px;cursor:pointer;
 user-select:none;-webkit-user-select:none;line-height:0}
.bigred img{display:block;width:100%;height:auto;image-rendering:pixelated}
.bigred .wig{position:absolute;top:-22px;left:24%;pointer-events:none}
.bigred .gavel{position:absolute;top:16%;right:-12px;pointer-events:none;transform-origin:24% 88%}
.bigred .close{position:absolute;top:-10px;right:-4px;width:20px;height:20px;
 border:1px solid var(--line);background:var(--paper);color:var(--ink3);font-size:12px;
 line-height:17px;text-align:center;cursor:pointer;padding:0;font-family:var(--ui)}
.bigred .close:hover{color:var(--red);border-color:var(--red)}
.bigred .say{position:absolute;bottom:100%;right:6%;margin-bottom:12px;background:var(--black);
 color:#fff;font-family:var(--ui);font-size:11px;letter-spacing:.05em;padding:7px 11px;
 white-space:nowrap;opacity:0;transition:opacity .2s;pointer-events:none;line-height:1.4}
.bigred .say:after{content:"";position:absolute;top:100%;right:20px;border:6px solid transparent;
 border-top-color:var(--black)}
.bigred.talk .say{opacity:1}
@keyframes br-bang{0%,100%{transform:rotate(0)}35%{transform:rotate(-58deg)}
 60%{transform:rotate(14deg)}80%{transform:rotate(-6deg)}}
.bigred.bang .gavel{animation:br-bang .7s ease}
@media(prefers-reduced-motion:reduce){.bigred .gavel{animation:none!important}}
@media(max-width:640px){.bigred{width:104px;right:8px}}
"""

# ---------------------------------------------------------------- Big Red
# The official Big Red artwork, downsampled to a 30px sprite
# (data/photos/bigred-8bit.png) and rendered pixelated. The wig and the gavel
# are pixel-drawn overlays.
_PX = {"W": "#F4F2ED", "G": "#D8D5CE", "B": "#1A1A1C", "O": "#8B5A2B"}
_WIG = [
    "..WWWWWWWWWW..",
    ".WWWWWWWWWWWW.",
    "WWWGWWWWWWGWWW",
    "WWW........WWW",
    "GWG........GWG",
    "WWW........WWW",
    "GWG........GWG",
    "WWW........WWW",
]
_GAVEL = [
    "BBBBBB..",
    "BBBBBB..",
    "BBBBBB..",
    "...OO...",
    "...OO...",
    "...OO...",
    "...OO...",
    "...OO...",
]


def _pixels(rows, s=7):
    out = []
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != ".":
                out.append(f'<rect x="{x*s}" y="{y*s}" width="{s+0.4}" '
                           f'height="{s+0.4}" fill="{_PX[c]}"/>')
    return "".join(out)


BIGRED = (
    '<div class="bigred" id="bigred" role="img" aria-label="Big Red in a judicial wig, '
    'holding the SGA gavel.">'
    '<button class="close" id="brx" aria-label="Dismiss Big Red">&times;</button>'
    '<div class="say" id="brsay">Order, order.</div>'
    '<img src="photos/bigred-8bit.png" alt="" width="150" height="125">'
    f'<svg class="wig" width="98" height="56" viewBox="0 0 98 56" aria-hidden="true">{_pixels(_WIG)}</svg>'
    f'<svg class="gavel" width="56" height="56" viewBox="0 0 56 56" aria-hidden="true">{_pixels(_GAVEL)}</svg>'
    '</div>'
    '<script>(function(){var br=document.getElementById("bigred");if(!br)return;'
    'try{if(localStorage.getItem("bigred")==="hidden"){br.remove();return}}catch(e){}'
    'document.getElementById("brx").addEventListener("click",function(e){e.stopPropagation();'
    'br.remove();try{localStorage.setItem("bigred","hidden")}catch(e){}});'
    'var says=["Order, order.","Go Tops.","Sixty years on the Hill.","Motion carries.",'
    '"The Spirit Makes the Master."],i=0;'
    'br.addEventListener("click",function(){br.classList.remove("bang");void br.offsetWidth;'
    'document.getElementById("brsay").textContent=says[i++%says.length];'
    'br.classList.add("bang","talk");clearTimeout(br._t);'
    'br._t=setTimeout(function(){br.classList.remove("talk")},1800)});})();</script>'
)


# ---------------------------------------------------------------- searches
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
        (f'{name} with the SGA terms',
         f'https://www.google.com/search?q=site:digitalcommons.wku.edu+{q(DQ+name+DQ)}+{q("("+org+")")}'),
        (f'{name} anywhere on TopSCHOLAR',
         f'https://www.google.com/search?q=site:digitalcommons.wku.edu+{q(DQ+name+DQ)}'),
        (f'{name} in the WKU Timeline',
         f'https://www.google.com/search?q=site:digitalcommons.wku.edu/wku_timeline+{q(DQ+name+DQ)}'),
        (f'{name} in the Herald',
         f'https://wkuherald.com/?s={q(name)}'),
    ]


# ---------------------------------------------------------------- shell
NAV_ITEMS = [("index.html", "The board"), ("history.html", "Timeline"),
             ("legislation.html", "Legislation"), ("corrections.html", "Corrections"),
             ("about.html", "About and method")]

RIGHTS = ("Text on this site is the work of the project. Photographs, documents and "
          "legislation are reproduced from Western Kentucky University's own open "
          "archives and from the <cite>College Heights Herald</cite> and the "
          "<cite>Talisman</cite>; each item names the collection, issue and page it "
          "came from and links to the original.")


def nav(up, current):
    links = "".join(
        f'<li><a href="{up}{href}"' + (' aria-current="page"' if href == current else "")
        + f'>{h(label)}</a></li>' for href, label in NAV_ITEMS)
    return (f'<nav class="nav" aria-label="Sections"><div class="wrap">'
            f'<a class="brand" href="{up}index.html">SGA <b>60</b></a>'
            f'<ul>{links}</ul></div></nav>')


def footer(up):
    return f"""<footer class="foot"><div class="wrap"><div class="cols">
<div><h2>What this is</h2>
<p>A year-by-year record of student government at Western Kentucky University, from the
ratification of the Associated Students constitution in April 1966 to the present. Every
entry names the source it came from.</p></div>
<div><h2>Corrections</h2>
<p>The names here start with the plaque in the SGA Chambers, and the plaque is known to be
wrong in places. Where the archive disagrees with it, this site follows the archive and
records the change on the <a href="{up}corrections.html">corrections page</a>. If you
served, or you know that a year here is wrong, the project wants to hear from you through
the Student Government Association office.</p></div>
<div><h2>Reuse</h2><p>{RIGHTS}</p></div>
</div>
<p class="fine">Built {BUILT}. The whole record is readable as data:
<a href="{up}years.json">years.json</a>. Method and scope are set out
<a href="{up}about.html">on the about page</a>.</p>
</div></footer>"""


def shell(title, desc, body, css, depth, current, mascot=False):
    up = "../" * depth
    extra = BIGRED if mascot else ""
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0B0B0C">
<meta name="description" content="{h(desc)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{h(title)}">
<meta property="og:description" content="{h(desc)}">
<title>{h(title)}</title>
<style>{CORE}{css}</style></head><body>
<a class="skip" href="#main">Skip to the record</a>
{nav(up, current)}
<main id="main">
{body}
</main>
{footer(up)}
{extra}
</body></html>"""


# ---------------------------------------------------------------- pieces
def role_word(l):
    return {"regent": "student regent", "unresolved": "role unresolved"}.get(
        l["role"], "president")


def confidence_line(l, yid):
    """What the record says about this name and year, in plain words."""
    c = l.get("year_confidence")
    if c == "confirmed":
        return "Confirmed in the sources below."
    if c == "corrected":
        return ("Moved here from the year the plaque gives. The correction and its "
                "evidence are set out below.")
    if c == "ambiguous":
        return "Unsettled. The archive has not yet placed this name in a year."
    if c == "likely":
        return "Probable. The plate is consistent with the archive but no source states it outright."
    if c == "stated":
        return "As recorded on the plaque. Not yet corroborated in the archive."
    return ""


FOOTNOTE = re.compile(r"\[(\d{1,2})\]")


def profile_paragraphs(l, key):
    """Profile prose. Bracketed numbers such as [2] become footnote markers
    pointing at the numbered source list under the profile."""
    paras = l["profile"] if isinstance(l["profile"], list) else [l["profile"]]
    n_src = len(l.get("sources") or [])
    out = []
    for p in paras:
        txt = h(p)

        def mark(m):
            i = int(m.group(1))
            if 1 <= i <= n_src:
                return (f'<sup><a href="#{key}-s{i}" aria-label="Source {i}">'
                        f'{i}</a></sup>')
            return m.group(0)
        out.append(f"<p>{FOOTNOTE.sub(mark, txt)}</p>")
    return "".join(out)


def leader_sources(l, key):
    srcs = l.get("sources") or []
    if not srcs:
        return ""
    items = "".join(
        f'<li id="{key}-s{i}">{src_link(s)}</li>' for i, s in enumerate(srcs, 1))
    label = "Sources for this account" if l.get("profile") else "Sources for this name"
    return (f'<p class="lab" style="margin:18px 0 6px">{label}</p>'
            f'<ol class="srclist">{items}</ol>')


def render_leader(l, y, also):
    key = slug(l["name"])
    head = f'{h(l["name"])} <span class="r">{role_word(l)}, {h(y["id"])}</span>'
    facts = [("Office", role_word(l).capitalize()),
             ("Term recorded here", h(y["id"]))]
    if l.get("plaque_term") and l["plaque_term"] != y["id"]:
        facts.append(("Plaque in the Chambers", f'reads {h(l["plaque_term"])}'))
    line = confidence_line(l, y["id"])
    if line:
        facts.append(("Standing of the record", line))
    if l.get("name_verified"):
        facts.append(("Name in the archive", "Found in the sources below."))
    elif l.get("sources"):
        facts.append(("Name in the archive", "Not yet confirmed against a contemporary source."))
    if l.get("missing_from_plaque"):
        facts.append(("Not yet on the plaque",
                      "The Chambers plaque does not carry this name."))
    if l.get("current"):
        facts.append(("Status", "In office."))
    if also:
        links = ", ".join(f'<a href="{h(a)}.html">{h(a)}</a>' for a in also)
        facts.append(("Also on the wall", links))
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in facts)
    flagged = l.get("year_confidence") in ("corrected", "ambiguous") or l["role"] == "unresolved"
    note = ""
    if l.get("note"):
        note = (f'<div class="editorial{" flagged" if flagged else ""}">'
                f'<p>{h(l["note"])}</p></div>')
    prof = ""
    if l.get("profile"):
        prof = f'<div class="profile">{profile_paragraphs(l, key)}</div>'
    return (f'<section class="leader" id="{key}"><h2>{head}</h2>'
            f'<dl class="facts">{dl}</dl>{note}{prof}{leader_sources(l, key)}</section>')


def render_portraits(y):
    ports = [(l, l["photo"]) for l in y["leaders"] if l.get("photo")]
    if not ports:
        return ""
    figs = []
    for l, p in ports:
        credit = ""
        if p.get("src"):
            credit = f'<span class="credit">{src_link(p["src"])}</span>'
        figs.append(
            f'<figure class="portrait">'
            f'<img src="../photos/{h(p["file"])}" alt="Portrait of {h(l["name"])}." loading="lazy">'
            f'<figcaption><b>{h(l["name"])}</b>'
            f'<span class="who">{role_word(l).capitalize()}, {h(y["id"])}.</span>{credit}</figcaption>'
            f'</figure>')
    return f'<div class="plates-photo">{"".join(figs)}</div>'


def render_gallery(y):
    photos = y.get("photos")
    if not photos:
        return ""
    figs = []
    for p in photos:
        credit = f'<span class="credit">{src_link(p["src"])}</span>' if p.get("src") else ""
        figs.append(
            f'<figure><img src="../photos/{h(p["file"])}" alt="" loading="lazy">'
            f'<figcaption>{h(p.get("caption", ""))}{credit}</figcaption></figure>')
    n = len(photos)
    return (f'<h2 class="sec">The year in photographs<span class="n">{n}</span></h2>'
            f'<div class="gallery">{"".join(figs)}</div>')


def render_office(o):
    src = f'<span class="credit">{src_link(o["src"])}</span>' if o.get("src") else ""
    return (f'<div class="off"><span class="o">{h(o.get("office", ""))}</span><span>'
            f'<b>{h(o.get("name", ""))}</b>'
            + (f'<p>{h(o["note"])}</p>' if o.get("note") else "")
            + src + '</span></div>')


def render_org(y):
    org = y.get("organization")
    if not org:
        return ""
    execs = org.get("executive", [])
    sen = org.get("senate", {})
    officers = sen.get("officers", [])
    committees = sen.get("committees", [])
    exec_rows = "".join(render_office(o) for o in execs)
    sen_rows = "".join(render_office(o) for o in officers)
    sen_rows += "".join(
        f'<div class="off"><span class="o">committee</span><span><b>{h(c.get("name", ""))}</b>'
        + (f'<p>Chair: {h(c["chair"])}</p>' if c.get("chair") else "")
        + (f'<p>{h(c["note"])}</p>' if c.get("note") else "")
        + '</span></div>' for c in committees)
    meta = ""
    if sen.get("size"):
        meta += f'<p class="meta">{h(sen["size"])} senators this year.</p>'
    if sen.get("note"):
        meta += f'<p class="meta">{h(sen["note"])}</p>'
    if not (exec_rows or sen_rows or meta):
        return ""
    left = f'<div><h3>The executive</h3>{exec_rows}</div>' if exec_rows else ""
    right = f'<div><h3>The senate</h3>{sen_rows}{meta}</div>' if (sen_rows or meta) else ""
    return (f'<h2 class="sec">The organization</h2><div class="org">{left}{right}</div>')


def render_docs(y):
    docs = y.get("documents")
    if not docs:
        return ""
    out = [f'<h2 class="sec">Documents<span class="n">{len(docs)}</span></h2>'
           '<p class="secnote">Files mirrored on this site from the university archive. '
           'Each one links back to the original record.</p>']
    for d in docs:
        page = f'#page={d["page"]}' if d.get("page") else ""
        extract = ""
        if d.get("extract"):
            where = f' &middot; pages {h(d["sga_pages"])}' if d.get("sga_pages") else ""
            extract = (f'<div class="doc-extract"><p class="lab">From the document{where}</p>'
                       f'{h(d["extract"])}</div>')
        viewer = ""
        if d.get("file"):
            viewer = (f'<iframe class="doc-view" src="../docs/{h(d["file"])}{page}" '
                      f'loading="lazy" title="{h(d.get("title", d["file"]))}"></iframe>')
        links = []
        if d.get("file"):
            links.append(f'<a href="../docs/{h(d["file"])}">Open the file</a>')
        if d.get("src"):
            links.append(src_link(d["src"]))
        out.append(
            f'<article class="doc"><h3>{h(d.get("title", d.get("file", "")))}</h3>'
            + (f'<p>{h(d["summary"])}</p>' if d.get("summary") else "")
            + f'{extract}{viewer}<p class="doc-foot">{"".join(links)}</p></article>')
    return "".join(out)


def leg_sorted(entries):
    return sorted(entries, key=lambda e: (e.get("date") or "9999-99-99", e["title"]))


def leg_row(e, up):
    when = f' {time_tag(e["date"])}' if e.get("date") else ""
    return (f'<div class="lrow" data-t="{h(e["title"].lower())} {h(e["type"])}">'
            f'<span class="lt">{h(e["type"])}{when}</span>'
            f'<span>{h(e["title"])}</span>'
            f'<span class="ll"><a href="{up}legislation/{h(e["file"])}">Read</a>'
            f'{ext(e["source_url"], "Original")}</span></div>')


def render_leg_year(leg):
    if not leg:
        return ""
    return (f'<h2 class="sec">Legislation<span class="n">{len(leg)}</span></h2>'
            '<p class="secnote">Bills and resolutions from this session, held as files on '
            'this site.</p>'
            + "".join(leg_row(e, "../") for e in leg_sorted(leg)))


# ---------------------------------------------------------------- year page
def event_anchor(e, seen):
    base = "e-" + re.sub(r"[^0-9]", "", str(e["date"]))[:8]
    seen[base] = seen.get(base, 0) + 1
    return f"{base}-{seen[base]}"


def year_sources(y):
    """Every source cited anywhere in the year, deduplicated, with a count of
    how many entries rest on it."""
    counts = {}
    order = []

    def add(src):
        if not src or not src.get("label"):
            return
        k = (src.get("label"), src.get("url"))
        if k not in counts:
            counts[k] = 0
            order.append(k)
        counts[k] += 1

    for l in y["leaders"]:
        for s in l.get("sources") or []:
            add(s)
    for e in y["events"]:
        add(e.get("src"))
    for d in y.get("documents") or []:
        add(d.get("src"))
    org = y.get("organization") or {}
    for o in org.get("executive", []):
        add(o.get("src"))
    for o in (org.get("senate") or {}).get("officers", []):
        add(o.get("src"))
    for p in y.get("photos") or []:
        add(p.get("src"))
    for l in y["leaders"]:
        if l.get("photo") and l["photo"].get("src"):
            add(l["photo"]["src"])
    return [(label, url, counts[(label, url)]) for label, url in order]


def render_year(y, prev, nxt, leg, repeats):
    yid = y["id"]
    pres = [l["name"] for l in y["leaders"] if l["role"] == "president"]
    regs = [l["name"] for l in y["leaders"] if l["role"] == "regent"]
    unres = [l["name"] for l in y["leaders"] if l["role"] == "unresolved"]
    n_ev = len(y["events"])
    n_doc = len(y.get("documents") or [])
    n_pho = len(y.get("photos") or []) + sum(1 for l in y["leaders"] if l.get("photo"))
    srcs = year_sources(y)

    glance = [("Organization", h(y["org"]))]
    if pres:
        glance.append(("President" if len(pres) == 1 else "Presidents",
                       h(" and ".join(pres))))
    if regs:
        glance.append(("Student regent" if len(regs) == 1 else "Student regents",
                       h(" and ".join(regs))))
    if unres:
        glance.append(("Name not yet placed", h(" and ".join(unres))))
    glance.append(("Entries", str(n_ev)))
    if n_pho:
        glance.append(("Photographs", str(n_pho)))
    if n_doc:
        glance.append(("Documents", str(n_doc)))
    if leg:
        glance.append(("Legislation on file", str(len(leg))))
    glance.append(("Sources cited", str(len(srcs))))
    glance_html = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in glance)

    leaders = "".join(
        render_leader(l, y, repeats.get(l["name"], set()) - {yid}) for l in y["leaders"])

    # the chronology
    seen = {}
    rows = []
    for e in sorted(y["events"], key=lambda e: e["date"]):
        aid = event_anchor(e, seen)
        ctx = '<span class="ctx">campus</span>' if e.get("campus") else ""
        cites = []
        if e.get("src"):
            cites.append(src_link(e["src"]))
        if e.get("src", {}).get("file"):
            cites.append(f'<a href="../docs/{h(e["src"]["file"])}">Read it on this site</a>')
        cite = f'<p class="srcline">{"".join(cites)}</p>' if cites else ""
        rows.append(
            f'<article class="ev" id="{aid}"><div class="when">{time_tag(e["date"])}{ctx}</div>'
            f'<div><a class="pl" href="#{aid}" aria-label="Link to this entry">#</a>'
            f'<h3>{h(e["title"])}</h3><p>{h(e["body"])}</p>{cite}</div></article>')
    if rows:
        chron = ""
        if n_ev >= 3:
            chron = f'<h2 class="sec">The year, in order<span class="n">{n_ev}</span></h2>'
        chron += "".join(rows)
    else:
        links = "".join(f'<li>{ext(u, h(t))}</li>' for t, u in year_searches(y)[:8])
        chron = ('<h2 class="sec">The year, in order</h2>'
                 '<div class="empty"><p>No sourced record of student government in this '
                 'year has been found. Nothing is entered here until a source carries it.</p>'
                 '<p>These are the searches that cover the year. Anyone can pick up the '
                 'work from them.</p></div>'
                 f'<ul class="searchlist">{links}</ul>')

    # the bibliography for the year
    bib = ""
    if srcs:
        items = "".join(
            f'<li>{src_link({"label": lab, "url": url}) if url else h(lab)}'
            + (f' <span class="credit">{n} entries</span>' if n > 1 else "")
            + '</li>' for lab, url, n in srcs)
        bib = (f'<h2 class="sec">Sources for this year<span class="n">{len(srcs)}</span></h2>'
               '<p class="secnote">Every source cited above, once, with the number of '
               'entries that rest on it.</p>'
               f'<ol class="srclist" style="font-size:.92rem;color:var(--ink2)">{items}</ol>')

    cite_names = ", ".join(pres + regs + unres)
    citation = (f'&#8220;{h(yid)},&#8221; <cite>SGA 60: Student Government at Western '
                f'Kentucky University, 1966&#8211;2026</cite>, revised {BUILT}, ')

    pager = ""
    if prev:
        pager += f'<a href="{h(prev["id"])}.html">Previous year<b>{h(prev["id"])}</b></a>'
    if nxt:
        pager += f'<a class="r" href="{h(nxt["id"])}.html">Next year<b>{h(nxt["id"])}</b></a>'

    body = f"""
<header class="rec-head"><div class="wrap">
 <p class="kicker">{h(y['org'])} &middot; academic year</p>
 <h1>{h(yid)}</h1>
 <dl class="glance">{glance_html}</dl>
</div></header>
<div class="wrap"><div class="body">
{render_portraits(y)}
{leaders}
{render_org(y)}
{chron}
{render_gallery(y)}
{render_docs(y)}
{render_leg_year(leg)}
{bib}
<section class="citebox">
 <p class="lab">Preferred citation</p>
 <p class="citestr" id="cite">{citation}<span id="citeurl">y/{h(yid)}.html</span></p>
 <button class="copy" id="copy" type="button">Copy the citation</button>
 <p class="revised">This record was last rebuilt on {BUILT}. Where a name here differs from
 the plaque in the SGA Chambers, the difference is explained above and listed on the
 <a href="../corrections.html">corrections page</a>.</p>
</section>
<div class="pager">{pager}</div>
</div></div>
<script>
(function(){{
 var u=document.getElementById('citeurl');if(u)u.textContent=location.href.split('#')[0];
 var b=document.getElementById('copy'),c=document.getElementById('cite');
 if(b&&c&&navigator.clipboard){{b.addEventListener('click',function(){{
  navigator.clipboard.writeText(c.textContent.replace(/\\s+/g,' ').trim()).then(function(){{
   b.textContent='Copied';setTimeout(function(){{b.textContent='Copy the citation'}},1800);}});}});}}
 else if(b){{b.style.display='none'}}
}})();
</script>"""
    who = f"{cite_names}. " if cite_names else ""
    desc = (f"Student government at Western Kentucky University, {yid}. {who}"
            f"{n_ev} sourced entries.")
    return shell(f"{yid} · SGA 60", desc, body, "", depth=1, current="index.html")


# ---------------------------------------------------------------- the board
#          first year, last year, heading,        short label, file stem
DECADES = [(1966, 1969, "1966 to 1969", "1960s", "1960s"),
           (1970, 1979, "The 1970s", "1970s", "1970s"),
           (1980, 1989, "The 1980s", "1980s", "1980s"),
           (1990, 1999, "The 1990s", "1990s", "1990s"),
           (2000, 2009, "The 2000s", "2000s", "2000s"),
           (2010, 2019, "The 2010s", "2010s", "2010s"),
           (2020, 2029, "2020 onward", "2020s", "2020s")]

START_HERE = [
    ("1966-67", "The first year",
     "Students ratified the constitution 1,812 to 726 in April 1966 and elected Jim "
     "Haynes the first president the following month."),
    ("1968-69", "A second seat appears",
     "The student seat on the Board of Regents was created in 1968 and elected "
     "separately from the presidency, which is why several plaque years carry two names."),
    ("1969-70", "A name in the wrong decade",
     "The plaque reads 1970-71 for Larry Zielke. Herald election coverage puts his term "
     "here, a year earlier."),
    ("1974-75", "The first African American student regent",
     "Gregory McKinney beat Sid Stevens for the seat and was sworn in on 19 June 1974."),
    ("1981-82", "A term finished by someone else",
     "Marcel Bush resigned in January 1982 and David Payne served out the year. The "
     "plaque reads only 1982."),
    ("2014-15", "One officeholder, two plates",
     "The Chambers plaque carries Janet 'Nicki' Seay and Nicki Taylor as consecutive "
     "presidents. The Herald shows one continuous term and a change of name."),
]


def render_index(ys, n_leg, n_herald):
    n_ev = sum(len(y["events"]) for y in ys)
    n_lead = sum(len(y["leaders"]) for y in ys)
    n_src = sum(len(year_sources(y)) for y in ys)

    def disputed(y):
        return any(l["role"] == "unresolved" or l.get("year_confidence") == "ambiguous"
                   for l in y["leaders"])

    def corrected(y):
        return any(l.get("year_confidence") == "corrected" for l in y["leaders"])

    def unconfirmed(y):
        return any(not l.get("name_verified") for l in y["leaders"])

    counts = {"all": len(ys),
              "disputed": sum(1 for y in ys if disputed(y)),
              "corrected": sum(1 for y in ys if corrected(y)),
              "unconfirmed": sum(1 for y in ys if unconfirmed(y))}
    for lo, hi, *_ in DECADES:
        counts[f"d{lo}"] = sum(1 for y in ys if lo <= y["start"] <= hi)

    groups = []
    for lo, hi, label, short, stem in DECADES:
        block = [y for y in ys if lo <= y["start"] <= hi]
        if not block:
            continue
        plates = []
        for y in block:
            names = [l["name"] for l in y["leaders"]]
            cls = ["plate"]
            if any(l.get("current") for l in y["leaders"]):
                cls.append("now")
            tags = [f"d{lo}"]
            if disputed(y):
                tags.append("disputed")
            if corrected(y):
                tags.append("corrected")
            if unconfirmed(y):
                tags.append("unconfirmed")
            flag = ""
            if disputed(y):
                flag = '<span class="q">a name here is unsettled</span>'
            elif corrected(y):
                flag = '<span class="q">corrected against the plaque</span>'
            n = len(y["events"])
            plates.append(
                f'<a class="{" ".join(cls)}" href="y/{h(y["id"])}.html" '
                f'data-tags="{" ".join(tags)}" data-y="{h(y["id"])}">'
                f'<span class="yr">{h(y["id"])}</span>'
                f'<span class="nm{" two" if len(names) > 1 else ""}">'
                f'{" &middot; ".join(h(n) for n in names)}</span>'
                f'<span class="ct">{n} entries</span>{flag}</a>')
        ev = sum(len(y["events"]) for y in block)
        groups.append(
            f'<section class="decade" data-dec="d{lo}"><div class="dechead">'
            f'<h2>{h(label)}</h2><span class="c">{len(block)} years, {ev} entries</span></div>'
            f'<div class="grid">{"".join(plates)}</div></section>')

    facets = [("all", "All years")]
    for lo, hi, label, short, stem in DECADES:
        facets.append((f"d{lo}", short))
    for key, label in (("corrected", "Corrected"), ("disputed", "Unsettled"),
                       ("unconfirmed", "Name unconfirmed")):
        if counts[key]:
            facets.append((key, label))
    facet_html = "".join(
        f'<button type="button" data-f="{k}" aria-pressed="{"true" if k == "all" else "false"}">'
        f'{h(lab)} <span class="c">{counts[k]}</span></button>' for k, lab in facets)

    # a light index: years, names, entry dates and headlines. Bodies are not
    # carried here; the complete timeline searches the full text.
    idx = {}
    for y in ys:
        parts = [y["id"]] + [l["name"] for l in y["leaders"]]
        for e in y["events"]:
            parts.append(fmt_date(e["date"])[0])
            parts.append(e["title"])
        idx[y["id"]] = " ".join(parts).lower()
    payload = json.dumps(idx, ensure_ascii=False, separators=(",", ":"))

    starts = "".join(
        f'<li><a href="y/{h(yid)}.html">{h(title)}</a><span>{h(text)}</span></li>'
        for yid, title, text in START_HERE)

    body = """
<header class="head"><div class="wrap">
 <p class="kicker">Western Kentucky University</p>
 <h1>Student Government Association</h1>
 <p class="lede">A year-by-year record, 1966 to 2026.</p>
 <p class="scope">The spine of this archive is the academic year. Every name below starts as a
 claim from the plaque in the SGA Chambers and is then checked against the
 <cite>College Heights Herald</cite> back file, the university's own records on TopSCHOLAR and
 SGA's papers. Where the plaque and the archive disagree, the archive wins and the change is
 <a href="corrections.html">written down</a>.</p>
 <p class="scope">__COUNTS__</p>
</div></header>

<div class="wrap">
 <div class="tools">
  <label class="field" for="q"><span class="lab">Search the board</span>
   <input id="q" type="search" autocomplete="off" spellcheck="false"></label>
  <p class="secnote" style="margin:8px 0 0">Names, years and entry headlines. For the full
  text of every entry, use <a href="history.html">the complete timeline</a>.</p>
  <div class="facets" role="group" aria-label="Filter the years">__FACETS__</div>
  <p class="readout" id="readout" role="status"></p>
 </div>

 <div class="board" id="board">__GROUPS__</div>

 <div class="legend">
  <p>Each plate carries the year, the names on it, and how many sourced entries that year has
  so far. A year with three entries is a year the archive has not given up much of yet, not a
  year in which little happened.</p>
  <p>A plate marked <b>unsettled</b> holds a name the record cannot yet place. A plate marked
  <b>corrected</b> holds a name this site has moved from the year the plaque gives it.
  The current year is outlined in red.</p>
 </div>

 <section class="starthere">
  <h2 class="sec" style="margin-top:0;border-top:0;padding-top:0">Where to start</h2>
  <p class="secnote">Sixty-one years is a lot of doors. These six are the ones worth
  opening first.</p>
  <ol>__STARTS__</ol>
 </section>
</div>
<script>
var D=__PAYLOAD__;
var plates=[].slice.call(document.querySelectorAll('.plate')),
    decs=[].slice.call(document.querySelectorAll('.decade')),
    chips=[].slice.call(document.querySelectorAll('.facets button')),
    readout=document.getElementById('readout'),qi=document.getElementById('q');
var facet='all';
function apply(){
 var s=qi.value.toLowerCase().trim(),n=0;
 plates.forEach(function(el){
  var ok=(facet==='all'||el.dataset.tags.split(' ').indexOf(facet)>-1)&&
         (!s||(D[el.dataset.y]||'').indexOf(s)>-1);
  el.classList.toggle('hidden',!ok);if(ok)n++;
 });
 decs.forEach(function(d){
  d.classList.toggle('hidden',!d.querySelector('.plate:not(.hidden)'));
 });
 var word=n===1?'year':'years';
 if(s)readout.textContent=n+' '+word+' match \\u201c'+qi.value.trim()+'\\u201d.';
 else if(facet!=='all')readout.textContent='Showing '+n+' '+word+' of '+plates.length+'.';
 else readout.textContent='Showing all '+plates.length+' years.';
 var p=new URLSearchParams(location.search);
 if(s)p.set('q',qi.value.trim());else p.delete('q');
 if(facet!=='all')p.set('in',facet);else p.delete('in');
 var qs=p.toString();
 history.replaceState(null,'',location.pathname+(qs?'?'+qs:''));
}
chips.forEach(function(c){c.addEventListener('click',function(){
 facet=c.dataset.f;chips.forEach(function(x){
  x.setAttribute('aria-pressed',String(x.dataset.f===facet))});apply();});});
qi.addEventListener('input',apply);
var params=new URLSearchParams(location.search);
if(params.get('q'))qi.value=params.get('q');
if(params.get('in')){facet=params.get('in');
 chips.forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.f===facet))});}
apply();
</script>"""
    counts_line = (
        f"Sixty-one academic years have a page. {n_ev} entries are sourced to the "
        f"<cite>Herald</cite>, the WKU Timeline, SGA's own papers or the university archive; "
        f"{n_lead} presidents and student regents are recorded, {n_leg} pieces of legislation "
        f"are held as files, and {n_herald} further <cite>Herald</cite> index lines are "
        f"listed on the timeline. What is still unsettled is set out on the "
        f'<a href="corrections.html">corrections page</a>.')
    body = (body.replace("__COUNTS__", counts_line)
                .replace("__FACETS__", facet_html)
                .replace("__GROUPS__", "".join(groups))
                .replace("__STARTS__", starts)
                .replace("__PAYLOAD__", payload))
    desc = (f"A year-by-year record of the Student Government Association at Western "
            f"Kentucky University, 1966 to 2026. {n_ev} sourced entries across 61 "
            f"academic years, {n_src} citations.")
    return shell("SGA 60 · Student Government at Western Kentucky University",
                 desc, body, BOARD_CSS, depth=0, current="index.html", mascot=True)


# ---------------------------------------------------------------- timeline
def academic_year(dstr):
    y = int(dstr[:4])
    m = int(dstr[5:7]) if len(dstr) >= 7 else 1
    start = y if m >= 8 else y - 1
    if start == 1965:
        start = 1966  # the founding spring belongs to year one
    if start < 1966 or start > 2026:
        return None
    return f"{start}-{str(start + 1)[2:]}"


def timeline_sections(ys, by_year, up):
    secs = []
    for y in ys:
        v = by_year[y["id"]]
        seen = {}
        rows = []
        for e in v["events"]:
            aid = event_anchor(e, seen)
            links = f'{src_link(e["src"])}' if e.get("src") else ""
            if e.get("src", {}).get("file"):
                links += f'<a href="{up}docs/{h(e["src"]["file"])}">Read it here</a>'
            rows.append(
                f'<div class="hx" data-t="{h(e["title"].lower())} {h(e["body"].lower())}">'
                f'<span class="when">{time_tag(e["date"])}</span>'
                f'<span class="t"><b>{h(e["title"])}.</b> {h(e["body"])} '
                f'<a href="{up}y/{h(y["id"])}.html#{aid}">In the record</a>{links}</span></div>')
        hx = "".join(
            f'<div class="hx" data-t="{h(ln.lower())}">'
            f'<span class="when">{time_tag(x["date"])}</span>'
            f'<span class="t">{h(ln)} {src_link({"label": x["issue"][:60], "url": x["url"]})}'
            f'</span></div>'
            for x in sorted(v["herald"], key=lambda e: e["date"]) for ln in x["lines"])
        n_hx = sum(len(x["lines"]) for x in v["herald"])
        who = " &middot; ".join(f'{h(l["name"])} <span>({role_word(l)})</span>'
                                for l in y["leaders"])
        secs.append(
            f'<h2 class="hyear" id="y{h(y["id"])}">'
            f'<a href="{up}y/{h(y["id"])}.html">{h(y["id"])}</a>'
            f'<span class="who">{who}</span></h2>' + "".join(rows)
            + (f'<details class="hidx"><summary>{n_hx} further mentions in the '
               f'<cite>Herald</cite> index</summary>{hx}</details>' if hx else ""))
    return "".join(secs)


TIMELINE_JS = """
<script>
var hf=document.getElementById('hf'),hr=document.getElementById('hr'),
    rows=[].slice.call(document.querySelectorAll('.hx')),
    heads=[].slice.call(document.querySelectorAll('.hyear'));
function run(){
 var q=hf.value.toLowerCase().trim(),n=0;
 rows.forEach(function(r){var ok=!q||r.dataset.t.indexOf(q)>-1;
  r.style.display=ok?'':'none';if(ok)n++;});
 heads.forEach(function(hd){
  var any=false,el=hd.nextElementSibling;
  while(el&&!el.classList.contains('hyear')){
   if(el.classList.contains('hx')&&el.style.display!=='none')any=true;
   if(el.tagName==='DETAILS'&&el.querySelector('.hx:not([style*="none"])'))any=true;
   el=el.nextElementSibling;}
  hd.style.display=(!q||any)?'':'none';});
 if(!q){hr.textContent='Showing all '+rows.length+' lines.';return;}
 hr.textContent=n?n+' of '+rows.length+' lines match \\u201c'+hf.value.trim()+'\\u201d.'
  :'Nothing in the timeline matches \\u201c'+hf.value.trim()+'\\u201d.';
 var p=new URLSearchParams(location.search);
 if(q)p.set('q',hf.value.trim());else p.delete('q');
 var qs=p.toString();
 history.replaceState(null,'',location.pathname+(qs?'?'+qs:''));
}
hf.addEventListener('input',run);
var pq=new URLSearchParams(location.search).get('q');
if(pq)hf.value=pq;
run();
</script>"""


def timeline_head(title, kicker, lede, up, current_dec):
    links = []
    for lo, hi, label, short, stem in DECADES:
        if lo == current_dec:
            links.append(f'<span>{h(short)}</span>')
        else:
            links.append(f'<a href="{up}history/{stem}.html">{h(short)}</a>')
    if current_dec is None:
        allx = '<span>The complete timeline</span>'
    else:
        allx = f'<a href="{up}history.html">The complete timeline</a>'
    return (f'<header class="head"><div class="wrap"><p class="kicker">{h(kicker)}</p>'
            f'<h1>{h(title)}</h1><p class="scope">{lede}</p></div></header>'
            f'<div class="wrap"><div class="tools">'
            f'<label class="field" for="hf"><span class="lab">Search the entries</span>'
            f'<input id="hf" type="search" autocomplete="off" spellcheck="false"></label>'
            f'<p class="readout" id="hr" role="status"></p></div>'
            f'<div class="decnav" style="margin-top:22px">{" ".join(links)} {allx}</div>')


def render_history(ys, herald):
    by_year = {y["id"]: {"events": sorted(y["events"], key=lambda e: e["date"]),
                         "herald": []} for y in ys}
    for e in herald:
        yid = academic_year(e["date"])
        if yid and yid in by_year:
            by_year[yid]["herald"].append(e)

    n_ev = sum(len(v["events"]) for v in by_year.values())
    n_hx = sum(len(x["lines"]) for v in by_year.values() for x in v["herald"])
    lede = (f"Every sourced entry in the archive, {n_ev} of them, in the order they "
            f"happened. Under each year sit a further {n_hx} lines from the "
            f"<cite>Herald</cite> index: headlines the project has recorded but not yet "
            f"worked into the record. On a phone, one decade at a time reads better.")
    pages = {}
    body = (timeline_head("The complete timeline", "1966 to 2026", lede, "", None)
            + '<div class="body">'
            + timeline_sections(ys, by_year, "") + '</div></div>' + TIMELINE_JS)
    pages["history.html"] = shell(
        "The complete timeline · SGA 60",
        f"Every sourced entry in the SGA 60 archive, {n_ev} entries from 1966 to 2026, "
        f"in chronological order.", body, "", depth=0, current="history.html")

    for i, (lo, hi, label, short, stem) in enumerate(DECADES):
        block = [y for y in ys if lo <= y["start"] <= hi]
        if not block:
            continue
        ev = sum(len(by_year[y["id"]]["events"]) for y in block)
        hxn = sum(len(x["lines"]) for y in block for x in by_year[y["id"]]["herald"])
        d_lede = (f"{ev} sourced entries across {len(block)} academic years, "
                  f"{block[0]['id']} to {block[-1]['id']}, with {hxn} further lines from "
                  f"the <cite>Herald</cite> index under the years they belong to.")
        pager = ""
        if i:
            p = DECADES[i - 1]
            pager += (f'<a href="{p[4]}.html">Previous decade<b>{h(p[3])}</b></a>')
        if i < len(DECADES) - 1:
            nx = DECADES[i + 1]
            pager += (f'<a class="r" href="{nx[4]}.html">Next decade<b>{h(nx[3])}</b></a>')
        dbody = (timeline_head(label, "The timeline", d_lede, "../", lo)
                 + '<div class="body">'
                 + timeline_sections(block, by_year, "../")
                 + f'<div class="pager">{pager}</div></div></div>' + TIMELINE_JS)
        pages[f"history/{stem}.html"] = shell(
            f"{label} · SGA 60",
            f"The SGA 60 timeline, {label.lower()}: {ev} sourced entries from "
            f"{block[0]['id']} to {block[-1]['id']}.",
            dbody, "", depth=1, current="history.html")
    return pages


# ---------------------------------------------------------------- legislation
def render_legislation(entries):
    groups = {}
    for e in entries:
        groups.setdefault(e["session"], []).append(e)
    sessions = sorted((k for k in groups if k not in ("governing", "undated")), reverse=True)
    order = ([("governing", "Governing documents")] if "governing" in groups else []) \
        + [(s, s) for s in sessions] \
        + ([("undated", "Undated")] if "undated" in groups else [])
    jump = " ".join(f'<a href="#s{h(k)}">{h(lab)}</a>' for k, lab in order)
    secs = "".join(
        f'<section class="lsec" id="s{h(k)}">'
        f'<h2 class="sec">{h(lab)}<span class="n">{len(groups[k])}</span></h2>'
        + "".join(leg_row(e, "") for e in leg_sorted(groups[k])) + '</section>'
        for k, lab in order)
    body = f"""
<header class="head"><div class="wrap">
 <p class="kicker">The paper trail</p>
 <h1>Legislation</h1>
 <p class="scope">Every bill and resolution the project has been able to get hold of,
 {len(entries)} files in all, held on this site and linked back to the original. Sessions
 with nothing listed are sessions whose legislation has not been found, not sessions in
 which nothing passed.</p>
</div></header>
<div class="wrap"><div class="tools">
 <label class="field" for="lf"><span class="lab">Search the legislation</span>
  <input id="lf" type="search" autocomplete="off" spellcheck="false"></label>
 <p class="readout" id="lr" role="status"></p>
</div>
<div class="decnav" style="margin-top:22px">{jump}</div>
<div class="body">{secs}</div></div>
<script>
var lf=document.getElementById('lf'),lr=document.getElementById('lr'),
    lrows=[].slice.call(document.querySelectorAll('.lrow'));
function lrun(){{
 var q=lf.value.toLowerCase().trim(),n=0;
 lrows.forEach(function(r){{var ok=!q||r.dataset.t.indexOf(q)>-1;
  r.style.display=ok?'':'none';if(ok)n++;}});
 [].slice.call(document.querySelectorAll('.lsec')).forEach(function(s){{
  s.style.display=s.querySelector('.lrow:not([style*="none"])')?'':'none';}});
 var w=n===1?'document':'documents';
 lr.textContent=q?(n?n+' '+w+' match \\u201c'+lf.value.trim()+'\\u201d.'
  :'Nothing matches \\u201c'+lf.value.trim()+'\\u201d.')
  :'Showing all '+lrows.length+' documents.';
}}
lf.addEventListener('input',lrun);lrun();
</script>"""
    return shell("Legislation · SGA 60",
                 f"{len(entries)} bills, resolutions and governing documents of the WKU "
                 f"Student Government Association, held as files and linked to the originals.",
                 body, "", depth=0, current="legislation.html")


# ---------------------------------------------------------------- corrections
def render_corrections(ys):
    corrected, open_q, unconfirmed = [], [], []
    for y in ys:
        for l in y["leaders"]:
            c = l.get("year_confidence")
            if c == "corrected":
                corrected.append((y, l))
            elif c == "ambiguous" or l["role"] == "unresolved":
                open_q.append((y, l))
            elif not l.get("name_verified"):
                unconfirmed.append((y, l))

    def block(y, l, plaque_label):
        facts = [(plaque_label, h(l.get("plaque_term", "not recorded"))),
                 ("Where this site places the term", f'<a href="y/{h(y["id"])}.html">{h(y["id"])}</a>'),
                 ("Office", role_word(l).capitalize())]
        note = f'<div class="editorial flagged"><p>{h(l["note"])}</p></div>' if l.get("note") else ""
        srcs = ""
        if l.get("sources"):
            srcs = ('<p class="lab" style="margin:14px 0 6px">What the change rests on</p>'
                    '<ol class="srclist">'
                    + "".join(f"<li>{src_link(s)}</li>" for s in l["sources"]) + "</ol>")
        dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in facts)
        return (f'<section class="leader"><h2>{h(l["name"])} '
                f'<span class="r">{h(y["id"])}</span></h2>'
                f'<dl class="facts">{dl}</dl>{note}{srcs}</section>')

    def group(title, note, rows, plaque_label):
        if not rows:
            return ""
        return (f'<h2 class="sec">{h(title)}<span class="n">{len(rows)}</span></h2>'
                f'<p class="secnote" style="max-width:35rem">{note}</p>'
                + "".join(block(y, l, plaque_label) for y, l in rows))

    body = f"""
<header class="head"><div class="wrap">
 <p class="kicker">What the plaque gets wrong</p>
 <h1>Corrections and open questions</h1>
 <p class="scope">The names in this archive begin as a claim made by the plaque in the SGA
 Chambers. People who served have reported that their year on it is wrong, so every plate is
 treated as something to check. This page is the running account of what has been moved, what
 is still unsettled, and what has simply not been confirmed yet.</p>
 <p class="scope">A correction is not an embarrassment. It is the part of the record that
 shows the work.</p>
</div></header>
<div class="wrap"><div class="body">
{group("Corrections made", "The archive placed these terms somewhere other than the plaque does. The site follows the archive.", corrected, "What the plaque reads")}
{group("Still open", "Two names on one plate, or a name the record cannot yet place. Nothing is asserted here that a source does not carry.", open_q, "What the plaque reads")}
{group("Recorded, not yet confirmed", "These names are on the plaque and stand in the record, but no contemporary source has been found that puts them in the year given. They are printed as the plaque has them until the archive says otherwise.", unconfirmed, "What the plaque reads")}
<h2 class="sec">Spellings the project will not quietly fix</h2>
<p class="prose">Two names on the plaque are recorded here exactly as they appear on it,
because no source has been found that settles them: <b>Hargroave</b>, which may be a
misspelling of Hargrove, and <b>Keyanna</b>, which appears elsewhere as Keyana. Guessing at
a spelling would put a person in the record under a name they never used.</p>
<h2 class="sec">Telling us</h2>
<p class="prose">If you served, or you know that a year here is wrong, the project wants to
hear it. Corrections come through the Student Government Association office at Western
Kentucky University, and they are recorded on this page with the evidence that settled
them.</p>
</div></div>"""
    return shell("Corrections and open questions · SGA 60",
                 "What the plaque in the WKU SGA Chambers gets wrong, what this archive has "
                 "moved, and what is still unsettled.",
                 body, "", depth=0, current="corrections.html")


# ---------------------------------------------------------------- about
def render_about(ys, meta, n_leg, n_herald, n_docs, n_port, n_gal):
    n_ev = sum(len(y["events"]) for y in ys)
    n_lead = sum(len(y["leaders"]) for y in ys)
    thick = sorted(ys, key=lambda y: -len(y["events"]))[:1][0]
    body = f"""
<header class="head"><div class="wrap">
 <p class="kicker">Scope, method and conditions</p>
 <h1>About this archive</h1>
 <p class="lede">SGA 60 is a record of the Student Government Association at Western Kentucky
 University, from the ratification of the Associated Students constitution in April 1966 to
 the present.</p>
</div></header>
<div class="wrap"><div class="body">

<h2 class="sec">Scope and content</h2>
<div class="prose">
<p>The archive holds one page for each academic year from 1966-67 to 2026-27, {n_ev} dated
entries, and {n_lead} presidents and student regents with their terms as far as the record
supports them. Entries cover the organization, not only its presidents: elections and turnout,
budgets, appointments, committee work, resolutions that passed and resolutions that failed,
and the fights with the administration and the <cite>Herald</cite>. Campus events that shaped
a year are included where they bear on student government and are marked as such.</p>
<p>Alongside the entries the site holds {n_port} portraits, {n_gal} year photographs,
{n_docs} archival documents mirrored as files, {n_leg} pieces of legislation, and
{n_herald} further lines from the <cite>Herald</cite> index that have been recorded but not
yet worked into the record.</p>
</div>

<h2 class="sec">Arrangement</h2>
<div class="prose">
<p>The spine is the academic year, not the person. {h(meta.get("why", ""))}</p>
<p>Within a year, entries run in date order. A date is shown only as precisely as its source
gives it: a day where the source gives a day, a month where it gives a month, a year where it
gives only a year.</p>
</div>

<h2 class="sec">The plaque, and why it is not trusted</h2>
<div class="prose">
<p>The names come first from the plaque in the SGA Chambers. People who served have reported
that their year on it is wrong. Every plate is therefore treated as a claim to verify rather
than a fact to copy, and no name is moved silently. Where a term has been moved, the plaque's
reading is kept and printed beside the corrected one on the year page and on the
<a href="corrections.html">corrections page</a>.</p>
</div>

<h2 class="sec">What is settled</h2>
<div class="prose">
<p>The student seat on the Board of Regents was a separately elected office from April 1968.
William Menser was the first to hold it. That is why several plaque years carry two names:
one president and one regent. {h(meta.get("student_regent_history", ""))}</p>
<p>Michael Fiorella in 1972-73, Gregory McKinney in 1974-75 and Sandra Norfleet in 1982-83
are confirmed as regents rather than presidents. By about 2001 the two offices had merged;
after that, a second name in a year means a mid-year succession.</p>
</div>

<h2 class="sec">Sources, in the order they are useful</h2>
<div class="prose"><ol class="srclist" style="font-size:1rem;color:var(--ink)">
<li>The <cite>College Heights Herald</cite> back file on TopSCHOLAR, indexed article by
article, at {ext("https://digitalcommons.wku.edu/dlsc_ua_records/", "digitalcommons.wku.edu/dlsc_ua_records")}.</li>
<li>The WKU Timeline, dated and citable single events, at
{ext("https://digitalcommons.wku.edu/wku_timeline/", "digitalcommons.wku.edu/wku_timeline")}.</li>
<li>SGA's own constitutions, minutes, legislation and correspondence at
{ext("https://digitalcommons.wku.edu/sga/", "digitalcommons.wku.edu/sga")}.</li>
<li>The <cite>Herald</cite> online, roughly 2003 onward, at
{ext("https://wkuherald.com/", "wkuherald.com")}.</li>
<li>The <cite>Talisman</cite> yearbooks, the best source for portraits, at
{ext("https://digitalcommons.wku.edu/talisman/", "digitalcommons.wku.edu/talisman")}.</li>
</ol></div>

<h2 class="sec">How an entry gets on the site</h2>
<div class="prose">
<p>No source, no entry. Every dated line here carries the issue, page or record it came from,
and links to it. Quotation from the <cite>Herald</cite> and the <cite>Talisman</cite> is held
under fifteen words, once per source; everything else is paraphrase, because this is a public
site reusing a university archive and a student newspaper.</p>
<p>Accuracy beats completeness. A thin year is left thin. Where a year holds nothing, the
page says what was searched rather than apologising, so the next person can pick up the work.
The thickest year at present is {h(thick["id"])}, with {len(thick["events"])} entries; that is
a measure of what has been found, not of what happened.</p>
<p>Two people can share a name, so names are not merged across years without evidence.
Doubtful spellings are flagged, not fixed.</p>
</div>

<h2 class="sec">Living people</h2>
<div class="prose">
<p>Some entries touch resignations, investigations and conduct cases. Only what a cited source
reported is repeated here. Accusers who were not named publicly are not named. Where a source
covers an allegation and never its resolution, the entry says so.</p>
</div>

<h2 class="sec">Conditions of use</h2>
<div class="prose"><p>{RIGHTS}</p>
<p>The underlying record is published as data: <a href="years.json">years.json</a> holds every
year, leader, entry and citation on the site.</p></div>

<section class="citebox">
 <p class="lab">Preferred citation for the archive</p>
 <p class="citestr"><cite>SGA 60: Student Government at Western Kentucky University,
 1966&#8211;2026</cite>, revised {BUILT}, <span id="citeurl">about.html</span></p>
 <p class="revised">Individual year pages carry their own citation. Cite the year page, not
 this one, when you are citing a fact from a particular year.</p>
</section>
</div></div>
<script>var u=document.getElementById('citeurl');
if(u)u.textContent=location.href.split('/').slice(0,-1).join('/')+'/';</script>"""
    return shell("About and method · SGA 60",
                 "Scope, arrangement, sources and conditions of use for SGA 60, a "
                 "year-by-year record of student government at Western Kentucky University.",
                 body, "", depth=0, current="about.html")


# ---------------------------------------------------------------- data
def apply_photo_overlay(ys):
    """Merge data/photos.json onto the years. Photographs live in their own file so
    the photograph agent and the decade agents never edit the same file."""
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
    raw = json.loads(DATA.read_text())
    ys = raw["years"]
    meta = raw.get("_meta", {})
    apply_photo_overlay(ys)
    leg = json.loads(LEGMETA.read_text())["entries"] if LEGMETA.exists() else []
    by_session = {}
    for e in leg:
        by_session.setdefault(e["session"], []).append(e)
    hpath = ROOT / "data" / "herald-index.json"
    herald = json.loads(hpath.read_text())["entries"] if hpath.exists() else []
    n_herald = sum(len(e["lines"]) for e in herald
                   if academic_year(e["date"]) in {y["id"] for y in ys})

    repeats = {}
    for y in ys:
        for l in y["leaders"]:
            repeats.setdefault(l["name"], set()).add(y["id"])

    YDIR.mkdir(parents=True, exist_ok=True)
    HDIR.mkdir(parents=True, exist_ok=True)

    (SITE / "index.html").write_text(render_index(ys, len(leg), n_herald))
    for i, y in enumerate(ys):
        (YDIR / f'{y["id"]}.html').write_text(
            render_year(y, ys[i - 1] if i else None,
                        ys[i + 1] if i < len(ys) - 1 else None,
                        by_session.get(y["id"], ()), repeats))
    hist = render_history(ys, herald)
    for path, page in hist.items():
        (SITE / path).write_text(page)
    # a year that has been renamed or a decade page that no longer exists should
    # not linger in the output
    keep_years = {f'{y["id"]}.html' for y in ys}
    for f in YDIR.glob("*.html"):
        if f.name not in keep_years:
            f.unlink()
    keep_hist = {p.split("/", 1)[1] for p in hist if p.startswith("history/")}
    for f in HDIR.glob("*.html"):
        if f.name not in keep_hist:
            f.unlink()
    (SITE / "legislation.html").write_text(render_legislation(leg))
    (SITE / "corrections.html").write_text(render_corrections(ys))

    n_port = sum(1 for y in ys for l in y["leaders"] if l.get("photo"))
    n_gal = sum(len(y.get("photos") or []) for y in ys)
    n_docs = sum(len(y.get("documents") or []) for y in ys)
    (SITE / "about.html").write_text(
        render_about(ys, meta, len(leg), n_herald, n_docs, n_port, n_gal))

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
    print(f'built the board, {len(ys)} year pages, the timeline and {len(DECADES)} decade '
          f'pages, the legislation archive, corrections and about '
          f'+ {ndocs} documents + {len(leg)} legislation files -> {SITE}')


if __name__ == "__main__":
    main()
