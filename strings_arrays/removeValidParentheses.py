def isValidExpr(string):
    count = 0
    for s in string:
        if s == "(":
            count += 1
        elif s == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0


memo = dict()


def solution(s, memo):
    if s in memo:
        return memo[s]

    if isValidExpr(s):
        res = ({s}, 0)
        memo[s] = res
        return res

    bestShortenings = set()
    minNumRemovals = float('inf')
    for idx in range(len(s)):
        currShortenings, currRemovals = solution(s[:idx] + s[idx+1:], memo)
        currRemovals += 1
        if currRemovals < minNumRemovals:
            minNumRemovals = currRemovals
            bestShortenings = currShortenings
        elif currRemovals == minNumRemovals:
            bestShortenings |= currShortenings

    res = (bestShortenings, minNumRemovals)
    memo[s] = res
    return res


def removeInvalidParentheses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    memo = dict()
    bestShortening, minNumRemoved = solution(s, memo)
    return list(bestShortening) if bestShortening else [""]


string = "()((c))()())(m)))()("
print(removeInvalidParentheses(string))