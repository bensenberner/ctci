"""
Implement subtract, multiply, divide using only add
"""


def negate(num):
    negated_num = 0
    opposite_sign = 1 if num < 0 else -1
    while num != 0:
        num += opposite_sign
        negated_num += opposite_sign
    return negated_num


def subtract(a, b):
    return a + negate(b)


def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    is_negative = False
    if a < 0:
        a = negate(a)
        is_negative = not is_negative
    if b < 0:
        b = negate(b)
        is_negative = not is_negative
    result = 0
    for _ in range(b):
        result += a
    return negate(result) if is_negative else result


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    is_negative = False
    if a < 0:
        a = negate(a)
        is_negative = not is_negative
    if b < 0:
        b = negate(b)
        is_negative = not is_negative
    multiplier = 1
    while a >= b * multiplier:
        multiplier += 1
    return negate(multiplier - 1) if is_negative else (multiplier - 1)
