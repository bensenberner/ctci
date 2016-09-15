class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isTreeBalanced(node):
    leftHeight = getHeight(node.left)
    rightHeight = getHeight(node.right)
    return abs(leftHeight - rightHeight) <= 1

def getHeight(node):
    if not node: return -1
    leftHeight = getHeight(node.left)
    rightHeight = getHeight(node.right)
    return max(leftHeight, rightHeight) + 1

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    a.left = b
    a.right = c
    c.left = d
    c.right = e
    b.left = f

    print(isTreeBalanced(a))
    print(isTreeBalanced(d))
    print(isTreeBalanced(f))
