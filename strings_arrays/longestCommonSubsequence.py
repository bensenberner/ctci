def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [['' for x in range(n + 1)] for y in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = ''

            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + str1[i-1]

            else:
                dp[i][j] = dp[i-1][j] \
                        if len(dp[i-1][j]) > len(dp[i][j-1]) \
                        else dp[i][j-1]

    return dp[m][n]

def main():
    x = 'aggtab'
    y = 'gxtxayb'
    print(LCS(x, y))

main()
