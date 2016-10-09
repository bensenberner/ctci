def masterMind(computer, guess):
    colors = {color: 0 for color in ['R', 'Y', 'G', 'B']}
    hits = 0
    pseudohits = 0
    for color in computer:
        colors[color] += 1

    for i in range(len(computer)):
        if computer[i] == guess[i]:
            colors[computer[i]] -= 1
            hits += 1

    for color in colors:
        pseudohits += colors[color]
