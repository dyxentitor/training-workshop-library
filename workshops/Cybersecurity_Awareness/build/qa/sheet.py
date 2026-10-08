"""QA helper: 2x2 contact sheets of 1366x768 renders (expanded state when present).
Usage: python3 build/qa/sheet.py SL01 SL02 ... -> prints sheet paths (needs Pillow)."""
import os, sys
from PIL import Image
d = 'validation/screenshots/1366x768'
out = '/tmp/claude-1000/-home-universal-Claude-Cybersecurity-training-awareness/60fb327e-0383-4328-ac04-07935ddab15e/scratchpad/sheets76'
os.makedirs(out, exist_ok=True)
def pick(i):
    for st in ('expanded', 'default'):
        p = f'{d}/{i}-1366x768-{st}.png'
        if os.path.exists(p):
            return p
ids = sys.argv[1:]
for k in range(0, len(ids), 4):
    s = Image.new('RGB', (1366, 768), 'white')
    for j, i in enumerate(ids[k:k + 4]):
        s.paste(Image.open(pick(i)).resize((683, 384)), ((j % 2) * 683, (j // 2) * 384))
    p = f'{out}/{ids[k]}-{ids[min(k + 3, len(ids) - 1)]}.png'
    s.save(p)
    print(p)
