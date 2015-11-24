# square the elements of an array, keep it sorted

a = [-4, -3, -1, 0, 2, 3, 5, 8]

def squareArr(arr):
    j = 0
    for i in range(len(arr) - 1, -1, -1):
        if abs(arr[i]) < abs(arr[0]):
            # arr[i], arr[0] = arr[0], arr[i]
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
        arr[i] *= arr[i]
            # j += 1
    return(arr)

print(a)
print(squareArr(a))

