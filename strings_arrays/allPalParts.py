def main():
    string = "nitin"
    allPalPartitions(string)


def allPalPartitions(string):
    n = len(string)
    allPart = [[]]
    currPart = []
    allPalPartUtil(allPart, currPart, 0, n, string)
    for i in range(len(allPart)):
        for j in range(len(allPart[i])):
            print(allPart[i][j])


def isPalindrome(string, low, high):
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


def allPalPartUtil(allPart, currPart, start, n, string):
    if start >= n:
        allPart.append(currPart)
        return

    for i in range(start, n):
        print(string[start : i - start + 1])
        if isPalindrome(string, start, i):
            currPart.append(string[start : i - start + 1])
            allPalPartUtil(allPart, currPart, i + 1, n, string)
            currPart._pop()


main()
