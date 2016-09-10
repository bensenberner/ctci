class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.minRight = None
        self.maxLeft = None

    def setMinsMaxes(self):
        self.minRight = self.right.getMin() if self.right else float('inf')
        self.maxLeft = self.getMaxLeft()

    def getMin(self):
        if not self.left:
            leftMin = float('inf')
        else:
            leftMin = self.left.getMin()

        if not self.right:
            rightMin = float('inf')
        else:
            rightMin = self.right.getMin()

        return min(leftMin, rightMin)

    def getMax(self):
        if not self.left:
            leftMax = -float('inf')
        else:
            leftMax = self.left.getMax()

        if not self.right:
            rightMax = -float('inf')
        else:
            rightMax = self.right.getMax()

        return max(leftMax, rightMax)


def isBinarySearchTree(node):
    node.setMinsMaxes()

if __name__ == "__main__":

