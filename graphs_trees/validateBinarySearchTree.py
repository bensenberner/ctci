class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.min = float('inf')
        self.max = float('-inf')

    def __repr__(self):
        return "{}|min:{}|max:{}".format(self.val, self.min, self.max)

def setMinOrMax(root, isMin):
    if not root: return
    if isMin:
        root.min = root.min if root.min else min(root.val,
                getMinOrMax(root.left, isMin),
                getMinOrMax(root.right, isMin))
    else:
        root.max = root.max if root.max else max(root.val,
                getMinOrMax(root.left, isMin),
                getMinOrMax(root.right, isMin))


def isValidBST(root):
    if not root: return True
    isLeftGood = isValidBST(root.left)
    isRightGood = isValidBST(root.right)
    setMinOrMax(root.right, True)
    setMinOrMax(root.left, False)

    isBalanced = root.max <= root.val <= root.min

    return isLeftGood and isRightGood and isBalanced


if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(5)
    e = TreeNode(50)
    a.left = b
    a.right = d
    d.left = c
    d.right = e
    print(isValidBST(d))
