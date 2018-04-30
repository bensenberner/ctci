from collections import Counter, defaultdict

a = ord("a")


class HashableCounter:
    def __init__(self, word):
        self.c = Counter(word)

    def __hash__(self):
        total = 0
        for char, count in self.c.items():
            # turn each count into base 26
            baseAlphabet = 26 ** (ord(char) - a)
            total += baseAlphabet * count
        return total

    def __eq__(self, other):
        return hash(self) == hash(other)


def group_by_anagram(words):
    d = defaultdict(lambda: list())
    for word in words:
        hashCounter = HashableCounter(word)
        d[hashCounter].append(word)

    # flatten the list of lists of grouped words
    return [word for group in d.values() for word in group]


if __name__ == "__main__":
    words = ["bat", "tag", "tab", "gank", "gat", "tba"]
    print(group_by_anagram(words))