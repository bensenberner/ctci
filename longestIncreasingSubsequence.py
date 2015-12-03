def lis(arr):
    n = len(arr)

    dp = [1]*n

    maximum = 0
    for i in range(1, n):
        for j in range(0, i):
            # first part sees if the current index is greater than the j
            # index, i.e. that the sequence is increasing up until i.

            # the second part sees if the LIS up until j is greater than
            # the LIS at i, because if it is, then dp[i] is now one more than
            # whatever the longest subsequence was before it... I think
            if arr[i] > arr[j] and dp[i] < (dp[j] + 1):
                dp[i] = dp[j] + 1
                maximum = max(maximum, dp[i])
    return maximum

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of LIS is " + str(lis(arr)))
