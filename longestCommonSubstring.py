def LCSubStr(str1, str2):
    dp = [[0]*(len(str1) + 2)] * (len(str2) + 2)
    res = 0
    for i in range(0, len(str1) - 1):
        for j in range(0, len(str2) - 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    return res

print(LCSubStr('abcdef', 'cde'))
