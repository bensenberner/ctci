import pprint as pp
def minCuts(string):
    n = len(string)
    isPalindrome = [[False for x in range(n)] for y in range(n)]
    minCuts = [[float('inf') for x in range(n)] for y in range(n)]
    cutPositions = [False for x in range(n-1)]

    # initialize that every substring of length 1 is a palindrome. Palindromes
    # require 0 cuts to become palindromes.
    for i in range(n):
        isPalindrome[i][i] = True
        minCuts[i][i] = 0

    for length in range(2, n+1):
        for startIndex in range(n - length + 1):
            endIndex = startIndex + length - 1

            # a base case, this sets the tables for the smallest even length
            # palindromes
            if length == 2:
                if string[startIndex] == string[endIndex]:
                    isPalindrome[startIndex][endIndex] = True
                    minCuts[startIndex][endIndex] = 0
                else:
                    minCuts[startIndex][endIndex] = 1
                    cutPositions[startIndex]
            else:

                # first check if the current substring is a palindrome
                if string[startIndex] is string[endIndex] \
                    and isPalindrome[startIndex + 1][endIndex - 1]:
                        isPalindrome[startIndex][endIndex] = True
                        minCuts[startIndex][endIndex] = 0
                        for i in range(startIndex, endIndex):
                            cutPositions[i] = False
                else:
                    splitDecision = 0
                    for splitIndex in range(startIndex, endIndex):
                        # add 1 because we are joining two substrings together
                        cuts = 1 + minCuts[startIndex][splitIndex] + \
                                minCuts[splitIndex + 1][endIndex]
                        # minCuts at this position will eventually be the minimum
                        # for all possible cuts within itself
                        if cuts < minCuts[startIndex][endIndex]:
                            minCuts[startIndex][endIndex] = cuts
                            splitDecision = splitIndex

                    # write where the final cut was placed in the array
                    cutPositions[splitDecision] = True

    # trying to figure out how to display the cut positions
    # print(cutPositions)
    return minCuts[0][n-1]
print(minCuts('aaaababbabababbaaaababaaa'))
