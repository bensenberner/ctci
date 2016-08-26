def findLexMinStringRot(string):
    minIndices = {}
    minChar = '}'
    for i in range(len(string)):
        if not string[i] in minIndices:
            minIndices[string[i]] = set([i])
        else:
            minIndices[string[i]].add(i)
        minChar = min(minChar, string[i])

