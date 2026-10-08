/* QA renderer (validation only; not part of the deck).
   Requires playwright-core and a Chromium build:
     PW=/path/to/node_modules/playwright-core CHROME=/path/to/chrome node build/qa/render.cjs [--slides SL01,SL02] [--vp 1920x1080,1366x768,1280x720,390x844] [--no-shots] [--shots-vp 1366x768,390x844]
   The slide canvas is authored at 1600×900 and scaled to landscape viewports, so fit is measured in
   canvas pixels on the active slide: content must stay inside the canvas (no vertical or horizontal
   spill, nothing under the header strip or over the slide counter), and body content must end above the
   footer row (or above the 840 px padding line on slides without a source line). Narrow viewports use the reading
   layout; there only horizontal overflow is a failure. For each slide the default state and an
   "expanded" state (reveal on, every choice tried, preferred one left selected) are measured, page
   errors and non-local requests are recorded. Results: validation/qa-results.json */
const path = require('path');
const fs = require('fs');
const { chromium } = require(process.env.PW || 'playwright-core');
const ROOT = path.resolve(__dirname, '../..');
const DECK = 'file://' + path.join(ROOT, 'dist/workshop.html');
const args = process.argv.slice(2);
const opt = k => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : null; };
const vps = (opt('--vp') || '1920x1080,1366x768,1280x720,390x844').split(',').map(v => v.split('x').map(Number));
const shotVps = (opt('--shots-vp') || '1366x768,390x844').split(',');
const only = opt('--slides') ? opt('--slides').split(',') : null;
const shots = !args.includes('--no-shots');
const outDir = path.join(ROOT, 'validation/screenshots');

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROME });
  const results = [];
  const external = [];
  for (const [w, h] of vps) {
    const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e)));
    page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
    page.on('request', r => { const u = r.url(); if (!/^(file|data|about):/.test(u)) external.push(u); });
    await page.goto(DECK);
    const ids = await page.$$eval('.slide', s => s.map(x => x.id));
    const vpName = `${w}x${h}`;
    const takeShots = shots && shotVps.includes(vpName);
    if (takeShots) fs.mkdirSync(path.join(outDir, vpName), { recursive: true });
    const narrow = w < 900;
    for (const id of ids) {
      if (only && !only.includes(id)) continue;
      await page.evaluate(i => { location.hash = '#' + i; }, id);
      await page.waitForTimeout(60);
      const measure = async state => {
        await page.waitForTimeout(220);
        const m = await page.evaluate(narrow => {
          const d = document.documentElement, s = document.querySelector('.slide.active');
          const stage = document.getElementById('stage');
          const sr = stage.getBoundingClientRect();
          const scale = narrow ? 1 : sr.width / 1600;
          const toCanvas = r => ({ top: (r.top - sr.top) / scale, bottom: (r.bottom - sr.top) / scale, left: (r.left - sr.left) / scale, right: (r.right - sr.left) / scale });
          const spill = [];
          let maxBottom = 0, maxRight = 0, bodyBottom = 0, footTop = Infinity;
          if (!narrow) {
            const counter = toCanvas(document.getElementById('counter').getBoundingClientRect());
            const foot = s.querySelector('.foot');
            footTop = foot ? toCanvas(foot.getBoundingClientRect()).top : Infinity;
            s.querySelectorAll('*').forEach(e => {
              const r = e.getBoundingClientRect();
              if (!r.width || !r.height) return;
              const c = toCanvas(r);
              maxBottom = Math.max(maxBottom, c.bottom); maxRight = Math.max(maxRight, c.right);
              if (!(foot && foot.contains(e)) && e.children.length === 0) bodyBottom = Math.max(bodyBottom, c.bottom);
              const name = (e.className && String(e.className).split(' ')[0]) || e.tagName;
              if (c.bottom > 900 + 1 || c.right > 1600 + 1 || c.top < 72 - 1) spill.push(name);
              // body content reaching into the footer row (slide grid, 8 Oct 2026): any leaf below the footer's top edge
              if (foot && !foot.contains(e) && e.children.length === 0 && c.bottom > footTop + 1) spill.push('foot:' + name);
              // over the slide counter (bottom-right corner)
              if (e.children.length === 0 && c.bottom > counter.top && c.right > counter.left - 8 && c.top < counter.bottom) spill.push('counter:' + name);
            });
          }
          return { scrollW: d.scrollWidth, innerW: innerWidth, scrollH: d.scrollHeight, innerH: innerHeight,
            maxBottom: Math.round(maxBottom), maxRight: Math.round(maxRight), bodyBottom: Math.round(bodyBottom), footTop: Number.isFinite(footTop) ? Math.round(footTop) : null,
            spill: [...new Set(spill)].slice(0, 6), active: s.id };
        }, narrow);
        const hOver = m.scrollW > m.innerW + 1;
        // the footer row ends on the padding line (canvas 840); body content must end above the footer's top edge, or above
        // the padding line when the slide has no footer; no tolerance (slide grid, 8 Oct 2026)
        const vOver = !narrow && (m.maxBottom > 841 || m.bodyBottom > (m.footTop === null ? 841 : m.footTop + 1) || m.spill.length > 0);
        const ok = !hOver && !vOver && (narrow || m.maxRight <= 1601);
        results.push({ vp: vpName, id, state, maxBottom: m.maxBottom, bodyBottom: m.bodyBottom, footTop: m.footTop, maxRight: m.maxRight, spill: m.spill, hOver, ok });
        if (takeShots) {
          await page.screenshot({ path: path.join(outDir, vpName, `${id}-${vpName}-${state}.png`), fullPage: narrow });
        }
      };
      await measure('default');
      const has = await page.evaluate(() => {
        const s = document.querySelector('.slide.active');
        return { reveal: s.querySelectorAll('[data-act="reveal"]').length, groups: s.querySelectorAll('[data-choice-group]').length };
      });
      if (has.reveal + has.groups === 0) continue;
      await page.evaluate(() => {
        const s = document.querySelector('.slide.active');
        const r = s.querySelector('[data-act="reveal"]'); if (r && !s.classList.contains('revealed')) r.click();
      });
      if (has.groups) {
        const groups = await page.evaluate(() => [...document.querySelectorAll('.slide.active [data-choice-group]')].map(g => g.querySelectorAll('[data-act="choose"]').length));
        for (let gi = 0; gi < groups.length; gi++) for (let oi = 0; oi < groups[gi]; oi++) {
          await page.evaluate(([gi, oi]) => { document.querySelectorAll('.slide.active [data-choice-group]')[gi].querySelectorAll('[data-act="choose"]')[oi].click(); }, [gi, oi]);
          await measure(`choice-${gi}-${oi}`);
        }
        await page.evaluate(() => {
          const D = JSON.parse(document.getElementById('deck-data').textContent);
          document.querySelectorAll('.slide.active [data-choice-group]').forEach(g => {
            const opts = D.choices[g.dataset.choiceGroup] || [];
            const i = opts.findIndex(o => o.preferred);
            const b = g.querySelectorAll('[data-act="choose"]')[i];
            if (b) b.click();
          });
        });
      }
      await measure('expanded');
      // reset through the menu so later checks start clean
      await page.evaluate(() => {
        document.getElementById('menuBtn').click();
        const b = document.getElementById('resetBtn'); if (b && !b.hidden && !b.disabled) b.click(); else document.getElementById('menu').close();
      });
      await page.waitForTimeout(40);
    }
    results.push({ vp: vpName, pageErrors: errors });
    await ctx.close();
  }
  await browser.close();
  const fails = results.filter(r => r.ok === false);
  fs.writeFileSync(path.join(ROOT, 'validation/qa-results.json'), JSON.stringify({ when: new Date().toISOString(), external, results }, null, 1));
  console.log(`checked ${results.filter(r => r.state).length} states; failures: ${fails.length}; external requests: ${external.length}`);
  fails.forEach(f => console.log(` FAIL ${f.vp} ${f.id} ${f.state} bottom:${f.maxBottom} body:${f.bodyBottom} foot:${f.footTop} right:${f.maxRight} h:${f.hOver} ${JSON.stringify(f.spill || [])}`));
  results.filter(r => r.pageErrors && r.pageErrors.length).forEach(r => console.log(' ERRORS', r.vp, r.pageErrors));
})();
