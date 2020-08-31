import unittest

from hard.word_search_ii_212 import findWords


class Test(unittest.TestCase):
    def test_lc(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "rain"]

        expected = ["eat", "oath"]
        self.assertCountEqual(expected, findWords(board, words))

    def no_words_found(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = []
        expected = []
        self.assertCountEqual(expected, findWords(board, words))

    def test_duplicates(self):
        board = [["a", "a"]]
        words = ["a"]
        self.assertCountEqual(["a"], findWords(board, words))
