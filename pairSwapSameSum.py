'''two arrays, find a pair of values (one from each) that you can swap to give
each of the arrays the same sum'''

def findEqualizerPair(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    diff = sum2 - sum1
    # need to find a pair whose diff is this
    for num1 in arr1:
        # check if that's the diff?
        num2 = diff - num1

        # could use binary search instead
        if num2 in arr2:
            return (num1, num2)
    return (None, None)

if __name__ == "__main__":
    arr1 = [4, 1, 2, 1, 1, 2]
    arr2 = [3, 6, 3, 3]
    print(findEqualizerPair(arr1, arr2))
