def findLongestPalindrome(string):
    longestOLP = ""
    longestELP = ""
    n = len(string)
    i = 0
    j = 1
    while i < n and j < n:
        oddLeft = i
        oddRight = i
        oddPalindrome = string[i]
        while (oddLeft > 0 and \
                oddRight < n and \
                string[oddLeft] == string[oddRight]):
                oddPalindrome = string[oddLeft : oddRight + 1]
                oddLeft -= 1
                oddRight += 1

        evenLeft = i-1
        evenRight = i
        evenPalindrome = ''
        while (evenLeft > 0 and \
                evenRight < n and \
                string[evenLeft] == string[evenRight]):

            evenPalindrome = string[evenLeft : evenRight + 1]
            evenLeft -= 1
            evenRight -= 1

        longestOLP = oddPalindrome if \
                len(oddPalindrome) > len(longestOLP) \
                else longestOLP
        longestELP = evenPalindrome if \
                len(evenPalindrome) > len(longestELP) \
                else longestELP

        i += 1
        j += 1

    return longestOLP if len(longestOLP) > len(longestELP) else longestELP

string = 'abcdbcdbacbadbcadabdcbddadbdabacbababacbab'
print(findLongestPalindrome(string))
