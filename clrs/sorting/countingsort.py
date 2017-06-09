def countsort(A, k):
    C = [0 for _ in range(k)]
    B = []
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(len(C)):
        for j in range(C[i]):
            B.append(i)
    return B

if __name__ == "__main__":
    arr = [5, 4, 2, 8, 6, 4, 4, 2, 8, 6, 2]
    k = 10
    sorted_arr = countsort(arr, k)
    print(sorted_arr)
