"""
You are given two strings, pattern and value. The pattern string consists ONLY of the letters a and b, describing a pattern.
For example, catcatgocatgo matches the pattern aabab (cat is a, go is b). It also matches patterns like a, ab, and b.
Write a method to determine if value matches pattern.
------------------------
Dang, I'm a little tired. But I"m still gonna try this.

my first though is: what are the possible lengths of the real strings represented by a and b that would allow it
to fit the length of value.
let's say |a| is the length of the string represented by a (e.g. 3 if it ends up being cat).
in this case
3|a| + 2|b| = |v| where |v| is the length of value.
This sounds like an integer programming problem.
|a| and |b| have to be non-negative.
So I could end up trying all the possible sizes of a and b until I find one.
This would take me at most O(n) attempts. But then for each possible size, I'd have to construct a string
and compare it to the value string. So that would be O(n^2). Uh oh!!

Not sure I can beat that though. I think I'm going to have to try multiple values of a and b....and each "try" is going
to involve a string comparison which I can short circuit but I can't worst case lower bound lower than n (for a single check).
"""
from collections import Counter


def matches(pattern, value):
    pattern_char_counter = Counter(pattern)
    for a_length in range(len(value) + 1):
        b_length = (
            int(
                (len(value) - pattern_char_counter["a"] * a_length)
                / pattern_char_counter["b"]
            )
            if pattern_char_counter["b"] > 0
            else 0
        )

        total_a_len = pattern_char_counter["a"] * a_length
        total_b_len = pattern_char_counter["b"] * b_length
        if total_a_len + total_b_len == len(value):
            a_strings = set()
            b_strings = set()
            curr_value_idx = 0
            is_match = True
            for pattern_char in pattern:
                is_a = pattern_char == "a"
                curr_length = a_length if is_a else b_length
                set_to_which_to_add = a_strings if is_a else b_strings
                set_to_which_to_add.add(
                    value[curr_value_idx : curr_value_idx + curr_length]
                )
                if len(a_strings) > 1 or len(b_strings) > 1:
                    # the patterns were inconsistent
                    is_match = False
                    break
                curr_value_idx += curr_length
            if is_match:
                return True
    return False
