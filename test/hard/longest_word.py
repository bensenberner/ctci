import unittest

from hard.longest_word import longest_word, TrieNode


class Test(unittest.TestCase):
    def test(self):
        words = ["banana", "cat", "dog", "nana", "walk", "walker", "dogwalker"]
        self.assertEqual("dogwalker", longest_word(words))

    def test_no_word_works(self):
        words = ["cat", "dog", "hotdog"]
        self.assertEqual("", longest_word(words))


class TestTrie(unittest.TestCase):
    def test(self):
        trie = TrieNode.create_from_words(["cat", "cats", "and", "sand", "dog"])
        self.assertCountEqual(["cat", "cats"], trie.get_all_prefix_words("catsand"))
