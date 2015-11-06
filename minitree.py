import math

treeProxy = []

def addNodeToTree(arr, start, end):
    midDex = math.ceil((((end - start)) / 2))
    treeProxy.append(midDex)
    if abs(start - end) > 1:
        addNodeToTree(arr, start, midDex)
        addNodeToTree(arr, midDex, end)

a = [2, 3, 5, 8, 11, 12, 15]
addNodeToTree(a, 0, len(a))

print(treeProxy)
