import ctypes

# TODO: fix it
def nextNum(num):
    v = ctypes.c_ulong(num)
    t = (v | (v - ctypes.c_ulong(1))) + ctypes.c_ulong(1)
    w = t | ((((t & -t) / (v & -v)) >> ctypes.c_ulong(1)) - ctypes.c_ulong(1))
    return w

def main():
    num = 2
    for i in range(10):
        print(num)
        num = nextNum(num)

if __name__ == "__main__":
    main()
