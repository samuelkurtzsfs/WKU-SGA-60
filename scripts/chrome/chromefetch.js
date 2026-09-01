// Fetch URLs through a real headless Chrome, waiting out any JS challenge.
//   node chromefetch.js <outdir> <name>=<url> [...]
// Text/JSON responses are written as <name>.txt; images/PDFs as binary.
const { spawn } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
// One debug port per process: the whole fleet may run this at once,
// and a second Chrome on a taken port attaches to the first one's
// tabs instead of its own, which corrupts both downloads.
const PORT = 9300 + (process.pid % 600);
const outdir = process.argv[2];
const jobs = process.argv.slice(3).map(s => {
  const i = s.indexOf('=');
  return { name: s.slice(0, i), url: s.slice(i + 1) };
});
const sleep = ms => new Promise(r => setTimeout(r, ms));

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
      setTimeout(() => { if (this.pending.delete(id)) rej(new Error('timeout ' + method)); }, 900000);
    });
  }
}
const open = u => new Promise((res, rej) => {
  const ws = new WebSocket(u);
  ws.addEventListener('open', () => res(new Session(ws)));
  ws.addEventListener('error', () => rej(new Error('ws')));
});
const log = (...a) => console.log(new Date().toTimeString().slice(0, 8), ...a);

(async () => {
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'sk-fetch-'));
  const HEADLESS = process.env.SK_VISIBLE ? [] : ['--headless=new', '--disable-gpu'];
  const chrome = spawn(CHROME, [...HEADLESS, '--no-first-run',
    '--no-default-browser-check', '--disable-extensions', '--mute-audio',
    '--window-size=1200,900', '--window-position=-3000,-3000',
    '--disable-blink-features=AutomationControlled',
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

  // warm up: visit the site root so the challenge cookie is set once
  const first = new URL(jobs[0].url);
  await s.send('Page.navigate', { url: first.origin + '/' });
  for (let i = 0; i < 20; i++) {
    await sleep(2000);
    const r = await s.send('Runtime.evaluate', { returnByValue: true, expression: 'document.title' });
    const t = String(r.result.value || '');
    if (!/just a moment|attention required/i.test(t)) { log('warm', JSON.stringify(t.slice(0, 50))); break; }
  }

  for (const j of jobs) {
    let body = null;
    for (let attempt = 0; attempt < 3; attempt++) {
      const r = await s.send('Runtime.evaluate', {
        awaitPromise: true, returnByValue: true,
        expression: `
          (async () => {
            const r = await fetch(${JSON.stringify(j.url)}, {credentials:'include'});
            const ct = r.headers.get('content-type') || '';
            if (!r.ok) return 'ERR ' + r.status + ' ' + ct;
            if (/json|text|html/.test(ct)) return 'TXT:' + (await r.text());
            const b = new Uint8Array(await r.arrayBuffer());
            let s2 = ''; const CH = 0x8000;
            for (let i = 0; i < b.length; i += CH) s2 += String.fromCharCode.apply(null, b.subarray(i, i+CH));
            return 'BIN:' + btoa(s2);
          })()`,
      });
      body = String(r.result.value || '');
      if (!body.startsWith('ERR')) break;
      log('retry', j.name, body.slice(0, 40));
      await sleep(8000);
    }
    if (body.startsWith('TXT:')) {
      fs.writeFileSync(path.join(outdir, j.name + '.txt'), body.slice(4));
      log('OK-TXT', j.name, body.length - 4, 'chars');
    } else if (body.startsWith('BIN:')) {
      const buf = Buffer.from(body.slice(4), 'base64');
      fs.writeFileSync(path.join(outdir, j.name), buf);
      log('OK-BIN', j.name, Math.round(buf.length / 1024) + 'KB',
          buf.slice(0, 4).toString('hex'));
    } else {
      log('FAIL', j.name, body.slice(0, 120));
    }
    await sleep(9000 + Math.random()*6000);
  }
  try { s.ws.close(); } catch (e) {}
  chrome.kill(); await sleep(1200);
  try { fs.rmSync(profile, { recursive: true, force: true }); } catch (e) {}
  process.exit(0);
})().catch(e => { console.error('FATAL', e); process.exit(1); });
