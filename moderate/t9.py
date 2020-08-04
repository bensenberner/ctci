"""
On old cellphones, users typed numbers and they corresponded to letters.
Return a list of matching words, given a sequence of digits.
You are provided a list of valid words in whatever datastructure you like.

e.g.
input: 8733
output: tree, used
---------------------

dictionary will be represented by a Trie
"""
from __future__ import annotations

from typing import List


class TrieNode:
    START_SYMBOL = "^"

    def __init__(self, val, is_leaf=False):
        self.val = val
        self.is_leaf = is_leaf
        self.children = dict()

    def __repr__(self):
        return f"<val:{self.val} | is_leaf:{self.is_leaf} | children:{list(self.children.keys())}>"

    @classmethod
    def create_root(cls):
        return TrieNode(val=cls.START_SYMBOL)

    @classmethod
    def build_from_words(cls, words: List[str]):
        root = cls.create_root()
        for word in words:
            root.insert(word)
        return root

    def add_child(self, node: TrieNode):
        self.children[node.val] = node

    def insert(self, word):
        curr_node = self
        for char in word[:-1]:
            if char in curr_node.children:
                new_node = curr_node.children[char]
            else:
                new_node = TrieNode(val=char, is_leaf=False)
                curr_node.add_child(new_node)
            curr_node = new_node
        leaf_node = TrieNode(val=word[-1], is_leaf=True)
        curr_node.add_child(leaf_node)

    def contains(self, word):
        curr_node = self
        for char in word:
            if char not in curr_node.children.keys():
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_leaf


class T9:
    cell_phone_map = {
        "2": {"a", "b", "c"},
        "3": {"d", "e", "f"},
        "4": {"g", "h", "i"},
        "5": {"j", "k", "l"},
        "6": {"m", "n", "o"},
        "7": {"p", "q", "r", "s"},
        "8": {"t", "u", "v"},
        "9": {"w", "x", "y", "z"},
    }

    @classmethod
    def find_all_words_spellable_from(cls, t9_input: str, possible_words: List[str]):
        result = []
        curr_word = []

        def build_result(node, curr_digits_idx):
            if curr_digits_idx == len(t9_input):
                if node.is_leaf:
                    result.append("".join(curr_word))
                curr_word.pop()
                return
            for new_letter in cls.cell_phone_map[t9_input[curr_digits_idx]]:
                if new_letter in node.children:
                    curr_word.append(new_letter)
                    build_result(node.children[new_letter], curr_digits_idx + 1)
            if curr_word:
                curr_word.pop()

        build_result(TrieNode.build_from_words(possible_words), 0)
        return result
