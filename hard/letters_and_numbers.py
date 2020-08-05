from typing import List


def find_largest_subarray_len_of_equal_alphanum(arr: List[str]):
    """
    Find length of the largest contiguous subarray that contains an equal amount of letters and numbers.
    :param arr:
    :return:
    """
    count_alpha = 0
    count_num = 0
    alpha_cumulative = []
    num_cumulative = []
    for e in arr:
        if e.isalpha():
            count_alpha += 1
        else:
            count_num += 1
        alpha_cumulative.append(count_alpha)
        num_cumulative.append(count_num)
    diffs = [alpha - num for alpha, num in zip(alpha_cumulative, num_cumulative)]
    max_len = 0
    seen_at = {}
    for idx, diff in enumerate(diffs):
        if diff not in seen_at:
            seen_at[diff] = idx
        else:
            max_len = max(max_len, idx - seen_at[diff])
    return max_len
