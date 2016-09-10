def numTrailingZeroesInFactorial(n):
    nums = []
    for i in [2, 5, 10]:
        divisor = n
        while (divisor % i != 0):
            divisor -= 1
        j = divisor / i
        nums.append(computeSumOneToN(j))

    print(nums)
    numTwos, numFives, numTens = nums
    print('numtwos', numTwos)
    print('numfives', numFives)
    print('numtens', numTens)

    numTwos -= numTens
    numFives -= numTens
    numTwoFivePairs = min(numTwos, numFives)
    return int(numTwoFivePairs - numTens)

def computeSumOneToN(n):
    return (n * (n+1)) / 2

if __name__ == "__main__":
    print(numTrailingZeroesInFactorial(10))
