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
