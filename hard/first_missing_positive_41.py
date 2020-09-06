from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    nums.append(0)
    for idx in range(len(nums)):
        while (
            0 <= nums[idx] < len(nums)
            and nums[idx] != idx  # when the number is set properly, escape
            and nums[idx] != nums[nums[idx]]  # escape the duplicate trap
        ):
            nums[nums[idx]], nums[idx] = nums[idx], nums[nums[idx]]
    for idx in range(len(nums)):
        if idx != nums[idx]:
            return idx
    return len(nums)
