def generateUtil(x, arr, curr_sum, curr_dex):
    if curr_dex > len(arr) - 1:
        return
    if curr_sum == x:
        print(arr)
        return

    num = 1
    while (num <= x - curr_sum and (curr_dex == 0 or num <= arr[curr_dex - 1])):
        arr[curr_dex] = num
        generateUtil(x, arr, curr_sum + num, curr_dex+1)
        num += 1

def generate(x):
    arr = [None] * x
    generateUtil(x, arr, 0, 0)

generate(5)
