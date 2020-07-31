"""
Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, the entire array would be sorted.
minimize n - m (find the shortest such sequence). See test case for example
"""
from collections import deque
from typing import Tuple, List


def is_sorted(arr):
    """
    O(n) check to see if a list is sorted
    """
    if len(arr) <= 1:
        return True
    prev_element = arr[0]
    for curr_element in arr[1:]:
        if curr_element < prev_element:
            return False
        prev_element = curr_element
    return True


def find_sub_sort_indexes(arr: List[int]) -> Tuple[int, int]:
    if is_sorted(arr):
        return 0, 0
    curr_max = float("-inf")
    maxes = deque()
    for num in arr:
        curr_max = max(curr_max, num)
        maxes.append(curr_max)

    curr_min = float("inf")
    mins = deque()
    for num in arr[::-1]:
        curr_min = min(curr_min, num)
        mins.appendleft(curr_min)

    low = 0
    for idx in range(len(arr)):
        if maxes[idx] != mins[idx]:
            break
        low = idx

    high = len(arr) - 1
    for rev_idx in range(len(arr) - 1, -1, -1):
        if maxes[rev_idx] != mins[rev_idx]:
            break
        high = rev_idx
    return low, high
