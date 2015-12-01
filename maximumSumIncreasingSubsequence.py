def maxSumIncSubseq(arr, n):
    maximum = 0
    dp = [0] * n
    subSeqs = []

    # initialize the dp array with the values from the input array,
    # since every value can be thought of as an increasing subseq of
    # length 1
    for i in range(n):
        dp[i] = arr[i]

    for i in range(1, n):
        # find the maximum increasing subsequence up until that point
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]

    for i in range(n):
        if maximum < dp[i]:
            maximum = dp[i]

    return maximum
