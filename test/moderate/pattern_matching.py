from unittest import TestCase

from moderate.pattern_matching import matches


class Test(TestCase):
    def test(self):
        pattern = "aabab"
        string = "catcatgocatgo"
        self.assertTrue(matches(pattern, string))

    def test_single_a_matches_everything(self):
        pattern = "a"
        string = "asdifasiodufasefasefaseasdfjai"
        self.assertTrue(matches(pattern, string))

    def test_single_b_matches_everything(self):
        pattern = "b"
        string = "asdifasiodufasefasefaseasdfjai"
        self.assertTrue(matches(pattern, string))

    def test_ab_matches_everything(self):
        pattern = "ab"
        string = "asdifasiodufasefasefaseasdfjai"
        self.assertTrue(matches(pattern, string))

    def test_ab_matches_single_char(self):
        pattern = "ab"
        string = "j"
        self.assertTrue(matches(pattern, string))

    def test_no_match(self):
        pattern = "aababa"
        string = "catcatgocatgo"
        self.assertFalse(matches(pattern, string))
