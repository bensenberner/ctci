from llist import dllist, dllistnode
class LRU(object):

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.lst = dllist()
        self.d = {}

    def insert(self, key, value):
        if key in self.d:
            node = self.d[key]
            self.lst.remove(node)
            node.value = value
            self.lst.appendleft(node)
        else:
            if self.lst.size < self.maxSize:
                newNode = dllistnode(value)
                self.d[key] = newNode
                self.lst.appendleft(newNode)

            else:
                oldNode = lst.nodeat(-1)
                del
