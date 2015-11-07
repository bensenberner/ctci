# counts the number of possible ways to climb n stairs if you can go 1, 2, or 3
# stairs at a time
def countStairs(n, memo):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    else:
        if (memo[n] == None):
            memo[n] = countStairs(n - 1, memo) + \
                        countStairs(n - 2, memo) + \
                        countStairs(n - 3, memo)
        return memo[n]

def main():
    n = 250
    memo = [None] * n
    print(countStairs(n - 1, memo))

main()
