from collections import Counter
from enum import Enum


class Paren(Enum):
    LEFT = "("
    RIGHT = ")"


def print_all_parens(n: int):
    curr_list = []
    counter = Counter()

    def _print():
        if counter[Paren.LEFT] == counter[Paren.RIGHT] == n:
            print("".join(curr_list))
            return
        if counter[Paren.LEFT] > n:
            return
        if counter[Paren.RIGHT] > counter[Paren.LEFT]:
            return
        for paren in [Paren.LEFT, Paren.RIGHT]:
            counter[paren] += 1
            curr_list.append(paren.value)
            _print()
            curr_list.pop()
            counter[paren] -= 1

    _print()
