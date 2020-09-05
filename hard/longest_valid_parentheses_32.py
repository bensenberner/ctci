from functools import lru_cache
from typing import NamedTuple, List


class Node(NamedTuple):
    curr_len: int
    max_len: int


def longestValidParentheses(s: str) -> int:
    """TODO: FIGURE THIS OUT??!!!"""
    stack: List[Node] = []
    max_len = 0
    curr_len = 0
    for idx in range(len(s)):
        if s[idx] == "(":
            stack.append(Node(curr_len, max_len))
        else:
            if not stack:
                curr_len = 0
                continue
            stack.pop()
            curr_len = curr_len + 2
            max_len = max(max_len, curr_len)
    return max_len


def longestValidParenthesesN2(s: str) -> int:
    """this is an n^2 solution, I can do better..."""

    def is_within_bounds(idx):
        return 0 <= idx < len(s)

    def are_paren_indexes(left_idx, right_idx):
        return s[left_idx] == "(" and s[right_idx] == ")"

    @lru_cache(maxsize=None)
    def is_valid(start_idx, inclusive_end_idx):
        if not is_within_bounds(start_idx) or not is_within_bounds(inclusive_end_idx):
            return False
        if inclusive_end_idx - start_idx < 1:
            return False
        if inclusive_end_idx - start_idx == 1:
            return are_paren_indexes(start_idx, inclusive_end_idx)
        for partition_idx in range(start_idx + 1, inclusive_end_idx + 1):
            if is_valid(start_idx, partition_idx - 1) and is_valid(
                partition_idx, inclusive_end_idx
            ):
                return True
        return (
            (
                are_paren_indexes(start_idx, inclusive_end_idx)
                and is_valid(start_idx + 1, inclusive_end_idx - 1)
            )
            or (
                are_paren_indexes(start_idx, start_idx + 1)
                and is_valid(start_idx + 2, inclusive_end_idx)
            )
            or (
                are_paren_indexes(inclusive_end_idx - 1, inclusive_end_idx)
                and is_valid(start_idx, inclusive_end_idx - 2)
            )
        )

    longest_valid_len = 0
    for begin_idx in range(len(s)):
        for end_idx in range(begin_idx + 1, len(s)):
            if not is_valid(begin_idx, end_idx):
                continue
            longest_valid_len = max(longest_valid_len, end_idx - begin_idx + 1)

    return longest_valid_len
