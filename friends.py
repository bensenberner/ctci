def frenemy(size, grid, first, last, personIdx, chainIdx, chain):
    # reached the end of the friendship chain
    if chainIdx == len(chain) - 1:
        # if we are at the last person then return True
        if personIdx == last:
            return True
        # if we're at someone else then this didn't work
        else:
            return False
    for i in range(size):
        if grid[personIdx][i] == chain[chainIdx]:
            if frenemy(size, grid, first, last, i, chainIdx + 1, chain):
                return True
    # if we exit the loop then that means that none of the people that this person
    # knows would allow the chain to continue. So, this is a dead end
    return False

def main():
    with open('friendsInput', 'r') as f:
        size = int(f.readline())
        # One Line Wonder
        grid = [list(f.readline().strip()) for s in range(size)]
        first = int(f.readline())
        last = int(f.readline())
        chain = f.readline()
        ans = frenemy(size, grid, first, last, first, 0, chain)
        print(ans)

main()
