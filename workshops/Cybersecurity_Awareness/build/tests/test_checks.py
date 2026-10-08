import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import checks


class TestSets(unittest.TestCase):
    def test_pause_ids_exact(self):
        self.assertEqual(checks.PAUSE_IDS, frozenset(
            'SL05 SL06 SL11 SL16 SL25 SL26 SL31 SL36 SL49 SL53 SL57 SL62 SL63 SL64 SL65 SL73'.split()))
        self.assertEqual(len(checks.PAUSE_IDS), 16)

    def test_exempt_ids(self):
        self.assertEqual(checks.EXEMPT_IDS, frozenset({'SL01', 'SL18', 'SL40', 'SL59', 'SL76'}))


class TestPlanFields(unittest.TestCase):
    def base(self, **kw):
        s = {'id': 'SL03', 'layout': 'email', 'what_this_shows': 'x', 'key_point': 'y', 'pause_point': False}
        s.update(kw)
        return s

    def test_ok(self):
        self.assertEqual(checks.check_plan_fields(self.base()), [])

    def test_missing_what(self):
        self.assertTrue(checks.check_plan_fields(self.base(what_this_shows='')))

    def test_exempt_needs_nothing(self):
        self.assertEqual(checks.check_plan_fields({'id': 'SL18', 'layout': 'intermission', 'pause_point': False}), [])

    def test_pause_flag_must_match_list(self):
        self.assertTrue(checks.check_plan_fields(self.base(id='SL05', pause_point=False)))
        self.assertTrue(checks.check_plan_fields(self.base(id='SL03', pause_point=True)))


class TestOpenSlide(unittest.TestCase):
    def test_clean_open_slide(self):
        self.assertEqual(checks.check_open_slide('SL03', '<div class="mail"><p>hi</p></div>'), [])

    def test_rejects_toggle_and_hidden(self):
        errs = checks.check_open_slide('SL03', '<button data-act="toggle"></button><p hidden>x</p>')
        self.assertEqual(len(errs), 2)

    def test_word_hidden_in_text_is_fine(self):
        self.assertEqual(checks.check_open_slide('SL03', '<p>The hidden fact is shown.</p>'), [])

    def test_rejects_reveal_classes(self):
        self.assertTrue(checks.check_open_slide('SL03', '<p class="callout if-revealed">x</p>'))
        self.assertTrue(checks.check_open_slide('SL03', '<div class="if-chosen"><div class="takeaway">x</div></div>'))

    def test_allows_navigation_actions(self):
        self.assertTrue(checks.check_open_slide('SL01', '<button data-act="next">Go</button>'))
        self.assertIn('SL01', checks.COVER_REVEAL_IDS)
        self.assertEqual(checks.check_open_slide('SL76', '<button data-act="sources">S</button>'), [])


class TestParticipantText(unittest.TestCase):
    def test_clock_time_on_break(self):
        self.assertTrue(checks.check_participant_text('SL18', '<p>Back at 11:15</p>', 'intermission'))

    def test_clock_time_allowed_in_evidence(self):
        self.assertEqual(checks.check_participant_text('SL03', '<span>Tuesday, 16:42</span>', 'email'), [])

    def test_prayer_anywhere(self):
        self.assertTrue(checks.check_whole_output('<p>Lunch and Prayer</p>'))
        self.assertEqual(checks.check_whole_output('<p>Lunch break</p>'), [])


class TestTakeaway(unittest.TestCase):
    def test_open_slide_takeaway_is_fine(self):
        self.assertEqual(checks.check_takeaway('SL03', '<div class="takeaway"><p class="tmain">x</p></div>', ''), [])

    def test_pause_slide_takeaway_must_wait(self):
        self.assertTrue(checks.check_takeaway('SL05', '<div class="takeaway"><p class="tmain">x</p></div>', 'vote'))
        self.assertEqual(checks.check_takeaway('SL05', '<div class="if-chosen"><div class="takeaway">x</div></div>', 'vote'), [])
        self.assertEqual(checks.check_takeaway('SL06', '<div class="if-revealed"><div class="takeaway row">x</div></div>', 'reveal'), [])
        self.assertTrue(checks.check_takeaway('SL05', '<div class="if-revealed"><div class="takeaway">x</div></div>', 'vote'))

    def test_whole_output_rejects_old_banner(self):
        self.assertTrue(checks.check_whole_output('<div class="keypoint"><b>Key point</b></div>'))
        self.assertTrue(checks.check_whole_output('<div class="answerbox">x</div>'))
        self.assertEqual(checks.check_whole_output('<div class="takeaway">x</div>'), [])


class TestPauseKind(unittest.TestCase):
    def test_kinds(self):
        self.assertEqual(checks.pause_kind('<div data-choice-group="SL05"></div>'), 'vote')
        self.assertEqual(checks.pause_kind('<div class="if-revealed"></div>'), 'reveal')


if __name__ == '__main__':
    unittest.main()
