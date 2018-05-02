from collections import Counter, defaultdict

a = ord("a")

"""
Given a list of words, group them such that anagrams are adjacent

My idea: for each word, create a counter representing the counts of the letters in the word.
Deterministically hash the counter so that it can serve as the key in a dict.
Build up a list of words that map to the same counter (no need to sort the words)
In the end, flatten out the list of lists of grouped words
"""
class HashableCounter:
    def __init__(self, word):
        self.c = Counter(word.lower())
        # cache the value
        self.hashval = None

    def __hash__(self):
        if self.hashval is not None:
            return self.hashval

        # initialize the hashval
        self.hashval = 0
        for char, count in self.c.items():
            # turn each count into base 26
            baseAlphabet = 26 ** (ord(char) - a)
            self.hashval += baseAlphabet * count
        return self.hashval

    def __eq__(self, other):
        return hash(self) == hash(other)


def group_by_anagram(words):
    d = defaultdict(lambda: list())
    for word in words:
        d[HashableCounter(word)].append(word)

    # flatten the list of lists of grouped words
    return [word for group in d.values() for word in group]


if __name__ == "__main__":
    words = ["bat", "tag", "tab", "gank", "gat", "tba", "ankg"]
    print(group_by_anagram(words))