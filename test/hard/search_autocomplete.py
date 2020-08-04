import unittest

from hard.search_autocomplete import AutocompleteSystem


class Test(unittest.TestCase):
    def test(self):
        historical_sentences = ["i love you", "island", "ironman", "i love leetcode"]
        historical_counts = [5, 3, 2, 2]
        ac_system = AutocompleteSystem(historical_sentences, historical_counts)
        self.assertListEqual(
            ["i love you", "island", "i love leetcode"], ac_system.input("i")
        )

        self.assertListEqual(["i love you", "i love leetcode"], ac_system.input(" "))

        self.assertListEqual([], ac_system.input("a"))

        self.assertListEqual([], ac_system.input("#"))

        self.assertListEqual(
            ["i love you", "island", "i love leetcode"], ac_system.input("i")
        )
        self.assertListEqual(
            ["i love you", "i love leetcode", "i a"], ac_system.input(" ")
        )
        self.assertListEqual(["i a"], ac_system.input("a"))
        self.assertListEqual([], ac_system.input("m"))
        self.assertListEqual([], ac_system.input("#"))
