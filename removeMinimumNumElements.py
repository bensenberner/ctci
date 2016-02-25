def minRemovals(nums):
    if 2 * min(nums) > max(nums):
        return 0
    else:
        return min(minRemovals(nums[1:]), minRemovals(nums[:-1])) + 1

def main():
    nums = [4, 5, 100, 9, 10, 11, 12, 15, 200]
    nums.sort()
    print(minRemovals(nums))

main()
