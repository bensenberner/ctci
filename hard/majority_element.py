"""
a majority element makes up more than half the items in an array. given a positive integers array, find the majority
element. if there is no majority element, return -1. do this in O(N) time and O(1) space.
---------------
with o(n) space, I could of course first create a counter, and then go through the counter and see which element
had the max occurrences, and then check if max occurrences is greater than n/2. But I can't use a counter.

all of them are positive. does that help?
what if I multiplied them all together. what could I do with that? I could go through and divide by each ...but no..
then I'd have to associate each element with the number of times it divided the big number...that's just a counter

another brute force approach:
go through each element, compare it to every other element, count the number of times it matches (or doesnt).
if "doesnt" ever goes above n/2, break. if matches ever goes above n/2, return True.
O(n^2) time, O(1) space.

okay. it has to appear MORE than half the time.
so it can't be alternating like [1, 9, 2, 9, 3, 9]. 9 is NOT the majority. it needs to take up 4 spots in a len(3) array.
OKAY.
"""
from collections import Counter


def majority_element(arr):
    shmuh = Counter()

    def _majority_of_subarray_splits(start_idx, exclusive_end_idx):
        shmuh[(start_idx, exclusive_end_idx)] += 1
        if start_idx + 1 == exclusive_end_idx:
            return arr[start_idx]
        mid_idx = (start_idx + exclusive_end_idx) // 2
        # TODO: make sure indexes are correct
        left_maj = _majority_of_subarray_splits(start_idx, mid_idx)
        right_maj = _majority_of_subarray_splits(mid_idx, exclusive_end_idx)
        len_left_half = mid_idx - start_idx
        len_right_half = exclusive_end_idx - mid_idx
        # TODO: one of these won't ever be called
        if len_left_half < len_right_half:
            return right_maj
        else:
            if left_maj == right_maj:
                return left_maj
            else:
                return -1

    def _majority_of_subarray_iterate():
        """
        [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]

        :return:
        """
        curr_idx = 0
        curr_arr_len = 1
        curr_mode_element = arr[curr_idx]
        curr_element_count = 1

        curr_idx += 1
        while curr_idx < len(arr):
            curr_element = arr[curr_idx]
            if curr_element != curr_mode_element:
                # TODO:
                pass
            else:
                pass
        return curr_mode_element

    return _majority_of_subarray_iterate()
