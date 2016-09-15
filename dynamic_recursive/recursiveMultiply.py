# seems more like this should be done iteratively

def mult(num1, num2):
    isPositive = True
    if (num1 == 0 or num2 == 0):
        return 0

    if ((num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0)):
        isPositive = False

    n1 = abs(num1)
    n2 = abs(num2)
    i, j = (n1, n2) if n1 < n2 else (n2, n1)

    sum = 0
    while i > 0:
        sum += j
        i -= 1


    return sum if isPositive else 0 - sum

def recursiveMult(num1, num2):
    n1 = abs(num1)
    n2 = abs(num2)

    isPositive = False if ((num1 > 0 and num2 < 0) or \
                            (num1 < 0 and num2 > 0)) else True

    num = recurse(n1, n2)
    return num if isPositive else 0 - num

def recurse(num1, num2):
    if num2 == 0:
        return 0
    if num2 == 1:
        return num1
    return recurse(num1, num2 - 1) + num1

print(recursiveMult(-10, -11))
