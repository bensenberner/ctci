class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def setLeft(self, val):
        newNode = Node(val)
        self.left = newNode

    def setRight(self, val):
        newNode = Node(val)
        self.right = newNode

    def setLeftNode(self, newNode):
        self.left = newNode

    def setRightNode(self, newNode):
        self.right = newNode

    def printPreOrder(self):
        print(self.val)
        if self.left: self.left.printPreOrder()
        if self.right: self.right.printPreOrder()

    def printInOrder(self):
        if self.left: self.left.printInOrder()
        print(self.val)
        if self.right: self.right.printInOrder()

    def printPostOrder(self):
        if self.left: self.left.printPostOrder()
        if self.right: self.right.printPostOrder()
        print(self.val)

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(5)
    d = Node(12)
    e = Node(58)
    b.setLeftNode(a)
    c.setLeftNode(b)
    d.setRightNode(e)
    c.setRightNode(d)

    c.printPreOrder()
    print('\n\n')
    c.printInOrder()
    print('\n\n')
    c.printPostOrder()
