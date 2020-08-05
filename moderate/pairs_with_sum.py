"""
find all pairs of integers within an array which sum to a particular value
Brute force:
O(n^2) possible combinations
O(n) space to contain all the pairs

Approach 1:
1) sort the array
2) place indexes at both ends. sum up the indexes. if that sum is less than target, move the bottom index up
if the sum is greater than target, move the top index down. if they equal sum, add to the list, and move both closer to
each other (can't use the same indexes twice, even if they repeat??) TODO:
if the indexes ever equal each other or cross, break.

O(nlog(n)) possible combos
O(n) space to store all the pairs

Approach 2:
1) create a counter of all the numbers
2) iterate through the array, see if any number in the array + the current number = target number (excluding current number)
3) if so, add them to the list of results

Time complexity: O(n) (one pass to build the counter, then another pass through each element)
Space complexity: O(n) for the counter
"""
from collections import Counter


def find_pairs_with_sum_sorted(arr, target_sum):
    sorted_arr = sorted(arr)
    start_idx, end_idx = 0, len(arr) - 1
    pairs = []
    while start_idx < end_idx:
        start_element, end_element = sorted_arr[start_idx], sorted_arr[end_idx]
        curr_sum = start_element + end_element
        if curr_sum < target_sum:
            start_idx += 1
        elif curr_sum > target_sum:
            end_idx -= 1
        else:
            pairs.append((start_element, end_element))
            start_idx += 1
            end_idx -= 1
    return pairs


def find_pairs_with_sum(arr, target_sum):
    counter = Counter(arr)
    pairs = set()
    for num in arr:
        counter[num] -= 1
        other_num_to_sum_to_target = target_sum - num
        if counter[other_num_to_sum_to_target] >= 1:
            small, large = (
                (num, other_num_to_sum_to_target)
                if num < other_num_to_sum_to_target
                else (other_num_to_sum_to_target, num)
            )
            pairs.add((small, large))
        counter[num] += 1
    return list(pairs)
