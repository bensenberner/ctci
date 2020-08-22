import unittest

from hard.longest_word import longest_word


class Test(unittest.TestCase):
    def test(self):
        words = ["banana", "cat", "dog", "nana", "walk", "walker", "dogwalker"]
        self.assertEqual("dogwalker", longest_word(words))

    def test_no_word_works(self):
        words = ["cat", "dog", "hotdog"]
        self.assertEqual("", longest_word(words))


if __name__ == "__main__":
    unittest.main()
