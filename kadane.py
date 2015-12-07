def main():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(findMaxContigSum(arr))

def findMaxContigSum(arr):
    maxSum = 0
    maxStartIndex = 0
    maxLen = 0
    currStartIndex = 0
    currLen = 0
    currSum = 0
    for i in range(len(arr)):
        currSum += arr[i]
        if currSum > 0:
            maxSum
        if currSum > maxSum:
            maxStartIndex = i
            maxSum = currSum
    return maxSum
main()
