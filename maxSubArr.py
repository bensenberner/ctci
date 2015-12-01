def findSubArr(arr):
    maxSoFar = a[0]
    maxStartIndex = 0
    maxLen = 1
    currMax = a[0]
    currStartIndex = 0
    currLen = 1
    for i in range(1, len(arr)):
        if currMax + arr[i] > arr[i]:
            currLen += 1
            currMax = currMax + arr[i]
        else:
            currStartIndex = i
            currLen = 1
            currMax = arr[i]

        if currMax > maxSoFar:
            maxSoFar = currMax
            maxStartIndex = currStartIndex
            maxLen = currLen
        # currMax = max(arr[i], currMax + arr[i])
        # maxSoFar = max(maxSoFar, currMax)

    return arr[maxStartIndex : maxStartIndex + maxLen]

a = [-2, -3, -7, -1, -2, -2, -5, -3]
print("Maximum sum in subarr " + str(a) + " is " + str(findSubArr(a)))
