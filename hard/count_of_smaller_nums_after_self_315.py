"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
----
Approach 1:
start from the right end. initialize a max heap.
for every element:
    pop items off from the heap until either it is empty or the max is less than the current element
    store the size of the heap in the result array
    move to the left

hmmm but this is taking a while...maybe I can use better memoization?
But as I'm going through the output array...how would I know which previous result I could reuse?
They could be all different sizes
I'm going to try my approach first
wait a sec...I might have to pop out ALL the items...this is n^2logn!
no way this is the best answer

"""
import heapq
from collections import deque


class MaxHeap:
    def __init__(self):
        self.heap = []

    def __bool__(self):
        return bool(self.heap)

    def push(self, val):
        heapq.heappush(self.heap, -val)

    def _pop(self):
        return -heapq.heappop(self.heap)

    def _peek(self):
        return -self.heap[0]

    def find_num_elements_greater_than(self, val):
        position = 0
        temp_stack = []
        while self and val <= self._peek():
            temp_stack.append(self._pop())
            position += 1
        while temp_stack:
            self.push(temp_stack.pop())
        return position


def countSmaller(nums):
    n = len(nums)
    if n == 0:
        return []
    result = deque()
    heap = MaxHeap()
    for idx in range(n - 1, -1, -1):
        num_elements_less_than = (
            n - idx - 1 - heap.find_num_elements_greater_than(nums[idx])
        )
        result.appendleft(num_elements_less_than)
        heap.push(nums[idx])
    return list(result)
