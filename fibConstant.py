from __future__ import division
import math

def fib(n):
    sqrt5 = math.sqrt(5)
    phi = (sqrt5 + 1) / 2
    return int(phi ** n / sqrt5 + 0.5)

print(fib(5))
