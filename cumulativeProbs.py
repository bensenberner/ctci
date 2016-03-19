import random

def randomN(probs):
    random.seed()
    normalizedProbabilities = [x * 100 for x in probs]
    randNum = random.randint(0, 99)
    index = 0
    while randNum > 0:
        randNum -= normalizedProbabilities[index]
        index += 1

    while probs[index - 1] == 0:
        index -= 1

    return index - 1

for i in range(10):
    print(randomN([0.31, 0, 0.69]))
