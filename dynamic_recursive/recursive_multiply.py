"""
Write a recursive function to multiply two numbers without using the * operator.
You can use addition, subtraction, and bit shifting, but minimize the number needed
------------
Approach 1:
result = 0
for _ in range(n):
    result += m
where n is the smaller number.

That is O(n) runtime. Can we do better? Using bitshifting? Could make it O(log(n))?? how is this a recursive algorithm??
TODO:
"""


def xor(bool1, bool2):
    return bool1 != bool2


def recursive_multiply(num1, num2):
    is_positive = not xor(num1 < 0, num2 < 0)
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == 1:
        return (
            num2 if is_positive else -num2
        )  # could also treat this as (0 - num2) instead of (-1 * num2) since multiplication is banned
    if num2 == 1:
        return num1 if is_positive else -num1
    if num1 < num2:
        return recursive_multiply(num1, num2 >> 1) << 1
    else:
        return recursive_multiply(num1 >> 1, num2) << 1
