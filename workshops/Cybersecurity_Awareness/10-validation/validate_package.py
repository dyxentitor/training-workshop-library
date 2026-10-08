"""Validate the handover's factual cross-references, timing and assets. No dependency install."""
from pathlib import Path
import json, hashlib
r=Path(__file__).resolve().parents[1]
s=json.loads((r/'04-content/slides.json').read_text())
sources={x['id'] for x in json.loads((r/'02-research/sources.json').read_text())}
assert len(s['slides'])==s['slide_count']==89
assert len({x['id'] for x in s['slides']})==89
assert sum(x['duration_minutes'] for x in s['slides'])==420
expected={'M0':20,'M1':45,'B1':10,'M2':45,'M3':60,'B2':75,'M4':50,'M5':35,'B3':25,'M6':35,'M7':20}
for m,n in expected.items(): assert sum(x['duration_minutes'] for x in s['slides'] if x['module']==m)==n
for x in s['slides']:
 assert x['title'] and x['objective'] and x['screen_text']
 assert set(x['source_ids'])<=sources
 assert x['evidence_kind'] in ['fictional','documented','guidance','logistics']
 if x['evidence_kind']=='documented':assert x['source_ids']
 if x['layout']=='decision':assert x['options']
 if x['options']:assert sum(bool(o.get('preferred')) for o in x['options'])==1
assert s['slides'][0]['planned_start']=='10:00' and s['slides'][-1]['planned_end']=='17:00'
assert len(list((r/'06-prototype/reference_screenshots').glob('slide-0[1-6].png')))==6
assert (r/'06-prototype/prototype.html').stat().st_size>20000
manifest=json.loads((r/'MANIFEST.json').read_text())
for f in manifest['files']:
 p=r/f['path'];assert p.is_file(),p
 assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],p
print('PASS: slide IDs, 420-minute timing, source references, decision keys, prototype screenshots and manifest integrity')
