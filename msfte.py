def gap(nums):
    n = len(nums)
    missing = []
    for idx in range(n-1):
        missing.extend(range(nums[idx]+1, nums[idx+1]))
    return missing

print(gap([1,2,5,6,10]))

