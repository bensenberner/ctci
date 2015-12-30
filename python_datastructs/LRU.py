class Node():
    def __init__(self, k, v):
        self.key = k
        self.val = v


class LRUCache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.mapping = {}
        head = None
        tail = None

    def get(self, key):
        if key in self.mapping:
            n = self.mapping[key]
            self.remove(n)
            self.insertFront(n)
            return n.val
        else:
            return None

    def put(self, key, val):
        if key in self.mapping:
            node = self.mapping[key]
            node.val = val
            self.remove(node)
            self.insertFront(node)

        else:
            node = Node(key, val)
            if len(self.mapping) > capacity:
                self.remove(self.tail)
                del self.mapping[self.tail.key]
                self.insertFront(node)
            else:
                self.insertFront(node)

    def remove(self, node):
        if node.prevNode:
            node.prevNode.nextNode = node.nextNode
        else:
            self.head = node.nextNode

        if node.nextNode:
            node.nextNode.prevNode = node.prevNode
        else:
            self.tail = node.prevNode

    def insertFront(self, node):
        if not self.head:
            self.head = node
            self.tail = node

        else:
            node.nextNode = self.head
            self.head = node

    def printCache(self, rev=False):
        node = self.head if not rev else self.tail
        while (node):
            print(node.val)
            node = node.nextNode if not rev else node.prevNode

lru = LRUCache(2)
a = Node('a', 23)
b = Node('b', 51)
c = Node('c', 58)
d = Node('d', 68)
e = Node('e', 76)
lru.put(a)
lru.printCache()
lru.put(b)
lru.printCache()
lru.put(c)
lru.printCache()
lru.put(d)
lru.printCache()
lru.put(e)
lru.printCache()
