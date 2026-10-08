/* Workshop runtime.
   - One navigation owner (go): keyboard, menu, swipe and hash entry all route through it.
   - The slide canvas is designed at 1600×900 and scaled to the viewport on landscape screens;
     narrow screens use an unscaled reading layout (see CSS).
   - Slide interactions are scoped to their slide through data-act delegation, so state never
     leaks between slides and survives navigation until the page reloads.
   - Overlays are native <dialog> elements opened modally: the browser contains focus inside
     them and the rest of the page is inert while one is open. Strings are inserted with textContent. */
(function () {
  'use strict';
  const D = JSON.parse(document.getElementById('deck-data').textContent);
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const stage = $('#stage');
  const main = $('#slides');
  const slides = $$('.slide', main);
  const pristine = slides.map(s => s.cloneNode(true));
  const meta = Object.fromEntries(D.slides.map(s => [s.id, s]));
  const sources = Object.fromEntries(D.sources.map(s => [s.id, s]));
  const total = slides.length;
  let current = 0;

  function el(tag, cls, text) {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function announce(t) { const a = $('#announce'); a.textContent = ''; setTimeout(() => { a.textContent = t; }, 30); }
  function pad(n) { return String(n).padStart(2, '0'); }
  function safeUrl(u) { return /^https?:\/\//i.test(u || '') ? u : null; }
  function sourceLink(s) {
    const url = safeUrl(s.url);
    const a = el(url ? 'a' : 'span', null, s.title + (s.published ? ', ' + s.published : ''));
    if (url) { a.href = url; a.target = '_blank'; a.rel = 'noopener noreferrer'; }
    return a;
  }
  function moduleLabel(m) { return m.kind === 'break' ? m.name : `${m.id === 'M0' ? 'Opening' : 'Module ' + m.id.slice(1)} · ${m.name}`; }

  /* ---------- canvas scaling (desktop only; CSS handles the narrow reading layout) ---------- */
  const BASE_W = 1600, BASE_H = 900;
  const narrow = window.matchMedia('(max-width: 899px)');
  function fit() {
    if (narrow.matches) { stage.style.removeProperty('--s'); return; }
    const s = Math.min(document.documentElement.clientWidth / BASE_W, document.documentElement.clientHeight / BASE_H);
    stage.style.setProperty('--s', s.toFixed(4));
  }
  window.addEventListener('resize', fit);
  narrow.addEventListener('change', fit);
  fit();

  /* ---------- navigation (single owner) ---------- */
  function go(n, opts = {}) {
    const prev = current;
    current = Math.max(0, Math.min(total - 1, n));
    const leaving = slides[prev];
    const hadFocus = leaving && leaving.contains(document.activeElement);
    slides.forEach((s, i) => {
      const on = i === current;
      s.classList.toggle('active', on);
      s.setAttribute('aria-hidden', String(!on));
      if (on) s.removeAttribute('inert'); else s.setAttribute('inert', '');
    });
    const s = slides[current], m = meta[s.id], mod = D.modules.find(x => x.id === s.dataset.module);
    $('#counter').textContent = `${pad(current + 1)} / ${pad(total)}`;
    document.body.dataset.layout = s.dataset.layout || '';          // lets the viewport carry a full-window backdrop on cover/openers
    $('#modlabel').textContent = mod ? (mod.kind === 'break' ? mod.name : mod.id === 'M0' ? 'Opening' : `Module ${mod.id.slice(1)} · ${mod.name}`) : '';
    announce(`Slide ${current + 1} of ${total}: ${m.title}`);
    if (!opts.keepHash) history.replaceState(null, '', '#' + s.id);
    window.scrollTo(0, 0);
    if (hadFocus || opts.focus) { const h = $('h1,h2', s); if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); } }
    updateResetButton();
  }

  /* ---------- slide-scoped interactions ---------- */
  function setLabel(btn, on) {
    const l = on ? btn.dataset.on : btn.dataset.off;
    if (l) btn.textContent = l;
  }
  const actions = {
    reveal(btn, slide) {
      const on = !slide.classList.contains('revealed');
      slide.classList.toggle('revealed', on);
      $$('[data-act="reveal"]', slide).forEach(b => { b.setAttribute('aria-expanded', String(on)); setLabel(b, on); });
      announce(on ? 'Content revealed.' : 'Content hidden.');
      updateResetButton();
    },
    choose(btn, slide) {
      const group = btn.closest('[data-choice-group]');
      const gid = group.dataset.choiceGroup;
      const opt = (D.choices[gid] || [])[Number(btn.dataset.idx)];
      if (!opt) return;
      slide.classList.add('chosen');
      $$('[data-act="choose"]', group).forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
      const fb = slide.querySelector(`[data-feedback="${CSS.escape(group.dataset.fb || gid)}"]`);
      if (fb) {
        fb.className = fb.className.replace(/\b(good|caution)\b/g, '').trim() + ' ' + (opt.preferred ? 'good' : 'caution');
        fb.textContent = '';
        fb.append(el('span', 'verdict', opt.preferred ? 'Recommended' : 'Reconsider'));
        if (group.dataset.fb) fb.append(el('span', 'fbfor', group.getAttribute('aria-label').split(':')[0] + ': '));
        fb.append(el('strong', null, opt.feedback));
        if (opt.detail) fb.append(document.createTextNode(' ' + opt.detail));
      }
      updateResetButton();
    },
    sources() { openSources(); },
  };
  main.addEventListener('click', e => {
    const btn = e.target.closest('[data-act]');
    if (!btn || btn.disabled) return;
    const slide = btn.closest('.slide');
    if (!slide || !slide.classList.contains('active')) return;
    const fn = actions[btn.dataset.act];
    if (fn) { e.preventDefault(); fn(btn, slide); }
  });

  /* ---------- reset (current slide only, from the menu) ---------- */
  function hasInteraction(slide) { return !!slide.querySelector('[data-act="reveal"],[data-act="choose"]'); }
  function hasState(slide) { return slide.classList.contains('revealed') || slide.classList.contains('chosen'); }
  function updateResetButton() {
    const slide = slides[current], b = $('#resetBtn');
    const show = hasInteraction(slide);
    b.hidden = !show;
    if (!show) return;
    b.disabled = !hasState(slide);
    $('#resetSub').textContent = b.disabled ? 'Nothing to reset on this slide yet' : 'Clears this slide’s choice or reveal';
  }
  function resetSlide() {
    const fresh = pristine[current].cloneNode(true);
    slides[current].replaceWith(fresh);
    slides[current] = fresh;
    go(current);
    announce('This slide has been reset.');
  }
  $('#resetBtn').addEventListener('click', () => { resetSlide(); closeDialog(menu); });

  /* ---------- dialogs: native modal <dialog>, focus restored to the opener ---------- */
  const menu = $('#menu'), menuBtn = $('#menuBtn');
  const returnTo = new Map();
  function openDialog(d, opener) {
    if (d.open) return;
    returnTo.set(d, opener || document.activeElement);
    d.showModal();
    if (d === menu) menuBtn.setAttribute('aria-expanded', 'true');
  }
  function closeDialog(d) { if (d && d.open) d.close(); }
  $$('dialog').forEach(d => {
    d.addEventListener('click', e => { if (e.target === d) d.close(); });          // backdrop
    d.addEventListener('cancel', e => { e.preventDefault(); d.close(); });         // Escape: close this overlay only
    d.addEventListener('close', () => {
      if (d === menu) menuBtn.setAttribute('aria-expanded', 'false');
      if (!returnTo.has(d)) return;                      // focus already placed elsewhere (slide heading or another panel)
      const back = returnTo.get(d);
      returnTo.delete(d);
      if (back && back.isConnected && typeof back.focus === 'function') back.focus({ preventScroll: true });
      else menuBtn.focus({ preventScroll: true });
    });
  });
  $$('[data-close]').forEach(b => b.addEventListener('click', () => b.closest('dialog').close()));
  /* From the menu, a tool replaces the menu with its own panel; closing the panel returns focus to the menu button. */
  function fromMenu(open) {
    return () => {
      const wasMenu = menu.open;
      if (wasMenu) { returnTo.delete(menu); closeDialog(menu); }
      open(wasMenu ? menuBtn : document.activeElement);
    };
  }

  /* ---------- menu: tools and slide index built from the slide data ---------- */
  function toggleMenu() {
    if (menu.open) { closeDialog(menu); return; }
    renderIndex();
    openDialog(menu, menuBtn);
    const here = $('.idxbtn.here', menu);
    if (here) { here.focus({ preventScroll: true }); here.scrollIntoView({ block: 'nearest' }); }
  }
  menuBtn.addEventListener('click', toggleMenu);

  const indexBody = $('#indexBody');
  function buildIndex() {
    D.modules.forEach(m => {
      const members = slides.map((s, i) => [s, i]).filter(([s]) => s.dataset.module === m.id);
      if (!members.length) return;
      const sec = el('section', 'idxmod' + (m.kind === 'break' ? ' brk' : ''));
      sec.dataset.module = m.id;
      const h = el('h3', 'idxhead');
      const tb = el('button', 'idxtoggle');
      tb.type = 'button';
      tb.setAttribute('aria-expanded', 'false');
      tb.setAttribute('aria-controls', 'menu-' + m.id);
      tb.append(el('span', 'idxchev'), el('span', 'idxname', moduleLabel(m)), el('span', 'idxcount', `${members.length} ${members.length === 1 ? 'slide' : 'slides'}`));
      tb.addEventListener('click', () => setExpanded(sec, tb.getAttribute('aria-expanded') !== 'true'));
      h.append(tb);
      const ol = el('ol', 'idxlist');
      ol.id = 'menu-' + m.id;
      ol.hidden = true;
      members.forEach(([s, i]) => {
        const li = el('li');
        const b = el('button', 'idxbtn');
        b.type = 'button';
        b.dataset.index = String(i);
        b.append(el('span', 'idxid', pad(i + 1)), el('span', 'idxtitle', meta[s.id].title));
        b.addEventListener('click', () => { returnTo.delete(menu); closeDialog(menu); go(i, { focus: true }); });
        li.append(b);
        ol.append(li);
      });
      sec.append(h, ol);
      indexBody.append(sec);
    });
  }
  function setExpanded(sec, on) {
    $('.idxtoggle', sec).setAttribute('aria-expanded', String(on));
    $('.idxlist', sec).hidden = !on;
  }
  function renderIndex() {
    const cur = slides[current];
    $$('.idxmod', indexBody).forEach(sec => {
      const isCurrent = sec.dataset.module === cur.dataset.module;
      sec.classList.toggle('current', isCurrent);
      setExpanded(sec, isCurrent);
    });
    $$('.idxbtn', indexBody).forEach(b => {
      const on = Number(b.dataset.index) === current;
      b.classList.toggle('here', on);
      if (on) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current');
    });
  }
  buildIndex();

  /* ---------- presenter notes ---------- */
  function showNotes(opener) {
    const m = meta[slides[current].id];
    $('#noteTitle').textContent = `${pad(current + 1)} · ${m.title}`;
    const body = $('#noteBody');
    body.textContent = '';
    body.append(el('p', 'notemeta', `${m.start}–${m.end} MYT · ${m.minutes} min · ${m.moduleName}`));
    const add = (label, text) => {
      if (!text || (Array.isArray(text) && !text.length)) return;
      body.append(el('h4', null, label));
      (Array.isArray(text) ? text : [text]).forEach(t => body.append(el('p', null, t)));
    };
    add('Objective', m.objective);
    add('What this slide shows', m.whatThisShows);
    add('Key point', m.keyPoint);
    add('Facilitator notes', m.notes);
    add('Run it', m.interaction);
    add('Expected answer / reveal', m.answer || m.reveal);
    add('Further notes', m.notesExtra);
    if (m.sourceIds.length) {
      body.append(el('h4', null, 'Sources'));
      const ul = el('ul');
      m.sourceIds.forEach(id => { const li = el('li'); li.append(el('b', null, id + ' '), sourceLink(sources[id])); ul.append(li); });
      body.append(ul);
    }
    body.append(el('p', 'notewarn', 'These notes are shown on this screen, so a projected audience sees them. Use the facilitator guide for private reference.'));
    openDialog($('#notes'), opener);
    $('#notes .sheetbody').scrollTop = 0;
  }
  $('#notesBtn').addEventListener('click', fromMenu(showNotes));

  /* ---------- sources ---------- */
  function openSources(opener) {
    const body = $('#refBody');
    body.textContent = '';
    const cited = meta[slides[current].id].sourceIds;
    if (cited.length) {
      body.append(el('h4', null, 'Cited on this slide'));
      const ul = el('ul', 'reflist');
      cited.forEach(id => { const li = el('li'); li.append(el('b', null, id + ' '), sourceLink(sources[id])); ul.append(li); });
      body.append(ul);
    }
    D.sourceGroups.forEach(g => {
      body.append(el('h4', null, g.name));
      const ul = el('ul', 'reflist');
      g.ids.forEach(id => {
        const s = sources[id];
        const li = el('li');
        li.append(el('b', null, id + ' '), sourceLink(s));
        li.append(el('span', 'refuse', s.use_and_limits));
        ul.append(li);
      });
      body.append(ul);
    });
    openDialog($('#refs'), opener);
    $('#refs .sheetbody').scrollTop = 0;
  }
  $('#refsBtn').addEventListener('click', fromMenu(openSources));

  /* ---------- help and about ---------- */
  const openHelp = opener => openDialog($('#help'), opener);
  $('#helpBtn').addEventListener('click', fromMenu(openHelp));
  $('#aboutBtn').addEventListener('click', fromMenu(opener => openDialog($('#about'), opener)));

  /* ---------- fullscreen: labels follow the real API state ---------- */
  const fullBtn = $('#fullBtn'), fullSub = $('#fullSub');
  function fsSupported() { return !!(document.fullscreenEnabled && document.documentElement.requestFullscreen); }
  function updateFullscreenLabel() {
    if (!fsSupported()) {
      fullBtn.firstChild.textContent = 'Fullscreen unavailable here';
      fullSub.textContent = 'Use the browser’s own full-screen mode (often F11)';
      fullBtn.disabled = true;
      return;
    }
    fullBtn.firstChild.textContent = document.fullscreenElement ? 'Exit fullscreen' : 'Enter fullscreen';
    fullSub.textContent = 'Shortcut: F';
  }
  async function toggleFullscreen() {
    if (!fsSupported()) { announce('Fullscreen is unavailable here. Use the browser’s own full-screen mode.'); return; }
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else await document.documentElement.requestFullscreen();
    } catch (e) {
      fullSub.textContent = 'The browser refused fullscreen. Use its own full-screen mode (often F11).';
      announce('The browser refused fullscreen. Use its own full-screen mode.');
    }
  }
  document.addEventListener('fullscreenchange', updateFullscreenLabel);
  fullBtn.addEventListener('click', toggleFullscreen);
  updateFullscreenLabel();

  /* ---------- keyboard ---------- */
  function isTyping(t) {
    if (!t || t === document.body) return false;
    if (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) return true;
    return !!t.closest('[role="slider"],[role="radiogroup"],[role="radio"],[role="listbox"],[role="combobox"],[role="menu"],[role="menubar"],[role="tablist"],[role="textbox"],[role="spinbutton"],audio,video,[contenteditable]');
  }
  let lastNav = -Infinity;
  function step(delta, e) {
    e.preventDefault();
    if (e.repeat) return;                                  // holding a key never skips slides
    const now = performance.now();
    if (now - lastNav < 80) return;                        // clicker double-fire guard
    lastNav = now;
    go(current + delta);
  }
  document.addEventListener('keydown', e => {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    const k = e.key;
    const open = $('dialog[open]');
    if (k === 'Escape') {                                  // the dialog's own cancel handler closes it; nothing else to do
      return;
    }
    if (open) {
      if ((k === 'm' || k === 'M') && open === menu && !isTyping(e.target)) { e.preventDefault(); closeDialog(menu); }
      return;                                              // no slide navigation while an overlay is open
    }
    if (isTyping(e.target)) return;
    if (k === 'ArrowRight' || k === 'PageDown') step(1, e);
    else if (k === 'ArrowLeft' || k === 'PageUp') step(-1, e);
    else if (k === 'Home') { e.preventDefault(); go(0); }
    else if (k === 'End') { e.preventDefault(); go(total - 1); }
    else if (k === 'm' || k === 'M') { e.preventDefault(); toggleMenu(); }
    else if (k === 'f' || k === 'F') { e.preventDefault(); toggleFullscreen(); }
    else if (k === '?') { e.preventDefault(); openHelp(document.activeElement === document.body ? menuBtn : document.activeElement); }
  });

  /* ---------- touch: horizontal swipe on non-interactive space ---------- */
  let touch = null;
  main.addEventListener('touchstart', e => {
    if (e.target.closest('button,a,[data-act],.diagram-wrap')) { touch = null; return; }   // diagrams scroll sideways on narrow screens
    touch = { x: e.changedTouches[0].clientX, y: e.changedTouches[0].clientY };
  }, { passive: true });
  main.addEventListener('touchend', e => {
    if (!touch) return;
    const dx = e.changedTouches[0].clientX - touch.x, dy = e.changedTouches[0].clientY - touch.y;
    if (Math.abs(dx) > 80 && Math.abs(dx) > Math.abs(dy) * 2) go(current + (dx < 0 ? 1 : -1));
    touch = null;
  }, { passive: true });

  /* ---------- hash entry: #SL07 (or a continuation such as #SL09B), or legacy #slide-7 (position-based; it shifts when slides are inserted) ---------- */
  function fromHash() {
    const h = location.hash;
    let i = -1, m;
    if ((m = h.match(/^#(SL\d{2}[A-Z]?)$/))) i = slides.findIndex(s => s.id === m[1]);
    else if ((m = h.match(/^#slide-(\d{1,2})$/))) i = Number(m[1]) - 1;
    return i >= 0 && i < total ? i : 0;
  }
  window.addEventListener('hashchange', () => go(fromHash(), { keepHash: true }));
  go(fromHash(), { keepHash: true });
})();
