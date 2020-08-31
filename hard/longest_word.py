"""
Given a list of words, find the longest word made of other words
-------

Let's say that there are n words and each one is on average m letters long.
I want to go through each one and see whether it is composed of another word.
I want to go through each word in the list. For each word, I immediately want to see if any other word is the prefix
of this word. If it is, then I want to see if the suffix of that word (as in, the current word without the prefix
that is a different word) itself contains a prefix that is another word.
I'll keep track how many letters are in my current traversal and will keep track of the max. Every time I hit a leaf
node within the trie, that's another potential word; I don't need to go all the way to the bottom.

TODO: what if there are overlapping prefixes??

If I added them all to a trie, that would take O(mn) time.
If I added them all to a set, that would also take O(mn) time.

"""
from functools import lru_cache
from typing import List, Dict, Iterable


class TrieNode:
    START_SYMBOL = "^"

    def __init__(self, string, is_leaf=False):
        self.string = string
        self.is_leaf = is_leaf
        self.children: Dict[str, TrieNode] = dict()

    def __repr__(self):
        return f"<{self.string}|leaf:{self.is_leaf}>"

    def get_or_create_child(self, char: str):
        if char in self.children:
            return self.children[char]
        else:
            string = (
                self.string + char if self.string is not self.START_SYMBOL else char
            )
            child_node = TrieNode(string=string)
            self.children[char] = child_node
            return child_node

    @classmethod
    def create_from_words(cls, words: Iterable[str]):
        root = TrieNode(string=cls.START_SYMBOL)
        for word in words:
            curr_node = root
            for char in word:
                curr_node = curr_node.get_or_create_child(char)
            curr_node.is_leaf = True
        return root

    @lru_cache
    def contains_prefix(self, prefix):
        curr = self
        for char in prefix:
            if curr.is_leaf:
                return True
            if char not in curr.children:
                return False
            curr = curr.children.get(char)
        return curr.is_leaf

    def get_all_prefix_words(self, string):
        result = []
        curr = self
        for idx, char in enumerate(string):
            if curr.is_leaf:
                result.append(curr.string)
            if char not in curr.children:
                break
            curr = curr.children.get(char)
        return result


def longest_word_trie(words: List[str]):
    word_set = set(words)
    trie_root = TrieNode.create_from_words(words)

    curr_word_list = []
    max_word_length = 0
    max_word = ""
    curr_word_length = 0

    stack = [trie_root]

    def dfs():
        curr_node = stack.pop()
        if curr_node.string is not curr_node.START_SYMBOL:
            curr_word_list.append(curr_node.string)
        if curr_node.is_leaf:
            print(curr_word_list)
        for child in curr_node.children.values():
            stack.append(child)
            dfs()
        curr_word_list.pop()

    dfs()


def longest_word(words):
    word_set = set(words)
    max_len_word = ""

    @lru_cache(maxsize=None)
    def is_composed_of_other_words(string, performed_partition):
        if string in word_set and performed_partition:
            return True
        for partition_idx in range(1, len(string)):
            left_word = string[:partition_idx]
            right_word = string[partition_idx:]
            found_match = is_composed_of_other_words(
                left_word, True
            ) and is_composed_of_other_words(right_word, True)
            if found_match:
                return True
        return False

    for word in words:
        if len(word) > len(max_len_word) and is_composed_of_other_words(
            word, performed_partition=False
        ):
            max_len_word = word
    return max_len_word
