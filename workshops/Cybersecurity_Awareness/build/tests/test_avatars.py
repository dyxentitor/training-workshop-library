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
