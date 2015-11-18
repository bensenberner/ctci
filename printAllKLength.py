def printAllKLengthRec(origSet, prefix, k, damn):
    if k == 0:
        # print(prefix)
        damn.append(prefix)
        return damn

    for i in range(len(origSet)):
        newPrefix = prefix + origSet[i]
        printAllKLengthRec(origSet, newPrefix, k - 1, damn)

    return damn

thisset = ['a', 'b', 'c']
damn = []
print(printAllKLengthRec(thisset, '', 1, damn))
