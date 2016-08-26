'''
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.

Questions to consider:
    unique elements in either?
    unique elements between both?
    does it matter?

'''

def sortedMerge(a, b):
    # find where the buffer space of a ends
    aIdx = len(a) - 1
    while (a[aIdx] is None):
        aIdx -= 1
    bIdx = len(b) - 1
    placementIdx = len(a) - 1
    while (aIdx >= 0 and bIdx >= 0):
        if a[aIdx] > b[bIdx]:
            a[placementIdx] = a[aIdx]
            aIdx -= 1
        else:
            a[placementIdx] = b[bIdx]
            bIdx -= 1
        placementIdx -= 1

    # add any remaining elements of b
    while bIdx >= 0:
        a[placementIdx] = b[bIdx]
        bIdx -= 1
        placementIdx -= 1

if __name__ == "__main__":
    a = [3, 4, 6, 22, None, None, None, None, None]
    b = [2, 5, 7, 7, 8]
    print(a)
    sortedMerge(a, b)
    print(a)
