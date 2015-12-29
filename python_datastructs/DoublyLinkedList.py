class Node():

    def __init__(self, val):
        self.val = val
        self.nextNode = None
        self.prevNode = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def insertFront(self, node):
        if not self.tail:
            self.tail = node
        if not self.head:
            self.head = node
        else:
            self.head.prevNode = node
            node.nextNode = self.head
            self.head = node

    def insertBack(self, node):
        if not self.head:
            self.head = node
        if not self.tail:
            self.tail = node
        else:
            self.tail.nextNode = node
            node.prevNode = self.tail
            self.tail = node

    def remove(self, node):
        if node.prevNode:
            node.prevNode.nextNode = node.nextNode
        else:
            self.head = node.nextNode

        if node.nextNode:
            node.nextNode.prevNode = node.prevNode
        else:
            self.tail = node.prevNode

    def printList(self, rev=False):
        node = self.tail if rev else self.head
        while (node):
            print(node.val)
            node = node.prevNode if rev else node.nextNode

    def exists(self, node):
        curr = self.head
        while curr:
            if node.val == curr.val:
                return True
            curr = curr.nextNode

        return False

    def reverseList(self):
        curr = self.head
        while curr:
            tmp = curr.prevNode
            curr.prevNode = curr.nextNode
            curr.nextNode = tmp
            curr = curr.prevNode

        temp = self.head
        self.head = self.tail
        self.tail = temp


l = LinkedList()
l.insertFront(Node(4))
l.insertFront(Node(5))
l.insertFront(Node(7))
l.insertFront(Node(9))
l.printList()
# l.printList(rev=True)
print('reversed!')
l.reverseList()
l.printList()
l.printList(rev=True)
