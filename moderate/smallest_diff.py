"""
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference.
Return the difference.

Let's say the arrays are differently sized, |m| > |n|.
Sorting is an O(nlog(n)) operation. Ideally, I would only sort the smaller array, if I'm doing any sorting at all.

Naive approach is, of course, O(mn), where I compare every element with every other element and keep track of the min.
Smarter approach would be to sort the smaller array in nlog(n) time, and then try to find each element of the larger array
within the smaller array. If you can find it, great! That's a difference of 0, as small as it gets.
Otherwise, you will wind up "between" two elements of the smaller array or off to the side of the smaller array. If that's the case,
then you look at the closest elements to this "gap" where the element from the larger array would be, and find the diffs.
This is a log(n) search, and you do it m times.
Thus, the runtime would be
O(nlog(n) [to sort smaller array] + mlog(n) [to search for every element of the larger array in the smaller array])
or O((n + m)log(n))
which is better than O(mn).

"""


def binary_search_return_low_if_not_found(haystack, needle):
    """
    :param haystack: array that is searched
    :param needle: number that is searched for
    :return: (is_present, idx)
        where is_present represents whether needle was actually
        in haystack. If it was, then idx is the real idx.
        Otherwise, idx is the idx right *below* where needle
        would be if it were in haystack.
    """
    low = 0
    high = len(haystack) - 1
    while low <= high:
        mid = (high + low) // 2
        if haystack[mid] < needle:
            low = mid + 1
        elif haystack[mid] > needle:
            high = mid - 1
        else:
            return True, mid
    # if the loop above was exited, that means that high < low
    # therefore, if x WAS in the list, it would be between index
    # high and high + 1
    return False, high


def find_smallest_diff(l1, l2):
    """
    this runs in O((m + n)log(n)) time, where n is the length of the
    smaller array
    """
    small, large = (l1, l2) if len(l1) < len(l2) else (l2, l1)
    small.sort()
    min_diff = float("inf")
    for num in large:
        is_present, idx = binary_search_return_low_if_not_found(small, num)
        if is_present:
            return 0
        if idx >= 0:
            min_diff = min(min_diff, abs(num - small[idx]))
        if idx < len(small) - 1:
            min_diff = min(min_diff, abs(num - small[idx + 1]))
    return min_diff
