def check(string):
    s = sorted(string)
    hasMiddleChar = False
    currCharCount = 1
    prevChar = s[0]
    for char in s[1:]:
        if char != prevChar:
            if currCharCount % 2 == 1:
                if hasMiddleChar:
                    return False
                hasMiddleChar = True
            currCharCount = 1
            prevChar = char
        else:
            currCharCount += 1

    return False if currCharCount % 2 == 1 and hasMiddleChar else True

print(check('abbb'))
