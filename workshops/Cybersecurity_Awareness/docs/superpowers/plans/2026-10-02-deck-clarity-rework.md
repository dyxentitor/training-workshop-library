# Deck Clarity Rework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the 61-slide click-heavy workshop deck into a 76-slide self-explanatory deck: content open by default, 16 deliberate pause points, a "What this slide shows" line and Key point on every content slide, module opener and takeaway slides, character photos, and no clock times or prayer wording on participant-facing screens.

**Architecture:** Keep the existing stdlib Python build (`build/build.py`) that merges `04-content/slides.json` with HTML fragments in `src/slides/*.html` into one offline `dist/workshop.html`. A one-off migration script renumbers everything to SL01–SL76 and inserts the new plan entries with their text. New pure-function modules (`build/checks.py`, `build/avatars.py`, `build/generated.py`) hold the new validation, photo embedding and opener/takeaway/agenda rendering, so they can be unit-tested. Fragments are then converted module by module to the "open" style.

**Tech Stack:** Python 3 standard library (build and unit tests via `unittest`); Pillow, used only once in a dev tool to shrink photos; vanilla HTML/CSS/JS runtime; Node + playwright-core + cached Chromium for QA scripts (validation only).

**Spec:** `docs/superpowers/specs/2026-10-02-deck-clarity-rework-design.md`

## Global Constraints

- Package root (all paths below are relative to it): `/home/universal/Claude/Cybersecurity_training_awareness/Cybersecurity_Awareness_Claude_Package`
- Slide count 76, IDs SL01–SL76 in order; programme 420 minutes; module totals M0 20, M1 45, B1 10, M2 45, M3 60, B2 75, M4 50, M5 35, B3 25, M6 35, M7 20; first slide starts 10:00, last ends 17:00.
- Pause points (exactly 16): votes SL05, SL11, SL16, SL25, SL26, SL49, SL53, SL57, SL73; reveals SL06, SL31, SL62, SL63, SL64, SL65; exercise SL36. No other slide may contain `data-act` controls except `next` (cover) and `sources` (SL76), nor `hidden`, `if-revealed` or `if-unrevealed`.
- Explanation exemptions (no "What this shows"/Key point required): SL01, SL18, SL40, SL59, SL76.
- Break titles: SL18 "Short break", SL40 "Lunch break", SL59 "Tea break". The word "prayer" must not appear anywhere in `dist/workshop.html`, and no clock time (`H:MM`/`HH:MM`) may appear on intermission, opener, takeaway or agenda slides or in module bar/index labels. Story timestamps inside scenario evidence (e.g. "16:42") are allowed.
- English only. Palette, typography and navigation unchanged. Offline single file; no remote assets; CSP unchanged.
- Evidence text must not shrink below current sizes; a slide that cannot fit 1366×768 and 1440×900 is split and recorded.
- Photos: `dist/Image_ref/profile-pictures/{aina,farid,mei,ravi,nadia,siti,daniel,lina,it-caller}.png`; credit "Portraits are AI-generated; no real person is depicted." Missing file → initial-letter avatar.
- The package is not a git repository; Task 0 creates a local one so each task can commit. Never push anywhere.

## Commands used throughout

```bash
cd /home/universal/Claude/Cybersecurity_training_awareness/Cybersecurity_Awareness_Claude_Package
python3 -m unittest discover -s build/tests -v          # unit tests
python3 build/build.py                                  # build (fails loudly on any check)
QA=/tmp/claude-1000/-home-universal-Claude-Cybersecurity-training-awareness/60fb327e-0383-4328-ac04-07935ddab15e/scratchpad
export PW=$QA/node_modules/playwright-core CHROME=$HOME/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome
node build/qa/render.cjs --vp 1440x900,1366x768,390x844   # fit checks + screenshots
node build/qa/interact.cjs                                 # interaction + contrast checks
```

If `$QA/node_modules/playwright-core` is missing: `cd $QA && npm init -y && npm i playwright-core`.

## File structure

| File | Status | Responsibility |
|---|---|---|
| `build/tools/migrate_v2.py` | create | One-off: renumber 61→76, insert new entries, timings, `what_this_shows`/`key_point`/`pause_point`, rename IDs in fragments/choices/notes/make_docs |
| `build/tools/make_avatars.py` | create | Dev-only (Pillow): shrink portraits to `src/img/avatars/*.jpg` |
| `src/img/avatars/*.jpg` | create | 9 small embedded-ready avatars |
| `build/avatars.py` | create | `CAST`, `avatar_html()`, `cast_html()` |
| `build/checks.py` | create | Pure validation functions and the pause/exempt sets |
| `build/generated.py` | create | HTML for `agenda`, `opener`, `takeaway`, `recap` layouts |
| `build/tests/test_checks.py`, `test_avatars.py`, `test_generated.py`, `test_migration.py` | create | Unit tests |
| `build/build.py` | modify | Use the three modules; render what-line and key point; generated layouts; drop `prayer_note` |
| `src/js/deck.js` | modify | Remove stepper/toggle; `chosen` class; no times in module bar/index |
| `src/css/deck.css` | modify | Append clarity-layer CSS |
| `src/slides/M0–M7.html` | modify | Convert to open style, markers, photos |
| `src/content/modules.json`, `notes.json`, `choices.json` | modify | Break names; notes for new slides; remove obsolete choice groups |
| `04-content/slides.json` | modify (via migration) | 76 entries |
| `build/make_docs.py`, `dist/README.md`, `build/qa/*.cjs`, `10-validation/validate_package.py` | modify | New numbering, no prayer, new checks |
| `validation/QA_REPORT.md`, `10-validation/PROGRESS_LEDGER.md`, `10-validation/COVERAGE_MATRIX.md`, `MANIFEST.json` | modify | Evidence and continuity |

---

### Task 0: Local git checkpoint

**Files:** none created (adds `.git/`, `.gitignore`)

- [ ] **Step 1: Initialise and commit the current state**

```bash
cd /home/universal/Claude/Cybersecurity_training_awareness/Cybersecurity_Awareness_Claude_Package
git init -q
printf '__pycache__/\n*.pyc\nvalidation/screenshots/\n' > .gitignore
git add -A
git commit -qm "chore: baseline before clarity rework (61-slide build)"
git log --oneline | head -1
```

Expected: one commit hash printed. (Screenshots are ignored because they are regenerated.)

---

### Task 1: Validation module (`build/checks.py`) with unit tests

**Files:**
- Create: `build/checks.py`
- Create: `build/tests/__init__.py` (empty), `build/tests/test_checks.py`

**Interfaces:**
- Produces: `PAUSE_IDS: frozenset[str]`, `EXEMPT_IDS: frozenset[str]`, `GENERATED_LAYOUTS: frozenset[str]`, `check_plan_fields(s: dict) -> list[str]`, `check_open_slide(sid: str, html: str) -> list[str]`, `check_participant_text(sid: str, html: str, layout: str) -> list[str]`, `check_whole_output(html: str) -> list[str]`, `pause_kind(body_html: str) -> str` (returns `'vote'` or `'reveal'`).

- [ ] **Step 1: Write the failing tests**

`build/tests/test_checks.py`:

```python
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import checks


class TestSets(unittest.TestCase):
    def test_pause_ids_exact(self):
        self.assertEqual(checks.PAUSE_IDS, frozenset(
            'SL05 SL06 SL11 SL16 SL25 SL26 SL31 SL36 SL49 SL53 SL57 SL62 SL63 SL64 SL65 SL73'.split()))
        self.assertEqual(len(checks.PAUSE_IDS), 16)

    def test_exempt_ids(self):
        self.assertEqual(checks.EXEMPT_IDS, frozenset({'SL01', 'SL18', 'SL40', 'SL59', 'SL76'}))


class TestPlanFields(unittest.TestCase):
    def base(self, **kw):
        s = {'id': 'SL03', 'layout': 'email', 'what_this_shows': 'x', 'key_point': 'y', 'pause_point': False}
        s.update(kw)
        return s

    def test_ok(self):
        self.assertEqual(checks.check_plan_fields(self.base()), [])

    def test_missing_what(self):
        self.assertTrue(checks.check_plan_fields(self.base(what_this_shows='')))

    def test_exempt_needs_nothing(self):
        self.assertEqual(checks.check_plan_fields({'id': 'SL18', 'layout': 'intermission', 'pause_point': False}), [])

    def test_pause_flag_must_match_list(self):
        self.assertTrue(checks.check_plan_fields(self.base(id='SL05', pause_point=False)))
        self.assertTrue(checks.check_plan_fields(self.base(id='SL03', pause_point=True)))


class TestOpenSlide(unittest.TestCase):
    def test_clean_open_slide(self):
        self.assertEqual(checks.check_open_slide('SL03', '<div class="mail"><p>hi</p></div>'), [])

    def test_rejects_toggle_and_hidden(self):
        errs = checks.check_open_slide('SL03', '<button data-act="toggle"></button><p hidden>x</p>')
        self.assertEqual(len(errs), 2)

    def test_word_hidden_in_text_is_fine(self):
        self.assertEqual(checks.check_open_slide('SL03', '<p>The hidden fact is shown.</p>'), [])

    def test_rejects_reveal_classes(self):
        self.assertTrue(checks.check_open_slide('SL03', '<p class="callout if-revealed">x</p>'))

    def test_allows_navigation_actions(self):
        self.assertEqual(checks.check_open_slide('SL01', '<button data-act="next">Go</button>'), [])
        self.assertEqual(checks.check_open_slide('SL76', '<button data-act="sources">S</button>'), [])


class TestParticipantText(unittest.TestCase):
    def test_clock_time_on_break(self):
        self.assertTrue(checks.check_participant_text('SL18', '<p>Back at 11:15</p>', 'intermission'))

    def test_clock_time_allowed_in_evidence(self):
        self.assertEqual(checks.check_participant_text('SL03', '<span>Tuesday, 16:42</span>', 'email'), [])

    def test_prayer_anywhere(self):
        self.assertTrue(checks.check_whole_output('<p>Lunch and Prayer</p>'))
        self.assertEqual(checks.check_whole_output('<p>Lunch break</p>'), [])


class TestPauseKind(unittest.TestCase):
    def test_kinds(self):
        self.assertEqual(checks.pause_kind('<div data-choice-group="SL05"></div>'), 'vote')
        self.assertEqual(checks.pause_kind('<div class="if-revealed"></div>'), 'reveal')


if __name__ == '__main__':
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `touch build/tests/__init__.py && python3 -m unittest discover -s build/tests -v`
Expected: FAIL/ERROR with `ModuleNotFoundError: No module named 'checks'`.

- [ ] **Step 3: Implement `build/checks.py`**

```python
"""Pure validation rules for the clarity rework (spec 2026-10-02 §4, §5, §7, §10)."""
import re

PAUSE_IDS = frozenset('SL05 SL06 SL11 SL16 SL25 SL26 SL31 SL36 SL49 SL53 SL57 SL62 SL63 SL64 SL65 SL73'.split())
EXEMPT_IDS = frozenset({'SL01', 'SL18', 'SL40', 'SL59', 'SL76'})
GENERATED_LAYOUTS = frozenset({'agenda', 'opener', 'takeaway', 'recap'})
NO_CLOCK_LAYOUTS = frozenset({'intermission', 'agenda', 'opener', 'takeaway', 'recap'})
NAV_ACTS = frozenset({'next', 'sources'})
CLOCK = re.compile(r'(?<![\d:])(?:[01]?\d|2[0-3]):[0-5]\d(?![\d:])')


def check_plan_fields(s):
    errs = []
    sid = s['id']
    if bool(s.get('pause_point')) != (sid in PAUSE_IDS):
        errs.append(f'{sid}: pause_point flag must be {sid in PAUSE_IDS}')
    if sid not in EXEMPT_IDS:
        for f in ('what_this_shows', 'key_point'):
            if not (s.get(f) or '').strip():
                errs.append(f'{sid}: {f} is required')
    return errs


def check_open_slide(sid, html):
    errs = []
    for act in re.findall(r'data-act="([^"]+)"', html):
        if act not in NAV_ACTS:
            errs.append(f'{sid}: open slide has interactive control data-act="{act}"')
    if re.search(r'<[^>]*\shidden(?=[\s>=])[^>]*>', html):
        errs.append(f'{sid}: open slide hides content (hidden attribute)')
    if re.search(r'\bif-(?:un)?revealed\b', html):
        errs.append(f'{sid}: open slide uses reveal-only classes')
    return errs


def check_participant_text(sid, html, layout):
    if layout in NO_CLOCK_LAYOUTS:
        text = re.sub(r'<[^>]+>', ' ', html)
        m = CLOCK.search(text)
        if m:
            return [f'{sid}: clock time "{m.group(0)}" on a {layout} slide']
    return []


def check_whole_output(html):
    return ['"prayer" appears in the deck'] if re.search(r'prayer', html, re.I) else []


def pause_kind(body_html):
    return 'vote' if 'data-choice-group' in body_html else 'reveal'
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest discover -s build/tests -v`
Expected: all tests in `test_checks` PASS.

- [ ] **Step 5: Commit**

```bash
git add build/checks.py build/tests && git commit -qm "feat(build): validation rules for clarity rework"
```

---

### Task 2: Photo avatars (`make_avatars.py` + `build/avatars.py`)

**Files:**
- Create: `build/tools/make_avatars.py`, `src/img/avatars/*.jpg` (generated), `build/avatars.py`, `build/tests/test_avatars.py`

**Interfaces:**
- Produces: `CAST: dict[str, tuple[str, str]]` (key → (name, role)); `avatar_html(key: str, cls: str = 'avatar', alt: str = '') -> str`; `cast_html(keys: list[str]) -> str`.

- [ ] **Step 1: Write the dev tool and generate avatars**

`build/tools/make_avatars.py`:

```python
#!/usr/bin/env python3
"""Dev-only: shrink the AI-generated portraits into small JPEG avatars (needs Pillow).
Source: dist/Image_ref/profile-pictures/*.png  ->  src/img/avatars/*.jpg (192x192)."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'dist/Image_ref/profile-pictures'
OUT = ROOT / 'src/img/avatars'
OUT.mkdir(parents=True, exist_ok=True)
for name in ['aina', 'farid', 'mei', 'ravi', 'nadia', 'siti', 'daniel', 'lina', 'it-caller']:
    im = Image.open(SRC / f'{name}.png').convert('RGB')
    side = min(im.size)
    left, top = (im.width - side) // 2, (im.height - side) // 2
    im = im.crop((left, top, left + side, top + side)).resize((192, 192), Image.LANCZOS)
    im.save(OUT / f'{name}.jpg', 'JPEG', quality=80, optimize=True, progressive=True)
    print(name, (OUT / f'{name}.jpg').stat().st_size, 'bytes')
```

Run: `python3 build/tools/make_avatars.py`
Expected: nine lines, each size below 20000 bytes.

- [ ] **Step 2: Write the failing tests**

`build/tests/test_avatars.py`:

```python
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import avatars


class TestAvatars(unittest.TestCase):
    def test_cast_complete(self):
        self.assertEqual(set(avatars.CAST), {'aina', 'farid', 'mei', 'ravi', 'nadia', 'siti', 'daniel', 'lina', 'it-caller'})

    def test_photo_embedded(self):
        h = avatars.avatar_html('aina')
        self.assertTrue(h.startswith('<img class="avatar photo" src="data:image/jpeg;base64,'))
        self.assertIn('alt=""', h)

    def test_alt_and_class(self):
        h = avatars.avatar_html('ravi', cls='pavatar', alt='Ravi, Manager')
        self.assertIn('class="pavatar photo"', h)
        self.assertIn('alt="Ravi, Manager"', h)

    def test_missing_file_falls_back_to_initial(self):
        h = avatars.avatar_html('nobody')
        self.assertEqual(h, '<span class="avatar" aria-hidden="true">N</span>')

    def test_cast_html_has_names_and_roles(self):
        h = avatars.cast_html(['aina', 'farid'])
        self.assertIn('<strong>Aina</strong>Operations', h)
        self.assertIn('<strong>Farid</strong>Finance', h)


if __name__ == '__main__':
    unittest.main()
```

Run: `python3 -m unittest build.tests.test_avatars -v 2>&1 | tail -3` (or `discover`). Expected: FAIL `No module named 'avatars'`.

- [ ] **Step 3: Implement `build/avatars.py`**

```python
"""Embedded character portraits (AI-generated; spec §6). Falls back to an initial if a file is missing."""
import base64
import html
from pathlib import Path

IMG_DIR = Path(__file__).resolve().parents[1] / 'src/img/avatars'
CAST = {
    'aina': ('Aina', 'Operations'),
    'farid': ('Farid', 'Finance'),
    'mei': ('Mei', 'IT support'),
    'ravi': ('Ravi', 'Manager'),
    'nadia': ('Nadia', 'Supplier contact, Maju Supplies'),
    'siti': ('Siti', 'Communications'),
    'daniel': ('Daniel', 'Project contact, Riverside Partners'),
    'lina': ('Lina', 'HR'),
    'it-caller': ('Caller', 'Claims to be IT'),
}
_cache = {}


def _data_uri(key):
    if key not in _cache:
        p = IMG_DIR / f'{key}.jpg'
        _cache[key] = 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode() if p.is_file() else None
    return _cache[key]


def avatar_html(key, cls='avatar', alt=''):
    uri = _data_uri(key)
    if uri is None:
        return f'<span class="{cls}" aria-hidden="true">{html.escape(key[:1].upper())}</span>'
    return f'<img class="{cls} photo" src="{uri}" alt="{html.escape(alt, quote=True)}">'


def cast_html(keys):
    people = []
    for k in keys:
        name, role = CAST[k]
        people.append(f'<div class="person">{avatar_html(k)}<span><strong>{html.escape(name)}</strong>{html.escape(role)}</span></div>')
    return '<div class="cast">' + ''.join(people) + '</div>'
```

- [ ] **Step 4: Run tests**

Run: `python3 -m unittest discover -s build/tests -v`
Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add build/tools/make_avatars.py build/avatars.py build/tests/test_avatars.py src/img/avatars
git commit -qm "feat(build): embedded AI-generated character avatars with initial fallback"
```

---

### Task 3: Generated layouts (`build/generated.py`)

**Files:**
- Create: `build/generated.py`, `build/tests/test_generated.py`

**Interfaces:**
- Consumes: `avatars.cast_html(keys)`.
- Produces: `render_generated(s: dict, modules: list[dict], habits: list[tuple[str, str]]) -> str`. `s` is a slides.json entry with `layout` in `{'agenda','opener','takeaway','recap'}`. `habits` is `[(module_label, habit_text), ...]` for the recap. Uses fields: agenda → `outcomes`, `rules`; opener → `why`, `outcomes`, `cast`, optional `glossary` (list of `[term, definition]`), `module_label`; takeaway → `takeaways`, `habit`, `module_label`; recap → `key_point`. Always uses `title`, `what_this_shows`, and for opener/agenda `key_point`.

- [ ] **Step 1: Write the failing tests**

`build/tests/test_generated.py`:

```python
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generated

MODS = [{'id': 'M0', 'name': 'Opening baseline', 'kind': 'module'},
        {'id': 'B1', 'name': 'Short break', 'kind': 'break'},
        {'id': 'M1', 'name': 'The borrowed identity', 'kind': 'module'}]


class TestGenerated(unittest.TestCase):
    def test_opener(self):
        s = {'id': 'SL08', 'layout': 'opener', 'title': 'Module 1: The borrowed identity', 'module_label': 'Module 1',
             'what_this_shows': 'Why', 'why': 'Anyone can copy a name.', 'outcomes': ['A', 'B'], 'cast': ['aina'],
             'key_point': 'K', 'glossary': [['MFA', 'A second check']]}
        h = generated.render_generated(s, MODS, [])
        self.assertIn('<h1 id="SL08-title">Module 1: The borrowed identity</h1>', h)
        self.assertIn('Anyone can copy a name.', h)
        self.assertEqual(h.count('<li>'), 2)
        self.assertIn('<dt>MFA</dt><dd>A second check</dd>', h)
        self.assertIn('<strong>Aina</strong>', h)
        self.assertIn('class="keypoint"', h)

    def test_takeaway_habit(self):
        s = {'id': 'SL17', 'layout': 'takeaway', 'title': 'Module 1 takeaways', 'module_label': 'Module 1',
             'what_this_shows': 'W', 'takeaways': ['t1', 't2', 't3'], 'habit': 'Use the directory.', 'key_point': 'Use the directory.'}
        h = generated.render_generated(s, MODS, [])
        self.assertEqual(h.count('<li>'), 3)
        self.assertIn('Your habit from this module', h)
        self.assertIn('Use the directory.', h)

    def test_agenda_lists_modules_without_times(self):
        s = {'id': 'SL02', 'layout': 'agenda', 'title': 'Today’s workshop', 'what_this_shows': 'W',
             'outcomes': ['o1'], 'rules': ['r1'], 'key_point': 'K'}
        h = generated.render_generated(s, MODS, [])
        self.assertIn('Short break', h)
        self.assertIn('The borrowed identity', h)
        self.assertNotRegex(h, r'\d{1,2}:\d{2}')

    def test_recap(self):
        s = {'id': 'SL75', 'layout': 'recap', 'title': 'Today’s takeaways', 'what_this_shows': 'W', 'key_point': 'K'}
        h = generated.render_generated(s, MODS, [('Module 1', 'h1'), ('Module 2', 'h2')])
        self.assertIn('h1', h)
        self.assertIn('Module 2', h)

    def test_escapes(self):
        s = {'id': 'SL17', 'layout': 'takeaway', 'title': 'T', 'module_label': 'M', 'what_this_shows': '<b>',
             'takeaways': ['<i>'], 'habit': 'h', 'key_point': 'h'}
        h = generated.render_generated(s, MODS, [])
        self.assertIn('&lt;b&gt;', h)
        self.assertNotIn('<i>', h)


if __name__ == '__main__':
    unittest.main()
```

Run: `python3 -m unittest discover -s build/tests -v`. Expected: ERROR `No module named 'generated'`.

- [ ] **Step 2: Implement `build/generated.py`**

```python
"""HTML for slides generated from slides.json fields: agenda, module opener, module takeaway, day recap."""
import html
from avatars import cast_html


def e(x):
    return html.escape(str(x), quote=True)


def keypoint(text):
    return f'<div class="keypoint"><b>Key point</b><span>{e(text)}</span></div>'


def _ul(items, cls=''):
    return f'<ul class="{cls}">' + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ul>'


def _ol(items, cls=''):
    return f'<ol class="{cls}">' + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ol>'


def render_generated(s, modules, habits):
    sid, lay = s['id'], s['layout']
    head = (f'<p class="kicker">{e(s.get("module_label", "Today"))}</p>'
            f'<h1 id="{sid}-title">{e(s["title"])}</h1><p class="sub">{e(s["what_this_shows"])}</p>')
    if lay == 'agenda':
        agenda = ''.join(
            f'<li class="{"brk" if m["kind"] == "break" else ""}">'
            f'{"" if m["kind"] == "break" else e(("Opening" if m["id"] == "M0" else "Module " + m["id"][1:]) + " · ")}{e(m["name"])}</li>'
            for m in modules)
        return (f'<div class="gen agenda"><div>{head}<p class="eyebrow">Today you will be able to</p>{_ul(s["outcomes"], "outcomes")}</div>'
                f'<div class="scene"><p class="eyebrow">The day</p><ol class="daylist">{agenda}</ol>'
                f'<p class="eyebrow">How we work today</p>{_ul(s["rules"], "rules")}</div></div>{keypoint(s["key_point"])}')
    if lay == 'opener':
        gloss = ''
        if s.get('glossary'):
            gloss = ('<p class="eyebrow">Words we will use</p><dl class="glossary">'
                     + ''.join(f'<dt>{e(t)}</dt><dd>{e(d)}</dd>' for t, d in s['glossary']) + '</dl>')
        return (f'<div class="gen opener"><div>{head}<p class="eyebrow">Why this matters</p><p class="why">{e(s["why"])}</p>'
                f'<p class="eyebrow">Who you will meet</p>{cast_html(s["cast"])}</div>'
                f'<div class="scene"><p class="eyebrow">By the end you will be able to</p>{_ul(s["outcomes"], "outcomes")}{gloss}</div></div>'
                f'{keypoint(s["key_point"])}')
    if lay == 'takeaway':
        return (f'<div class="gen takeaway"><div>{head}</div><div class="scene">{_ol(s["takeaways"], "tlist")}'
                f'<div class="habit"><p class="eyebrow">Your habit from this module</p><p class="habittext">{e(s["habit"])}</p></div></div></div>')
    if lay == 'recap':
        rows = ''.join(f'<li><span class="hmod">{e(m)}</span><span>{e(h)}</span></li>' for m, h in habits)
        return (f'<div class="gen recap"><div>{head}</div><div class="scene"><p class="eyebrow">Seven habits</p>'
                f'<ol class="habits">{rows}</ol></div></div>{keypoint(s["key_point"])}')
    raise ValueError(f'{sid}: unknown generated layout {lay}')
```

Note: the recap passes module labels for habit rows and its `kicker` is "Today". The takeaway template renders the habit box instead of a separate key point (its `key_point` equals the habit).

- [ ] **Step 3: Run tests**

Run: `python3 -m unittest discover -s build/tests -v`
Expected: all PASS.

- [ ] **Step 4: Commit**

```bash
git add build/generated.py build/tests/test_generated.py && git commit -qm "feat(build): generated agenda/opener/takeaway/recap layouts"
```

---

### Task 4: Migration to 76 slides

**Files:**
- Create: `build/tools/migrate_v2.py`, `build/tests/test_migration.py`
- Modify (by running the script): `04-content/slides.json`, `src/slides/*.html`, `src/content/choices.json`, `src/content/notes.json`, `src/content/modules.json`, `build/make_docs.py`

**Interfaces:**
- Produces: slides.json entries with `what_this_shows`, `key_point`, `pause_point` on every slide; opener entries with `why`, `outcomes`, `cast`, `module_label` (+`glossary` on SL41); takeaway entries with `takeaways`, `habit`, `module_label`; agenda SL02 with `outcomes`, `rules`; recap SL75. Fragment and data IDs renamed to new numbers.

- [ ] **Step 1: Write the failing test** (checks the migrated plan)

`build/tests/test_migration.py`:

```python
import json, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'build'))
import checks


class TestMigratedPlan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = json.loads((ROOT / '04-content/slides.json').read_text(encoding='utf-8'))
        cls.s = cls.plan['slides']

    def test_count_and_ids(self):
        self.assertEqual(self.plan['slide_count'], 76)
        self.assertEqual([x['id'] for x in self.s], [f'SL{i:02d}' for i in range(1, 77)])

    def test_timing(self):
        self.assertEqual(sum(x['duration_minutes'] for x in self.s), 420)
        totals = {}
        for x in self.s:
            totals[x['module']] = totals.get(x['module'], 0) + x['duration_minutes']
        self.assertEqual(totals, {'M0': 20, 'M1': 45, 'B1': 10, 'M2': 45, 'M3': 60, 'B2': 75, 'M4': 50,
                                  'M5': 35, 'B3': 25, 'M6': 35, 'M7': 20})
        self.assertEqual(self.s[0]['planned_start'], '10:00')
        self.assertEqual(self.s[-1]['planned_end'], '17:00')

    def test_fields(self):
        for x in self.s:
            self.assertEqual(checks.check_plan_fields(x), [], x['id'])

    def test_breaks_renamed(self):
        self.assertEqual([self.s[i]['title'] for i in (17, 39, 58)], ['Short break', 'Lunch break', 'Tea break'])

    def test_no_prayer_in_plan(self):
        self.assertNotRegex(json.dumps(self.plan), '(?i)prayer')

    def test_fragments_renamed(self):
        ids = set()
        for f in (ROOT / 'src/slides').glob('*.html'):
            ids |= set(__import__('re').findall(r'data-slide="(SL\d\d)"', f.read_text(encoding='utf-8')))
        generated = {x['id'] for x in self.s if x['layout'] in checks.GENERATED_LAYOUTS}
        self.assertEqual(ids | generated, {x['id'] for x in self.s})
        self.assertFalse(ids & generated)


if __name__ == '__main__':
    unittest.main()
```

Run: `python3 -m unittest build.tests.test_migration -v 2>&1 | tail -3` from the package root with `python3 -m unittest discover -s build/tests -v`.
Expected: FAIL (`slide_count` is 61).

- [ ] **Step 2: Write `build/tools/migrate_v2.py`**

```python
#!/usr/bin/env python3
"""One-off migration for the clarity rework (spec 2026-10-02). Refuses to run twice."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / '04-content/slides.json'
plan = json.loads(PLAN.read_text(encoding='utf-8'))
if plan['slide_count'] != 61:
    raise SystemExit('Already migrated (slide_count != 61).')
old = {s['id']: s for s in plan['slides']}

# New order: old IDs ("SLxx") or new-slide keys ("+key").
ORDER = ['SL01', '+today', 'SL02', 'SL03', 'SL04', 'SL05', 'SL06',
         '+m1o', 'SL07', 'SL08', 'SL09', 'SL10', 'SL11', 'SL12', 'SL13', 'SL14', '+m1t',
         'SL15',
         '+m2o', 'SL16', 'SL17', 'SL18', 'SL19', 'SL20', 'SL21', 'SL22', '+m2t',
         '+m3o', 'SL23', 'SL24', 'SL25', 'SL26', 'SL27', 'SL28', 'SL29', 'SL30', 'SL31', 'SL32', '+m3t',
         'SL33',
         '+m4o', 'SL34', 'SL35', 'SL36', 'SL37', 'SL38', 'SL39', 'SL40', 'SL41', '+m4t',
         '+m5o', 'SL42', 'SL43', 'SL44', 'SL45', 'SL46', 'SL47', '+m5t',
         'SL48',
         '+m6o', 'SL49', 'SL50', 'SL51', 'SL52', 'SL53', 'SL54', '+m6t',
         '+m7o', 'SL55', 'SL56', 'SL57', 'SL58', 'SL59', 'SL60', '+recap', 'SL61']
assert len(ORDER) == 76
MINUTES = [1, 3, 3, 3, 4, 3, 3,
           2, 3, 6, 6, 4, 5, 7, 5, 5, 2,
           10,
           2, 4, 6, 6, 6, 7, 7, 5, 2,
           2, 5, 6, 5, 5, 5, 5, 5, 8, 7, 5, 2,
           75,
           3, 5, 6, 5, 8, 6, 5, 5, 5, 2,
           2, 4, 6, 5, 6, 5, 5, 2,
           25,
           2, 2, 6, 7, 7, 7, 2, 2,
           1, 2, 5, 3, 2, 3, 1, 2, 1]
assert len(MINUTES) == 76 and sum(MINUTES) == 420
OLD_TO_NEW = {o: f'SL{i + 1:02d}' for i, o in enumerate(ORDER) if not o.startswith('+')}
NEW_KEY = {o: f'SL{i + 1:02d}' for i, o in enumerate(ORDER) if o.startswith('+')}
PAUSE = set('SL05 SL06 SL11 SL16 SL25 SL26 SL31 SL36 SL49 SL53 SL57 SL62 SL63 SL64 SL65 SL73'.split())

# what_this_shows / key_point for every non-exempt slide, keyed by NEW id.
TEXT = {
 'SL02': ('What we will practise today, in what order, and how we will work together.',
          'Today is about one habit: when a message asks for money, information or access, check it through a route you already trust.'),
 'SL03': ('Farid gets an expected invoice email from a known supplier, but the bank details have changed.',
          'A correct sender address and a familiar conversation do not prove who is writing. A change to bank details always needs an independent check.'),
 'SL04': ('A chat using the manager’s name pushes Farid to pay quickly.',
          'A display name and urgency tell you nothing about who controls the account. Pressure to skip a check is a reason to slow down.'),
 'SL05': ('Your first decision of the day: what should Farid do next?',
          'Verify through a contact you already hold, such as the supplier record, then follow the normal approval process. Replying to the same email cannot verify anything.'),
 'SL06': ('Farid calls the supplier on the number already held in the finance system.',
          'Independent verification gives you facts the message never could. Hold the payment, keep the evidence and report.'),
 'SL07': ('A real case: a fabricated video meeting helped convince an employee to transfer about HK$200 million.',
          'Even a convincing meeting can be fabricated. A separate, authorised payment check is what stops the loss.'),
 'SL08': ('What this module covers and why it matters.',
          'Identity on a screen is easy to borrow. Verify the person through a route you already trust.'),
 'SL09': ('Three words we use all day, and how they overlap in one attack.',
          'Impersonation borrows a trusted identity; phishing asks you to act; spear phishing aims at you specifically. One message can do all three.'),
 'SL10': ('Everything on Aina’s public profile that a stranger could reuse.',
          'Public work details make a fake message feel expected. Knowing them does not prove the sender works with you.'),
 'SL11': ('Two profiles with the same photo, name and posts. Can you tell which is real?',
          'You cannot tell from the screen. Photos, names, posts and follower counts can all be copied. Contact the person through the staff directory.'),
 'SL12': ('A real colleague’s account asks Aina for the full staff contact list.',
          'A genuine account can still be used by someone else, and even a genuine request needs permission. Verify the purpose separately and share only what is needed.'),
 'SL13': ('Aina complains publicly about a login problem and “support” replies within minutes.',
          'If support found you, do not use it. Start from the app, your saved bookmark or your IT helpdesk.'),
 'SL14': ('A friendly professional contact builds trust, then asks for a sign-in and internal documents.',
          'Re-check whenever a conversation reaches money, access or information, however friendly it has been.'),
 'SL15': ('What to do when someone pretends to be you, and how that differs from someone taking over your account.',
          'A copied profile needs a platform report; a taken-over account needs official recovery. Both need you to warn contacts through a trusted channel.'),
 'SL16': ('A familiar profile asks Farid for a supplier contract.',
          'Verify through the staff directory, then check the contract may be shared that way.'),
 'SL17': ('What to remember from Module 1.', 'Contact people through the directory, not through the message.'),
 'SL19': ('What this module covers and why it matters.', 'Urgency and authority are reasons to check, not reasons to skip the check.'),
 'SL20': ('“Ravi” asks Farid to pay a new supplier now and approve it later.',
          'Normal approval still applies when the deadline is close. Confirm with Ravi on his directory number.'),
 'SL21': ('The three pressure tactics hidden in one short message.',
          'Urgency, secrecy and “I’ll approve it later” all try to remove a check. The risk is the exception, even if the sender is genuine.'),
 'SL22': ('Practise saying “not yet” politely to someone senior.',
          'Name the route and the next step: “I’ll call you back on your directory number, then raise it for approval.”'),
 'SL23': ('A caller knows Aina’s name and manager, and asks her to read out a code.',
          'Knowing names proves nothing. Hang up and call the service desk on its known number. Never read out a sign-in code.'),
 'SL24': ('Why spotting a fake video is not a reliable defence.',
          'Do not rely on spotting glitches. A separate, authorised payment process works whether the video is real or fake.'),
 'SL25': ('A bank-change email gives Farid a new number to call.',
          'Call the number already in your records, never one supplied with the change.'),
 'SL26': ('The supplier confirms the bank change is real. Can Farid pay now?',
          'Verification checks who is asking. Authorisation decides whether it may happen. A genuine change still goes through approval.'),
 'SL27': ('What to remember from Module 2.', 'Call back on a number you already have before you pay, reset or share.'),
 'SL28': ('What this module covers and why it matters.',
          'Ask three questions of every message: who is asking, what would I authorise, and how can I check outside this message?'),
 'SL29': ('Three ordinary work messages, each asking for a different risky action.',
          'Look for the action: sign in, share data, open a file. Then verify outside the message. Any of these could be genuine.'),
 'SL30': ('What the full sender address reveals behind the display name.',
          'A mismatched address is a warning sign, but a matching one does not prove safety. Verify the request itself.'),
 'SL31': ('Who really controls this link? Vote, then see how to read it.',
          'Read the web address from the right, up to the first single slash. The last part, attacker.test, owns the site.'),
 'SL32': ('Two professional-looking messages: one genuine, one deceptive.',
          'Polish and logos prove nothing. Judge the action requested and check it in the system you normally use.'),
 'SL33': ('The same kind of request on a phone screen, where details are hidden.',
          'Phones hide the full sender and link. Open the app or website yourself instead of tapping the message.'),
 'SL34': ('A QR code that moves a sign-in request onto your phone.',
          'Treat a QR code like a link you cannot read. Use the known portal instead.'),
 'SL35': ('Shared files and attachments that lead to a sign-in or download.',
          'A file type or brand does not make it safe. If you did not expect it, check with the sender through a known contact first.'),
 'SL36': ('Four realistic requests: decide for each whether to proceed, verify first, or hold and report.',
          'Some requests are genuine. The right answer depends on the action and the route, not on calling everything phishing.'),
 'SL37': ('Six common “safety signs” and what each one really proves.',
          'Logos, padlocks, known senders and completed MFA do not validate the request. HTTPS still matters: it protects the connection.'),
 'SL38': ('The three trusted routes you can use to check any request.',
          'Use a known app or bookmark, an established contact, or your organisation’s process. Never the contact details inside the message.'),
 'SL39': ('What to remember from Module 3.', 'Go to the app or website yourself instead of using the link.'),
 'SL41': ('What this module covers, and the words we will use.',
          'Before approving anything, ask: what does this give, and to whom? Did I start it?'),
 'SL42': ('Four ways to give someone access without sharing a password.',
          'A session, an MFA approval, an app permission or a linked device can each let someone act as you.'),
 'SL43': ('How a fake sign-in page can capture a working login, even with MFA.',
          'Sign in from your bookmark or app, not from a link. Phishing-resistant MFA, such as security keys and passkeys, blocks this relay.'),
 'SL44': ('Sign-in prompts arrive late at night while Aina is not signing in.',
          'Deny any prompt you did not start and report it. Never approve just to make the prompts stop.'),
 'SL45': ('A genuine sign-in page asks for a code that someone else sent Aina.',
          'Only enter a code for a sign-in you started yourself. Here the code would sign in the sender’s device as Aina.'),
 'SL46': ('A meeting app asks for far more access than it needs.',
          'A real permission screen does not make the app trustworthy. Ask IT to approve apps through the normal process.'),
 'SL47': ('The difference between joining a group and linking a device.',
          'Linking gives another device ongoing access to your account. Link only devices you own and set up yourself.'),
 'SL48': ('A real case where staff entered passwords but security keys stopped the attack.',
          'Strong controls and quick reporting work together. Some MFA types resist phishing much better than others.'),
 'SL49': ('A trusted service asks you to approve an unfamiliar session.',
          'Check where the request came from through a route you know. If you did not start it, deny it and report it.'),
 'SL50': ('What to remember from Module 4.', 'Approve only what you started and recognise.'),
 'SL51': ('What this module covers and why it matters.', 'Real help can be checked: a ticket you raised, through a portal or number you know.'),
 'SL52': ('Someone using Mei’s name and photo offers to fix a problem Aina never reported.',
          'Verify a support offer with the helpdesk through a route you know. A name and photo in chat prove nothing.'),
 'SL53': ('A remote-control request appears on Aina’s screen.',
          'No ticket, no session. Check with the helpdesk first, and never send a login code to prove anything.'),
 'SL54': ('A fake “are you human?” check ends by asking you to run something on your computer.',
          'No real check asks you to open a system tool and paste text. Stop, close it and contact IT.'),
 'SL55': ('A documented technique: a fake extension breaks your browser, then offers a harmful “fix”.',
          'Install software and get fixes only through approved sources and your IT team.'),
 'SL56': ('An unexpected renewal notice urges Farid to call a number.',
          'Check the account through the service or team you already know, not the number in the notice.'),
 'SL57': ('This time the support request matches a ticket Aina raised herself.',
          'Verified help can go ahead under normal rules: stay present and share only what the fix needs.'),
 'SL58': ('What to remember from Module 5.', 'No ticket you raised, no remote access.'),
 'SL60': ('What this module covers and why it matters.',
          'You do not need the full picture to report. Report what you saw and let the right team connect the dots.'),
 'SL61': ('Your table becomes the Meranti team. Each role checks different things.',
          'Every role matters: operations spots the request, finance holds payments, managers protect time to check, IT handles access.'),
 'SL62': ('Evidence card 1: a document invitation after a normal call.', 'Use a known route before signing in or sharing.'),
 'SL63': ('Evidence card 2: Aina admits she entered a code.',
          'Report immediately, thank the reporter, and let IT review access. Do not wait for proof.'),
 'SL64': ('Evidence card 3: a bank change plus an urgent chat from “Ravi”.',
          'Hold, call back from records and keep approvals. A link to card 2 is a guess until IT confirms it.'),
 'SL65': ('Evidence card 4: an unrequested offer to take control of a screen.',
          'Verify with the helpdesk, allow no control, and report facts and uncertainty together.'),
 'SL66': ('Which decisions stopped the chain, and what is still unknown.',
          'Independent checks, normal approval and early reporting each reduced the risk.'),
 'SL67': ('What to remember from Module 6.', 'Report early, even if you are not sure.'),
 'SL68': ('What this module covers and why it matters.', 'Reporting a mistake quickly is the right thing to do, and it is never blamed.'),
 'SL69': ('Four steps to remember for any suspicious request.', 'Pause, verify, report, recover. This is our course summary, not an official framework.'),
 'SL70': ('How to report at your organisation, step by step.',
          'Keep the original, say what happened and when, and use another channel if your account may be affected.'),
 'SL71': ('What to do depends on what happened.',
          'A password reset alone may not remove access. Report early so the right team can check sessions, apps and devices.'),
 'SL72': ('The difference between a vague report and a useful one.',
          'Include the time, channel, who it claimed to be, what you did and which device. Never include passwords or codes.'),
 'SL73': ('A new situation: a genuine HR colleague asks for staff records.',
          'A genuine requester still needs a permitted reason and the approved sharing route.'),
 'SL74': ('Your commitment for tomorrow.', 'Pick one request you handle at work and the route you will use to check it.'),
 'SL75': ('The seven habits from today, in one place.',
          'When a message asks for money, information or access: pause, check through a route you already trust, and report anything unusual.'),
}

HABIT = {'+m1t': 'Contact people through the directory, not through the message.',
         '+m2t': 'Call back on a number you already have before you pay, reset or share.',
         '+m3t': 'Go to the app or website yourself instead of using the link.',
         '+m4t': 'Approve only what you started and recognise.',
         '+m5t': 'No ticket you raised, no remote access.',
         '+m6t': 'Report early, even if you are not sure.'}

NEW = {
 '+today': dict(module='M0', title='Today’s workshop', layout='agenda', module_label='Today',
   outcomes=['Spot when a message asks for money, information or access',
             'Check requests through a route you already trust',
             'Know what an approval, code or app permission really gives away',
             'Report quickly and usefully, including your own mistakes'],
   rules=['Everything in today’s story is fictional; real cases are labelled',
          'There are no wrong questions',
          'Nobody needs to share a personal incident',
          'Reporting is never blamed: thank people for speaking up']),
 '+m1o': dict(module='M1', title='Module 1: The borrowed identity', layout='opener', module_label='Module 1',
   why='Anyone can copy a name, photo and job title, and messages that borrow a familiar identity get trusted.',
   outcomes=['Tell a copied profile from a genuine account someone else controls',
             'Spot when a friendly conversation turns into a sensitive request',
             'Respond if someone uses your name'],
   cast=['aina', 'siti', 'daniel', 'farid']),
 '+m1t': dict(module='M1', title='Module 1 takeaways', layout='takeaway', module_label='Module 1',
   takeaways=['Photos, names and job titles are easy to copy.',
              'A real account can be misused, and a real request can still need permission.',
              'Re-check when a chat turns to money, access or information.']),
 '+m2o': dict(module='M2', title='Module 2: The trusted request', layout='opener', module_label='Module 2',
   why='Attackers borrow authority and urgency because people want to help their manager and meet deadlines.',
   outcomes=['Name the pressure tactics in an urgent request',
             'Pause politely without refusing outright',
             'Verify payments and calls through records you already hold'],
   cast=['ravi', 'farid', 'nadia', 'it-caller']),
 '+m2t': dict(module='M2', title='Module 2 takeaways', layout='takeaway', module_label='Module 2',
   takeaways=['Urgency, secrecy and “approve it later” are pressure tactics.',
              'A face, a voice or a caller’s inside knowledge does not prove identity.',
              'Genuine requests still follow the approval process.']),
 '+m3o': dict(module='M3', title='Module 3: The message that fits your job', layout='opener', module_label='Module 3',
   why='The most convincing messages look like ordinary work: an invitation, a shared file, an account notice.',
   outcomes=['Find the action a message is asking you to take',
             'Read sender addresses and links without opening them',
             'Recognise “safety signs” that prove nothing'],
   cast=['aina', 'farid', 'ravi', 'nadia']),
 '+m3t': dict(module='M3', title='Module 3 takeaways', layout='takeaway', module_label='Module 3',
   takeaways=['Find the action the message wants.',
              'Read addresses and links without opening them.',
              'Polish, padlocks and logos are not proof.']),
 '+m4o': dict(module='M4', title='Module 4: Beyond the password', layout='opener', module_label='Module 4',
   why='Attackers no longer need your password if you approve a sign-in, a code, an app or a device for them.',
   outcomes=['Explain what an approval actually grants',
             'Respond to sign-in prompts you did not start',
             'Recognise code, app-permission and device-linking tricks'],
   cast=['aina', 'mei'],
   glossary=[['MFA', 'A second check when you sign in, such as an app prompt or a code'],
             ['Session', 'Staying signed in after you log in, so you are not asked again'],
             ['Device code', 'A short code that signs another device in to your account'],
             ['App permission', 'Letting an app read or change your mail and files'],
             ['Linked device', 'Another phone or computer that can use your account'],
             ['Phishing-resistant MFA', 'Security keys or passkeys that only work on the real site']]),
 '+m4t': dict(module='M4', title='Module 4 takeaways', layout='takeaway', module_label='Module 4',
   takeaways=['Approvals, codes, apps and linked devices can all grant access.',
              'MFA helps, but never approve something you did not start.',
              'A genuine sign-in page can still sign in someone else.']),
 '+m5o': dict(module='M5', title='Module 5: The helpful stranger', layout='opener', module_label='Module 5',
   why='Fake IT help, fake “verification” pages and fake renewal notices all try to get you to let them in.',
   outcomes=['Check a support request before giving access',
             'Stop when a web page asks you to run something',
             'Tell genuine support from a fake offer'],
   cast=['mei', 'aina', 'farid']),
 '+m5t': dict(module='M5', title='Module 5 takeaways', layout='takeaway', module_label='Module 5',
   takeaways=['Unrequested help is a warning sign.',
              'Never run instructions that a web page gives you.',
              'Genuine support can be checked and still follows the rules.']),
 '+m6o': dict(module='M6', title='Module 6: Stop the chain', layout='opener', module_label='Module 6',
   why='Real incidents rarely look like one obvious attack. They look like several small, separate events.',
   outcomes=['Work as a team across operations, finance, management and IT',
             'Separate facts from guesses',
             'Report early, before you know everything'],
   cast=['aina', 'farid', 'ravi', 'mei']),
 '+m6t': dict(module='M6', title='Module 6 takeaways', layout='takeaway', module_label='Module 6',
   takeaways=['Small events can be connected, so report each one.',
              'Keep facts and guesses separate.',
              'Early reporting gives IT time to act.']),
 '+m7o': dict(module='M7', title='Module 7: Report and recover', layout='opener', module_label='Module 7',
   why='Mistakes happen. Fast, honest reporting limits the damage.',
   outcomes=['Use your organisation’s reporting route',
             'Write a report that helps the response team',
             'Know what to do after different kinds of mistake'],
   cast=['aina', 'lina', 'mei']),
 '+recap': dict(module='M7', title='Today’s takeaways', layout='recap', module_label='Today'),
}
for k, v in HABIT.items():
    NEW[k]['habit'] = v

# ---- build the new slide list
slides = []
for i, key in enumerate(ORDER):
    sid = f'SL{i + 1:02d}'
    if key.startswith('+'):
        n = NEW[key]
        s = {'id': sid, 'module': n['module'], 'title': n['title'], 'duration_minutes': 0, 'layout': n['layout'],
             'objective': TEXT[sid][0], 'screen_text': n.get('outcomes') or n.get('takeaways') or [TEXT[sid][1]],
             'evidence': '', 'interaction': '', 'reveal': '',
             'facilitator_notes': 'Read the slide aloud briefly; it frames the module. No hidden content.',
             'source_ids': [], 'evidence_kind': 'guidance', 'options': []}
        s.update({k: v for k, v in n.items() if k not in ('module', 'title', 'layout')})
    else:
        s = dict(old[key])
        s['id'] = sid
    s['duration_minutes'] = MINUTES[i]
    s['pause_point'] = sid in PAUSE
    if sid in TEXT:
        s['what_this_shows'], s['key_point'] = TEXT[sid]
    slides.append(s)

# breaks
for sid, title, nxt in (('SL18', 'Short break', 'Module 2 · The trusted request'),
                        ('SL40', 'Lunch break', 'Module 4 · Beyond the password'),
                        ('SL59', 'Tea break', 'Module 6 · Stop the chain')):
    b = slides[int(sid[2:]) - 1]
    b.update(title=title, objective='Scheduled break', screen_text=[title, f'We return with {nxt}'],
             facilitator_notes='Break. Restart on time; nothing advances automatically.')

# times
t = 10 * 60
for s in slides:
    s['planned_start'] = f'{t // 60:02d}:{t % 60:02d}'
    t += s['duration_minutes']
    s['planned_end'] = f'{t // 60:02d}:{t % 60:02d}'
assert slides[-1]['planned_end'] == '17:00'

plan['slides'] = slides
plan['slide_count'] = 76
plan['version'] = '2.0'
PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---- rename IDs in other files (single pass, old -> new)
rx = re.compile(r'SL(\d\d)(?!\d)')


def ren(text):
    return rx.sub(lambda m: OLD_TO_NEW.get(m.group(0), m.group(0)), text)


for p in list((ROOT / 'src/slides').glob('*.html')) + [ROOT / 'build/make_docs.py']:
    p.write_text(ren(p.read_text(encoding='utf-8')), encoding='utf-8')
for name in ('choices.json', 'notes.json'):
    p = ROOT / 'src/content' / name
    data = json.loads(ren(p.read_text(encoding='utf-8')))
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# modules.json break names
mp = ROOT / 'src/content/modules.json'
mods = json.loads(mp.read_text(encoding='utf-8'))
for m in mods:
    m['name'] = {'B1': 'Short break', 'B2': 'Lunch break', 'B3': 'Tea break'}.get(m['id'], m['name'])
mp.write_text(json.dumps(mods, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('Migrated to 76 slides. Old->new:', ', '.join(f'{o}->{n}' for o, n in OLD_TO_NEW.items()))
```

- [ ] **Step 3: Run the migration and the test**

```bash
python3 build/tools/migrate_v2.py | tail -c 300
python3 -m unittest discover -s build/tests -v 2>&1 | tail -5
```

Expected: "Migrated to 76 slides" line; `test_migration` PASS except `test_no_prayer_in_plan` if any old facilitator text still contains "prayer". If it fails, grep with `grep -n -i prayer 04-content/slides.json` and edit those strings in slides.json to neutral wording (for example "Lunch break. Restart on time."), then re-run until all tests pass.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -qm "feat(content): migrate plan to 76 slides with explanation fields and new IDs"
```

---

### Task 5: Build integration

**Files:**
- Modify: `build/build.py`
- Modify: `src/content/notes.json` (remove prayer wording, add notes for new slides)
- Modify: `src/content/choices.json` (delete groups no longer rendered)

**Interfaces:**
- Consumes: `checks.*`, `avatars.avatar_html`, `generated.render_generated`.
- Produces: rendered head `<p class="what">…</p>` under every non-exempt fragment heading; `<div class="keypoint">` before the source line on non-generated, non-exempt slides; section classes `pause pause-vote` or `pause pause-reveal` on pause slides; new token `{{avatar:key}}` / `{{avatar:key|cls|alt}}`.

- [ ] **Step 1: Edit `build/build.py`**

Make these exact changes:

1. Imports, after `from pathlib import Path`:

```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import checks
from avatars import avatar_html
from generated import render_generated, keypoint as keypoint_html
```

2. Delete the `'prayer_note'` entry from `PLACEHOLDERS` and the two `if path == 'prayer_note':` lines in `config_value`.

3. In `render_tokens`, add before the final `err(...)`:

```python
        if kind == 'avatar':
            parts = arg.split('|')
            return avatar_html(parts[0], parts[1] if len(parts) > 1 and parts[1] else 'avatar', parts[2] if len(parts) > 2 else '')
```

4. Replace the body of `render_slide(s, frag)` with:

```python
def render_slide(s, frag, habits):
    sid = s['id']
    exempt = sid in checks.EXEMPT_IDS
    if s['layout'] in checks.GENERATED_LAYOUTS:
        a, body, head = {}, render_generated(s, MODULES, habits), ''
    else:
        a = frag['attrs']
        body = render_tokens(frag['body'], s)
        head = ''
        if a.get('data-head') != 'none':
            right = ''
            if 'data-reveal' in a:
                on, _, off = a['data-reveal'].partition('|')
                right = (f'<button type="button" class="primary" data-act="reveal" aria-expanded="false" '
                         f'data-off="{esc(on)}" data-on="{esc(off or "Hide")}">{esc(on)}</button>')
            else:
                pill = a.get('data-pill', DEFAULT_PILL.get(s['evidence_kind'], ''))
                if pill:
                    right = f'<span class="pill">{esc(pill)}</span>'
            what = '' if exempt else f'<p class="what">{esc(s["what_this_shows"])}</p>'
            head = (f'<div class="head"><div><p class="kicker">{esc(a.get("data-kicker", ""))}</p>'
                    f'<h2 id="{sid}-title">{esc(s["title"])}</h2>{what}</div>{right}</div>')
        if not exempt:
            body += keypoint_html(s['key_point'])
    cls = ['slide']
    if s['pause_point']:
        cls += ['pause', 'pause-' + checks.pause_kind(body)]
    return (f'<section class="{" ".join(cls)}" id="{sid}" data-module="{s["module"]}" data-layout="{s["layout"]}" '
            f'aria-labelledby="{sid}-title" aria-roledescription="slide">'
            f'{head}{body}{source_line(s, a)}</section>')
```

5. In `build_deck()`:
   - Replace the missing-fragment loop with:

```python
    generated_ids = {s['id'] for s in SLIDES if s['layout'] in checks.GENERATED_LAYOUTS}
    for sid in plan_ids:
        if sid not in frags and sid not in generated_ids:
            err(f'missing fragment for {sid}')
    for sid in frags:
        if sid not in plan_ids or sid in generated_ids:
            err(f'fragment {sid} not expected (unknown ID or generated layout)')
```

   - Before rendering sections, add the plan-field checks and the habits list:

```python
    for s in SLIDES:
        for m in checks.check_plan_fields(s):
            err(m)
    habits = [(s.get('module_label', ''), s['habit']) for s in SLIDES if s['layout'] == 'takeaway']
    habits.append(('Module 7', 'Pause, verify, report, recover.'))
```

   - In the section loop, change `h = render_slide(s, frags[s['id']])` to `h = render_slide(s, frags.get(s['id']), habits)` and after `check_html(...)` add:

```python
        if not s['pause_point']:
            for m in checks.check_open_slide(s['id'], h):
                err(m)
        for m in checks.check_participant_text(s['id'], h, s['layout']):
            err(m)
```

   - After `out` is assembled (before the forbidden-API loop), add `for m in checks.check_whole_output(out): err(m)`.
   - In the `data` dict for each slide add `'whatThisShows': s.get('what_this_shows', ''), 'keyPoint': s.get('key_point', '')`.

6. `check_html`: the generated headings are `<h1 id="SLxx-title">` and contain the title, so it still passes. No change.

- [ ] **Step 2: Content data edits**

In `src/content/notes.json`:
- Set `"SL40"` to `{"answer": "", "extra": ["75-minute lunch break. Restart on time; nothing advances automatically."]}`.
- Set `"SL59"` to `{"answer": "", "extra": ["25-minute tea break. Set up table roles for the tabletop on return."]}`.
- Set `"SL18"` to `{"answer": "", "extra": ["10-minute break. Restart on time."]}`.
- Add entries for each new slide ID (SL02, SL08, SL17, SL19, SL27, SL28, SL39, SL41, SL50, SL51, SL58, SL60, SL67, SL68, SL75) with `{"answer": "", "extra": ["<one line>"]}`, using these lines:
  - SL02 "Set expectations: everything is fictional, no wrong questions, nobody shares personal incidents, reporting is never blamed."
  - Openers (SL08, SL19, SL28, SL41, SL51, SL60, SL68): "Read the ‘why this matters’ line, then ask: has anyone seen something like this at work? Keep it to one or two answers."
  - Takeaways (SL17, SL27, SL39, SL50, SL58, SL67): "Ask one person to put the habit in their own words for their job."
  - SL41 extra second line: "The glossary covers every technical term used in this module; point back to it whenever a term comes up."
  - SL75: "Read the seven habits; ask which one each person will use first."
- Search the file for the old phrase "Confirm prayer" and remove any remaining prayer wording: `grep -n -i prayer src/content/notes.json` must return nothing.

In `src/content/choices.json`, delete the keys for groups whose slides become open (they will no longer be rendered): `SL15-a`, `SL15-b`, `SL15-c` (old SL13 sort), `SL36-1`…`SL36-4` (exercise buttons removed), `SL44-pick`, `SL46-pick`, `SL56-pick` (old SL36/38/46). Keep `SL11-pick` and all decision-slide entries.

- [ ] **Step 3: Run the build to see the expected failures**

Run: `python3 build/build.py 2>&1 | head -40`
Expected: BUILD FAILED listing `open slide has interactive control …`, `hides content`, `uses reveal-only classes` and `clock time` errors for fragments not yet converted. Generated slides and avatars produce no errors. This failure list is the to-do list for Tasks 7–14.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -qm "feat(build): render what-line, key point, generated slides, pause rules"
```

---

### Task 6: Runtime and CSS for the clarity layer

**Files:**
- Modify: `src/js/deck.js`
- Modify: `src/css/deck.css` (append)
- Modify: `src/shell.html` (help text credit line)

- [ ] **Step 1: Edit `src/js/deck.js`**

1. Module bar: replace the two lines that set `aria-label` and `title` with:

```js
    const label = m.kind === 'break' ? m.name : `${m.id === 'M0' ? 'Opening' : 'Module ' + m.id.slice(1)}: ${m.name}`;
    b.setAttribute('aria-label', label);
    b.title = label;
```

2. In `openIndex()`, replace the `h4` text with
   ``sec.append(el('h4', null, m.kind === 'break' ? m.name : `${m.id === 'M0' ? 'Opening' : 'Module ' + m.id.slice(1)} · ${m.name}`));``
3. In `actions`: delete `toggle`, `step` and `'step-reset'`. In `choose`, add `slide.classList.add('chosen');` as the first line after `if (!opt) return;`.
4. Delete the `stepTo` function, the `initSlide` function, the `slides.forEach(initSlide);` line, and `initSlide(fresh);` inside `resetSlide`.
5. Notes dialog: after `add('Objective', m.objective);` insert `add('What this slide shows', m.whatThisShows); add('Key point', m.keyPoint);`.

- [ ] **Step 2: Append CSS to `src/css/deck.css`**

```css
/* ===== clarity rework (spec 2026-10-02) ===== */
.what{font-size:19px;line-height:1.4;color:var(--text-secondary);margin-top:8px;max-width:1050px}
.keypoint{margin-top:16px;display:flex;gap:16px;align-items:baseline;background:#13342f;border-left:3px solid var(--accent);padding:12px 18px;font-size:19px;line-height:1.45;border-radius:0 9px 9px 0}
.keypoint b{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);white-space:nowrap}
.slide.pause-vote:not(.chosen) .keypoint,.slide.pause-reveal:not(.revealed) .keypoint{display:none}
mark.hl{background:#fff0bb;color:inherit;padding:0 2px;border-radius:3px}
.marker{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:var(--warning);color:#1b1300;font-size:13px;font-weight:700;margin-left:4px;vertical-align:2px;line-height:1}
.markers{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.markers li{display:grid;grid-template-columns:30px 1fr;gap:10px;font-size:18px;line-height:1.4;color:var(--text-secondary)}
.markers li .marker{margin:2px 0 0}
.markers li strong{color:var(--text-primary)}
img.photo{object-fit:cover;padding:0;background:#dfe8f1}
.pavatar.photo{display:block}
.answerbox{border:1px solid var(--accent);border-radius:12px;padding:14px 18px;font-size:18px;line-height:1.45}
.answerbox b{display:block;font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--accent);margin-bottom:4px}
.gen{display:grid;grid-template-columns:1.1fr 1fr;gap:4vw;align-items:start;flex:1}
.gen h1{font-size:clamp(40px,4vw,60px);letter-spacing:-2px}
.gen .sub{margin-top:10px}
.gen .eyebrow{margin:22px 0 10px}
.gen .why{font-size:22px;line-height:1.45}
.gen .outcomes,.gen .rules,.gen .tlist{margin:0;padding-left:22px;font-size:21px;line-height:1.5}
.gen .outcomes li+li,.gen .rules li+li,.gen .tlist li+li{margin-top:8px}
.gen .tlist{font-size:23px}
.daylist{margin:0;padding-left:22px;font-size:18px;line-height:1.55;color:var(--text-primary)}
.daylist li.brk{color:var(--text-secondary);list-style:none;margin-left:-22px;padding-left:22px;font-style:italic}
.glossary{display:grid;grid-template-columns:auto 1fr;gap:6px 14px;margin:0;font-size:16px;line-height:1.4}
.glossary dt{font-weight:700}
.glossary dd{margin:0;color:var(--text-secondary)}
.habit{margin-top:22px;border:1px solid var(--accent);border-radius:12px;padding:16px 18px}
.habit .eyebrow{margin:0 0 6px;color:var(--accent)}
.habittext{font-size:25px;line-height:1.35;font-weight:700}
.habits{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.habits li{display:grid;grid-template-columns:110px 1fr;gap:12px;font-size:19px;line-height:1.4;border-top:1px solid var(--line);padding-top:9px}
.hmod{color:var(--accent);font-size:13px;letter-spacing:1.4px;text-transform:uppercase;padding-top:3px}
.coverfoot .credit{font-size:13px;color:var(--text-secondary)}
@media(min-width:901px) and (max-height:800px){
  .what{font-size:17px;margin-top:6px}
  .keypoint{margin-top:12px;padding:10px 16px;font-size:17px}
  .gen .why,.gen .outcomes,.gen .rules{font-size:19px}
  .gen .tlist{font-size:21px}
  .gen .eyebrow{margin:14px 0 8px}
  .habits li{font-size:17px;padding-top:7px}
  .habittext{font-size:22px}
}
@media(max-width:900px){.gen{grid-template-columns:1fr}.habits li{grid-template-columns:1fr}.keypoint{flex-direction:column;gap:4px}}
```

- [ ] **Step 3: Help text credit**

In `src/shell.html`, inside the `#help` dialog body, after the paragraph ending "Documented incidents are labelled and cited.", add:

```html
<p>Portraits are AI-generated; no real person is depicted.</p>
```

- [ ] **Step 4: Check the JS parses and commit**

Run: `node -e "new Function(require('fs').readFileSync('src/js/deck.js','utf8'))" && echo JS-OK`
Expected: `JS-OK`.

```bash
git add -A && git commit -qm "feat(runtime): remove steppers/toggles, chosen key point, no times in labels; clarity CSS"
```

---

### Conversion rules used by Tasks 7–14

Apply to every slide that is **not** a pause point. Each module task lists the slides and any slide-specific content.

- **R1 Steppers:** remove `data-stepper`, `data-step`, `data-count-label` attributes; delete every `<div class="chatcontrols">…</div>`, every `.stepctl` block, every element with `data-step-count`, and every button with `data-act="step"` or `data-act="step-reset"`.
- **R2 Toggles:** delete every `<button … data-act="toggle" …>…</button>`; remove the `hidden` attribute from the element it controlled; change `class="details at-sender"` / `class="details at-link"` to `class="details static"`.
- **R3 Reveals:** on the `<section>`, delete `data-reveal="…"` and add `data-pill="Training scenario"` (or the slide-specific pill given below); delete every element with class `if-unrevealed` unless the task says to keep it; remove the class token `if-revealed` from remaining elements (keep their content).
- **R4 Marks → markers:** replace `<span class="mark">TEXT</span>` with `<mark class="hl">TEXT</mark><span class="marker" aria-hidden="true">N</span>` (N = 1, 2, 3 in reading order), and put an `<ol class="markers">` in the side column with one `<li><span class="marker" aria-hidden="true">N</span><span><strong>Short label.</strong> Note.</span></li>` per marker, using the notes given in the task.
- **R5 No duplication:** delete any `.callout` whose text repeats the slide’s Key point (the Key point box is now added automatically).
- **R6 Photos:** replace `<span class="avatar">X</span>` with the `{{avatar:key}}` token named in the task; replace `<div class="pavatar" aria-hidden="true">A</div>` with `{{avatar:aina|pavatar}}`.

After each module task: `python3 build/build.py` must list **no errors for that module’s slide IDs**. Then run `node build/qa/render.cjs --slides <that module’s IDs> --vp 1440x900,1366x768`. It must report 0 failures, and you must open at least the 1366×768 screenshots of every slide in the module and look at them. If a slide overflows, first remove repetition (R5); then shorten copy; if it still does not fit, split it (add a slide to slides.json, renumber nothing else, set its minutes from the neighbour so module totals stay unchanged, and record the split in `validation/QA_REPORT.md`). Commit with `git add -A && git commit -qm "content(<module>): open style, markers, photos"`.

---

### Task 7: M0 opening (SL01–SL07)

**Files:** Modify `src/slides/M0.html`.

- [ ] **Step 1: SL01 cover.** Replace the four `<span class="avatar">A|F|M|R</span>` with `{{avatar:aina}}`, `{{avatar:farid}}`, `{{avatar:mei}}`, `{{avatar:ravi}}`. Replace the `coverfoot` contents with:

```html
<div class="coverfoot"><p class="prompt">Training scenario. All people, organisations and messages in this story are fictional.</p><p class="credit">Portraits are AI-generated; no real person is depicted.</p><p class="sessionline">{{config:session_date}} · {{config:venue}}</p></div>
```

- [ ] **Step 2: SL03 email (old SL02).** R2 on both toggles (sender details and link details become `details static`; keep their text). R6: `N` → `{{avatar:nadia}}`. In `.mailcopy`, wrap with R4 markers: "Our bank details have changed." (1), "Please complete this before 5 PM." (2). Add marker 3 after the static link details text "Displayed destination: …". Replace the aside with:

```html
<aside class="side"><p class="eyebrow">What the email shows</p><ol class="markers">
<li><span class="marker" aria-hidden="true">1</span><span><strong>The risky action.</strong> New bank details for a real, expected payment.</span></li>
<li><span class="marker" aria-hidden="true">2</span><span><strong>Time pressure.</strong> A same-day deadline leaves no time to check.</span></li>
<li><span class="marker" aria-hidden="true">3</span><span><strong>Looks right.</strong> Sender and link use the supplier’s real domain, which cannot show who is typing.</span></li>
</ol><p class="hint">Ask the room: what can this email actually prove?</p></aside>
```

- [ ] **Step 3: SL04 chat (old SL03).** R1 (all three bubbles visible; delete the Replay button). R6 `R` → `{{avatar:ravi}}`. Keep the aside quote and hint.
- [ ] **Step 4: SL05 (pause, vote).** No change except R6 does not apply (no avatars).
- [ ] **Step 5: SL06 (pause, reveal).** R6 `N` → `{{avatar:nadia}}`. Delete the callout "Independent verification gives Farid evidence…" (R5; the Key point appears on reveal).
- [ ] **Step 6: SL07 HK case.** No interaction. Keep the callout question (it is a prompt, not the key point).
- [ ] **Step 7: Build, render, inspect, commit** per the conversion rules (IDs SL01–SL07).

---

### Task 8: M1 (SL09–SL16; SL08 and SL17 are generated)

**Files:** Modify `src/slides/M1.html`.

- [ ] **SL09 terms (old SL07):** R3 (`data-pill="Course definitions"`); make the three step labels visible (remove `if-revealed`); delete the `if-unrevealed` span and keep the second span’s text as a plain `<p class="lede">`.
- [ ] **SL10 profile (old SL08):** R3; R6 `{{avatar:aina|pavatar}}`; R4 with markers 1–5 on: job title, Riverside office move, Farid and Ravi, Maju Supplies, forum on Thursday. Side `<ol class="markers">` notes: 1 “Job title: lets a message mention her real work.” 2 “Project: makes ‘about the Riverside move…’ sound expected.” 3 “Colleague names: a sender can name-drop to seem connected.” 4 “Supplier name: invoices or requests can borrow it.” 5 “Event date: tells a stranger when she is away from her desk.” Delete the `if-unrevealed` question and the callout (R5). Keep the eyebrow “Discuss in pairs”.
- [ ] **SL11 (pause vote):** replace both `<div class="pavatar" …>A</div>` with `{{avatar:aina|pavatar}}` (the same photo on both, deliberately). Add under the two profiles, in the left column after the inner grid, `<p class="hint">Both profiles use the same AI-generated photo. Fake accounts often use real people’s photos or AI-generated faces.</p>`.
- [ ] **SL12 Siti chat (old SL10):** R1, R3, R6 `S` → `{{avatar:siti}}`. Keep findings 01/02 visible; delete the callout (R5); add as last aside element `<p class="hint">Cloning copies a profile. Compromise means someone else controls the real account. Both can send this message.</p>`.
- [ ] **SL13 fake support (old SL11):** R2 (account details shown static), R3 (pill `Training scenario · fictional brand`), R5 delete the callout.
- [ ] **SL14 collaboration (old SL12):** R1, R3, R6 `D` → `{{avatar:daniel}}`, R4: the two existing marks become markers 1 and 2; aside `ol.markers`: 1 “Asks for a work sign-in.” 2 “Asks for internal documents.” Keep eyebrow “In pairs · 3 minutes” and the big question; delete the hint and callout.
- [ ] **SL15 clone vs takeover (old SL13):** R3; replace the whole sorting `.stack` (eyebrow, `.sorttable`, feedback and the callout) with:

```html
<div class="stack">
<p class="eyebrow">Which action fits which situation?</p>
<table class="ticks"><thead><tr><th>Action</th><th>Copied profile</th><th>Taken-over account</th></tr></thead><tbody>
<tr><td>Preserve link, handle, screenshots and times</td><td>✓</td><td>✓</td></tr>
<tr><td>Report the copy to the platform</td><td>✓</td><td>—</td></tr>
<tr><td>Use official account recovery; review sessions and apps</td><td>—</td><td>✓</td></tr>
<tr><td>Warn contacts through a trusted channel</td><td>✓</td><td>✓</td></tr>
</tbody></table>
<p class="hint">Password changes alone do not remove a copied profile.</p>
</div>
```

and append to `src/css/deck.css`:

```css
.ticks{border-collapse:collapse;width:100%;font-size:18px;line-height:1.4}
.ticks th{font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:var(--text-secondary);text-align:left;padding:0 10px 8px;font-weight:400}
.ticks td{border-top:1px solid var(--line);padding:10px}
.ticks td+td,.ticks th+th{text-align:center;width:150px;font-size:22px;color:var(--accent)}
```

- [ ] **SL16 (pause vote):** no change.
- [ ] **SL18 break (old SL15):** replace the whole section body with:

```html
<div class="intermission"><div><p class="kicker">Break</p><h1 id="SL18-title">Short break</h1><p class="sub">We return with Module 2 · The trusted request.</p></div>
<div class="scene"><p class="eyebrow">Next</p><p class="return"><strong>Module 2 · The trusted request</strong></p><p class="small">Urgent requests, authority and calls you did not expect. No slide advances automatically.</p></div></div>
```

- [ ] Build, render (SL08–SL18), inspect, commit.

---

### Task 9: M2 (SL20–SL26; SL19 and SL27 are generated)

**Files:** Modify `src/slides/M2.html`.

- [ ] **SL20 urgent manager (old SL16):** R1, R3, R6 `R` → `{{avatar:ravi}}`; R5 delete the callout; keep eyebrow and big question; replace the hint with `<p class="hint">The deadline is real pressure, but it does not change who can approve a payment.</p>`.
- [ ] **SL21 pressure tactics (old SL17):** R3, R6 `{{avatar:ravi}}`, R4: the three marks become markers 1–3; delete `if-unrevealed`; turn the findings into the markers list (1 Urgency, 2 Secrecy, 3 Exception, keeping the existing explanation text); R5 delete the callout.
- [ ] **SL22 roleplay (old SL18):** R3; show the strong-response callout as `<div class="answerbox"><b>A strong response</b>“I’ll call you back on your directory number, then raise it for approval. It should take ten minutes.”</div>`.
- [ ] **SL23 phone call (old SL19):** R1, R3; change the head avatar `?` to `{{avatar:it-caller}}` and its small text to `Read aloud by the trainer · photo is an illustration`; delete the callout (R5); keep the big question; replace the hint with `<p class="hint">Nothing said in a call can prove who is calling.</p>`.
- [ ] **SL24 face or voice (old SL20):** R3 (pill `Course guidance`); make both reveal notes visible; delete the two `if-unrevealed` “Would this protect Farid?” lines.
- [ ] **SL25, SL26 (pause votes):** no change.
- [ ] Build, render (SL19–SL27), inspect, commit.

---

### Task 10: M3 (SL29–SL38; SL28 and SL39 are generated) and lunch SL40

**Files:** Modify `src/slides/M3.html`.

- [ ] **SL29 inbox (old SL23):** R2 for the three “Requested action?” buttons (the `askfor` lines become visible).
- [ ] **SL30 sender (old SL24):** R2 (sender details static), R3, R6 `R` → `{{avatar:ravi}}`; findings visible; delete the `if-unrevealed` hint.
- [ ] **SL31 (pause reveal):** no change.
- [ ] **SL32 polished messages (old SL26):** R3 (both reveal notes visible); R5 delete the bottom callout.
- [ ] **SL33 phone view (old SL27):** R2 (desktop comparison card visible), R3, R5 delete the callout.
- [ ] **SL34 QR (old SL28):** R3 (destination details visible); delete the `if-unrevealed` hint; R5 delete the callout; replace with `<p class="hint">Device-linking QR codes come later in the day. They grant account access instead of opening a page.</p>`.
- [ ] **SL35 shared files (old SL29):** R2 for the three file cards, R3, R5 delete the callout.
- [ ] **SL36 four-card exercise (pause reveal):** delete the four `{{choices:SL36-N|mini|SL36-fb}}` tokens and the `{{feedback:SL36-fb…}}` token. In each card, replace the existing `reveal-note` paragraph with a revealed answer:
  - Card 1: `<p class="reveal-note if-revealed"><span class="flag ok">Verify first</span> Genuine change, not yet approved: call the established contact, then complete approval.</p>`
  - Card 2: `<p class="reveal-note if-revealed"><span class="flag">Verify first</span> Genuine account, someone else using it: check with Siti through the directory and report.</p>`
  - Card 3: `<p class="reveal-note if-revealed"><span class="flag ok">Proceed</span> Genuine notice found through a known route; it asks for nothing sensitive.</p>`
  - Card 4: `<p class="reveal-note if-revealed"><span class="flag">Hold and report</span> Not Ravi: an impersonated urgent exception. Verify through the directory.</p>`
  
  Change the intro lede to `<p class="lede ex-intro"><strong>Proceed, verify first, or hold and report?</strong> Tables vote with a show of hands for each card, then reveal.</p>`.
- [ ] **SL37 signals (old SL31):** delete the four-column header’s last empty `<span></span>` and every `Reveal` button; remove `hidden` from all cells; change `.sigrow` grid in CSS by appending `.sigrow{grid-template-columns:1.05fr 1.5fr 1.5fr}`; R5 delete the bottom callout.
- [ ] **SL38 route (old SL32):** no interaction; keep.
- [ ] **SL40 lunch (old SL33):** replace the section body with:

```html
<div class="intermission"><div><p class="kicker">Break</p><h1 id="SL40-title">Lunch break</h1><p class="sub">We return with Module 4 · Beyond the password.</p></div>
<div class="scene"><p class="eyebrow">Next</p><p class="return"><strong>Module 4 · Beyond the password</strong></p><p class="small">Sign-ins, codes, app permissions and linked devices. No slide advances automatically.</p></div></div>
```

- [ ] Build, render (SL28–SL40), inspect, commit.

---

### Task 11: M4 (SL42–SL49; SL41 and SL50 are generated)

**Files:** Modify `src/slides/M4.html`.

- [ ] **SL42 access types (old SL34):** R2 (four “What does it grant?” answers visible), R3, R5 delete the bottom callout.
- [ ] **SL43 relayed sign-in (old SL35):** R3; step 3 shows “Signed in as Aina” content (delete the `h3.if-unrevealed`); the MFA lede becomes visible.
- [ ] **SL44 MFA prompts (old SL36):** replace `{{choices:SL44-pick|stacked}}` and its feedback token with `<div class="answerbox"><b>What Aina should do</b>Deny each prompt and report it to IT. Approving one, even to stop the prompts, lets the other person in.</div>`.
- [ ] **SL45 device code (old SL37):** R3; findings visible; R5 delete the callout.
- [ ] **SL46 consent (old SL38):** R2 (permission notes static); replace the choices and feedback tokens with `<div class="answerbox"><b>What Aina should do</b>Request the app through the approved IT process. Accepting would give access immediately, and data could be read before anyone removes it.</div>`.
- [ ] **SL47 linking (old SL39):** R3; the two comparison cards are visible; delete the `if-unrevealed` lede; R5 delete the callout.
- [ ] **SL48 Cloudflare:** no change.
- [ ] **SL49 (pause vote):** no change.
- [ ] Build, render (SL41–SL50), inspect, commit.

---

### Task 12: M5 (SL52–SL57; SL51 and SL58 are generated) and tea SL59

**Files:** Modify `src/slides/M5.html`.

- [ ] **SL52 fake Mei (old SL42):** R1, R2 (account details static, placed after the chat head), R3, R6 `M` → `{{avatar:mei}}`; delete the `if-unrevealed` hint and the callout (R5).
- [ ] **SL53 (pause vote):** no change.
- [ ] **SL54 fake CAPTCHA (old SL44):** R1: both browser steps visible; delete the `.stepctl` and the Start again button; keep the STOP box; R5 delete the callout.
- [ ] **SL55 CrashFix (old SL45):** R1: all four stages visible; delete `.stepctl` and Start again.
- [ ] **SL56 renewal (old SL46):** R2 (sender details static), R6 `S` stays as an initial (SecureSuite is not a cast member: replace with `<span class="avatar">S</span>` unchanged); replace the choices and feedback tokens with `<div class="answerbox"><b>The safer route</b>Check the account through IT or finance records. The number in the notice belongs to whoever sent it.</div>`.
- [ ] **SL57 (pause vote):** R6 on any avatar if present; no other change.
- [ ] **SL59 tea break (old SL48):** replace the body with:

```html
<div class="intermission"><div><p class="kicker">Break</p><h1 id="SL59-title">Tea break</h1><p class="sub">We return with Module 6 · Stop the chain.</p></div>
<div class="scene"><p class="eyebrow">Next</p><p class="return"><strong>Module 6 · Stop the chain</strong></p><p class="small">Your table becomes the Meranti team. No slide advances automatically.</p></div></div>
```

- [ ] Build, render (SL51–SL59), inspect, commit.

---

### Task 13: M6 (SL61–SL66; SL60 and SL67 are generated)

**Files:** Modify `src/slides/M6.html`.

- [ ] **SL61 roles (old SL49):** R6 `A/F/R/M` → `{{avatar:aina}}`, `{{avatar:farid}}`, `{{avatar:ravi}}`, `{{avatar:mei}}`. Replace the “How it runs · 35 minutes” panel heading with `How it runs` and its text with `Roles first, then four evidence cards one at a time, then a short debrief.` followed by the existing bold sentence and “Write hypotheses separately.” (no minute values on screen).
- [ ] **SL62–SL65 (pause reveals):** delete each card’s callout text that duplicates the Key point (R5). The Key point now shows on reveal. Keep the three record questions.
- [ ] **SL66 debrief (old SL54):** R3 (pill `Debrief`); delete the `if-unrevealed` question; make card texts, the facts panels and the callout visible; R5 delete the callout “A useful report can come before a complete diagnosis.” (the Key point covers it).
- [ ] Build, render (SL60–SL67), inspect, commit.

---

### Task 14: M7 (SL69–SL74, SL76; SL68 and SL75 are generated)

**Files:** Modify `src/slides/M7.html`.

- [ ] **SL69 mnemonic (old SL55):** R2 (four examples visible).
- [ ] **SL70 reporting route (old SL56):** R1 (all four steps visible; delete the `.stepctl`).
- [ ] **SL71 after a mistake (old SL57):** R3 (owners visible); R5 delete the bottom callout.
- [ ] **SL72 useful report (old SL58):** R3 (missing-facts note visible).
- [ ] **SL73 (pause vote):** R6 not applicable; no change. Optionally add `{{avatar:lina}}` before “HR’s Lina” inside the decision context: `<span class="ctxperson">{{avatar:lina}}</span>`, and append CSS `.ctxperson .avatar{width:44px;height:44px;margin-right:12px;vertical-align:middle}`.
- [ ] **SL74 reflection, SL76 references:** no change.
- [ ] Build, render (SL68–SL76), inspect, commit.

---

### Task 15: Whole-deck build, docs and validators

**Files:**
- Modify: `build/make_docs.py`, `dist/README.md`, `10-validation/validate_package.py`, `build/qa/interact.cjs`

- [ ] **Step 1: Full build must pass**

Run: `python3 build/build.py && python3 -m unittest discover -s build/tests`
Expected: `OK: …workshop.html (… 76 slides, 420 minutes)` and all unit tests pass. If the build fails, fix the named slide using the conversion rules, then re-run.

- [ ] **Step 2: `build/make_docs.py` edits**

- Status paragraph: replace “Customer reporting details, date, venue and prayer arrangements are unconfirmed” with “Customer reporting details, date and venue are unconfirmed”.
- “Before the day” list: replace the item beginning “Confirm lunch and prayer times…” with `'Confirm break arrangements for the date and venue. If a longer break is needed, revise the whole timetable; do not shorten the reporting segment.'`
- Delete the customer-inputs line beginning `f'Prayer arrangements for the date and venue`.
- After the timetable, add a “Module goals and habits” section:

```python
    a('## Module goals and habits')
    a('')
    for s in SLIDES:
        if s['layout'] == 'opener':
            a(f'- **{s["title"]}**: {s["why"]} You will be able to: ' + '; '.join(s['outcomes']) + '.')
        if s['layout'] == 'takeaway':
            a(f'    - Habit: {s["habit"]}')
    a('')
```

- In the runbook loop, after `- **Objective:**`, add `a(f'- **Say:** {s["what_this_shows"]}')` and `a(f'- **Key point (on screen):** {s["key_point"]}')` when present, and change the label “Expected answer / reveal” to “Ask, then confirm”. Add `if s['pause_point']: a('- **Pause point:** let the room vote or discuss before clicking.')`.
- Participant card: after the “If you already acted” list, add a “Seven habits” `<h2>` and an `<ol>` built from the takeaway habits plus “Pause, verify, report, recover.”, and a “Words to know” `<dl>` from SL41’s `glossary`. Re-check that the card still prints on one A4 page (Task 16).

- [ ] **Step 3: `10-validation/validate_package.py`**

Change `61` to `76` in the two `len(...)==` assertions.

- [ ] **Step 4: `dist/README.md`**

Replace “It has 61 screens: 58 learning and activity screens and 3 breaks.” with “It has 76 screens: 73 learning, activity, opener and takeaway screens, and 3 breaks.” Replace “all 61 slides” with “all 76 slides”. In “Before live delivery”, delete the “Prayer times…” bullet and replace the SL56/SL32/cover references with SL70/SL38/SL01. Add under “Opening and presenting”: “16 slides are pause points (marked in the facilitator guide): the room votes or discusses first, then you click once. Every other slide shows everything from the start.”

- [ ] **Step 5: `build/qa/interact.cjs` ID updates**

Apply these replacements (old → new) in the file: `SL61`→`SL76` (counter `01 / 61`→`01 / 76`, `61 slides` checks → `76`), `#SL33`→`#SL40`, `#slide-7`→`#slide-9` expecting `SL09`, `#SL99` unchanged, module bar M4 start `SL34`→`SL41`, B2 `SL33`→`SL40`, index button text `Evidence 2`→ expects `SL63`, notes check `SL51`→`SL63` with time `16:14`→ the new SL63 `planned_start` from slides.json and text `Do not request the actual code`, SL02 sender toggle test → **delete** (no toggles remain), SL03 stepper test → replace with a check that all three `.bubble` in `#SL04` are visible, SL04 decision → `SL05`, SL14 → `SL16`, SL05 reveal → `SL06`, SL30 exercise test → replace with: click `#SL36 [data-act="reveal"]` and check four `.reveal-note` are visible, SL31 row toggle test → **delete**, swipe test `#SL06`→`#SL07` expecting `SL08` and the control `#SL09 …` → use `#SL11 [data-act="choose"]`. Add these checks:

```js
  // open slides hide nothing; pause slides hide key point until acted on
  const audit = await page.evaluate(() => {
    const D = JSON.parse(document.getElementById('deck-data').textContent);
    const pause = new Set(D.slides.filter((s, i) => document.querySelectorAll('.slide')[i].classList.contains('pause')).map(s => s.id));
    const bad = [...document.querySelectorAll('.slide:not(.pause)')].filter(s => s.querySelector('[hidden],[data-act="toggle"],[data-act="step"]')).map(s => s.id);
    return { pauseCount: pause.size, bad };
  });
  check('exactly 16 pause-point slides', audit.pauseCount === 16, String(audit.pauseCount));
  check('open slides contain no hidden content or toggles', audit.bad.length === 0, audit.bad.join(','));
  await page.goto(DECK + '#SL05');
  check('vote key point hidden before choosing', !(await page.isVisible('#SL05 .keypoint')));
  await page.click('#SL05 [data-idx="2"]');
  check('vote key point shown after choosing', await page.isVisible('#SL05 .keypoint'));
  await page.goto(DECK + '#SL03');
  check('open slide key point visible immediately', await page.isVisible('#SL03 .keypoint'));
  check('photos embedded as data URIs', (await page.$$eval('img.photo', x => x.every(i => i.src.startsWith('data:image/jpeg')))));
  check('no "prayer" in the page', !(await page.evaluate(() => /prayer/i.test(document.documentElement.outerHTML))));
```

- [ ] **Step 6: Run validators and commit**

```bash
python3 build/build.py && python3 10-validation/validate_package.py
git add -A && git commit -qm "docs+qa: 76-slide docs, habits, glossary, updated validators"
```

Expected: build OK; validator prints PASS **except** the manifest hash check (fixed in Task 16).

---

### Task 16: Full visual QA, reports and handover

**Files:**
- Modify: `validation/QA_REPORT.md`, `10-validation/PROGRESS_LEDGER.md`, `10-validation/COVERAGE_MATRIX.md`, `MANIFEST.json`

- [ ] **Step 1: Full render at all viewports**

```bash
rm -rf validation/screenshots/1440x900 validation/screenshots/1366x768 validation/screenshots/390x844
node build/qa/render.cjs --vp 1440x900,1366x768,390x844
```

Expected: `failures: 0; external requests: 0`. For any failure, fix the slide (R5, then shorter copy, then split as described in the conversion rules) and re-run only that slide.

- [ ] **Step 2: Look at every slide**

Build 2×2 contact sheets of the 1366×768 renders (default state for open slides, expanded for pause slides) and open each one:

```bash
python3 - <<'EOF'
from PIL import Image; import os
d='validation/screenshots/1366x768'; out='/tmp/claude-1000/-home-universal-Claude-Cybersecurity-training-awareness/60fb327e-0383-4328-ac04-07935ddab15e/scratchpad/sheets76'; os.makedirs(out,exist_ok=True)
def pick(i):
    for st in ('expanded','default'):
        p=f'{d}/SL{i:02d}-1366x768-{st}.png'
        if os.path.exists(p): return p
fs=[pick(i) for i in range(1,77)]
for k in range(0,76,4):
    s=Image.new('RGB',(1366,768),'white')
    for j,f in enumerate(fs[k:k+4]): s.paste(Image.open(f).resize((683,384)),((j%2)*683,(j//2)*384))
    s.save(f'{out}/sheet_{k//4:02d}.png')
EOF
```

Check each sheet for: Key point present, what-line present, photos not distorted, no overlapping text, markers aligned with their notes. Fix and re-render any problem slide.

- [ ] **Step 3: Interaction, contrast and card checks**

```bash
node build/qa/interact.cjs | tail -8
```

Expected: all checks PASS, including contrast (text over photos is not text-on-image; photos have no overlaid text). Also re-render the participant card to PDF using the snippet from the original QA (Chromium `page.pdf({format:'A4'})`) and confirm it is still 1 page; if it is 2 pages, shorten the glossary to the four most important terms (MFA, session, device code, app permission).

- [ ] **Step 4: Update reports**

- `validation/QA_REPORT.md`: add a section “Clarity rework (v2)” stating the count change 61→76 and its reason (14 module openers/takeaways + agenda), the old→new ID mapping printed by the migration (paste it), the 16 pause points, the timing table (per module, unchanged totals), any slides split, render/interaction results with counts from `validation/qa-results.json` and `validation/interaction-results.json`, the removal of prayer wording and on-screen clock times, the photo credit, and anything not tested.
- `10-validation/PROGRESS_LEDGER.md`: add a v2 row group (implemented/tested), and the next action (customer inputs, rehearsal).
- `10-validation/COVERAGE_MATRIX.md`: update slide locations to new IDs (REQ03 SL09–SL16, REQ04 SL10, REQ05 SL11, SL12, SL15, REQ06 SL03–SL06, SL20–SL26, REQ07 SL07, SL23, SL24, REQ08 SL22, REQ09 SL29–SL38, REQ10 SL30, SL32, SL37, REQ11 SL26, SL36, SL57, SL73, REQ12 SL42–SL49, REQ13 SL52, SL53, SL57, REQ14 SL54–SL56, REQ15 SL61–SL66, REQ16 SL70, REQ17 SL71, SL72, REQ18 SL05, SL73, SL74) and add REQ22 “Self-explanatory slides: what-line, key point, openers and takeaways — SL01–SL76”.

- [ ] **Step 5: Manifest and package validator**

```bash
python3 - <<'EOF'
import json,hashlib
from pathlib import Path
m=json.load(open('MANIFEST.json'))
for f in m['files']:
    p=Path(f['path']); d=p.read_bytes(); f['sha256']=hashlib.sha256(d).hexdigest(); f['size_bytes']=len(d)
m['purpose']='Claude build handover; clarity rework v2 (76 slides) built 2026-10-02'
json.dump(m,open('MANIFEST.json','w'),indent=2)
EOF
python3 10-validation/validate_package.py
```

Expected: `PASS: …`.

- [ ] **Step 6: Final commit**

```bash
git add -A && git commit -qm "qa: v2 renders, interaction checks, reports and manifest"
git log --oneline | head -20
```

---

## Self-review notes

- **Spec coverage:** §2 decisions → Tasks 4–14; §3 structure → Task 4 ORDER; §4 interaction rules → Task 1 checks, Task 5 enforcement, Tasks 7–14, R1–R5; §5 explanation layer → Task 4 TEXT/NEW, Task 3 templates, Task 5 rendering, Task 6 CSS; §6 photos → Task 2, R6, Task 6 credit; §7 breaks and times → Task 4 (break titles, modules.json), Tasks 8/10/12 bodies, Task 6 labels, Task 1 clock/prayer checks; §8 timing → Task 4 MINUTES (M7 opener is 1 minute because M7 has only 20 minutes; all other openers/takeaways 2, SL41 3 for the glossary); §9 outputs → Task 15; §10 validation → Tasks 1, 15, 16.
- **Deviation recorded:** M7 opener 1 minute, SL41 opener 3 minutes (spec §8 says 2 each). Record in QA report.
- **Names consistent:** `checks.PAUSE_IDS`, `EXEMPT_IDS`, `GENERATED_LAYOUTS`, `check_plan_fields`, `check_open_slide`, `check_participant_text`, `check_whole_output`, `pause_kind`; `avatars.CAST`, `avatar_html`, `cast_html`; `generated.render_generated`, `keypoint`.
