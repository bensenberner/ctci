import heapq
from collections import Counter

class MaxHeap:
    def __init__(self):
        self.h = []

    def __repr__(self):
        return str(self.h)

    def push(self, val):
        heapq.heappush(self.h, -val)

    def pop(self):
        return -heapq.heappop(self.h)

    def peek(self):
        return -(self.h[0])


def max_val(arr, k):
    heap = MaxHeap()
    c = Counter()
    n = len(arr)
    dp = [float("-inf") for _ in range(n)]
    dp[0] = arr[0]
    heap.push(arr[0])
    c[arr[0]] = 1
    for idx, element in enumerate(arr):
        if idx == 0: continue
        if idx >= k:
            c[dp[idx - k]] -= 1

        # find a max that is within the (idx - k, idx)
        while c[heap.peek()] <= 0:
            heap.pop()
        currMax = heap.peek()

        dp[idx] = arr[idx] + currMax
        heap.push(dp[idx])
        c[dp[idx]] += 1

    print(dp)
    return dp[-1]


if __name__ == "__main__":
    arr = [2, 5, -7, -3, -4, 8, -17, 20, 4]
    k = 3
    print(max_val(arr, k))