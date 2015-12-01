from collections import Counter

def main():
    arr = [2, 2, 2, 3, 5, 7, 2, 4, 8, 2]
    targetSum = 6
    print(pointerSolution(arr, targetSum))

def compare(x, y):
    return Counter(x) == Counter(y)

def checkIfListInList(smallList, bigList):
    for l in bigList:
        if compare(l, smallList):
            return True
    return False

def checkIfListInListSorted(smallList, bigList):
    for l in bigList:
        if l == smallList:
            return True
    return False

def pointerSolution(arr, targetSum):
    arr = sorted(arr)
    allSols = []
    for i in range(len(arr) - 2):
        j = i + 1
        k = len(arr) - 1

        while k > j:
            sortList = sorted([arr[i], arr[j], arr[k]])
            if sum(sortList) == targetSum and not \
                    checkIfListInListSorted(sortList, allSols):
                allSols.append(sortList)
                j += 1
                k -= 1
            elif arr[i] + arr[j] + arr[k] > targetSum:
                k -= 1
            else:
                j += 1

    return allSols
# def subSumExists(arr, targetSum):
#     arr = sorted(arr)
#     lookup = {}
#     for num in range(len(arr)):
#         diff = targetSum - arr[num]
#         if not diff in lookup:
#             lookup[diff] = [num]
#         else:
#             lookup[diff].append(num)
#     print(lookup)
#
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i == j: continue
#             sumOfTwo = arr[i] + arr[j]
#             if sumOfTwo in lookup:
#                 return True
#
#     return False

main()
