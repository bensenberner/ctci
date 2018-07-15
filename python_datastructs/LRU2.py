class Node():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

class LRU():

    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}

    def put(self, key, val):
        # imagine this is memoized
        if len(d) == self.capacity:

    def getKey(self, key):
        if key in self.d:
            self.remove(key)
            self.put(key)
            return self.d[key]
        else:
            return None

    def getLatest(self):
        return self.head

    def remove(self, key):
        # check just in case
        if key in self.d:
            node = self.d[key]
