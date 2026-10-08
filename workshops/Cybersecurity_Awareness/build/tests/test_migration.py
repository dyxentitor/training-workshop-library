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
        self.assertEqual(self.plan['slide_count'], 89)   # 87 + SL23B (takeaway rework) + SL04B (layout fix), 8 Oct 2026
        self.assertEqual(len(self.s), 89)
        originals = [x['id'] for x in self.s if len(x['id']) == 4]
        self.assertEqual(originals, [f'SL{i:02d}' for i in range(1, 77)])
        # continuation slides (readability rework, 8 Oct 2026) sit directly after their parent, in the same module
        for i, x in enumerate(self.s):
            if len(x['id']) == 5:
                self.assertEqual(self.s[i - 1]['id'][:4], x['id'][:4], x['id'])
                self.assertEqual(x['module'], self.s[i - 1]['module'])

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
        by = {x['id']: x['title'] for x in self.s}
        self.assertEqual([by[i] for i in ('SL18', 'SL40', 'SL59')], ['Short break', 'Lunch break', 'Tea break'])

    def test_no_prayer_in_plan(self):
        self.assertNotRegex(json.dumps(self.plan), '(?i)prayer')

    def test_fragments_renamed(self):
        ids = set()
        for f in (ROOT / 'src/slides').glob('*.html'):
            ids |= set(__import__('re').findall(r'data-slide="(SL\d\d[A-Z]?)"', f.read_text(encoding='utf-8')))
        generated = {x['id'] for x in self.s if x['layout'] in checks.GENERATED_LAYOUTS}
        self.assertEqual(ids | generated, {x['id'] for x in self.s})
        self.assertFalse(ids & generated)


if __name__ == '__main__':
    unittest.main()
