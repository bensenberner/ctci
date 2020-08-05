import copy
import math
from random import random
from typing import List

"""
Shuffle a deck of cards such that each of the 52! permutations are equally likely.
Assume you have a random number generator which is perfect.
------------
Approach 1:
I remember hearing this one before. Just go through the array and swap every number with another random index. It's okay if you pick the same index twice.
O(n) time, O(1) space
"""


def randint(n):
    return math.floor(random() * n)


def shuffle(cards: List[int]):
    for idx in range(len(cards)):
        new_idx = randint(len(cards))
        cards[idx], cards[new_idx] = cards[new_idx], cards[idx]
