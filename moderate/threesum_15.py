from collections import Counter
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    counter = Counter(nums)
    result = set()
    curr_attempt = []
    curr_sum = 0
    sorted_nums = sorted(nums)

    def backtrack(idx):
        nonlocal curr_sum
        if curr_sum > 0:
            return
        if len(curr_attempt) == 2:
            if counter[-curr_sum] > 0 and -curr_sum >= curr_attempt[-1]:
                result.add(tuple(curr_attempt + [-curr_sum]))
            return
        for new_idx in range(idx, len(sorted_nums)):
            curr_attempt.append(sorted_nums[new_idx])
            counter[sorted_nums[new_idx]] -= 1
            curr_sum += sorted_nums[new_idx]

            backtrack(new_idx + 1)

            curr_sum -= sorted_nums[new_idx]
            counter[sorted_nums[new_idx]] += 1
            curr_attempt.pop()

    backtrack(0)
    return [list(e) for e in result]
