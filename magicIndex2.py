'''
if values are distinct
'''
def magicIndex(arr, low, high):
    if low > high: return -1

    mid = (low + high) // 2

    leftExists = -1
    rightExists = -1

    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        rightExists = magicIndex(arr, mid, high)
    else:
        leftExists = magicIndex(arr, low, mid)

    if (leftExists == -1 and rightExists == -1):
        return -1
    else:
        return leftExists if leftExists != -1 else rightExists

if __name__ == "__main__":
    arr = [-8, 0, 1, 3, 16]
    # arr = [-16, -4, 4, 4, 4, 8, 12]
    print(magicIndex(arr, 0, len(arr)))
