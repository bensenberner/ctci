from typing import List

from hard.shuffle import shuffle

"""
Pick m elements from an array of length n with equal probability of each of the m elements.

Approach 1:
create a list of n indexes, shuffle them randomly, pick the first m
Runtime: O(n)
Space: O(n) to store all the indexes

m <= n, can we do something in O(m)?

Approach 2:
Randomly pick numbers that are in range(n). Keep track of elements you've already chosen so that you don't repick.
If you pick an element twice, then keep trying until you pick a new one.
Runtime O(nondeterministic)
Space: O(m) (only have to remember up to m indexes you've already picked

That's no good!

Approach 3:
Shuffle the input list in place up til index m
keep track of all the swaps you've made
create a set of the first m elements
then undo all the swaps

Runtime: O(m) to do the swaps and then undo them
Space: O(m) to remember all the swaps you did

if we don't bother undoing the swaps then we can do it in 
O(m) runtime and O(1) space
"""


def random_set(arr: List[int], m: int):
    if m > len(arr):
        raise AssertionError(
            f"Cannot pick {m} elements from an array of size {len(arr)}"
        )
    indexes = list(range(len(arr)))
    shuffle(indexes)
    return {arr[idx] for idx in indexes[:m]}
