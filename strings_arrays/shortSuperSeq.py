def superSeq(str1, str2):
    dp = [[0 for x in range(len(str1) + 1)] for y in range(len(str2 + 1))]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if not i:
                dp[i][j] = j
            elif not j:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:

