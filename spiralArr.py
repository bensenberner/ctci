import math
arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]

def printSpiral(arr):
    length = len(arr)
    width = len(arr[0])
    layers = math.ceil(length / 2)
    for layer in range(layers):
        if length < 1 and width < 1:
            return
        peri = 2*width + 2*length - 4
        for i in range(peri):
            if i < width:
                print(arr[layer][i + layer])
            elif width <= i and i < width + length - 1:
                print(arr[(layer + i - width + 1)][(len(arr[0]) - layer) - 1])
            elif width + length - 1 <= i and i < width + length - 1 + width - 1:
                print(arr[len(arr) - 1 - layer][len(arr[0]) - 1 - layer - (i - (width + length - 1)) - 1])
            else:
                print(arr[len(arr) - 1 - layer - (i - (width + length - 1 + width - 1)) - 1][layer])
        length -= 2
        width -= 2

for a in arr:
    print(a)
printSpiral(arr)
