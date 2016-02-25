def makeMinNum(pattern):
    nums = [1]
    for char in pattern:
        i = len(nums) - 1
        if char == 'D':
            while i > 0 and nums[i] < nums[i-1]:
                i -= 1
            while i < len(nums):
                nums[i] += 1
                i += 1
            nums.append(nums[-1]-1)

        if char == 'I':
            while i > 0 and nums[i] < nums[i-1]:
                i -= 1
            while i < len(nums):
                nums[i] += 1
                i += 1
            nums.append(nums[-1]+1)

    return(nums)

print(makeMinNum('I'))

DDI
321
