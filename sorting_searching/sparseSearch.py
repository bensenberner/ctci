'''
given a sorted array of strings that is interspersed with empty strings,
write a method to find the location of a given string
'''

def sparseSearch(testWord, arr):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        # should I preserve this check or is it redundant or WHAT
#        while (arr[low] == "" and low <= high):
#            low += 1
#        while (arr[high] == "" and low <= high):
#            high -= 1
        initMid = (low + high) // 2
        mid = findRealMid(initMid, low, high, arr)
        # early return
        if mid == -1:
            return -1
        if testWord < arr[mid]:
            high = mid - 1
        elif testWord > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1

# think of this as breadth-first search around "mid" on the number line
def findRealMid(mid, low, high, arr):
    counter = 0
    num = 0
    oldMid = mid
    while (arr[mid] == ""):
        if mid > high or mid < low:
            return -1
        if counter % 4 == 0:
            num += 1
        elif counter % 4 == 1:
            num *= -1
        elif counter % 4 == 2:
            num -= 1
        else:
            num *= -1
        mid = oldMid + num
        counter += 1
    return mid

if __name__ == "__main__":
    testWord = "dad"
    arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(sparseSearch(testWord, arr))
