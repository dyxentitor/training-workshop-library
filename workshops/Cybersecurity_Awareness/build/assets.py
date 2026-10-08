"""Visual assets embedded by the build (asset pack of 8 October 2026, src/img/assets/).

- Diagrams (FLOW-*, INFO-*) are inlined as SVG so their text stays editable and selectable. Every id
  inside a diagram is prefixed with the slide ID and the asset name, so an asset can be repeated and
  the build's "ids start with the slide ID" rule still holds. The root width/height are dropped so the
  slide stylesheet sizes the drawing; the viewBox keeps the proportions.
- Icons (ICON-001) are one sprite of <symbol>s inlined once in the shell and referenced with <use>.
- Scene photographs and the cover backdrop (IMG-*, BG-001) are JPEG data URIs (CSP img-src data:).
- Opener/break patterns (BG-002/003) are SVG data URIs used as CSS backgrounds.
Pure helpers; build.py wires the {{asset}}, {{icon}} and {{image}} tokens.
"""
import base64
import html
import re
from pathlib import Path

ASSET_DIR = Path(__file__).resolve().parents[1] / 'src/img/assets'
ID_ATTR = re.compile(r'\bid="([^"]+)"')
SPRITE = 'icon-001-workshop-icons'
ICON_PREFIX = 'icon-'
_cache = {}


def _read(name):
    if name not in _cache:
        _cache[name] = (ASSET_DIR / name).read_bytes()
    return _cache[name]


def namespace_svg(svg, prefix):
    """Prefix every id and every reference to it (url(#id), href="#id", aria-labelledby)."""
    ids = set(ID_ATTR.findall(svg))
    svg = ID_ATTR.sub(lambda m: f'id="{prefix}{m.group(1)}"', svg)
    for i in sorted(ids, key=len, reverse=True):
        svg = svg.replace(f'url(#{i})', f'url(#{prefix}{i})').replace(f'href="#{i}"', f'href="#{prefix}{i}"')

    def labelled(m):
        return 'aria-labelledby="' + ' '.join(prefix + t if t in ids else t for t in m.group(1).split()) + '"'
    return re.sub(r'aria-labelledby="([^"]+)"', labelled, svg)


def _clean_svg(text):
    text = re.sub(r'<\?xml[^>]*\?>', '', text)
    text = re.sub(r'<style>.*?</style>', '', text, flags=re.S)   # fonts come from the deck stylesheet
    return text.strip()


def inline_svg(name, sid, variant=''):
    """Inline diagram for one slide: <div class="diagram-wrap [wide]"><svg class="diagram" …>."""
    text = _clean_svg(_read(f'{name}.svg').decode('utf-8'))

    def root(m):
        attrs = re.sub(r'\s(?:width|height)="[^"]*"', '', m.group(1))
        return f'<svg class="diagram"{attrs}'
    text = re.sub(r'<svg([^>]*)', root, text, count=1)
    text = namespace_svg(text, f'{sid}-{name}-')
    cls = 'diagram-wrap' + (f' {variant}' if variant else '')
    return f'<div class="{cls}">{text}</div>'


def sprite_html():
    """The icon sprite, inlined once per document; symbol ids become icon-<name>."""
    text = _clean_svg(_read(f'{SPRITE}.svg').decode('utf-8'))
    text = namespace_svg(text, ICON_PREFIX)
    return re.sub(r'<svg([^>]*)', r'<svg class="sprite" aria-hidden="true" focusable="false"\1', text, count=1)


def icon_names():
    return set(re.findall(r'<symbol id="([^"]+)"', _read(f'{SPRITE}.svg').decode('utf-8')))


def icon_html(name, cls=''):
    if name not in icon_names():
        raise KeyError(f'unknown icon {name}')
    c = 'icon' + (f' {cls}' if cls else '')
    return f'<svg class="{c}" aria-hidden="true" focusable="false"><use href="#{ICON_PREFIX}{name}"/></svg>'


def data_uri(filename, band=None, transparent=False):
    data = _read(filename)
    if filename.endswith('.svg'):
        text = data.decode('utf-8')
        if band is not None:
            text = svg_band_variant(text, band)
        if transparent:
            text = svg_without_base(text)
        return 'data:image/svg+xml;base64,' + base64.b64encode(text.encode('utf-8')).decode()
    mime = 'image/jpeg' if filename.endswith(('.jpg', '.jpeg')) else 'image/png'
    return f'data:{mime};base64,' + base64.b64encode(data).decode()


def svg_band_variant(text, band):
    """BG-002 restricted band (SL41 keeps its glossary clear): clip the pattern to `band` canvas px below y 74."""
    out, n = re.subn(r'(<clipPath id="[^"]+"><rect x="0" y="74" width="\d+" height=")\d+(")', rf'\g<1>{band}\2', text)
    if n != 1:
        raise ValueError('band clip not found')
    return out


def svg_without_base(text):
    """Drop the full-canvas navy rect so a backdrop pattern can overlay a photograph."""
    out, n = re.subn(r'<rect width="\d+" height="\d+" fill="#0B1220"/>', '', text)
    if n != 1:
        raise ValueError('base rect not found')
    return out


def image_html(name, alt, cls=''):
    c = 'scene-photo' + (f' {cls}' if cls else '')
    return f'<img class="{c}" src="{data_uri(name + ".jpg")}" alt="{html.escape(alt, quote=True)}">'
