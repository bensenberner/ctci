from time import time

class Node():
    def __init__(self, val):
        self.val = val
        self.nextNode = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.hour = None
        self.minute = None
        self.second = None

    def pushToFront(self, node):
        if not self.hour:
            self.hour = node
        if not self.minute:
            self.minute = node
        if not self.second:
            self.second = node

class Events():
    def __init__(self):
        self.events = LinkedList()
        self.prevSecondCount = 0
        self.prevMinuteCount = 0
        self.prevHourCount = 0

    def increment(self):
        newNode = Node(time.time())
        self.events.pushToFront(newNode)
        self.prevSecondCount += 1
        self.prevMinuteCount += 1
        self.prevHourCount += 1

    def getAllEventsMostRecentHour(self):
        pass
