"""
Given two arrays of integers, find a pair of values (one from each array) that you can swap to give the two arrays
the same sum.
-----------------
m = |arr1|
n = |arr2|

Okay we definitely gotta visit each element once since they're not sorted

Best Case:
time: O(m + n)

let's say we get sum(arr1) and sum(arr2). okay. then we find the difference.

arr1 = [4, 1, 2, 1, 1, 2]
arr2 = [3, 6, 3, 3]
sum(arr1) == 11
sum(arr2) == 15
so the difference is 4.

Hm.
the solution here was [1, 3] (1 came from the arr1 obviously)
so
1 + 3 = 4??
but it has to be such that the 3 came from the second list.

Okay so it seems like
1) find the sums
2) find the diff
3) hash all the items in the arr1 (or rather, whichever is the bigger list)
4) for element in arr2, if (diff - element) in first_set, return [diff - element, element]

okay but I think the 4 is throwing me off because 4 = 2*2 = 2+2. so that could've come from other places

arr1 = [1, 2, 5, 2, 9] = sum of 19
arr2 = [1, 7, 5, 7, 9] = sum of 29

actually need to look for (needle_element - sum_diff // 2) in haystack_arr
"""


def sum_swap(arr1, arr2):
    # first list should be smaller than larger list. better to iterate through a short list and do O(1) lookups
    if len(arr1) > len(arr2):
        return sum_swap(arr2, arr1)[::-1]
    sum_diff = sum(arr1) - sum(arr2)
    arr2_set = set(arr2)
    for arr1_element in arr1:
        possible_arr2_element = arr1_element - sum_diff // 2
        if possible_arr2_element in arr2_set:
            return [arr1_element, possible_arr2_element]
