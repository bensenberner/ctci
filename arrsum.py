'''
Determine all possible pairs of numbers in a list that sum to some
particular value.
'''
def findSumInArr(sumnum, arr):
    # logN operation
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1
    pairs = []
    # iterate through the list once
    # TODO: implement logic for duplicate numbers
    while start < end:
        summation = arr[start] + arr[end]
        if summation == sumnum:
            pairs.append([arr[start],arr[end]])
            start += 1
        elif summation < sumnum:
            start += 1
        elif summation > sumnum:
            end -= 1

    return pairs

def main():
    a = [-4, -2, -1, 0, 1, 3, 7, 9, 11, 12, 13]
    num = 10
    print(findSumInArr(num, a))

main()
