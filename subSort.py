'''
given an array of ints, write a method to find indices m and n such that if you
sorted elements m through n, the entire array would be sorted. Minimize n - m,
i.e. find the smallest such sequence
'''

# wouldn't you have to start from the ends and then move inward on either
# side...?
# no, you idiot, because what if it was like
# 1, 3, 5, 7, 9, 2, 4, 6, 8, 10

def subSort(arr):
    n = len(arr)

    i = 0
    j = len(arr) - 1

    # find the left third of the array that is already sorted
    while (i < n-1 and arr[i+1] >= arr[i]):
        i += 1

    # find the right third of the array that is already sorted
    while (j > 0 and arr[j-1] <= arr[j]):
        j -= 1

    # the entire list is already sorted
    if (i >= j): return (-1, -1)

    # could do this in one pass, whatever
    maxMidNum = max(arr[i+1], j)
    minMidNum = min(arr[i+1], j)

    while (j < n-1 and arr[j+1] <= maxMidNum):
        j += 1

    while (i > 0 and arr[i-1] >= minMidNum):
        i -= 1

    return (i, j)

if __name__ == "__main__":
    arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print(subSort(arr))
