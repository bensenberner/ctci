'''
given an arr of ints, positive and negative, find the contiguous seq with the
largest sum. Return that sum.
'''

def largestSum(arr):
    # for robustness
    n = len(arr)
    if n == 0: return None

    maxSum = currSum = arr[0]
    startIdx = endIdx = 0
    for i in range(1, n):

