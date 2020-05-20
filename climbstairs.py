def climbStairs(n: int) -> int:
    memo = [0] * (n + 1)
    for idx in range(n + 1):
        if idx > 0:
            memo[idx] = memo[idx - 1] + 1
            print('hello', idx)
        if idx > 1:
            memo[idx] = memo[idx - 2] + 1
            print('uh oh', idx)
        print(memo)
    return memo[-1]

climbStairs(2)