class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def setLeftNode(self, node):
        self.left = node
        node.parent = self

    def setRightNode(self, node):
        self.right = node
        node.parent = self

    def getNextNode(self):

