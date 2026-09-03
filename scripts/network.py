#!/usr/bin/env python3
"""The people of SGA as a graph you can walk.

Sixty years of rosters are a filing cabinet: to find out who somebody sat with
you have to open their year, read a list, and open each name in it. The link
that matters most to a reader — who was in the room with them — is the one the
archive never draws.

This draws it. Every person is a point, every year is an anchor, and a person
sits near the years they served. Ask for anyone and the graph moves to them and
lights up everyone who held office alongside them.

The edges are not shipped. Two people are connected when they share a year, and
across sixty years that is roughly a hundred thousand pairs, most of them in a
handful of very large senates. Sending that list would be a several-megabyte
download to draw a hairball nobody can read. Instead each person carries the
years they served, and the cohort is worked out in the browser for the one
person being looked at, which is the only cohort anyone ever sees.

The layout is computed here rather than in the browser so the page opens with
the graph already settled instead of writhing for five seconds, and so it looks
the same every time it is built.
"""

import json
import math
import random


def _anchors(years):
    """One point per academic year, oldest at the centre, spiralling outward.

    A ring would put 1966 next to 2026 and imply a closeness that is the
    artefact of a circle. A spiral keeps time monotonic: distance from the
    centre is age, so the eye reads the shape as a chronology.
    """
    out, n = {}, max(len(years), 1)
    for i, y in enumerate(years):
        t = i / n
        ang = t * math.tau * 3.2                 # three turns across sixty years
        r = 120 + 900 * math.sqrt(t)
        out[y] = (math.cos(ang) * r, math.sin(ang) * r)
    return out


def _relax(pos, home, rounds=140, repel=520.0, pull=0.055):
    """Push points apart so names do not stack, without letting them drift.

    Pure repulsion turns the spiral into a disc and loses the chronology, so
    every point is also sprung back to the middle of the years it served. The
    repulsion is only computed against points in neighbouring grid cells: all
    pairs is 1.7 million comparisons a round and does not finish.
    """
    keys = list(pos)
    cell = 46.0
    for _ in range(rounds):
        grid = {}
        for k in keys:
            x, y = pos[k]
            grid.setdefault((int(x // cell), int(y // cell)), []).append(k)
        for k in keys:
            x, y = pos[k]
            gx, gy = int(x // cell), int(y // cell)
            fx = fy = 0.0
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for j in grid.get((gx + dx, gy + dy), ()):
                        if j == k:
                            continue
                        ox, oy = pos[j]
                        vx, vy = x - ox, y - oy
                        d2 = vx * vx + vy * vy
                        if d2 < 1e-6:
                            vx, vy, d2 = random.random() - .5, random.random() - .5, .25
                        if d2 < cell * cell * 4:
                            f = repel / d2
                            fx += vx * f
                            fy += vy * f
            hx, hy = home[k]
            fx += (hx - x) * pull
            fy += (hy - y) * pull
            m = math.hypot(fx, fy)
            if m > 14:                            # a long step overshoots and rings
                fx, fy = fx * 14 / m, fy * 14 / m
            pos[k] = (x + fx, y + fy)
    return pos


def layout(people, years):
    """Fixed positions for everyone, plus the year anchors to label them with."""
    random.seed(60)                               # same graph on every build
    anch = _anchors(years)
    home, pos = {}, {}
    for name, p in people.items():
        ys = [y for y in p["years"] if y in anch]
        if not ys:
            continue
        hx = sum(anch[y][0] for y in ys) / len(ys)
        hy = sum(anch[y][1] for y in ys) / len(ys)
        home[name] = (hx, hy)
        pos[name] = (hx + random.uniform(-30, 30), hy + random.uniform(-30, 30))
    _relax(pos, home)
    return pos, anch


def payload(people, years):
    """Everything the page needs, in the smallest shape that stays readable.

    Field names are single letters and coordinates are rounded to whole pixels;
    the graph is a thousand-odd people and the difference between this and the
    obvious spelling is most of a megabyte over the wire.
    """
    pos, anch = layout(people, years)
    yi = {y: i for i, y in enumerate(years)}
    nodes = []
    for name, p in sorted(people.items()):
        if name not in pos:
            continue
        x, y = pos[name]
        nodes.append({
            "n": name,
            "s": p["slug"],
            "y": sorted(yi[v] for v in p["years"] if v in yi),
            "o": p["office"],
            "p": 1 if p["president"] else 0,
            "r": 1 if p.get("regent") else 0,
            "f": p.get("photo") or "",
            "x": round(x),
            "z": round(y),
        })
    return {
        "years": years,
        "anchors": [[round(anch[y][0]), round(anch[y][1])] for y in years],
        "nodes": nodes,
    }


if __name__ == "__main__":
    print(json.dumps({"note": "imported by build.py"}))


NETWORK_CSS = """
:root{--ink:#0B0B0C;--pap:#F7F5F2;--red:#9E1B32;--dim:#8A8A8F}
.netwrap{position:fixed;inset:0;top:var(--navh,56px);background:
  radial-gradient(1200px 800px at 50% 42%,#15161A 0%,#0B0B0C 62%,#070708 100%);
  overflow:hidden;touch-action:none}
#net{display:block;width:100%;height:100%;cursor:grab}
#net.drag{cursor:grabbing}
.netui{position:absolute;z-index:5;font:500 13px/1.45 ui-sans-serif,-apple-system,"Segoe UI",system-ui,sans-serif}
.netsearch{top:18px;left:18px;width:min(330px,calc(100vw - 36px))}
.netsearch input{width:100%;padding:11px 14px;border-radius:11px;
  border:1px solid #2A2C33;background:rgba(18,19,23,.92);color:#EFEFF2;
  font:500 14px/1.2 inherit;outline:none;backdrop-filter:blur(14px);
  box-shadow:0 10px 34px rgba(0,0,0,.55)}
.netsearch input:focus{border-color:var(--red);box-shadow:0 0 0 3px rgba(158,27,50,.22),0 10px 34px rgba(0,0,0,.55)}
.netsearch input::placeholder{color:#6B6D77}
.hits{margin-top:7px;max-height:46vh;overflow:auto;border-radius:11px;
  background:rgba(18,19,23,.96);border:1px solid #2A2C33;backdrop-filter:blur(14px);
  box-shadow:0 16px 44px rgba(0,0,0,.6)}
.hits:empty{display:none}
.hits b{display:block;padding:9px 13px;cursor:pointer;color:#E7E7EC;font-weight:500;
  border-bottom:1px solid #212228}
.hits b:last-child{border-bottom:0}
.hits b:hover,.hits b.on{background:#22242B}
.hits b i{display:block;color:#82848E;font-style:normal;font-size:11.5px;margin-top:1px}
.card{top:18px;right:18px;width:min(320px,calc(100vw - 36px));border-radius:14px;
  background:rgba(18,19,23,.96);border:1px solid #2A2C33;color:#E7E7EC;
  backdrop-filter:blur(14px);box-shadow:0 18px 50px rgba(0,0,0,.62);
  opacity:0;transform:translateY(-6px);pointer-events:none;transition:.18s ease}
.card.on{opacity:1;transform:none;pointer-events:auto}
.card .pad{padding:15px 16px}
.card h3{margin:0 0 2px;font:600 17px/1.25 ui-serif,Georgia,serif;color:#fff}
.card .sub{color:#8A8C96;font-size:12px;margin-bottom:11px}
.card .who{display:flex;gap:11px;align-items:flex-start}
.card img{width:54px;height:54px;border-radius:9px;object-fit:cover;flex:none;
  background:#26272E;border:1px solid #34363E}
.card .mates{border-top:1px solid #24252C;max-height:32vh;overflow:auto}
.card .mates a{display:block;padding:7px 16px;color:#C9CAD2;text-decoration:none;font-size:12.5px}
.card .mates a:hover{background:#22242B;color:#fff}
.card .mates a span{color:#7C7E88;float:right;font-size:11px}
.card .go{display:block;margin:11px 16px 15px;padding:9px;text-align:center;
  background:var(--red);color:#fff;border-radius:9px;text-decoration:none;font-weight:600;font-size:13px}
.card .go:hover{background:#B02039}
.card .x{position:absolute;top:9px;right:11px;color:#74767F;cursor:pointer;font-size:19px;line-height:1}
.card .x:hover{color:#fff}
.legend{bottom:18px;left:18px;color:#7E808A;font-size:11.5px;max-width:280px}
.legend b{color:#B9BAC3;font-weight:600}
.zoomui{bottom:18px;right:18px;display:flex;gap:7px}
.zoomui button{width:34px;height:34px;border-radius:9px;border:1px solid #2A2C33;
  background:rgba(18,19,23,.92);color:#C9CAD2;font-size:16px;cursor:pointer;
  backdrop-filter:blur(14px)}
.zoomui button:hover{background:#22242B;color:#fff}
@media (max-width:720px){.card{top:auto;bottom:18px;right:18px;left:18px;width:auto}
 .legend{display:none}}
"""


def network_page(data):
    """The graph page. One canvas, no libraries, no network calls."""
    blob = json.dumps(data, separators=(",", ":"))
    return """
<div class="netwrap">
<canvas id="net"></canvas>

<div class="netui netsearch">
  <input id="q" type="search" autocomplete="off" spellcheck="false"
         placeholder="Find anyone who held office, 1966 to today">
  <div class="hits" id="hits"></div>
</div>

<div class="netui card" id="card">
  <span class="x" id="cx">&times;</span>
  <div class="pad">
    <div class="who"><img id="cimg" alt="" hidden>
      <div><h3 id="cname"></h3><div class="sub" id="csub"></div></div></div>
  </div>
  <div class="mates" id="cmates"></div>
  <a class="go" id="cgo" href="#">Open their record</a>
</div>

<div class="netui legend">
  <b>Every person the record shows in office.</b> Colour is the decade they
  started; the ringed points are presidents and student regents. Drag to move,
  scroll to zoom, click anyone to light up everyone who served alongside them.
</div>

<div class="netui zoomui">
  <button id="zin" title="Zoom in">+</button>
  <button id="zout" title="Zoom out">&minus;</button>
  <button id="zfit" title="Fit the whole web">&#9633;</button>
</div>
</div>

<script>
(function(){
"use strict";
const D = __DATA__;
const cv = document.getElementById("net"), cx = cv.getContext("2d");
const N = D.nodes, YEARS = D.years;

// Decade of first service. A continuous ramp reads as one blur; six steps let
// the eye separate the sixties from the nineties at a glance.
const PAL = ["#5B8DEF","#3FB8AF","#7BC96F","#E8B84B","#E8834B","#D9536F"];
function tone(n){
  const y = YEARS[n.y[0]] ? +YEARS[n.y[0]].slice(0,4) : 1966;
  return PAL[Math.max(0, Math.min(5, Math.floor((y-1966)/10)))];
}
N.forEach(n => { n.c = tone(n); n.R = 2.6 + Math.min(n.y.length,8)*0.62 + (n.p?2.1:0); });

// Who sat with whom. Built once as year -> people, then read for one person at
// a time; the full pair list is ~100k edges and pointless to hold.
const BYYEAR = new Map();
N.forEach((n,i) => n.y.forEach(y => { if(!BYYEAR.has(y)) BYYEAR.set(y,[]); BYYEAR.get(y).push(i); }));
function cohortOf(i){
  const seen = new Map();
  for(const y of N[i].y) for(const j of BYYEAR.get(y)||[])
    if(j!==i) seen.set(j,(seen.get(j)||0)+1);
  return seen;
}

let cam = {x:0, y:0, k:0.5}, want = Object.assign({}, cam);
let sel = -1, hov = -1, cohort = new Map(), dragging = false, moved = false;
let px = 0, py = 0, DPR = 1;

function size(){
  DPR = Math.min(window.devicePixelRatio||1, 2);
  cv.width = cv.clientWidth*DPR; cv.height = cv.clientHeight*DPR;
}
function fit(){
  let a=1e9,b=1e9,c=-1e9,d=-1e9;
  N.forEach(n=>{a=Math.min(a,n.x);b=Math.min(b,n.z);c=Math.max(c,n.x);d=Math.max(d,n.z);});
  const w=cv.clientWidth, h=cv.clientHeight, pad=70;
  want.k = Math.min((w-pad*2)/(c-a||1),(h-pad*2)/(d-b||1));
  want.x = (a+c)/2; want.y = (b+d)/2;
}
const S = (n)=>({x:(n.x-cam.x)*cam.k + cv.clientWidth/2, y:(n.z-cam.y)*cam.k + cv.clientHeight/2});

// Redraw when something changes, and stop when it does not. A permanent
// animation frame loop holds the main thread at full tilt for a picture that
// is not moving: it drains a laptop battery, and it starves anything else the
// page or the browser wants to do.
let raf = 0, dirty = true;
function invalidate(){ dirty = true; if(!raf) raf = requestAnimationFrame(draw); }

function draw(){
  raf = 0;
  // ease the camera rather than jumping; a search that teleports loses the
  // reader's sense of where they were
  const dx0 = want.x-cam.x, dy0 = want.y-cam.y, dk0 = want.k-cam.k;
  const moving = Math.abs(dx0) > 0.4 || Math.abs(dy0) > 0.4 || Math.abs(dk0) > 0.0008;
  cam.x += dx0*0.16; cam.y += dy0*0.16; cam.k += dk0*0.16;
  if(!moving){ cam.x = want.x; cam.y = want.y; cam.k = want.k; }
  if(!dirty && !moving) return;
  dirty = false;
  const w = cv.clientWidth, h = cv.clientHeight;
  cx.setTransform(DPR,0,0,DPR,0,0);
  cx.clearRect(0,0,w,h);

  const focus = sel>=0 ? sel : hov;
  const lit = focus>=0 ? cohort : null;

  // year rings, faint, so the spiral of time is legible under the people
  if(cam.k > 0.16){
    cx.save(); cx.globalAlpha = Math.min(.5,(cam.k-.16)*1.5);
    cx.font = "600 10px ui-sans-serif,system-ui,sans-serif";
    cx.fillStyle = "#3A3C45"; cx.textAlign="center";
    D.anchors.forEach((a,i)=>{
      if(i%2) return;
      const p = S({x:a[0],z:a[1]});
      if(p.x<-60||p.x>w+60||p.y<-40||p.y>h+40) return;
      cx.fillText(YEARS[i], p.x, p.y);
    });
    cx.restore();
  }

  // edges only for the person in focus
  if(focus>=0){
    const o = S(N[focus]);
    cx.lineWidth = Math.max(.5, cam.k*0.9);
    lit.forEach((shared,j)=>{
      const p = S(N[j]);
      if((p.x<-200&&o.x<-200)||(p.x>w+200&&o.x>w+200)) return;
      const g = cx.createLinearGradient(o.x,o.y,p.x,p.y);
      const al = Math.min(.62, .16 + shared*0.13);
      g.addColorStop(0,"rgba(255,255,255,"+al+")");
      g.addColorStop(1, N[j].c + Math.round(al*150).toString(16).padStart(2,"0"));
      cx.strokeStyle = g;
      cx.beginPath(); cx.moveTo(o.x,o.y);
      const mx=(o.x+p.x)/2, my=(o.y+p.y)/2, dx=p.x-o.x, dy=p.y-o.y;
      cx.quadraticCurveTo(mx - dy*0.11, my + dx*0.11, p.x, p.y);
      cx.stroke();
    });
  }

  // people
  for(let i=0;i<N.length;i++){
    const n = N[i], p = S(n), r = Math.max(1.1, n.R*Math.sqrt(cam.k)*1.15);
    if(p.x<-30||p.x>w+30||p.y<-30||p.y>h+30) continue;
    const on = focus<0 || i===focus || (lit && lit.has(i));
    cx.globalAlpha = on ? 1 : 0.13;
    if(i===focus){
      cx.shadowColor = n.c; cx.shadowBlur = 22*Math.min(1.6,cam.k+.5);
    }
    cx.beginPath(); cx.arc(p.x,p.y,r,0,6.2832);
    cx.fillStyle = i===focus ? "#FFFFFF" : n.c; cx.fill();
    cx.shadowBlur = 0;
    if(n.p||n.r){                       // presidents and regents carry a ring
      cx.lineWidth = Math.max(.7, r*0.28);
      cx.strokeStyle = i===focus ? "#FFFFFF" : "rgba(255,255,255,.62)";
      cx.beginPath(); cx.arc(p.x,p.y,r+Math.max(1.6,r*0.5),0,6.2832); cx.stroke();
    }
    cx.globalAlpha = 1;
  }

  // names, once there is room for them
  const showAll = cam.k > 1.25;
  cx.font = "600 11px ui-sans-serif,system-ui,sans-serif";
  cx.textAlign = "center"; cx.textBaseline = "bottom";
  for(let i=0;i<N.length;i++){
    const n=N[i], big = n.p||n.r;
    const near = i===focus || (lit&&lit.has(i));
    if(!(showAll || (cam.k>0.62&&big) || near)) continue;
    const p = S(n); if(p.x<-90||p.x>w+90||p.y<-30||p.y>h+30) continue;
    const r = Math.max(1.1, n.R*Math.sqrt(cam.k)*1.15);
    cx.globalAlpha = (focus<0||near) ? (i===focus?1:.82) : .1;
    cx.lineWidth = 3.2; cx.strokeStyle = "rgba(7,7,8,.92)";
    cx.strokeText(n.n, p.x, p.y-r-3.5);
    cx.fillStyle = i===focus ? "#FFFFFF" : "#C6C7D0";
    cx.fillText(n.n, p.x, p.y-r-3.5);
    cx.globalAlpha = 1;
  }
  if(moving) raf = requestAnimationFrame(draw);
}

function pick(mx,my){
  let best=-1, bd=18*18;
  for(let i=0;i<N.length;i++){
    const p=S(N[i]), dx=p.x-mx, dy=p.y-my, d=dx*dx+dy*dy;
    if(d<bd){bd=d;best=i;}
  }
  return best;
}

const card=document.getElementById("card");
function open(i){
  sel = i; cohort = cohortOf(i);
  const n = N[i];
  document.getElementById("cname").textContent = n.n;
  const yrs = n.y.map(k=>YEARS[k]);
  document.getElementById("csub").textContent =
    (n.o||"Served") + " \\u00b7 " + (yrs.length>1 ? yrs[0]+" to "+yrs[yrs.length-1] : yrs[0]);
  const im = document.getElementById("cimg");
  if(n.f){ im.src = "photos/"+n.f; im.hidden=false; } else im.hidden=true;
  document.getElementById("cgo").href = "o/"+n.s+".html";
  const rows = [...cohort.entries()].sort((a,b)=>b[1]-a[1]||N[a[0]].n.localeCompare(N[b[0]].n));
  document.getElementById("cmates").innerHTML =
    '<a style="color:#8A8C96;cursor:default" onclick="return false">'
    + rows.length + ' held office alongside them</a>'
    + rows.slice(0,60).map(([j,c])=>'<a href="o/'+N[j].s+'.html">'+N[j].n
        +'<span>'+c+(c>1?" yrs":" yr")+'</span></a>').join("");
  card.classList.add("on");
  want.x = n.x; want.y = n.z; want.k = Math.max(want.k, 1.15);
  invalidate();
}
function shut(){ sel=-1; cohort=new Map(); card.classList.remove("on"); invalidate(); }
document.getElementById("cx").onclick = shut;

cv.addEventListener("pointerdown", e=>{
  dragging=true; moved=false; px=e.clientX; py=e.clientY;
  cv.setPointerCapture(e.pointerId); cv.classList.add("drag");
});
cv.addEventListener("pointermove", e=>{
  const r = cv.getBoundingClientRect();
  if(dragging){
    const dx=e.clientX-px, dy=e.clientY-py;
    if(Math.abs(dx)+Math.abs(dy)>3) moved=true;
    want.x -= dx/cam.k; want.y -= dy/cam.k;
    cam.x -= dx/cam.k; cam.y -= dy/cam.k;
    px=e.clientX; py=e.clientY; invalidate(); return;
  }
  const i = pick(e.clientX-r.left, e.clientY-r.top);
  if(i!==hov){ hov=i; if(sel<0) cohort = i>=0 ? cohortOf(i) : new Map(); invalidate(); }
  cv.style.cursor = i>=0 ? "pointer" : "grab";
});
cv.addEventListener("pointerup", e=>{
  dragging=false; cv.classList.remove("drag");
  if(moved) return;
  const r=cv.getBoundingClientRect();
  const i=pick(e.clientX-r.left,e.clientY-r.top);
  if(i>=0) open(i); else shut();
});
cv.addEventListener("wheel", e=>{
  e.preventDefault();
  const r=cv.getBoundingClientRect(), mx=e.clientX-r.left, my=e.clientY-r.top;
  const wx = (mx-cv.clientWidth/2)/cam.k + cam.x, wy = (my-cv.clientHeight/2)/cam.k + cam.y;
  want.k = Math.max(0.09, Math.min(7, want.k * Math.exp(-e.deltaY*0.0014)));
  want.x = wx - (mx-cv.clientWidth/2)/want.k;
  want.y = wy - (my-cv.clientHeight/2)/want.k;
  invalidate();
}, {passive:false});

document.getElementById("zin").onclick = ()=>{want.k=Math.min(7,want.k*1.45);invalidate();};
document.getElementById("zout").onclick = ()=>{want.k=Math.max(0.09,want.k/1.45);invalidate();};
document.getElementById("zfit").onclick = ()=>{shut();fit();invalidate();};

const q=document.getElementById("q"), hits=document.getElementById("hits");
let idx = N.map((n,i)=>[n.n.toLowerCase(),i]);
q.addEventListener("input", ()=>{
  const s=q.value.trim().toLowerCase();
  if(s.length<2){ hits.innerHTML=""; return; }
  const out = idx.filter(([t])=>t.includes(s))
    .sort((a,b)=>a[0].indexOf(s)-b[0].indexOf(s)||a[0].localeCompare(b[0])).slice(0,24);
  hits.innerHTML = out.map(([,i])=>{
    const n=N[i], y=n.y.map(k=>YEARS[k]);
    return '<b data-i="'+i+'">'+n.n+'<i>'+(n.o||"")+" \\u00b7 "
      +(y.length>1?y[0]+"\\u2013"+y[y.length-1]:y[0])+'</i></b>';
  }).join("");
});
hits.addEventListener("click", e=>{
  const b=e.target.closest("b"); if(!b) return;
  open(+b.dataset.i); hits.innerHTML=""; q.value="";
});
q.addEventListener("keydown", e=>{
  if(e.key!=="Enter") return;
  const b=hits.querySelector("b"); if(b){ open(+b.dataset.i); hits.innerHTML=""; q.value=""; }
});
window.addEventListener("keydown", e=>{ if(e.key==="Escape"){shut();hits.innerHTML="";} });

window.addEventListener("resize", ()=>{size();invalidate();});
size(); fit(); cam.k = want.k*0.55; invalidate();

// deep link: /network.html#name-slug opens straight onto that person
if(location.hash.length>1){
  const s=location.hash.slice(1), i=N.findIndex(n=>n.s===s);
  if(i>=0) setTimeout(()=>open(i), 120);
}
})();
</script>
""".replace("__DATA__", blob)
