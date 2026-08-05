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

/* ---- the story, on the front page ---- */
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


# ---------------------------------------------------------------- pieces
REGENT_SEAT_CREATED = 1968


def held_both(l, y):
    """The student seat on the Board of Regents has existed since April 1968 and
    has never gone away. In most years the elected president also holds it, so a
    lone name on the plaque means one person in both offices. The years that
    carry two names are the exceptions, when someone other than the president
    held the seat - usually because the president was ineligible."""
    return (l["role"] == "president" and len(y["leaders"]) == 1
            and y["start"] >= REGENT_SEAT_CREATED)


def role_word(l, y=None):
    if l["role"] == "regent":
        return "student regent"
    if l["role"] == "unresolved":
        return "role unresolved"
    if y is not None and held_both(l, y):
        return "president and student regent"
    return "president"


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

    counts = {"all": len(ys),
              "disputed": sum(1 for y in ys if disputed(y)),
              "corrected": sum(1 for y in ys if corrected(y)),
              "unconfirmed": sum(1 for y in ys if unconfirmed(y)),
              "regent": sum(1 for y in ys
                            if any(l["role"] == "regent" for l in y["leaders"]))}
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
            if any(l["role"] == "regent" for l in y["leaders"]):
                tags.append("regent")
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
                + (" &middot; ".join(
                    f'{h(l["name"])}<span class="ro">{h(role_word(l, y))}</span>'
                    for l in y["leaders"])
                   if len(names) > 1 else h(names[0])) + '</span>'
                f'<span class="ct">{n} entries</span>{flag}</a>')
        ev = sum(len(y["events"]) for y in block)
        groups.append(
            f'<section class="decade" data-dec="d{lo}"><div class="dechead">'
            f'<h2>{h(label)}</h2><span class="c">{len(block)} years, {ev} entries</span></div>'
            f'<div class="grid">{"".join(plates)}</div></section>')

    facets = [("all", "All years")]
    if counts["regent"]:
        facets.append(("regent", "Offices held by two people"))
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
 <a class="readfirst" href="story.html">
  <p class="lab">Start here</p>
  <h2>The story</h2>
  <p>Sixty years of student government at Western Kentucky University, read straight through:
  the fight for a seat on the Board of Regents, the concert losses that nearly cost it the job, the
  gazebo that was never built, the resolution that drew national coverage and was rejected
  within days. Every claim links back to the year it came from.</p>
  <span class="go">Read the narrative</span>
 </a>

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
        f"All {len(ys)} academic years have a page. {n_ev} entries are sourced to the "
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
            if e.get("src", {}).get("file"):
                cites.append(f'<a href="{up}docs/{h(e["src"]["file"])}">Read it here</a>')
            tag = '<span class="tag">campus</span>' if e.get("campus") else ""
            rows.append(
                f'<article class="hx" id="{h(yid)}-{aid}" data-k="e">'
                f'<div class="when">{hx_date(e["date"])}{tag}</div>'
                f'<div class="t"><h3>{h(e["title"])}</h3><p>{h(e["body"])}</p>'
                f'<p class="cite">{"".join(cites)}</p></div></article>')
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
   var r=rows[i],isx=r.dataset.k==='i',
       ok=(kind==='all'||(kind==='e')===!isx)&&(!q||r._k.indexOf(q)>-1);
   r.hidden=!ok;
   if(ok){if(isx)vi++;else ve++;}
  }
  var d=sec.querySelector('details.hidx');
  if(d){d.hidden=!vi;d.open=!!(q&&vi);
   var c=d.querySelector('.hn');if(c)c.textContent=vi;}
  var none=sec.querySelector('.hxnone');
  if(none)none.hidden=!!q||kind==='i';
  sec.hidden=!(ve+vi)&&!(!q&&kind==='all');
  if(jumps[sec.dataset.y])jumps[sec.dataset.y].classList.toggle('off',sec.hidden);
  ne+=ve;ni+=vi;if(ve+vi)ny++;
 });
 var counted=[];
 if(kind!=='i'&&(ne||!q))counted.push(word(ne,'entry','entries'));
 if(kind!=='e'&&(ni||!q))counted.push(word(ni,'index line','index lines'));
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
if(p0.get('show')==='e'||p0.get('show')==='i'){kind=p0.get('show');
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
    n_ev, n_hx = counts
    facets = [("all", "Everything", n_ev + n_hx), ("e", "Archive entries", n_ev),
              ("i", "Herald index", n_hx)]
    chips = "".join(
        f'<button type="button" data-k="{k}" '
        f'aria-pressed="{"true" if k == "all" else "false"}">{h(lab)} '
        f'<span class="c">{n}</span></button>' for k, lab, n in facets if n or k != "i")
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
                sum(len(x["lines"]) for y in block for x in by_year[y["id"]]["herald"]))

    def nav_items(block):
        return [(y["id"], len(by_year[y["id"]]["events"])) for y in block]

    n_ev, n_hx = tally(ys)
    lede = (f"Every sourced entry in the archive, {n_ev} of them, in the order they "
            f"happened, with the {n_hx} unworked lines from the <cite>Herald</cite> index "
            f"kept separate under the year they belong to. Jump to a year below, or read "
            f"one decade at a time.")
    pages = {}
    rows = []
    for lo, hi, label, short, stem in DECADES:
        block = [y for y in ys if lo <= y["start"] <= hi]
        if block:
            rows.append((short, nav_items(block)))
    body = (timeline_head("The complete timeline", "1966 to 2026", lede, "", None,
                          (n_ev, n_hx), year_nav(rows, True))
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
        ev, hxn = tally(block)
        d_lede = (f"{ev} sourced entries across {len(block)} academic years, "
                  f"{block[0]['id']} to {block[-1]['id']}, with {hxn} further lines from "
                  f"the <cite>Herald</cite> index held under the years they belong to.")
        pager = ""
        if i:
            p = DECADES[i - 1]
            pager += (f'<a href="{p[4]}.html">Previous decade<b>{h(p[3])}</b></a>')
        if i < len(DECADES) - 1:
            nx = DECADES[i + 1]
            pager += (f'<a class="r" href="{nx[4]}.html">Next decade<b>{h(nx[3])}</b></a>')
        dbody = (timeline_head(label, "The timeline", d_lede, "../", lo,
                               (ev, hxn), year_nav([("Years", nav_items(block))], False))
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
About thirteen students turned up to the meeting for prospective candidates; Patti Johnson, the
sitting executive vice president, was the only one interested, and
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

<p>Two votes three months apart taught the organization the limits of consent. On 24 September
2015 the senate voted 21-4 to
<a href="y/2015-16.html#e-20150924-1">disapprove the process by which the Confucius Institute
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
<a href="y/2014-15.html">changed her surname in mid-term</a>. Hargroave, Mollozzi, Keyana or
Keyanna: doubtful spellings are flagged on the year pages, not fixed.</p>

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

<p class="storyfoot">Every fact above is drawn from a dated, sourced entry on this site. The
<a href="history.html">complete timeline</a> holds all __NEV__ of them in order; the
<a href="index.html">board</a> holds every year; the <a href="sources.html">sources page</a>
sets out what each collection covers and where it fails.</p>

</div>
</section>

</div></div>
"""


def render_story(ys):
    n_ev = sum(len(y["events"]) for y in ys)
    body = STORY_BODY.replace("__NEV__", f"{n_ev:,}")
    desc = ("Sixty years of student government at Western Kentucky University read as one "
            "continuous narrative, from the 1966 constitution to the 2026 election, with "
            "every claim linked to the year it came from.")
    return shell("The story · SGA 60", desc, body, STORY_CSS, depth=0, current="story.html")


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
<p>So a single name on the plaque after 1968 means one person holding both offices. Two names
mean the offices were split that year, and there are six such years in this record: 1968-69
and 1969-70 (Paul Gerard), 1972-73 (Michael Fiorella), 1974-75 (Gregory McKinney), 1982-83
(Sandra Norfleet), and 2008-09, when Johnathon Boles resigned the presidency in January 2009,
Kayla Shelton succeeded him without taking the Board seat, and Reagan Gilley won it in a
special election the following month.</p>
</div>

<h2 class="sec">Scope and content</h2>
<div class="prose">
<p>The archive holds one page for each of the {len(ys)} academic years from {h(ys[0]["id"])} to
{h(ys[-1]["id"])}, {n_ev} dated entries, and {n_lead} presidents and student regents with
their terms as far as the record supports them. Entries cover the organization, not only its presidents: elections and turnout,
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
    (SITE / "story.html").write_text(render_story(ys))
    (SITE / "legislation.html").write_text(render_legislation(leg))
    (SITE / "corrections.html").write_text(render_corrections(ys))

    n_port = sum(1 for y in ys for l in y["leaders"] if l.get("photo"))
    n_gal = sum(len(y.get("photos") or []) for y in ys)
    n_docs = sum(len(y.get("documents") or []) for y in ys)
    (SITE / "about.html").write_text(
        render_about(ys, meta, len(leg), n_herald, n_docs, n_port, n_gal))
    (SITE / "sources.html").write_text(
        render_sources(ys, leg, herald, n_docs, n_port, n_gal))

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
