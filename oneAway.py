'''
Given the three edit operations: insertion, removal, and deletion, write a function to check
if two strings are one or zero edits away
abcde
abcXde
'''

def isOneEditAway(strtup):
    str1, str2 = strtup
    '''
    three cases: str1 is shorter, the same length, or longer than str2
    '''
    shortStr, longStr = str1, str2 if len(str1) < len(str2) else str2, str1
    shortLen = len(shortStr)
    longLen = len(longStr)
    if abs(m - n) > 1: return False
    # can only be edited through replacement
    if shortLen == longLen:
        different = False
        for i in range(shortLen):
            if shortStr[i] != longStr[i]:
                # too many differences for one edit
                if different:
                    return False
                else:
                    different = True
        return True

    # if the longer string has an extra character, then inserting that char into the shorter string
    # and removing the char from the longer string will both make the strings equivalent. So, count
    # how many chars are off in the longer string

    i = 0
    j = 0
    difference = False
    while (i < shortLen and j < longLen):
        if shortStr[i] != longStr[j]:
            if difference:
                return False
            else:
                difference = True
                j += 1
        else:
            i += 1
            j += 1

    return True

print([isOneEditAway(x) for x in [('ABCD', 'ABCD'), ('ABC', 'ABCD'), ('ABC', 'ABD'), ('ABC', 'ABDC')]])
