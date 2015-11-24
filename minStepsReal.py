def steps(source, step, dest):
    if abs(source) > dest: return float('inf')
    if source == dest: return step

    pos = steps(source + step + 1, step + 1, dest)
    neg = steps(source - step - 1, step + 1, dest)

    return min(pos, neg)

print(steps(0, 0, 11))
