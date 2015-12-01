def main():
    arr = [1, -6, 3, -1, 4, 2, -3, 2]
    print(findMaxContigSum(arr))

def findMaxContigSum(arr):
    maxSum = 0
    maxStartIndex = 0
    maxLen = 0
    currStartIndex = 0
    currLen = 0
    currSum = 0
    for i in range(arr):
        currSum += arr[i]
        if currSum > 0:
            maxSum
        if currSum > maxSum:
            maxStartIndex = i
            maxSum = currSum
main()
