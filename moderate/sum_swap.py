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
3) hash all the items in the arr1 (TODO: actually bigger list), call that first_set
4) for element in arr2, if (diff - element) in first_set, return [diff - element, element]

okay but I think the 4 is throwing me off because 4 = 2*2 = 2+2. so that could've come from other places

arr1 = [1, 2, 5, 2, 9] = sum of 19
arr2 = [1, 7, 5, 7, 9] = sum of 29
"""


def sum_swap(arr1, arr2):
    arr_1_is_smaller = len(arr1) < len(arr2)
    small_arr, large_arr = (arr1, arr2) if arr_1_is_smaller else (arr2, arr1)
    sum_diff = sum(small_arr) - sum(large_arr)
    # better to iterate through a short list and do O(1) lookups
    large_set = set(large_arr)
    for small_arr_element in small_arr:
        possible_large_arr_element = small_arr_element - sum_diff // 2
        if possible_large_arr_element in large_set:
            return (
                [small_arr_element, possible_large_arr_element]
                if arr_1_is_smaller
                else [possible_large_arr_element, small_arr_element]
            )
