from pprint import PrettyPrinter

def matrixchainorder(p):
    # number of matrices
    # n = 6
    n = len(p) - 1
    m = [[None for i in range(n)] for j in range(n)]
    s = [[None for i in range(n)] for j in range(n - 1)]
    for i in range(n):
        m[i][i] = 0
    # l is chain length
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def printoptimalparens(s, i, j):
    if i == j:
        print("A%d" % i, end='')
    else:
        print("(", end='')
        printoptimalparens(s, i, s[i][j])
        printoptimalparens(s, s[i][j]+1, j)
        print(")", end='')

if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    #     0   1   2  3   4   5   6
    '''
    there are 6 matrices:
    30 x 35, 35 x 15, 15 x 5, 5 x 10, 10 x 20, 20 x 25
       0        1        2      3        4        5
                                i                 j
                                k        k
    '''
    m, s = matrixchainorder(p)
    pp = PrettyPrinter()
    pp.pprint(m)
    printoptimalparens(s, 0, 5)
