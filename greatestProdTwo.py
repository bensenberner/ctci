def findProd(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] * arr[1]
    else:
        max1 = min2 = max(arr[0], arr[1])
        min1 = max2 = min(arr[0], arr[1])
        for e in arr[2:]:
            if e > max1:
                max2 = max1
                max1 = e
            elif e > max2:
                max2 = e
            elif e < min1:
                min2 = min1
                min1 = e
            elif e < min2:
                min2 = e
        return max(max1 * max2, min1 * min2)

print(findProd([-5, 1, -5]))
