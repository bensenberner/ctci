def SCS(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [['' for x in range(m + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i is 0:
                dp[i][j] = str2[:j]
            elif j is 0:
                dp[i][j] = str1[:i]

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]

            else:
                dp[i][j] = dp[i - 1][j] \
                        if len(dp[i-1][j]) < len(dp[i][j-1]) \
                        else dp[i][j-1]

    return dp[n][m]

def main():
    x = 'aggtab'
    y = 'gxtxayb'
    print(SCS(x, y))

main()
