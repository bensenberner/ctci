import heapq

class Maxstack(object):
    def __init__(self):
        self.heap = []
        self.stack = []

    def push(self, item):
        heapq.heappush(self.heap, -item)
        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        maxItem = -self.heap[0]
        if item == maxItem:
            return -heapq.heappop(self.heap)
        else:
            return item

    def findMax(self):
        return -self.heap[0]

stacky = Maxstack()
stacky.push(5)
stacky.push(8)
stacky.push(3)
stacky.push(14)
print(stacky.findMax())
print(stacky.pop())
print(stacky.findMax())
