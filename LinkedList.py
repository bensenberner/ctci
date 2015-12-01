class Node():
    def __init__(self, v):
        self.val = v
        self.nextNode = None

class LinkedList():

    def __init__(self, node):
        self.head = node

    def add(self, node):
        node.nextNode = self.head
        self.head = node

    def printList(self):
        node = self.head
        while node:
            print(node.val)
            node = node.nextNode

a = Node(32)
b = Node(55)
c = Node(48)
l = LinkedList(a)
l.add(b)
l.add(c)
l.printList()
