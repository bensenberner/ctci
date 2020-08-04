import unittest

from moderate.t9 import T9


class Test(unittest.TestCase):
    def test(self):
        digits = "8733"
        words = [
            "crayon",
            "hemp",
            "live",
            "lol",
            "tree",
            "trunk",
            "tune",
            "used",
        ]
        self.assertCountEqual(
            ["tree", "used"],
            T9.find_all_words_spellable_from(t9_input=digits, possible_words=words),
        )
