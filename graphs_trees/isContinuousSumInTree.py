def findSum(root, currNum, originalNum, inPath):
    if not root: return False
    if root.val == currNum: return True
    foundInPath = findSum(root.left, currNum - root.val, originalNum, True) \
            or findSum(root.right, currNum - root.val, originalNum, True)
    if foundInPath: return True
    return foundInPath if inPath else foundInPath \
            or findSum(root.left, originalNum, originalNum, False) \
            or findSum(root.right, originalNum, originalNum, False)

