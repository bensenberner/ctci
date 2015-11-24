def longestValid(string):
    stack = []
    stack.append(-1)
    result = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) != 0:
                result = max(result, i - stack[-1])
            else:
                stack.append(i)
    return result

print(longestValid(')))((()())('))
