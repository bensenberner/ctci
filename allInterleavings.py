'''
Given two strings str1 and str2, write a function that prints all interleavings
of the given two strings. You may assume that all characters in both strings
are different
'''

def interleavings(currStr, str1, str2, index1, index2, n, m):
    if len(currStr) == n + m:
        print(currStr)
        return

    # we have run out of letters to interleave
    if index2 == m:
        return

    # starting from index1 (which is right after the position of the
    # character that we just inserted), proceed to place the current character
    # from string 2 (as indicated by index2) in all possible positions in the
    # current string.
    for i in range(index1, len(currStr) + 1):

        # place the character
        newStr = currStr[:i] + str2[index2] + currStr[i:]

        # in the next call, index1 must be ahead of the current character
        # that was placed at position i. index2 must be incremented to use
        # the next character in the weaving.
        interleavings(newStr, str1, str2, i + 1, index2 + 1, n, m)

def main():
    str1 = 'ab'
    str2 = 'cd'
    interleavings(str1, str2, str2, 0, 0, len(a), len(b))
