from math import floor

def merge(A, p, q, r):
    L = A[p:q] + [float('inf')]
    R = A[q:r] + [float('inf')]
    i = j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergesort(A, p, r):
    if p < r - 1:
        q = floor((p + r) / 2)
        mergesort(A, p, q)
        mergesort(A, q, r)
        merge(A, p, q, r)

if __name__ == "__main__":
    arr = [5, 2, 4, 1, 3]
    print("Before: %s" % str(arr))
    mergesort(arr, 0, len(arr))
    print("After: %s" % str(arr))
