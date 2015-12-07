def compress(string):
    currCharCount = 1
    prevChar = string[0]
    newString = ""
    for char in string[1:]:
        if char != prevChar:
            newString += (prevChar + str(currCharCount))
            prevChar = char
            currCharCount = 1
        else:
            currCharCount += 1
    newString += (prevChar + str(currCharCount))
    print(newString)
    return newString if len(newString) < len(string) else string

print(compress("aabccccaaa"))
