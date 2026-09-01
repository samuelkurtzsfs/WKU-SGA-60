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
const PACE = parseInt(process.env.PACE || '2500', 10);
const outdir = process.argv[2];
const FIRST = parseInt(process.argv[3] || '2016', 10);
const LAST = parseInt(process.argv[4] || '2023', 10);
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

  // The fetch below runs inside this page, so it must BE wkuherald.com:
  // the Cloudflare clearance cookie is per-origin, and a request made from
  // another origin is challenged again exactly as curl is.
  await s.send('Page.navigate', { url: 'https://wkuherald.com/' });
  await sleep(7000);
  log('warm', JSON.stringify(String(await s.ev('document.title')).slice(0, 50)));


  const API = 'https://wkuherald.com/wp-json/wp/v2/media';
  const out = [];
  for (let year = FIRST; year <= LAST; year++) {
    let page = 1, pages = 1, got = 0;
    while (page <= pages) {
      const url = `${API}?after=${year}-01-01T00:00:00&before=${year}-12-31T23:59:59`
                + `&order=asc&orderby=date&per_page=100&page=${page}`
                + `&_fields=id,date,source_url,caption`;
      let res;
      try {
        res = await s.ev(`
          (async () => {
            const r = await fetch(${JSON.stringify('')} + ${JSON.stringify(url)}, {credentials:'include'});
            if (!r.ok) return {err: r.status};
            return {pages: +(r.headers.get('X-WP-TotalPages') || 1),
                    body: await r.text()};
          })()`, true);
      } catch (e) { log('ERR', year, page, String(e).slice(0, 60)); break; }
      if (!res || res.err) { log('FAIL', year, 'page', page, 'status', res && res.err); break; }
      if (page === 1) pages = res.pages || 1;
      let rows;
      try { rows = JSON.parse(res.body); } catch (e) { log('BADJSON', year, page); break; }
      for (const m of rows) {
        const cap = String((m.caption && m.caption.rendered) || '')
          .replace(/<[^>]+>/g, ' ').replace(/&#(\d+);/g, (_, d) => String.fromCharCode(d))
          .replace(/&amp;/g, '&').replace(/&nbsp;/g, ' ').replace(/&#8217;/g, "'")
          .replace(/\s+/g, ' ').trim();
        if (!cap) continue;
        out.push({id: m.id, date: String(m.date).slice(0, 10), url: m.source_url,
                  caption: cap, x: cap.toLowerCase()});
        got++;
      }
      page++;
      await sleep(PACE);
    }
    log(year, got, 'captioned');
  }
  // Merge, never replace. A run that is rate limited partway through returns
  // nothing, and writing that over a good run costs everything it collected.
  const dest = path.join(outdir, 'herald-chrome.json');
  const seen = new Map();
  if (fs.existsSync(dest)) {
    for (const r of JSON.parse(fs.readFileSync(dest, 'utf8'))) seen.set(r.id, r);
  }
  const before = seen.size;
  for (const r of out) seen.set(r.id, r);
  const all = [...seen.values()].sort((a, b) => a.date.localeCompare(b.date));
  fs.writeFileSync(dest, JSON.stringify(all, null, 1));
  log('had', before, '+', out.length, 'this run =', all.length, 'captioned');
  process.exit(0);
})();
