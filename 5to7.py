import random
from collections import Counter

def rand7():
    random.seed()
    randSum = 0
    for i in range(8):
        randSum += rand5()
    return randSum % 7 + 1


def rand5():
    random.seed()
    return random.randint(1,5)

def main():
    c = Counter()
    for i in range(1000):
        c[rand7()] += 1
    print(c)

main()
