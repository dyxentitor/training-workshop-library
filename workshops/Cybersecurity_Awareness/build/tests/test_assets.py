import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import assets


SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50" viewBox="0 0 100 50" role="img" aria-labelledby="title desc">'
       '<title id="title">T</title><desc id="desc">D</desc><defs><style>text{font-family:Arial}</style>'
       '<marker id="arrow-grey"></marker><marker id="arrow-grey2"></marker></defs>'
       '<text id="label-1">a</text><text id="label-10">b</text>'
       '<path marker-end="url(#arrow-grey)"/><path marker-end="url(#arrow-grey2)"/><use href="#label-1"/></svg>')


class NamespaceTests(unittest.TestCase):
    def test_ids_and_references_get_the_prefix(self):
        out = assets.namespace_svg(SVG, 'SL43-x-')
        self.assertIn('id="SL43-x-arrow-grey"', out)
        self.assertIn('id="SL43-x-arrow-grey2"', out)
        self.assertIn('url(#SL43-x-arrow-grey)', out)
        self.assertIn('url(#SL43-x-arrow-grey2)', out)
        self.assertIn('href="#SL43-x-label-1"', out)
        self.assertIn('id="SL43-x-label-10"', out)
        self.assertIn('aria-labelledby="SL43-x-title SL43-x-desc"', out)
        self.assertNotIn('url(#arrow', out)

    def test_every_id_in_the_output_carries_the_prefix(self):
        out = assets.namespace_svg(SVG, 'SL12-y-')
        for i in re.findall(r'\bid="([^"]+)"', out):
            self.assertTrue(i.startswith('SL12-y-'), i)


class InlineTests(unittest.TestCase):
    def test_inline_svg_drops_fixed_size_and_style_and_wraps(self):
        out = assets.inline_svg('flow-002-device-code', 'SL45')
        self.assertTrue(out.startswith('<div class="diagram-wrap">'))
        self.assertIn('class="diagram"', out)
        self.assertNotIn('<style>', out)
        self.assertNotIn(' width="698"', out)
        self.assertIn('viewBox="0 0 698 340"', out)
        for i in re.findall(r'\bid="([^"]+)"', out):
            self.assertTrue(i.startswith('SL45-flow-002-device-code-'), i)

    def test_wide_variant_adds_the_class(self):
        self.assertTrue(assets.inline_svg('info-003-chain-strip', 'SL66', 'wide').startswith('<div class="diagram-wrap wide">'))

    def test_unknown_asset_raises(self):
        with self.assertRaises(FileNotFoundError):
            assets.inline_svg('no-such-asset', 'SL01')


class IconTests(unittest.TestCase):
    def test_sprite_prefixes_symbol_ids_once(self):
        sprite = assets.sprite_html()
        self.assertEqual(sprite.count('<symbol'), 14)
        self.assertIn('id="icon-route-app"', sprite)
        self.assertIn('aria-hidden="true"', sprite)
        self.assertNotIn('id="route-app"', sprite)

    def test_icon_reference(self):
        self.assertEqual(assets.icon_html('report'), '<svg class="icon" aria-hidden="true" focusable="false"><use href="#icon-report"/></svg>')
        self.assertIn('class="icon lg"', assets.icon_html('pause', 'lg'))

    def test_unknown_icon_raises(self):
        with self.assertRaises(KeyError):
            assets.icon_html('mfa-done')


class ImageTests(unittest.TestCase):
    def test_image_is_an_embedded_jpeg(self):
        out = assets.image_html('img-001-aina-unexpected-call', 'Aina at her desk', 'short')
        self.assertTrue(out.startswith('<img class="scene-photo short" src="data:image/jpeg;base64,/9j/'))
        self.assertIn('alt="Aina at her desk"', out)

    def test_transparent_variant_drops_the_base_rect(self):
        text = (assets.ASSET_DIR / 'bg-002-opener-pattern.svg').read_text()
        self.assertIn('fill="#0B1220"/>', text)
        self.assertNotIn('<rect width="1600" height="900"', assets.svg_without_base(text))
        self.assertNotEqual(assets.data_uri('bg-002-opener-pattern.svg'), assets.data_uri('bg-002-opener-pattern.svg', transparent=True))
        self.assertNotEqual(assets.data_uri('bg-002-opener-pattern.svg', band=26), assets.data_uri('bg-002-opener-pattern.svg', band=26, transparent=True))

    def test_data_uri_svg_band_variant(self):
        full = assets.data_uri('bg-002-opener-pattern.svg')
        short = assets.data_uri('bg-002-opener-pattern.svg', band=26)
        self.assertTrue(full.startswith('data:image/svg+xml;base64,'))
        self.assertNotEqual(full, short)
        self.assertIn('height="26"', assets.svg_band_variant((assets.ASSET_DIR / 'bg-002-opener-pattern.svg').read_text(), 26))


if __name__ == '__main__':
    unittest.main()
