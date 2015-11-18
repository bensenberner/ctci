def findAllSequences(arr, currArr, currIndex, num):
    if (sum(currArr) == num):
        print(currArr)
        currArr = [arr[currIndex]]
        return

    for i in range(len(arr[currIndex:])):
        if arr[i] <= currArr[-1]:
            currArr.append(arr[i])
            if currIndex == len(arr) - 1:
                break
            findAllSequences(arr, currArr, currIndex + 1, num)
        else:
            currArr = [arr[i]]


arr = [3, 7, 2, 8, 4, 3, 2]
num = 9


findAllSequences(arr, [arr[0]], 1, num)
