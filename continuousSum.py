def func(num):
    currSum = 0
    memo = {currSum}
    numWays = 0
    for i in range(1, num//2+3):
        currSum += i
        if currSum - num in memo:
            numWays += 1
        memo.add(currSum)
    return numWays

print(func(21))
