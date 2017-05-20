def insertion_sort(A, rev=False):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and \
                (A[i] < key if rev else A[i] > key):
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    sorted_arr = insertion_sort(arr, rev=True)
    print(sorted_arr)
