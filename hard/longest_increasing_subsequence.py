from collections import deque
from typing import List, NamedTuple, Optional


class SubSeq(NamedTuple):
    element_at_end: int
    prev_idx: Optional[int]
    seq_len: int


def longest_increasing_subsequence_len(arr: List[int]):
    n = len(arr)
    if n == 0:
        return []
    longest_subseq_til = [SubSeq(element_at_end=arr[0], prev_idx=None, seq_len=1)]

    for idx in range(1, n):
        curr_val = arr[idx]
        # go back through all the subseqs
        idx_of_max_prev_subseq = None
        longest_prev_subseq_len = 0
        for rev_idx in range(idx - 1, -1, -1):
            rev_val = arr[rev_idx]
            if (
                rev_val < curr_val
                and longest_prev_subseq_len < longest_subseq_til[rev_idx].seq_len
            ):
                idx_of_max_prev_subseq = rev_idx
                longest_prev_subseq_len = longest_subseq_til[rev_idx].seq_len
        longest_subseq_til.append(
            SubSeq(
                element_at_end=curr_val,
                prev_idx=idx_of_max_prev_subseq,
                seq_len=longest_prev_subseq_len + 1,
            )
        )
    arr = deque()
    curr_subseq_node = longest_subseq_til[-1]
    while curr_subseq_node.prev_idx is not None:
        arr.appendleft(curr_subseq_node.element_at_end)
        curr_subseq_node = longest_subseq_til[curr_subseq_node.prev_idx]
    arr.appendleft(curr_subseq_node.element_at_end)
    return list(arr)
