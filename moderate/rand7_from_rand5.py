"""
Given a method that generates a number between 0 and 4 (inclusive) write a method that generates
a random number between 0 and 6 (inclusive)
------------
"""
import random


def rand5():
    return random.randint(0, 4)


included_rolls = [(x, y) for x in range(0, 5) for y in range(0, 5)][:21]
rolls_to_7 = {roll: idx % 7 for idx, roll in enumerate(included_rolls)}


def rand7():
    # there are 25 combinations of rolls, but 21 is divisible by 25
    while True:
        rolls = rand5(), rand5()
        if rolls not in included_rolls:
            continue
        return rolls_to_7[rolls]
