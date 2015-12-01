import numpy as np
# count the nber of ways to divide a nber up four ways
# sounds like a change making problem!!!

#dp = [[]] * 5001
#for i in range(5001):
#    dp[i].append([-1] * 5)
#print(dp)

def countWays(num, kParts):
    dp = np.full((5001, 5001, kParts + 1), -1.)
    def countWaysUtil(n, parts, nextPart):
        if parts == 0 and n == 0: return 1
        if n <= 0 or parts <= 0: return 0

        if dp[n][nextPart][parts] != -1:
            return dp[n][nextPart][parts]

        ans = 0
        for i in range(nextPart, n + 1):
            ans += countWaysUtil(n - i, parts - 1, i)

        dp[n][nextPart][parts] = ans
        return ans
    return countWaysUtil(num, kParts, 1)

print(countWays(8, 4))
