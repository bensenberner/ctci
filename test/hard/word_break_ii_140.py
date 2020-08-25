import unittest

from hard.word_break_ii_140 import wordBreak


class Test(unittest.TestCase):
    def test(self):
        s = "catsanddog"
        word_dict = ["cat", "cats", "and", "sand", "dog"]
        expected = ["cats and dog", "cat sand dog"]
        self.assertCountEqual(expected, wordBreak(s, word_dict))

    def test_dumb(self):
        self.assertEqual([], wordBreak("", ["a", "b", "c'"]))

    def test_long(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        word_dict = [
            "a",
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
        ]
        self.assertEqual([], wordBreak(s, word_dict))
