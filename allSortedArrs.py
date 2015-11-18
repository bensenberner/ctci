def sortedArrs(arrA, arrB, dexA, dexB, currList, currElement, isB):
    if isB:
        currList.append(currElement)
        print(currList)

    if not isB:
        for i in range(len(arrA)):
