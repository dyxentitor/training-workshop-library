#!/usr/bin/env python3
"""Build the offline workshop deck and its companion documents.

Standard library only. Run from anywhere:  python3 build/build.py

Inputs (all editable):
  04-content/slides.json            canonical plan: titles, timing, notes, options, sources
  02-research/sources.json          source registry
  config/customer-config.json       customer values (null = unconfirmed placeholder)
  src/slides/M*.html                per-slide body fragments (authored HTML)
  src/content/*.json                choice details, extra notes, modules, source groups
  src/css/*.css, src/js/deck.js     styles and runtime
  src/img/assets/*                  diagrams (inline SVG), icon sprite, scene photographs and backdrops
Outputs:
  dist/workshop.html                single self-contained deck (no network needed)
  dist/participant-quick-reference.html, dist/facilitator-guide.md, dist/SOURCE_INDEX.md
"""
import html
import json
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import checks  # noqa: E402
from avatars import avatar_html  # noqa: E402
from generated import render_generated  # noqa: E402
import assets  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
import os
DIST = Path(os.environ['DIST_DIR']) if os.environ.get('DIST_DIR') else ROOT / 'dist'
errors = []


def err(msg):
    errors.append(msg)


def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))


def esc(s):
    return html.escape(str(s), quote=True)


plan = load('04-content/slides.json')
SLIDES = plan['slides']
SOURCES = load('02-research/sources.json')
SRC_BY_ID = {s['id']: s for s in SOURCES}
CONFIG = json.loads(Path(os.environ['CUSTOMER_CONFIG']).read_text(encoding='utf-8')) if os.environ.get('CUSTOMER_CONFIG') else load('config/customer-config.json')
CHOICES = load('src/content/choices.json')
NOTES = load('src/content/notes.json')
MODULES = load('src/content/modules.json')
GROUPS = load('src/content/source-groups.json')

# ---------------------------------------------------------------- config
PLACEHOLDERS = {
    'customer_name': 'Customer name to be confirmed',
    'session_date': 'Date to be confirmed',
    'venue': 'Venue to be confirmed',
    'reporting.button_label': 'Confirm report button or menu',
    'reporting.mailbox': 'Confirm reporting mailbox',
    'reporting.phone': 'Confirm urgent phone route',
    'reporting.instructions': 'Confirm your organisation’s reporting steps',
    'support.contact': 'Confirm IT support contact',
    'support.ticket_process': 'Confirm support ticket process',
}


def config_value(path):
    """Return a confirmed value or None. Reporting/support values count only when verified."""
    parts = path.split('.')
    if parts[0] in ('reporting', 'support') and not CONFIG.get(parts[0], {}).get('verified'):
        return None
    v = CONFIG
    for p in parts:
        v = v.get(p) if isinstance(v, dict) else None
    return v if v not in (None, '', []) else None


def config_html(path):
    v = config_value(path)
    if v is not None:
        return f'<span class="confirmed">{esc(v)}</span>'
    return f'<span class="placeholder">[{esc(PLACEHOLDERS.get(path, "To be confirmed"))}]</span>'


REPORTING_VERIFIED = bool(CONFIG.get('reporting', {}).get('verified'))

# ---------------------------------------------------------------- QR (non-functional)


def qr_svg(seed, label='DEMO QR · NO SCAN'):
    """Decorative QR-like tile. Random cells carry no encoded data; a solid label band
    covers the centre, so the tile cannot be decoded. It never encodes a destination."""
    rnd = random.Random(seed)
    n, c = 25, 8
    cells = []
    finder = lambda x, y: (x < 7 and y < 7) or (x >= n - 7 and y < 7) or (x < 7 and y >= n - 7)
    for y in range(n):
        for x in range(n):
            if finder(x, y):
                continue
            if rnd.random() < .48:
                cells.append(f'<rect x="{x*c}" y="{y*c}" width="{c}" height="{c}"/>')
    fp = ''
    for (fx, fy) in ((0, 0), (n - 7, 0), (0, n - 7)):
        fp += (f'<rect x="{fx*c}" y="{fy*c}" width="{7*c}" height="{7*c}"/>'
               f'<rect x="{fx*c+c}" y="{fy*c+c}" width="{5*c}" height="{5*c}" fill="#fff"/>'
               f'<rect x="{fx*c+2*c}" y="{fy*c+2*c}" width="{3*c}" height="{3*c}"/>')
    w = n * c
    return (f'<svg class="qrsvg" viewBox="-8 -8 {w+16} {w+16}" role="img" aria-label="Illustrative QR-style tile. Not scannable; training demo only.">'
            f'<rect x="-8" y="-8" width="{w+16}" height="{w+16}" fill="#fff"/><g fill="#19283b">{"".join(cells)}{fp}</g>'
            f'<rect x="12" y="{w/2-22}" width="{w-24}" height="44" rx="6" fill="#19283b"/>'
            f'<text x="{w/2}" y="{w/2+6}" text-anchor="middle" fill="#fff" font-size="15" font-family="Arial, Helvetica, sans-serif" font-weight="700" letter-spacing="1">{esc(label)}</text></svg>')

# ---------------------------------------------------------------- choices


def choice_options(gid):
    """Options for a group: decision slides take label/feedback/preferred from slides.json."""
    extra = CHOICES.get(gid, {})
    plan_slide = next((s for s in SLIDES if s['id'] == gid), None)
    if plan_slide and plan_slide['options']:
        subs = extra.get('subs', [])
        details = extra.get('details', [])
        opts = []
        for i, o in enumerate(plan_slide['options']):
            opts.append({'label': o['label'], 'feedback': o['feedback'], 'preferred': bool(o.get('preferred')),
                         'sub': subs[i] if i < len(subs) else '', 'detail': details[i] if i < len(details) else ''})
        return opts
    if 'options' in extra:
        return [{'label': o['label'], 'feedback': o['feedback'], 'preferred': bool(o.get('preferred')),
                 'sub': o.get('sub', ''), 'detail': o.get('detail', '')} for o in extra['options']]
    err(f'choice group {gid} has no options')
    return []


USED_GROUPS = {}


def choices_html(gid, variant='', fb=''):
    opts = choice_options(gid)
    USED_GROUPS[gid] = opts
    if sum(o['preferred'] for o in opts) != 1:
        err(f'choice group {gid} must have exactly one preferred option')
    label = CHOICES.get(gid, {}).get('aria', 'Choose an action')
    letters = 'ABCDEF'
    btns = []
    for i, o in enumerate(opts):
        mini = 'mini' in variant.split()
        sub = f'<small>{esc(o["sub"])}</small>' if o['sub'] and not mini else ''
        letter = f'<span class="letter">{letters[i]}</span>' if not mini else ''
        btns.append(f'<button type="button" class="choice" data-act="choose" data-idx="{i}" aria-pressed="false">'
                    f'{letter}<strong>{esc(o["label"])}</strong>{sub}</button>')
    cls = 'choices' + (f' {variant}' if variant else '') + f' n{len(opts)}'
    fbattr = f' data-fb="{esc(fb)}"' if fb else ''
    return f'<div class="{cls}" role="group" aria-label="{esc(label)}" data-choice-group="{esc(gid)}"{fbattr}>{"".join(btns)}</div>'


def feedback_html(gid, prompt, cls=''):
    if not prompt:
        cls = (cls + ' mini').strip()
    return (f'<div class="feedback{(" " + cls) if cls else ""}" role="status" aria-live="polite" data-feedback="{esc(gid)}">'
            f'{prompt}</div>')

# ---------------------------------------------------------------- fragments


FRAG_RE = re.compile(r'<section\s+data-slide="(SL\d{2}[A-Z]?)"([^>]*)>(.*?)</section>', re.S)  # SL09B = continuation of SL09 (readability rework)
ATTR_RE = re.compile(r'(data-[\w-]+)(?:="([^"]*)")?')


def read_fragments():
    frags = {}
    for f in sorted((SRC / 'slides').glob('*.html')):
        text = f.read_text(encoding='utf-8')
        for m in FRAG_RE.finditer(text):
            sid = m.group(1)
            if sid in frags:
                err(f'duplicate fragment {sid}')
            frags[sid] = {'attrs': dict(ATTR_RE.findall(m.group(2))), 'body': m.group(3), 'file': f.name}
    return frags


def module_of(mid):
    return next(m for m in MODULES if m['id'] == mid)


def render_tokens(body, s):
    def rep(m):
        kind, arg = m.group(1), m.group(2) or ''
        if kind == 'title':
            return esc(s['title'])
        if kind == 'start':
            return esc(s['planned_start'])
        if kind == 'end':
            return esc(s['planned_end'])
        if kind == 'config':
            return config_html(arg)
        if kind == 'sessionline':
            # Date and venue appear on the slide only once confirmed; otherwise they stay in the
            # workshop information panel as placeholders and out of the presentation layout.
            parts = [config_value('session_date'), config_value('venue')]
            parts = [esc(x) for x in parts if x]
            return f'<p class="sessionline">{" · ".join(parts)}</p>' if parts else ''
        if kind == 'qr':
            parts = arg.split('|')
            return qr_svg(parts[0], parts[1] if len(parts) > 1 else 'DEMO QR · NO SCAN')
        if kind == 'choices':
            parts = arg.split('|')
            return choices_html(parts[0] or s['id'], parts[1] if len(parts) > 1 else '', parts[2] if len(parts) > 2 else '')
        if kind == 'feedback':
            parts = arg.split('|')
            gid = parts[0] or s['id']
            prompt = parts[1] if len(parts) > 1 else '<strong>Choose an action.</strong> Discuss your reasons before selecting.'
            return feedback_html(gid, prompt, parts[2] if len(parts) > 2 else '')
        if kind == 'decision':
            prompt = arg or '<strong>Choose an action.</strong> What makes your verification route trustworthy?'
            return choices_html(s['id']) + feedback_html(s['id'], prompt)
        if kind == 'reporting-banner':
            if REPORTING_VERIFIED:
                return '<div class="routebanner confirmed">Confirmed reporting route supplied by the customer</div>'
            return ('<div class="routebanner demo" role="note"><b>Demo reporting workflow</b> — confirm your organisation’s route. '
                    'Customer preparation: replace each bracketed field with verified details before live delivery.</div>')
        if kind == 'avatar':
            parts = arg.split('|')
            return avatar_html(parts[0], parts[1] if len(parts) > 1 and parts[1] else 'avatar', parts[2] if len(parts) > 2 else '')
        if kind == 'asset':                       # inline SVG diagram, ids namespaced to this slide
            parts = arg.split('|')
            return assets.inline_svg(parts[0], s['id'], parts[1] if len(parts) > 1 else '')
        if kind == 'icon':                        # <use> of the sprite inlined once in the shell
            parts = arg.split('|')
            return assets.icon_html(parts[0], parts[1] if len(parts) > 1 else '')
        if kind == 'image':                       # embedded JPEG scene photograph (illustrative, fictional)
            parts = arg.split('|')
            return assets.image_html(parts[0], parts[1] if len(parts) > 1 else '', parts[2] if len(parts) > 2 else '')
        err(f'{s["id"]}: unknown token {kind}')
        return ''
    return re.sub(r'\{\{(\w[\w-]*)(?::([^}]*))?\}\}', rep, body)


DEFAULT_PILL = {'fictional': 'Training scenario', 'documented': 'Documented incident'}
DEFAULT_SOURCE_PREFIX = {'fictional': 'Fictional scenario. Guidance:', 'documented': 'Source:', 'guidance': 'Sources:', 'logistics': ''}


def source_line(s, attrs):
    ids = s['source_ids']
    if not ids or 'data-nosource' in attrs:
        return ''
    prefix = attrs.get('data-source-note', DEFAULT_SOURCE_PREFIX[s['evidence_kind']])
    links = '; '.join(
        f'<a href="{esc(SRC_BY_ID[i]["url"])}" target="_blank" rel="noopener noreferrer">{esc(SRC_BY_ID[i]["title"])}'
        f'{", " + esc(SRC_BY_ID[i]["published"]) if SRC_BY_ID[i]["published"] else ""}</a>' for i in ids)
    after = attrs.get('data-source-after', '')
    return f'<p class="source">{esc(prefix)} {links}.{(" " + esc(after)) if after else ""}</p>'


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
                # data-on = label while revealed; data-off = label while hidden
                right = (f'<button type="button" class="primary" data-act="reveal" aria-expanded="false" '
                         f'data-off="{esc(on)}" data-on="{esc(off or "Hide")}">{esc(on)}</button>')
            else:
                pill = a.get('data-pill', DEFAULT_PILL.get(s['evidence_kind'], ''))
                if pill:
                    right = f'<span class="pill">{esc(pill)}</span>'
            what = '' if exempt else f'<p class="what">{esc(s["what_this_shows"])}</p>'
            # kicker and pill share one row so the title can use the full width; a reveal button is pinned at the right
            btn = 'data-reveal' in a
            head = (f'<div class="head{" has-btn" if btn else ""}"><div class="headrow"><p class="kicker">{esc(a.get("data-kicker", ""))}</p>'
                    f'{"" if btn else right}</div><h2 id="{sid}-title">{esc(s["title"])}</h2>{what}{right if btn else ""}</div>')
    # the footer carries only the source line; the teaching point sits inside the content (takeaway rework, 8 Oct 2026)
    foot = source_line(s, a)
    if foot:
        foot = f'<div class="foot">{foot}</div>'
    cls = ['slide']
    kind = checks.pause_kind(body) if s['pause_point'] else ''
    if s['pause_point']:
        cls += ['pause', 'pause-' + kind]
    for m in checks.check_takeaway(sid, body, kind):
        err(m)
    return (f'<section class="{" ".join(cls)}" id="{sid}" data-module="{s["module"]}" data-layout="{s["layout"]}" '
            f'aria-labelledby="{sid}-title" aria-roledescription="slide">'
            f'{head}<div class="body">{body}</div>{foot}</section>')   # body row of the slide grid (8 Oct 2026)

# ---------------------------------------------------------------- checks


def check_html(sid, h, title):
    ids = re.findall(r'\sid="([^"]+)"', h)
    for i in ids:
        if not i.startswith(sid):
            err(f'{sid}: element id "{i}" must start with the slide ID')
    for cs in re.findall(r'aria-controls="([^"]+)"', h):
        for c in cs.split():
            if c not in ids:
                err(f'{sid}: aria-controls target {c} missing')
    m = re.search(rf'<h[12][^>]*id="{sid}-title"[^>]*>(.*?)</h[12]>', h, re.S)
    if not m:
        err(f'{sid}: heading with id {sid}-title missing')
        return
    else:
        text = html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'<br\s*/?>', ' ', m.group(1))))
        if ' '.join(text.split()) != title:
            err(f'{sid}: heading "{text}" differs from slides.json title "{title}"')
    for bad, why in ((r'<input|<textarea|<select|<form', 'form control'), (r'<iframe|<object|<embed', 'embedded content'),
                     (r'href="(?:mailto|tel|javascript):', 'functional contact/script link'),
                     (r'href="[^"]*\.(?:example|test)\b', 'link to a mock destination'),
                     (r'\son\w+="', 'inline event handler'), (r'<script', 'script in fragment'),
                     (r'src="https?:', 'remote asset')):
        if re.search(bad, h, re.I):
            err(f'{sid}: forbidden {why}')
    for href in re.findall(r'href="([^"]+)"', h):
        if not href.startswith(('https://', 'http://', '#')) and not href.endswith('.html'):
            err(f'{sid}: unexpected href {href}')


def build_deck():
    frags = read_fragments()
    plan_ids = [s['id'] for s in SLIDES]
    generated_ids = {s['id'] for s in SLIDES if s['layout'] in checks.GENERATED_LAYOUTS}
    for sid in plan_ids:
        if sid not in frags and sid not in generated_ids:
            err(f'missing fragment for {sid}')
    for sid in frags:
        if sid not in plan_ids or sid in generated_ids:
            err(f'fragment {sid} not expected (unknown ID or generated layout)')
    if errors:
        return None
    # programme checks
    if sum(s['duration_minutes'] for s in SLIDES) != plan['duration_minutes'] or plan['duration_minutes'] != 420:
        err('programme must total 420 minutes')
    for m in MODULES:
        got = sum(s['duration_minutes'] for s in SLIDES if s['module'] == m['id'])
        if got != m['minutes']:
            err(f'module {m["id"]} totals {got}, modules.json says {m["minutes"]}')
    for s in SLIDES:
        for i in s['source_ids']:
            if i not in SRC_BY_ID:
                err(f'{s["id"]}: unknown source {i}')
    for s in SLIDES:
        for m in checks.check_plan_fields(s):
            err(m)
    habits = [(s.get('module_label', ''), s['habit']) for s in SLIDES if s['layout'] == 'takeaway']
    habits.append(('Module 7', 'Pause, verify, report, recover.'))
    sections = []
    for s in SLIDES:
        h = render_slide(s, frags.get(s['id']), habits)
        check_html(s['id'], h, s['title'])
        if not s['pause_point'] and s['id'] not in checks.COVER_REVEAL_IDS:
            for m in checks.check_open_slide(s['id'], h):
                err(m)
        for m in checks.check_participant_text(s['id'], h, s['layout']):
            err(m)
        sections.append(h)
    for s in SLIDES:
        if s['options'] and s['id'] not in USED_GROUPS:
            err(f'{s["id"]}: decision options in slides.json are not rendered')
    all_ids = re.findall(r'\sid="([^"]+)"', ''.join(sections))
    dup = {i for i in all_ids if all_ids.count(i) > 1}
    if dup:
        err(f'duplicate element ids: {sorted(dup)}')

    data = {
        'slides': [{
            'id': s['id'], 'module': s['module'], 'moduleName': module_of(s['module'])['name'], 'title': s['title'],
            'start': s['planned_start'], 'end': s['planned_end'], 'minutes': s['duration_minutes'],
            'objective': s['objective'], 'notes': s['facilitator_notes'], 'interaction': s['interaction'],
            'reveal': s['reveal'], 'answer': NOTES.get(s['id'], {}).get('answer', ''),
            'notesExtra': NOTES.get(s['id'], {}).get('extra', []), 'sourceIds': s['source_ids'],
            'whatThisShows': s.get('what_this_shows', ''), 'keyPoint': s.get('key_point', ''),   # notes summary; on screen as a takeaway
        } for s in SLIDES],
        'modules': MODULES,
        'sources': [{k: x[k] for k in ('id', 'title', 'url', 'published', 'use_and_limits')} for x in SOURCES],
        'sourceGroups': GROUPS,
        'choices': {g: [{k: o[k] for k in ('label', 'feedback', 'detail', 'preferred')} for o in opts] for g, opts in USED_GROUPS.items()},
    }
    grouped = [i for g in GROUPS for i in g['ids']]
    if sorted(grouped) != sorted(SRC_BY_ID):
        err('source-groups.json must list every source exactly once')
    css = (SRC / 'css/base.css').read_text(encoding='utf-8') + '\n' + (SRC / 'css/deck.css').read_text(encoding='utf-8')
    def asset_uri(m):
        opts = dict(o.partition('=')[::2] for o in m.group(2).split('|') if o)
        return assets.data_uri(m.group(1), int(opts['band']) if 'band' in opts else None, 'transparent' in opts)
    css = re.sub(r'\{\{asset-uri:([\w.-]+)((?:\|[\w=]+)*)\}\}', asset_uri, css)
    js = (SRC / 'js/deck.js').read_text(encoding='utf-8')
    shell = (SRC / 'shell.html').read_text(encoding='utf-8')
    data_json = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    shell = re.sub(r'\{\{config:([\w.]+)\}\}', lambda m: config_html(m.group(1)), shell)
    out = (shell.replace('/*CSS*/', css).replace('<!--SLIDES-->', '\n'.join(sections)).replace('<!--SPRITE-->', assets.sprite_html())
           .replace('/*DATA*/', data_json).replace('/*JS*/', js)
           .replace('{{course_title}}', esc(CONFIG.get('course_title') or 'Cybersecurity Awareness: Impersonation and Phishing')))
    for m in checks.check_whole_output(out):
        err(m)
    for bad in ('fetch(', 'XMLHttpRequest', 'navigator.clipboard', 'execCommand', 'localStorage', 'sessionStorage', 'document.cookie', 'WebSocket', 'sendBeacon'):
        if bad in out:
            err(f'runtime contains forbidden API {bad}')
    if re.search(r'<(?:link|script)[^>]+(?:href|src)="https?:', out):
        err('remote stylesheet/script reference found')
    return out


def main():
    deck = build_deck()
    if errors:
        print('BUILD FAILED' if '--draft' not in sys.argv else f'DRAFT BUILD with {len(errors)} errors (not for delivery)')
        for e in errors:
            print(' -', e)
        if '--draft' not in sys.argv or deck is None:
            sys.exit(1)
        DIST.mkdir(exist_ok=True)
        (DIST / 'workshop.html').write_text(deck, encoding='utf-8')
        sys.exit(2)
    DIST.mkdir(exist_ok=True)
    (DIST / 'workshop.html').write_text(deck, encoding='utf-8')
    import make_docs  # companion documents share the same data
    make_docs.run(globals())
    print(f'OK: {DIST / "workshop.html"} ({len(deck)//1024} KB, {len(SLIDES)} slides, '
          f'{sum(s["duration_minutes"] for s in SLIDES)} minutes); companion documents written.')


if __name__ == '__main__':
    sys.path.insert(0, str(Path(__file__).parent))
    main()
