"""
approach 1:
create a counter for num elements from the first seq.
start extending the end index all the way.
as soon as you have at least one element from all four counts, then record that as the longest seq
then start shrinking it until you one of the counts goes to 0
then expand again.
Do this until you get to the end.
"""


def shortest_supersequence(distinct_nums, big_nums):
    counter = {distinct_num: 0 for distinct_num in distinct_nums}
    big_len = len(big_nums)
    num_elements_in_range = 0
    start_idx, end_idx = 0, 0
    min_range_len = float("inf")
    best_low_idx, best_high_idx = None, None
    while end_idx < big_len:
        while num_elements_in_range < len(distinct_nums) and end_idx < big_len:
            end_num = big_nums[end_idx]
            if end_num in counter:
                if counter[end_num] == 0:
                    num_elements_in_range += 1
                counter[end_num] += 1
            end_idx += 1

        # if we've reached this point then our current range should be good. but one quick check for bad inputs cant hurt
        while num_elements_in_range == len(distinct_nums) and start_idx <= end_idx:
            range_len = end_idx - start_idx
            if range_len < min_range_len:
                min_range_len = range_len
                best_low_idx, best_high_idx = (
                    start_idx,
                    end_idx - 1,  # it is too large from before
                )
            start_num = big_nums[start_idx]
            if start_num in counter:
                counter[start_num] -= 1
                if counter[start_num] == 0:
                    num_elements_in_range -= 1
            start_idx += 1

    return best_low_idx, best_high_idx
