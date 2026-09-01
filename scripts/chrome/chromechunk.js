// Fetch PDFs in a real browser, then pull the bytes back in slices so a large
// broadsheet issue never has to cross CDP as one giant base64 string.
//   node chromechunk.js <outdir> <name>=<url> [...]
const { spawn } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
// One debug port per process: the whole fleet may run this at once,
// and a second Chrome on a taken port attaches to the first one's
// tabs instead of its own, which corrupts both downloads.
const PORT = 9300 + (process.pid % 600);
const CHUNK = 512 * 1024;
const outdir = process.argv[2];
const jobs = process.argv.slice(3).map(s => {
  const i = s.indexOf('=');
  return { name: s.slice(0, i), url: s.slice(i + 1) };
});
const sleep = ms => new Promise(r => setTimeout(r, ms));
const log = (...a) => console.log(new Date().toTimeString().slice(0, 8), ...a);

class Session {
  constructor(ws) {
    this.ws = ws; this.id = 0; this.pending = new Map();
    ws.addEventListener('message', ev => {
      const m = JSON.parse(ev.data);
      if (m.id && this.pending.has(m.id)) {
        const { resolve, reject } = this.pending.get(m.id);
        this.pending.delete(m.id);
        m.error ? reject(new Error(JSON.stringify(m.error))) : resolve(m.result);
      }
    });
  }
  send(method, params = {}) {
    const id = ++this.id;
    this.ws.send(JSON.stringify({ id, method, params }));
    return new Promise((res, rej) => {
      this.pending.set(id, { resolve: res, reject: rej });
      setTimeout(() => { if (this.pending.delete(id)) rej(new Error('timeout ' + method)); }, 120000);
    });
  }
  async ev(expression, awaitPromise = false) {
    const r = await this.send('Runtime.evaluate',
      { expression, awaitPromise, returnByValue: true });
    return r.result ? r.result.value : undefined;
  }
}
const open = u => new Promise((res, rej) => {
  const ws = new WebSocket(u);
  ws.addEventListener('open', () => res(new Session(ws)));
  ws.addEventListener('error', () => rej(new Error('ws')));
});

(async () => {
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'sk-chunk-'));
  const chrome = spawn(CHROME, ['--no-first-run', '--no-default-browser-check',
    '--disable-extensions', '--mute-audio', '--window-size=1100,800',
    '--window-position=-3000,-3000', '--disable-blink-features=AutomationControlled',
    `--user-data-dir=${profile}`, `--remote-debugging-port=${PORT}`, 'about:blank'],
    { stdio: 'ignore' });

  let targets = null;
  for (let i = 0; i < 40; i++) {
    await sleep(500);
    try { targets = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json(); break; } catch (e) {}
  }
  if (!targets) { chrome.kill(); throw new Error('no chrome'); }
  const s = await open(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
  await s.send('Page.enable'); await s.send('Runtime.enable');

  await s.send('Page.navigate', { url: 'https://digitalcommons.wku.edu/' });
  await sleep(7000);
  log('warm', JSON.stringify(String(await s.ev('document.title')).slice(0, 50)));

  for (const j of jobs) {
    const dest = path.join(outdir, j.name);
    if (fs.existsSync(dest) && fs.statSync(dest).size > 150000) { log('have', j.name); continue; }
    let total;
    try {
      total = await s.ev(`
        (async () => {
          const r = await fetch(${JSON.stringify(j.url)}, {credentials:'include'});
          if (!r.ok) { window.__b = null; return -r.status; }
          window.__b = new Uint8Array(await r.arrayBuffer());
          return window.__b.length;
        })()`, true);
    } catch (e) { log('ERR', j.name, String(e).slice(0, 80)); continue; }

    if (!total || total < 0) { log('FAIL', j.name, 'status', total); await sleep(9000); continue; }
    log('fetched', j.name, Math.round(total / 1024) + 'KB, pulling in slices');

    const parts = [];
    let ok = true;
    for (let off = 0; off < total; off += CHUNK) {
      const b64 = await s.ev(`
        (() => {
          const b = window.__b.subarray(${off}, ${Math.min(off + CHUNK, total)});
          let s = ''; const C = 0x8000;
          for (let i = 0; i < b.length; i += C) s += String.fromCharCode.apply(null, b.subarray(i, i+C));
          return btoa(s);
        })()`);
      if (typeof b64 !== 'string') { ok = false; break; }
      parts.push(Buffer.from(b64, 'base64'));
      if (parts.length % 5 === 0) log('  ..', j.name, parts.length, 'slices');
    }
    await s.ev('window.__b = null; 1');
    if (!ok) { log('FAIL', j.name, 'slice error'); continue; }
    const buf = Buffer.concat(parts);
    if (buf.slice(0, 4).toString() === '%PDF') {
      fs.writeFileSync(dest, buf);
      log('GOT', j.name, Math.round(buf.length / 1024) + 'KB');
    } else {
      log('NOTPDF', j.name, buf.slice(0, 8).toString('hex'));
    }
    await sleep(9000 + Math.random() * 7000);
  }
  try { s.ws.close(); } catch (e) {}
  chrome.kill(); await sleep(1200);
  try { fs.rmSync(profile, { recursive: true, force: true }); } catch (e) {}
  process.exit(0);
})().catch(e => { console.error('FATAL', e); process.exit(1); });
