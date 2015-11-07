#!/usr/bin/env python
import os, sys

def solve_coin_change(coins, value):
    """A dynamic solution to the coin change problem"""

    table = [None for x in range(value + 1)]
    table[0] = []
    for i in range(1, value + 1):
        for coin in coins:
            if coin > i: continue
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
                if table[i - coin] != None:
                    table[i] = table[i - coin][:]
                    table[i].append(coin)

    if table[-1] != None:
        print('%d coins: %s' % (len(table[-1]), table[-1]))
    else:
        print('No solution possible')


if __name__ == '__main__':
    def usage():
        sys.stderr.write('Usage: %s value\n' % os.path.basename(sys.argv[0]))
        sys.exit(1)

    # Modify this to alter the denominations of coins
    coins = [1, 6, 9, 20]

    if len(sys.argv) != 2:
        usage()
    try:
        value = int(sys.argv[1])
    except ValueError:
        usage()
    solve_coin_change(coins, value)
