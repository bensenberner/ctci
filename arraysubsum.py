def subarraymaxsum(arr):
    n = len(arr)
    if n == 0: return 0
    currSum = arr[0]
    maxNum = arr[0]
    maxSum = currSum
    for idx in range(1, n):
        e = arr[idx]
        maxNum = max(maxNum, e)
        currSum += e
        if currSum < 0:
            currSum = 0
        maxSum = max(maxSum, currSum)

    if maxNum < 0: return maxNum
    return maxSum

arr = [-4, -420, -6900]
print(subarraymaxsum(arr))
