from functools import lru_cache
from typing import List

from graphs_trees import TreeNode


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    n = len(nums)

    def _construct(start_idx, end_idx):
        if start_idx < 0 or start_idx >= end_idx or end_idx > n:
            return None
        max_idx = 0
        max_val = float("-inf")
        for idx in range(start_idx, end_idx):
            num = nums[idx]
            if num > max_val:
                max_val = num
                max_idx = idx
        return TreeNode(
            val=max_val,
            left=_construct(start_idx, max_idx),
            right=_construct(max_idx + 1, end_idx),
        )

    return _construct(0, n)
