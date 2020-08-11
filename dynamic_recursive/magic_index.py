from typing import List


def magic_index(arr: List[int]):
    """
    A magic index in an array is an index such that A[i] = i. Given a sorted array of ints, find a magic index, if one exists,
    in an array.
    FOLLOW-UP:
        what if values are not distinct?
    -----------
    Approach 1:
        O(n) solution would just scan through the whole list and find it. Easy.
    Approach 2:
        O(log(n)) solution starts from the middle. Then what?
        let's say A[mid_idx] < mid_idx.  that means all indexes less than mid_idx are also lower than their indexes.
        we can eliminate all of them and move to the upper half.
        Vice versa for A[mid_idx] > mid_idx.
        Okay, that should find it.
        But what if there are repeated elements?
        should....be fine.....???
        [-1, 0, 2, 2, 2]
    """
    n = len(arr)
    low_idx, high_idx = 0, n - 1
    # TODO: +1 stuff!!
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        if arr[mid_idx] > mid_idx:
            high_idx = mid_idx - 1
        elif arr[mid_idx] < mid_idx:
            low_idx = mid_idx + 1
        else:
            return mid_idx
    return -1
