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
        self.assertNotIn('keypoint', h)                 # openers carry no banner (takeaway rework, 8 Oct 2026)
        self.assertNotIn('class="takeaway"', h)

    def test_glossary(self):
        s = {'id': 'SL41B', 'layout': 'glossary', 'title': 'Words we will use', 'module_label': 'Module 4',
             'what_this_shows': 'Six words', 'key_point': 'K', 'glossary': [['MFA', 'A second check'], ['Session', 'Staying signed in']]}
        h = generated.render_generated(s, MODS, [])
        self.assertIn('<h1 id="SL41B-title">Words we will use</h1>', h)
        self.assertEqual(h.count('<dt>'), 2)
        self.assertIn('class="takeaway"', h)            # the point sits under the title, not in a footer banner
        self.assertNotIn('keypoint', h)

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
        s = {'id': 'SL75', 'layout': 'recap', 'title': 'Today’s takeaways', 'what_this_shows': 'W', 'key_point': 'When asked: pause and check.'}
        h = generated.render_generated(s, MODS, [('Module 1', 'h1'), ('Module 2', 'h2')])
        self.assertIn('h1', h)
        self.assertIn('Module 2', h)
        self.assertIn('<p class="tmain">When asked:</p>', h)
        self.assertIn('<p class="tnote">pause and check.</p>', h)

    def test_agenda_takeaway_under_day_list(self):
        s = {'id': 'SL02', 'layout': 'agenda', 'title': 'T', 'what_this_shows': 'W', 'outcomes': ['o'], 'rules': ['r'],
             'key_point': 'Today is about one habit: check it.'}
        h = generated.render_generated(s, MODS, [])
        self.assertIn('</ul><div class="takeaway"><p class="tlabel">One habit for today</p><p class="tmain">Check it.</p></div></div>', h)

    def test_takeaway_block(self):
        h = generated.takeaway('Main <b>', 'Label', ['a', 'b'], 'note')
        self.assertEqual(h, '<div class="takeaway"><p class="tlabel">Label</p><p class="tmain">Main &lt;b&gt;</p>'
                            '<ul class="tacts"><li>a</li><li>b</li></ul><p class="tnote">note</p></div>')
        self.assertEqual(generated.takeaway('M', ''), '<div class="takeaway"><p class="tmain">M</p></div>')

    def test_escapes(self):
        s = {'id': 'SL75', 'layout': 'recap', 'title': 'T', 'what_this_shows': '<b>', 'key_point': '<i>'}
        h = generated.render_generated(s, MODS, [('M', '<i>')])
        self.assertIn('&lt;b&gt;', h)
        self.assertNotIn('<i>', h)


if __name__ == '__main__':
    unittest.main()
