import math

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def printTree(self, i):
        if self.left:
            self.left.printTree(i+1)
        print(self.val, i)
        if self.right:
            self.right.printTree(i+1)

def buildTree(arr, start, end):
    # base case
    if start > end: return None
    midDex = math.ceil((((end + start)) / 2))

    newNode = Node(arr[midDex])
    newNode.left = buildTree(arr, start, midDex-1)
    newNode.right = buildTree(arr, midDex+1, end)

    return newNode

a = [2, 3, 5, 8, 11, 12, 15]
tree = buildTree(a, 0, len(a)-1)
tree.printTree(0)
