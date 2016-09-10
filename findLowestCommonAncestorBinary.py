class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def findLowestAncestor(self, nodeA, nodeB):
        isLeftAncestorA = False
        isRightAncestorA = False
        isLeftAncestorB = False
        isRightAncestorB = False
        if self.left:
            isLeftAncestorA = self.left.isAncestorOfNode(nodeA)
            isLeftAncestorB = self.left.isAncestorOfNode(nodeB)
            if (isLeftAncestorA and isLeftAncestorB):
                return self.left.findLowestAncestor(nodeA, nodeB)
        if self.right:
            isRightAncestorA = self.right.isAncestorOfNode(nodeA)
            isRightAncestorB = self.right.isAncestorOfNode(nodeB)
            if (isRightAncestorA and isRightAncestorB):
                return self.right.findLowestAncestor(nodeA, nodeB)
        if ((isLeftAncestorA and isRightAncestorB) or (isLeftAncestorB and isRightAncestorA)):
            return self
        return None

    def isAncestorOfNode(self, node):
        # a node is an ancestor of itself
        if self is node: return True
        # if the node has no children then it cannot be anyone's ancestor
        if not self.left and not self.right: return False

        leftAncestorNode = False
        rightAncestorNode = False
        if self.left:
            leftAncestorNode = self.left.isAncestorOfNode(node)
        if self.right:
            rightAncestorNode = self.right.isAncestorOfNode(node)
        return leftAncestorNode or rightAncestorNode

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)
    i = Node(9)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = g
    g.left = h
    g.right = i
    print(a.findLowestAncestor(h, i).val)
