def findAnySet(nums, targetNum):
    if not nums or not targetNum:
        return []

    elif sum(nums) == targetNum:
        return nums

    else:
        for i in range(len(nums)):
            newNums = nums[:i] + nums[i+1:]
            res = None
            if findAnySet(newNums, targetNum):
                if not res:
                    res = newNums
            if findAnySet(newNums, targetNum - nums[i]):
                res = newNums

            if res:
                return res

        return []

nums = [1, 2, 3]
print(findAnySet(nums, 1))
