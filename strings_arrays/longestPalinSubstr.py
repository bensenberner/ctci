def longestPalinSubstr(string):
    n = len(string)
    table = []
    for i in range(n):
        table.append([False] * n)

    # all substrings of length 1 are palindromes
    maxLength = 1
    for i in range(n):
        table[i][i] = True

    start = 0
    print(table)
    for i in range(1, n):
        if string[i-1] == string[i]:
            table[i-1][i] = True
            start = i-1
            maxLength = 2
    print(table)
    # check for lengths greater than 2. k is the length of the substr
    for k in range(3, n + 1):
        # fix the starting index for a given length
        for i in range(n-k+1):
            # get the ending index of a substring of length k that starts
            # at index i.
            j = i + k - 1

            # for a given substring string[i:j], check to make sure that
            # the string within that range is, itself, a palindrome, and then
            # simply check that the outermost indices (i and j) are the same,
            # which would make the entire string[i:j] a palindrome without checking
            # the whole string (since the whole string has already been checked

            if table[i+1][j-1] and string[i] == string[j]:
                table[i][j] = True
                if k > maxLength:
                    # all we need to know is where it starts and how long it is
                    start = i
                    maxLength = k

    return(string[start:maxLength])

print(longestPalinSubstr('aabbcb'))
