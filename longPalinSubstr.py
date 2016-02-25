def longestPalinSubstr(string):
    palindrome = ''
    n = len(string)
    for i in range(n):
        j = k = i

        # find longest odd length palindrome
        while j >= 0 and k <= n-1 and string[j] == string[k]:
            if len(string[j:k+1]) > len(palindrome):
                palindrome = string[j:k+1]
            j -= 1
            k += 1

        # find longest ELP
        j = i
        k = i + 1
        while j >= 0 and k <= n-1 and string[j] == string[k]:
            if len(string[j:k+1]) > len(palindrome):
                palindrome = string[j:k+1]
            j -= 1
            k += 1

    return palindrome

print(longestPalinSubstr('aaaabbaaaababababaaaabaaaaabaabaaabaabbabbabaaa'))
