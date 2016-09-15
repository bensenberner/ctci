'''
Given an infinite number of quarters, nickels, dimes, pennies, return all the ways of representing n cents
'''

def countWays(denoms, memo, index, n):
    if index > len(denoms): return 1
    if memo[index][n] > 0: return memo[index][n]

    ways = 0
    currDenom = denoms[index]
    for i in range(0, n, currDenom):
        if n - currDenom >= 0:
            ways += countWays(denoms, memo, index+1, n-currDenom)
    return ways

def main():
    denoms = [25, 10, 5, 1]
    n = 5
    memo = [[0 for numOfCents in range(n + 1)] for denom in denoms]
    print("Num of ways to count "+str(n)+" cents is "+str(countWays(denoms, memo, 0, n)))
    for row in memo:
        print(row)

main()
