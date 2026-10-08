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
