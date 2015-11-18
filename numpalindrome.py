def upsideNum(number):
    s = str(number)
    isOdd = True if len(s) % 2 == 1 else False

    validNums = ['0', '1', '2', '5', '8']
    # 189691

    if isOdd and not s[int(len(s)/2)] in validNums:
        return False

    for i in range(0, (int(len(s)/2))):
        if (s[i] == s[len(s) - i - 1] and s[i] in validNums):
            continue
        if (s[i] == '6' and s[len(s) - i - 1] == '9' or
                s[i] == '9' and s[len[s] - i - 1] == '6'):
            continue
        else:
            return False

    return True

print(upsideNum(10101))
