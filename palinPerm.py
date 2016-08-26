'''
Sees if the input string is a permutation of a palindrome
'''
def palPerm(string):
    strSet = {}
    oddChars = 0
    for char in string:
        if char is ' ':
            continue
        if not char in strSet:
            strSet[char] = 1
            oddChars += 1
        else:
            strSet[char] += 1
            if strSet[char] % 2 == 0:
                oddChars -= 1
            else:
                oddChars += 1

    return True if oddChars <= 1 else False

print(palPerm('aaaaaa'))
