"""
Create a partition of a list of numbers such that the difference between them is minimized
# TODO: finish this! this doesn't work??

Naive Solution:
Try all possible ways of creating two partitions from a collection of elements. There are 2^n possibilities. Awful!

Are there any overlapping subproblems?
let's think about
[1, 5, 6, 12]

if it was just [1], then the best partition would be
[1], []

if it was [1, 5] then the best would be
[1], [5]

if it was [1, 5, 6] then the best would be
[1, 5], [6]

so how did we go from step 2 to step 3?
At every step, given some existing partition, and a new (larger) element, we have four options:
1. add the new element to left partition
2. add new element to right partition
3. move an element (TODO: which?) from left to right partition, add new element to left partition
4. move an element (TODO: which?) from right to left partition, add new element to right partition

what if we start with the largest element instead?
[12], []
[12], [6]
[12], [6, 5]
[12], [6, 5, 1]
boom! does this always work? idk. but we're gonna try it mate

Okay this does NOT work if nums can contain negative elements. So I'll assume it only works for positive.
TODO: why was this in dynamic_recursive??
"""


def min_partition(nums):
    desc_sorted_nums = sorted(nums, reverse=True)
    left = []
    right = []
    left_sum = 0
    right_sum = 0
    curr_diff = left_sum - right_sum
    for num in desc_sorted_nums:
        # left partition is larger than right
        if curr_diff > 0:
            right.append(num)
            right_sum += num
        else:
            left.append(num)
            left_sum += num
        curr_diff = left_sum - right_sum
    return left, right
