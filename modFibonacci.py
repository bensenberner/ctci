import math

A, B, N = 0, 1, 10

seq = [A, B]

i = 2
while i < N:
    seq.append(A**2 + B)
    A = seq[i]
    B = seq[i - 1]
    i += 1

print(seq)
