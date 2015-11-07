def findDex(arr):
    for i in range(0, len(arr)):
        if (arr[i] > i):
            return False
        elif (arr[i] == i):
            return True
    return False

a = [0, 1, 2, 3, 7, 9, 12, 15, 18]
print(findDex(a))
