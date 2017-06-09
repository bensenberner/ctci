import pprint

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    c = [[None for i in range(m+1)] for j in range(n+1)]
    b = [[None for i in range(m+1)] for j in range(n+1)]

    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(m+1):
        for j in range(n+1):
            if s1[i] == s2[j]:
                c[i][j] = c[i-1][j-1] + 1
                # diagonal
                b[i][j] = "d"

            elif c[i][j-1] > c[i-1][j]:
                c[i][j] = c[i][j-1]
                # left
                b[i][j] = "l"

            else:
                c[i][j] = c[i-1][j]
                # up
                b[i][j] = "u"

    return c, b

if __name__ == "__main__":
    s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
    s2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
    '''
    [
                s1
            [0, 0, 0 ...]
    s2      [0, 1, 1 ...]
            [0, 1, 0 ...]
            .
            .
            .
    ]
    '''
    pp = pprint.PrettyPrinter()
    c, b = lcs(s1, s2)
    # pp.pprint(c)
    # pp.pprint(b)
    print(c)
    print(b)
