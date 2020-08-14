def maxPeak(stack):
    if not stack:
        return None
    maximum = stack._pop()
    tmpStack = [maximum]
    while stack:
        tmp = stack._pop()
        maximum = tmp if tmp > maximum else maximum
        tmpStack.append(tmp)
    while tmpStack:
        stack.append(tmpStack.pop())
    return maximum


stack = [43, 23, 1, 3, 31, 6, 2]
print(maxPeak(stack))
