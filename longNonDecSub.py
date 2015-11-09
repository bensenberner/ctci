def longestSeq(arr):
    # [4, 6, 8, 9]
    #  i  i  i  i
    #  carries with it the value
    # lengths = [None]*(len(arr) + 1)
    # lengths[1] = 0
    indexLengths = [1] * (len(arr))
    prevLargests = [-(float('inf'))]*(len(arr))
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1] and indexLengths[i - 1]:
            length += 1
            if length > longestLength:
                longestLength = length
            else:
                length = 1

    return longestLength

a = [5, 4, 6, 8, 9]
print(longestSeq(a))
