import math

def findDex(arr, startDex, endDex):
    midDex = int(math.ceil(startDex + endDex) / 2)
    if startDex > endDex: return -1
    if arr[midDex] == midDex: return midDex
    if arr[midDex] < midDex:
        return findDex(arr, midDex + 1, endDex)
    if arr[midDex] > midDex:
        return findDex(arr, startDex, midDex - 1)

a = [-1, 0, 0, 0, 3]
print(findDex(a, 0, len(a) - 1))
