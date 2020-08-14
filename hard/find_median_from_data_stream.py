import heapq
from typing import Optional


class Heap:
    def __init__(self, is_max):
        self._heap = []
        self._multiplier = -1 if is_max else 1

    def __bool__(self):
        return bool(self._heap)

    def __len__(self):
        return len(self._heap)

    def push(self, val):
        heapq.heappush(self._heap, self._multiplier * val)

    def pop(self):
        return self._multiplier * heapq.heappop(self._heap)

    def peek(self):
        return self._multiplier * self._heap[0] if self._heap else None


class MedianFinder:
    def __init__(self):
        self.lower_heap = Heap(is_max=True)
        self.upper_heap = Heap(is_max=False)

    def addNum(self, num: int) -> None:
        self.lower_heap.push(num)
        if len(self.lower_heap) - len(self.upper_heap) >= 2:
            self.upper_heap.push(self.lower_heap.pop())
        if self.upper_heap and self.lower_heap.peek() > self.upper_heap.peek():
            lower_max = self.lower_heap.pop()
            upper_min = self.upper_heap.pop()
            self.lower_heap.push(upper_min)
            self.upper_heap.push(lower_max)

    def findMedian(self) -> Optional[float]:
        if not self.lower_heap and not self.upper_heap:
            return None
        if not self.upper_heap:
            return self.lower_heap.peek()
        if len(self.lower_heap) == len(self.upper_heap):
            return (self.lower_heap.peek() + self.upper_heap.peek()) / 2
        else:
            return self.lower_heap.peek()
