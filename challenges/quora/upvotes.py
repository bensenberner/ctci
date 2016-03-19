nums = [4, 8, 7, 6, 9]

nonIncIntervalStart = 0
nonDecIntervalStart = 0

intervals = [None for x in range(0, len(nums)-1)]
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        intervals[i - 1] = 1
    elif nums[i] < nums[i - 1]:
        intervals[i - 1] = -1
    else:
        intervals[i - 1] = 0


# Format= [(relativeNonIncreasingIntervalLength, relativeNonDecreasingIntervalLength)]
# Could replace this with a hash of size k, constantly cycling through it
# Keep adding until we get to the window size, then start subtracting from the beginning of the previous windows








# relIntervalsList = [(0,0) for x in nums]

#for i in range(1, len(nums)):
#
#    isNonIncreasing = False
#    isNonDecreasing = False
#    if nums[i] >= nums[i - 1]:
#        isNonDecreasing = True
#        relIntervalsList[i - 1][1] += 1
#    if nums[i] <= nums[i - 1]:
#        isNonIncreasing = True
#        relIntervalsList[i - 1][0] += 1
#
#    if isNonDecreasing and relIntervalsList[i - 1][1] is 0:
