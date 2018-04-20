from collections import Counter
def shortestSuperseq(short, long):
    longN = len(long)
    shortN = len(short)
    elementsFound = 0
    startIdx = minStart = minEnd = 0
    minLen = float("inf")
    counter = Counter()
    for endIdx in range(longN):
        currEle = long[endIdx]
        if counter[currEle] == 0 and currEle in short:
            elementsFound += 1
        counter[currEle] += 1
        if elementsFound < shortN:
            continue
        # move startIdx up as much as possible
        while True:
            startEle = long[startIdx]
            # should never be less than, but whatever
            if startEle in short and counter[startEle] <= 1:
                break
            counter[startEle] -= 1
            startIdx += 1
        currLen = endIdx - startIdx + 1
        if currLen < minLen:
            minLen, minStart, minEnd = currLen, startIdx, endIdx

    return long[minStart : minEnd + 1]


if __name__ == "__main__":
    short = {1, 5, 9}
    long = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    print(shortestSuperseq(short, long))