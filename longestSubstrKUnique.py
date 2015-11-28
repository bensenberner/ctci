# finds the number of unique characters, calculates if the string
# has at most k unique characters
def charNum(char):
    return ord(char) - ord('a')

def kUniqueString(s, k):
    charArr = [0] * 26
    numUniq = 0
    maxStartIndex = 0
    maxLen = 0
    currStartIndex = 0
    currLen = 0
    for i in range(len(s)):
        if not charArr[charNum(s[i])]:
            numUniq += 1

        charArr[charNum(s[i])] += 1

        # if numUniq > k, move the currStartIndex forward until the number of
        # unique characters is under the limit
        while numUniq > k:
            charArr[charNum(s[currStartIndex])] -= 1
            if charArr[charNum(s[currStartIndex])] == 0:
                numUniq -= 1
            currStartIndex += 1
            currLen -= 1

        currLen = i - currStartIndex + 1
        if currLen > maxLen:
            maxStartIndex = currStartIndex
            maxLen = currLen

    return s[maxStartIndex:maxStartIndex + maxLen] if maxLen > 0 else ""

if __name__ == "__main__":
    string = "abjabbbakbabacccacbcbababddabadbadb"
    k = 3
    print(string)
    print(kUniqueString(string, k))
