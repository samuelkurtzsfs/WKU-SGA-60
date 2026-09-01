// Run TopSCHOLAR's client-side search in a real browser and dump the results.
//   node chromesearch.js "query one" "query two" ...
const { spawn } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
// One debug port per process: the whole fleet may run this at once,
// and a second Chrome on a taken port attaches to the first one's
// tabs instead of its own, which corrupts both downloads.
const PORT = 9300 + (process.pid % 600);
const queries = process.argv.slice(2);
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
      setTimeout(() => { if (this.pending.delete(id)) rej(new Error('timeout ' + method)); }, 120000);
    });
  }
}
const open = url => new Promise((res, rej) => {
  const ws = new WebSocket(url);
  ws.addEventListener('open', () => res(new Session(ws)));
  ws.addEventListener('error', () => rej(new Error('ws')));
});

(async () => {
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'sk-search-'));
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--no-first-run',
    '--no-default-browser-check', '--disable-extensions', '--mute-audio',
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

  for (const q of queries) {
    const url = 'https://digitalcommons.wku.edu/do/search/?q=' +
      encodeURIComponent(q) + '&start=0&context=276414&facet=';
    await s.send('Page.navigate', { url });
    let out = '[]';
    for (let i = 0; i < 18; i++) {
      await sleep(1500);
      const r = await s.send('Runtime.evaluate', {
        returnByValue: true,
        expression: `
          (() => {
            const rows = [...document.querySelectorAll('.result, .article-listing, #results .item, .search-result')];
            const out = [];
            for (const el of rows) {
              const a = el.querySelector('a[href]');
              if (!a) continue;
              out.push({t: (a.textContent||'').trim().slice(0,110), u: a.href,
                        d: (el.textContent||'').replace(/\\s+/g,' ').trim().slice(0,300)});
            }
            if (!out.length) {
              for (const a of document.querySelectorAll('a[href*="digitalcommons.wku.edu/"]')) {
                const h = a.getAttribute('href')||'';
                if (/\\/[a-z_]+\\/[0-9]+\\/?$/.test(h) || /vol[0-9]+\\/iss/.test(h))
                  out.push({t:(a.textContent||'').trim().slice(0,110), u:a.href, d:''});
              }
            }
            return JSON.stringify(out.slice(0,30));
          })()`,
      });
      out = String(r.result.value || '[]');
      if (out !== '[]') break;
    }
    console.log('##QUERY## ' + q);
    console.log(out);
  }
  try { s.ws.close(); } catch (e) {}
  chrome.kill(); await sleep(1000);
  try { fs.rmSync(profile, { recursive: true, force: true }); } catch (e) {}
  process.exit(0);
})().catch(e => { console.error('FATAL', e); process.exit(1); });
