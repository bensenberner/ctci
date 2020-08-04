"""
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list. Your job is to implement the following functions:
The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

Example:

Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
Note: The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words. The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100. Please use double-quote instead of single-quote when you write test cases even for a character input. Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
----------
- What does "hot" mean? most frequent?
- however I store searches, I'm going to need some sort of counter in the TrieNodes


Initialization:
Create a Trie containing all of the historical searches.
TrieNode consists of:
char: str
is_leaf: bool
hot_degree: int
"""
from operator import itemgetter
from typing import Dict, List, Tuple


class TrieNode:
    START_SYMBOL = "^"

    def __init__(self, char, is_leaf, hot_degree):
        self._char = char
        self.is_leaf = is_leaf
        self.hot_degree = hot_degree
        self.children: Dict[str, TrieNode] = dict()

    @property
    def is_root_node(self):
        return self._char == self.START_SYMBOL

    @property
    def char(self):
        if self.is_root_node:
            raise ValueError("Cannot directly access root node")
        return self._char

    def __repr__(self):
        return f"<char:{self._char}|is_leaf:{self.is_leaf}|deg:{self.hot_degree}>"

    @classmethod
    def create_root(cls):
        return TrieNode(
            char=cls.START_SYMBOL, is_leaf=False, hot_degree=0
        )  # TODO: will this intro weirdness??

    def insert_char(self, char, degree=1):
        if char in self.children:
            new_node = self.children[char]
            new_node.hot_degree += degree
        else:
            new_node = TrieNode(char=char, is_leaf=False, hot_degree=degree)
            self.children[char] = new_node
        return new_node

    def insert_full_string_with_count(self, string, degree):
        """
        :param string: a complete search query. It is assumed that this would have
        ended with a '#' sign
        :param degree: hot degree from the historical data
        """
        curr_node = self
        for character in string[:-1]:
            curr_node = curr_node.insert_char(character, degree)
        last_char = string[-1]
        last_node = curr_node.insert_char(last_char, degree)
        last_node.is_leaf = True

    def get_top_three_degree_strings(self):
        all_strs_to_counts: List[Tuple[str, int]] = []
        curr_str_list = []
        stack = [self]

        def dfs():
            if not stack:
                return
            node = stack.pop()
            if not node.is_root_node:
                curr_str_list.append(node.char)
            if node.is_leaf:
                all_strs_to_counts.append(("".join(curr_str_list), node.hot_degree))
            for child in node.children.values():
                stack.append(child)
                dfs()
                curr_str_list.pop()

        dfs()
        all_strs_to_counts.sort(key=itemgetter(0))
        all_strs_to_counts.sort(key=itemgetter(1), reverse=True)
        return [s for s, count in all_strs_to_counts][:3]


class AutocompleteSystem:
    EOL_CHAR = "#"

    def __init__(self, sentences, counts):
        self.trie_root = TrieNode.create_root()
        self.query_node = self.trie_root
        self.previous_query_inputs = []

        for sentence, count in zip(sentences, counts):
            self.trie_root.insert_full_string_with_count(sentence, count)

    def get_autocomplete_results(self):
        autocomplete_suffixes = self.query_node.get_top_three_degree_strings()
        prefix = "".join(self.previous_query_inputs)
        return [prefix + suffix for suffix in autocomplete_suffixes]

    def input(self, char: str):
        if char == self.EOL_CHAR:
            self.query_node.is_leaf = True
            # reset things back to the beginning
            self.query_node = self.trie_root
            self.previous_query_inputs = []
            # TODO: what if I ended up searching an identical string as before?
            return []
        else:
            new_node = self.query_node.insert_char(char, 1)
            self.query_node = new_node
            results = self.get_autocomplete_results()
            self.previous_query_inputs.append(char)
            return results
