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
import subprocess
import sys
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
    """Render a citation. When the archive gives us a direct file, offer it:
    the record page for context, the PDF for the document itself."""
    if not src or not src.get("url"):
        return h(src.get("label", "")) if src else ""
    out = ext(src["url"], h(src.get("label", src["url"])), cls)
    if src.get("pdf"):
        lbl = src.get("label", "this source")
        out += (f' <a class="{(cls + " ext pdf").strip()}" href="{h(src["pdf"])}"'
                f' rel="noopener" aria-label="PDF of {h(lbl)}">PDF</a>')
    return out


# ---------------------------------------------------------------- style
CORE = """
:root{
 --red:#B01E24; --red-dark:#8A171C; --black:#0B0B0C;
 --ink:#141416; --ink2:#44444B; --ink3:#6B6B72;
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
img{max-width:100%;height:auto}
.srclist a,.srcline a,.credit a,.doc-foot a{overflow-wrap:anywhere}
a{color:var(--red);text-underline-offset:3px;text-decoration-thickness:1px}
a:hover{color:var(--red-dark)}
a.ext::after{content:"\\00A0\\2197";color:var(--ink3);font-size:.82em;text-decoration:none}
:focus-visible{outline:2px solid var(--red);outline-offset:2px}
.nav :focus-visible,.board :focus-visible,.foot :focus-visible{outline-color:#FFFFFF}
.wrap{max-width:1120px;margin:0 auto;padding:0 34px}
@media(max-width:640px){.wrap{padding:0 18px}}
.prose{max-width:var(--measure)}
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
.kicker{font-family:var(--ui);font-size:12px;font-weight:600;letter-spacing:.12em;
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
 letter-spacing:0}
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
.ev .money{margin:8px 0 0;font-size:.88rem;color:var(--ink2);
 border-left:2px solid var(--red);padding-left:11px;max-width:var(--measure)}
/* the badge on an entry that records something student government put on */
.kind{color:var(--red);font-weight:600}
.ev .when .kind{display:block;font-size:10px;letter-spacing:.1em;
 text-transform:uppercase;margin-top:4px}

/* ---- what they put on, on a year page ---- */
.puton{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));
 gap:22px 34px;margin:4px 0 0}
.pgrp h3{font-size:12px;font-family:var(--ui);font-weight:600;letter-spacing:.1em;
 text-transform:uppercase;color:var(--ink3);margin:0 0 7px;padding-bottom:6px;
 border-bottom:1px solid var(--line)}
.pgrp h3 .n{color:var(--red);margin-left:8px;letter-spacing:0}
.pgrp ul{list-style:none;margin:0;padding:0}
.pgrp li{margin:0 0 7px;font-size:.9rem;line-height:1.35}
.pgrp li a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line)}
.pgrp li a:hover{color:var(--red);border-color:var(--red)}
.pgrp .pw{display:block;font-size:.78rem;color:var(--ink3);
 font-variant-numeric:tabular-nums}
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
.lrow .ll{font-size:.85rem;overflow-wrap:anywhere}
.lrow .ll a{margin-left:16px}
@media(max-width:700px){.lrow .ll a{margin:0 16px 0 0}}
.lsec{margin:0 0 26px}

/* ---- filters and search ---- */
.decnav{display:flex;flex-wrap:wrap;gap:0 18px;margin:22px 0 0;font-size:.92rem}
.decnav a{text-decoration:none;border-bottom:1px solid rgba(176,30,36,.35);padding-bottom:1px}
.decnav span{color:var(--ink3)}
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
 .nav,.tools,.pager,.board,.legend,.starthere,.foot .cols,.copy,.decnav,
 .yearnav{display:none!important}
 .yrbar{position:static!important;box-shadow:none}
 details.hidx{background:none;border-left-color:#999}
 .yr,.hx{break-inside:avoid}
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
.plate{position:relative}
.plate .nums{position:absolute;top:8px;right:10px;display:flex;gap:5px;align-items:baseline}
.plate .num{font-family:var(--mono);font-size:11.5px;font-variant-numeric:tabular-nums;
 letter-spacing:.02em;font-weight:600}
.plate .num.pres{color:var(--red)}
.plate .num.reg{color:var(--ink);font-weight:500}
.plate:hover .num,.plate:focus-visible .num{color:var(--red)}
.plate .yr{padding-right:46px}
.plate .ro{display:block;font-size:11px;color:var(--ink3);margin-top:3px;line-height:1.3}
.plate .ct{display:block;font-size:11px;color:var(--ink3);margin-top:7px;
 font-variant-numeric:tabular-nums}
.plate .q{display:block;font-size:11px;color:var(--red);margin-top:3px}
.plate.now{border-color:var(--red);box-shadow:inset 0 0 0 1px var(--red)}
.plate.hidden{display:none}
.decade.hidden{display:none}
.numkey{display:flex;flex-wrap:wrap;gap:8px 28px;margin:20px 0 12px;padding:12px 14px;
 background:var(--paper2);font-size:.87rem;color:var(--ink2)}
.numkey .sw{display:flex;align-items:baseline;gap:8px}
.numkey .num{font-family:var(--mono);font-size:12px;font-variant-numeric:tabular-nums;
 font-weight:600}
.numkey .num.pres{color:var(--red)}
.numkey .num.reg{color:var(--ink)}
.numkey .kred{color:var(--red)}
.legend .kred{color:var(--red)}
.legend{margin:18px 0 0;font-size:.85rem;color:var(--ink3);max-width:44rem}
.legend p{margin:0 0 .5em}
.starthere{margin:56px 0 0;padding-top:16px;border-top:1px solid var(--line)}
.starthere ol{list-style:none;margin:14px 0 0;padding:0;
 display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:0 34px}
.starthere li{padding:12px 0;border-top:1px solid var(--line2);max-width:32rem}
.starthere a{font-family:var(--display);font-weight:650;text-decoration:none;
 border-bottom:1px solid rgba(176,30,36,.35)}
.starthere span{display:block;color:var(--ink2);font-size:.92rem;margin-top:4px}

/* ---- the story, on the front page ---- */
.twoup{display:grid;grid-template-columns:repeat(3,1fr);gap:0 36px;margin:30px 0 0}
@media(max-width:1000px){.twoup{grid-template-columns:1fr 1fr;gap:0 32px}}
@media(max-width:820px){.twoup{grid-template-columns:1fr;gap:0}}
.twoup .readfirst{margin:0}
@media(max-width:820px){.twoup .readfirst+.readfirst{border-top-width:1px}}
.readfirst{display:block;text-decoration:none;color:var(--ink);border-top:2px solid var(--black);
 border-bottom:1px solid var(--line);padding:20px 0 22px;margin:30px 0 0}
.readfirst:hover{color:var(--ink)}
.readfirst .lab{color:var(--red)}
.readfirst h2{font-size:clamp(1.5rem,3.4vw,2rem);line-height:1.05;margin:9px 0 0;
 max-width:30rem}
.readfirst p{max-width:var(--measure);color:var(--ink2);margin:11px 0 0;font-size:1rem}
.readfirst .go{display:inline-block;margin-top:13px;font-size:.9rem;color:var(--red);
 border-bottom:1px solid rgba(176,30,36,.4)}
.readfirst:hover .go{color:var(--red-dark)}

/* ---- Big Red ---- */
 line-height:17px;text-align:center;cursor:pointer;padding:0;font-family:var(--ui)}
 white-space:nowrap;opacity:0;transition:opacity .2s;pointer-events:none;line-height:1.4}
"""

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
NAV_ITEMS = [("index.html", "The board"), ("story.html", "The story"),
             ("patterns.html", "Patterns"), ("events.html", "What SGA put on"),
             ("irregular.html", "Irregular terms"),
             ("history.html", "Timeline"),
             ("legislation.html", "Legislation"), ("corrections.html", "Corrections"),
             ("sources.html", "Sources"), ("about.html", "About and method")]

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
<div><h2>What it rests on</h2>
<p>Everything here comes from what is publicly available online: the digitised
<cite>Herald</cite> and SGA's own papers on TopSCHOLAR, the <cite>Talisman</cite> yearbooks,
wkuherald.com, the university's news pages and the Wayback Machine. That is a fraction of
what happened. Student government has met most weeks for sixty years, and the greater part
of it was never written down, or was written down on paper that has never been scanned. A
thin year here is a thin record, not a quiet one.</p></div>
<div><h2>Reuse</h2><p>{RIGHTS}</p></div>
</div>
<p class="fine">Built {BUILT}. The whole record is readable as data:
<a href="{up}years.json">years.json</a>. Method and scope are set out
<a href="{up}about.html">on the about page</a>.</p>
</div></footer>"""


def shell(title, desc, body, css, depth, current, mascot=False):
    up = "../" * depth
    extra = ""
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


# ---------------------------------------------------------------- programmes
# What student government put on: the concerts, lectures, films, festivals,
# annual traditions and standing services it ran for the campus. These are
# ordinary events carrying a `kind`, so the same entry appears in its year, in
# the complete timeline and on the programmes page without being stored twice.
KINDS = [
    ("concert", "Concert", "Concerts",
     "Music student government booked and paid for, from the block-booked "
     "package shows of the 1960s to the co-funded bills of the present."),
    ("speaker", "Lecture", "Lectures",
     "The lecture series: writers, politicians, scientists and activists "
     "brought to campus on student government's budget."),
    ("film", "Film", "Films",
     "Film series and single screenings run for students."),
    ("festival", "Festival", "Festivals",
     "Multi-day events built around music, spring weather or a cause."),
    ("tradition", "Tradition", "Traditions",
     "The things that came back every year: homecoming week, registration "
     "week, mock elections, awards and welcome events."),
    ("service", "Service", "Services",
     "Standing services rather than single nights: escorts, shuttles, "
     "book exchanges, discount cards, legal aid, printed guides."),
    ("program", "Programme", "Programmes",
     "Programmes and initiatives that were neither a single show nor a "
     "permanent service."),
    ("other", "Other", "Other",
     "Programme business that does not fit the categories above: what students "
     "said about what was booked, and the decisions that changed who did the "
     "booking at all."),
]
KIND_ONE = {k: one for k, one, _, _ in KINDS}
KIND_MANY = {k: many for k, _, many, _ in KINDS}
KIND_BLURB = {k: b for k, _, _, b in KINDS}
KIND_ORDER = [k for k, _, _, _ in KINDS]


def is_program(e):
    return e.get("kind") in KIND_ONE


def kind_tag(e, cls="kind"):
    """The badge that marks an entry as something SGA put on."""
    if not is_program(e):
        return ""
    k = e["kind"]
    return f'<span class="{cls} k-{k}">{h(KIND_ONE[k])}</span>'


def money_line(e):
    """A sourced figure - a budget, a loss, a gate, a crowd - shown under the
    entry it belongs to, because the money is most of the story with these."""
    if not e.get("money"):
        return ""
    return f'<p class="money">{h(e["money"])}</p>'


# ---------------------------------------------------------------- pieces
# The seat was created in April 1968, inside the 1967-68 academic year, and
# William Menser took it while serving as that year's president. The year the
# archive starts counting the dual office from is therefore 1967-68, not 1968-69.
REGENT_SEAT_CREATED = 1967


def held_both(l, y):
    """The student seat on the Board of Regents has existed since April 1968 and
    has never gone away. In most years the elected president also holds it, so a
    lone name on the plaque means one person in both offices. The years that
    carry two names are the exceptions, when someone other than the president
    held the seat - usually because the president was ineligible.

    A year in which the presidency changed hands has two presidents, and then
    the count of names cannot answer the question: one of them may have held the
    seat, or neither, or both in turn. Where a source settles it, the leader
    carries `also_regent` and that is used instead of the guess."""
    if l["role"] != "president":
        return False
    if "also_regent" in l:
        return bool(l["also_regent"])
    return len(y["leaders"]) == 1 and y["start"] >= REGENT_SEAT_CREATED


# How many people have held each office, and in what order. A person is counted
# once, at their first term, so a second term does not make a second holder.
ORDINAL = {"president": {}, "regent": {}}


def seat_gaps(ys):
    """Years since the seat was created in which the archive cannot name whoever
    sat on the Board. Reported at build time rather than papered over, because
    the alternative is a guess that reads like a fact."""
    return [y["id"] for y in ys if y["start"] >= REGENT_SEAT_CREATED
            and not any(l["role"] == "regent" or held_both(l, y) for l in y["leaders"])]


def index_offices(ys):
    for k in ORDINAL:
        ORDINAL[k].clear()
    for y in ys:
        for l in y["leaders"]:
            if l["role"] == "president" and l["name"] not in ORDINAL["president"]:
                ORDINAL["president"][l["name"]] = len(ORDINAL["president"]) + 1
            if (l["role"] == "regent" or held_both(l, y)) \
                    and l["name"] not in ORDINAL["regent"]:
                ORDINAL["regent"][l["name"]] = len(ORDINAL["regent"]) + 1


def nth(n):
    if 10 <= n % 100 <= 20:
        suf = "th"
    else:
        suf = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suf}"


def role_word(l, y=None):
    if l["role"] == "regent":
        return "student regent"
    if l["role"] == "unresolved":
        return "role unresolved"
    # someone who filled the office without being elected to it says so
    if l.get("acting"):
        return "acting president"
    if y is not None and held_both(l, y):
        return "president and student regent"
    return "president"


def role_title(l, y=None):
    """The office as a name rather than a description, for the board plates."""
    w = role_word(l, y)
    w = w.replace("student regent", "Student Regent").replace("president", "President")
    return w[:1].upper() + w[1:]


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
    head = f'{h(l["name"])} <span class="r">{role_word(l, y)}, {h(y["id"])}</span>'
    facts = [("Office", role_word(l, y).capitalize()),
             ("Term recorded here", h(y["id"]))]
    place = []
    if ORDINAL["president"].get(l["name"]):
        place.append(f'the {nth(ORDINAL["president"][l["name"]])} president')
    if ORDINAL["regent"].get(l["name"]):
        place.append(f'the {nth(ORDINAL["regent"][l["name"]])} student regent')
    if place:
        facts.append(("Place in the line", h(" and ".join(place))))
    if l.get("plaque_term") and l["plaque_term"] != y["id"]:
        facts.append(("On the plaque", h(l["plaque_term"])))
    line = confidence_line(l, y["id"])
    if line:
        facts.append(("Standing of the record", line))
    # Only speak to the name separately when it adds something the standing
    # line did not already say; otherwise the two rows contradict each other.
    if not line:
        if l.get("name_verified"):
            facts.append(("Name in the archive", "Found in the sources below."))
        elif l.get("sources"):
            facts.append(("Name in the archive",
                          "Not yet confirmed against a contemporary source."))
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
            f'<span class="who">{role_word(l, y).capitalize()}, {h(y["id"])}.</span>{credit}</figcaption>'
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
            f'<figure><img src="../photos/{h(p["file"])}" alt="{h(p.get("caption","Archive photograph"))[:180]}" loading="lazy">'
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
            f'<span class="ll"><a href="{up}legislation/{h(e["file"])}"'
            f' aria-label="Read {h(e["title"])}">Read</a>'
            f'<a class="ext" href="{h(e["source_url"])}" rel="noopener"'
            f' aria-label="Original record for {h(e["title"])}">Original</a></span></div>')


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
    labels = {}
    urls = {}

    def add(src):
        if not src or not src.get("label"):
            return
        url = (src.get("url") or "").rstrip("/")
        k = url or src.get("label")
        if k not in counts:
            counts[k] = 0
            order.append(k)
            labels[k] = src.get("label")
            urls[k] = src.get("url")
        elif len(src.get("label") or "") > len(labels.get(k) or ""):
            labels[k] = src.get("label")   # keep the fullest form of the label
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
    return [(labels[k], urls[k], counts[k]) for k in order]


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
    n_prog = sum(1 for e in y["events"] if is_program(e))
    if n_prog:
        glance.append(("Put on for students", str(n_prog)))
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
    anchors = {}
    for e in sorted(y["events"], key=lambda e: e["date"]):
        aid = event_anchor(e, seen)
        anchors[id(e)] = aid
        ctx = '<span class="ctx">campus</span>' if e.get("campus") else ""
        ctx += kind_tag(e, "ctx kind")
        cites = []
        if e.get("src"):
            cites.append(src_link(e["src"]))
            if e.get("src2"):
                cites.append(src_link(e["src2"]))
        if e.get("src", {}).get("file"):
            cites.append(f'<a href="../docs/{h(e["src"]["file"])}">Read it on this site</a>')
        cite = f'<p class="srcline">{"".join(cites)}</p>' if cites else ""
        rows.append(
            f'<article class="ev" id="{aid}"><div class="when">{time_tag(e["date"])}{ctx}</div>'
            f'<div><a class="pl" href="#{aid}" aria-label="Link to this entry">#</a>'
            f'<h3>{h(e["title"])}</h3><p>{h(e["body"])}</p>{money_line(e)}{cite}</div></article>')
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

    # what student government put on this year, gathered out of the chronology
    progs = [e for e in sorted(y["events"], key=lambda e: e["date"]) if is_program(e)]
    puton = ""
    if progs:
        groups = []
        for k in KIND_ORDER:
            inks = [e for e in progs if e["kind"] == k]
            if not inks:
                continue
            lis = "".join(
                f'<li><a href="#{anchors[id(e)]}">{h(e["title"])}</a>'
                f'<span class="pw">{h(fmt_date(e["date"])[0])}</span></li>' for e in inks)
            groups.append(f'<div class="pgrp"><h3>{h(KIND_MANY[k])}'
                          f'<span class="n">{len(inks)}</span></h3>'
                          f'<ul>{lis}</ul></div>')
        word = "thing" if len(progs) == 1 else "things"
        puton = (f'<h2 class="sec">What they put on<span class="n">{len(progs)}</span></h2>'
                 f'<p class="secnote">The {len(progs)} {word} student government staged or '
                 f'ran for the campus this year, drawn from the chronology below. Every one '
                 f'of them also appears on the '
                 f'<a href="../events.html">programmes page</a>, which runs the whole '
                 f'sixty years together.</p>'
                 f'<div class="puton">{"".join(groups)}</div>')

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
{puton}
{chron}
{render_gallery(y)}
{render_docs(y)}
{render_leg_year(leg)}
{bib}
<section class="citebox">
 <p class="lab">Preferred citation</p>
 <p class="citestr" id="cite">{citation}<span id="citeurl">y/{h(yid)}.html</span></p>
 <button class="copy" id="copy" type="button">Copy the citation</button>
 <p class="revised">Where a name on this page differs from the plaque in the SGA
 Chambers, the difference is explained above and recorded on the
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

    leaders_all = [(y, l) for y in ys for l in y["leaders"]]
    counts = {
        "all": len(leaders_all),
        "disputed": sum(1 for _, l in leaders_all
                        if l["role"] == "unresolved"
                        or l.get("year_confidence") == "ambiguous"),
        "corrected": sum(1 for _, l in leaders_all
                         if l.get("year_confidence") == "corrected"),
        "unconfirmed": sum(1 for _, l in leaders_all if not l.get("name_verified")),
        "regent": sum(1 for _, l in leaders_all if l["role"] == "regent"),
        "acting": sum(1 for _, l in leaders_all if l.get("acting")),
    }
    for lo, hi, *_ in DECADES:
        counts[f"d{lo}"] = sum(1 for y, _ in leaders_all if lo <= y["start"] <= hi)

    # One plate to a person, the way the wall does it, rather than one to a year.
    # A year in which the presidency changed hands puts two or three names on the
    # board, each with its own number in the line.
    def leader_tags(l, y, lo):
        t = [f"d{lo}"]
        if l["role"] == "unresolved" or l.get("year_confidence") == "ambiguous":
            t.append("disputed")
        if l.get("year_confidence") == "corrected":
            t.append("corrected")
        if not l.get("name_verified"):
            t.append("unconfirmed")
        if l["role"] == "regent":
            t.append("regent")
        if l.get("acting"):
            t.append("acting")
        return t

    all_plates = []
    groups = []
    for lo, hi, label, short, stem in DECADES:
        block = [y for y in ys if lo <= y["start"] <= hi]
        if not block:
            continue
        plates = []
        for y in block:
            n = len(y["events"])
            for l in y["leaders"]:
                pid = f'{y["id"]}--{slug(l["name"])}'
                cls = ["plate"]
                if l.get("current"):
                    cls.append("now")
                tags = leader_tags(l, y, lo)
                flag = ""
                if "disputed" in tags:
                    flag = '<span class="q">unsettled</span>'
                elif "corrected" in tags:
                    flag = '<span class="q">corrected against the plaque</span>'
                # Two separate lines of succession, shown as two numbers rather than
                # one: red for the president's place in the line of presidents, black
                # for their place in the line of student regents. Most people after
                # 1968 held both offices and so carry both numbers.
                pnum = ORDINAL["president"].get(l["name"])
                rnum = ORDINAL["regent"].get(l["name"])
                nums = []
                if pnum:
                    nums.append(f'<span class="num pres" title="the {nth(pnum)} president '
                                f'of student government at Western">{pnum}</span>')
                if rnum:
                    nums.append(f'<span class="num reg" title="the {nth(rnum)} student '
                                f'regent on the WKU Board of Regents">{rnum}</span>')
                badge = f'<span class="nums">{"".join(nums)}</span>' if nums else ""
                all_plates.append((pid, y, l))
                plates.append(
                    f'<a class="{" ".join(cls)}" href="y/{h(y["id"])}.html#{slug(l["name"])}" '
                    f'data-tags="{" ".join(tags)}" data-y="{h(pid)}">'
                    f'{badge}<span class="yr">{h(y["id"])}</span>'
                    f'<span class="nm">{h(l["name"])}</span>'
                    f'<span class="ro">{h(role_title(l, y))}</span>'
                    f'<span class="ct">{n} entries</span>{flag}</a>')
        ev = sum(len(y["events"]) for y in block)
        groups.append(
            f'<section class="decade" data-dec="d{lo}"><div class="dechead">'
            f'<h2>{h(label)}</h2><span class="c">{len(block)} years, {len(plates)} names, '
            f'{ev} entries</span></div>'
            f'<div class="grid">{"".join(plates)}</div></section>')

    facets = [("all", "All names")]
    if counts["regent"]:
        facets.append(("regent", "Student regents"))
    if counts["acting"]:
        facets.append(("acting", "Acting"))
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
        shared = [y["id"]]
        for e in y["events"]:
            shared.append(fmt_date(e["date"])[0])
            shared.append(e["title"])
        for l in y["leaders"]:
            n = ORDINAL["president"].get(l["name"]) or ORDINAL["regent"].get(l["name"])
            own = [l["name"], role_word(l, y)] + ([str(n), nth(n)] if n else [])
            idx[f'{y["id"]}--{slug(l["name"])}'] = " ".join(shared + own).lower()
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
 <div class="twoup">
 <a class="readfirst" href="story.html">
  <p class="lab">Start here</p>
  <h2>The story</h2>
  <p>Sixty years of student government at Western Kentucky University, read straight through:
  the fight for a seat on the Board of Regents, the concert losses that nearly cost it the job, the
  gazebo that was never built, the resolution that drew national coverage and was rejected
  within days. Every claim links back to the year it came from.</p>
  <span class="go">Read the narrative</span>
 </a>
 <a class="readfirst" href="patterns.html">
  <p class="lab">Or read across</p>
  <h2>The patterns</h2>
  <p>What recurs rather than what happened: campus lighting, textbook prices, tuition and the
  road to Frankfort, the turnout numbers in sequence, the constitutional rewrites that won the
  organization almost no new power, and sixty years of verdicts on whether anyone was
  listening.</p>
  <span class="go">Read the patterns</span>
 </a>
 <a class="readfirst" href="events.html">
  <p class="lab">Or read what it did</p>
  <h2>What SGA put on</h2>
  <p>__PUTON__</p>
  <span class="go">Read the programmes</span>
 </a>
 </div>

 <div class="tools">
  <label class="field" for="q"><span class="lab">Search the board</span>
   <input id="q" type="search" autocomplete="off" spellcheck="false"></label>
  <p class="secnote" style="margin:8px 0 0">Names, years and entry headlines. For the full
  text of every entry, use <a href="history.html">the complete timeline</a>.</p>
  <div class="facets" role="group" aria-label="Filter the years">__FACETS__</div>
  <p class="readout" id="readout" role="status"></p>
 </div>

 <p class="numkey"><span class="sw"><b class="num pres">58</b> the number in
 <b class="kred">red</b> is which President of student government they are</span>
 <span class="sw"><b class="num reg">55</b> the number in <b>black</b> is which Student
 Regent they are</span></p>

 <div class="board" id="board">__GROUPS__</div>

 <div class="legend">
  <p>One plate to a person, the way the wall does it. A year in which the presidency changed
  hands therefore carries two or three plates, which is the whole point: the wall gives each
  year a single name and the people who finished somebody else's term disappear. The corner
  carries two numbers, because there are two offices and two lines of succession. The
  <b class="kred">red</b> number is their place in the line of presidents, counting people
  rather than years, so the fifty-eighth plate is the fifty-eighth person to hold the office.
  The <b>black</b> number is their place in the line of student regents, the seat on the
  Board of Regents that has existed since April 1968. Most people since then held both and
  carry both numbers; a few held only one. One plate has no number at all, because the
  archive cannot yet say which office that name held. They are gathered on the <a href="irregular.html">irregular terms page</a>.</p>
  <p>Each plate also carries the year and how many sourced entries that year has so far. A
  year with three entries is a year the archive has not given up much of yet, not a year in
  which little happened.</p>
  <p>A plate marked <b>unsettled</b> holds a name the record cannot yet place. A plate marked
  <b>corrected</b> holds a name this site has moved from the year the plaque gives it.
  The current year is outlined in red.</p>
 </div>

 <section class="starthere">
  <h2 class="sec" style="margin-top:0;border-top:0;padding-top:0">Where to start</h2>
  <p class="secnote">Six entry points, chosen for what they show about how this
  record was put together.</p>
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
 var word=n===1?'name':'names';
 if(s)readout.textContent=n+' '+word+' match \\u201c'+qi.value.trim()+'\\u201d.';
 else if(facet!=='all')readout.textContent='Showing '+n+' '+word+' of '+plates.length+'.';
 else readout.textContent='Showing all '+plates.length+' names.';
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
        f"All {len(ys)} academic years have a page, {ys[0]['id']} to {ys[-1]['id']}: sixty "
        f"years of student government, plus the year now running. {n_ev} entries are sourced to the "
        f"<cite>Herald</cite>, the WKU Timeline, SGA's own papers or the university archive; "
        f"{n_lead} presidents and student regents are recorded, {n_leg} pieces of legislation "
        f"are held as files, and {n_herald} further <cite>Herald</cite> index lines are "
        f"listed on the timeline. What is still unsettled is set out on the "
        f'<a href="corrections.html">corrections page</a>.')
    progs = [e for y in ys for e in y["events"] if is_program(e)]
    kc = {}
    for e in progs:
        kc[e["kind"]] = kc.get(e["kind"], 0) + 1
    top = sorted(kc.items(), key=lambda kv: -kv[1])[:3]
    named = ", ".join(f"{n} {KIND_MANY[k].lower()}" for k, n in top)
    puton_line = (
        f"The other half of the job: the concerts it booked, the lecturers it paid, the "
        f"films it screened and the services it kept running. {len(progs)} of them are "
        f"here, dated and sourced, from "
        f"{min(e['date'][:4] for e in progs)} to {max(e['date'][:4] for e in progs)}, "
        f"among them {named}. Where a source records what a night cost or what it took "
        f"at the gate, the figure is on the entry."
        if progs else
        "The concerts, lecturers, films and services student government ran for the "
        "campus, gathered in one place as the archive turns them up.")
    body = (body.replace("__PUTON__", puton_line)
                .replace("__COUNTS__", counts_line)
                .replace("__FACETS__", facet_html)
                .replace("__GROUPS__", "".join(groups))
                .replace("__STARTS__", starts)
                .replace("__PAYLOAD__", payload))
    desc = (f"A year-by-year record of the Student Government Association at Western "
            f"Kentucky University, 1966 to 2026. {n_ev} sourced entries across "
            f"{len(ys)} academic years, {n_src} citations.")
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


TIMELINE_CSS = """
/* ---- timeline: the year block ---- */
.tl{padding-bottom:56px}
.yr{margin:0;scroll-margin-top:2px}
.yr:first-child .yrbar{margin-top:8px}
.yrbar{position:sticky;top:0;z-index:6;background:var(--paper);
 display:flex;flex-wrap:wrap;align-items:baseline;gap:2px 18px;
 margin:46px 0 0;padding:12px 0 9px;border-top:2px solid var(--black);
 box-shadow:0 1px 0 var(--line),0 10px 12px -10px rgba(11,11,12,.10)}
.yrbar h2{font-size:1.32rem;letter-spacing:-.022em;font-variant-numeric:tabular-nums}
.yrbar h2 a{color:var(--ink);text-decoration:none}
.yrbar h2 a:hover{color:var(--red)}
.yrbar .who{margin:0;font-size:.9rem;color:var(--ink2)}
.yrbar .who span{color:var(--ink3)}
.yrbar .tally{margin:0 0 0 auto;font-size:.8rem;color:var(--ink3);
 font-variant-numeric:tabular-nums;white-space:nowrap}
.yrbar .tally b{font-weight:600;color:var(--ink2)}
@media(max-width:640px){.yrbar{gap:2px 12px;padding:10px 0 8px;margin-top:36px}
 .yrbar .tally{margin-left:0;flex-basis:100%}}

/* ---- timeline: one line ---- */
.hx .t .money{margin:7px 0 0;font-size:.87rem;color:var(--ink2);
 border-left:2px solid var(--red);padding-left:11px;max-width:var(--measure)}
.hx{display:grid;grid-template-columns:7.5rem 1fr;gap:0 26px;padding:16px 0;
 border-top:1px solid var(--line2)}
.rows .hx:first-child{border-top:0}
@media(max-width:640px){.hx{grid-template-columns:1fr;gap:4px;padding:14px 0}}
.hx .when{padding-top:4px;font-size:.83rem;font-variant-numeric:tabular-nums}
.hx .when time{display:flex;flex-direction:column;line-height:1.25}
.hx .when .dm{color:var(--ink2);font-weight:600}
.hx .when .yy{color:var(--ink3);font-size:.77rem}
@media(max-width:640px){.hx .when time{flex-direction:row;gap:0 6px}}
.hx .when .tag{display:block;margin-top:6px;font-size:10px;letter-spacing:.1em;
 text-transform:uppercase;color:var(--ink3)}
@media(max-width:640px){.hx .when .tag{display:inline-block;margin:0 0 0 10px}}
.hx .t{max-width:38rem}
.hx h3{font-size:1.03rem;line-height:1.35;margin:0 0 5px}
.hx .t p{margin:0;color:var(--ink);line-height:1.55}
.hx .cite{margin:9px 0 0;font-size:.82rem;color:var(--ink3);line-height:1.5}
.hx .cite a{margin-right:15px;overflow-wrap:anywhere}
.hx:target{background:var(--paper2);box-shadow:-14px 0 0 var(--paper2),14px 0 0 var(--paper2)}

/* ---- timeline: the unworked index ---- */
details.hidx{margin:18px 0 4px;border-left:2px solid var(--line);background:var(--paper2)}
details.hidx summary{cursor:pointer;padding:11px 16px;font-size:.86rem;color:var(--ink2);
 font-variant-numeric:tabular-nums}
details.hidx summary:hover{color:var(--red)}
details.hidx summary .hn{font-weight:600}
.hidx .hxin{padding:0 16px 10px}
.hidx .note{margin:0 0 4px;font-size:.8rem;color:var(--ink3);max-width:38rem}
.hidx .hx{padding:10px 0;border-top:1px solid var(--line)}
.hidx .hx .t{max-width:44rem;color:var(--ink2);font-size:.9rem;line-height:1.5}
.hidx .hx .t a{font-size:.8rem;margin-left:10px;overflow-wrap:anywhere}
.hidx .hx .when{font-size:.79rem}

/* ---- timeline: navigation and filters ---- */
.yearnav{border-top:1px solid var(--line2);margin:20px 0 0;padding:14px 0 4px}
.ynrow{display:flex;flex-wrap:wrap;align-items:baseline;gap:7px 8px;margin:0 0 9px}
.ynlab{flex:0 0 3.6rem;font-size:11px;font-weight:600;letter-spacing:.12em;
 text-transform:uppercase;color:var(--ink3)}
.yearnav a{font-size:.83rem;text-decoration:none;color:var(--ink2);white-space:nowrap;
 border:1px solid var(--line);padding:3px 8px;font-variant-numeric:tabular-nums}
.yearnav a:hover{border-color:var(--red);color:var(--red)}
.yearnav a .n{color:var(--ink3);margin-left:7px;font-size:.78rem}
.yearnav a.off{opacity:.34}
.tlkey{margin:14px 0 0;font-size:.84rem;color:var(--ink3);max-width:44rem}
.tlkey b{color:var(--ink2);font-weight:600}
.clearq{background:none;border:0;padding:0;margin-left:12px;color:var(--red);
 font-family:var(--ui);font-size:.86rem;cursor:pointer;text-decoration:underline;
 text-underline-offset:3px}
.totop{margin:34px 0 0;font-size:.86rem}
.hxnone{margin:0;padding:14px 0;color:var(--ink3);font-size:.9rem}
.hx[hidden],.yr[hidden],details.hidx[hidden],.hxnone[hidden]{display:none!important}
"""


def hx_date(iso):
    """A timeline date, stacked so the column scans down the page: day and month
    on one line, the year under it."""
    disp, mach, prec = fmt_date(iso)
    parts = disp.split(" ")
    if prec == "day":
        top, yr = " ".join(parts[:2]), parts[2]
    elif prec == "month":
        top, yr = parts[0], parts[1]
    else:
        top, yr = disp, ""
    y = f' <span class="yy">{h(yr)}</span>' if yr else ""
    return f'<time datetime="{mach}"><span class="dm">{h(top)}</span>{y}</time>'


def timeline_sections(ys, by_year, up):
    secs = []
    for y in ys:
        v = by_year[y["id"]]
        yid = y["id"]
        seen = {}
        rows = []
        for e in v["events"]:
            aid = event_anchor(e, seen)
            cites = [f'<a href="{up}y/{h(yid)}.html#{aid}">In the record</a>']
            if e.get("src"):
                cites.append(src_link(e["src"]))
                if e.get("src2"):
                    cites.append(src_link(e["src2"]))
            if e.get("src", {}).get("file"):
                cites.append(f'<a href="{up}docs/{h(e["src"]["file"])}">Read it here</a>')
            tag = '<span class="tag">campus</span>' if e.get("campus") else ""
            tag += kind_tag(e, "tag kind")
            pflag = ' data-p="1"' if is_program(e) else ""
            rows.append(
                f'<article class="hx" id="{h(yid)}-{aid}" data-k="e"{pflag}>'
                f'<div class="when">{hx_date(e["date"])}{tag}</div>'
                f'<div class="t"><h3>{h(e["title"])}</h3><p>{h(e["body"])}</p>'
                f'{money_line(e)}<p class="cite">{"".join(cites)}</p></div></article>')
        hx = []
        for x in sorted(v["herald"], key=lambda e: e["date"]):
            when = hx_date(x["date"])
            cite = src_link({"label": x["issue"][:60], "url": x["url"],
                             "pdf": x.get("pdf")})
            for ln in x["lines"]:
                hx.append(f'<div class="hx" data-k="i">'
                          f'<div class="when">{when}</div>'
                          f'<div class="t">{h(ln)} {cite}</div></div>')
        hx = "".join(hx)
        n_hx = sum(len(x["lines"]) for x in v["herald"])
        who = " &middot; ".join(f'{h(l["name"])} <span>({role_word(l)})</span>'
                                for l in y["leaders"]) or "No name recorded"
        tally = [f'<b>{len(v["events"])}</b> {"entry" if len(v["events"]) == 1 else "entries"}']
        if n_hx:
            tally.append(f'<b>{n_hx}</b> index {"line" if n_hx == 1 else "lines"}')
        idx = ""
        if hx:
            idx = (f'<details class="hidx"><summary><span class="hn">{n_hx}</span> further '
                   f'{"mention" if n_hx == 1 else "mentions"} in the <cite>Herald</cite> '
                   f'index</summary><div class="hxin">'
                   f'<p class="note">Article-index lines recorded from the digitised '
                   f'<cite>Herald</cite> and not yet written up as entries. Each one links '
                   f'to the issue it came from.</p>{hx}</div></details>')
        body = ("".join(rows) if rows
                else '<p class="hxnone">No entry has been sourced for this year yet.</p>')
        secs.append(
            f'<section class="yr" id="y{h(yid)}" data-y="{h(yid)}">'
            f'<div class="yrbar"><h2><a href="{up}y/{h(yid)}.html">{h(yid)}</a></h2>'
            f'<p class="who">{who}</p>'
            f'<p class="tally">{" &middot; ".join(tally)}</p></div>'
            f'<div class="rows">{body}</div>{idx}</section>')
    return "".join(secs)


TIMELINE_JS = """
<script>
(function(){
var hf=document.getElementById('hf'),hr=document.getElementById('hr'),
    cl=document.getElementById('hclear'),
    secs=[].slice.call(document.querySelectorAll('.yr')),
    chips=[].slice.call(document.querySelectorAll('.tlfilter button')),
    jumps={},kind='all';
[].slice.call(document.querySelectorAll('.yearnav a')).forEach(function(a){
 jumps[a.dataset.y]=a;});
// the search key is the text of the line itself, plus the year and the names in
// the year's heading, so a president's name finds their year
function keyOf(el,skip,skipTag){
 // the words a reader would search for: the record itself, not the furniture
 // (no role labels, no citation chrome, no tallies)
 var t='';
 [].slice.call(el.childNodes).forEach(function(n){
  if(n.nodeType===3){t+=' '+n.nodeValue;return;}
  if(n.nodeType!==1)return;
  if(skipTag&&n.tagName===skipTag)return;
  if(skip&&skip.test(n.className||''))return;
  t+=' '+keyOf(n,skip,skipTag);});
 return t;}
secs.forEach(function(sec){
 var bar=sec.querySelector('.yrbar'),
     who=sec.querySelector('.yrbar .who'),
     head=(who?keyOf(who,/^$/,'SPAN'):'')+' '+sec.dataset.y;
 sec._rows=[].slice.call(sec.querySelectorAll('.hx'));
 sec._rows.forEach(function(r){
  r._k=(keyOf(r,/cite|srcline|ext/)+' '+head).replace(/\\s+/g,' ').toLowerCase();});
});
function word(n,s,p){return n+' '+(n===1?s:p);}
function run(){
 var q=hf.value.toLowerCase().trim(),ne=0,ni=0,ny=0;
 secs.forEach(function(sec){
  var ve=0,vi=0,rows=sec._rows;
  for(var i=0;i<rows.length;i++){
   var r=rows[i],isx=r.dataset.k==='i',isp=r.dataset.p==='1',
       km=kind==='all'?true:kind==='i'?isx:kind==='p'?isp:!isx,
       ok=km&&(!q||r._k.indexOf(q)>-1);
   r.hidden=!ok;
   if(ok){if(isx)vi++;else ve++;}
  }
  var d=sec.querySelector('details.hidx');
  if(d){d.hidden=!vi;d.open=!!(q&&vi);
   var c=d.querySelector('.hn');if(c)c.textContent=vi;}
  var none=sec.querySelector('.hxnone');
  if(none)none.hidden=!!q||kind==='i'||kind==='p';
  sec.hidden=!(ve+vi)&&!(!q&&kind==='all');
  if(jumps[sec.dataset.y])jumps[sec.dataset.y].classList.toggle('off',sec.hidden);
  ne+=ve;ni+=vi;if(ve+vi)ny++;
 });
 var counted=[];
 if(kind==='p')counted.push(word(ne,'thing SGA put on','things SGA put on'));
 else{
  if(kind!=='i'&&(ne||!q))counted.push(word(ne,'entry','entries'));
  if(kind!=='e'&&(ni||!q))counted.push(word(ni,'index line','index lines'));}
 var what=counted.join(' and ');
 if(q&&!(ne+ni))hr.textContent='Nothing matches \\u201c'+hf.value.trim()+'\\u201d. '
   +'Try a name, a year or a single word.';
 else if(q)hr.textContent=what+(ne+ni===1?' matches \\u201c':' match \\u201c')
   +hf.value.trim()+'\\u201d, in '+word(ny,'year','years')+'.';
 else hr.textContent='Showing '+what+' across '+word(secs.length,'year','years')+'.';
 if(cl)cl.hidden=!q;
 var p=new URLSearchParams(location.search);
 if(q)p.set('q',hf.value.trim());else p.delete('q');
 if(kind!=='all')p.set('show',kind);else p.delete('show');
 var qs=p.toString();
 history.replaceState(null,'',location.pathname+(qs?'?'+qs:''));
}
chips.forEach(function(c){c.addEventListener('click',function(){
 kind=c.dataset.k;chips.forEach(function(x){
  x.setAttribute('aria-pressed',String(x.dataset.k===kind))});run();});});
hf.addEventListener('input',run);
if(cl)cl.addEventListener('click',function(){hf.value='';hf.focus();run();});
var p0=new URLSearchParams(location.search);
if(p0.get('q'))hf.value=p0.get('q');
if(/^[eip]$/.test(p0.get('show')||'')){kind=p0.get('show');
 chips.forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.k===kind))});}
run();
})();
</script>"""


def year_nav(rows, group):
    """Jump links to every year on the page, in decade rows."""
    out = []
    for label, items in rows:
        links = "".join(
            f'<a href="#y{h(yid)}" data-y="{h(yid)}">{h(yid)}'
            f'<span class="n">{n}</span></a>' for yid, n in items)
        lab = f'<span class="ynlab">{h(label)}</span>' if group else ""
        out.append(f'<div class="ynrow">{lab}{links}</div>')
    return (f'<nav class="yearnav" aria-label="Jump to a year">{"".join(out)}</nav>')


def timeline_head(title, kicker, lede, up, current_dec, counts, ynav):
    links = []
    for lo, hi, label, short, stem in DECADES:
        if lo == current_dec:
            links.append(f'<span>{h(short)}</span>')
        else:
            links.append(f'<a href="{up}history/{stem}.html">{h(short)}</a>')
    allx = ('<span>The complete timeline</span>' if current_dec is None
            else f'<a href="{up}history.html">The complete timeline</a>')
    n_ev, n_hx, n_prog = counts
    facets = [("all", "Everything", n_ev + n_hx), ("e", "Archive entries", n_ev),
              ("p", "What SGA put on", n_prog), ("i", "Herald index", n_hx)]
    chips = "".join(
        f'<button type="button" data-k="{k}" '
        f'aria-pressed="{"true" if k == "all" else "false"}">{h(lab)} '
        f'<span class="c">{n}</span></button>' for k, lab, n in facets
        if n or k not in ("i", "p"))
    return (f'<header class="head"><div class="wrap"><p class="kicker">{h(kicker)}</p>'
            f'<h1>{h(title)}</h1><p class="scope">{lede}</p></div></header>'
            f'<div class="wrap">'
            f'<div class="decnav">{" ".join(links)} {allx}</div>'
            f'<div class="tools">'
            f'<label class="field" for="hf"><span class="lab">Search the entries</span>'
            f'<input id="hf" type="search" autocomplete="off" spellcheck="false"></label>'
            f'<div class="facets tlfilter" role="group" aria-label="What to show">'
            f'{chips}</div>'
            f'<p class="readout" id="hr" role="status"></p>'
            f'<button class="clearq" id="hclear" type="button" hidden>Clear the search</button>'
            f'<p class="tlkey"><b>Entries</b> are the archive’s own record: each one is '
            f'dated, written up and carries the source it rests on. The grey blocks under a '
            f'year hold <b>index lines</b> from the digitised <cite>Herald</cite> that have '
            f'been recorded but not yet worked into the record.</p>'
            f'</div>{ynav}')


def render_history(ys, herald):
    by_year = {y["id"]: {"events": sorted(y["events"], key=lambda e: e["date"]),
                         "herald": []} for y in ys}
    for e in herald:
        yid = academic_year(e["date"])
        if yid and yid in by_year:
            by_year[yid]["herald"].append(e)

    def tally(block):
        return (sum(len(by_year[y["id"]]["events"]) for y in block),
                sum(len(x["lines"]) for y in block for x in by_year[y["id"]]["herald"]),
                sum(1 for y in block for e in by_year[y["id"]]["events"] if is_program(e)))

    def nav_items(block):
        return [(y["id"], len(by_year[y["id"]]["events"])) for y in block]

    n_ev, n_hx, n_prog = tally(ys)
    lede = (f"Every sourced entry in the archive, {n_ev} of them, in the order they "
            f"happened, with the {n_hx} unworked lines from the <cite>Herald</cite> index "
            f"kept separate under the year they belong to. {n_prog} of the entries are "
            f"things student government put on for the campus, and the filter above "
            f"will show only those. Jump to a year below, or read one decade at a time.")
    pages = {}
    rows = []
    for lo, hi, label, short, stem in DECADES:
        block = [y for y in ys if lo <= y["start"] <= hi]
        if block:
            rows.append((short, nav_items(block)))
    body = (timeline_head("The complete timeline", "1966 to 2026", lede, "", None,
                          (n_ev, n_hx, n_prog), year_nav(rows, True))
            + '<div class="body tl">'
            + timeline_sections(ys, by_year, "")
            + '<p class="totop"><a href="#main">Back to the top of the timeline</a></p>'
            + '</div></div>' + TIMELINE_JS)
    pages["history.html"] = shell(
        "The complete timeline · SGA 60",
        f"Every sourced entry in the SGA 60 archive, {n_ev} entries from 1966 to 2026, "
        f"in chronological order.", body, TIMELINE_CSS, depth=0, current="history.html")

    for i, (lo, hi, label, short, stem) in enumerate(DECADES):
        block = [y for y in ys if lo <= y["start"] <= hi]
        if not block:
            continue
        ev, hxn, pn = tally(block)
        d_lede = (f"{ev} sourced entries across {len(block)} academic years, "
                  f"{block[0]['id']} to {block[-1]['id']}, with {hxn} further lines from "
                  f"the <cite>Herald</cite> index held under the years they belong to.")
        if pn:
            d_lede += (f" {pn} of the entries are things student government put on for "
                       f"the campus.")
        pager = ""
        if i:
            p = DECADES[i - 1]
            pager += (f'<a href="{p[4]}.html">Previous decade<b>{h(p[3])}</b></a>')
        if i < len(DECADES) - 1:
            nx = DECADES[i + 1]
            pager += (f'<a class="r" href="{nx[4]}.html">Next decade<b>{h(nx[3])}</b></a>')
        dbody = (timeline_head(label, "The timeline", d_lede, "../", lo,
                               (ev, hxn, pn),
                               year_nav([("Years", nav_items(block))], False))
                 + '<div class="body tl">'
                 + timeline_sections(block, by_year, "../")
                 + '<p class="totop"><a href="#main">Back to the top of the decade</a></p>'
                 + f'<div class="pager">{pager}</div></div></div>' + TIMELINE_JS)
        pages[f"history/{stem}.html"] = shell(
            f"{label} · SGA 60",
            f"The SGA 60 timeline, {label.lower()}: {ev} sourced entries from "
            f"{block[0]['id']} to {block[-1]['id']}.",
            dbody, TIMELINE_CSS, depth=1, current="history.html")
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
            label = ("What the change rests on" if l.get("year_confidence") == "corrected"
                     else "What has been found so far")
            srcs = (f'<p class="lab" style="margin:14px 0 6px">{label}</p>'
                    '<ol class="srclist">'
                    + "".join(f"<li>{src_link(s)}</li>" for s in l["sources"]) + "</ol>")
        hunt = ""
        if not l.get("name_verified"):
            links = "".join(f'<li>{ext(u, h(t))}</li>' for t, u in name_searches(l["name"]))
            hunt = ('<p class="lab" style="margin:16px 0 6px">Where to look next</p>'
                    f'<ul class="searchlist">{links}</ul>')
        dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in facts)
        return (f'<section class="leader"><h2>{h(l["name"])} '
                f'<span class="r">{h(y["id"])}</span></h2>'
                f'<dl class="facts">{dl}</dl>{note}{srcs}{hunt}</section>')

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
<p class="prose">One name on the plaque is still recorded here exactly as it appears on it,
because no source has been found that settles it: <b>Keyanna</b>, which appears elsewhere as
Keyana. Guessing at a spelling would put a person in the record under a name they never used.
<b>Hargroave</b> and <b>Marcell</b> are settled and no longer guesses: the <cite>Herald</cite>
and SGA's own roster of former presidents, archived in September 2001, both give Hargrove and
Marcel, so the site follows them and prints the plaque's reading beside each.</p>
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
# ---------------------------------------------------------------- sources
def all_citations(ys):
    """Every citation on the site, once per use, as (academic year, label, url).
    Not deduplicated: the point is to weigh how much of the record rests on each
    collection."""
    for y in ys:
        for l in y["leaders"]:
            for s in l.get("sources") or []:
                yield y, s
            if l.get("photo") and l["photo"].get("src"):
                yield y, l["photo"]["src"]
        for e in y["events"]:
            if e.get("src"):
                yield y, e["src"]
        for d in y.get("documents") or []:
            if d.get("src"):
                yield y, d["src"]
        for p in y.get("photos") or []:
            if p.get("src"):
                yield y, p["src"]
        org = y.get("organization") or {}
        for o in org.get("executive", []):
            if o.get("src"):
                yield y, o["src"]
        for o in (org.get("senate") or {}).get("officers", []):
            if o.get("src"):
                yield y, o["src"]


def source_bucket(url, label=""):
    """Which collection a citation comes from. The buckets are the ones a
    researcher actually has to work differently."""
    u = (url or "").lower()
    if not u:
        return "unlinked"
    if "web.archive.org" in u:
        return "wayback"
    if "talisman" in (label or "").lower():
        return "talisman"   # the yearbook is scanned into more than one collection
    if "digitalcommons.wku.edu" in u:
        segs = [s for s in urllib.parse.urlparse(u).path.split("/") if s]
        seg = segs[0] if segs else ""
        if seg in ("context", "cgi"):
            seg = next((s for s in segs[1:] if s not in ("viewcontent", "article")), "")
        return {"dlsc_ua_records": "herald_print", "sga": "sga_records",
                "wku_timeline": "timeline", "talisman": "talisman",
                "bor": "wku_admin", "univ_senate": "wku_admin"}.get(seg, "topscholar")
    if "wkuherald.com" in u:
        return "herald_web"
    if "talisman" in u or "archive.org" in u:
        return "talisman"
    if "wku.edu" in u:
        return "sga_records" if "/sga" in u else "wku_admin"
    if "wikipedia" in u or "wikimedia" in u or ".edu" in u or ".gov" in u:
        return "elsewhere"
    return "press"


SOURCE_ORDER = ["herald_print", "herald_web", "talisman", "sga_records", "wku_admin",
                "timeline", "press", "wayback", "topscholar", "elsewhere", "unlinked"]
SOURCE_NAMES = {
    "herald_print": "The <cite>Herald</cite> back file, digitised",
    "herald_web": "The <cite>Herald</cite> online",
    "talisman": "The <cite>Talisman</cite>",
    "sga_records": "SGA's own records",
    "wku_admin": "WKU administrative records",
    "timeline": "The WKU Timeline",
    "press": "Local and national press",
    "wayback": "The Wayback Machine",
    "topscholar": "Other TopSCHOLAR collections",
    "elsewhere": "Reference works and other institutions",
    "unlinked": "Cited without a link",
}
SOURCE_SECTIONS = {"herald_print", "herald_web", "talisman", "sga_records",
                   "wku_admin", "timeline", "press", "wayback"}


def source_report(ys):
    """Count what the archive actually rests on, collection by collection."""
    rep = {k: {"n": 0, "urls": set(), "years": set(), "dec": {}, "hosts": {}}
           for k in SOURCE_ORDER}
    for y, s in all_citations(ys):
        k = source_bucket(s.get("url"), s.get("label"))
        r = rep[k]
        r["n"] += 1
        if s.get("url"):
            r["urls"].add(s["url"].rstrip("/"))
        r["years"].add(y["id"])
        d = (y["start"] // 10) * 10
        r["dec"][d] = r["dec"].get(d, 0) + 1
        host = urllib.parse.urlparse((s.get("url") or "").lower()).netloc
        if k == "wayback":
            m = re.search(r"web/[^/]+/(?:https?://)?([^/]+)", s.get("url") or "")
            host = m.group(1).lower() if m else "unknown"
        if host:
            r["hosts"][host] = r["hosts"].get(host, 0) + 1
    for r in rep.values():
        yrs = sorted(r["years"])
        r["first"], r["last"] = (yrs[0], yrs[-1]) if yrs else ("", "")
        r["thick"] = sorted(r["dec"].items(), key=lambda kv: -kv[1])[:3]
    rep["_total"] = sum(rep[k]["n"] for k in SOURCE_ORDER)
    return rep


HERALD_CITE = re.compile(
    r"\bHerald\b[^,;]*?\b(\d{2,3})\s*[:.]\s*\d+\s*,\s*\d{1,2}\s+([A-Za-z]{3,9})\.?\s+"
    r"((?:19|20)\d{2})")


def herald_volumes(ys):
    """The volume-to-academic-year map, read back out of the archive's own
    citations. Every pair here is carried by a citation that prints both the
    volume and the issue date."""
    pairs = {}
    for _, s in all_citations(ys):
        m = HERALD_CITE.search(s.get("label") or "")
        if not m:
            continue
        mon = next((i for i, name in enumerate(MONTHS, 1)
                    if name[:3].lower() == m.group(2)[:3].lower()), 0)
        if not mon:
            continue
        cal = int(m.group(3))
        start = cal if mon >= 8 else cal - 1
        pairs.setdefault(int(m.group(1)), {}).setdefault(
            f"{start}-{str(start + 1)[2:]}", 0)
        pairs[int(m.group(1))][f"{start}-{str(start + 1)[2:]}"] += 1
    return {v: sorted(d, key=lambda k: -d[k]) for v, d in sorted(pairs.items())}


def year_gaps(have, ys):
    """The academic years missing from a set, compressed into readable runs."""
    ids = [y["id"] for y in ys]
    runs = []
    for i, yid in enumerate(ids):
        if yid in have:
            continue
        if runs and runs[-1][1] == i - 1:
            runs[-1][1] = i
        else:
            runs.append([i, i])
    return [ids[a] if a == b else f"{ids[a]} to {ids[b]}" for a, b in runs]


SOURCES_CSS = """
.srcguide{max-width:none}
.holdings{width:100%;border-collapse:collapse;margin:18px 0 0;font-size:.92rem}
.holdings th,.holdings td{text-align:left;padding:9px 16px 9px 0;
 border-top:1px solid var(--line2);vertical-align:baseline}
.holdings thead th{border-top:0;border-bottom:1px solid var(--line);font-size:11px;
 font-weight:600;letter-spacing:.11em;text-transform:uppercase;color:var(--ink3);
 padding-bottom:7px}
.holdings td.n,.holdings th.n{text-align:right;font-variant-numeric:tabular-nums;
 padding-right:0;white-space:nowrap}
.holdings tbody tr:hover{background:var(--paper2)}
.holdings .sh{color:var(--ink3);font-size:.85rem}
.tscroll{overflow-x:auto;margin:0 0 6px}
.coll{padding:0 0 8px}
.coll h2{font-size:1.32rem;margin:52px 0 0;padding-top:16px;border-top:2px solid var(--black)}
.coll .what{font-size:.9rem;color:var(--ink3);margin:6px 0 0}
.cfacts{display:grid;grid-template-columns:max-content 1fr;gap:0 26px;margin:16px 0 20px;
 max-width:46rem;font-size:.93rem;border-top:1px solid var(--line2)}
.cfacts dt{font-family:var(--ui);font-size:11px;font-weight:600;letter-spacing:.11em;
 text-transform:uppercase;color:var(--ink3);padding:9px 0 0}
.cfacts dd{margin:0;padding:7px 0 0;color:var(--ink);font-variant-numeric:tabular-nums}
@media(max-width:560px){.cfacts{grid-template-columns:1fr}.cfacts dt{padding-top:12px}
 .cfacts dd{padding-top:2px}}
.good,.bad{max-width:var(--measure);margin:0 0 14px;padding-left:16px;
 border-left:2px solid var(--line)}
.bad{border-left-color:var(--red)}
.good p,.bad p{margin:0 0 .7em}
.good p:last-child,.bad p:last-child{margin-bottom:0}
.good .lab,.bad .lab{margin:0 0 5px}
.howto{max-width:46rem;margin:0 0 6px;padding:0 0 0 1.2em;font-size:.94rem}
.howto li{margin:0 0 7px}
.voltab{display:grid;grid-template-columns:repeat(auto-fill,minmax(148px,1fr));gap:0 22px;
 margin:14px 0 6px;font-size:.88rem;max-width:56rem}
.voltab div{display:flex;justify-content:space-between;gap:10px;padding:5px 0;
 border-top:1px solid var(--line2);font-variant-numeric:tabular-nums}
.voltab .v{color:var(--ink3)}
.voltab .twice{color:var(--red)}
.voltab .twice b{font-weight:600}
.method{max-width:var(--measure)}
.method ol{padding-left:1.2em}
.method li{margin:0 0 9px}
.rule{border-top:2px solid var(--black);margin:38px 0 0;padding:16px 0 0;max-width:46rem}
.rule p{font-size:1.05rem;margin:0 0 .6em}
.rule p b{font-weight:700}
"""


def _fact(rows):
    return "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows if v)


def _weight(rep, key, total):
    r = rep[key]
    if not r["n"]:
        return "Nothing in the archive rests on it yet."
    share = round(100 * r["n"] / total)
    items = f'{len(r["urls"])} separate items' if r["urls"] else "no linked items"
    return (f'{r["n"]} citations, about {share} per cent of the archive, drawn from '
            f'{items}.')


def _span(rep, key):
    r = rep[key]
    if not r["years"]:
        return ""
    same = r["first"] == r["last"]
    thick = ", ".join(f"{d}s ({n})" for d, n in r["thick"])
    span = r["first"] if same else f'{r["first"]} to {r["last"]}'
    return f"{span} &middot; thickest in {thick}" if thick else span


def render_sources(ys, leg, herald, n_docs, n_port, n_gal):
    rep = source_report(ys)
    total = rep["_total"] or 1
    vols = herald_volumes(ys)
    n_lead = sum(len(y["leaders"]) for y in ys)
    n_hx = sum(len(e["lines"]) for e in herald
               if academic_year(e["date"]) in {y["id"] for y in ys})
    leg_years = {e["session"] for e in leg}
    leg_gaps = year_gaps(leg_years, ys)
    doc_sessions = len({y["id"] for y in ys if y.get("documents")})
    wayback_hosts = sorted(rep["wayback"]["hosts"].items(), key=lambda kv: -kv[1])[:4]
    talisman_ia = sum(n for host, n in rep["talisman"]["hosts"].items()
                      if "archive.org" in host)

    # holdings table
    trows = []
    for k in SOURCE_ORDER:
        r = rep[k]
        if not r["n"]:
            continue
        share = round(100 * r["n"] / total)
        name = (f'<a href="#{k}">{SOURCE_NAMES[k]}</a>'
                if k in SOURCE_SECTIONS else SOURCE_NAMES[k])
        trows.append(
            f'<tr><td>{name}'
            f'<span class="sh"><br>{h(r["first"])}&#8211;{h(r["last"])}</span></td>'
            f'<td class="n">{r["n"]}</td><td class="n">{share}%</td>'
            f'<td class="n">{len(r["urls"])}</td>'
            f'<td class="n">{len(r["years"])}</td></tr>')
    holdings = (
        '<div class="tscroll"><table class="holdings">'
        '<thead><tr><th scope="col">Collection</th><th scope="col" class="n">Citations</th>'
        '<th scope="col" class="n">Share</th><th scope="col" class="n">Items</th>'
        '<th scope="col" class="n">Years</th></tr></thead>'
        f'<tbody>{"".join(trows)}</tbody>'
        f'<tfoot><tr><td><b>Everything cited</b></td><td class="n"><b>{total}</b></td>'
        f'<td class="n">100%</td><td class="n"></td><td class="n">{len(ys)}</td>'
        f'</tr></tfoot></table></div>')

    # the volume map
    vcells = []
    twice = [v for v, yy in vols.items() if len(yy) > 1]
    for v, yy in vols.items():
        cls = ' class="twice"' if len(yy) > 1 else ""
        label = " and ".join(h(a) for a in sorted(yy))
        vcells.append(f'<div{cls}><span class="v">Vol. {v}</span><b>{label}</b></div>')
    volmap = f'<div class="voltab">{"".join(vcells)}</div>'
    twice_line = (
        f'Volumes {", ".join(str(v) for v in twice)} each carry two academic years, '
        f'four years apart: the <cite>Herald</cite>&#8217;s volume numbering was restarted '
        f'in the mid-1970s and the archive holds citations from both runs. A volume number '
        f'on its own does not pin a year. The printed issue date does.'
        if twice else
        'Every volume in the archive maps to one academic year.')

    def coll(key, title, what, facts, good, bad, howto):
        return (f'<section class="coll" id="{key}"><h2>{title}</h2>'
                f'<p class="what">{what}</p>'
                f'<dl class="cfacts">{_fact(facts)}</dl>'
                f'<div class="good"><p class="lab">What it is good for</p>{good}</div>'
                f'<div class="bad"><p class="lab">Where it fails</p>{bad}</div>'
                f'<p class="lab" style="margin:18px 0 6px">How to search it</p>'
                f'<ol class="howto">{howto}</ol></section>')

    sections = []

    sections.append(coll(
        "herald_print", 'The <cite>College Heights Herald</cite>, digitised',
        'WKU Archives&#8217; scanned run of the student newspaper on TopSCHOLAR, '
        'catalogued issue by issue with the contents of each issue listed in the record.',
        [("What it holds", "Page-image PDFs of the paper, one record per issue, each "
                           "record carrying an article-level index of that issue"),
         ("Period it covers", _span(rep, "herald_print")),
         ("Weight here", _weight(rep, "herald_print", total)),
         ("Unworked index lines", f"{n_hx} lines are listed on the timeline but not yet "
                                  f"written up as entries" if n_hx else "")],
        '<p>This is the spine of the archive. Nothing else covers student government week '
        'by week for the first forty years: election results and turnout, senate votes, '
        'budget fights, resignations, and the editorials that argued with all of it. '
        'Because the index is catalogued per issue, a search returns the specific issue '
        'and date rather than a year, which is what makes a dated entry possible.</p>',
        '<p>The searchable text is the index, not the page. The body of an article is a '
        'scanned image, so a name that appears only in the fourth paragraph is invisible to '
        'search, and the index line is often the whole of what you can cite without opening '
        'the PDF.</p>'
        '<p>The digitised run thins out at the end of the 2000s. Nothing in this archive '
        f'after {h(rep["herald_print"]["last"])} rests on it; from there the '
        '<cite>Herald</cite> online takes over.</p>'
        '<p>TopSCHOLAR blocks automated requests. Its own search page refuses bots, and a '
        'burst of rapid requests gets every following request refused for a while.</p>',
        f'<li>Search Google rather than the site: '
        f'{ext("https://www.google.com/search?q=site:digitalcommons.wku.edu+%22student+government%22", "site:digitalcommons.wku.edu &quot;student government&quot;")}, '
        f'crossed with both calendar years of the academic year you are working on.</li>'
        f'<li>Try each name the organisation has used: Associated Students, Associated '
        f'Student Government, ASG, Student Government Association, SGA, student regent.</li>'
        f'<li>Browse the collection directly at '
        f'{ext("https://digitalcommons.wku.edu/dlsc_ua_records/", "digitalcommons.wku.edu/dlsc_ua_records")}.</li>'
        f'<li>One request at a time, a few seconds apart. If you are refused, stop for a '
        f'minute and start again slowly.</li>'))

    sections.append(
        f'<section class="coll" id="volumes"><h2>Reading a <cite>Herald</cite> citation</h2>'
        f'<p class="what">A citation here reads <b>Herald 50:45, 28 Mar 1975</b>: volume, '
        f'issue number, printed date. This table is the volume-to-year map the project has '
        f'established, read back out of the {len(vols)} volumes already cited here with '
        f'both a volume number and a printed date.</p>'
        f'{volmap}<p class="secnote" style="max-width:46rem">{twice_line} Volumes with no '
        f'row are volumes nothing has been cited from yet, not volumes that do not exist. '
        f'In the 1970s the paper published twice a week, so issue numbers run into the '
        f'fifties within a single year.</p></section>')

    sections.append(coll(
        "herald_web", 'The <cite>Herald</cite> online, wkuherald.com',
        'The student newspaper&#8217;s own website: full text, searchable, and the only '
        'continuous account of SGA for the recent decades.',
        [("What it holds", "Full-text articles, roughly 2003 to today"),
         ("Period it covers", _span(rep, "herald_web")),
         ("Weight here", _weight(rep, "herald_web", total))],
        '<p>Full text means a name, a bill number or a vote count can be searched directly, '
        'and meeting coverage is often detailed enough to date an event to the day. For '
        'everything after about 2003 this is the first place to look and usually the last.</p>',
        '<p>The site has been rebuilt more than once and the older articles moved with it. '
        'Links to the previous system, media.www.wkuherald.com, are dead, and the surviving '
        'copies are in the Wayback Machine.</p>'
        '<p>Its own search is weighted to recent material and misses much of the 2000s. '
        'Photographs and captions were frequently lost in the migrations, so an article can '
        'survive with its illustration gone.</p>',
        f'<li>Search the site directly: {ext("https://wkuherald.com/?s=student+government", "wkuherald.com/?s=student government")}, '
        f'then by officer name.</li>'
        f'<li>Where a result is missing or truncated, look the same URL up in the Wayback '
        f'Machine before giving up on it.</li>'
        f'<li>Google with {ext("https://www.google.com/search?q=site:wkuherald.com+SGA", "site:wkuherald.com SGA")} '
        f'catches pages the paper&#8217;s own search does not return.</li>'))

    sections.append(coll(
        "talisman", 'The <cite>Talisman</cite> yearbooks',
        'The university yearbook. For most of the twentieth century every volume carried a '
        'student government section with named portraits.',
        [("What it holds", "Officer portraits and organisation pages, named in the caption"),
         ("Period it covers", _span(rep, "talisman")),
         ("Weight here", _weight(rep, "talisman", total)),
         ("Portraits on this site", f"{n_port} of {n_lead} recorded leaders have a "
                                    f"portrait; {n_gal} further year photographs")],
        '<p>The yearbook is the best answer to the question of what these people looked '
        'like, and often the only place an executive council is listed office by office. '
        'The caption names the sitter, which is the identification this project requires '
        'before an image goes on a page.</p>',
        '<p>The <cite>Talisman</cite> PDFs on TopSCHOLAR are large and frequently refuse to '
        'download. The Internet Archive copies of the same volumes are far more reliably '
        f'downloadable, and {talisman_ia} of the images here came that way.</p>'
        '<p>A yearbook is published at the end of the year it names, so its portraits belong '
        'to the officers who served that year, not the ones elected in the spring it appeared. '
        'Captions misspell names, and a portrait can outlive the term it illustrates: never '
        'let a yearbook caption alone move a name into a year.</p>',
        f'<li>The run on TopSCHOLAR: '
        f'{ext("https://digitalcommons.wku.edu/dlsc_ua_records/", "digitalcommons.wku.edu/talisman")}.</li>'
        f'<li>The same volumes on the Internet Archive: '
        f'{ext("https://archive.org/search?query=talisman+western+kentucky", "archive.org, talisman western kentucky")}. '
        f'Try this first if a TopSCHOLAR download stalls.</li>'
        f'<li>The <cite>Talisman</cite> as it publishes now: '
        f'{ext("https://wkutalisman.com/", "wkutalisman.com")}.</li>'))

    sections.append(coll(
        "sga_records", "SGA&#8217;s own records",
        'Constitutions, bylaws, senate and cabinet minutes, and the legislation itself, '
        'split between the archived collection on TopSCHOLAR and what SGA currently posts.',
        [("What it holds", f"{len(leg)} pieces of legislation held here as files, "
                           f"{n_docs} archival documents mirrored across {doc_sessions} years"),
         ("Period it covers", _span(rep, "sga_records")),
         ("Weight here", _weight(rep, "sga_records", total)),
         ("Sessions with no legislation on file",
          h(", ".join(leg_gaps)) if leg_gaps else "None")],
        '<p>This is the only source that gives the exact text of what was passed, the vote '
        'as it was recorded, and the names of the senators in the room. Minutes settle '
        'arguments the <cite>Herald</cite> reports second-hand, and the constitutions date '
        'every structural change: when the regent seat merged with the presidency, when the '
        'senate was resized, what the judicial council could do.</p>',
        '<p>Coverage is lumpy rather than continuous. The archived collection is thickest '
        'for the 1990s; SGA&#8217;s own site holds only recent sessions and has dropped '
        'whole years when it was rebuilt. The gaps listed above are gaps in what has been '
        'found, and some of them are recoverable from the Wayback Machine.</p>'
        '<p>Minutes are summaries typed by a secretary, not transcripts. Bills are numbered '
        'by session and the numbering restarts, so a bill number without its session year '
        'identifies nothing.</p>',
        f'<li>The archived collection at '
        f'{ext("https://digitalcommons.wku.edu/sga/", "digitalcommons.wku.edu/sga")} '
        f'holds constitutions, minutes, correspondence and older legislation.</li>'
        f'<li>What SGA posts now: {ext("https://www.wku.edu/sga/", "wku.edu/sga")}.</li>'
        f'<li>For a missing session, try '
        f'{ext("https://web.archive.org/web/*/wku.edu/sga/*", "web.archive.org/web/*/wku.edu/sga/*")}.</li>'
        f'<li>What this archive already holds is listed on the '
        f'<a href="legislation.html">legislation page</a>.</li>'))

    sections.append(coll(
        "wku_admin", "WKU administrative records",
        'The other side of the table: Board of Regents minutes, university news releases, '
        'and the presidential correspondence held in the UA collections on TopSCHOLAR.',
        [("What it holds", "Regents minutes, UA record groups, WKU News releases"),
         ("Period it covers", _span(rep, "wku_admin")),
         ("Weight here", _weight(rep, "wku_admin", total))],
        '<p>Regents minutes are where a student resolution either becomes policy or dies, '
        'and they record the student regent as present, voting or absent. The UA collections '
        'hold the letters: the 1966 approval of the constitution is a letter from President '
        'Kelly Thompson to the committee that drafted it. WKU News dates appointments and '
        'awards precisely.</p>',
        '<p>Regents minutes are scanned and indexed by meeting, not by subject, so you need '
        'an approximate date before you can find anything. Student government is usually a '
        'line in a long agenda.</p>'
        '<p>WKU News is the university speaking about itself: it publishes what the '
        'administration wanted published and quietly retires old pages. Anything cited from '
        'it should be checked against the <cite>Herald</cite>, and older releases often '
        'survive only in the Wayback Machine.</p>',
        f'<li>Regents minutes: '
        f'{ext("https://digitalcommons.wku.edu/bor/", "digitalcommons.wku.edu/bor")}.</li>'
        f'<li>UA record groups and correspondence: search '
        f'{ext("https://www.google.com/search?q=site:digitalcommons.wku.edu+UA3+%22student+government%22", "site:digitalcommons.wku.edu UA3 &quot;student government&quot;")}.</li>'
        f'<li>{ext("https://www.wku.edu/news/", "wku.edu/news")} for the recent decades.</li>'))

    sections.append(coll(
        "timeline", "The WKU Timeline",
        'A curated collection of single dated events in the university&#8217;s history, '
        'each one described and citable on its own.',
        [("What it holds", "One record per event, with a date and a short description"),
         ("Period it covers", _span(rep, "timeline")),
         ("Weight here", _weight(rep, "timeline", total))],
        '<p>The quickest way to pin a date when you know roughly when something happened. '
        'Each record is already checked and already citable, which makes it a good anchor '
        'for the founding period and for campus events that frame an SGA year.</p>',
        '<p>It is a selection, not a record. Student government appears in it only when an '
        'event was significant to the university as a whole, so it will never carry an '
        'ordinary senate vote, and it is of little use for anything recent.</p>',
        f'<li>{ext("https://digitalcommons.wku.edu/wku_timeline/", "digitalcommons.wku.edu/wku_timeline")}, '
        f'browsable by year.</li>'
        f'<li>Or {ext("https://www.google.com/search?q=site:digitalcommons.wku.edu/wku_timeline+student+government", "site:digitalcommons.wku.edu/wku_timeline student government")}.</li>'))

    sections.append(coll(
        "press", "Local and national press",
        'Reporting from outside the university: the <cite>Bowling Green Daily News</cite>, '
        'regional public radio, and the national coverage that arrived in 2017.',
        [("What it holds", "Off-campus reporting on SGA and on the university"),
         ("Period it covers", _span(rep, "press")),
         ("Weight here", _weight(rep, "press", total))],
        '<p>Useful at exactly the moments when SGA stopped being a campus story: a fee '
        'increase that reached the city, a regent appointment, a resolution that drew '
        'attention beyond the Hill. The town paper also names people the <cite>Herald</cite> '
        'left as titles.</p>',
        '<p>There is no free, indexed archive of the <cite>Daily News</cite> before the '
        '2000s, so the founding decades have no local press record here at all: every '
        'citation for 1966 in this archive is a campus one, the <cite>Herald</cite>, the '
        'constitution file and the president&#8217;s approval letter.</p>'
        '<p>National attention came once, in 2017, around the reparations resolution, and '
        'much of what circulated was wrong: fabricated headlines claiming the university had '
        'granted free tuition. The archive cites the correction rather than the false '
        'headlines, and the wire stories themselves are not held here. Treat national '
        'coverage of a student government as evidence of what was said about SGA, not of '
        'what SGA did.</p>',
        f'<li>{ext("https://bgdailynews.com/?s=WKU+student+government", "bgdailynews.com, search WKU student government")}. '
        f'Most of it sits behind a paywall.</li>'
        f'<li>Check any national claim against the <cite>Herald</cite> and against SGA&#8217;s '
        f'own minutes for the same week before it goes into the record.</li>'))

    wb_list = ", ".join(f"{h(host)} ({n})" for host, n in wayback_hosts)
    sections.append(coll(
        "wayback", "The Wayback Machine",
        'Not a collection of its own: the route back to pages the university and the '
        'newspaper have taken down.',
        [("What it holds", f"Captures of pages that no longer exist, mostly {wb_list}"
                           if wb_list else "Captures of pages that no longer exist"),
         ("Period it covers", _span(rep, "wayback")),
         ("Weight here", _weight(rep, "wayback", total))],
        '<p>Officer lists, election results, committee rosters and news releases that WKU '
        'has since removed are frequently still readable in a capture, and the dead '
        '<cite>Herald</cite> CMS survives almost entirely this way. For the 1990s and 2000s '
        'web record it is not a fallback, it is the primary route.</p>',
        '<p>Crawls are irregular. A page may exist in one capture and never again, and the '
        'capture you find may predate the change you are looking for, so read the timestamp '
        'as the date of the evidence.</p>'
        '<p>Attached files are often not captured, navigation frequently breaks, and pages '
        'built by scripts come back half-empty. Always cite the dated capture URL, never the '
        'live URL it was taken from, because the live URL is the thing that failed.</p>',
        f'<li>Wildcard search a directory: '
        f'{ext("https://web.archive.org/web/*/wku.edu/sga/*", "web.archive.org/web/*/wku.edu/sga/*")}.</li>'
        f'<li>For older <cite>Herald</cite> articles, try the dead host: '
        f'{ext("https://web.archive.org/web/*/media.www.wkuherald.com/*", "web.archive.org/web/*/media.www.wkuherald.com/*")}.</li>'
        f'<li>Copy the capture URL with its timestamp into the citation.</li>'))

    body = f"""
<header class="head"><div class="wrap">
 <p class="kicker">Where the evidence lives</p>
 <h1>Sources</h1>
 <p class="lede">A working guide to the collections this archive is built from: what each
 one holds, the period it covers, how complete it is, how to search it, and where it lets
 you down.</p>
 <p class="scope">The {total} citations on this site come from the collections below. The
 figures are counted from the archive itself when the site is built, so they describe what
 has actually been found, not what exists.</p>
</div></header>
<div class="wrap"><div class="body srcguide">

<h2 class="sec" style="margin-top:34px">The holdings, weighed</h2>
<p class="secnote">Every citation on the site, grouped by the collection it comes from.
&#8220;Items&#8221; counts separate documents, issues or pages; a single issue cited by
four entries is one item.</p>
{holdings}

{"".join(sections)}

<section class="coll" id="method"><h2>The method, in practice</h2>
<p class="what">Three habits do most of the work.</p>

<p class="lab" style="margin:20px 0 6px">How to pin a date</p>
<div class="method"><ol>
<li>Date the event, not the paper. A <cite>Herald</cite> issue of 25 February reporting a
Tuesday senate vote dates the vote to the Tuesday, and the issue is the citation.</li>
<li>Use the printed issue date, never the volume and issue number alone. Volume numbers in
this run repeat four years apart.</li>
<li>Record only the precision the source gives. A day where it gives a day, a month where it
gives a month, a bare year where it gives a year. Padding a date to look precise is the one
error that cannot be spotted later.</li>
<li>Where a source says &#8220;last week&#8221; or &#8220;earlier this semester&#8221; and
nothing else fixes it, keep the month and stop.</li>
</ol></div>

<p class="lab" style="margin:20px 0 6px">How to check a name</p>
<div class="method"><ol>
<li>Start from the plaque in the SGA Chambers as a claim, not a fact. People who served have
reported that their year on it is wrong.</li>
<li>Cross the name with every name the organisation has used, in both calendar years of the
academic year, and look for election coverage rather than a passing mention.</li>
<li>Separate the offices. The student regent was separately elected from 1968 until the seats
merged around 2001, which is why several plaque years carry two names.</li>
<li>Two people can share a name. Do not merge a later career into a student record without a
source that connects them.</li>
<li>If the archive puts the term in a different year, move the person and keep the plaque
reading beside the correction. The correction is part of the history and is written down on
the <a href="corrections.html">corrections page</a>.</li>
</ol></div>

<div class="rule">
<p><b>No year, no entry.</b> A fact that cannot be placed in a year has nowhere to live in
this archive, and a fact without a source is not a fact yet. A thin year stays thin.</p>
<p class="secnote" style="max-width:none">Accuracy beats completeness. Everything on this
site can be checked from the links it carries; the whole record is published as data in
<a href="years.json">years.json</a>, and what is still unsettled is listed on the
<a href="corrections.html">corrections page</a>.</p>
</div>
</section>
</div></div>"""
    return shell("Sources · SGA 60",
                 "Where the evidence for SGA 60 lives: the Herald back file, the Herald "
                 "online, the Talisman, SGA's own records, WKU administrative records, the "
                 "WKU Timeline, the press and the Wayback Machine, with what each is good "
                 "for and where it fails.",
                 body, SOURCES_CSS, depth=0, current="sources.html")


STORY_CSS = """
.story{max-width:37rem}
.story p{font-size:1.06rem;line-height:1.66;margin:0 0 1.15em}
.story a{text-decoration-color:rgba(176,30,36,.42)}
.era{scroll-margin-top:14px}
.erahead{border-top:2px solid var(--black);margin:76px 0 0;padding-top:17px}
.erahead:first-of-type{margin-top:44px}
.erahead .yrs{font-family:var(--mono);font-size:.78rem;letter-spacing:.07em;
 color:var(--red);font-variant-numeric:tabular-nums;display:block}
.erahead h2{font-size:clamp(1.55rem,3.7vw,2.15rem);line-height:1.06;margin:9px 0 0}
.stand{max-width:37rem;color:var(--ink2);font-size:1.06rem;line-height:1.6;
 margin:14px 0 30px}
h3.sub{font-size:1.06rem;margin:36px 0 9px;max-width:37rem}
.pq{max-width:34rem;margin:30px 0 32px;padding:2px 0 2px 20px;
 border-left:3px solid var(--red);font-family:var(--display);font-weight:650;
 font-size:1.2rem;line-height:1.36;letter-spacing:-.01em;text-wrap:balance}
.pq b{display:block;font-family:var(--ui);font-weight:400;font-size:.83rem;
 letter-spacing:0;color:var(--ink3);margin-top:9px;line-height:1.5}
.contents{border-top:1px solid var(--line);border-bottom:1px solid var(--line);
 padding:18px 0 20px;margin:30px 0 0;max-width:46rem}
.contents ol{list-style:none;margin:12px 0 0;padding:0;
 display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0 30px}
.contents li{padding:8px 0;border-top:1px solid var(--line2)}
.contents a{font-family:var(--display);font-weight:650;text-decoration:none;
 border-bottom:1px solid rgba(176,30,36,.35)}
.contents span{display:block;font-family:var(--mono);font-size:.76rem;color:var(--ink3);
 letter-spacing:.05em;margin-bottom:3px}
.storyfoot{border-top:1px solid var(--line);margin:60px 0 0;padding:18px 0 0;
 max-width:37rem;color:var(--ink2);font-size:.95rem}
@media print{.contents{display:none}.erahead{break-before:page}}
"""

STORY_BODY = """
<header class="head"><div class="wrap">
 <p class="kicker">Sixty years, read straight through</p>
 <h1>The story</h1>
 <p class="lede">President Kelly Thompson approved a student constitution on 1 April 1966.
 Students ratified it on 26 April, 1,812 to 726. On 18 May they elected Jim Haynes the first
 president, and on 16 June Western Kentucky State College became Western Kentucky University.
 The student government and the university are almost exactly the same age.</p>
 <p class="scope">What follows is one continuous account of what that organization has done
 with itself since, drawn from the __NEV__ dated entries on this site. Every claim links back
 to the year it came from. Where the record is thin or contradicts itself, this page says so.</p>
</div></header>

<div class="wrap">
<nav class="contents" aria-label="The four eras">
 <p class="lab">Four eras</p>
 <ol>
  <li><span>1966&#8211;1980</span><a href="#seats">Seats, and then money</a></li>
  <li><span>1980&#8211;1992</span><a href="#vendor">Government or vendor</a></li>
  <li><span>1992&#8211;2010</span><a href="#apparatus">The apparatus arrives</a></li>
  <li><span>2010&#8211;2026</span><a href="#loud">Loud, then useful</a></li>
  <li><span>Across all four</span><a href="#repeats">What repeats</a></li>
  <li><span>The gaps</span><a href="#gaps">What the record does not hold</a></li>
 </ol>
</nav>

<div class="body">

<section class="era" id="seats">
<header class="erahead"><span class="yrs">1966 to 1980</span>
<h2>Seats, and then money</h2></header>
<p class="stand">Fourteen years spent converting an organization&#8217;s existence into
actual power. The first half is about winning seats. The second half is about spending a
budget, and nearly losing the organization over it.</p>

<div class="story">

<p>The ratification referendum drew 2,538 votes. It is a number worth holding onto, because
the record says most SGA elections since have not matched it. The
<cite>College Heights Herald</cite> greeted the founding with an editorial headed
&#8220;We Do Not Deserve Student Government.&#8221; A year later, reviewing the first full
term, the paper settled on three words: organization, progress, apathy. Those three words
describe the next fourteen years better than any summary written since.</p>

<p>The first half of the era is a hunt for seats. In February 1968 Western sent lobbyists to
Frankfort for a bill seating a student on the Board of Regents, and on 4 April the
<cite>Herald</cite> reported that president William Menser
<a href="y/1967-68.html#e-19680404-1">assumed duties as a board member</a>. It was the single
largest expansion of what the organization could reach, and it carried no vote. Students were
still campaigning for voting power in February 1970, the enabling bill
<a href="y/1969-70.html#e-19700313-1">was dropped that March</a> under a headline saying
lawmakers had kept students impotent, and the paper was still running
&#8220;Student Regent May Get Vote&#8221;
<a href="y/1971-72.html#e-19720201-1">in February 1972</a>.</p>

<p>The seat also came detached from the presidency almost immediately, which is why the plaque
in the SGA Chambers carries two names in several years. Bill Straeffer, elected president in
1968 by 1,732 votes to 1,098, was an out-of-state student, and the seat required a Kentucky
resident, so the Congress of Associated Students
<a href="y/1968-69.html">elected Paul Gerard to the board seat instead</a>. Straeffer&#8217;s
election is also the era&#8217;s most exactly measured: the organization&#8217;s own results
memo puts turnout at 2,894, about 34 per cent of roughly 8,500 students. The
<cite>Herald</cite> ran an editorial in the same issue headed &#8220;Elections Illustrate
Faults, Indifference.&#8221;</p>

<p>Blocked at the board, the organization took representation wherever it was actually offered.
The Regents <a href="y/1970-71.html#e-19700828-1">seated eight students on the Academic
Council</a> in August 1970. Students won six votes on a university council in April 1972. In
March 1979 president Steve Thornton and Terri Craig were
<a href="y/1978-79.html#e-19790327-1">elected to the executive council</a> of the Student
Government Association of Kentucky, two months after the body had pressed for a student seat
on a state-level council. Academic committees and statewide bodies opened before the board
did.</p>

<h3 class="sub">The week that decided what it was</h3>

<p>In one semester of 1969-70 the organization did two things it had never done. On 7 October
the Associated Student Congress <a href="y/1969-70.html#e-19691007-1">endorsed the Vietnam
Moratorium</a>, the clearest early instance of taking a position outside the campus fence. In
November an ASG committee <a href="y/1969-70.html#e-19691107-1">compiled Western&#8217;s first
student evaluations of teachers</a>, the first time the body produced data the university had
to reckon with rather than a resolution it could ignore.</p>

<p>Then came May 1970. In the Strike Western! week after the Kent State shootings, John Lyne
and Larry Zielke <a href="y/1969-70.html#e-19700508-1">presented resolutions to President Dero
Downing and Dean Charles Keown</a> on 8 May. On 16 May the Associated Student Congress
unanimously endorsed Downing&#8217;s reply to the protesters. Offered the most volatile campus
politics of the era, the elected student government positioned itself as the channel to the
administration rather than the opposition to it, exactly as a <cite>Herald</cite> piece of
February 1969 had suggested it might, saying the organization could deter turmoil at Western.
That posture explains why the era&#8217;s durable wins are procedural and domestic:
evaluations, visitation, women&#8217;s hours, book exchanges, a discount card.</p>

<p>It was not always accommodation. Linda Jones, <a href="y/1970-71.html#e-19710406-1">elected
the first woman president</a> on 6 April 1971, spent a single year on a section-by-section
constitutional rewrite, a formal endorsement of a Kentucky Civil Liberties Union lawsuit, under a headline that
also named the underground paper <cite>The Fly</cite>, a front page reading &#8220;Chaos Reigns at
Associated Students Meeting,&#8221; and her own published piece correcting the
<cite>Herald</cite>. Her <a href="y/1971-72.html">term closed</a> with a Mass Action Committee
calling for a strike over dorm visitation. In September 1972 the body
<a href="y/1972-73.html#e-19720929-1">rejected President Downing&#8217;s position on an Office
of Black Affairs</a>, weeks after passing a resolution deploring a cheerleader selection ruling
amid Black students&#8217; demands. And in June 1974 Gregory McKinney was
<a href="y/1973-74.html#e-19740619-1">sworn in as WKU&#8217;s first African American student
regent</a>, seven years before the first Black gubernatorial appointee joined the board. The
student seat integrated the Board of Regents before the governor did.</p>

<h3 class="sub">What money did to it</h3>

<p>In August 1973 the Board of Regents
<a href="y/1973-74.html#e-19730828-1">voted to increase the ASG allotment</a>, and the
organization became something else. It ran a Free University of no-cost evening courses, a
housing survey, paper recycling, and it booked Senate Watergate chairman Sam Ervin to speak in
April 1974. It also became a concert promoter. In September 1975 a show
<a href="y/1975-76.html#e-19750919-1">drew 4,300 people and lost $7,000</a>. Fund misuse
charges were aired in October. Quorum failure had already halted business twice in a single
week the previous February, and a <cite>Herald</cite> editorial said the confusion signalled a
need for change. Congress member Gerard Faulk faced impeachment hearings in March 1976 and was
acquitted in April. Seals and Crofts lost the organization $3,800 that November. By January
1979 ASG <a href="y/1978-79.html#e-19790125-1">faced losing control of student activities
funding</a> altogether.</p>

<p>The best single document of what a year of this organization actually consisted of is the
supplement ASG wrote and paid for in the <cite>Herald</cite> of
<a href="y/1975-76.html#e-19760427-1">27 April 1976</a>: women&#8217;s hours abolished with ASG
backing, better intramural facilities credited to its resolutions, a new discount card, a
second check-cashing site, a book exchange run with Veterans on Campus, plus the full roster of
congress members and every bill and resolution of the year. It is the first time in the record
the organization publishes its own accounting rather than letting the paper judge it.</p>

<p>The last stretch of the era is self-reform. Christy Vogt&#8217;s congress created a
constitutional revision committee in its first month, asked the university for a student
minimum wage, opposed a tuition increase, created a complaint committee, and in February 1977
passed Bill 6 proposing that ASG evaluate itself
<a href="y/1976-77.html#e-19770215-1">for transparency and improvement</a>. A resolution on
discrimination <a href="y/1976-77.html#e-19770225-1">failed the same month with fourteen
members abstaining</a>. Bob Moore won the following year by 26 votes, one of the narrowest
margins in the record. Steve Thornton&#8217;s year, 1978-79, produced the tightest cluster of
institutional change in the era: roll-call votes made public in September, a plan to
<a href="y/1978-79.html#e-19781019-1">add minorities to the regents&#8217; presidential
screening panel</a> in October, a revised constitution in November, a Minorities Board in
February. It landed during a presidential succession, with Downing resigning effective 31
December 1978 and Donald Zacharias taking office the following August. ASG intervened in how
the university chose its next president rather than reacting after the fact.</p>

<p>And the era ends where it began, on turnout. The spring 1979 primary
<a href="y/1979-80.html#e-19790412-1">drew 830 voters</a>. The same issue carried a piece
justifying student apathy in ASG voting. In thirteen years the <cite>Herald</cite> had moved
from scolding non-voters to explaining them.</p>

</div>
</section>

<section class="era" id="vendor">
<header class="erahead"><span class="yrs">1980 to 1992</span>
<h2>Government or vendor</h2></header>
<p class="stand">Twelve years of a body with very little money, chronic trouble filling its own
seats, and a student newspaper that treated it as a running joke. It answers by selling things,
then by rebuilding its own machinery, then by naming a chairman of the Board of Regents.</p>

<div class="story">

<p>Steve Fuller opened the era in autumn 1980 with a fight over dormitory room inspections. A
measure was voted down in September. A bill against bugs in the dorms
<a href="y/1980-81.html#e-19800911-1">drew a cartoon of an imperilled cockroach</a>. In
November ASG re-endorsed inspections in a session the <cite>Herald</cite> reported it had
nearly slept through, and a week later introduced a stricter room-entry rule. In October 1980
it also proposed changing its own name, twelve years before that actually happened.</p>

<p>From there almost no spring election in the era passes cleanly. Close races forced recounts
in April 1981. Marcel Bush resigned the presidency
<a href="y/1981-82.html#e-19820114-1">on 14 January 1982</a> and vice president David Payne
finished the term, which the Board of Regents minutes of 30 January confirm and the plaque
does not. That February the student regency became a campus-wide elected office for the first
time: five students filed, the 9 February vote produced no majority, and Sandra Norfleet
<a href="y/1982-83.html#e-19820216-1">won the runoff</a> into a term that ran about two months.
In April the general election results were voided, a decision the paper said disgusted the
candidates, and <a href="y/1982-83.html#e-19820420-1">the whole thing was run again</a> on 20
April. Margaret Ragan won the do-over.</p>

<p class="pq">Govern, the paper said, rather than market cards.
<b>The <cite>Herald</cite>&#8217;s verdict on the student discount card, 1 September 1983</b></p>

<p>The card was the era&#8217;s defining argument. ASG floated it in August 1983; the
<cite>Herald</cite> told it to govern instead; and on 8 September the paper reported that ASG
<a href="y/1983-84.html#e-19830908-1">would pay its own members a commission</a> on card sales,
drawing columns headed &#8220;Cheap Shots&#8221; and &#8220;And Old Tricks.&#8221; The body did
not settle the question. In October 1985 the congress passed Bill 85-15-F ordering production
of <a href="y/1985-86.html#e-19851012-1">its own discount card</a> anyway. Around it sat the
rest of the catalogue: a shuttle to the mall, a student book exchange, change machines in the
dorms, cable television in dorm rooms, weekend pizza from the Unicorn, microwaves in the
cafeterias, a left-handed desk in every classroom.</p>

<p>Jack Smith presided over two years of this and is the era&#8217;s most argued-over figure:
68 students filed the spring he won, his supporters filled the letters pages, he was accused in
print of partying while committees waited, he wrote in to protest a cartoon, and in April 1984
the paper caught him <a href="y/1983-84.html#e-19840410-1">impersonating a bunny</a> while his
ASG ran a low-turnout poll on beer and a campus pub. When he left in April 1985 the
<cite>Herald</cite> credited his enthusiasm with reviving interest in the organization.</p>

<h3 class="sub">The year the record changes shape</h3>

<p>Then the archive itself changes texture. <a href="y/1985-86.html">1985-86</a> is the first
year of the decade that holds a run of ASG&#8217;s own numbered legislation rather than only
<cite>Herald</cite> headlines: ten bills survive with their numbers and subjects, and the
story stops being about personalities. Mitchell McKinney&#8217;s congress abolished its
own Finance Committee in September 1985, wrote a Financial Advisory Council into the by-laws
the following April, created major and minor college representative seats, adopted a new
membership application, and
<a href="y/1985-86.html#e-19860401-2">asked that Board of Regents members attend and speak at
an SGA meeting</a> during their term - one of the few recorded attempts to bring the regents
into the room. McKinney then withdrew from re-election in March 1986, was commended by his own
outgoing congress, and was honoured by the Board of Regents on 8 August 1986, the same day the
board named Kern Alexander president. That summer the twenty years of amendments to the 1966
framework were <a href="y/1986-87.html#e-19860804-1">consolidated into a single document</a>,
the only such snapshot that survives.</p>

<p>What follows is a legitimacy crisis that ran six months. Scott Whitehouse won on 7 April
1988 amid editorials saying oversight and closed minds had marred the process, in a year when
only two of 32 congress positions were contested. Bruce Cambron demanded a new election a week
later over write-in votes the congress was told it could not ignore. ASG&#8217;s answer, on 15
September, was to <a href="y/1988-89.html#e-19880915-1">ban write-in campaigns</a>. The paper
said the block showed ASG was not listening. Cambron took his complaint to university president
Thomas Meredith on 6 October. The body narrowed its own franchise rather than reopen the
result. The same year it filed a formal written reaction to the General Education Task Force
proposal, one of the <a href="y/1988-89.html#e-19880101-1">earliest surviving examples</a> of
student government intervening in curriculum rather than campus life.</p>

<h3 class="sub">Letters, and then a name</h3>

<p>Amos Gott&#8217;s <a href="y/1989-90.html">1989-90</a> is the best-documented presidency
before 1992, and it is well documented because his ASG kept its mail. Resolutions went out as
memoranda to named administrators and answers came back: extended library hours, the final exam
schedule, AIDS and HIV education, the Downing University Center flagpole, the stadium press
box, mace sales at the bookstore, larger diplomas. For the first time in the era there is
evidence of what administrators said back.</p>

<p>Money shaped everything around it. In September 1989 the <cite>Herald</cite>
<a href="y/1989-90.html#e-19890912-1">reported ASG&#8217;s budget was tiny</a> compared with
student governments at other schools. Two weeks later the congress joined the Board of Student
Body Presidents while admitting it could not afford the dues. In November it killed a proposed
Public Interest Research Group over its fee system. Faced with being too small and too poor, it
voted in March 1990 to make itself bigger, and on the day Michael Colvin&#8217;s election was
reported it <a href="y/1989-90.html#e-19900419-1">called for the student activity fee to be
raised</a>.</p>

<p>Colvin&#8217;s year is the one where the internal machinery visibly works. His congress
asked for a left-handed desk in every classroom, killed a resolution that would have excused
absences tied to a widely publicised prediction of a New Madrid earthquake that never came,
rewrote the by-law governing how a presidential veto is overridden, and then
<a href="y/1990-91.html#e-19910314-1">used the new rule weeks later</a> when the emergency-kit
resolution survived a veto. It is the only veto fight the Herald index records that year, of the
organization&#8217;s separation of powers being exercised.</p>

<p>Heather Falmlen, who won in April 1991 amid protests, a boycott call and an editorial
condemning immature antics, held the presidency and the regency at once, which WKU&#8217;s own
newsletter confirmed that May. On 29 October 1991 her ASG passed Resolution 91-6-F
<a href="y/1991-92.html#e-19911029-1">asking that Joe Iracane not be re-elected chair of the
Board of Regents</a>, citing FBI, IRS and U.S. attorney investigations into an alleged $6
million payment to a mining company in return for contracts, and a separate alleged $14,500
consulting payment, and accusing him of overstepping into operations the board&#8217;s own
by-laws reserved for the president. It asked Falmlen to vote against him. The board re-elected
him <a href="y/1991-92.html#e-19911106-1">a week later</a>. No source in the archive reports
how the investigations ended.</p>

<p>The institutional answer came in January 1992, when the body introduced
<a href="y/1991-92.html#e-19920128-1">Bill #92-01-S</a>, creating a Student Advisory Committee
of class presidents, one representative from each college and the executive council, to brief
the student regent on Board of Regents agenda items and canvass student opinion before every
meeting. Having failed to move the board, it built a mechanism to bind the student seat to the
students.</p>

<p>Then the era ends in one week and in miniature. On 7 April 1992 the spring primary was
<a href="y/1991-92.html#e-19920407-2">cancelled outright</a> for want of candidates. The same
day the Associated Students voted to rename itself the Student Government Association, and
students ratified the change on 14 April. An organization that could not field enough
candidates to require a primary successfully renamed itself into a government.</p>

</div>
</section>

<section class="era" id="apparatus">
<header class="erahead"><span class="yrs">1992 to 2010</span>
<h2>The apparatus arrives</h2></header>
<p class="stand">Eighteen years in which the organization acquires every instrument of a real
government, faster than it acquires the mandate to use them. Each new power then turns on it in
sequence.</p>

<div class="story">

<p>Joe Rains took office that autumn as the first president under the new name, having been
elected in a race the <cite>Herald</cite> covered with a
<a href="y/1992-93.html#e-19920414-1">cartoon drawing him as Darth Vader</a>. His year&#8217;s
minutes appear under both titles, which is the only physical trace of the changeover. He pushed
an escort service, ran a call-in radio programme called Just Ask Joe, and went to Frankfort to
argue against cuts to higher education, for which the University Senate formally commended
him.</p>

<p>Four years later the organization built the one thing in this era that outlasted every
administration in it. Kristen Miller opened her term in August 1996 with
<a href="y/1996-97.html#e-19960829-1">a plan to drive party-goers home</a>. It became
Provide-A-Ride: a free blue fifteen-passenger van running Thursday and Friday nights from 11
p.m. to 2 a.m. anywhere in Bowling Green on a valid Western ID. It survived the doubts, posted
929 riders over twelve nights in the autumn of 2001, and was one of two things a president
explicitly protected when he made the first mid-year budget cut in SGA history twelve years
later. Miller also sat as the student representative on the committee that hired Gary Ransdell,
recalling in 2016 that there was one pot of money everyone was fighting over.</p>

<p>In one April 1997 session the congress passed resolutions to
<a href="y/1996-97.html#e-19970415-1">reactivate the Kentucky Students Association and
establish a student representative on the Council for Postsecondary Education</a>. Days later
it passed, by a slim margin, a measure calling for gay students to be included in
Western&#8217;s anti-discrimination policy. It is a rare recorded instance of
the congress dividing narrowly over a question that was not money, parking or grades.</p>

<h3 class="sub">The spring the Judicial Council became real</h3>

<p>In April 1999 the spring election collapsed. The Judicial Council
<a href="y/1998-99.html#e-19990420-1">overturned it on 20 April</a>. On the recount the
presidential margin narrowed from 616-611 to 614-611 out of 1,436 votes cast. The
vice-presidential race for finance was decided 700-688 and survived a judicial review over
campaign fliers left overnight on classroom desks. A letter to the editor reported fliers
circulating in dorms that attached the word racism to Will Jones, described as the first Black
candidate for the presidency in years, and questioned whether SGA&#8217;s investigation was
following proper procedure rather than assuming his involvement. The archive records plainly
that <a href="y/1999-00.html#e-19990415-5">no source found says how, or whether, that
investigation was resolved</a>.</p>

<p>Out of that election came Amanda Coates, whose signature project was publishing faculty
evaluations. From February 2000 she met the university president, the Faculty Senate chair and
its executive committee, and in April
<a href="y/1999-00.html#e-20000404-1">co-authored Resolution 00-2-S</a> asking for a mandatory
published evaluation from that autumn. The <cite>Herald</cite> confirmed that month that the
evaluations would be conducted and published. It did not hold: by November 2004 the ask had
been scaled back to a five-question pilot posted on TopNet, and faculty evaluations were still
listed as an unfinished goal.</p>

<p>On 27 October 2000 the Board of Regents voted 8-2 to raise the $16 student athletic fee by
$40 in January and another $40 that autumn. Student regent Cassie Martin was
<a href="y/2000-01.html#e-20001027-1">one of two dissenters</a>. That is the start of a pattern
that runs four administrations deep. Leslie Bedo told the board in August 2001 that voting a 9
per cent tuition rise before classes began sent a message to students, then joined the
unanimous vote. Katie Dawson abstained on a $46 construction fee in April 2006 after her
proposal to exempt the coming year&#8217;s seniors was rejected 10-1. Jeanne Johnson seconded a
motion to cap the 2008 increase at 6 per cent; it died with two votes. The seat gave students a
voice and almost never a result. By about 2001 the presidency and the separately elected
regency had merged into one office, which is what made every later resignation strip students
of board representation.</p>

<h3 class="sub">A fee it wrote itself, and a constitution nobody voted on</h3>

<p>In March 2003 the congress unanimously put a $3 student fee for campus radio station
Revolution 91.7 to the April ballot. The station was operating on a $7,000 budget unchanged
since 1998. The fee <a href="y/2002-03.html#e-20030408-1">passed 1,066 to 765 with 2,014
students voting</a>, the highest turnout figure recorded anywhere in the era. It was the first
student referendum in SGA history, and it demonstrated the thing the organization spent sixty
years failing to believe: a real question on the ballot brings students out.</p>

<p>The following spring the Constitutional Convention rebuilt the body into three branches and
made every enrolled student a member of SGA with the right to vote in its elections. That
document is the one WKU still recognises. Only
<a href="y/2003-04.html#e-20040316-1">132 of about 18,000 students voted to ratify it</a>.
Within weeks it failed its own first test: its author was elected the first speaker of the
senate 9 votes to 8, and the result was
<a href="y/2003-04.html#e-20040415-1">immediately contested</a> because the new text was
unclear on whether two-thirds meant of those eligible or of total membership.</p>

<p class="pq">&#8220;The turmoil within the organization.&#8221;
<b>Patti Johnson, 2004, on why she stayed in the job</b></p>

<p>Three presidencies did not survive their terms. Nick Todd was elected in March 2004 with 772
of 1,232 votes, was investigated over $611 missing from an SGA Dining Dollars account that had
started the year with $5,000, was <a href="y/2003-04.html#e-20040429-1">sworn in anyway</a> on
27 April with the case unresolved, and resigned in July citing personal conflicts. The internal
auditor found $872 in questionable purchases plus a $71 charge and recommended repayment.
About thirteen students turned up to the meeting for prospective candidates; Patti Johnson,
executive vice president the year before, was the only one interested, and
<a href="y/2004-05.html#e-20040928-1">won the special election with 1,291 votes</a>.</p>

<p>Rob Watkins, who had written the 2004 constitution and served as its first speaker, resigned
as president and student regent in November 2006. The resignation was read into the
senate&#8217;s own minutes on <a href="y/2006-07.html#e-20061128-1">28 November</a>, the day
after senators aired concerns about him at an unannounced 10 p.m. meeting. The
<cite>Herald</cite>&#8217;s editorial that week was headed &#8220;SGA actions an embarrassment
to Western.&#8221; Students had no voting voice on the governing board for at least a month,
and Jeanne Johnson had to win a February special election with 688 votes, 41 per cent of
ballots cast, to get it back. Two years later Johnathon Boles
<a href="y/2008-09.html">resigned on 30 January 2009</a> for health reasons; Kayla Shelton
succeeded him as president but not as regent; the Judicial Council voted 2-1 to hold a special
election over the written objection of the executive vice president and the dissent of the
chief justice, who then resigned; and the seat sat empty 26 days before Reagan Gilley won it
477 to 224.</p>

<p>Against all that, the era&#8217;s largest policy win. SGA had opposed plus/minus grading
since September 2003 with unanimous legislation, a petition past 1,500 signatures, a rally and
meetings with university donors. On 24 April 2007 Provost Barbara Burch told the University
Senate she <a href="y/2006-07.html#e-20070424-1">would not implement the system</a> the senate
itself had passed 36-23 the month before. It is the only case in the record where SGA beat the
faculty&#8217;s own governing body, across four years and three administrations.</p>

<p>The other genuinely new thing was a change in tactics. In October 2007 SGA organised Walk
Out Western, a class walkout protesting state cuts after Western received 54 per cent of the
funding the Council on Postsecondary Education had recommended; President Ransdell
<a href="y/2007-08.html#e-20071018-2">said he could not condone it</a>. Chief of staff Skylar
Jordan then built Listen Up Legislators, one-on-one senator-to-legislator meetings in Frankfort,
explicitly because the traditional February rally had not worked. Fifteen years of bus trips
were finally being examined as a tactic rather than repeated as a ritual. About fifty senators
filed <a href="y/2007-08.html#e-20080220-1">individual written reflections</a> after the
February 2008 trip, which the archive calls the richest first-person source in the whole
collection.</p>

<p>The era closes on the question it spent eighteen years arguing. In September 2009 Kevin
Smiley <a href="y/2009-10.html#e-20090904-1">nominated his brother</a> to the paid, voting post
of chief of staff, saying he had chosen him because he had no previous political agenda; a
former executive vice president called it completely unethical. In October three senators
resigned over his nomination of a member to the Student Publications Committee, which helps
choose the <cite>Herald</cite>&#8217;s editor-in-chief. That the flashpoint was the committee
choosing the paper&#8217;s editor closes a circle opened by the Darth Vader cartoon of 1992.</p>

</div>
</section>

<section class="era" id="loud">
<header class="erahead"><span class="yrs">2010 to 2026</span>
<h2>Loud, then useful</h2></header>
<p class="stand">The organization discovers it holds a gate, becomes an openly political actor,
pays for it, and then deliberately rebuilds itself as something smaller and more practical.</p>

<div class="story">

<p>In 2010 SGA was a 50-member body spending a $121,335 tuition-funded budget, with
<a href="y/2010-11.html#e-20110211-1">21 of its 50 members in Greek organizations</a> on a
campus under 8 per cent Greek. Its one piece of real leverage was procedural: the Board of
Regents could not approve the $49 million Downing renovation until SGA voted on the design and
the fee. President Gary Ransdell brought the plan to the 16 November 2010 meeting. Senators
<a href="y/2010-11.html#e-20101210-1">tabled it on 7 December</a> because three weeks was not
enough student input, which pushed SGA&#8217;s presentation to the Board of Regents from
January to April. It passed on second reading on 22 February 2011, capped at $49,128,545 with a
student fee of up to $70 a semester for twenty years. Students ended up paying $36 million of
the total. Nothing else in the era shows the organization exercising, and knowingly delaying,
formal consent over a capital decision.</p>

<p>In February 2013 the senate <a href="y/2012-13.html#e-20130301-2">rewrote its own
constitution</a>, replacing class-year seats with college-based representation and guaranteeing
seats for Glasgow and Owensboro. Every later expansion of the franchise runs from there: an
international student seat created by referendum in 2013, regional ambassadors in 2017, a
first-generation seat passed 33-0 in 2019, a Mahurin Honors College seat in 2023. The same
package had one clause stripped out of it, the one that would have barred SGA members from
receiving SGA scholarships. Four leaders, including the sitting president, published a
commentary calling that a breach of student trust and noting that
<a href="y/2012-13.html#e-20130319-1">eleven serving SGA members</a> had received such
members.</p>

<p>That spring also settled who could overrule SGA&#8217;s own judiciary. Keyana Boka won the
presidency on 4 April 2013 with 626 votes; five days later the Judicial Council disqualified
her 3-2 over a self-promotional email, on a complaint from the runner-up who would have become
president; Vice President for Student Affairs Howard Bailey reinstated her. Chief Justice Seth
Church called the intervention a serious infringement on the council&#8217;s autonomy, and the
council then <a href="y/2012-13.html#e-20130416-1">declined to contest it</a>.</p>

<h3 class="sub">Where its power ended</h3>

<p>Two votes three months apart taught the organization the limits of consent. On 22 September
2015 the senate voted 21-4 to
<a href="y/2015-16.html#e-20150922-1">disapprove the process by which the Confucius Institute
building was approved</a>, after Ransdell signed the contract in China in December 2014, more
than a month before the Board of Regents voted on it. President Jay Todd Richey wrote that
senators had warned him the vote would make powerful enemies. The Regents declined to revisit
the matter on 25 September and Richey told the senate it was a done deal. Then in January 2016
administrators <a href="y/2015-16.html#e-20160128-1">discarded Topper Tavern</a>, the pub name
students had chosen with 2,132 votes cast, in favour of Topper Grill and Pub. Richey said it
made SGA question how much the administration listened.</p>

<p>Richey was re-elected in April 2016 with 64 per cent of 2,442 votes, one of the
highest-turnout elections in the record and the first two-term presidency since 1988. His
second year produced the era&#8217;s two most revealing votes. In April 2017 a bill lowering
SGA&#8217;s own GPA floor from 2.5 to 2.0 <a href="y/2016-17.html#e-20170405-1">passed 24-7</a>,
exactly the margin required, after failing twice the previous year on arguments that senators
are expected to be elitist. It settled, for a decade, whether SGA existed to be representative
or exemplary. Two weeks later Resolution 6-17-S, supporting reparations for Black students,
<a href="y/2016-17.html#e-20170418-1">passed 19-10-1</a> and became national news, with wire
coverage, a cable television interview and fabricated headlines claiming WKU had granted free
tuition. Ransdell stated within days that it was not a university position. The substantive act
had come five months earlier: $750, matched by $100 from the Center
for Citizenship and Social Justice, for a
<a href="y/2016-17.html#e-20161130-2">scholarship memorializing Jonesville</a>, the Black
community WKU bought and demolished for under $200,000 in the late 1960s.</p>

<p class="pq">&#8220;Almost toxic in nature.&#8221;
<b>Andi Dahmer, March 2018, describing her own year as president</b></p>

<p>Andi Dahmer&#8217;s term is the most consequential single year in the era. Her senate failed
a clean DREAM Act resolution 12-17 in October 2017, then passed a narrowed DACA solidarity
resolution 32-1 in November. More than fifteen constitutional amendments were proposed against
about ten the year before. In April 2018 she
<a href="y/2017-18.html#e-20180424-1">told the <cite>Herald</cite></a> she had endured months
of harassment: senators cursing at her, a group message thread wishing her harm, and a profane
note left on her car on 9 February that prompted a police report. Title IX found the conduct
below the legal standard; the Office of Student Conduct issued no-contact orders against two
senators. She did not seek re-election, sued in September 2018, lost on summary judgment in
2021, had the case partially revived by the Sixth Circuit in 2022, and settled in January 2024
for $10,000 paid by WKU&#8217;s insurer. President Timothy Caboni
<a href="y/2017-18.html#e-20180501-1">convened a review</a> of the university&#8217;s Title IX,
equal opportunity and student conduct processes in May 2018.</p>

<p>The years on either side of it are the era at full volume. Stephen Mayer won the following
April with 35 per cent of 2,378 presidential votes, days after the Judicial Council had
<a href="y/2017-18.html#e-20180417-1">disqualified his ticket</a> over a Pepe the Frog image
used in campaign chalkings and then downgraded the penalty to a suspension before results were
announced. His senate voted 29-1 to relocate the marker identifying Bowling Green as the
Confederate capital of Kentucky, 30-0 to protect transgender students against a proposed
federal redefinition of sex,
and <a href="y/2018-19.html#e-20190424-1">23-1 to endorse a $5 per-student fee</a> to fund the
<cite>Herald</cite>, the paper that had been criticising it since 1966. In October 2019 senators
Symone Whalin and Anthony Survance organised a protest at a sorority philanthropy event over a
video of members singing a racial slur, wrote a resolution seeking discipline up to suspension,
got it through the senate 24-7, and
<a href="y/2019-20.html#e-20191030-1">lost it to a 4-0 executive veto</a>, with President Will
Harris abstaining and then facing questions about his standing as an Alpha Xi Delta knight.
Survance said they had wanted more than an article in the <cite>Herald</cite>.</p>

<h3 class="sub">The one it won outright</h3>

<p>Then the pandemic. With campus closed, SGA postponed its spring 2020 elections until at
least September, wrote an emergency clause into its constitution extending cabinet terms under
judicial oversight, and <a href="y/2019-20.html#e-20200420-1">gave its remaining budget</a> to
WKU&#8217;s Opportunity and Emergency Relief funds. That autumn Associate Provost Rob Hale
rebuffed SGA&#8217;s request to restore Pass/D/Fail grading, calling the extended drop deadline
sufficient. President Garrett Edmonds said he was deeply disturbed, ran a petition that took
3,500 signatures in three days, the Faculty Senate voted 40-9, and on 1 December Provost Cheryl
Stevens <a href="y/2020-21.html#e-20201201-1">told faculty</a> students could take a pass in
place of a B or C. It is the era&#8217;s only unambiguous win against an administration
decision already made.</p>

<p>The volume kept rising for two more years. In December 2021 a resolution condemning bans on
the teaching of critical race theory <a href="y/2021-22.html#e-20211201-1">passed 16-15</a>
with two abstentions. In February 2023 the Speaker of the Senate took the President to the
Judicial Council over anti-transgender Instagram posts he had liked; the council
<a href="y/2022-23.html#e-20230217-1">voted unanimously against censure</a>; a Title IX report
seeking his removal was filed two days later; and on 21 February the Queer Student Union told
the senate it had struck SGA from its list of campus safe spaces and would not associate with
it until a public apology was issued, questioning the fairness of a council most of whose
members the president nominates. Cole Bornefeld, who was also student regent, said he always
commits to loving thy neighbor but could not commit to always agreeing.</p>

<h3 class="sub">Smaller on purpose</h3>

<p>What followed was a deliberate change in what the organization was for. Sam Kurtz ran
unopposed in 2023 and again in 2024. On 3 September 2024 the senate passed
<a href="y/2024-25.html#e-20240903-1">Bill 50-23-S</a> unanimously, reaffirming that SGA
represents the student body rather than acting as a political group and stating a duty to put
forward only nonpartisan legislation. The programme shifted to things a student could pick up
at an office: 450 Uber vouchers at $10 each, a Borrow-a-Calculator scheme built on a survey
finding 17 per cent of students owned none, dental and ID and transcript vouchers, $700 set
aside to pay other students&#8217; parking fines, money for the food pantry. When the student
group For the People told the senate in March 2024 that SGA was the only major organization not
to oppose a Kyle Rittenhouse campus visit, and that 40 per cent of the senate was Greek, Kurtz
replied that <a href="y/2023-24.html#e-20240329-1">as an apolitical organization</a> SGA&#8217;s
role was to ensure all voices could be heard. Spring 2025 scholarship applications reached 295
against a past average of about 40.</p>

<p>None of that made it independent. After the January 2025 executive order on federal
diversity programmes, the chief justice said the constitution might need amending, and Bill
21-25-S restructured the Diversity, Equity and Inclusion Committee as the Action and
Opportunity Committee. It <a href="y/2024-25.html#e-20250404-2">passed only after absent
senators were phoned onto Zoom</a> to make the two-thirds quorum, and was then ratified by 88
per cent of voters in April. On 1 October 2025 General Counsel Andrea Anderson
<a href="y/2025-26.html#e-20251001-1">told the senate</a> that Kentucky&#8217;s House Bill 4
applies to SGA because it receives university money, that its funding must be content neutral,
that social media counts as a resource, and that the WKU Pride Center would lose its Downing
Student Union office. For the first time in the record, outside statute rather than campus
politics was dictating SGA&#8217;s internal structure.</p>

<p>Rush Robinson ran in 2025 explicitly on turning SGA away from national politics toward
direct student advocacy, won unopposed on a turnout of 966, and presided over 56 pieces of
legislation, the most since 2018-19. He spent the year on student mental health with committee
chair Veronica Butler, citing a WKU professor&#8217;s finding that 44 per cent of students
reported depression symptoms and 10 per cent had considered suicide in the past year. Sitting
beside the faculty regent during a discussion of housing, he
<a href="y/2025-26.html#e-20260416-1">told the Faculty Senate to take a field trip</a> and look
at the residence halls. At his last Board of Regents meeting, on 5 June 2026, he
<a href="y/2025-26.html#e-20260605-1">cast the only vote against</a> a $204 tuition
increase.</p>

<p>The last thing the record shows is the clearest answer it gives to its own oldest complaint.
The 2026 presidential race was the first genuinely contested one in three years. Two tickets
took 27 student-submitted questions at a town hall and sat for a debate hosted with the campus
radio station. Caden Lucas, who had entered SGA as the inaugural Mahurin
Honors College senator in 2024, beat Jaden Marshall, who was seeking to become the first Black
male
student body president. <a href="y/2025-26.html#e-20260415-1">1,601 students voted</a>, 635
more than the year before, a rise of 66 per cent. At his
<a href="y/2026-27.html#e-20260428-1">first meeting</a> Lucas nominated Marshall as an at-large
senator. Days later he was named a 2026 Truman Scholar. Outgoing president
Robinson handed him the red suit jacket that passes from president to president, the one Sam
Kurtz had given Robinson the year before.</p>

</div>
</section>

<section class="era" id="repeats">
<header class="erahead"><span class="yrs">Across all four eras</span>
<h2>What repeats</h2></header>
<p class="stand">Six arguments the organization has never finished having.</p>

<div class="story">

<h3 class="sub">Turnout, and what actually moves it</h3>
<p>Every generation has treated low turnout as a moral failure of the student body. The numbers
say otherwise. The high points in the record are all contests or referendums: 2,538 in the 1966
ratification, 2,894 in the 1968 presidential race, 2,014 in 2003 when a radio-station fee was on
the ballot, 2,442 in Richey&#8217;s contested 2016 re-election, 2,447 in the disputed 2018
election, 1,601 in the contested 2026 race. The low points are all uncontested: 830 in the 1979
primary, about 500 in 1983, a cancelled 1992 primary, 132 votes to ratify a whole constitution
in 2004, 908 in 2014 which a <cite>Herald</cite> editorial called pathetic, 398 in the autumn of
2021, 966 for an unopposed ticket in 2025. In the spring of 2011
<a href="y/2010-11.html#e-20110407-1">all 35 senate candidates were elected to 36 seats</a>,
each needing a single vote to win. The variable is the contest, not the electorate.</p>

<h3 class="sub">The constitution is never finished</h3>
<p>A new constitution was sent back for study in November 1969, four amendments went to a vote
in April 1970, a study committee reopened the question in January 1971, Linda Jones&#8217;s
congress voted section by section in February 1972, a constitutional change passed in March
1975, Bill 2 created another revision committee in September 1976, and a revised constitution
finally passed in November 1978. That is one rewrite attempt roughly every two years for the
whole first era, and the pattern never stops: revisions ratified in 1983, twenty years of
amendments consolidated in 1986, a by-law cluster in 1991, a three-branch rebuild in 2004, a
constitutional package in 2013, six referendums in 2017, a DEI committee renamed by referendum
in 2025, and a fully codified rewrite of the bylaws adopted on
<a href="y/2025-26.html#e-20260224-1">24 February 2026</a>.</p>

<h3 class="sub">Government or vendor</h3>
<p>Concerts in the 1970s, discount cards in the 1980s, book exchanges and web textbook deals in
the 1990s, vouchers and lending programmes in the 2020s. The <cite>Herald</cite> put the
question directly in 1983, telling the organization to govern rather than market cards, and the
organization answered by ordering its own card two years later. Forty years on it was buying
umbrellas, calculators, transcripts and CPR certifications for students to borrow or collect,
and calling that its central programme.</p>

<h3 class="sub">The paper</h3>
<p>The <cite>Herald</cite> is both the only witness for most of these sixty years and a standing
antagonist. It graded the government at the end of every year. It drew ASG as a cockroach
problem in 1980, its president as a salesman in 1989, and in the spring of 1992 one president
as a ventriloquist&#8217;s dummy and the next as Darth Vader. It ran
&#8220;Students Just Don&#8217;t Care&#8221; in 1996, &#8220;Gazebo-Gate&#8221; in 2002 and
&#8220;SGA misspending&#8221; in 2006. Presidents answered in print, sometimes for years. In April 2019 the senate voted 23-1 to endorse a student fee to
fund it.</p>

<h3 class="sub">Who gets appointed, and who gets the money</h3>
<p>In February 2016 a president told his own senate he had appointed 42 per cent of it and that
appointments should be more democratic. Bills to move committee chair appointments from the
president to the speaker failed in 2017 and again in March 2018, 26-2, with the speaker himself
voting against. A 2023 bill requiring a two-thirds vote before a vacant seat could become a
presidential at-large appointment failed 19-15, its sponsor calling appointment dependence a
dangerous practice for a government organization. The money question runs alongside it: an ASG
commission on discount card sales in 1983, SGA members receiving SGA scholarships in 2013, an
administrative vice president <a href="y/2023-24.html#e-20240209-1">censured 6-0 in 2024</a>
for spending funds before the senate approved them.</p>

<h3 class="sub">Never enough of it</h3>
<p>The operating budget was $12,100 in 1986-87, $121,335 in 2010-11, $138,500 in 2015-16 against
the University of Louisville&#8217;s $1.2 million, and $100,000 flat from 2018-19 onward. The
recurring problem is not only scarcity but the failure to spend: about $24,000 of $115,000 left
unspent and lost to the general fund in 2005-06, a $46,883.62 surplus at mid-year in 2014, and
a chief financial officer reporting in February 2026 that the autumn had produced more bills
than usual and spent under half the semester budget. The most memorable financial event in
sixty years is a surprise: a <a href="y/2011-12.html#e-20111118-1">$15,000 retroactive
Provide-A-Ride bill</a> in November 2011 that took $7,500 each from organizational aid and
scholarships.</p>

</div>
</section>

<section class="era" id="gaps">
<header class="erahead"><span class="yrs">The limits of the record</span>
<h2>What the record does not hold</h2></header>
<p class="stand">The shape of this story is partly the shape of what survived. Saying so is
part of the archive&#8217;s job.</p>

<div class="story">

<p>The plaque in the SGA Chambers is where the names start, and it is wrong in places. A
single-year 1968 plate reads Reed Morgan, and searches have turned up only his 1966 role as
chair of the committee that drafted the constitution and a forensics roster;
<a href="y/1968-69.html">no source describes him as president</a>. The plaque pairs Larry
Zielke and John Lyne under 1970-71, but <cite>Herald</cite> election coverage puts
<a href="y/1969-70.html">Zielke&#8217;s term a year earlier</a> and Lyne&#8217;s the year
after. David Payne&#8217;s plate reads 1982; he filled the balance of
<a href="y/1981-82.html">Marcel Bush&#8217;s 1981-82 term</a>. Every contemporaneous source for
1999-2000 gives the president as <a href="y/1999-00.html">Amanda Coates, never Lich</a>. Two
consecutive plates for 2014-15 record one continuous officeholder who
<a href="y/2014-15.html">changed her surname in mid-term</a>. The same happened to
<a href="y/1976-77.html">Christy Vogt</a>, whom the plaque calls Mollozzi. Keyana or Keyanna
is still doubtful, and doubtful spellings are flagged on the year pages, not fixed.</p>

<p>Whole stretches are thin in specific ways. For most of the 1980s the only witness is the
<cite>Herald</cite>&#8217;s article index, which reliably gives a headline and rarely gives a
result. The archive cannot confirm who won the April 1987 presidential election: the paper
endorsed the challenger on election day, indexed the race as no contest, and the surviving
issues never record the published outcome. For much of the 1990s the year pages note that no
full officer list, committee structure or seat count survives beyond the president, and between
the 1992 rename and the collapsed election of 1999 not one race in the record carries a vote
total. Three recent years, <a href="y/2019-20.html">2019-20</a>,
<a href="y/2021-22.html">2021-22</a> and <a href="y/2022-23.html">2022-23</a>, hold no account
of the organization&#8217;s own structure at all.</p>

<p>Some questions the record simply drops. No source found reports how the investigations into
Board of Regents chair Joe Iracane ended. No source found reports how, or whether, SGA resolved
its 1999 investigation into racially charged campaign fliers. The archive does not hold the
reason Bob Moore was ruled ineligible for an SGA job in September 1978. What is not known here
is written down as not known, on the <a href="corrections.html">corrections page</a> and on the
year pages themselves.</p>

<h3 class="sub">The decade it spent booking acts</h3>

<p>The archive holds __NPROG__ entries recording something student government put on, and
__NPROG70S__ of them fall in the ten academic years from 1970-71 to 1979-80. The lecture series brought James Farmer
in March 1969, which the <cite>Herald</cite>
<a href="y/1968-69.html#e-19690325-1">called a first for the series</a>; Dick Gregory, Julian
Bond and Bernadette Devlin over the next two years; and, jointly with the University Lecture
Series, Coretta Scott King, Betty Friedan and Buckminster Fuller.
Senator Edmund Muskie used an ASG lecture on 11 December 1973
<a href="y/1973-74.html#e-19731211-1">to call for Nixon&#8217;s impeachment</a>. __NLECTPRE79__ of the
__NLECT__ lecture entries in the archive are dated before July 1979.</p>

<p>The concerts were the expensive half. Ike and Tina Turner played Homecoming 1971
<a href="y/1971-72.html#e-19711015-1">before an estimated 12,000</a>. Chicago played free in
October 1972 and Jethro Tull followed three weeks later; the 1973
<cite>Talisman</cite> recorded that many in the audience
<a href="y/1972-73.html#e-19721026-1">called it the best concert ever staged at Western</a>, and
that it was a major financial loss. Kiss played Van Meter in December 1974 with fire-eating and
stage blood, after which Ron Beck, who did the booking,
<a href="y/1974-75.html#e-19741207-1">said he would never again help book the genre</a> because
it had no educational value for students.</p>

<p>Money moved in both directions. The Regents added $11,000 to the ASG allotment in August 1973
and <a href="y/1975-76.html#e-19750826-1">$16,000 to the entertainment budget</a> in August 1975,
which president Steve Henry said bought a second free concert. ASG ran on $42,000 for
entertainment in 1974-75. Against that, Dave Mason and
Kenny Loggins lost $13,200 in November 1977 and Atlanta Rhythm Section and Brick
<a href="y/1977-78.html#e-19780214-1">lost about $12,000</a> on Valentine&#8217;s Day 1978. The
crowds were at the free shows: 7,500 for the Spinners and Wet Willie in January 1976, 7,000 for
Barry Manilow that November. Chicago drew 10,450 on 15 October 1976 and
<a href="y/1976-77.html#e-19761015-1">grossed $53,092</a> against a $25,000 fee. The 1977
<cite>Talisman</cite> called it Western&#8217;s most financially successful concert.</p>

<p>Students argued about who chose the acts. About thirty of them picketed the doors of the Doc
Severinsen Homecoming concert in October 1974. Within days the <cite>Herald</cite>
<a href="y/1974-75.html#e-19741015-2">reported a coalition seeking change</a> in the booking; the
committee that came out of it wanted the activities vice president to negotiate with acts, and
settled for an advisory role because Kentucky law barred a student from controlling the funds.
ASG&#8217;s answer, in operation from 2 December 1975, was a
<a href="y/1975-76.html#e-19751202-1">Student Activities Committee</a> of seventeen members chosen
from 63 applicants: seven for concerts, five for lectures, five for publicity.</p>

<h3 class="sub">31 March 1979</h3>

<p>The programme did not survive its own accounts. ASG lost more than $23,000 on major concerts
in 1977-78, and dean of student affairs Charles Keown asked the Board of Regents to halve its
entertainment budget and to study whether the University Center Board should take the programming
over. Bob Moore argued at the meeting of 29 April 1978 that students would have less involvement,
and the Regents <a href="y/1977-78.html#e-19780429-1">let ASG keep the full $62,000</a> while
directing President Downing to appoint the committee. ASG hired the work out to Sunshine
Promotions of Indianapolis for 13 per cent of net profits; eight days before the
Homecoming show the firm had still not signed, because it would not post the $100,000 performance
bond Western required. Player and Exile
<a href="y/1978-79.html#e-19781103-1">grossed $25,694.29 after tax</a> against $24,000 of
production costs. The <cite>Herald</cite> told ASG on 9 November to get out of the concert
business, and the Outlaws cancelled in December after 242 tickets sold.</p>

<p>On 31 March 1979 the Board of Regents approved a rebuilt University Center Board and
<a href="y/1978-79.html#e-19790331-1">gave it $80,000</a> for programming. From the autumn its
committees of students and administrators ran the lectures and concerts ASG had been running. ASG
kept three seats on a board that also held the Greek councils, United Black Students, the two
residence hall councils, two other students and three faculty members. The university programs
coordinator, Tim Nemeth, said the new board would involve more student participation, and then
put its maximum at ten students working on lectures and concerts against the fifty involved under
ASG. President Jamie Hargrove said the transfer
<a href="y/1979-80.html#e-19800101-1">cost ASG between $60,000 and $70,000</a> of budget and no
real power; the year that followed was spent on opinion polls and a radio phone-in.</p>

<p>__NCONCPRE79__ of the archive&#8217;s __NCONC__ concert entries are dated before 31 March
1979. What follows is a thin and different record. Three entries are from 1999, when Amanda
Coates campaigned on bringing a major act to the Hill, was
<a href="y/1999-00.html#e-19990826-1">still pursuing one that August</a>, and got as far as an
October headline saying big-name concerts might arrive; the archive does not record that one
came. A Nappy Roots concert reached the senate agenda in September 2008 and the minutes never
say whether it happened. A resolution of April 2011 endorsed a benefit concert two other
student groups were running.</p>

<p>Then it comes back, small. SGA and the Campus Activities Board co-sponsored a free outdoor
show on South Lawn in September 2011 at which
<a href="y/2011-12.html#e-20110921-1">Cage the Elephant played to several thousand</a> and the
singer had to ask the crowd to stand back off the guard rail. In April 2025 SGA staged
<a href="y/2024-25.html#e-20250413-1">Pollooza</a>, an all-day festival on the same lawn with
food trucks and a bill drawn entirely from current WKU students, timed so that the spring
election opened that night. Thirty-two years after the Regents took the concerts away, the
organisation was putting on a music festival again, with its own students playing it.</p>

<h3 class="sub">Four times the office changed hands</h3>

<p>Four presidents have left before their year was out, and the way the office was filled was not
the same each time. Marcel Bush resigned on 14 January 1982 and his administrative vice president, David Payne, took
the balance of the term; the Board of Regents minutes of 30 January
<a href="y/1981-82.html#e-19820130-1">name Payne the president</a>. The Board seat did not travel
with the office. It went instead to a campus-wide special election in February, which Sandra
Norfleet won on a runoff, into a term the <cite>Herald</cite> measured at two months.</p>

<p>In 2004 the office was treated as vacant rather than inherited. Nick Todd resigned in July
after an investigation into an SGA Dining Dollars account, and his executive vice president Katie
Dawson <a href="y/2004-05.html#e-20040824-1">acted as president through the summer</a>; no source
found records her being sworn in. The presidency went back to the students in a special election
on 14 and 15 September, and Patti Johnson was the only one to come forward. Three people held the
office within twelve months.</p>

<p>By 2006 the executive vice president simply succeeded. SGA&#8217;s senate minutes for 28
November record Rob Watkins&#8217;s resignation being read to the chamber and senators being told
Jeanne Johnson would be sworn in a week later; the minutes of 5 December
<a href="y/2006-07.html#e-20061205-1">list the executive vice presidency as vacant</a> because
she had moved up. The Board seat still did not move, and Johnson had to win it in a February
special election. The same split ran again in 2009, when Kayla Shelton succeeded Johnathon Boles
as president but not as regent and the seat stood empty 26 days until Reagan Gilley
<a href="y/2008-09.html#e-20090226-1">won a special election 477 to 224</a>.</p>

<p>The plaque in the SGA Chambers gives one name to a year and cannot show a year that changed
hands. No plate on it carries Nick Todd&#8217;s name, or Reagan Gilley&#8217;s. Katie Dawson is
plated only for 2005-06 and Jeanne Johnson only for 2007-08, the full terms they went on to win
in their own right.</p>

<h3 class="sub">The services that kept coming back</h3>

<p>The earliest standing service in the record is a calendar of the month&#8217;s events
<a href="y/1966-67.html#e-19670119-1">posted outside the Associated Students office</a> in
January 1967. In May that year the <cite>Herald</cite> argued that Western should run a student
book exchange as Murray State and the University of Louisville did, noting that the one on this
campus belonged to the Veterans Club. ASG ran one in September 1969 and another from December
1972. By January 1976 it was running the
exchange with Veterans on Campus, selling more than 600 books at 25 cents profit each and
<a href="y/1976-77.html#e-19770204-1">more than 1,100 by February 1977</a>, and it called the
swap off for the spring of 1978.</p>

<p>It came back. ASG voted to study an exchange in September 1984, and over the Christmas break
four people keyed the listings into an IBM Personal Computer. The Book Exchanger appeared as a
tabloid that January; senior class president Danny Broderick said
ASG made no money from it and called it
<a href="y/1984-85.html#e-19850101-1">&#8220;a labor of love.&#8221;</a> By November 1987 it had
raised about $60 the previous autumn against printing costs of about $653, and the student
affairs chairman said he would recommend dropping it if that run failed.</p>

<p>The discount card ran longer and cost more. Twenty-one Bowling Green merchants signed in
December 1969, and the programme covered 29 by May 1977. Then it was taken twice. In September
1981 ASG filed complaints against a Texas and Georgia
firm that had taken $275 from each of at least four Bowling Green merchants for ASG-endorsed
cards that were never produced; Marcel Bush spent three weeks chasing it and found
<a href="y/1981-82.html#e-19810929-1">a disconnected number, an Atlanta number nobody answered
and a returned letter</a>. In November 1983 ASG printed its own after an agreement with a
Missouri company collapsed, putting nine businesses on the card, seven of which had paid that
company and never got a refund; president Jack Smith said of them,
<a href="y/1983-84.html#e-19831110-2">&#8220;They got what they paid for.&#8221;</a> ASG took
production in house in August 1986, after a later printer was indicted over the $500 he owed
it.</p>

<p>Getting students home is the thread that never stops. A volunteer escort service began in
September 1982, run with Interhall Council and the university police, walking women anywhere on
campus from dark until midnight on a single telephone number; its coordinator said it had
<a href="y/1982-83.html#e-19820902-2">filled 500 to 600 requests</a> in its first year, and the
public safety director said requests had tripled after two rapes the previous year. When
Provide-A-Ride&#8217;s contract lapsed in September 2009, three students set up a taxi in
the gap charging $5 a rider. The service&#8217;s own 2010 report counted
<a href="y/2010-11.html#e-20101022-1">more than 9,200 passengers</a> in 2009-10, with none for
2008-09 because a fire had destroyed the handwritten logs.</p>

<p>The modern form of it is the voucher: $1,225 for
<a href="y/2011-12.html#e-20120228-1">175 transcript vouchers</a> in 2012, $800 for 80
replacement student ID vouchers in 2013, $500 for 25 counselling registration vouchers in 2018,
$500 for 20 dental cleanings in 2022.</p>

<p class="storyfoot">Every fact above is drawn from a dated, sourced entry on this site. The
<a href="history.html">complete timeline</a> holds all __NEV__ of them in order; the
<a href="index.html">board</a> holds every year; <a href="events.html">what SGA put on</a>
gathers the concerts, lectures and services separately; the <a href="sources.html">sources
page</a> sets out what each collection covers and where it fails.</p>

</div>
</section>

</div></div>
"""


def render_story(ys):
    n_ev = sum(len(y["events"]) for y in ys)
    # counted from the record at build time, because these numbers moved twice
    # while the sections that quote them were being written
    prog = [(y, e) for y in ys for e in y["events"] if is_program(e)]
    lect = [(y, e) for y, e in prog if e["kind"] == "speaker"]
    conc = [(y, e) for y, e in prog if e["kind"] == "concert"]
    counts = {
        "__NEV__": f"{n_ev:,}",
        "__NPROG__": str(len(prog)),
        "__NPROG70S__": str(sum(1 for y, e in prog if 1970 <= y["start"] <= 1979)),
        "__NLECT__": str(len(lect)),
        "__NLECTPRE79__": str(sum(1 for y, e in lect if e["date"] < "1979-07-01")),
        "__NCONC__": str(len(conc)),
        "__NCONCPRE79__": str(sum(1 for y, e in conc if e["date"] < "1979-03-31")),
    }
    body = STORY_BODY
    for k, v in counts.items():
        body = body.replace(k, v)
    desc = ("Sixty years of student government at Western Kentucky University read as one "
            "continuous narrative, from the 1966 constitution to the 2026 election, with "
            "every claim linked to the year it came from.")
    return shell("The story · SGA 60", desc, body, STORY_CSS, depth=0, current="story.html")


def render_about(ys, meta, n_leg, n_herald, n_docs, n_port, n_gal):
    n_ev = sum(len(y["events"]) for y in ys)
    n_lead = sum(len(y["leaders"]) for y in ys)
    n_prog = sum(1 for y in ys for e in y["events"] if is_program(e))
    n_pres = len(ORDINAL["president"])
    n_reg = len(ORDINAL["regent"])
    n_pterm = sum(1 for y in ys for l in y["leaders"] if l["role"] == "president")
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

<h2 class="sec">The two offices</h2>
<div class="prose">
<p>The Kentucky legislature added a student to every state university's governing board in
1968. At Western the seat and the presidency of the student body have usually been held by
the same person, but they are two offices, and the record turns on the difference.</p>
<p>As the statute stood in 1972, the student regent <em>was</em> the student body president
by right &mdash; unless that president failed a test. KRS 164.320(8) then read that if the
president "is not a full-time student who maintains permanent residency in the Commonwealth
of Kentucky, a special election shall be held to select a full-time student who does maintain
permanent residency in this Commonwealth as the student member."
(<a class="ext" href="https://files.eric.ed.gov/fulltext/ED067026.pdf" rel="noopener">Kentucky
Revised Statutes Pertaining to Higher Education, June 1972, p. 12</a>)</p>
<p>That residency bar is why the offices came apart in the archive's early years. Bill
Straeffer, elected president in 1968, was an out-of-state student, so the Congress of
Associated Students elected Paul Gerard to the Board seat instead. The <cite>Herald</cite>
explained the same mechanism again in September 1972: "The student regent normally is the
president of the student governing body, if he is a Kentucky resident."</p>
<p>The requirement did not merely lapse; it was reversed. By the 1997 amendment the statute
said the student member "may be an out-of-state resident if applicable," and that permission
stayed on the books for at least sixteen years. The 2016 and 2017 rewrite dropped residency
language altogether. Today
(<a class="ext" href="https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=57974" rel="noopener">KRS
164.321(1)(j)</a>) the student member must be the elected student body president and a
full-time student, and nothing more; the residency conditions that remain in that section
apply only to the governor's appointees.</p>
<p>So a single name on the plaque after 1968 means one person holding both offices. More than one
name can mean either of two different things, and the difference matters. In six years the
offices were genuinely split, with someone other than the president on the Board: 1968-69 and
1969-70 (Paul Gerard), 1972-73 (Michael Fiorella), 1974-75 (Gregory McKinney), 1981-82
(Sandra Norfleet), and 2008-09, when Johnathon Boles resigned the presidency in January 2009,
Kayla Shelton succeeded him without taking the Board seat, and Reagan Gilley won it in a
special election the following month.</p>

<p>In the other years the presidency simply changed hands partway through, and the plaque
records the change poorly or not at all. Four presidents have left office early: Marcel Bush
in January 1982, Nick Todd in July 2004, Rob Watkins in November 2006 and Johnathon Boles in
January 2009. Each was followed by someone who finished the year, and this archive counts
those people as presidents, because they held the office, however briefly. The wall does not.
Nick Todd, elected in March 2004 and resigned by July, has no plate at all; Katie
Dawson, who filled the office through that summer, has one only for the year she was later
elected to; and Jeanne Johnson, who took over in December 2006, is plated only for the full
term she won afterwards. No president in this record has ever been removed by impeachment,
though the attempt has been made more than once.</p>
</div>

<h2 class="sec">Scope and content</h2>
<div class="prose">
<p>The archive holds one page for each of the {len(ys)} academic years from {h(ys[0]["id"])} to
{h(ys[-1]["id"])}, {n_ev} dated entries, and {n_lead} presidents and student regents with
their terms as far as the record supports them. Sixty years of student government come to
{len(ys)} academic years, which looks like an error and is not: the constitution was ratified
in April 1966, so {h(ys[0]["id"])} is the first year and {h(ys[-2]["id"])} the sixtieth, the
anniversary year. The {nth(len(ys))}, {h(ys[-1]["id"])}, is the one running now, and it is the
one in which the sixtieth anniversary is being marked: sixty calendar years from the spring of
1966 fall in the spring of 2026, at the end of the sixtieth academic year, and the occasion is
being kept the following autumn. So the archive covers sixty years of student government across
sixty-one academic years, and is published in the sixty-first. {n_pres} people have been student body
president, holding {n_pterm} terms between them, and {n_reg} people have held the student
seat on the Board of Regents since it was created in April 1968; each of them is given their
number in the line on their year page. The two counts differ because for most of the last
sixty years one person held both offices, and because of 1982-83, the one year since the seat
was created where the archive has no name for it at all: Margaret Ragan wrote in February 1983
that the presidency and the seat were separate posts, and who held the other one has not yet
been found. Entries cover the organization, not only its presidents: elections and turnout,
budgets, appointments, committee work, resolutions that passed and resolutions that failed,
and the fights with the administration and the <cite>Herald</cite>. Campus events that shaped
a year are included where they bear on student government and are marked as such.</p>
<p>{n_prog} of those entries record something student government put on for the campus
rather than something it debated: the concerts it booked, the lecturers it paid, the films it
screened, the festivals and annual traditions it ran, and the standing services it kept going.
Those entries carry a kind, which is what lets the same record appear on
<a href="events.html">its own page</a> grouped by what sort of thing it was, in a summary on
each president's year page, and as a filter on the timeline, without being stored more than
once.</p>
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

<h2 class="sec">Who counts as a president</h2>
<div class="prose">
<p>Anyone who held the office, for any length of time, by any route. Elected in April and served
the year; won a special election; succeeded to it as vice president when the president resigned;
or filled it in an acting capacity. Duration is not a qualification. Someone who held the office
for a week held it, and is counted and named here with everyone else.</p>
<p>This is not how the office has usually been recorded. The plaque in the Chambers gives one name
to each year, and so does every later list, including the history page on the university's own
site. A list written afterwards cannot show a year in which the presidency changed hands, so the
people who finished those years quietly drop out of the count. Each of them is on this site,
whether or not any plate carries their name, and they are gathered on the
<a href="irregular.html">irregular terms page</a>.</p>
<p>A person is counted once, at the first time they held the office, however many terms they serve
afterwards. Two plates are not two presidents when the surname changed in between, which has
happened at least four times here.</p>
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
<p>{h(meta.get("student_regent_history", ""))}</p>
<p>Michael Fiorella in 1972-73, Gregory McKinney in 1974-75 and Sandra Norfleet in 1982-83
are confirmed as regents rather than presidents. By about 2001 the two offices had merged;
after that, a second name in a year means a mid-year succession.</p>
</div>

<h2 class="sec">Sources</h2>
<div class="prose">
<p>The record rests on the <cite>College Heights Herald</cite>, digitised issue by issue on
TopSCHOLAR and then full text at {ext("https://wkuherald.com/", "wkuherald.com")}; on SGA's
own constitutions, minutes and legislation; on the university's administrative record; on
the <cite>Talisman</cite> yearbooks for portraits; and on the Wayback Machine for the pages
the university has taken down.</p>
<p>What each of those collections holds, the period it covers, how complete it is, how to
search it and where it fails is set out in full on the
<a href="sources.html">sources page</a>, together with the volume-to-year map for
<cite>Herald</cite> citations and the rules this project works by.</p>
<p>Every one of them is a public source available online, and that is the boundary of this
archive. Nothing here comes from a filing cabinet, a private paper, or anyone's memory. To
be on this site a thing had to happen and then be written down somewhere that has since
been scanned and published. Most of what student government has done in sixty years does
not clear that bar. The organisation has met most weeks since 1966; the record holds a few
thousand entries. What is missing is not the quiet part of the history, it is simply the
part that was never digitised, and a year that looks thin here is a thin record rather than
an uneventful year. Anyone who served, or was there, knows things this site cannot, and the
project would rather be told than go on guessing.</p>
</div>

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


# ---------------------------------------------------------------- patterns
PATTERNS_CSS = """
.contents{border-top:1px solid var(--line);border-bottom:1px solid var(--line);
 padding:18px 0 20px;margin:30px 0 0;max-width:46rem}
.contents ol{list-style:none;margin:12px 0 0;padding:0;
 display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:0 30px}
.contents li{padding:8px 0;border-top:1px solid var(--line2)}
.contents a{font-family:var(--display);font-weight:650;text-decoration:none;
 border-bottom:1px solid rgba(176,30,36,.35)}
.contents span{display:block;font-family:var(--mono);font-size:.76rem;color:var(--ink3);
 letter-spacing:.05em;margin-bottom:3px}
.part{scroll-margin-top:14px}
.parthead{border-top:2px solid var(--black);margin:78px 0 0;padding-top:17px}
.parthead:first-of-type{margin-top:42px}
.parthead .n{font-family:var(--mono);font-size:.78rem;letter-spacing:.07em;color:var(--red);
 display:block}
.parthead h2{font-size:clamp(1.55rem,3.7vw,2.15rem);line-height:1.06;margin:9px 0 0}
.stand{max-width:37rem;color:var(--ink2);font-size:1.06rem;line-height:1.6;margin:14px 0 26px}
.note{max-width:37rem;font-size:1.02rem;line-height:1.64;margin:0 0 1.1em}
.finding{border-left:3px solid var(--red);padding:2px 0 2px 20px;margin:28px 0 32px;
 max-width:35rem;font-family:var(--display);font-weight:650;font-size:1.18rem;
 line-height:1.38;letter-spacing:-.01em;text-wrap:balance}
.finding b{display:block;font-family:var(--ui);font-weight:400;font-size:.83rem;
 letter-spacing:0;color:var(--ink3);margin-top:9px;line-height:1.5}
.pindex{margin:0 0 6px;padding:0;list-style:none;max-width:46rem;
 display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:0 30px}
.pindex li{padding:9px 0;border-top:1px solid var(--line2);font-size:.93rem}
.pindex a{text-decoration:none;border-bottom:1px solid rgba(176,30,36,.32);
 font-family:var(--display);font-weight:650}
.pindex .sp{display:block;font-family:var(--mono);font-size:.74rem;letter-spacing:.05em;
 color:var(--ink3);margin-top:3px;font-variant-numeric:tabular-nums}
.pat{border-top:1px solid var(--line);padding:30px 0 4px;scroll-margin-top:14px}
.pat h3{font-size:1.16rem;margin:0}
.pat .sp{display:block;font-family:var(--mono);font-size:.76rem;letter-spacing:.05em;
 color:var(--ink3);margin-top:6px;font-variant-numeric:tabular-nums}
.pat .what{max-width:37rem;color:var(--ink2);font-size:.98rem;margin:11px 0 0}
.inst{list-style:none;margin:18px 0 0;padding:0;max-width:45rem}
.inst li{display:grid;grid-template-columns:4.4rem 1fr;gap:0 22px;padding:10px 0;
 border-top:1px solid var(--line2);font-size:.95rem}
.inst p{margin:0;max-width:var(--measure)}
.inst .yr{font-variant-numeric:tabular-nums;font-size:.85rem;color:var(--ink3);
 text-decoration:none;border-bottom:1px solid rgba(176,30,36,.28);justify-self:start;
 padding-top:2px}
.inst .yr:hover{color:var(--red)}
@media(max-width:560px){.inst li{grid-template-columns:1fr;gap:3px}
 .inst .yr{padding-top:0}}
.inst.wide{max-width:46rem}
h3.sub{font-size:1.1rem;margin:40px 0 0;max-width:37rem;padding-top:16px;
 border-top:1px solid var(--line)}
h3.sub+.note{margin-top:14px}
.shift{max-width:37rem;margin:18px 0 4px;font-size:.95rem;color:var(--ink);
 border-left:2px solid var(--line);padding-left:16px}
.shift b{font-family:var(--display);font-weight:700}
.tn{list-style:none;margin:22px 0 0;padding:0;max-width:46rem}
.tn li{display:grid;grid-template-columns:4.4rem 6rem 1fr;gap:0 22px;padding:11px 0;
 border-top:1px solid var(--line2);font-size:.95rem}
.tn .yr{font-variant-numeric:tabular-nums;font-size:.85rem;color:var(--ink3);
 text-decoration:none;border-bottom:1px solid rgba(176,30,36,.28);justify-self:start;
 padding-top:4px}
.tn .yr:hover{color:var(--red)}
.tn .c{font-family:var(--display);font-weight:700;font-size:1.05rem;
 font-variant-numeric:tabular-nums;letter-spacing:-.01em}
.tn p{margin:0;color:var(--ink2);max-width:var(--measure)}
.tn li.up .c{color:var(--red)}
@media(max-width:640px){.tn li{grid-template-columns:4.4rem 1fr;gap:0 18px}
 .tn .c{grid-column:2}.tn p{grid-column:2;margin-top:3px}}
.patfoot{border-top:1px solid var(--line);margin:60px 0 0;padding:18px 0 0;
 max-width:37rem;color:var(--ink2);font-size:.95rem}
@media print{.contents{display:none}.parthead{break-before:page}
 .pat,.inst li,.tn li{break-inside:avoid}}
"""


ANCHORS = {}


def index_anchors(ys):
    """Every anchor each year page will actually publish, so a link written
    against an older shape of the record can be repaired rather than left to
    land nowhere. Editing the archive moves anchors: merging two entries into
    one, or correcting a date, renumbers everything that shared that day."""
    ANCHORS.clear()
    for y in ys:
        seen = {}
        ANCHORS[y["id"]] = [event_anchor(e, seen)
                            for e in sorted(y["events"], key=lambda e: e["date"])]


def repair_anchors(html):
    """Point every link at an anchor the year page really publishes.

    Prose written by hand names an entry by its anchor, and anchors move when
    the record is edited. Rather than leave a link landing nowhere, send it to
    another entry on the same day, or failing that to the year itself."""
    def sub(m):
        up, yid, aid = m.group("up"), m.group("yid"), m.group("aid")
        live = ANCHORS.get(yid)
        if live is None or aid in live:
            return m.group(0)
        same = [x for x in live if x.startswith(aid[:10] + "-")]
        return (f'href="{up}y/{yid}.html#{same[0]}"' if same
                else f'href="{up}y/{yid}.html"')
    return re.sub(r'href="(?P<up>(?:\.\./)*)y/(?P<yid>[0-9\-]+)\.html'
                  r'#(?P<aid>e-\d{8}-\d+)"', sub, html)


def _yhref(yid):
    """A year id, optionally with an event anchor: 1966-67 or 1966-67#e-19660426-1.

    A named anchor that no longer exists is repaired: first to another entry on
    the same day, and failing that the fragment is dropped so the link still
    lands on the right year rather than nowhere at all."""
    if "#" not in yid:
        return f"y/{yid}.html"
    a, b = yid.split("#", 1)
    live = ANCHORS.get(a)
    if live is not None and b not in live:
        day = b[:10] if re.fullmatch(r"e-\d{8}-\d+", b) else None
        same = [x for x in live if day and x.startswith(day + "-")]
        b = same[0] if same else None
    return f"y/{a}.html#{b}" if b else f"y/{a}.html"


# Each pattern: id, heading, span, what it is, how it changed, and dated instances.
# An instance is (label, year id [+ anchor], what happened). Every instance is
# checked against data/years.json; where the miners' reading was not in the record
# it has been dropped rather than repeated.

STANDING = [
 {"id": "safety", "name": "Campus safety, lighting and getting home at night",
  "span": "1983&#8211;2026",
  "what": "Lighting, crosswalks, emergency telephones, escorts and rides home. Nothing "
          "on lighting or night safety appears in this archive before 1983, which is a "
          "fact about the surviving record as much as about the organization.",
  "shift": "The 1980s ask was a resolution asking the university to install something. "
           "The 1990s ask was hardware SGA lobbied for and then counted, one phone at a "
           "time. From 1996 it stopped asking and ran the service itself, and by 2011 that "
           "was costing it real money. By 2024 the answer was to subsidise a commercial "
           "service instead, and to go back to crosswalks, where the 1987 congress started.",
  "inst": [
   ("1983", "1983-84#e-19830823-1",
    "The <cite>Herald</cite>&#8217;s opening issue reported that the student escort service "
    "would resume."),
   ("1985", "1985-86#e-19851212-1",
    "Student government defeated a campus lighting proposal in the last week of the autumn "
    "semester."),
   ("1987", "1987-88#e-19871001-1",
    "The congress passed a crosswalk resolution; screens for dormitory windows filled much "
    "of the same autumn agenda."),
   ("1993", "1993-94#e-19931109-1",
    "Bill 93-6-F proposed buying and installing emergency telephones on campus."),
   ("1995", "1995-96#e-19950822-1",
    "Two more emergency phones went in at the start of the year."),
   ("1996", "1996-97#e-19960829-1",
    "&#8220;Kristen Miller Makes Plan to Drive Party-Goers Home&#8221; is the earliest "
    "indexed trace of what became Provide-A-Ride."),
   ("2000", "1999-00#e-20000101-1",
    "Provide-A-Ride ran free on Thursday and Friday nights, a fifteen-passenger van "
    "answering calls in about fifteen minutes."),
   ("2001", "2001-02#e-20011109-1",
    "929 riders over twelve nights between 20 September and 9 November."),
   ("2011", "2011-12#e-20111118-2",
    "A surprise $15,000 retroactive Provide-A-Ride bill took $7,500 from organizational aid "
    "and $7,500 from scholarships."),
   ("2015", "2014-15#e-20150429-1",
    "Bill 10-15-S put $825.95 into a surveillance camera by the Downing Student Union cash "
    "machines, passing 15-5."),
   ("2016", "2016-17#e-20161116-1",
    "SafeWalk launched, pairing students who felt unsafe with student escorts."),
   ("2017", "2016-17#e-20170208-1",
    "Safe Ride lost its Thursday service as ridership fell from about 5,000 in autumn 2015 "
    "to nearly 1,500 in autumn 2016. Richey blamed Uber&#8217;s arrival in Bowling Green."),
   ("2022", "2021-22#e-20220216-2",
    "Three crosswalk resolutions passed in a single night."),
   ("2024", "2023-24#e-20240215-2",
    "450 Uber vouchers worth $10 each, handed out through giveaways, meeting attendance and "
    "need-based scholarships."),
   ("2026", "2025-26#e-20260402-1",
    "Resolution 7-26-S backed a crosswalk at Alumni Avenue and Kentucky Street."),
  ]},
 {"id": "parking", "name": "Parking, the shuttle and getting around campus",
  "span": "1972&#8211;2026",
  "what": "Fees, spaces, routes, shelters and fines. The clearest register in the archive "
          "of a campus physically outgrowing itself.",
  "shift": "In 1972 students questioned a $5 vehicle registration fee. In 1983 two hundred "
           "of them voted for the idea of a shuttle at all. By 1991 the shuttle existed and "
           "the fight was over its fare. By 2015 SGA was voting to raise its own tuition to "
           "build a garage, and by 2024 it was capping the fines and paying them for "
           "students who could not.",
  "inst": [
   ("1972", "1972-73#e-19720822-1",
    "The regents approved a five dollar vehicle registration fee; the same issue reported "
    "students questioning it."),
   ("1979", "1978-79#e-19790426-1",
    "One of the outgoing Thornton administration&#8217;s final acts was a pair of "
    "resolutions on campus housing and parking policy."),
   ("1983", "1982-83#e-19830210-1",
    "206 students voted for a campus shuttle service."),
   ("1985", "1985-86#e-19851121-1",
    "The congress discussed running a shuttle from campus to the mall."),
   ("1988", "1988-89#e-19881103-1",
    "ASG sought shelters and seats for the campus shuttle stops."),
   ("1991", "1991-92#e-19910901-1",
    "Resolution 91-2-F asked for a one-way fare on the Big Red Shuttle for students who did "
    "not ride daily."),
   ("1994", "1994-95#e-19941101-1",
    "Expanded shuttle service, a route SGA had pushed to extend, drew enthusiasm from shops "
    "along the new stops."),
   ("1997", "1997-98#e-19971111-1",
    "A speed hump for the Regents Avenue lot and fifteen-minute parking spaces, among at "
    "least fifteen resolutions passed in a fortnight."),
   ("2002", "2001-02#e-20020327-1",
    "Bedo pressed the university after the Forest Park Trailer Park purchase collapsed and "
    "the Diddle Arena renovation removed about 200 spaces."),
   ("2003", "2003-04#e-20030930-1",
    "$8,000 asked for a shuttle shelter at the Jones-Jaggers stop."),
   ("2014", "2014-15#e-20141001-1",
    "A commuter focus group asked for an iWKU function listing free spaces in each lot, and "
    "a South Campus park and ride."),
   ("2015", "2014-15#e-20150303-1",
    "SGA backed a roughly 500-space, $10 million structure on part of Creason Lot, funded by "
    "a $30-a-semester tuition rise."),
   ("2024", "2023-24#e-20240215-2",
    "Resolution 18-23-S supported capping student parking fees at $50, noting citations ran "
    "from $10 to $600; a companion bill set aside $700 to pay other students&#8217; fines."),
   ("2026", "2025-26#e-20260414-2",
    "The parking director told the senate the monthly diesel bill for WKU buses, normally "
    "seven to eight thousand dollars, had reached fourteen."),
  ]},
 {"id": "textbooks", "name": "Textbooks and what they cost",
  "span": "1968&#8211;2022",
  "what": "Book swaps, exchanges, subsidies and the bookstore. One of the two oldest "
          "continuous service ideas in the record, and the one reinvented in every "
          "technology that came along.",
  "shift": "The grievance never changed and the object never stopped changing shape: a "
           "physical book swap, then a bulletin board in Grise Hall, then a dot-com link on "
           "the SGA website, then a cash subsidy matched by the bookstore, then two iPads, "
           "then a shelf of used Colonnade texts, then an argument about whether an "
           "inclusive-access programme should default to opt-out.",
  "inst": [
   ("1968", "1967-68#e-19680222-1",
    "The <cite>Herald</cite> reported the Associated Student Government directing a student "
    "book swap, in the same issue that questioned its Judicial Council."),
   ("1973", "1972-73#e-19730116-1",
    "ASG sponsored a student book exchange."),
   ("1975", "1975-76#e-19751125-1",
    "A spring book exchange co-sponsored by ASG and Veterans on Campus."),
   ("1984", "1984-85#e-19840920-1",
    "The congress began studying a book exchange; by January 1985 the venture looked likely "
    "to pause for the summer."),
   ("1991", "1990-91#e-19910101-5",
    "Bill #91-9-S proposed a book exchange bulletin board in Grise Hall."),
   ("1998", "1998-99#e-19981201-1",
    "Bill 98-12-F had SGA sponsor Bookswap.com."),
   ("1999", "1999-00#e-19991130-1",
    "Bill 99-17-F joined VarsityBooks.com and put a link on the SGA website, the first "
    "e-commerce deal in the digitised SGA record."),
   ("2005", "2004-05#e-20050414-1",
    "$2,000 to Buy-A-Book, matched by the University Bookstore and amended unanimously to "
    "help twenty students rather than ten."),
   ("2006", "2006-07#e-20061128-2",
    "Bill 11-06-F collected textbooks the bookstore would not buy back and sent them to "
    "Africa."),
   ("2008", "2008-09#e-20081119-1",
    "$500 to start a Textbook Subsidy Program, with $500 matched by the bookstore."),
   ("2011", "2011-12#e-20110930-1",
    "Two iPads loaded with textbooks, lent free through the Educational Resource Center."),
   ("2018", "2018-19#e-20181113-1",
    "Bill 18-18-F, $1,000 for a used-textbook library for Colonnade courses, was tabled "
    "24-3."),
   ("2022", "2022-23#e-20220914-1",
    "SGA pressed the administrator of the Big Red Backpack programme on why it defaulted to "
    "opt-out."),
  ]},
 {"id": "housing", "name": "Housing and the residence halls",
  "span": "1968&#8211;2026",
  "what": "Who may be in the building, what is in the building, who the building is for, "
          "and finally whether the building should still be standing.",
  "shift": "Three distinct eras. Rules, from 1968 to about 1985: women&#8217;s dormitory "
           "rules, curfews, visitation, coed halls, room inspections. Amenities, through the "
           "1980s and 1990s: cable, change machines, ice machines, sprinklers, windows that "
           "open. Then belonging and fabric, from 2011: the live-on requirement used as a "
           "bargaining chip, integration, rooming questions, mould, failing air conditioning "
           "and buildings scheduled for demolition.",
  "inst": [
   ("1968", "1967-68#e-19680229-1",
    "A committee investigating women&#8217;s dormitory rules ran in the same issue as a "
    "tuition increase and the Frankfort lobbying for a student regent."),
   ("1970", "1970-71#e-19701027-1",
    "The congress passed a resolution on the women&#8217;s curfew; the paper reported "
    "abolition was unlikely that year and called the curfew obsolete."),
   ("1972", "1971-72#e-19720428-1",
    "A Mass Action Committee called for a strike over dormitory visitation in the same week "
    "next year&#8217;s officers were installed."),
   ("1973", "1973-74#e-19730925-1",
    "An ASG housing survey urged improvement in dormitory conditions."),
   ("1977", "1977-78#e-19771117-1",
    "ASG and the Interhall Council backed a coed dormitory and the end of the door-ajar "
    "visitation rule."),
   ("1979", "1979-80#e-19791101-1",
    "ASG rejected a move to close Diddle Hall."),
   ("1980", "1980-81#e-19801113-1",
    "Having voted them down in September, ASG re-endorsed dormitory room inspections in a "
    "session the paper said it had nearly slept through."),
   ("1981", "1980-81#e-19810324-1",
    "Resolution 80-32 asked for change machines in the residence halls."),
   ("1986", "1985-86#e-19860401-3",
    "Bill 86-26-S asked for chains on Pearce-Ford Tower windows so they could be opened. "
    "In February 1990 the congress was still asking."),
   ("2011", "2011-12#e-20111005-1",
    "Ransdell told senators that ending the two-year on-campus living requirement did not "
    "work &#8220;from a business standpoint&#8221; while debt remained on renovations."),
   ("2017", "2016-17#e-20170223-1",
    "Housing and Residence Life&#8217;s ten-year plan made Southwest honors housing and "
    "Northeast international housing, with no mention of the integration SGA had endorsed "
    "27-1."),
   ("2018", "2017-18#e-20180411-1",
    "The senate voted 28-2 to make the sexual orientation question on housing applications "
    "optional and add one asking whether an applicant was comfortable rooming with an LGBTQ "
    "student."),
   ("2021", "2021-22#e-20210929-1",
    "SGA reported working with Housing and Residence Life on mould in the residence halls."),
   ("2025", "2025-26#e-20250902-1",
    "Caboni told the senate that community showers and bathrooms would be phased out as "
    "halls were replaced."),
   ("2026", "2025-26#e-20260416-1",
    "Sitting beside the faculty regent, Robinson told the Faculty Senate to take a field "
    "trip and see the state of the halls."),
  ]},
 {"id": "tuition", "name": "Tuition, fees and the road to Frankfort",
  "span": "1968&#8211;2026",
  "what": "Opposing the price of attending Western, lobbying the state about it, and &#8212; "
          "once the presidency and the student regent seat merged &#8212; voting on it.",
  "shift": "The 1970s and 1980s form was a resolution. The 1990s added the bus. The 2000s "
           "industrialised it, with reserved seats and a transport budget, and then began to "
           "doubt it: by 2012 the bus was cancelled when eight people signed up. Meanwhile "
           "the same student who wrote the resolution against the increase now sat on the "
           "board that passed it, and lost, usually alone.",
  "inst": [
   ("1968", "1967-68#e-19680229-1",
    "A tuition increase ran in the same <cite>Herald</cite> issue as the lobbying for a "
    "student seat on the Board of Regents."),
   ("1977", "1976-77#e-19770308-1",
    "Bill 9 formally opposed a proposed tuition increase, in the same March meeting that "
    "created a Complaint Committee for student grievances."),
   ("1981", "1980-81#e-19810205-1",
    "ASG asked the state to evaluate higher education, in a legislative season dominated by "
    "budget worries."),
   ("1991", "1990-91#e-19910212-1",
    "In a single February issue ASG wanted to cap tuition increases, proposed overhauling "
    "the Detrex registration system and planned lobbying to protect financial aid."),
   ("1992", "1992-93#e-19921211-1",
    "The University Senate adopted Resolution R92.11 commending president Joe Rains for "
    "joining a Frankfort rally against cuts."),
   ("2000", "2000-01#e-20001027-1",
    "The Board of Regents voted 8-2 to raise the $16 athletics fee by $80 in two "
    "instalments. Student regent Cassie Martin was one of the two dissenters."),
   ("2001", "2001-02#e-20010818-1",
    "Bedo told the board an August vote sent students a message, then joined the unanimous "
    "vote for a 9 per cent increase."),
   ("2003", "2002-03#e-20030304-1",
    "About 200 students from six public universities rallied at the Capitol. Sears said "
    "seventeen took the initiative to get on the bus."),
   ("2004", "2003-04#e-20040129-1",
    "The congress approved $650 for transport and reserved 47 seats for a February rally, "
    "under slogans about not balancing the budget on students&#8217; backs."),
   ("2006", "2005-06#e-20060408-1",
    "The regents approved a $46-a-semester construction fee 9-1 with Katie Dawson "
    "abstaining, and rejected her proposal to exempt the next year&#8217;s seniors 10-1."),
   ("2007", "2007-08#e-20071018-2",
    "SGA ran Walk Out Western, a class walkout aimed at Frankfort. Ransdell said he could "
    "not condone it."),
   ("2008", "2007-08#e-20080424-1",
    "Student regent Jeanne Johnson seconded a motion to cap the increase at 6 per cent. It "
    "died with two votes and the board approved 9."),
   ("2012", "2011-12#e-20120206-1",
    "SGA cancelled the $1,175 bus to the Frankfort rally after eight people confirmed, and "
    "arranged carpools instead."),
   ("2016", "2015-16#e-20160224-1",
    "Senators lobbied eight state officials in Frankfort against cuts that could have taken "
    "as much as 9 per cent of WKU&#8217;s funding."),
   ("2026", "2025-26#e-20260605-1",
    "At his last board meeting Robinson cast the only vote against a $204 increase, the "
    "sixth consecutive yearly rise."),
  ]},
 {"id": "aid", "name": "Scholarships and organizational aid",
  "span": "1979&#8211;2026",
  "what": "Money going out of the door: grants to student organizations and scholarships to "
          "individual students. The largest discretionary line in the modern budget, and the "
          "thing the organization most reliably points to when asked what it does.",
  "shift": "It began as a request that somebody else do it. By the mid-2000s SGA was the "
           "granting body, and its categories tracked whoever the campus had decided it was "
           "neglecting: study abroad, disability, the displaced Jonesville community, "
           "first-generation students, international students. Demand outran the money. "
           "About forty applications a year became 398 in 2019 and 295 in a single spring "
           "in 2025.",
  "inst": [
   ("1979", "1979-80#e-19791113-1",
    "Resolution 79-10 urged the university to assign staff to administer academic "
    "scholarships."),
   ("2006", "2006-07#e-20061024-1",
    "About $24,000 of the previous year&#8217;s $115,000 budget had gone unspent back into "
    "WKU&#8217;s general fund; the administrative vice president added almost $10,000 more "
    "to organizational aid."),
   ("2010", "2010-11#e-20100914-1",
    "The scholarship budget rose from $12,000 to $20,000 and general senate funding fell "
    "from $20,000 to $12,000 to pay for it."),
   ("2012", "2011-12#e-20120420-1",
    "About $34,000 in organizational aid reached roughly 50 organizations."),
   ("2016", "2016-17#e-20160907-1",
    "Bill 4-16-F created SGA&#8217;s first scholarships for students with disabilities, "
    "passing unanimously after a sophomore told senators his ADHD and dyslexia had cost him "
    "merit money."),
   ("2016", "2016-17#e-20161130-2",
    "$750, matched by $100, created the Jonesville Memorial Scholarship for the Black "
    "community WKU bought and displaced."),
   ("2018", "2018-19#e-20181024-2",
    "A recurring $2,000 first-generation scholarship passed 31-1."),
   ("2019", "2019-20#e-20191120-1",
    "A record 398 applications: 132 winter term, 122 first-generation, 81 study abroad, 31 "
    "scholar development, 10 for the Intercultural Student Engagement Center and 22 for a "
    "revived Earn-a-Computer scheme."),
   ("2022", "2021-22#e-20220420-3",
    "$15,500 across five scholarship programmes, including a first $500 for Black Student "
    "Alliance awards, alongside $8,000 of organizational aid at $500 a group."),
   ("2024", "2024-25#e-20240828-1",
    "A $100,000 budget carrying $20,000 for organizational aid and $23,500 for "
    "scholarships."),
   ("2025", "2024-25#e-20250416-4",
    "295 scholarship applications in one spring."),
   ("2026", "2025-26#e-20260311-1",
    "$10,000 split among 33 organizations in grants of $100 to $500."),
  ]},
 {"id": "grading", "name": "Grading",
  "span": "1983&#8211;2020",
  "what": "The scale itself and the mechanics around it: incompletes, the withdrawal "
          "deadline, the ten-point scale, plus and minus grades, value-added grading and "
          "finally pass/fail.",
  "shift": "Early legislation was procedural and small. From 2003 the category became a "
           "defensive war, and a finer grading scale kept coming back under a new name: a "
           "University Senate proposal in 2003, which Provost Barbara Burch declined to "
           "implement in 2007; Provost Gordon Emslie&#8217;s value-added scheme in 2012; a "
           "plus-minus resolution in 2013. In 2020 the polarity reversed. Instead of "
           "resisting a grading change SGA campaigned for one, and won.",
  "inst": [
   ("1983", "1983-84#e-19831027-1",
    "ASG passed its proposal on the deadline for incomplete grades after tabling it the "
    "week before."),
   ("1984", "1984-85#e-19840927-1",
    "Its proposal for a new grade scale was denied, the first setback of the autumn."),
   ("1994", "1994-95#e-19941101-3",
    "Resolution 94-11-F asked that students receive a grade before the withdrawal deadline "
    "so they could decide whether to drop."),
   ("1997", "1997-98#e-19970923-1",
    "Resolution 97-6-F called for the ten-point grade scale to be reinstated."),
   ("2003", "2003-04#e-20031016-1",
    "SGA unanimously passed legislation against the plus/minus system proposed in the "
    "University Senate. By November its petition had passed 1,500 signatures."),
   ("2007", "2006-07#e-20070424-1",
    "Provost Barbara Burch told the University Senate she would not implement the "
    "plus/minus system it had passed 36-23. President Jeanne Johnson credited SGA&#8217;s "
    "campaign."),
   ("2012", "2012-13#e-20121205-1",
    "Provost Gordon Emslie pitched value-added grading to SGA; the senate rejected the "
    "resolution in a close vote that February."),
   ("2013", "2012-13#e-20130226-2",
    "A plus-minus resolution was tabled with the idea floated of putting the question "
    "straight to students on the spring ballot."),
   ("2020", "2020-21#e-20201202-2",
    "After the provost&#8217;s office refused and a petition passed 3,500 signatures in "
    "three days, students could take a pass in place of a B or C."),
  ]},
 {"id": "library", "name": "Library hours",
  "span": "1986&#8211;2025",
  "what": "Keeping the library and the study space open later, particularly at finals.",
  "shift": "It started as a request to the administration. From 1999 SGA simply paid for it "
           "&#8212; $600 a year, described by 2011 as an annual practice, covering staff "
           "time and lighting to 2 a.m. By 2025 the ask had grown to round-the-clock hours, "
           "and the answer was that staffing made it unworkable.",
  "inst": [
   ("1986", "1985-86#e-19860320-1",
    "ASG proposals asked for more library hours, in the same issue that pushed the spring "
    "elections back a week."),
   ("1989", "1989-90#e-19891109-1",
    "Extended hours pursued through signed correspondence between president Amos Gott and "
    "three named administrators."),
   ("1999", "1999-00#e-19991130-1",
    "A bill extended library hours during finals week, passed the same day as the "
    "VarsityBooks.com deal."),
   ("2010", "2010-11#e-20101207-1",
    "The senate approved $600 to keep the library open until 2 a.m. during finals. "
    "President Colton Jessie said continuing the service was never in question."),
   ("2011", "2011-12#e-20111130-1",
    "$600 to Helm-Cravens for a 2 a.m. closing Sunday through Thursday of finals week, by "
    "then an annual practice."),
   ("2025", "2024-25#e-20250226-1",
    "Resolution 1-25-S sought 24/7 hours at the Commons at Helm during finals week."),
   ("2025", "2024-25#e-20250418-1",
    "The Faculty Senate endorsed it. The dean&#8217;s position was that staffing made "
    "24-hour service unworkable."),
  ]},
 {"id": "technology", "name": "Technology",
  "span": "1983&#8211;2026",
  "what": "Whatever the university had not yet bought students. The subject changes "
          "completely every decade; the posture does not.",
  "shift": "Cable television gave way to photocopiers and email accounts, then typewriters, "
           "then a printing quota, then a wireless network, then streaming video, then "
           "iPads, charging stations, second-hand computers, graphing calculators and "
           "finally bulk subscriptions to commercial artificial intelligence. The consistent "
           "move was SGA buying, on a small scale, the device gap it could see.",
  "inst": [
   ("1983", "1983-84#e-19831013-1",
    "ASG asked for cable television in dormitory rooms."),
   ("1996", "1996-97#e-19960917-1",
    "The September meeting created the SGA Technology Committee; student email accounts ran "
    "through the autumn minutes."),
   ("1997", "1997-98#e-19971104-1",
    "A bill to buy typewriters for the library, in the same week as designated driver "
    "cards."),
   ("1999", "1999-00#e-19990915-2",
    "Bill 99-10-F created an SGA Information Technology Director, with a companion bill "
    "writing website guidelines into the constitution."),
   ("2006", "2005-06#e-20060201-1",
    "SGA took up a $45-a-semester fee to pay for a campus-wide wireless network, a health "
    "centre and renovations."),
   ("2006", "2006-07#e-20061128-2",
    "Resolution 08-06-F backed a university study of a printing quota in the computer labs."),
   ("2007", "2007-08#e-20071025-1",
    "The Academic Affairs Committee prepared legislation for a roughly $1,995 subscription "
    "to some 45,000 educational video clips."),
   ("2013", "2013-14#e-20131024-1",
    "$1,598 with WKU Libraries for five charging stations, two of them for the Glasgow and "
    "Owensboro campuses."),
   ("2020", "2020-21#e-20201118-1",
    "The senate voted 28-3 to fund second-hand computers for the SGA office, the number "
    "scaled back to meet distancing guidance."),
   ("2024", "2023-24#e-20240228-1",
    "Borrow-a-Calculator, created after a survey found 17 per cent of students surveyed "
    "owned no calculator and 93 per cent had taken a class requiring one."),
   ("2026", "2025-26#e-20260414-1",
    "WKU&#8217;s new Artificial Intelligence Committee was in early talks about bulk "
    "subscriptions for all students."),
  ]},
 {"id": "health", "name": "Mental health, health services and wellbeing",
  "span": "1989&#8211;2026",
  "what": "The campus clinic, vaccination, sexual assault prevention, suicide prevention "
          "and counselling. Nothing on this appears in the archive before 1989.",
  "shift": "It entered the record as a single resolution asking for education about a "
           "disease, and as a defence of the campus clinic. From 2016 it became structural: "
           "a standing committee, then a constitutionally defined one, then a required "
           "termly meeting with the counselling director and the Title IX coordinator, then "
           "a full-year programme with its own campus data.",
  "inst": [
   ("1989", "1989-90#e-19890101-1",
    "Resolution 89-3-F had ASG write to administrators asking for education on AIDS, HIV "
    "and sexually transmitted diseases."),
   ("1991", "1991-92#e-19911212-1",
    "The Residence Hall Association and ASG sent a joint mailing asking parents to support "
    "the campus health service."),
   ("2015", "2015-16#e-20151119-1",
    "Resolution 6-15-F unanimously supported a meningitis vaccination requirement for "
    "incoming freshmen in campus housing."),
   ("2016", "2015-16#e-20160302-1",
    "Ransdell declined it, citing a $143.77 cost for uninsured students, and said WKU would "
    "stop short of requiring it."),
   ("2016", "2016-17#e-20161012-2",
    "The senate created SAVES, on sexual assault prevention, suicide prevention and "
    "expanded mental health resources."),
   ("2017", "2017-18#e-20170927-1",
    "A resolution supporting a one-credit sexual assault education course in the Colonnade "
    "passed 29-1."),
   ("2022", "2021-22#e-20220323-1",
    "Bill 22-22-S amended the constitution to redefine the Student Mental Health and "
    "Wellbeing Committee&#8217;s duties."),
   ("2023", "2022-23#e-20230215-2",
    "Resolution 2-23-S unanimously supported putting Narcan in the residence halls."),
   ("2025", "2024-25#e-20250326-1",
    "Resolution 4-25-S supported a Mental Health and Suicide Prevention Advisory Board to "
    "advise senior administrators."),
   ("2026", "2025-26#e-20260418-1",
    "A year-long push closed with an Out of the Darkness walk, built on a WKU "
    "professor&#8217;s finding that 44 per cent of students reported symptoms of "
    "depression."),
  ]},
 {"id": "green", "name": "Sustainability, recycling and the campus environment",
  "span": "1973&#8211;2024",
  "what": "Paper drives, bins and cleanups, then committees, food and a dedicated fee. The "
          "thread has one documented hole of nearly twenty years.",
  "shift": "A scrappy volunteer effort in the 1970s, which a <cite>Herald</cite> reporter "
           "found had come to nothing by 1974. It returned in the early 1990s as budgeted "
           "money and bins, and from 2015 became institutional: a committee created by "
           "executive proposal, made permanent by constitutional amendment, and by 2024 "
           "proposing a fee on students to fund the university office whose food pantry SGA "
           "was already restocking.",
  "inst": [
   ("1973", "1972-73#e-19730116-1",
    "A city recycling ordinance left ASG holding the bag on trash collection for its own "
    "paper-recycling programme."),
   ("1974", "1974-75#e-19741015-1",
    "A <cite>Herald</cite> reporter found ASG&#8217;s ecology projects were non-existent, in "
    "the same issue as protesters urging the organization be revamped."),
   ("1991", "1991-92#e-19910924-1",
    "A recycling resolution had its first reading in the same week officers went to a city "
    "meeting over the noise ordinance."),
   ("1993", "1992-93#e-19930413-1",
    "The last meeting of the year took up Adopt-a-Spot and Earth Day alongside the budget "
    "and the elections."),
   ("2015", "2015-16#e-20150910-1",
    "An executive proposal creating a sustainability committee passed unanimously."),
   ("2016", "2015-16#e-20160427-1",
    "Resolution 3-16-S supported recycling in the Downing Student Union, Garrett and Tower "
    "food courts."),
   ("2016", "2016-17#e-20161116-1",
    "The Sustainability committee was written into the constitution as a permanent standing "
    "committee."),
   ("2021", "2020-21#e-20210303-1",
    "Senators unanimously funded a community garden outside the Office of Sustainability."),
   ("2022", "2021-22#e-20220118-2",
    "$1,000 to restock the Office of Sustainability food pantry, drained by tornado "
    "recovery."),
   ("2024", "2023-24#e-20240222-1",
    "Resolution 26-23-S put SGA behind a $5-a-semester sustainability fee, with the proceeds "
    "going to the Office of Sustainability."),
  ]},
 {"id": "dining", "name": "Dining, food service and food insecurity",
  "span": "1990&#8211;2026",
  "what": "Hours, menus, contracts and, recently, whether students can afford to eat.",
  "shift": "For twenty years the subject was convenience: microwaves, food court hours, "
           "notice of closures, 24-hour dining, vegetarian options. In 2018 the object "
           "changed from the food to the contract. From 2022 the frame was hunger: donated "
           "meal swipes, a food insecurity clause in course syllabi, and a pantry bill "
           "amended upward when federal food assistance was cut.",
  "inst": [
   ("1990", "1990-91#e-19900901-2",
    "Bill #90-4-F requested microwaves in the campus cafeterias."),
   ("1997", "1997-98#e-19971022-1",
    "Outgoing correspondence to the administration covered food court hours alongside ice "
    "machines and campus safety."),
   ("2003", "2003-04#e-20031023-1",
    "SGA unanimously called on Dining Services to advertise changes to service hours or "
    "facilities at least two weeks in advance."),
   ("2013", "2013-14#e-20130912-2",
    "A resident assistant gathered more than 700 signatures in about a week for a 24-hour "
    "dining option and brought the petition to SGA."),
   ("2016", "2015-16#e-20160427-1",
    "Resolution 5-16-S supported vegetarian options on the Downing Student Union meal plan."),
   ("2018", "2017-18#e-20180228-1",
    "A unanimous resolution sought renegotiation of the 20-year Aramark contract, under "
    "which the fee for full-time students without a meal plan would climb from $75 to $350 "
    "a semester."),
   ("2021", "2021-22#e-20210929-1",
    "Long queues in the Downing Student Union were raised with the senate, attributed partly "
    "to a shortage of staff."),
   ("2022", "2021-22#e-20220217-1",
    "A meal-swipe donation programme let students give up unused swipes, with the WKU "
    "Restaurant Group matching one for every four."),
   ("2025", "2025-26#e-20251104-1",
    "A food pantry bill introduced at $123 was amended up to $750 after cuts to federal food "
    "assistance."),
   ("2026", "2025-26#e-20260210-1",
    "Restaurant Group representatives answered senators on Steak &#8217;n Shake seasoning, "
    "Subway kiosks and the meal-swipe menu."),
  ]},
 {"id": "teaching", "name": "Evaluating the teaching",
  "span": "1969&#8211;2021",
  "what": "Student evaluation of faculty, courses, teaching assistants and advisors. "
          "Repeatedly won, repeatedly lost, repeatedly restarted.",
  "shift": "Every generation fought the same two-stage battle: get the evaluation done, "
           "then get the results published. The first attempt was in 1969. A mandatory "
           "published evaluation was won on paper in 2000, scaled back to five questions on "
           "TopNet by 2004, extended to teaching assistants in 2013 and to academic advisors "
           "in 2021.",
  "inst": [
   ("1969", "1969-70#e-19691107-1",
    "An ASG committee compiled the results of Western&#8217;s first student "
    "teacher-evaluation effort, after the paper had editorialised demanding the tabulation "
    "move faster."),
   ("1972", "1972-73#e-19720829-2",
    "The <cite>Herald</cite> judged ASG&#8217;s course evaluation the best yet, as filing "
    "opened for autumn offices."),
   ("1987", "1987-88#e-19871029-1",
    "ASG took up a proposal to make course evaluations a requirement."),
   ("1989", "1988-89#e-19890216-1",
    "January efforts to find a way to print the teacher evaluations preceded a "
    "recommendation for an extra study day before exams."),
   ("2000", "1999-00#e-20000404-1",
    "Resolution 00-2-S asked the Faculty Senate to approve a mandatory, published "
    "SGA-sponsored evaluation from that autumn."),
   ("2004", "2004-05#e-20041116-1",
    "A two-year pilot scaled the plan back to five questions added to faculty evaluations "
    "and posted on TopNet."),
   ("2013", "2012-13#e-20130409-2",
    "A Board of Regents committee unanimously approved SGA&#8217;s teaching assistant "
    "evaluation policy."),
   ("2021", "2021-22#e-20211006-1",
    "Resolution 1.21f, on the lack of any advisor evaluation system, passed 21-2 as the "
    "first resolution of the 21st Senate."),
  ]},
 {"id": "voting", "name": "Voter registration and getting students to the polls",
  "span": "1991&#8211;2026",
  "what": "SGA turning outward to state and national elections, as opposed to worrying "
          "about its own.",
  "shift": "It began in 1991 as a registration drive the organization restarted. In the 2000s "
           "it became a resolution, with the "
           "bylaws suspended so it could pass before polling day. By 2018 it was a demand on "
           "the university to cancel classes, and by the 2020s the ask was infrastructural: "
           "a trolley to the polling place, then a polling place on campus.",
  "inst": [
   ("1991", "1991-92#e-19910924-1",
    "The organization restarted its voter registration drive."),
   ("1992", "1992-93#e-19920825-1",
    "The first meeting of the autumn took up a new logo, discount cards and a voter "
    "registration drive."),
   ("1996", "1996-97#e-19960924-1",
    "A voter registration drive sat on a September agenda alongside Provide-A-Ride, roller "
    "blading rules and the budget."),
   ("2003", "2003-04#e-20031030-1",
    "The senate suspended its bylaws to pass a resolution urging students to vote on 4 "
    "November and to research candidates&#8217; stands on higher education."),
   ("2007", "2007-08#e-20071002-1",
    "A mock gubernatorial election co-sponsored with the Secretary of State&#8217;s office "
    "drew 127 student voters."),
   ("2018", "2018-19#e-20180920-2",
    "Resolution 5-18-F asked WKU to cancel classes for the midterm elections and gave $300 "
    "to a registration campaign."),
   ("2023", "2023-24#e-20231101-1",
    "Caboni told the senate WKU would use the Historic RailPark&#8217;s trolley to carry "
    "students to the State Street polling places on a class day."),
   ("2024", "2024-25#e-20240910-1",
    "The vice president told the senate he was working to get a polling centre on campus, "
    "because otherwise he had to drive about three hours home to vote."),
   ("2026", "2026-27",
    "The chair of the Hilltoppers Vote Coalition was elected student body president."),
  ]},
 {"id": "race", "name": "Race, representation and who gets a seat",
  "span": "1972&#8211;2025",
  "what": "Who is in the room, whose name is on the building, and whether the organization "
          "speaks for anyone outside itself.",
  "shift": "It started as individual fights the record holds mostly as headlines. WKU&#8217;s "
           "student seat integrated the Board of Regents in 1974, seven years before the "
           "first Black gubernatorial appointee. From the mid-1990s the mechanism shifted to "
           "policy, and from 2013 to guaranteed seats. The 2016-17 peak drew national "
           "coverage and a flat rejection; the 2025 amendment ran the other way, renaming "
           "the diversity committee under a federal executive order.",
  "inst": [
   ("1972", "1972-73#e-19720929-1",
    "ASG rejected President Dero Downing&#8217;s position on an Office of Black Affairs, one "
    "of the sharpest confrontations of the autumn."),
   ("1974", "1973-74#e-19740619-1",
    "Gregory McKinney was sworn in as WKU&#8217;s first African American student regent, "
    "seven years before the first Black gubernatorial appointee joined the board."),
   ("1977", "1976-77#e-19770225-1",
    "Fourteen members abstained as ASG rejected a resolution on discrimination."),
   ("1979", "1978-79#e-19790215-1",
    "ASG established a Minorities Board, following the previous autumn&#8217;s push to add "
    "minority voices to the presidential screening panel."),
   ("1997", "1996-97#e-19970417-1",
    "SGA passed a measure calling for gay students to be included in Western&#8217;s "
    "anti-discrimination policy, by a slim margin."),
   ("2011", "2010-11#e-20110211-1",
    "The <cite>Herald</cite> reported 21 of SGA&#8217;s 50 members belonged to Greek "
    "organizations, more than 40 per cent, against less than 8 per cent of the student "
    "body."),
   ("2012", "2011-12#e-20120502-1",
    "A transgender and gender-nonconforming support resolution passed 18-5 at the last "
    "meeting of the year, watched by students who were not SGA members."),
   ("2013", "2013-14#e-20130919-2",
    "A referendum created a Navitas/ESL international student senate seat, passing with 310 "
    "of 426 votes."),
   ("2017", "2016-17#e-20170421-1",
    "Resolution 6-17-S, supporting reparations for Black students, passed 19-10-1 and drew "
    "national coverage. Ransdell stated within days that it was not a university position."),
   ("2019", "2019-20#e-20191030-2",
    "A resolution seeking discipline against a sorority over a video of members singing a "
    "racial slur passed 24-7 and was vetoed 4-0."),
   ("2021", "2021-22#e-20210806-1",
    "Northeast Hall was renamed for Margaret Munday, WKU&#8217;s first African American "
    "student to enrol, at the meeting where the student regent was sworn in."),
   ("2024", "2023-24#e-20240329-1",
    "The student group For the People told the senate that 40 per cent of it belonged to "
    "Greek life and that SGA had a disconnect with cultural communities."),
   ("2025", "2024-25#e-20250404-2",
    "Bill 21-25-S renamed the Diversity, Equity and Inclusion Committee the Action and "
    "Opportunity Committee, after a federal executive order. Students ratified it with 88 "
    "per cent."),
  ]},
]

VERDICTS = [
 {"id": "v-deserve", "name": "&#8220;We do not deserve student government&#8221;",
  "span": "1966&#8211;1987",
  "what": "The <cite>Herald</cite> doubted the organization&#8217;s right to exist in the "
          "week it was created, and recycled the doubt as a standing editorial frame for "
          "twenty years.",
  "shift": "Framed at first as a judgement on the student body &#8212; <em>we</em> do not "
           "deserve it &#8212; and recast by the mid-1970s as a judgement on the "
           "organization. By 1987 the word in the letters column was simply impotent.",
  "inst": [
   ("1966", "1966-67",
    "The issue reporting Jim Haynes&#8217;s election as first president carried an editorial "
    "headed &#8220;We Do Not Deserve Student Government.&#8221;"),
   ("1966", "1966-67#e-19661027-1",
    "Midway through the first autumn the paper judged leaders were performing well but "
    "failing to communicate with the students they represented."),
   ("1967", "1966-67#e-19670512-1",
    "Reviewing the first year, the paper settled on three words: organization, progress and "
    "apathy."),
   ("1968", "1967-68#e-19680429-3",
    "As Menser&#8217;s term ended the paper ran &#8220;Past Performance of Associated "
    "Student Government Analyzed.&#8221; The archive holds the headline, not the text."),
   ("1972", "1971-72#e-19720225-1",
    "&#8220;Chaos Reigns at Associated Students Meeting,&#8221; alongside a piece arguing "
    "student interest had collapsed and the organization had followed it down."),
   ("1976", "1975-76#e-19760326-1",
    "An editorial held ASG&#8217;s troubles up as a cautionary example for the "
    "university&#8217;s newly forming Faculty Senate."),
   ("1987", "1986-87#e-19870414-1",
    "On election day the paper endorsed the challenger, printed a letter calling the "
    "organization impotent and indexed the race itself as no contest."),
  ]},
 {"id": "v-apathy", "name": "Apathy, named and renamed each decade",
  "span": "1967&#8211;2014",
  "what": "The single most persistent charge. Apathy was diagnosed in editorials, drawn in "
          "cartoons, made into a candidate&#8217;s platform and eventually turned into an "
          "SGA-branded week.",
  "shift": "The paper scolded non-voters into the late 1970s, then began explaining them: "
           "the 1979 primary issue carried a defence of not voting. SGA answered by "
           "adopting the word itself. After 2003 apathy was discussed as a turnout statistic "
           "rather than a moral failing.",
  "inst": [
   ("1967", "1966-67#e-19670518-1",
    "&#8220;Goof Government Needs Student Vote&#8221; ran as Menser&#8217;s administration "
    "took over."),
   ("1968", "1967-68#e-19680509-1",
    "The issue reporting Bill Straeffer&#8217;s win carried &#8220;Elections Illustrate "
    "Faults, Indifference.&#8221;"),
   ("1979", "1979-80#e-19790412-1",
    "830 students voted in the spring primary and the same issue carried a defence of "
    "student apathy in ASG voting."),
   ("1985", "1984-85#e-19850214-1",
    "&#8220;Voter Apathy Can be Solved&#8221; ran with a cartoon on election apathy."),
   ("1987", "1987-88#e-19871029-2",
    "The paper argued apathy was killing both ASG and the Residence Hall Association."),
   ("1990", "1989-90#e-19900222-1",
    "Anti-Apathy Week drew enough criticism that president Amos Gott published a defence of "
    "it a week later."),
   ("1994", "1993-94#e-19940208-1",
    "&#8220;Let&#8217;s Work Together for Change,&#8221; with a People Poll asking how SGA "
    "could reach more students."),
   ("2004", "2003-04#e-20040316-1",
    "An editorial faulted students after 132 of about 18,000 voted on the new constitution, "
    "contrasting it with 86 per cent turnout in South Africa&#8217;s 1999 election."),
   ("2014", "2013-14#e-20140415-1",
    "Reporting turnout of 908, an editorial called turnout below 1,000 pathetic and said the "
    "student body could do better."),
  ]},
 {"id": "v-cartoons", "name": "The cartoons: drawing the presidents",
  "span": "1980&#8211;1999",
  "what": "For two decades the paper&#8217;s sharpest commentary on student government was "
          "pictorial, and several cartoons took a named sitting president as their subject.",
  "shift": "The cartoons began with policy mockery, moved by the end of the 1980s to "
           "caricaturing the president himself, and ended in images of emptiness: student "
           "government in an empty room, then in a glass box. No editorial cartoon about SGA "
           "appears anywhere in this archive after 1999.",
  "inst": [
   ("1980", "1980-81#e-19800911-1",
    "A bill against bugs in the dormitories drew a cartoon of an imperilled cockroach."),
   ("1983", "1983-84#e-19831013-1",
    "A Lou Bloss cartoon on an ASG penalty ran in the same issue as the request for cable "
    "television."),
   ("1984", "1984-85#e-19841108-1",
    "LaMont Jones withdrew from a revote and the same issue carried an editorial cartoon on "
    "the organization."),
   ("1985", "1984-85#e-19850411-1",
    "The end of Jack Smith&#8217;s presidency was marked with a news story, an editorial "
    "crediting his enthusiasm, and a cartoon."),
   ("1989", "1988-89#e-19890202-1",
    "John Chattin drew Scott Whitehouse as a salesman, alongside &#8220;Scott Whitehouse "
    "Selling Good Government.&#8221;"),
   ("1990", "1989-90#e-19900412-1",
    "A report that interest in the organization might be lower was illustrated with a "
    "cartoon of student government in an empty room."),
   ("1992", "1991-92#e-19920130-2",
    "Patrick Richardson&#8217;s &#8220;Ventriloquist&#8217;s Dummy&#8221; took president "
    "Heather Falmlen as its subject."),
   ("1992", "1992-93#e-19920414-1",
    "On election day the same cartoonist drew Joe Rains as Darth Vader."),
   ("1995", "1994-95#e-19950425-1",
    "A Stacy Curtis cartoon put student government in a glass box, paired with an editorial "
    "on visibility."),
   ("1999", "1998-99#e-19990420-1",
    "A cartoon on nasty campaigns ran with the report that the Judicial Council had "
    "overturned the spring election."),
  ]},
 {"id": "v-reply", "name": "Presidents answering back in print",
  "span": "1972&#8211;2001",
  "what": "A distinct sub-genre: the sitting or outgoing president using the "
          "<cite>Herald</cite>&#8217;s own pages to correct, dispute or defend against its "
          "coverage. One of the few places the archive preserves an officer&#8217;s voice.",
  "shift": "Early replies corrected facts. By the 1980s they complained about tone and about "
           "cartoons. By the late 1990s the reply had become documentary &#8212; circulating "
           "the legislative record as the rebuttal &#8212; and the last one the archive "
           "holds, in 2001, was self-criticism rather than defence.",
  "inst": [
   ("1972", "1971-72",
    "President Linda Jones published a piece headed &#8220;Associated Students Corrects "
    "Herald.&#8221; The archive holds the headline, not the text."),
   ("1977", "1977-78#e-19771027-1",
    "After the editorial answering his questions about freshman campaign spending, Bob Moore "
    "wrote back disputing it."),
   ("1983", "1983-84#e-19831206-1",
    "ASG voided its own procedures, the editorial page mocked it, and president Jack Smith "
    "wrote in under the heading &#8220;Cartoon Aggravates.&#8221;"),
   ("1985", "1984-85#e-19850405-1",
    "A reader&#8217;s letter took issue with a <cite>Herald</cite> editorial about ASG in "
    "the middle of the campaign season."),
   ("1990", "1989-90#e-19900222-1",
    "Amos Gott published a defence of Anti-Apathy Week in the same issue as ASG&#8217;s "
    "demand that the Pearce-Ford Tower windows be opened."),
   ("1998", "1998-99#e-19981210-1",
    "Vice president Matthew Bastin circulated the autumn&#8217;s passed legislation to the "
    "adviser, the officers and the <cite>Herald</cite>&#8217;s editor. The list was the "
    "rebuttal."),
   ("2001", "2001-02#e-20011129-2",
    "President Leslie Bedo&#8217;s own opinion piece on meeting SGA&#8217;s goals but not "
    "students&#8217; was answered in the same issue by a member of her own organization."),
  ]},
 {"id": "v-admin", "name": "Administrators speaking to and about it",
  "span": "1966&#8211;2025",
  "what": "University presidents, deans, provosts and general counsel appearing before the "
          "body, answering it, overruling it or being rejected by it. After the "
          "<cite>Herald</cite>, the most continuous relationship in the archive.",
  "shift": "In the first years the administration created and funded the body: Thompson "
           "approved the constitution, the Dean of Students designed its budget. From the "
           "1980s presidents came to meetings to ask SGA for something. From 2006 the "
           "pattern was a formal written answer to SGA legislation. By 2025 the "
           "administration was telling SGA what state law forbade it to fund.",
  "inst": [
   ("1966", "1966-67#e-19661110-1",
    "Student government leaders met President Kelly Thompson to discuss campus problems."),
   ("1967", "1966-67#e-19670530-1",
    "Dean of Students Charles Keown sent Thompson a memo proposing a student fee structure "
    "to create a budget for the new government, attaching fee models from universities "
    "across the South and Midwest."),
   ("1983", "1982-83#e-19830317-1",
    "Dean Keown publicly questioned ASG&#8217;s constitutional revisions the week after they "
    "were approved."),
   ("1992", "1992-93#e-19921013-2",
    "President Thomas Meredith came to the October meeting to talk about computers, laundry, "
    "cable television, lighting and Potter Hall."),
   ("2006", "2005-06#e-20060201-1",
    "President Gary Ransdell urged senators to back the proposed construction fee before the "
    "regents voted on it."),
   ("2011", "2011-12#e-20111005-1",
    "In his first visit of the semester Ransdell told senators that ending the two-year "
    "housing requirement did not work from a business standpoint."),
   ("2015", "2014-15#e-20150304-2",
    "Ransdell emailed faculty and staff his official response to four SGA resolutions at "
    "once."),
   ("2020", "2020-21#e-20201118-2",
    "Associate Provost Rob Hale rebuffed SGA&#8217;s Pass/D/Fail request; the president said "
    "he was deeply disturbed."),
   ("2025", "2025-26#e-20251001-1",
    "General Counsel Andrea Anderson told the senate that House Bill 4 binds SGA&#8217;s "
    "spending because SGA receives university money."),
  ]},
 {"id": "v-floor", "name": "Students confronting it from the floor",
  "span": "1974&#8211;2025",
  "what": "Non-members, and sometimes their own constituents, coming to meetings and forums "
          "to tell the organization it had failed them.",
  "shift": "Almost absent before 2000. From 2012 it became routine, and after the editorial "
           "cartoons stopped it was the archive&#8217;s main channel for criticism: petitions, "
           "testimony about disability and racism, and organised groups reading SGA its own "
           "demographics.",
  "inst": [
   ("1974", "1974-75#e-19741015-1",
    "Protesters urged a revamping of the Associated Student Government, in the same issue "
    "that reported its ecology projects were non-existent."),
   ("2013", "2013-14#e-20130912-2",
    "A resident assistant brought SGA a petition of more than 700 signatures for 24-hour "
    "dining."),
   ("2016", "2016-17#e-20160907-1",
    "A sophomore told senators his ADHD and dyslexia had cost him merit scholarships. The "
    "bill creating disability scholarships passed unanimously."),
   ("2018", "2017-18#e-20180404-1",
    "LGBTQ activists addressed the senate after a senator read Bible verses to explain his "
    "vote against funding Lavender Graduation stoles."),
   ("2023", "2022-23#e-20230222-2",
    "The Queer Student Union told the senate it had removed SGA meetings from its list of "
    "campus safe spaces."),
   ("2024", "2023-24#e-20240329-1",
    "The advocacy group For the People told the senate SGA was the only major organization "
    "not to oppose a Kyle Rittenhouse campus visit, and called the executive board&#8217;s "
    "response unacceptable."),
   ("2025", "2024-25#e-20250225-1",
    "A wheelchair user and honorary SGA member drove the resolution for an elevator in "
    "Gordon Wilson Hall after being scheduled for a third-floor class in a 1927 building."),
  ]},
 {"id": "v-exit", "name": "Walking out: resignation and withdrawal",
  "span": "1973&#8211;2023",
  "what": "The strongest criticism short of a lawsuit: resigning, breaking affiliation, or "
          "formally refusing to associate with the organization.",
  "shift": "Early withdrawals were institutional and reversible &#8212; a delegation left a "
           "statewide legislature and rejoined. From 2009 they were personal and reputational: "
           "senators and justices resigning over appointments, complaints and ridicule, and "
           "in 2023 an outside organization publicly withdrawing recognition of SGA as a safe "
           "space.",
  "inst": [
   ("1973", "1973-74#e-19731204-1",
    "ASG representative Reginald Glass resigned his post in protest, an early sign of strain "
    "inside the congress."),
   ("1987", "1987-88#e-19870910-1",
    "ASG considered dropping its membership in the intercollegiate legislature."),
   ("2009", "2009-10#e-20091020-1",
    "Three senators resigned over the president&#8217;s nomination to the Student "
    "Publications Committee, one saying the pick was not based on merit or experience."),
   ("2015", "2015-16#e-20151203-3",
    "Chief Justice Kelsey Luttrell resigned, saying the Judicial Council had been publicly "
    "ridiculed and lacked support from fellow members."),
   ("2016", "2016-17#e-20161012-1",
    "A senator and a justice resigned the morning after a complaint of racist remarks by SGA "
    "members was aired; the planned investigation was dropped because they had already "
    "left."),
   ("2017", "2016-17#e-20170222-1",
    "Senator Chase Coffey resigned the same night the Executive Council vetoed his "
    "unanimously passed resolution."),
   ("2020", "2020-21#e-20200923-1",
    "The Speaker of the Senate resigned and quit the executive vice president race after a "
    "video showing him using a racial slur was sent anonymously to the paper."),
   ("2023", "2022-23#e-20230222-2",
    "The Queer Student Union said it would not associate with SGA until a public apology was "
    "released."),
  ]},
 {"id": "v-greek", "name": "Greek dominance, the standing charge",
  "span": "1974&#8211;2024",
  "what": "That fraternities and sororities control the organization out of all proportion "
          "to their numbers. Unusually, the archive supplies the arithmetic.",
  "shift": "Reported as an observation about elections in the 1970s, quantified in 2011 at "
           "more than 40 per cent of the membership against under 8 per cent of the student "
           "body, legislated against and defeated by one vote in 2018, and thrown back at "
           "SGA by outside students in 2024 with the same figure.",
  "inst": [
   ("1974", "1973-74#e-19740329-1",
    "Jeff Consolo and Steve Henry won the spring election in a cycle whose primary the paper "
    "said showed Greek influence."),
   ("2011", "2010-11#e-20110211-1",
    "21 of SGA&#8217;s 50 members belonged to Greek organizations, with two fraternities "
    "accounting for nine of them."),
   ("2011", "2010-11#e-20110401-1",
    "The administrative vice president, who chaired the organizational aid committee, said "
    "he would be succeeded by his committee co-chair and fraternity brother, who ran "
    "unopposed."),
   ("2018", "2017-18#e-20180124-1",
    "A senator objected that nominating another fraternity man was hypocritical given the "
    "executive board&#8217;s stated concern about Greek over-representation."),
   ("2018", "2018-19#e-20181017-1",
    "Bill 10-18-F, barring SGA funding to Interfraternity and Panhellenic chapters, failed "
    "16-17. Its author, herself in a sorority, cited the University of Alabama."),
   ("2019", "2019-20#e-20191002-1",
    "The senate voted 17-15 to cancel a meeting for a sorority philanthropy event; two "
    "senators organised a protest at the event instead."),
   ("2024", "2023-24#e-20240329-1",
    "For the People told the senate 40 per cent of it belonged to Greek life. Kurtz replied "
    "that he did not control who chose to run."),
  ]},
 {"id": "v-money", "name": "Money as the sharpest charge",
  "span": "1975&#8211;2024",
  "what": "Financial trouble produces the harshest language in the archive, from the paper "
          "and from SGA&#8217;s own members. The 1970s, 1980s, 2000s, 2010s and 2020s each "
          "carry at least one episode.",
  "shift": "In the 1970s the charges were heard and settled internally. Between 2002 and 2011 "
           "they were investigated by the paper and the university&#8217;s internal auditor, "
           "and ended careers. From 2013 the criticism turned to conflict of interest and "
           "procedure, and was brought by officers against each other.",
  "inst": [
   ("1975", "1975-76#e-19751024-1",
    "Charges of ASG fund misuse were heard the same week the congress voted to create an "
    "activities committee."),
   ("1983", "1983-84#e-19830908-1",
    "ASG offered its own members a commission on discount card sales, drawing columns headed "
    "&#8220;Cheap Shots&#8221; and &#8220;And Old Tricks.&#8221;"),
   ("2002", "2002-03#e-20020924-1",
    "The <cite>Herald</cite>&#8217;s eleven-member editorial board called leaders&#8217; "
    "ignorance about the missing gazebo money shameful."),
   ("2004", "2004-05#e-20040826-1",
    "WKU&#8217;s internal auditor found $872 in questionable purchases from an SGA dining "
    "account between August 2003 and May 2004, and recommended the money be repaid."),
   ("2004", "2004-05#e-20040826-4",
    "Former SGA officers wrote to the paper saying they were dismayed by the resigned "
    "president&#8217;s lack of integrity."),
   ("2006", "2005-06#e-20060420-2",
    "An editorial headed &#8220;SGA misspending&#8221; said members should not have to be "
    "motivated by a giveaway to show up for meetings."),
   ("2011", "2011-12#e-20111118-2",
    "A $15,000 retroactive bill for a predecessor&#8217;s contract took $7,500 each from "
    "organizational aid and scholarships. The president said he was shocked."),
   ("2013", "2012-13#e-20130301-3",
    "The president and three colleagues published a commentary attacking their own senate "
    "for refusing to bar serving members from SGA-sponsored scholarships."),
   ("2024", "2023-24#e-20240209-1",
    "The Judicial Council censured the administrative vice president 6-0 for spending funds "
    "before the senate authorised them."),
  ]},
 {"id": "v-praise", "name": "Praise, and who was willing to give it",
  "span": "1967&#8211;2025",
  "what": "The minority report. Praise in this archive comes overwhelmingly from three "
          "places: individual letter writers, the outgoing body commending itself, and the "
          "institution&#8217;s own formal resolutions. Rarely from the editorial page.",
  "shift": "In the early years praise was a letter defending the idea of student government "
           "at all. In the 1980s and 1990s it became institutional: commendation bills and "
           "resolutions from the Board of Regents and the University Senate. After 2000 "
           "editorial praise nearly vanished, replaced by SGA&#8217;s own ceremonies. Praise "
           "is also structurally under-recorded, because most of the pre-2003 record is a "
           "headline index and the paper headlined complaints more readily than approval.",
  "inst": [
   ("1967", "1967-68#e-19671208-3",
    "The issue carrying the ASG activity survey also ran a letter commending the "
    "government&#8217;s efforts."),
   ("1969", "1968-69",
    "The outgoing administration&#8217;s own account of its year ran under &#8220;Associated "
    "Students Produces Year of Advancement.&#8221;"),
   ("1985", "1984-85#e-19850411-2",
    "An editorial said Jack Smith&#8217;s enthusiasm had revived student interest in ASG."),
   ("1986", "1985-86#e-19860403-1",
    "The outgoing congress passed Bill 86-13-S commending president Mitchell McKinney; the "
    "Board of Regents honoured him that August."),
   ("1988", "1988-89#e-19881103-1",
    "A week after ASG filled half its open seats and sought shelters for the shuttle stops, "
    "an editorial said its efforts directly helped and served students."),
   ("2008", "2007-08#e-20080718-1",
    "A Board of Regents resolution thanked Jeanne Johnson for able leadership, faithful "
    "service and dedication as the board&#8217;s student member."),
   ("2022", "1993-94",
    "Donald Smith, president in 1993-94, told the paper that structures had changed but a "
    "voice for the students had remained."),
   ("2025", "2024-25#e-20250416-2",
    "At the 24th Senate&#8217;s final meeting the three executives each received a standing "
    "ovation."),
  ]},
]

# The turnout series, in sequence. (label, year id, count, note, jumped?)
TURNOUT = [
 ("1966", "1966-67#e-19660426-1", "2,538",
  "The four-day referendum that ratified the constitution, 1,812 to 726. A vote to create the "
  "organization rather than to staff it.",
  True),
 ("1968", "1968-69#e-19680502-1", "2,894",
  "About 34 per cent of a roughly 8,500-student enrolment, in the second contested "
  "presidential race, with contests all the way down the ballot.", True),
 ("1976", "1975-76#e-19760402-1", "527",
  "Ballots cast in the presidential primary. The 1970s yield no general-election total at "
  "all.", False),
 ("1978", "1978-79#e-19780928-2", "95",
  "Voters in the freshman primary the week before a freshman president was elected by eleven "
  "votes.", False),
 ("1979", "1979-80#e-19790412-1", "830",
  "The spring primary. The same issue carried a defence of not voting.", False),
 ("1983", "1982-83#e-19830210-1", "206",
  "Students voting for a campus shuttle service in February, in the same week ASG passed a "
  "grade plan.", False),
 ("1983", "1982-83#e-19830407-1", "500",
  "About five hundred in the ASG primary.", False),
 ("1984", "1983-84#e-19840320-1", "450",
  "About 450 in the primary the week before the top four ASG offices were decided without "
  "runoffs.", False),
 ("1992", "1991-92#e-19920407-2", "0",
  "The primary was cancelled outright for want of candidates. The same week the organization "
  "voted to rename itself.", False),
 ("1992", "1991-92#e-19920416-1", "1,200",
  "About 1,200 voted in the general election nine days later, which Joe Rains won by a wide "
  "margin.", False),
 ("1999", "1998-99#e-19990415-2", "1,436",
  "Amanda Coates led 616-611; a recount narrowed it to 614-611. Five days later the Judicial "
  "Council overturned the election.", False),
 ("2002", "2001-02#e-20020411-1", "1,878",
  "Jamie Sears beat Sam Stinson 1,284 to 594 in the first online voting the record "
  "describes.", False),
 ("2003", "2002-03#e-20030408-1", "2,014",
  "The presidency was uncontested, but a $3 radio-station fee was on the ballot &#8212; the "
  "first student referendum in SGA history.", True),
 ("2004", "2003-04#e-20040316-1", "132",
  "Students voting on the new constitution, out of about 18,000. It decided the "
  "organization&#8217;s shape for the next twenty years.",
  False),
 ("2004", "2003-04#e-20040318-1", "1,232",
  "The presidential election a fortnight later. The outgoing president said he was "
  "disappointed by the turnout.", False),
 ("2005", "2004-05#e-20050317-1", "1,740",
  "Katie Dawson beat Josh Collins 1,268 to 472 in the only contested race on the ballot.",
  False),
 ("2006", "2007-08#e-20080401-1", "1,376",
  "The spring election. The figure survives only in a story two years later that compared "
  "turnout against it.", False),
 ("2006", "2006-07#e-20061025-1", "2,136",
  "Ballots cast in the online referendum on the move to Division I-A football, run alongside "
  "the homecoming queen election. The 1,695 who answered the football question were about 9 "
  "per cent of enrolment.", True),
 ("2007", "2006-07#e-20070201-1", "688",
  "Votes for Jeanne Johnson in the special election for the vacant student regent seat, 41 "
  "per cent of the ballots cast.", False),
 ("2007", "2007-08#e-20080401-1", "1,424",
  "The spring election, recorded a year later in the story about the following "
  "spring&#8217;s turnout.", False),
 ("2008", "2008-09#e-20080918-1", "687",
  "The autumn senate election, which the president said ran above the average for an "
  "autumn.", False),
 ("2010", "2009-10#e-20100401-1", "1,150",
  "Colton Jessie took 726 to Justin Thurman&#8217;s 424.", False),
 ("2010", "2010-11#e-20100923-1", "847",
  "The autumn senate election, in which twelve senators were elected and 25 students ran for "
  "the at-large seats.", False),
 ("2011", "2010-11#e-20110407-1", "1,066",
  "Billy Stephens took 56 per cent. Both vice presidencies were uncontested, and all 35 "
  "senate candidates were elected to 36 seats, each needing a single vote to win.", False),
 ("2011", "2011-12#e-20110923-1", "977",
  "The autumn senate election, twenty candidates for eleven seats.", False),
 ("2013", "2013-14#e-20130919-2", "564",
  "The autumn senate election, which also carried the referendum creating an international "
  "student seat.", False),
 ("2014", "2013-14#e-20140415-1", "908",
  "Down 555 votes on the year before, in a year the sitting president had run unopposed and "
  "spent nothing. The editorial called it pathetic.", False),
 ("2014", "2014-15#e-20140925-1", "742",
  "The autumn senate election, which seated seventeen senators.", False),
 ("2015", "2015-16#e-20151112-1", "2,132",
  "Votes cast in the Dub the Pub naming ballot, which Topper Tavern won with 480 of them "
  "after the cabinet pulled a rival name.", False),
 ("2016", "2015-16#e-20160420-1", "2,442",
  "One of the highest turnouts in the association&#8217;s history, in Richey&#8217;s "
  "contested re-election, in the year of the Confucius Institute vote and the pub-name "
  "override.", True),
 ("2017", "2016-17#e-20170419-2", "1,579",
  "A three-way race: Dahmer 930, Mujkanovic 305, Nellans 212. All six referendums passed.",
  False),
 ("2018", "2017-18#e-20180418-1", "2,378",
  "A genuine three-way race decided 35-33-32 per cent, days after the Judicial Council had "
  "disqualified the winning ticket and then downgraded the penalty.", True),
 ("2021", "2022-23#e-20220921-2", "398",
  "The autumn senate election. The figure survives only because the following "
  "year&#8217;s story compared against it.", False),
 ("2022", "2021-22#e-20220420-1", "1,448",
  "Cole Bornefeld took 49 per cent. That autumn the fall election doubled, 805 against 398.",
  False),
 ("2023", "2022-23#e-20230419-2", "0",
  "The Kurtz ticket ran unopposed; no turnout figure survives. It ran unopposed again in "
  "2024.", False),
 ("2025", "2024-25#e-20250415-1", "966",
  "Rush Robinson elected unopposed. Kurtz had told the senate in February that his goal was "
  "3,000 voters.", False),
 ("2026", "2025-26#e-20260415-1", "1,601",
  "635 more than the year before, a rise of 66 per cent, in the first contested presidential "
  "race after three unopposed ones.", True),
]

FIGHTS = [
 {"id": "f-elections", "name": "Disputed elections and the court that decides them",
  "span": "1978&#8211;2022",
  "what": "The most reliable conflict in the record. A losing candidate, an anonymous "
          "complaint or a rules technicality throws the result to the Judicial Council, "
          "which then decides who governs.",
  "shift": "It began as an appeal heard by a body the paper said lacked objectivity, became "
           "a habit of voiding and re-running elections, and after 2004 matured into a formal "
           "power to disqualify winners outright. The 2013 case set the ceiling: the "
           "council disqualified a president-elect, a vice president for student affairs "
           "reinstated her, and the council concluded it had no power to contest him.",
  "inst": [
   ("1978", "1977-78#e-19780418-1",
    "Ed Johnson, having lost the presidency, contested the result; the Judicial Council "
    "denied his appeal after a long debate."),
   ("1982", "1982-83#e-19820420-1",
    "The general election results were voided, a decision the paper said disgusted the "
    "candidates, and the whole thing was run again."),
   ("1988", "1987-88#e-19880414-1",
    "Bruce Cambron called for a new election over write-in votes the congress was told it "
    "could not ignore. He was still pressing the university president in October."),
   ("1999", "1998-99#e-19990420-1",
    "The Judicial Council overturned the spring election outright, amid what one opinion "
    "piece called a swath of scandal."),
   ("2013", "2012-13#e-20130416-1",
    "The council voted 3-2 to disqualify president-elect Keyana Boka. She appealed to the "
    "vice president for student affairs, who reinstated her; the council then decided "
    "unanimously that it did not believe it could challenge his memorandum."),
   ("2015", "2015-16",
    "Anonymous accusations alleged the president-elect had breached the election code on "
    "poster placement. The council warned him and confirmed he had rightfully won."),
   ("2018", "2017-18#e-20180417-1",
    "Two days before results, the council disqualified an entire presidential ticket and a "
    "senate candidate over a Pepe the Frog image in campaign chalkings, then reduced it to a "
    "suspension."),
   ("2022", "2021-22#e-20220414-2",
    "An hour-long hearing cleared a candidate whose student-wide email about a hunger "
    "initiative was said to breach the ban on self-promotion."),
  ]},
 {"id": "f-code", "name": "The election code itself",
  "span": "1974&#8211;2023",
  "what": "Separate from disputed results: the recurring fight over the rules of campaigning "
          "&#8212; spending caps, campaign length, who may run, which seats go on which "
          "ballot.",
  "shift": "The 1970s and 1980s fought over one number, the spending cap. From 2000 the "
           "argument became explicitly about access: closing loopholes, whether a one-week "
           "campaign suppressed turnout, whether high caps priced out poorer candidates. The "
           "direction of travel reversed repeatedly, which is itself the finding. Caps went "
           "up in 2017 and were halved in 2019.",
  "inst": [
   ("1974", "1973-74#e-19740222-1",
    "ASG voted to retain its campaign spending limit rather than loosen the cap."),
   ("1978", "1977-78#e-19780309-1",
    "Spending limits set for the coming spring election."),
   ("1981", "1981-82#e-19810924-1",
    "ASG voted to increase its own campaign spending limit."),
   ("2008", "2007-08#e-20080401-1",
    "Candidates blamed the one-week campaign window for low turnout. President Jeanne "
    "Johnson said the codes were inherited and warned that too much publicity hurts."),
   ("2016", "2015-16#e-20160323-1",
    "The senate refused even to vote on codes drafted by the Judicial Council that would "
    "have halved senate campaign spending. The president called it too much red tape."),
   ("2017", "2016-17#e-20170215-1",
    "Revised codes raised the spending allowances again, one year after the senate declined "
    "to lower them."),
   ("2019", "2019-20#e-20190919-2",
    "The senate halved the maximums over the executive vice president&#8217;s objection that "
    "turnout was awful. A senator argued poorer students were less likely to be able to run."),
   ("2023", "2022-23#e-20230322-2",
    "Bill 39-23-S, which would have required a two-thirds vote before a vacant seat could "
    "become a presidential appointment, failed 19-15. Its sponsor called the reliance on "
    "appointments a dangerous practice for a government organization."),
  ]},
 {"id": "f-discipline", "name": "Impeachment, censure and removal",
  "span": "1976&#8211;2024",
  "what": "The formal disciplinary machinery, used against senators, justices, vice "
          "presidents and once against a sitting president. There is a near-total "
          "documentary gap between 1976 and 2004.",
  "shift": "The first documented case was an acquittal. For nearly thirty years afterwards "
           "the archive records no impeachment at all, and discipline appeared only as "
           "enforcement against absence. It returned in 2004 as articles that died on a "
           "technicality, and from 2009 became routine and bureaucratic, until a 2024 "
           "amendment made two censures in one year automatic grounds for removal.",
  "inst": [
   ("1976", "1975-76#e-19760409-1",
    "Congress member Gerard Faulk was acquitted at impeachment, in the same issue that "
    "reported the presidential election result."),
   ("1987", "1987-88#e-19871027-1",
    "ASG moved to get tough on absenteeism after a member lost his seat."),
   ("2004", "2004-05#e-20040420-1",
    "Articles of impeachment were drafted against the outgoing finance vice president after "
    "$611 was found missing. The council ruled the two-week process could not finish before "
    "he left the office anyway."),
   ("2009", "2009-10#e-20091110-1",
    "The Judicial Council removed a senator for excessive unexcused absences; he did not "
    "attend to defend himself."),
   ("2011", "2011-12#e-20111115-2",
    "Ten of 36 senators were called before the judicial board for absences. Two were "
    "dismissed for failing to attend their own hearings; one was reappointed by the "
    "president three months later."),
   ("2015", "2015-16#e-20151203-3",
    "The council voted unanimously not to censure a senator over an &#8220;impeach "
    "Ransdell&#8221; sign, finding his conduct protected by the First Amendment. The chief "
    "justice resigned days later."),
   ("2023", "2022-23#e-20230217-1",
    "The Speaker of the Senate requested a censure hearing against her own president. The "
    "council voted unanimously against censure; a Title IX report seeking his removal was "
    "filed two days later."),
   ("2024", "2024-25#e-20241106-1",
    "The council voted 7-0 to remove three senators, each with at least six unexcused "
    "absences, under the provision requiring removal after a second censure."),
  ]},
 {"id": "f-veto", "name": "Vetoes and overrides",
  "span": "1981&#8211;2019",
  "what": "The executive striking down what the senate has passed, and the senate&#8217;s "
          "usually failed attempt to strike back.",
  "shift": "Before 2004 the archive records vetoes only as isolated index lines. After the "
           "three-branch constitution the veto became a live weapon used against the "
           "senate&#8217;s most contested votes, and the override became the senate&#8217;s "
           "most reliable failure.",
  "inst": [
   ("1981", "1981-82#e-19811029-1",
    "ASG vetoed a plan to pay an education lobbyist, weeks after rallying publicly for "
    "higher education funding."),
   ("1991", "1990-91#e-19910101-2",
    "Bill #91-6-S rewrote the by-law on overriding a presidential veto; the new procedure "
    "was tested weeks later when the emergency-kit resolution survived a veto."),
   ("1996", "1996-97#e-19961010-1",
    "A resolution was vetoed in the same week SGA proposed more campus lighting. The archive "
    "does not name it."),
   ("2014", "2014-15#e-20141204-1",
    "Resolution 11-14-F, supporting a smoke-free campus, passed 14-10 and was vetoed after "
    "the meeting. The override failed at the last meeting of the semester."),
   ("2017", "2016-17#e-20170222-1",
    "A resolution that had passed the senate unanimously was vetoed as unconstitutional. Its "
    "author resigned the same night."),
   ("2019", "2019-20#e-20191030-2",
    "The executive board vetoed the Alpha Xi Delta resolution 4-0 with two abstentions, and "
    "the senate sustained the veto."),
  ]},
 {"id": "f-quorum", "name": "Quorum failures and empty seats",
  "span": "1975&#8211;2025",
  "what": "Meetings that could not be held, votes that failed for want of bodies, and "
          "senators removed or resigned for absence. The internal face of the apathy "
          "argument.",
  "shift": "Early instances were reported as one-off embarrassments in the "
           "<cite>Herald</cite>. From the 2000s SGA&#8217;s own minutes recorded quorum "
           "failures directly, and by the 2020s the Judicial Council had codified machinery "
           "for removing absentees.",
  "inst": [
   ("1975", "1974-75#e-19750228-1",
    "ASG action was halted twice in one week for lack of quorum. An editorial said the "
    "confusion signalled a need for change."),
   ("1987", "1986-87#e-19870409-1",
    "A constitutional amendment was defeated because too few members turned up to vote on "
    "it."),
   ("2006", "2006-07#e-20061205-1",
    "With 16 of 31 senators present the senate lacked quorum and tabled two resolutions."),
   ("2014", "2013-14#e-20140213-1",
    "An amendment that had passed was voided when the Executive Council found too few "
    "senators had attended for the vote to count."),
   ("2016", "2016-17#e-20160921-1",
    "The Speaker told the senate that eleven at-large seats should have been filled the "
    "previous spring but only ten were, leaving SGA a senator short all summer."),
   ("2019", "2018-19#e-20190130-1",
    "Nine senators were forced to step down at once, leaving the chamber depleted with no "
    "new legislation introduced."),
   ("2020", "2019-20#e-20200205-1",
    "Senators and committee chairs had quietly vacated their positions since the autumn; two "
    "committee chairs were empty."),
   ("2025", "2024-25#e-20250404-2",
    "The meeting to pass the DEI amendment initially lacked the 21 members needed for a "
    "two-thirds vote, so absent members were phoned onto Zoom to reach quorum."),
  ]},
 {"id": "f-cash", "name": "Money that cannot be accounted for",
  "span": "1975&#8211;2024",
  "what": "Lost concert money, missing funds, unspent budgets, retroactive bills, and the "
          "scholarships SGA awards to its own members.",
  "shift": "In the 1970s the problem was operational: SGA ran concerts and lost on them. "
           "From 2002 it became accountability failure &#8212; money that vanished into the "
           "general fund, purchases with no receipts, a surprise bill for a "
           "predecessor&#8217;s contract. By the 2010s the fight was over whether SGA members "
           "might take SGA&#8217;s own scholarship money.",
  "inst": [
   ("1975", "1975-76#e-19750919-1",
    "A September concert drew 4,300 people and lost $7,000."),
   ("1976", "1976-77#e-19761109-1",
    "The Seals and Crofts concert set the organization back $3,800."),
   ("2002", "2002-03#e-20020919-1",
    "Three members petitioned congress over $28,000 they said was unaccounted for. President "
    "Jamie Sears said she had absolutely no idea where the money went."),
   ("2002", "2002-03#e-20021001-1",
    "By October the $13,000 had been traced: it had slipped back into the general fund and "
    "been spent on other things, including computers for the SGA office."),
   ("2006", "2006-07#e-20061024-1",
    "About $24,000 of a $115,000 budget went unspent and returned to the university&#8217;s "
    "general fund."),
   ("2013", "2012-13#e-20130301-2",
    "The senate stripped out the bylaw that would have barred serving SGA members from "
    "SGA-sponsored scholarships."),
   ("2015", "2014-15#e-20150423-1",
    "A former senator published a letter arguing a precedent set that session had damaged "
    "the organizational aid process."),
   ("2024", "2023-24#e-20240209-1",
    "A 6-0 censure of the administrative vice president for spending a $425.25 deposit "
    "before the funding bill passed."),
  ]},
 {"id": "f-regents", "name": "Fighting the Board of Regents",
  "span": "1991&#8211;2026",
  "what": "Direct confrontation with WKU&#8217;s governing board, over its chairman, its "
          "contracts, its fees and its process. The place where SGA&#8217;s formal "
          "representation and its actual power are furthest apart.",
  "shift": "The pattern was stable: SGA passed a resolution and the board did what it was "
           "going to do. What changed was the student regent&#8217;s posture &#8212; from "
           "voting yes under protest, through abstention, to open letters of dissent and "
           "lone recorded no votes. The dissent got louder as it stayed equally ineffective.",
  "inst": [
   ("1991", "1991-92#e-19911029-1",
    "Resolution 91-6-F asked that Joe Iracane not be re-elected chair, citing federal "
    "investigations. The board re-elected him a week later."),
   ("2000", "2000-01#e-20001027-1",
    "The board raised the athletics fee 8-2. Student regent Cassie Martin was one of two "
    "dissenters."),
   ("2006", "2005-06#e-20060408-1",
    "The construction fee passed 9-1 with the student regent abstaining; her proposal to "
    "exempt the next year&#8217;s seniors was rejected 10-1."),
   ("2015", "2015-16#e-20150922-1",
    "The senate voted 21-4 to disapprove of the procedure by which the Confucius Institute "
    "building was authorised. The board declined to revisit it."),
   ("2016", "2016-17#e-20160819-1",
    "The student regent published an open letter to students explaining his vote against a "
    "medical centre partnership approved 6-4-1."),
   ("2018", "2017-18#e-20180228-1",
    "A unanimous resolution sought renegotiation of a 20-year dining contract the president "
    "said had never come to SGA or to the full board."),
   ("2024", "2024-25#e-20240808-1",
    "At the regents&#8217; retreat the student regent challenged administrators over student "
    "worker funding and afterwards called the answers cookie-cutter."),
   ("2026", "2025-26#e-20260605-1",
    "The student regent cast the only vote against a $204 tuition increase at his last "
    "meeting."),
  ]},
 {"id": "f-override", "name": "The administration overrules the students",
  "span": "1972&#8211;2025",
  "what": "SGA passes something, the administration declines it, and the organization "
          "discovers the limit of a resolution. Including the rare inverse: the campaigns "
          "that worked.",
  "shift": "Early confrontations were about campus life and rights. From the 2000s they "
           "became academic and contractual, and the pattern hardened into a formula: SGA "
           "passed a resolution, an administrator answered by email or letter, and the answer "
           "was no. The wins came when SGA supplied a number an administrator could act on, not "
           "when it passed a resolution.",
  "inst": [
   ("1972", "1972-73#e-19720929-1",
    "ASG rejected the university president&#8217;s position on an Office of Black Affairs."),
   ("2003", "2003-04#e-20031120-1",
    "The petition against plus/minus grading passed 1,500 signatures. Four years later the "
    "provost declined to implement the system."),
   ("2011", "2011-12#e-20111109-2",
    "The senate voted 19-8 against renaming Downing University Center. The Administrative "
    "Council decided it would be called Downing Student Union anyway."),
   ("2016", "2015-16#e-20160128-2",
    "Administrators changed the pub name students had chosen. The president said it made SGA "
    "question how much the administration listens to students."),
   ("2016", "2015-16#e-20160302-1",
    "Ransdell declined the meningitis vaccination requirement the senate had passed "
    "unanimously."),
   ("2017", "2016-17#e-20170223-1",
    "Housing and Residence Life&#8217;s ten-year plan made no mention of the integration SGA "
    "had endorsed 27-1."),
   ("2020", "2020-21#e-20201202-2",
    "After a petition of more than 3,500 signatures in three days and a 40-9 Faculty Senate "
    "vote, the provost reversed the university&#8217;s position on Pass/D/Fail. It is the "
    "clearest win in the record against a decision already made."),
   ("2025", "2025-26#e-20251001-1",
    "General Counsel told the senate that state law now bound SGA&#8217;s spending, that its "
    "funding had to be content neutral, and that the Pride Center would lose its office."),
  ]},
 {"id": "f-opinions", "name": "Whether it is allowed to have opinions about the world",
  "span": "1969&#8211;2025",
  "what": "The recurring argument about temperament: is student government a service "
          "organization or a political one? It surfaces whenever the senate takes a position "
          "beyond the campus fence.",
  "shift": "The archive dates the origin to 1969 and the Vietnam Moratorium endorsement, and "
           "the same argument returned in 1982, 2017 and 2021. It never settled. In "
           "2017 a clean DREAM Act resolution failed and a narrower solidarity resolution "
           "passed two weeks later by staying inside a jurisdiction the senate agreed it "
           "had. By 2024 the senate voted unanimously to declare itself nonpartisan.",
  "inst": [
   ("1969", "1969-70#e-19691007-1",
    "The Associated Student Congress endorsed the Vietnam Moratorium; the paper called it a "
    "bold step."),
   ("1982", "1982-83#e-19820401-1",
    "ASG endorsed a congressional candidate; five days later the paper editorialised that "
    "endorsing was not wise for the organization."),
   ("2017", "2016-17#e-20170421-1",
    "The reparations resolution passed 19-10-1 and drew national coverage. Both authors "
    "described it as a conversation starter."),
   ("2017", "2017-18#e-20171025-1",
    "Resolution 2-17-F urging a clean DREAM Act failed 12-17, one senator saying it was not "
    "the university&#8217;s place to put a political hat in the ring."),
   ("2021", "2021-22#e-20211201-2",
    "A resolution condemning bans on the teaching of critical race theory passed 16-15 with "
    "two abstentions after weeks of debate."),
   ("2024", "2024-25#e-20240903-1",
    "Bill 50-23-S, reaffirming SGA as nonpartisan and stating a duty to put forward only "
    "nonpartisan legislation, passed unanimously."),
   ("2025", "2024-25#e-20250404-2",
    "The diversity committee was renamed under a federal executive order, ratified by 88 per "
    "cent of voters."),
  ]},
]

SHAPE = [
 {"id": "s-name", "name": "The name changed once in sixty years",
  "span": "1966&#8211;2025",
  "what": "Founded as the Associated Students of Western Kentucky University, renamed the "
          "Student Government Association only in 1992. Two earlier attempts to change the "
          "branding failed outright.",
  "shift": "After 1992 the renaming energy moved down to committee and officer titles, where "
           "it has stayed. The most recent rename, in 2025, was a response to a federal "
           "executive order and its co-author called the change mostly a formality.",
  "inst": [
   ("1966", "1966-67#e-19660401-1",
    "President Kelly Thompson approved the constitution of the Associated Students on 1 "
    "April; students ratified it on 26 April."),
   ("1980", "1980-81#e-19801030-1",
    "ASG proposed a title change. Nothing in the archive shows it taking effect."),
   ("1981", "1980-81#e-19810402-1",
    "A resolution asked for a new logo; the congress voted to keep the one it had a week "
    "later."),
   ("1992", "1991-92#e-19920407-1",
    "The Associated Students voted to rename themselves the Student Government Association; "
    "students ratified it a week later and it took effect that autumn."),
   ("1992", "1992-93",
    "The August minutes appear under both titles. The organization was still in "
    "transition at its first autumn meeting."),
   ("2016", "2016-17#e-20161116-1",
    "MyCampusToo was made a permanent standing committee and simultaneously renamed the "
    "Committee for Diversity and Inclusion."),
   ("2025", "2024-25#e-20250404-2",
    "Bill 21-25-S renamed the Diversity, Equity and Inclusion Committee the Action and "
    "Opportunity Committee and retitled its officers."),
  ]},
 {"id": "s-constitution", "name": "The constitution as a permanent construction site",
  "span": "1969&#8211;2026",
  "what": "Constitutional revision is the single most repeated activity in the entire "
          "record. There is a revision committee, a referendum, an amendment package or a "
          "full rewrite in more years than not, from the organization&#8217;s third year to "
          "its last.",
  "shift": "The early rewrites were fought section by section in public, with the paper "
           "printing the proposed text. From the 1980s they became routine housekeeping. The "
           "2004 convention was the only true rebuild. After it the pattern was annual "
           "amendment packages, and by the 2020s the work was largely custodial: fixing "
           "references to bodies that no longer existed.",
  "inst": [
   ("1969", "1968-69#e-19690227-1",
    "A committee was appointed to study revision of the constitution, three years in."),
   ("1972", "1971-72#e-19720222-1",
    "The congress voted section by section on a rewritten constitution, with the "
    "<cite>Herald</cite> printing the full proposed executive-branch text. The archive does "
    "not show the referendum&#8217;s result or turnout."),
   ("1978", "1978-79#e-19781130-1",
    "The congress approved a revised constitution."),
   ("1983", "1982-83#e-19830317-1",
    "Changes were approved in March; the Dean of Students publicly questioned them the "
    "following week; students voted on them on the same April ballot that elected Jack "
    "Smith."),
   ("1986", "1986-87#e-19860804-1",
    "Twenty years of amendments were consolidated into one document, the only surviving "
    "snapshot of how the 1966 framework had been patched."),
   ("2004", "2003-04#e-20040316-1",
    "The Constitutional Convention rebuilt the body into three branches. 132 students voted "
    "on it."),
   ("2005", "2004-05#e-20050317-1",
    "A package of 40 constitutional amendments passed 1,193 to 262."),
   ("2013", "2012-13#e-20130226-1",
    "The senate went through the constitution article by article, replacing class-year seats "
    "with college seats and guaranteeing seats for the regional campuses."),
   ("2023", "2023-24#e-20231128-1",
    "Three Legislative Operations bills corrected the governing documents, including "
    "references to a University Senate that had since split in two."),
   ("2026", "2025-26#e-20260224-1",
    "The 25th Senate adopted a codified version of the Executive and Legislative Bylaws, to "
    "supersede all prior versions."),
  ]},
 {"id": "s-regent", "name": "The student regent seat, made and remade by statute",
  "span": "1967&#8211;2009",
  "what": "The largest single expansion of student power in the record was written in "
          "Frankfort, not in the SGA constitution. The seat was created by state "
          "legislation, carried no vote for years, was separately elected for most of its "
          "first two decades, then merged into the presidency.",
  "shift": "Created non-voting in 1968 and filled by the Congress. Campaigns for a vote "
           "failed repeatedly into the 1970s. A 1982 state bill changed how the regent was "
           "chosen and produced WKU&#8217;s first campus-wide regent election. By 1991 one "
           "person held both offices, which is why every presidential resignation since has "
           "been a governance problem.",
  "inst": [
   ("1967", "1967-68#e-19671102-1",
    "A <cite>Herald</cite> article reported support for putting a student on the Board of "
    "Regents, months before a bill reached committee."),
   ("1968", "1967-68#e-19680404-1",
    "William Menser assumed duties as a board member. The seat carried no vote."),
   ("1969", "1968-69",
    "Because president Bill Straeffer was an out-of-state student, the Congress elected Paul "
    "Gerard to the seat instead. He sat as a non-voting member."),
   ("1970", "1969-70#e-19700313-1",
    "The legislature dropped the bill that would have given the seat a vote, under a headline "
    "saying lawmakers had kept students impotent."),
   ("1972", "1971-72#e-19720201-1",
    "&#8220;Student Regent May Get Vote.&#8221; Four years after the seat was created it was "
    "still non-voting."),
   ("1974", "1973-74#e-19740619-1",
    "Gregory McKinney was sworn in as WKU&#8217;s first African American student regent."),
   ("1982", "1981-82#e-19820202-1",
    "After a state bill changed how the regent was chosen, five students stood in the first "
    "campus-wide election for the seat. No majority on 9 February forced a runoff; the "
    "resulting term ran about two months."),
   ("1983", "1982-83#e-19830203-1",
    "President Margaret Ragan published a piece explaining that the presidency and the "
    "student regent seat were now separate positions."),
   ("1991", "1991-92",
    "WKU&#8217;s own newsletter reported Heather Falmlen as both student regent and ASG "
    "president &#8212; the two offices, separately elected two decades earlier, held by one "
    "person."),
   ("2009", "2008-09#e-20090212-1",
    "After a resignation split the offices, the Judicial Council voted 2-1 to hold a special "
    "election over the chief justice&#8217;s dissent. The seat had sat empty 26 days."),
  ]},
 {"id": "s-senate", "name": "Senate size and who counts as a constituency",
  "span": "1968&#8211;2025",
  "what": "The chamber has been called a Congress and a Senate, has run from a handful of "
          "at-large congressmen to 50 members, and has repeatedly redefined which students "
          "get a guaranteed seat.",
  "shift": "From four executives and two congressmen at large in 1968, through residence "
           "hall and college representation in the late 1970s and 1980s, to a 2013 rebuild "
           "that replaced class-year seats with college seats and guaranteed the regional "
           "campuses, to a 36-seat constitutional formula and then a proliferation of "
           "identity and status seats: international, Gatton Academy, graduate, "
           "first-generation, transfer, Honors.",
  "inst": [
   ("1968", "1968-69#e-19680502-1",
    "The elected slate was president, vice president, secretary, treasurer and two "
    "congressmen at large."),
   ("1979", "1979-80#e-19790920-1",
    "A seats bill passed after being revised under pressure; the paper called the "
    "representation bill a small step in the right direction."),
   ("1983", "1982-83#e-19830301-1",
    "Twenty-four students were elected to the Senate &#8212; the only hard seat count the "
    "archive preserves for the whole of the 1980s."),
   ("1988", "1987-88#e-19880223-1",
    "The organization publicly explained its empty seats; four congress positions had been "
    "filled at a single meeting."),
   ("1990", "1989-90#e-19900329-1",
    "The congress voted to expand itself so that classes and student groups would get more "
    "voice."),
   ("2006", "2006-07#e-20060905-1",
    "The senate opened the year with 18 seats and eight senators present, swore in eight "
    "more that night, and had grown to 31 seats by November."),
   ("2011", "2010-11#e-20110211-1",
    "The <cite>Herald</cite> reported 50 total members and an operating budget of $121,335 "
    "drawn from tuition."),
   ("2013", "2013-14#e-20130919-2",
    "A referendum created an international student senate seat, which the president said "
    "would make WKU the first student government in the state to have one."),
   ("2018", "2017-18#e-20180228-1",
    "A bill replacing at-large and graduate seats with first-generation, transfer, "
    "non-traditional and intercultural seats failed 14-18."),
   ("2023", "2023-24#e-20231129-1",
    "Bill 14-23-F created a Mahurin Honors College senator. Its first occupant was elected "
    "student body president in 2026."),
   ("2025", "2024-25#e-20250415-1",
    "The spring ballot filled at-large, class, transfer, non-traditional, first-generation, "
    "intercultural and college seats &#8212; constituencies the 1966 constitution had no "
    "concept of."),
  ]},
 {"id": "s-real", "name": "What actually changed the organization&#8217;s reach",
  "span": "1967&#8211;2025",
  "what": "A short list. Each of these altered what SGA could actually do, and almost every "
          "one originated outside SGA&#8217;s own constitution.",
  "shift": "The record&#8217;s hardest finding about itself: sixty years of internal "
           "constitutional revision redistributed authority among students, and the changes "
           "that enlarged or reduced the organization&#8217;s actual reach came from a state "
           "statute, a state bill, a university budget line, a referendum mechanism and, in "
           "2025, a state law.",
  "inst": [
   ("1967", "1966-67#e-19670530-1",
    "Dean Keown&#8217;s memo proposing a student fee structure to create a budget. Money "
    "made the body operational, and it was proposed by the Dean of Students, not by "
    "students."),
   ("1968", "1967-68#e-19680404-1",
    "The state statute creating the student regent seat gave students a permanent chair in "
    "the room where tuition and fees are set. SGA neither wrote it nor could amend it."),
   ("1982", "1981-82#e-19820202-1",
    "The state regents bill changed how the student regent was chosen, producing the first "
    "campus-wide election for the seat."),
   ("2003", "2002-03#e-20030304-2",
    "The first student referendum in SGA history put a $3 radio fee to students and sent it "
    "to the regents. The mechanism was used again for the Talisman fee and the football "
    "question."),
   ("2004", "2003-04#e-20040316-1",
    "The Constitutional Convention made every enrolled student a member of SGA with the "
    "right to vote in its elections. It is the quietest clause in the record and the one "
    "that changed the organization&#8217;s standing most."),
   ("2011", "2010-11#e-20110222-1",
    "SGA had to pass a resolution on the Downing renovation&#8217;s design and fees before "
    "the regents could approve the project; the senate tabled it in December for lack of "
    "student input. A veto point that actually bit."),
   ("2020", "2020-21#e-20201202-2",
    "Pass/D/Fail was won by mobilisation rather than by any clause: a petition of more than "
    "3,500 signatures in three days and nearly twenty pages of student testimony."),
   ("2025", "2025-26#e-20251001-1",
    "House Bill 4 bound SGA&#8217;s spending because SGA receives university money. A "
    "genuine reduction in its discretion, imposed entirely from outside."),
  ]},
 {"id": "s-cosmetic", "name": "Reform that was cosmetic",
  "span": "1977&#8211;2025",
  "what": "Changes framed as structural reform that left the organization&#8217;s capacity "
          "untouched: renamings, symbolic committees, procedural tinkering and "
          "self-evaluations with no recorded follow-through.",
  "shift": "The pattern did not change. The clearest single case was 1985-86, when the "
           "congress abolished its Finance Committee in September and wrote a Financial "
           "Advisory Council into the by-laws the following April &#8212; the same function "
           "under a new name, seven months apart.",
  "inst": [
   ("1977", "1976-77#e-19770215-1",
    "Bill 6 proposed that ASG conduct a self-evaluation for transparency and improvement. "
    "The archive holds the bill and nothing about a result."),
   ("1981", "1980-81#e-19810402-1",
    "The proposed title change and the new-logo resolution both went nowhere."),
   ("1985", "1985-86#e-19850924-1",
    "The congress abolished its own Finance Committee. It wrote a Financial Advisory Council "
    "into the by-laws the following April: the same function under a new name."),
   ("2014", "2013-14#e-20140213-1",
    "An amendment stripping the president&#8217;s sole power to appoint justices passed, "
    "then was undone by the same attendance problem it was meant to address."),
   ("2018", "2017-18#e-20180328-1",
    "Moving committee-chair appointments from the president to the speaker failed 26-2, with "
    "the speaker himself voting against. It had failed the year before too."),
   ("2021", "2021-22#e-20211006-2",
    "A bill barred the Speaker of the Senate from voting on legislation, alongside two bills "
    "scrubbing obsolete 2007-era bylaws."),
   ("2025", "2024-25#e-20250404-2",
    "The DEI committee rename. A co-author called the change mostly a formality; the chair "
    "said the committee at its core was not changing."),
  ]},
 {"id": "s-budget", "name": "The budget, and what could be done with it",
  "span": "1973&#8211;2024",
  "what": "The total is set by the university. What SGA controls is how it is divided, and "
          "in several years how much of it goes unspent.",
  "shift": "ASG ran concerts and lost money on them through the 1970s, until the Regents "
           "moved the lectures and concerts to a rebuilt University Center Board in March "
           "1979 and funded it with $80,000. University cuts in "
           "2013 removed the automatic inflation increase SGA had been receiving, but the "
           "modern totals did not move in one direction: $125,000 in 2013-14, $138,500 in "
           "2015-16, $100,000 in 2024-25. The recurring problem was not only scarcity but "
           "the failure to spend.",
  "inst": [
   ("1973", "1973-74#e-19730828-1",
    "The Board of Regents voted to increase the ASG allotment, and the organization became "
    "something else: a concert promoter, a survey-taker, a runner of free evening courses."),
   ("1979", "1978-79#e-19790331-1",
    "ASG faced losing control of student activities funding, and lost it. On 31 March the "
    "Board of Regents gave the lectures and concerts to a rebuilt University Center Board "
    "and funded that board with $80,000 for programming."),
   ("1986", "1986-87#e-19860911-1",
    "A $12,100 budget, reported alongside a plan to reach students by telephone."),
   ("2004", "2003-04#e-20040408-1",
    "With about $45,000 left of a $105,000 budget, SGA moved to spend the remainder before "
    "leftover funds went to offset university cuts."),
   ("2006", "2006-07#e-20061024-1",
    "About $24,000 of $115,000 had gone unspent the previous year and returned to the "
    "general fund."),
   ("2013", "2013-14#e-20131010-1",
    "A $125,000 budget funded from tuition at about $6.25 a student, after a planned "
    "increase did not come through."),
   ("2015", "2015-16#e-20150915-2",
    "The budget fell $19,500 to $138,500 when a private donation was not repeated and the "
    "university cut a further $4,500. Organizational funding took the largest share of the "
    "loss."),
   ("2024", "2024-25#e-20240828-1",
    "$100,000, the same total as the year before, with $20,000 for organizational aid and "
    "$23,500 for scholarships."),
  ]},
]

THIN = [
 ("1969&#8211;1975", "1971-72",
  "No general-election turnout figure survives for any year in this stretch. The "
  "constitutional referendum of March 1972 is the most consequential structural vote of the "
  "decade, and the archive does not show its result or its turnout."),
 ("The 1970s", "1975-76",
  "The decade yields three raw vote counts in total &#8212; 527 in the 1976 primary, 95 in a "
  "1978 freshman primary, 830 in the 1979 primary &#8212; and two margins, the 26 votes by "
  "which Bob Moore won in 1977 and the eleven by which a freshman president was elected in "
  "1978. There is not one general-election total for the whole decade."),
 ("1979&#8211;80", "1979-80",
  "The emptiest presidency in the file. The year page states outright that the archive does "
  "not yet show what the Hargrove administration passed or fought over, and that "
  "<cite>Herald</cite> issues from that autumn and spring have not been checked."),
 ("The 1980s", "1986-87",
  "Only one senate seat count survives for the entire decade: the 24 senators elected in "
  "March 1983. Committee structure is known from two bills and one filed Judicial Council "
  "roster. The published result of the April 1987 presidential election is not recorded at "
  "all."),
 ("1990&#8211;1998", "1994-95",
  "One turnout number in nine years. Several years&#8217; pages state that no full officer "
  "list, committee structure or seat count survives beyond the president. The 1995 and 1996 "
  "headlines describe a decline the archive cannot quantify."),
 ("2002&#8211;03", "2002-03",
  "TopSCHOLAR&#8217;s full-text files for this year sit behind an automated-access check and "
  "have not been read. The ad hoc financial review committee formed in the gazebo dispute is "
  "the only committee identified by name."),
 ("2019&#8211;2021", "2020-21",
  "No presidential turnout figure survives for the September 2020 or April 2021 elections, "
  "and the 2019 results story reported none either. The COVID year carries no editorial "
  "criticism of SGA at all &#8212; which is a fact about the sources, not about the year."),
 ("Cartoons after 1999", "1998-99",
  "No editorial cartoon about SGA appears anywhere in this archive after the 1999 cartoon on "
  "nasty campaigns. Whether the paper stopped drawing student government, or the digitised "
  "index stopped recording cartoons, cannot be resolved from this record."),
 ("Questions the record drops", "1991-92",
  "No source found reports how the investigations into the regents&#8217; chairman ended, or "
  "how SGA resolved its 1999 investigation into racially charged campaign fliers, or why Bob "
  "Moore was ruled ineligible for an SGA job in 1978."),
]


def _pat_block(p):
    rows = []
    for lab, yid, txt in p["inst"]:
        rows.append('<li><a class="yr" href="' + _yhref(yid) + '">' + lab
                    + '</a><p>' + txt + '</p></li>')
    return ('<article class="pat" id="' + p["id"] + '">'
            + '<h3>' + p["name"] + '<span class="sp">' + p["span"]
            + ' &middot; ' + str(len(p["inst"])) + ' instances</span></h3>'
            + '<p class="what">' + p["what"] + '</p>'
            + '<ol class="inst">' + "".join(rows) + '</ol>'
            + '<p class="shift"><b>How it changed.</b> ' + p["shift"] + '</p>'
            + '</article>')


def _pat_group(group):
    return "".join(_pat_block(p) for p in group)


def _pat_index(group, label):
    rows = []
    for p in group:
        rows.append('<li><a href="#' + p["id"] + '">' + p["name"] + '</a>'
                    + '<span class="sp">' + p["span"] + ' &middot; '
                    + str(len(p["inst"])) + ' instances</span></li>')
    return '<p class="lab">' + label + '</p><ul class="pindex">' + "".join(rows) + '</ul>'


PATTERNS_BODY = """
<header class="head"><div class="wrap">
 <p class="kicker">Read across the years, not down them</p>
 <h1>The patterns</h1>
 <p class="lede">The same arguments come back. Campus lighting, the price of a textbook, who
 is in the room, whether anybody voted: the subjects that recur across sixty years of student
 government at Western, set out with the years they recur in.</p>
 <p class="scope">This page holds __NPAT__ recurring patterns and __NINST__ dated instances,
 every one of them drawn from a sourced entry on this site and checked against the record.
 Each pattern gives its span, a spread of instances across different decades, and what changed
 between the first and the last. Where the record is thin, that is said rather than smoothed
 over. The <a href="story.html">story</a> reads the same archive in order, and
 <a href="events.html">what SGA put on</a> reads it by what the organization staged.</p>
</div></header>

<div class="wrap">
<nav class="contents" aria-label="Contents">
 <p class="lab">On this page</p>
 <ol>
  <li><span>One</span><a href="#business">What it does, generation after generation</a></li>
  <li><span>Two</span><a href="#verdicts">What people said about it</a></li>
  <li><span>Three</span><a href="#apathy">The apathy argument</a></li>
  <li><span>Four</span><a href="#fights">The recurring fights</a></li>
  <li><span>Five</span><a href="#shape">How the organization changed shape</a></li>
  <li><span>Six</span><a href="#thin">Where the record is thin</a></li>
 </ol>
</nav>

<div class="body">

<section class="part" id="business">
<header class="parthead"><span class="n">One</span>
<h2>What it does, generation after generation</h2></header>
<p class="stand">Fifteen subjects the organization has come back to every four or five years
since 1966, wearing whatever clothes the decade supplied. What changes is not the subject but
SGA&#8217;s position in relation to it.</p>

<div class="note">
<p>The strongest single finding in this material is a change of role rather than of subject.
For its first thirty years SGA asked the university to do things: put a telephone there, open
the library later, run a shuttle, assign staff to administer scholarships. For its last thirty
it increasingly does them itself, out of its own budget: $600 a year to keep the library open
until 2 a.m., a $15,000 retroactive bill for a year of the safe-ride van, $23,500 in
scholarships, 450 Uber vouchers, a shelf of borrowable graphing calculators, $10,000 split
among 33 clubs.</p>
</div>

<p class="finding">Petitioner to vendor. The organization converts from an applicant for
university action into a small vendor of student services, and calls that its central
programme.
<b>The arc runs from Resolution 79-10, which asked WKU to assign somebody to administer
scholarships, to a $100,000 budget in 2024 that awarded them itself.</b></p>

__IX_STANDING__

__G_STANDING__
</section>

<section class="part" id="verdicts">
<header class="parthead"><span class="n">Two</span>
<h2>What people said about it</h2></header>
<p class="stand">Sixty years of verdicts, grouped by the kind of verdict rather than by the
year. The <cite>College Heights Herald</cite> is the principal witness for most of this period
and the standing antagonist, and it opened with a judgement rather than a welcome. SGA&#8217;s
own legislation files, the Board of Regents minutes and the university&#8217;s records carry
the rest.</p>

<div class="note">
<p>The register moves in phases. From 1966 to about 1980 the paper scolds the student body for
not deserving its government. From 1980 to 1999 it stops arguing and starts drawing, and the
presidents write back in the letters column. After 1999 no editorial cartoon about SGA appears
in this archive at all, and the criticism migrates from the opinion page into the room itself:
students standing up at meetings, organizations withdrawing recognition, and censure
hearings.</p>
</div>

__IX_VERDICTS__

__G_VERDICTS__
</section>

<section class="part" id="apathy">
<header class="parthead"><span class="n">Three</span>
<h2>The apathy argument</h2></header>
<p class="stand">One continuous thread, and the only one in the archive that can be read as a
series of numbers. The counts the record preserves, in order.</p>

<div class="note">
<p>The organization has spent sixty years measuring itself against the day it was created.
2,538 students voted in the founding referendum of April 1966, and 2,894 in the election of
1968 &#8212; about 34 per cent of a roughly 8,500-student enrolment. Enrolment then more than
doubled and the raw count never recovered. Against the 17,500 students reported in 2002 and about 18,000 in 2004, the modern
ceiling is roughly 2,400.</p>
<p>Three cautions before reading the series as a trend. The denominators change and are
recorded only at scattered points, so the modern counts cannot be turned into comparable
percentages. Autumn senate elections and spring executive elections are different animals:
autumn totals in the record run from 398 to 977, spring general-election totals from 908 to
2,894. And some
figures are ballots cast while others are votes in the presidential race, which is why 2018
appears here as 2,378. Three totals below &#8212; 2002, 2005 and 2010 &#8212; are the two
candidates&#8217; votes added together, because the record gives no overall figure for those
years. The long gap in the middle is real: between the general election of April 1992 and the
collapsed election of 1999, not one race in this archive carries a vote total.</p>
</div>

<ol class="tn">__TURNOUT__</ol>

<h3 class="sub">Where it jumped, and what caused it</h3>
<div class="note">
<p>Every upward spike in the series is attached to one of three things: a constitutional
moment, a referendum sharing the ballot, or a genuinely contested race. 1966 and 1968 were
votes about whether the organization should exist and who should run it. In 2003 the presidency
was uncontested but a $3 radio-station fee was on the ballot, and the executive vice president
who championed it had argued in as many words that it would boost turnout. In 2006 SGA
deliberately ran its Division I-A football referendum alongside the homecoming queen election,
and the president conceded the tie-in probably drew football-friendly voters. 2016 and 2018
were real contests. So was 2026.</p>
<p>The counterexamples point the same way. Turnout fell to 908 in 2014, in a year the sitting
president ran unopposed and, she said, spent nothing on her campaign. The presidency was
uncontested in 2023, 2024 and 2025. Then in April 2026 two tickets took 27 student-submitted
questions at a town hall, sat for a debate with the campus radio station, and 1,601 students
voted &#8212; 635 more than the year before, a rise of 66 per cent. The archive&#8217;s own verdict is that turnout
tracks whether there is an actual contest.</p>
<p>What the organization tried instead fills sixty years: a survey of wanted activities in
1967, extra polling places in 1972, published roll-call votes in 1978, a telephone campaign in
1986, a ban on write-in campaigns in 1988, Anti-Apathy Week in 1990, an ambassador council in
2003, extra credit for attending the debate in 2008, new
seats for constituencies that had none, an SGA clause in every course syllabus in 2022, Uber
vouchers in 2024, and a POLLapalooza in 2025 that fell 2,034 votes short of its stated goal.
Two moves in the same decade cut in opposite directions on the same problem: in 2017 the senate
lowered its own grade-point requirement from 2.5 to 2.0 to make the body more representative,
ratified by referendum, and in 2024 senators voted to put the floors back up.</p>
</div>
</section>

<section class="part" id="fights">
<header class="parthead"><span class="n">Four</span>
<h2>The recurring fights</h2></header>
<p class="stand">Inside its own walls the organization can do almost anything: void an
election, disqualify a president-elect, censure a vice president, remove three senators in one
vote. Outside them it has rarely compelled anything, and the exceptions came by persuading
somebody who could act.</p>

<div class="note">
<p>The sharpest artefact of that ceiling is 2013. SGA&#8217;s Judicial Council disqualified the
president-elect 3-2; she appealed to the vice president for student affairs; he reinstated her;
and the council concluded in an emergency meeting that it did not believe it had the power to
contest him, while recording its official disapproval. The student judiciary discovered it was
not final.</p>
<p>What SGA wins outside itself, it wins by producing evidence somebody else can act on: 1,500
signatures against plus/minus grading in 2003, a 1,066-765 referendum that sent a fee to the
regents that same spring, 3,500 signatures in three days in 2020. Not by passing a
resolution.</p>
</div>

__IX_FIGHTS__

__G_FIGHTS__
</section>

<section class="part" id="shape">
<header class="parthead"><span class="n">Five</span>
<h2>How the organization changed shape</h2></header>
<p class="stand">Across sixty years SGA rewrote its own constitution constantly and gained
almost no new power by doing it.</p>

<div class="note">
<p>Almost every structural change that enlarged what the organization could do came from
outside its own document: a 1968 state statute that created the student regent seat, a 1982
state bill that changed how the seat was filled, the university&#8217;s annual decision about
the budget line, and in 2025 a state law that told SGA what it may spend money on. The internal
rewrites &#8212; from the revision fights of 1969 to 1972, through the 2004 Constitutional
Convention, to the codified bylaws of 2026 &#8212; almost always redistributed authority among
students rather than adding any against the administration.</p>
<p>Two items on the list below did come from inside. The referendum mechanism first used in
2003 put a $3 radio fee to students and sent it to the regents, and was used again for the
Talisman fee and the football question. And the 2004 convention made every enrolled student a
member of SGA with the right to vote in its elections, the quietest clause in the record. 132
of roughly 18,000 students voted on the constitution that did it.</p>
</div>

__IX_SHAPE__

__G_SHAPE__
</section>

<section class="part" id="thin">
<header class="parthead"><span class="n">Six</span>
<h2>Where the record is thin</h2></header>
<p class="stand">The shape of these patterns is partly the shape of what survived. The gaps are
findings too, and reading past them would make the recent decades look worse than the early
ones simply because they are better documented.</p>

<div class="note">
<p>For roughly the first twenty-five years the evidence is a digitised article index rather
than article text: we know what the <cite>Herald</cite> said a piece was about, not what it
said. Disciplinary conflict only becomes visible when SGA starts keeping and posting its own
minutes, which is why the 1970s look less litigious than the 2010s. The 1980s produced
recounts, a voided general election, a revote and a write-in dispute that ran six months, which
is not the profile of an organization with no internal conflict.</p>
</div>

<ol class="inst wide">__THIN__</ol>

<p class="patfoot">Every instance above is drawn from a dated, sourced entry on this site and
links to the year it came from. The <a href="history.html">complete timeline</a> holds them all
in order, the <a href="index.html">board</a> holds every year, and the
<a href="sources.html">sources page</a> sets out what each collection covers and where it
fails.</p>
</section>

</div></div>
"""


def render_patterns(ys):
    groups = STANDING + VERDICTS + FIGHTS + SHAPE
    n_pat = len(groups)
    n_inst = sum(len(p["inst"]) for p in groups) + len(TURNOUT) + len(THIN)

    trows = []
    for lab, yid, count, note, up in TURNOUT:
        trows.append('<li' + (' class="up"' if up else '') + '>'
                     + '<a class="yr" href="' + _yhref(yid) + '">' + lab + '</a>'
                     + '<span class="c">' + (count if count != "0" else "&#8212;")
                     + '</span><p>' + note + '</p></li>')

    hrows = []
    for lab, yid, txt in THIN:
        hrows.append('<li><a class="yr" href="' + _yhref(yid) + '">' + lab
                     + '</a><p>' + txt + '</p></li>')

    body = (PATTERNS_BODY
            .replace("__NPAT__", str(n_pat))
            .replace("__NINST__", str(n_inst))
            .replace("__IX_STANDING__", _pat_index(STANDING, "The fifteen"))
            .replace("__G_STANDING__", _pat_group(STANDING))
            .replace("__IX_VERDICTS__", _pat_index(VERDICTS, "Ten kinds of verdict"))
            .replace("__G_VERDICTS__", _pat_group(VERDICTS))
            .replace("__IX_FIGHTS__", _pat_index(FIGHTS, "Nine standing fights"))
            .replace("__G_FIGHTS__", _pat_group(FIGHTS))
            .replace("__IX_SHAPE__", _pat_index(SHAPE, "Seven structural threads"))
            .replace("__G_SHAPE__", _pat_group(SHAPE))
            .replace("__TURNOUT__", "".join(trows))
            .replace("__THIN__", "".join(hrows)))

    desc = ("What recurs across sixty years of student government at Western Kentucky "
            "University: " + str(n_pat) + " patterns and " + str(n_inst) + " dated "
            "instances, from campus lighting and textbook prices to turnout, constitutional "
            "rewrites and the student regent seat.")
    return shell("The patterns · SGA 60", desc, body, PATTERNS_CSS,
                 depth=0, current="patterns.html")


# ---------------------------------------------------------------- data
# ---------------------------------------------------------------- programmes
PROGRAMS_CSS = """
.pgheads{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
 gap:1px;background:var(--line);border:1px solid var(--line);margin:26px 0 0}
.pgheads a{background:var(--paper);padding:13px 14px 12px;text-decoration:none;
 display:block;transition:background .12s}
.pgheads a:hover{background:var(--paper2)}
.pgheads b{display:block;font-size:1.5rem;font-weight:600;letter-spacing:-.02em;
 color:var(--red);font-variant-numeric:tabular-nums;line-height:1.05}
.pgheads span{display:block;font-family:var(--ui);font-size:11.5px;font-weight:600;
 letter-spacing:.09em;text-transform:uppercase;color:var(--ink3);margin-top:5px}

.pgsec{margin:0 0 8px;scroll-margin-top:14px}
.pgsec>h2{font-size:1.3rem;margin:56px 0 3px;padding-top:16px;
 border-top:2px solid var(--black);letter-spacing:-.02em}
.pgsec>h2 .n{font-family:var(--ui);font-size:12px;font-weight:600;color:var(--red);
 letter-spacing:.02em;margin-left:11px;vertical-align:2px}
.pgsec>.blurb{color:var(--ink2);font-size:.93rem;max-width:var(--measure);margin:0 0 6px}

.pg{display:grid;grid-template-columns:8.5rem 1fr;gap:0 26px;padding:16px 0;
 border-top:1px solid var(--line2)}
@media(max-width:640px){.pg{grid-template-columns:1fr;gap:3px;padding:14px 0}}
.pg .when{font-size:.83rem;color:var(--ink3);padding-top:4px;
 font-variant-numeric:tabular-nums}
.pg .when time{display:block;color:var(--ink2);font-weight:600}
.pg .when .yr{display:block;margin-top:3px}
.pg .when .yr a{color:var(--ink3);text-decoration:none;border-bottom:1px solid var(--line)}
.pg .when .yr a:hover{color:var(--red)}
.pg h3{font-size:1.02rem;margin:0 0 5px;letter-spacing:-.01em}
.pg p{margin:0;max-width:var(--measure)}
.pg .money{margin:7px 0 0;font-size:.87rem;color:var(--ink2);
 border-left:2px solid var(--red);padding-left:11px}
.pg .cite{font-size:.83rem;color:var(--ink3);margin-top:8px;line-height:1.5}
.pg .cite a{margin-right:14px;overflow-wrap:anywhere}
.pg[hidden]{display:none}
.pgnone{color:var(--ink3);font-size:.9rem;margin:14px 0 0}
"""

PROGRAMS_JS = """
<script>
(function(){
var f=document.getElementById('pf'),ro=document.getElementById('pr'),
    cl=document.getElementById('pclear'),
    rows=[].slice.call(document.querySelectorAll('.pg')),
    secs=[].slice.call(document.querySelectorAll('.pgsec')),
    chips=[].slice.call(document.querySelectorAll('.pgfilter button')),era='all';
rows.forEach(function(r){
 r._k=(r.textContent||'').replace(/\\s+/g,' ').toLowerCase();});
function word(n,s,p){return n+' '+(n===1?s:p);}
function run(){
 var q=f.value.toLowerCase().trim(),n=0;
 rows.forEach(function(r){
  var ok=(era==='all'||r.dataset.d===era)&&(!q||r._k.indexOf(q)>-1);
  r.hidden=!ok;if(ok)n++;});
 secs.forEach(function(s){
  var v=s.querySelectorAll('.pg:not([hidden])').length;
  s.hidden=!v;
  var c=s.querySelector('h2 .n');if(c)c.textContent=v;});
 if(q&&!n)ro.textContent='Nothing matches \\u201c'+f.value.trim()+'\\u201d. Try a '
  +'performer, a year or a single word.';
 else ro.textContent=word(n,'thing','things')+' student government put on'
  +(q?' matching \\u201c'+f.value.trim()+'\\u201d':'')+'.';
 if(cl)cl.hidden=!q;
 var p=new URLSearchParams(location.search);
 if(q)p.set('q',f.value.trim());else p.delete('q');
 if(era!=='all')p.set('era',era);else p.delete('era');
 var qs=p.toString();
 history.replaceState(null,'',location.pathname+(qs?'?'+qs:''));
}
chips.forEach(function(c){c.addEventListener('click',function(){
 era=c.dataset.d;chips.forEach(function(x){
  x.setAttribute('aria-pressed',String(x.dataset.d===era))});run();});});
f.addEventListener('input',run);
if(cl)cl.addEventListener('click',function(){f.value='';f.focus();run();});
var p0=new URLSearchParams(location.search);
if(p0.get('q'))f.value=p0.get('q');
if(p0.get('era')){era=p0.get('era');chips.forEach(function(x){
 x.setAttribute('aria-pressed',String(x.dataset.d===era))});}
run();
})();
</script>"""


def year_anchors(y):
    """The anchor each event gets on its own year page, computed the same way
    render_year computes it so the links land on the right entry."""
    seen = {}
    return {id(e): event_anchor(e, seen)
            for e in sorted(y["events"], key=lambda e: e["date"])}


def render_programs(ys):
    """Everything student government put on for the campus, sixty years of it,
    gathered out of the year records and grouped by what kind of thing it was."""
    items = []
    for y in ys:
        anch = year_anchors(y)
        for e in y["events"]:
            if is_program(e):
                items.append((y, e, anch[id(e)]))
    items.sort(key=lambda t: t[1]["date"])
    n = len(items)

    def dec_of(yid):
        s = int(yid[:4])
        for lo, hi, label, short, stem in DECADES:
            if lo <= s <= hi:
                return short, label
        return None, None

    dec_counts = {}
    for y, e, _ in items:
        short, _lab = dec_of(y["id"])
        dec_counts[short] = dec_counts.get(short, 0) + 1

    by_kind = {}
    for y, e, a in items:
        by_kind.setdefault(e["kind"], []).append((y, e, a))

    # the summary strip: one figure per kind, linking to its section
    heads = "".join(
        f'<a href="#k-{k}"><b>{len(by_kind[k])}</b>'
        f'<span>{h(KIND_MANY[k])}</span></a>'
        for k in KIND_ORDER if by_kind.get(k))

    span = f"{items[0][1]['date'][:4]} to {items[-1][1]['date'][:4]}" if items else ""
    n_years = len({y["id"] for y, _, _ in items})
    n_money = sum(1 for _, e, _ in items if e.get("money"))
    lede = (f"Student government has always been more than a legislature. It booked the "
            f"bands, paid the lecturers, ran the film series and kept the services going. "
            f"This page gathers {n} of those things, {span}, across {n_years} academic "
            f"years, each one dated and carrying the source it rests on. "
            f"{n_money} of them record what it cost, what it took at the gate, or how "
            f"many people came.")

    chips = ['<button type="button" data-d="all" aria-pressed="true">All sixty years '
             f'<span class="c">{n}</span></button>']
    for lo, hi, label, short, stem in DECADES:
        if dec_counts.get(short):
            chips.append(f'<button type="button" data-d="{h(short)}" aria-pressed="false">'
                         f'{h(short)} <span class="c">{dec_counts[short]}</span></button>')

    secs = []
    for k in KIND_ORDER:
        block = by_kind.get(k)
        if not block:
            continue
        rows = []
        for y, e, a in block:
            disp, mach, _ = fmt_date(e["date"])
            cites = [f'<a href="y/{h(y["id"])}.html#{a}">In the record</a>']
            if e.get("src"):
                cites.append(src_link(e["src"]))
                if e.get("src2"):
                    cites.append(src_link(e["src2"]))
            if e.get("src", {}).get("file"):
                cites.append(f'<a href="docs/{h(e["src"]["file"])}">Read it here</a>')
            short, _lab = dec_of(y["id"])
            rows.append(
                f'<article class="pg" data-d="{h(short or "")}">'
                f'<div class="when"><time datetime="{mach}">{h(disp)}</time>'
                f'<span class="yr"><a href="y/{h(y["id"])}.html">{h(y["id"])}</a></span></div>'
                f'<div><h3>{h(e["title"])}</h3><p>{h(e["body"])}</p>{money_line(e)}'
                f'<p class="cite">{"".join(cites)}</p></div></article>')
        blurb = h(KIND_BLURB[k])
        if k == "concert":
            # The record's own shape: the concert era and the decision that closed
            # it. Said with the caveat it needs, because a gap in an archive can
            # always be a gap in the research instead.
            VOTE = "1979-03-31"
            pre = sum(1 for _, e, _ in block if e["date"] < VOTE)
            post = len(block) - pre
            if pre and post < pre:
                blurb += (
                    f' The shape of this list is worth noticing: {pre} of the {len(block)} '
                    f'fall before 31 March 1979, and {post} after it. On that day the '
                    f'Regents moved lectures and concerts away from Associated Student '
                    f'Government to a reorganised University Center Board, with $80,000 '
                    f'for programming (<a href="y/1978-79.html">1978-79</a>). Booking '
                    f'concerts had been student government’s work for a decade; after '
                    f'that vote it was somebody else’s. Later years are thinner in the '
                    f'record generally, so the fall in this list is not proof on its own, '
                    f'but the decision behind it is on the page.')
        secs.append(
            f'<section class="pgsec" id="k-{k}">'
            f'<h2>{h(KIND_MANY[k])}<span class="n">{len(block)}</span></h2>'
            f'<p class="blurb">{blurb}</p>{"".join(rows)}</section>')

    body = f"""
<header class="head"><div class="wrap">
 <p class="kicker">1966 to 2026</p>
 <h1>What SGA put on</h1>
 <p class="scope">{lede}</p>
 <div class="pgheads">{heads}</div>
</div></header>
<div class="wrap">
<div class="tools">
 <label class="field" for="pf"><span class="lab">Search what they put on</span>
 <input id="pf" type="search" autocomplete="off" spellcheck="false"
  placeholder="a performer, a speaker, a service"></label>
 <div class="facets pgfilter" role="group" aria-label="Which decade">{"".join(chips)}</div>
 <p class="readout" id="pr" role="status"></p>
 <button class="clearq" id="pclear" type="button" hidden>Clear the search</button>
 <p class="tlkey">Every item here is also an entry in its own year and in the
 <a href="history.html?show=p">complete timeline</a>. Nothing on this page is stored
 twice: it is the same record, sorted by what kind of thing it was. Where a source is
 an advance notice rather than a review, the entry says so, because the archive can
 prove what was booked more often than it can prove how the night went.</p>
 <p class="tlkey"><b>This is not everything SGA put on. It is not close.</b> To reach this
 page a thing had to survive twice: it had to happen, and somebody had to write it down
 somewhere that has since been digitised and put online. What that leaves is the
 <cite>Herald</cite> back file, the <cite>Talisman</cite> yearbooks, SGA's own legislation
 and minutes on TopSCHOLAR, wkuherald.com from about 2003, the university news pages and
 the Wayback Machine. Everything on this page came from those. Student government has been
 running events most weeks for sixty years, and the great majority of them left no trace
 that a search can reach: no notice in the paper, or a notice in an issue nobody has
 scanned, or a flyer on a board, or a night that was simply remembered. If you were at
 something that is not here, it is missing from the record rather than from the history,
 and the project would like to hear about it.</p>
</div>
<div class="body">
{"".join(secs)}
<p class="pgnone">This page is built from what the archive has so far. Years thin
here are years whose <cite>Herald</cite> issues have not yet been worked through, not
years when student government put nothing on.</p>
</div></div>{PROGRAMS_JS}"""
    desc = (f"Every concert, lecture, film, festival, tradition and service the Western "
            f"Kentucky University Student Government Association put on, {span}: {n} "
            f"dated and sourced entries.")
    return shell("What SGA put on · SGA 60", desc, body,
                 PROGRAMS_CSS, depth=0, current="events.html")


# ---------------------------------------------------------------- irregular terms
IRREGULAR_CSS = """
.hand{border-top:1px solid var(--line);padding:26px 0 4px}
.hand h3{font-size:1.12rem;margin:0 0 3px;letter-spacing:-.015em}
.hand .yr{font-family:var(--ui);font-size:12px;font-weight:600;letter-spacing:.1em;
 text-transform:uppercase;color:var(--red);margin:0 0 9px}
.hand p{margin:0 0 10px;max-width:var(--measure)}
.baton{display:grid;grid-template-columns:1fr auto 1fr;gap:0 18px;align-items:stretch;
 margin:14px 0 4px;max-width:38rem}
@media(max-width:640px){.baton{grid-template-columns:1fr;gap:10px}}
.baton .who{background:var(--paper2);padding:12px 14px;border-top:2px solid var(--black)}
.baton .who.in{border-top-color:var(--red)}
.baton .lab{display:block;font-family:var(--ui);font-size:10.5px;font-weight:600;
 letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);margin-bottom:4px}
.baton .who b{display:block;font-size:1rem;font-weight:600;letter-spacing:-.01em}
.baton .who b a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line)}
.baton .who b a:hover{color:var(--red);border-color:var(--red)}
.baton .who span.d{display:block;font-size:.83rem;color:var(--ink2);margin-top:3px}
.baton .arrow{align-self:center;color:var(--red);font-size:1.3rem;line-height:1}
@media(max-width:640px){.baton .arrow{display:none}}
.plist{list-style:none;padding:0;margin:10px 0 0;
 display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px 30px}
.plist li{font-size:.93rem;line-height:1.4;break-inside:avoid}
.plist li a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line)}
.plist li a:hover{color:var(--red);border-color:var(--red)}
.plist li span{display:block;font-size:.82rem;color:var(--ink3)}
.roll{margin:12px 0 0;padding:0 0 0 3.1rem;columns:2;column-gap:38px;font-size:.93rem}
@media(max-width:700px){.roll{columns:1}}
.roll li{margin:0 0 8px;break-inside:avoid;padding-left:4px}
.roll li::marker{font-family:var(--mono);font-size:.8rem;color:var(--ink3)}
.roll li a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line)}
.roll li a:hover{color:var(--red);border-color:var(--red)}
.roll li b{color:var(--red);font-weight:600;margin-left:4px;cursor:help}
.roll li span{display:block;font-size:.8rem;color:var(--ink3);font-variant-numeric:tabular-nums}
"""

# The four handovers, written out because there are four of them and each is a
# different kind of ending. Keyed by year and checked against the record at build
# time, so a case that leaves the data cannot leave a paragraph behind.
HANDOVERS = {
    "1981-82": (
        "The first mid-year handover in the record",
        "Marcel Bush resigned the presidency on 14 January 1982, in the same week the "
        "Herald ran a retrospective in which he listed the autumn's higher-education "
        "rally among his achievements. David Payne, his administrative vice president, "
        "took over for the balance of the year; the Board of Regents minutes of 30 "
        "January name Payne the new president. The Board seat did not travel with the "
        "office. Bush had held it, Payne did not, and it went instead to a campus-wide "
        "special election in February, which Sandra Norfleet won for a term the Herald "
        "measured at two months."),
    "2004-05": (
        "A resignation, a summer with an acting president, and a second election",
        "Nick Todd was elected in March 2004 and sworn in on 27 April, days after the "
        "judicial council found $611 missing from an SGA dining account. He resigned "
        "that July, citing personal conflicts within the association, after the "
        "university's internal auditor reported more than $800 of questionable "
        "purchases and recommended he repay them. His executive vice president, Katie "
        "Dawson, filled the office through the summer. Patti Johnson, the previous "
        "year's executive vice president, was the only student to come forward and won "
        "the special election of 14 and 15 September, saying she ran because of the "
        "turmoil within the organisation. Three people held the presidency in twelve "
        "months, and the plaque records one."),
    "2006-07": (
        "A resignation read into the minutes, and a seat left empty",
        "SGA's senate minutes for 28 November 2006 record Rob Watkins's resignation as "
        "president and student regent being read to the chamber, with senators told "
        "that Jeanne Johnson would be sworn in at the Winter Banquet on 5 December. The "
        "minutes of that meeting list the executive vice presidency as vacant because "
        "she had moved up. The Board seat did not pass with the presidency and Western "
        "went about two months without a student on its governing board: Johnson spoke "
        "against a tuition increase at the January meeting without a vote, then won the "
        "seat in a special election the following week."),
    "2008-09": (
        "A president who resigned, and a successor who did not take the seat",
        "Johnathon Boles resigned on 30 January 2009 for health reasons. Kayla Shelton, "
        "his executive vice president, became president but not student regent, so the "
        "seat stood empty for 26 days until Reagan Gilley won a special election on 25 "
        "and 26 February, beating Nate Eaton 477 to 224. It is the clearest case in the "
        "record of the two offices coming apart, and the year carries three names."),
}


def _leader_link(name, yid, extra=""):
    return (f'<b><a href="y/{h(yid)}.html#{slug(name)}">{h(name)}</a></b>'
            + (f'<span class="d">{extra}</span>' if extra else ""))


def render_irregular(ys):
    """The presidents the plaque's one-name-per-year format cannot show."""
    by_year = {y["id"]: y for y in ys}

    # who left early, and who finished, taken from the order of names in a year
    handovers = []
    for y in ys:
        pres = [l for l in y["leaders"] if l["role"] == "president"]
        if len(pres) > 1:
            handovers.append((y["id"], pres))

    hblocks = []
    for yid, pres in handovers:
        head, body = HANDOVERS.get(
            yid, (f"The presidency changed hands during {yid}",
                  "The record carries more than one president for this year."))
        cells = []
        for i, l in enumerate(pres):
            role = ("Elected, left early" if i == 0 else
                    ("Filled the office" if l.get("acting") else "Finished the year"))
            cells.append(f'<div class="who{"" if i == 0 else " in"}">'
                         f'<span class="lab">{role}</span>'
                         f'{_leader_link(l["name"], yid, role_word(l, by_year[yid]))}</div>')
        baton = '<div class="arrow">&rarr;</div>'.join(cells)
        hblocks.append(
            f'<article class="hand"><p class="yr">{h(yid)}</p><h3>{h(head)}</h3>'
            f'<p>{h(body)}</p><div class="baton">{baton}</div></article>')

    def plist(items):
        return ('<ul class="plist">'
                + "".join(f'<li><a href="y/{h(yid)}.html#{slug(n)}">{h(n)}</a>'
                          f'<span>{h(note)}</span></li>' for n, yid, note in items)
                + "</ul>")

    # people the wall does not carry, setting aside the year still running
    plated = {l["name"] for y in ys for l in y["leaders"]
              if not l.get("missing_from_plaque")}
    noplate = []
    for y in ys:
        for l in y["leaders"]:
            if not l.get("missing_from_plaque") or l.get("current") or y["id"] == ys[-1]["id"]:
                continue
            if l["role"] == "regent":
                why = "held the Board seat, no plate anywhere on the wall"
            elif l["name"] in plated:
                why = f"no plate for {y['id']}; plated only for the later term"
            else:
                why = "no plate anywhere on the wall"
            noplate.append((l["name"], y["id"], why))

    twice = {}
    for y in ys:
        for l in y["leaders"]:
            if l["role"] == "president":
                twice.setdefault(l["name"], []).append(y["id"])
    twice = [(n, v[0], "served " + " and ".join(v)) for n, v in twice.items() if len(v) > 1]

    regents = {}
    for y in ys:
        for l in y["leaders"]:
            if l["role"] == "regent":
                regents.setdefault(l["name"], []).append(y["id"])
    regents = [(n, v[0], "held the Board seat " + " and ".join(v) + ", never the presidency")
               for n, v in regents.items()]

    unresolved = [(l["name"], y["id"], "office not established")
                  for y in ys for l in y["leaders"] if l["role"] == "unresolved"]

    n_pres = len({l["name"] for y in ys for l in y["leaders"] if l["role"] == "president"})

    # the whole line, first term first, with the irregular ones marked
    odd_years = {yid for yid, _ in handovers}
    seen_p = {}
    roll_items = []
    for y in ys:
        for l in y["leaders"]:
            if l["role"] != "president" or l["name"] in seen_p:
                continue
            seen_p[l["name"]] = True
            terms = [z["id"] for z in ys
                     for m in z["leaders"] if m["name"] == l["name"] and m["role"] == "president"]
            odd = y["id"] in odd_years or l.get("acting")
            note = " and ".join(terms)
            if l.get("acting"):
                note += ", acting"
            star = ('<b title="term began or ended out of the ordinary">*</b>'
                    if odd else '')
            roll_items.append(
                f'<li><a href="y/{h(y["id"])}.html#{slug(l["name"])}">{h(l["name"])}</a>'
                f'{star}<span>{h(note)}</span></li>')
    roll = "".join(roll_items)

    body = f"""
<header class="head"><div class="wrap">
 <p class="kicker">The terms that did not run to the pattern</p>
 <h1>Irregular terms</h1>
 <p class="scope">Student government elects a president in April and that person serves the
 following academic year. Most of the {n_pres} people who have held the office did exactly
 that. This page is for the ones who did not: the four who left before their year was out,
 the people who finished those years in their place, the one who filled the office without
 ever being elected to it, and the term a pandemic stretched by five months.</p>
 <p class="scope">They are gathered here because the ordinary record cannot hold them. The
 plaque in the SGA Chambers gives one name to each year, and so does every list written
 afterwards, including the university's own. A format like that cannot show a year in which
 the presidency changed hands, so the people who finished those years drop quietly out of
 the count. This archive counts them. Anyone who held the office held it, and a week counts
 as much as a year.</p>
</div></header>

<div class="wrap"><div class="body">

<h2 class="sec">The handovers<span class="n">{len(hblocks)}</span></h2>
<p class="secnote">Four times in sixty years a president has left before the year ended.
Each time somebody finished it.</p>
{"".join(hblocks)}

<h2 class="sec">Filled the office without being elected to it</h2>
<p class="secnote">One person in the record held the presidency without ever having won it.</p>
{plist([(l["name"], y["id"], "acting president, " + y["id"])
        for y in ys for l in y["leaders"] if l.get("acting")])}

<h2 class="sec">A term the pandemic extended</h2>
<div class="prose">
<p>SGA voted on 20 April 2020 to postpone its spring election because the campus had closed
for COVID-19, and passed an emergency clause letting cabinet terms run on until the next
election under judicial oversight. Will Harris stayed in office through the summer and was
still president when the senate met for the first time since April on 15 September. Garrett
Edmonds was not elected to succeed him until 29 September and took office in October. It is
the only year in the record with no spring handover, and it is an extension rather than a
second term, so Harris is counted once.</p>
</div>

<h2 class="sec">No plate on the wall<span class="n">{len(noplate)}</span></h2>
<p class="secnote">Held the office, or the Board seat, and the Chambers wall does not say so.
Two of them appear on it only for a later term they went on to win in their own right.</p>
{plist(noplate)}

<h2 class="sec">Held the seat but never the presidency<span class="n">{len(regents)}</span></h2>
<p class="secnote">The student seat on the Board of Regents was separately elected from 1968.
In most years the president held it too, but not in these.</p>
{plist(regents)}

<h2 class="sec">Two terms<span class="n">{len(twice)}</span></h2>
<p class="secnote">Counted once each, at the first term. Two plates for one person is not two
presidents, which is also why a changed surname has to be checked before anyone is added.</p>
{plist(twice)}

<h2 class="sec">Still unsettled</h2>
<p class="secnote">A name on the wall the archive cannot place in an office.</p>
{plist(unresolved) if unresolved else '<p class="prose">Nothing outstanding.</p>'}

<h2 class="sec">Every president, in order<span class="n">{n_pres}</span></h2>
<p class="secnote">The whole line, counting people rather than years. Somebody who served
twice is counted once, at their first term. An asterisk marks the terms this page is about:
the ones that began or ended somewhere other than the usual spring handover.</p>
<ol class="roll">{roll}</ol>

<div class="prose" style="margin-top:34px">
<p>Where a name here differs from the plaque, the difference and the evidence that settled it
are on the <a href="corrections.html">corrections page</a>. How the count is kept, and what
makes somebody a president for the purposes of this archive, is set out
<a href="about.html">on the about page</a>.</p>
</div>

</div></div>"""
    desc = (f"The WKU student body presidents whose terms did not run to the pattern: the four "
            f"who resigned mid-year, the people who finished those years, the acting president, "
            f"and the term extended by COVID-19.")
    return shell("Irregular terms · SGA 60", desc, body, IRREGULAR_CSS,
                 depth=0, current="irregular.html")


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
    index_anchors(ys)
    index_offices(ys)
    gaps = seat_gaps(ys)
    if gaps:
        print('the Board seat is unidentified in: ' + ', '.join(gaps))
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

    (SITE / "index.html").write_text(repair_anchors(render_index(ys, len(leg), n_herald)))
    for i, y in enumerate(ys):
        (YDIR / f'{y["id"]}.html').write_text(repair_anchors(
            render_year(y, ys[i - 1] if i else None,
                        ys[i + 1] if i < len(ys) - 1 else None,
                        by_session.get(y["id"], ()), repeats)))
    hist = render_history(ys, herald)
    for path, page in hist.items():
        (SITE / path).write_text(repair_anchors(page))
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
    (SITE / "story.html").write_text(repair_anchors(render_story(ys)))
    (SITE / "patterns.html").write_text(repair_anchors(render_patterns(ys)))
    (SITE / "events.html").write_text(repair_anchors(render_programs(ys)))
    (SITE / "irregular.html").write_text(repair_anchors(render_irregular(ys)))
    (SITE / "legislation.html").write_text(render_legislation(leg))
    (SITE / "corrections.html").write_text(repair_anchors(render_corrections(ys)))

    n_port = sum(1 for y in ys for l in y["leaders"] if l.get("photo"))
    n_gal = sum(len(y.get("photos") or []) for y in ys)
    n_docs = sum(len(y.get("documents") or []) for y in ys)
    (SITE / "about.html").write_text(repair_anchors(
        render_about(ys, meta, len(leg), n_herald, n_docs, n_port, n_gal)))
    (SITE / "sources.html").write_text(repair_anchors(
        render_sources(ys, leg, herald, n_docs, n_port, n_gal)))

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

    # Say so loudly if the record broke its own rules. The build still runs, so
    # a page is never held hostage to a bad citation, but it does not get to
    # finish quietly either.
    checker = Path(__file__).with_name("check_data.py")
    if checker.exists():
        r = subprocess.run([sys.executable, str(checker), "--quiet"],
                           capture_output=True, text=True)
        if r.returncode:
            print("\n!! the archive does not check out against its own rules:")
            print(r.stdout.strip() or r.stderr.strip())
            print("!! run python3 scripts/check_data.py for the detail")


if __name__ == "__main__":
    main()
