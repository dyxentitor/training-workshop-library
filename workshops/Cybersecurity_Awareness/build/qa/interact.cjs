/* Interaction, accessibility-structure, safety and contrast checks (validation only).
   PW=/path/to/playwright-core CHROME=/path/to/chrome node build/qa/interact.cjs
   Writes validation/interaction-results.json and prints PASS/FAIL per check. */
const path = require('path');
const fs = require('fs');
const { chromium } = require(process.env.PW || 'playwright-core');
const ROOT = path.resolve(__dirname, '../..');
const DECK = 'file://' + path.join(ROOT, 'dist/workshop.html');
const results = [];
const check = (name, ok, info = '') => { results.push({ name, ok: !!ok, info }); console.log(`${ok ? 'PASS' : 'FAIL'}  ${name}${info ? '  — ' + info : ''}`); };

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROME });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, hasTouch: true });
  const page = await ctx.newPage();
  const errors = [], requests = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('request', r => requests.push(r.url()));
  await page.goto(DECK);
  const active = () => page.evaluate(() => document.querySelector('.slide.active').id);
  const key = async k => { await page.keyboard.press(k); await page.waitForTimeout(120); };
  const openDialogs = () => page.evaluate(() => [...document.querySelectorAll('dialog[open]')].map(d => d.id));
  const focused = () => page.evaluate(() => { const a = document.activeElement; return a ? (a.id || a.className || a.tagName) : ''; });

  // structure
  const s = await page.evaluate(() => ({
    n: document.querySelectorAll('.slide').length, activeN: document.querySelectorAll('.slide.active').length,
    counter: document.querySelector('#counter').textContent,
    inertOk: [...document.querySelectorAll('.slide:not(.active)')].every(x => x.hasAttribute('inert') && x.getAttribute('aria-hidden') === 'true'),
    ids: [...document.querySelectorAll('[id]')].map(e => e.id),
    bottomBar: !!document.querySelector('footer, .bottom, .modulebar, .seg, .dots, .nav, #prev, #next, .progress'),
    scale: getComputedStyle(document.getElementById('stage')).getPropertyValue('--s').trim(),
  }));
  const total = s.n;
  const lastId = await page.evaluate(() => [...document.querySelectorAll('.slide')].pop().id);   // SL76: continuation IDs (SL09B…) mean the count is not the last number
  check(`${total} slides, one active, counter generated from the sequence`, s.activeN === 1 && s.counter === `01 / ${String(total).padStart(2, '0')}`, s.counter);
  check('no bottom toolbar, module bar, progress segments or footer arrows in the DOM', !s.bottomBar);
  check('canvas scale applied at 1440×900 (0.9)', s.scale === '0.9000', s.scale);
  check('inactive slides are inert and aria-hidden', s.inertOk);
  check('no duplicate element IDs', new Set(s.ids).size === s.ids.length);

  // keyboard navigation
  await page.evaluate(() => document.activeElement && document.activeElement.blur());
  await key('ArrowRight'); const a1 = await active();
  await key('PageDown'); const a2 = await active();
  await key('PageUp'); const a3 = await active();
  await key('ArrowLeft'); const a4 = await active();
  check('ArrowRight / PageDown / PageUp / ArrowLeft', a1 === 'SL02' && a2 === 'SL03' && a3 === 'SL02' && a4 === 'SL01', [a1, a2, a3, a4].join(','));
  await key('ArrowLeft'); check('ArrowLeft on first slide stays on SL01', (await active()) === 'SL01');
  await key('End'); const e1 = await active();
  check(`End jumps to the last slide (${lastId})`, e1 === lastId, e1);
  await key('ArrowRight'); check('ArrowRight on last slide stays on the last slide', (await active()) === lastId);
  await key('Home'); check('Home returns to SL01', (await active()) === 'SL01');
  // held key: auto-repeat must not skip slides
  await page.waitForTimeout(120); await page.keyboard.down('ArrowRight'); await page.waitForTimeout(700); await page.keyboard.up('ArrowRight'); await page.waitForTimeout(60);
  check('holding ArrowRight advances exactly one slide', (await active()) === 'SL02', await active());
  await page.evaluate(() => { location.hash = '#SL01'; }); await page.waitForTimeout(60);
  // modifier combinations are ignored
  await key('Control+ArrowRight'); await key('Alt+ArrowRight'); await key('Meta+ArrowRight');
  check('Ctrl / Alt / Meta + ArrowRight do not navigate', (await active()) === 'SL01');
  check('hash updates to slide ID', (await page.evaluate(() => location.hash)) === '#SL01');
  // Escape with nothing open is left to the browser
  await key('Escape'); check('Escape with no overlay open changes nothing', (await active()) === 'SL01' && (await openDialogs()).length === 0);

  // hash entry
  const ninthId = await page.evaluate(() => document.querySelectorAll('.slide')[8].id);   // #slide-N is position-based and shifts when slides are inserted (SL04B, 8 Oct 2026)
  for (const [h, want] of [['#SL40', 'SL40'], ['#SL09B', 'SL09B'], ['#slide-9', ninthId], ['#SL99', 'SL01'], ['#SL09Z', 'SL01'], [`#${lastId}`, lastId]]) {
    await page.goto(DECK + h); await page.waitForTimeout(60);
    check(`hash entry ${h} → ${want}`, (await active()) === want, await active());
  }

  // menu drawer
  await page.goto(DECK + '#SL13'); await page.waitForTimeout(60);
  await key('m');
  check('M opens the menu as a modal dialog', (await openDialogs()).join() === 'menu');
  check('menu button reports aria-expanded=true', (await page.getAttribute('#menuBtn', 'aria-expanded')) === 'true');
  const idx = await page.evaluate(() => {
    const groups = [...document.querySelectorAll('#indexBody .idxmod')];
    const expanded = groups.filter(g => g.querySelector('.idxtoggle').getAttribute('aria-expanded') === 'true').map(g => g.dataset.module);
    const here = document.querySelector('#indexBody .idxbtn.here');
    return { groups: groups.length, buttons: document.querySelectorAll('#indexBody .idxbtn').length, expanded, here: here && here.textContent, hereCurrent: here && here.getAttribute('aria-current'),
      titlesOk: [...document.querySelectorAll('#indexBody .idxtitle')].every(t => t.textContent.trim().length > 3),
      hiddenFocusable: [...document.querySelectorAll('#indexBody .idxlist[hidden] button')].some(b => b.tabIndex >= 0 && b.offsetParent !== null),
      noTimes: !/\d:\d\d/.test(document.getElementById('indexBody').textContent) };
  });
  check(`index lists every slide (${total}) in 11 module groups with descriptive titles`, idx.groups === 11 && idx.buttons === total && idx.titlesOk, `${idx.groups} groups, ${idx.buttons} buttons`);
  const contOk = await page.evaluate(() => { const b = [...document.querySelectorAll('#indexBody .idxbtn')]; const i = b.findIndex(x => x.textContent.includes('One message can do all three')); return i > 0 && b[i - 1].textContent.includes('Impersonation and phishing') && b[i].querySelector('.idxid').textContent === String(i + 1).padStart(2, '0'); });
  check('continuation slide follows its parent in the index and is numbered by position', contOk);
  const pos13 = await page.evaluate(() => String([...document.querySelectorAll('.slide')].findIndex(s => s.id === 'SL13') + 1).padStart(2, '0'));   // position, not ID: continuation slides sit before it
  check('only the current module group is expanded and the current slide is highlighted', idx.expanded.join() === 'M1' && idx.here.startsWith(pos13) && idx.hereCurrent === 'page', idx.expanded.join() + ' | ' + idx.here);
  check('collapsed groups are not focusable', !idx.hiddenFocusable);
  check('index shows no clock times', idx.noTimes);
  check('focus moved into the drawer', (await focused()).includes('idxbtn'), await focused());
  await key('ArrowRight'); check('slide keys ignored while the menu is open', (await active()) === 'SL13');
  // Tab stays inside the drawer
  for (let i = 0; i < 40; i++) await page.keyboard.press('Tab');
  check('Tab cycles within the open drawer (focus contained)', await page.evaluate(() => document.getElementById('menu').contains(document.activeElement)));
  // expand another group and navigate
  await page.click('#indexBody .idxmod[data-module="M6"] .idxtoggle');
  check('module group expands on request', (await page.getAttribute('#indexBody .idxmod[data-module="M6"] .idxtoggle', 'aria-expanded')) === 'true');
  await page.click('#indexBody .idxbtn:has-text("Evidence 2")');
  check('selecting a slide navigates and closes the drawer', (await active()) === 'SL63' && (await openDialogs()).length === 0);
  check('focus moved to the new slide heading', (await focused()) === 'SL63-title', await focused());
  // Escape and backdrop close, focus returns to the menu button
  await page.click('#menuBtn'); await page.waitForTimeout(60);
  await key('Escape');
  check('Escape closes the menu and returns focus to the menu button', (await openDialogs()).length === 0 && (await focused()) === 'menuBtn', await focused());
  await page.click('#menuBtn'); await page.waitForTimeout(60);
  await page.mouse.click(60, 450); await page.waitForTimeout(60);
  check('backdrop click closes the menu', (await openDialogs()).length === 0);
  await key('m'); await key('m'); check('M toggles the menu closed again', (await openDialogs()).length === 0);

  // notes from the menu
  await key('m'); await page.click('#notesBtn'); await page.waitForTimeout(60);
  const nt = await page.textContent('#noteTitle');
  const nb = await page.textContent('#noteBody');
  check('Notes opens for the current slide with timing, what-line and key point', (await openDialogs()).join() === 'notes' && nt.includes('Evidence 2') && nb.includes('16:15') && nb.includes('Do not request the actual code') && nb.includes('Key point'), nt);
  check('notes say they are shown on this screen (not described as private)', nb.includes('shown on this screen') && !/private notes/i.test(nb));
  const noteFit = await page.evaluate(() => { const b = document.querySelector('#notes .sheetbody'); const c = document.querySelector('#notes .close').getBoundingClientRect(); return { scrolls: b.scrollHeight > b.clientHeight, closeVisible: c.top >= 0 && c.bottom <= innerHeight }; });
  check('long notes scroll inside the panel; close button stays visible', noteFit.closeVisible, JSON.stringify(noteFit));
  await key('ArrowRight'); check('slide keys ignored while notes are open', (await active()) === 'SL63');
  await key('Escape'); check('Escape closes notes; focus returns to the menu button', (await openDialogs()).length === 0 && (await focused()) === 'menuBtn', await focused());

  // sources from the menu
  await key('m'); await page.click('#refsBtn'); await page.waitForTimeout(60);
  const refText = await page.textContent('#refBody');
  const refLinks = await page.$$eval('#refBody a', a => a.map(x => ({ h: x.href, t: x.target, r: x.rel })));
  check('sources panel lists 21+ sources with safe external links', refLinks.length >= 21 && refLinks.every(l => /^https?:/.test(l.h) && l.t === '_blank' && l.r.includes('noopener')), String(refLinks.length));
  check('sources panel shows the sources cited on this slide first', refText.startsWith('Cited on this slide'));
  await key('Escape'); check('Escape closes sources', (await openDialogs()).length === 0);

  // help via ? and the menu
  await key('Shift+Slash');
  const helpOpen = (await openDialogs()).join() === 'help';
  const helpText = helpOpen ? await page.textContent('#help') : '';
  check('? opens keyboard help listing the shortcuts', helpOpen && /Page Down/.test(helpText) && /Esc/.test(helpText) && /fullscreen/i.test(helpText));
  await key('Escape');
  check('no permanent shortcut hints on the canvas', !(await page.evaluate(() => /Page Down|Press N|shortcut/i.test(document.getElementById('stage').textContent))));

  // reset only where the slide has state
  await page.goto(DECK + '#SL03'); await page.waitForTimeout(60);
  await key('m');
  check('Reset is hidden on a slide without interaction (SL03)', await page.evaluate(() => document.getElementById('resetBtn').hidden));
  await key('Escape');
  await page.goto(DECK + '#SL05'); await page.waitForTimeout(60);
  await key('m');
  check('Reset is shown but disabled on an untouched vote (SL05)', await page.evaluate(() => { const b = document.getElementById('resetBtn'); return !b.hidden && b.disabled; }));
  await key('Escape');

  // open slides: everything visible, no hidden content or clicks (cover excepted: it opens its email in place)
  const audit = await page.evaluate(() => {
    const all = [...document.querySelectorAll('.slide')];
    const pause = all.filter(s => s.classList.contains('pause')).map(s => s.id);
    const bad = all.filter(s => !s.classList.contains('pause') && s.id !== 'SL01').filter(s => s.querySelector('[hidden],[data-act="toggle"],[data-act="step"],[data-act="reveal"],[data-act="choose"],[data-act="next"]')).map(s => s.id);
    return { pause, bad };
  });
  check('exactly 16 pause-point slides', audit.pause.length === 16, audit.pause.join(','));
  check('open slides contain no hidden content or click controls', audit.bad.length === 0, audit.bad.join(','));
  await page.goto(DECK + '#SL04');
  check('open chat shows all three messages at once (SL04)', (await page.$$eval('#SL04 .bubble', x => x.filter(e => e.offsetParent !== null).length)) === 3);
  // discussion before explanation (layout fix, 8 Oct 2026): SL03 and SL04 show their question and no takeaway; SL04B carries both points with the S7 source
  check('SL03 and SL04 show a question and no takeaway', await page.evaluate(() => ['SL03', 'SL04'].every(id => { const s = document.getElementById(id); return !!s.querySelector('.big-question, .quote') && !s.querySelector('.takeaway'); })));
  await page.goto(DECK + '#SL04B'); await page.waitForTimeout(60);
  check('SL04B carries the email and chat takeaways, visible, with a source line', await page.evaluate(() => { const s = document.getElementById('SL04B'); const t = [...s.querySelectorAll('.takeaway')]; return t.length === 2 && t.every(x => x.offsetParent !== null) && /IC3/.test((s.querySelector('.foot') || {}).textContent || ''); }));
  check('SL04 keeps the desk photograph; SL04B adds no photograph', await page.evaluate(() => !!document.querySelector('#SL04 img.scene-photo') && !document.querySelector('#SL04B img.scene-photo')));
  // slide grid (layout fix, 8 Oct 2026): header, body and footer rows on every slide; the footer is the last child when present
  check('every slide has a body row and its footer, when present, is the last child', await page.evaluate(() => [...document.querySelectorAll('.slide')].every(s => { const b = s.querySelector(':scope > .body'); const f = s.querySelector(':scope > .foot'); return !!b && (!f || s.lastElementChild === f); })));
  await page.goto(DECK + '#SL13'); await page.waitForTimeout(60);
  check('open slide takeaway visible immediately, inside the content column (SL13)', await page.evaluate(() => { const t = document.querySelector('#SL13 .takeaway'); return !!t && t.offsetParent !== null && !!t.closest('.side') && !t.closest('.foot'); }));
  check('no key-point banner markup anywhere in the deck', (await page.$$eval('.keypoint, .answerbox', x => x.length)) === 0);
  check('photos embedded as data URIs', (await page.$$eval('img.photo', x => x.length > 0 && x.every(i => i.src.startsWith('data:image/jpeg')))));
  check('no "prayer" anywhere in the page', !(await page.evaluate(() => /prayer/i.test(document.documentElement.outerHTML))));

  // SL01 cover: email opens in place
  await page.goto(DECK + '#SL01'); await page.waitForTimeout(60);
  check('cover shows From / To / Subject and a preview before opening', await page.isVisible('#SL01 .mailmeta') && await page.isVisible('#SL01 .preview') && !(await page.isVisible('#SL01 .mailcopy')));
  await page.click('#SL01 [data-act="reveal"]');
  check('“Open the first message” reveals the full email in place and relabels', await page.isVisible('#SL01 .mailcopy') && (await page.textContent('#SL01 [data-act="reveal"]')) === 'Close the message' && (await active()) === 'SL01');
  check('date and venue placeholders are not on the cover', !(await page.evaluate(() => /to be confirmed/i.test(document.getElementById('SL01').textContent))));
  await key('m'); await page.click('#aboutBtn'); await page.waitForTimeout(60);
  const about = await page.textContent('#about');
  check('About panel carries the fictional-scenario and AI-portrait disclosures and the date/venue placeholders', /fictional/i.test(about) && /AI-generated/.test(about) && /Date to be confirmed/.test(about) && /Venue to be confirmed/.test(about));
  await key('Escape');

  // SL05 vote: neutral start, key point after choosing, persistence, isolation and reset
  await page.goto(DECK + '#SL05');
  check('vote starts neutral and takeaway hidden', (await page.$$eval('#SL05 [aria-pressed="true"]', x => x.length)) === 0 && !(await page.isVisible('#SL05 .takeaway')));
  await page.click('#SL05 [data-idx="0"]');
  const f0 = await page.getAttribute('#SL05 .feedback', 'class');
  const ft0 = await page.textContent('#SL05 .feedback');
  await page.click('#SL05 [data-idx="2"]');
  const f2 = await page.getAttribute('#SL05 .feedback', 'class');
  const ft = await page.textContent('#SL05 .feedback');
  check('choice A gives “Reconsider” feedback, C gives “Recommended” (text verdicts, not colour alone)', f0.includes('caution') && ft0.startsWith('Reconsider') && f2.includes('good') && ft.startsWith('Recommended'), ft.slice(0, 60));
  check('feedback explains why and what to do next', /established contact|normal payment approval/.test(ft), ft.slice(0, 120));
  check('takeaway shown after choosing, below the feedback', await page.evaluate(() => { const t = document.querySelector('#SL05 .takeaway'), f = document.querySelector('#SL05 .feedback'); return !!t && t.offsetParent !== null && t.getBoundingClientRect().top >= f.getBoundingClientRect().bottom; }));
  check('only one option pressed', (await page.$$eval('#SL05 [aria-pressed="true"]', x => x.length)) === 1);
  await key('ArrowRight'); await key('ArrowLeft');
  check('vote state kept after navigating away and back', (await page.getAttribute('#SL05 [data-idx="2"]', 'aria-pressed')) === 'true');
  await page.evaluate(() => { location.hash = '#SL16'; }); await page.waitForTimeout(60);
  check('another slide’s vote is unaffected', (await page.$$eval('#SL16 [aria-pressed="true"]', x => x.length)) === 0);
  await page.click('#SL16 [data-idx="0"]');
  await page.evaluate(() => { location.hash = '#SL05'; }); await page.waitForTimeout(60);
  await key('m');
  check('Reset enabled once the vote has state', await page.evaluate(() => { const b = document.getElementById('resetBtn'); return !b.hidden && !b.disabled; }));
  await page.click('#resetBtn'); await page.waitForTimeout(60);
  check('Reset clears only this slide, hides its takeaway and closes the menu', (await page.$$eval('#SL05 [aria-pressed="true"]', x => x.length)) === 0 && !(await page.isVisible('#SL05 .takeaway')) && (await active()) === 'SL05' && (await openDialogs()).length === 0);
  check('the other slide’s choice survives the reset', (await page.getAttribute('#SL16 [data-idx="0"]', 'aria-pressed')) === 'true');

  // SL06 reveal
  await page.goto(DECK + '#SL06');
  const rb = '#SL06 [data-act="reveal"]';
  check('findings and takeaway hidden before reveal', !(await page.isVisible('#SL06 .findings')) && !(await page.isVisible('#SL06 .takeaway')));
  await page.click(rb);
  check('reveal shows findings and takeaway, sets aria-expanded, swaps label', await page.isVisible('#SL06 .findings') && await page.isVisible('#SL06 .takeaway') && (await page.getAttribute(rb, 'aria-expanded')) === 'true' && (await page.textContent(rb)) === 'Hide the findings');
  await page.click(rb);
  check('reveal toggles back', !(await page.isVisible('#SL06 .findings')));

  // SL36 exercise: one click reveals all four answers
  await page.goto(DECK + '#SL36');
  check('exercise answers hidden before reveal', (await page.$$eval('#SL36 .reveal-note', x => x.filter(e => e.offsetParent !== null).length)) === 0);
  await page.click('#SL36 [data-act="reveal"]');
  check('one click reveals all four exercise answers', (await page.$$eval('#SL36 .reveal-note', x => x.filter(e => e.offsetParent !== null).length)) === 4);
  check('exercise takeaway appears with the answers, below the cards', await page.evaluate(() => { const t = document.querySelector('#SL36 .takeaway'), c = document.querySelector('#SL36 .excards'); return !!t && t.offsetParent !== null && t.getBoundingClientRect().top >= c.getBoundingClientRect().bottom; }));
  // SL23B: dedicated takeaway slide follows SL23 and carries the three actions
  await page.goto(DECK + '#SL23'); await page.waitForTimeout(60); await key('ArrowRight');
  check('SL23 is followed by its takeaway slide SL23B with one statement and three actions', (await active()) === 'SL23B' && (await page.$$eval('#SL23B .lesson .tacts li', x => x.length)) === 3 && (await page.$$eval('#SL23B img', x => x.length)) === 0);
  // takeaways on pause slides never show before the vote or reveal
  const early = await page.evaluate(() => [...document.querySelectorAll('.slide.pause')].filter(s => { const t = s.querySelector('.takeaway'); return t && !t.closest('.if-chosen, .if-revealed'); }).map(s => s.id));
  check('every takeaway on a pause slide waits for the vote or reveal', early.length === 0, early.join(','));

  // fullscreen: label follows API state; headless may refuse
  await page.goto(DECK + '#SL01'); await page.waitForTimeout(60);
  await key('m');
  const fsLabel = await page.evaluate(() => document.getElementById('fullBtn').firstChild.textContent);
  check('fullscreen button labelled from the API state', /Enter fullscreen|unavailable/.test(fsLabel), fsLabel);
  await key('Escape');
  await key('f'); await page.waitForTimeout(200);
  const fsNow = await page.evaluate(() => !!document.fullscreenElement);
  const fsLabel2 = await page.evaluate(() => document.getElementById('fullBtn').firstChild.textContent);
  check('F toggles fullscreen or fails gracefully without a page error', errors.length === 0 && (fsNow ? fsLabel2 === 'Exit fullscreen' : true), `fullscreen=${fsNow} label=${fsLabel2}`);
  if (fsNow) { await page.evaluate(() => document.exitFullscreen()); await page.waitForTimeout(100); }

  // SL76 sources button
  await page.goto(DECK + '#SL76'); await page.waitForTimeout(60);
  await page.click('#SL76 [data-act="sources"]');
  check('SL76 “Open the reference index” opens the sources panel', (await openDialogs()).join() === 'refs');
  await key('Escape');

  // touch swipe on empty space vs on a control
  await page.goto(DECK + '#SL07');
  const swipe = (x1, x2, y, sel) => page.evaluate(([x1, x2, y, sel]) => {
    const target = sel ? document.querySelector(sel) : document.elementFromPoint(x1, y);
    const mk = (x) => new Touch({ identifier: 1, target, clientX: x, clientY: y });
    target.dispatchEvent(new TouchEvent('touchstart', { bubbles: true, changedTouches: [mk(x1)], touches: [mk(x1)] }));
    target.dispatchEvent(new TouchEvent('touchend', { bubbles: true, changedTouches: [mk(x2)], touches: [] }));
  }, [x1, x2, y, sel]);
  await swipe(900, 600, 700); await page.waitForTimeout(60);
  check('swipe left on empty space goes to next slide', (await active()) === 'SL08', await active());
  await page.goto(DECK + '#SL11');
  await swipe(400, 100, 0, '#SL11 [data-act="choose"]'); await page.waitForTimeout(60);
  check('swipe that starts on a control does not navigate', (await active()) === 'SL11');

  // keyboard shortcuts do not hijack native button activation; typing guard
  await page.goto(DECK + '#SL05');
  await page.focus('#SL05 [data-idx="1"]'); await key('Enter');
  check('Enter on a focused choice selects it (native control)', (await page.getAttribute('#SL05 [data-idx="1"]', 'aria-pressed')) === 'true');
  await key('Space');
  check('Space on a focused choice keeps native activation and does not advance', (await active()) === 'SL05');
  const typed = await page.evaluate(async () => {
    const i = document.createElement('input'); i.id = 'qa-input'; document.body.append(i); i.focus();
    return true;
  });
  await key('ArrowRight'); await key('m'); await key('f');
  const typingOk = (await active()) === 'SL05' && (await openDialogs()).length === 0;
  await page.evaluate(() => document.getElementById('qa-input').remove());
  check('shortcuts ignored while typing in an input', typed && typingOk);

  // safety: no inputs/forms, links only to https sources, no storage use
  const safety = await page.evaluate(() => ({
    forms: document.querySelectorAll('input,textarea,select,form,iframe,object,embed').length,
    badLinks: [...document.querySelectorAll('a[href]')].filter(a => !/^https:\/\//.test(a.getAttribute('href')) || a.target !== '_blank' || !a.rel.includes('noopener')).map(a => a.getAttribute('href')),
    mockLinks: [...document.querySelectorAll('a[href]')].filter(a => /\.(example|test)(\/|$)/.test(new URL(a.href).hostname + '/')).length,
    storage: (() => { try { return localStorage.length + sessionStorage.length; } catch (e) { return 0; } })(),
    cookies: document.cookie.length,
  }));
  check('no form controls, iframes or embeds', safety.forms === 0);
  check('all links are https, new tab, noopener', safety.badLinks.length === 0, safety.badLinks.slice(0, 3).join(' '));
  check('no links to mock .example/.test destinations', safety.mockLinks === 0);
  check('no localStorage/sessionStorage/cookies used', safety.storage === 0 && safety.cookies === 0);
  check('no network requests other than the local file', requests.every(u => /^(file|data|about):/.test(u)), requests.filter(u => !/^(file|data|about):/.test(u)).slice(0, 3).join(' '));
  check('no page errors during the run', errors.length === 0, errors.join(' | '));

  // contrast of actual rendered text on every slide (expanded state)
  const contrast = [];
  const ids = await page.$$eval('.slide', x => x.map(e => e.id));
  for (const id of ids) {
    await page.goto(DECK + '#' + id); await page.waitForTimeout(30);
    await page.evaluate(() => {
      const s = document.querySelector('.slide.active');
      const r = s.querySelector('[data-act="reveal"]'); if (r) r.click();
      s.querySelectorAll('[data-choice-group]').forEach(g => g.querySelector('[data-act="choose"]').click());
    });
    const res = await page.evaluate(() => {
      const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(',').map(Number); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
      const lum = ({ r, g, b }) => { const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4; }; return .2126 * f(r) + .7152 * f(g) + .0722 * f(b); };
      const bgOf = el => { for (let e = el; e; e = e.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c && c.a > .5) return c; } return { r: 11, g: 18, b: 32, a: 1 }; };
      const out = [];
      const s = document.querySelector('.slide.active');
      const walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
      const seen = new Set();
      while (walker.nextNode()) {
        const t = walker.currentNode; if (!t.textContent.trim()) continue;
        const el = t.parentElement; if (seen.has(el)) continue; seen.add(el);
        const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || el.offsetParent === null && cs.position !== 'fixed') continue;
        if (el.closest('button:disabled')) continue;
        const fg = parse(cs.color), bg = bgOf(el); if (!fg) continue;
        const L1 = lum(fg), L2 = lum(bg); const ratio = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
        const size = parseFloat(cs.fontSize), bold = Number(cs.fontWeight) >= 700;
        const large = size >= 24 || (bold && size >= 18.66);
        if (ratio < (large ? 3 : 4.5)) out.push({ text: t.textContent.trim().slice(0, 40), ratio: Math.round(ratio * 100) / 100, size, cls: el.className });
      }
      return out;
    });
    res.forEach(r => contrast.push({ id, ...r }));
  }
  check('text contrast meets 4.5:1 (3:1 large) on every slide, expanded state', contrast.length === 0, contrast.length + ' low pairs');
  contrast.slice(0, 25).forEach(c => console.log('   low contrast', c.id, c.ratio, c.size + 'px', JSON.stringify(c.text), c.cls));
  // shell and overlay text contrast
  await page.goto(DECK + '#SL01'); await key('m');
  const shellContrast = await page.evaluate(() => {
    const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(',').map(Number); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
    const lum = ({ r, g, b }) => { const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4; }; return .2126 * f(r) + .7152 * f(g) + .0722 * f(b); };
    const bgOf = el => { for (let e = el; e; e = e.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c && c.a > .5) return c; } return { r: 11, g: 18, b: 32, a: 1 }; };
    const out = [];
    document.querySelectorAll('.top *, #counter, #menu *').forEach(el => {
      if (!el.childNodes.length || ![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) return;
      if (el.offsetParent === null && getComputedStyle(el).position !== 'fixed') return;
      const cs = getComputedStyle(el); const fg = parse(cs.color), bg = bgOf(el); if (!fg) return;
      const L1 = lum(fg), L2 = lum(bg); const ratio = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
      const size = parseFloat(cs.fontSize), bold = Number(cs.fontWeight) >= 700; const large = size >= 24 || (bold && size >= 18.66);
      if (ratio < (large ? 3 : 4.5)) out.push({ text: el.textContent.trim().slice(0, 30), ratio: Math.round(ratio * 100) / 100, cls: el.className });
    });
    return out;
  });
  check('shell and menu text contrast meets 4.5:1', shellContrast.length === 0, JSON.stringify(shellContrast.slice(0, 5)));
  await key('Escape');

  // narrow screen: reading layout, no horizontal overflow, counter visible, drawer usable
  const m = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const mp = await m.newPage(); await mp.goto(DECK);
  const mob = [];
  for (const id of ids) {
    await mp.goto(DECK + '#' + id); await mp.waitForTimeout(20);
    const r = await mp.evaluate(() => ({ h: document.documentElement.scrollWidth > innerWidth, scaled: getComputedStyle(document.getElementById('stage')).transform !== 'none' }));
    if (r.h || r.scaled) mob.push(id + (r.h ? ' overflow' : '') + (r.scaled ? ' scaled' : ''));
  }
  check('390px: unscaled reading layout with no horizontal overflow on every slide', mob.length === 0, mob.join(', '));
  await mp.goto(DECK + '#SL13'); await mp.click('#menuBtn'); await mp.waitForTimeout(100);
  const mobMenu = await mp.evaluate(() => { const d = document.getElementById('menu'); const r = d.getBoundingClientRect(); const c = document.querySelector('#menu .close').getBoundingClientRect(); return { open: d.open, fits: r.width <= innerWidth + 1, closeVisible: c.bottom <= innerHeight && c.top >= 0 }; });
  check('390px: drawer opens full-width with its close button visible', mobMenu.open && mobMenu.fits && mobMenu.closeVisible, JSON.stringify(mobMenu));
  await m.close();

  // reduced motion honoured
  const rm = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
  const rp = await rm.newPage(); await rp.goto(DECK);
  check('prefers-reduced-motion removes slide and drawer animation', (await rp.evaluate(() => { document.getElementById('menuBtn').click(); return getComputedStyle(document.querySelector('.slide.active')).animationName === 'none' && getComputedStyle(document.querySelector('#menu .sheet')).animationName === 'none'; })));
  await rm.close();

  fs.writeFileSync(path.join(ROOT, 'validation/interaction-results.json'), JSON.stringify({ when: new Date().toISOString(), results, contrast }, null, 1));
  const fails = results.filter(r => !r.ok).length;
  console.log(`\n${results.length - fails}/${results.length} checks passed`);
  await browser.close();
})();
