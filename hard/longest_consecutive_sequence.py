"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
from collections import defaultdict
from typing import List


def longest_consecutive_seq(nums: List[int]) -> int:
    seen_items = set()
    graph = defaultdict(lambda: list())
    for num in nums:
        seen_items.add(num)
        if num - 1 in seen_items:
            graph[num - 1].append(num)
            graph[num].append(num - 1)
        if num + 1 in seen_items:
            graph[num + 1].append(num)
            graph[num].append(num + 1)
    visited_items = set()
    longest_len = 0
    for key in graph.keys():
        if key in visited_items:
            continue
        curr_len = 0
        stack = [key]
        while stack:
            curr_num = stack.pop()
            curr_len += 1
            visited_items.add(curr_num)
            for neighbor_nums in graph[curr_num]:
                if neighbor_nums in visited_items:
                    continue
                stack.append(neighbor_nums)
        longest_len = max(longest_len, curr_len)
    return longest_len
