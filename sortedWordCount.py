from collections import Counter, defaultdict, deque
from sys import stdin
import re

WHITESPACE = re.compile("")
def removeWhitespace(s):
    # the last character is always a newline, so remove
    return re.sub("\s+", " ", s)[:-1]

def removePunctuation(s):
# TODO: refactor this
    res = re.sub("[^a-zA-Z\s]", "", s)
    return res

if __name__ == "__main__":
    c = Counter()
    for line in stdin:
        line = removeWhitespace(line)
        line = removePunctuation(line)
        line = line.lower()
        c.update(line.split(" "))

    # invert counter
    inv_c = defaultdict(lambda: list())
    for word, count in c.items():
        if word == "": continue
        inv_c[count].append(word)

    # iterate through the keys in descending order
    print_count = 0
    for count in sorted(inv_c.keys(), reverse=True):
        # sort the words in alphabetical order
        words_with_count = deque(sorted(inv_c[count]))

        while print_count < 10 and words_with_count:
            print(words_with_count.popleft() + " " + str(count))
            print_count += 1
