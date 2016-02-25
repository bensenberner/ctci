from copy import deepcopy

def powerset(nums):
    powerSet = [set()]
    for num in nums:
        n = len(powerSet)
        for i in range(n):
            newSet = deepcopy(sets[i])
            newSet.add(num)
            powerSet.append(newSet)

    return powerSet

nums = set([1, 2, 5, 6])
print(powerset(nums))
