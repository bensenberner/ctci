"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
from typing import List


def jump(nums: List[int]) -> int:
    num_hops = 0
    curr_idx = 0
    last_idx = len(nums) - 1
    while curr_idx != last_idx:
        best_idx = curr_idx + 1
        best_val = nums[best_idx] + best_idx
        for next_idx in range(nums[curr_idx] + curr_idx, curr_idx, -1):
            if next_idx >= last_idx:
                best_idx = last_idx
                break
            if next_idx + nums[next_idx] > best_val:
                best_idx = next_idx
                best_val = next_idx + nums[next_idx]
        curr_idx = best_idx
        num_hops += 1
    return num_hops
