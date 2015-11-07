# def basecase(n):
#     if n == 0:
#         return ""
#     if n == 1:
#         return "()"
#
# def parensCenter(n):
#     if n == 0 or n == 1:
#         return basecase(n)
#     return "(" + parens(n - 1) + ")"
#
# def parensRight(n):
#     if n == 0 or n == 1:
#         return basecase(n)
#     return parensCenter(n - 1) + parensRight(n - 1)
#
# def parensLeft(n):
#     if n == 0 or n == 1:
#         return basecase(n)
#     return parensLeft(n - 1) + parensCenter(n - 1)
#
# def parens(n):
#     return parensLeft(n) + " " + parensCenter(n) + " " + parensRight(n)
import functools

def generateParens(count):
    strings = [''] * count * 2
    newList = []
    addParen(newList, count, count, strings, 0)
    # strs = [''.join(z) for z in newList]
    return newList

def addParen(l, leftRem, rightRem, string, count):
    if (leftRem < 0 or rightRem < leftRem):
        return

    if (leftRem == 0 and rightRem == 0):
        l.append(string)
    else:
        if leftRem > 0:
            string[count] = '('
            addParen(l, leftRem - 1, rightRem, string, count+1)

        if rightRem > leftRem:
            string[count] = ')'
            addParen(l, leftRem, rightRem - 1, string, count+1)

print(generateParens(3))
