def kUniqueLongestSubstring(string, k):
    currStartIndex = 0
    currLength = 0
    maxStartIndex = 0
    maxLength = 0

    d = {}
    uniqueCount = 0

    for i in range(len(string)):
        if string[i] not in d or d[string[i]] == 0:
            d[string[i]] = 1
            uniqueCount += 1

        else:
            d[string[i]] += 1

        currLength += 1

        while uniqueCount > k:
            d[string[currStartIndex]] -= 1
            if d[string[currStartIndex]] == 0:
                uniqueCount -= 1

            currStartIndex += 1
            currLength -= 1

        if currLength > maxLength:
            maxLength = currLength
            maxStartIndex = currStartIndex

    return string[maxStartIndex : maxStartIndex + maxLength]

s = 'abacababcababcbcacacacbacabcacbacbacbacbaba'
k = 2

print(kUniqueLongestSubstring(s, k))
