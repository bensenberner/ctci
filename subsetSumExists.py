def isSubsetSum(nums, n, num):
    subset = [[None for x in range(n+1)] for y in range(num+1)]

    for i in range(n+1):
        subset[0][i] = True

    for i in range(num+1):
        subset[i][0] = False

    for i in range(n+1):
        for j in range(num+1):
            subset[i][j] = subset[i][j-1]
            if i >= nums[j-1]:
                subset[i][j] = subset[i][j] or subset[i - nums[j-1]][j-1]

    for row in subset:
        print(row)

    return subset[num][n]

nums = [3, 34, 4]
print(isSubsetSum(nums, 7, len(nums)))
