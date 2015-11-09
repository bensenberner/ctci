def maxContiguousProduct(arr):
    currMaxProd = 1
    currMinProd = 1
    totalMax = 1
    for i in range(0, len(arr)):
        if arr[i] > 0:
            currMaxProd *= arr[i]
            currMinProd = min(currMinProd * arr[i], 1)

        # reset at 0
        elif arr[i] == 0:
            currMaxProd = 1
            currMinProd = 1

        # else, negative
        else:
            temp = currMaxProd
            currMaxProd = max(currMinProd * arr[i], 1)
            currMinProd = temp * arr[i]

        if totalMax < currMaxProd:
            totalMax = currMaxProd

    return totalMax

print(maxContiguousProduct([2, 3, -1, -3, -5]))
