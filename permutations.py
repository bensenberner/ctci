def swap(arr, leftIndex, rightIndex):
    arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]
    return arr

def permute(arr, left, right):
    if left == right:
        print(''.join(arr))
    else:
        for i in range(left, right):
            arr = swap(arr, left, i)
            permute(arr, left+1, right)
            arr = swap(arr, left, i)

string = list("ABCDEFG")
permute(string, 0, len(string))
