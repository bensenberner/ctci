def compare_nums(num1, num2):
    if num1 == num2: return 0
    s1 = str(num1)
    s2 = str(num2)
    n1 = len(s1)
    n2 = len(s2)
    for e1, e2 in zip(s1, s2):
        if e1 > e2:
            return 1
        if e2 > e1:
            return -1
    if n1 > n2:
        return 1 if s1[n2] > s2[0] else -1
    else:
        return -1 if s2[n1] > s1[0] else 1

    return 1 if len(s1) < len(s2) else -1

def largestNumber(nums):
    nums.sort(compare_nums, reverse=True)
    return "".join([str(num) for num in nums])

print(largestNumber([12, 128]))
