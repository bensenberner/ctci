"""
Another year, another coin problem.
Given a cash register containing only quarters, dimes, and pennies,
Come up with a way to make change for any amount of cents that *minimizes the number of coins*
Return the minimum number of coins that adds up to some amount `n`.

e.g.
31 -> 3 dimes, 1 penny
---------------
Approach 1: Greedy
This will not work. If I start out by using the largest denomination first, and then the smaller ones,
then 31 cents would be 1 quarter and 6 pennies which is 7 total coins, GREATER than 3 dimes and 1 penny.

Approach 2: Dynamic programming:
Create an array that keeps track of the minimum number of coins necessary to add up to any amount, from 0-n.
Build it up in a bottom-first manner.
"""


def min_num_coins_to_make_change_for(n: int):
    """
    :param n: amount in cents to make change
    :return: min number of coins needed to make change
    """
    memo = [None for _ in range(n + 1)]  # need to include making 0 change
    denoms = [25, 10, 1]
    for denom in denoms:
        if denom < len(memo):
            memo[denom] = 1  # only one way to make

    def make_change_top_down(amount):
        if amount <= 0:
            raise ValueError(f"Cannot make change for {amount} cents")
        if memo[amount] is not None:
            return memo[amount]
        min_coins_needed = float("inf")
        for denom in denoms:
            if amount - denom > 0:
                min_coins_needed = min(
                    min_coins_needed, make_change_top_down(amount - denom) + 1
                )
        memo[amount] = min_coins_needed
        return min_coins_needed

    def _make_change_bottom_up(amount):
        for sub_amount in range(1, len(memo)):
            if memo[sub_amount] is not None:
                continue
            min_num_coins_needed = float("inf")
            for denom in denoms:
                if sub_amount - denom > 0:
                    min_num_coins_needed = min(
                        min_num_coins_needed, memo[sub_amount - denom] + 1
                    )
            memo[sub_amount] = min_num_coins_needed
        return memo[amount]

    return make_change_top_down(n)
