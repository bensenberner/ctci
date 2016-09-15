def minsteps(n, current, steps, dp):
    if current == n:
        return steps
    if not current in dp:
        dp[current] = steps
    if steps < dp[current]:
        dp[current] = steps
    return min(minsteps(n, current + steps, steps + 1, dp),
            minsteps(n, current - steps, steps + 1, dp))

minsteps(4, 0, 0, {})
