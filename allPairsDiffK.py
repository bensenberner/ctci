def findAllPairs(nums, k):
    recordedNums = set()
    pairs = []
    for num in nums:
        if num - k in recordedNums:
            pairs.append([num, num - k])
        if num + k in recordedNums:
            pairs.append([num, num + k])
        recordedNums.add(num)
    return pairs

def main():
    nums = [1, 3, 9, 6, 2, 8, 12, 10, 1]
    k = 3
    print(findAllPairs(nums, k))

main()
