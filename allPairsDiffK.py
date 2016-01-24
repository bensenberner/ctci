def findAllPairs(nums, k):
    recordedNums = set()
    pairs = set()
    for num in nums:
        if num - k in recordedNums and (num - k, num) not in pairs:
            pairs.add((num, num - k))
        if num + k in recordedNums and (num + k, num) not in pairs:
            pairs.add((num, num + k))
        recordedNums.add(num)
    return pairs

def main():
    nums = [1, 3, 9, 6, 2, 8, 12, 10, 1, 3, 3]
    k = 2
    print(findAllPairs(nums, k))

main()
