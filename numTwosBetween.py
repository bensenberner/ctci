def cumulativeNumTwos(num):
    res = 0
    for i in range(num):
        res += numTwos(i)
    return res

def numTwos(num):
    strNum = str(num)
    i = 0
    for n in strNum:
        if n == '2':
            i += 1
    return i

print(cumulativeNumTwos(10000000))
