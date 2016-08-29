# TODO: finish this
class Node():
    def __init__(self, val, rank):
        self.val = val
        self.rank = rank
        self.nextNode = None

def sortedLinkedList():

    def __init__(self):
        self.head = None

    def insert_node(self, newNode):
        if not self.head:
            self.head = newNode
        elif self.head.val > newNode.val:
            newNode.nextNode = self.head
            self.head = newNode
        else:
            node = self.head
            while (node.nextNode and node.nextNode.val <= newNode.val):
                node = node.nextNode
            newNode.nextNode = node.nextNode
            node.nextNode = newNode

    def increment_ranks(self, node):
        while node:
            node.rank += 1
            node = node.nextNode

class streamRank():

    def __init__(self, stream):
        self.d = {}
        for integer in stream:
            self.track(integer)

    def track(self, integer):

    def getRankOfNumber(self, num):
        if num not in self.d:
            return -1
        else:
            node = self.d[num]
            return node.rank
