"""
Given an array of integers (both positive and negative), find the continguous sequence with the largest sum.
Return the sum.
--------------
how many contiguous sequences are there?
there are
n of length 1
n-1 of length 2
...
1 of length n

That means that there are n^2 sequences. but how long are they? let's say they're (worst case) n long.
That means to *compute the sum* of every sequence would be O(n^3).
That's no good! We can definitely cache results from earlier lists.

Approach 1:
Go through every partition in the list (left and right split). For each partition, find the max of each recurseively.
Add up.
Do some sorta caching.
Runtime: O(n^2), each subset
Approach 2:

"""
from functools import lru_cache
from typing import List


def contig_seq_sum(arr: List[int]):
    # TODO: this is O(n^3)
    # goes through every sequence, which is O(n^2)
    @lru_cache(maxsize=None)
    def _contig_seq_sum(start_idx, exclusive_end_idx):
        if start_idx + 1 == exclusive_end_idx:
            return arr[start_idx]
        max_seq_sum = sum(
            arr[start_idx:exclusive_end_idx]  # O(n) operation! we should cache this
        )
        for split_idx in range(start_idx + 1, exclusive_end_idx):
            max_seq_sum = max(
                [
                    max_seq_sum,
                    _contig_seq_sum(start_idx, split_idx),
                    _contig_seq_sum(split_idx, exclusive_end_idx),
                ]
            )
        return max_seq_sum

    return _contig_seq_sum(0, len(arr))
