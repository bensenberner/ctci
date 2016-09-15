'''
Search in Rotated Array:
Given a sorted array of n integers that has been rotated an unknown number of times,
write code to find an element in the array. You may assume that the array was originally sorted in increasing order.

Rotation problem: I immediately think that I should append the array to itself.
Since it was in sorted order, if I do this, then there will be a point where the max number goes to the min number. That is the point
at which I can assume I have found the minimum.

CONSIDER THE SINGLETON CASE!
'''

def rotArrSearch(oldArr, n):
    '''
    space: O(n)
    time: O(n + log(n))
    '''
    arr = oldArr + oldArr
    minIndex = 1
    while minIndex < len(arr) and arr[minIndex] > arr[minIndex - 1]:
        minIndex += 1
    maxIndex = minIndex + len(oldArr)

    # perform binary search within this
    # needs to return the original index
