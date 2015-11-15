import ctypes

def nextNum(num):
    v = ctypes.c_ulong(num)
    t = (v | (v - ctypes.c_ulong(1))) + ctypes.c_ulong(1)
    w = t | ((((t & -t) / (v & -v)) >> ctypes.c_ulong(1)) - ctypes.c_ulong(1))
    return w

print(nextNum(2))
