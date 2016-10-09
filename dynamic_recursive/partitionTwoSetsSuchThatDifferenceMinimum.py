def findMinPartition(nums):
    sort = sorted(nums)
    set1 = nums[:-1]
    set2 = [nums[-1]]
    sum1 = sum(set1)
    sum2 = sum(set2)
    currDiff = abs(sum1 - sum2)
    for i in range(len(set1) - 1, -1, -1):
        num = set1[i]
        sum1 -= num
        sum2 += num
        newDiff = abs(sum1 - sum2)
        print(set1, set2, currDiff)
        if newDiff > currDiff:
            break
        set1.pop(i)
        set2.append(num)
        currDiff = newDiff
    return currDiff

arr1 = [1, 6, 11, 5]
print(findMinPartition(arr1))
