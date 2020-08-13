"""
Given a list of elements, and k <= n, find the kth largest element
"""
import heapq


def kth_largest(nums, k):
    minheap = []
    for num in nums:
        if len(minheap) == k:
            if minheap[0] < num:
                heapq.heappushpop(minheap, num)
        else:
            heapq.heappush(minheap, num)
    return minheap[0]
