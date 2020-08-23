"""
Given a string containing no spaces, just a series of characters, and a set of words, find a way to unconcatenate the
input string such that it is composed of words from the dictionary and the number of "unrecognized" characters (that
don't show up in the dictionary) are minimized
------------------
Approach 1:
Recursive algorithm with memoization.
Start at the beginning of the string. Check to see if the beginning of the string is in the dictionary. If it isn't,
then "extra_characters" = number of characters in the beginning of the string. Then call the algorithm on the rest of
the string. Keep track of how many characters it ultimately doesn't account for, and return a tuple of both of them,
the best string and the number of unaccounted for characters in that string.

Runtime: O(n^2)
Space complexity: O(n) calls in the call stack...O(n^2)
"""
from functools import lru_cache
from typing import Tuple, List, Union

words = {"looked", "just", "like", "her", "brother"}


def respace(string):
    n = len(string)

    @lru_cache(maxsize=None)
    def _respace(start_idx) -> Tuple[List[str], Union[int, float]]:
        full_string = string[start_idx:]
        best_respacing = [full_string]
        if full_string in words:
            # no need to split, the whole word is recognized!
            return best_respacing, 0
        min_num_unrecog_chars = n - start_idx
        for prefix_end_idx in range(start_idx + 1, n):
            prefix = string[start_idx:prefix_end_idx]
            num_unrecog_chars = 0 if prefix in words else len(prefix)
            best_suffix, best_suffix_min_chars = _respace(prefix_end_idx)
            # <= ensures that, within a range of characters that are not recognized, we do not split it up
            if num_unrecog_chars + best_suffix_min_chars <= min_num_unrecog_chars:
                min_num_unrecog_chars = num_unrecog_chars + best_suffix_min_chars
                best_respacing = [prefix] + best_suffix
        return best_respacing, min_num_unrecog_chars

    best_respace, _ = _respace(0)
    return best_respace
