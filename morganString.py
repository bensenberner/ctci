def morgan():
    a = 'BBA'
    b = 'BBBD'
    s1 = list(a[::-1])
    s2 = list(b[::-1])

    bigString = ''
    while (s1 or s2):
        if not s1:
            bigString += s2.pop()
            continue
        if not s2:
            bigString += s1.pop()
            continue
        if s1[-1] < s2[-1]:
            bigString += s1.pop()
        elif s1[-1] > s2[-1]:
            bigString += s2.pop()
        else:


    print(bigString)

def findSmallerChar(s1, s2):
    i, j = -1, -1
    while i == j and i > -(len(s1)) and j > -(len(s2)):
        i -= 1
        j -= 1
