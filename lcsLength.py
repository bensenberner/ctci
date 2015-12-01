def lcs(string1, string2, m, n):
    L = [[(0, '') for x in range(m+1)] for y in range(n+1)]
    print(L)
    result = ''
    for i in range(0, m):
        for j in range(0, n):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                print(L[i][j])
                L[i][j][0] = L[i-1][j-1][0] + 1
                L[i][j][1] += L[i-1][j-1][1]
                result = result if len(result) > len(L[i][j][1]) else L[i][j][1]
            else:
                L[i][j] = (0, '')
    return L
    # return L[m][n - 1]

string1 = 'AGGTAB'
string2 = 'GXTXAYB'
m = len(string1)
n = len(string2)
print(lcs(string1, string2, m, n))
