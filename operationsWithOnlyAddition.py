def multiply(num1, num2):
    bignum, smallnum = (num1, num2) if num1 > num2 else (num2, num1)
    res = 0
    for i in range(smallnum):
        res += bignum
    return res


def subtract(num1, num2):
    res = 0
    if num1 > num2:
        bignum, smallnum = num1, num2
        isNegative = False
    elif num2 > num1:
        bignum, smallnum = num2, num1
        isNegative = True
    else:
        return 0

    # could speed this up logarithmically
    for i in range(smallnum, bignum):
        res += 1
    return res


def divide(num1, num2):
    # assume that num1 > num2 and that num1 % num2 == 0.
    # what if they're not?
    res = 0
    while num1 > num2:
        num1 = subtract(num1, num2)
    return res
