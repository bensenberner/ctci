def findSubArr(arr):
    maxSoFar = a[0]
    currMax = a[0]
    for i in range(1, len(arr)):
        currMax = max(arr[i], currMax + arr[i])
        maxSoFar = max(maxSoFar, currMax)
        #maxEndingHere = maxEndingHere + arr[i]
        #if maxEndingHere < 0:
        #    maxEndingHere = 0
        #    maxArr = []

        #if maxSoFar < maxEndingHere:
        #    maxSoFar = maxEndingHere
        #    maxArr.append(arr[i])

    return maxSoFar

a = [2, 3, -7, -1, 2, 2, 5, 3]
print(findSubArr(a))
