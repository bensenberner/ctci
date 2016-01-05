def longestPalinSubstr(string):
    dp = [False for x in range(len(string))]

    for i in range(string):
        if i == 0:
            dp[i] = True
        elif i % 2 == 1:


