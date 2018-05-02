import heapq
from collections import deque

def smallestRange(arrs):
    num_arrs = len(arrs)
    curr_max = float("-inf")
    heap = []
    # initialize the heap with the elements from all of the arrs
    for arr in arrs:
        min_ele = arr[0]
        curr_max = max(curr_max, min_ele)
        heapq.heappush(heap, min_ele)
    min_range_diff = curr_max - heap[0]
    lower_range = heap[0]
    upper_range = curr_max
    deques = [deque(arr[1:]) for arr in arrs]
    # TODO: need to pick the correct deque in O(1) time
if __name__ == "__main__":
    arrs = [
        [4, 7, 9, 12, 15],
        [0, 8, 10, 14, 20],
        [6, 12, 16, 30, 50]
    ]
    print(smallestRange(arrs))