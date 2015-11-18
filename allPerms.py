def func(arr, tempArr, tempDex, r):
    if checkIntLen(tempArr) == r:
        print(tempArr)
        return

    for i in range(len(arr)):
        # if tempDex > r:
            # break
        tempArr[tempDex] = arr[i]
        if i == len(arr):
            break
        func(arr[i+1:], tempArr, tempDex + 1, r)

def checkIntLen(a):
    count = 0
    for i in a:
        if i is None:
            break
        count += 1
    return count

arr = [1, 2, 3, 4]
r = 2
func(arr, [None] * r, 0, r)
