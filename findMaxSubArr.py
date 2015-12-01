def main():
    str1 = "devcatoocco"
    str2 = "qacatoc"
    print(findMaxSubArrLen(str1, str2))

def findMaxSubArrLen(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n)] for y in range(m)]

    maxlen = 0
    maxI = 0
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + dp[i-1][j-1]
            if maxlen < dp[i][j]:
                maxI = i
                maxlen = dp[i][j]

    return(str1[maxI - maxlen + 1:maxI + 1])

main()
