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

# print(LCSubStr('abcdef', 'cde'))

def LCSubNaive(str1, str2):
    maxStr = ''
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                commonStr = findCommonStringAtIndex(str1, str2, i, j)
                if len(commonStr) > len(maxStr):
                    maxStr = commonStr
    return maxStr

def findCommonStringAtIndex(str1, str2, i, j):
    commonStr = ''
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            break
        commonStr += str1[i]
        i += 1
        j += 1

    return commonStr

print(LCSubNaive('aasdoijfasdklfajslkdfjaosidjfasiopefjaposijfalksdjfapsoiefjaslkdjfasefkljas;elfkjasl;efkajsdfjasioefjasiejfalksdjfaksjeflasekjfalskjfalksejfkasjdflaksjdflaksjefioajseflkajsbcdefg', 'lmncdefopgabaiosdjfoaisdlaksjdfklajsdklfjasdfasdfasiunfapseifnasoidfasdfjaoisejfpaoisejfpoisaejfapiejfapoisjefasoiefjalksdjfaoisejfj'))
