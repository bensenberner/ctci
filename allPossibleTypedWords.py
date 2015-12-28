def printAllPossible(keyPressDict, fingersUsed, currString, currIndex, n):
    if currIndex == n:
        print(currString)
        return
    for finger in fingersUsed[currIndex:]:
        allKeys = keyPressDict[finger]
        for key in allKeys:
            currString += key
            printAllPossible(keyPressDict, fingersUsed, currString, currIndex + 1, n)
