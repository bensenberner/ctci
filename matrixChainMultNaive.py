def matrixChainMult(arr, i, j):
    dp
    if i is j:
        return 0
    minimum = float('inf')
    for k in range(i, j):
        count = matrixChainMult(arr, i, k) + \
                matrixChainMult(arr, k+1, j) + \
                arr[i-1] * arr[k] * arr[j]
        minimum = min(minimum, count)
    return minimum

arr = [1, 2, 3, 4, 5]
print(matrixChainMult(arr, 1, len(arr)-1))
