def selection_sort(A):
    n = len(A)
    for i in range(n):
        minVal = A[i]
        minIdx = i
        for j in range(i+1, n):
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
        A[i], A[minIdx] = A[minIdx], A[i]
    return A

if __name__ == "__main__":
    arr = [5, 4, 2, 3, 1, -8, -4]
    print(arr)
    sorted_arr = selection_sort(arr)
    print(sorted_arr)
