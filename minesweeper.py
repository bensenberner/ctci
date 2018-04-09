import random

def isValid(i, j, m, n):
    return i >= 0 and i < m and j >= 0 and j < n

def reveal(i, j, board, visited, visible, flags, setFlag, m, n):
    if not isValid(i, j, m, n) or visited[i][j]: return False
    visited[i][j] = True
    if setFlag:
        visible[i][j] = "f"
        flags.add((i, j))
        return False
    visible[i][j] = board[i][j]
    if board[i][j] == "b": return True
    if board[i][j] != 0: return False
    for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        reveal(i + delta_y, j + delta_x, board, visited, visible, setFlag, m, n)

def buildBoard(m, n, num_bombs = 1):
    bomb_locs = set(zip(
        random.sample(range(m), num_bombs),
        random.sample(range(n), num_bombs)))
    board = [[0 for x in range(n)] for y in range(m)]
    for bomb_i, bomb_j in bomb_locs:
        for i in range(bomb_i-1, bomb_i+2):
            for j in range(bomb_j-1, bomb_i+2):
                if not isValid(i, j, m, n) or board[i][j] == "b":
                    continue
                if bomb_i == i and bomb_j == j:
                    board[i][j] = "b"
                    continue
                board[i][j] += 1
    return board, bomb_locs

def printBoard(visible):
    for line in visible:
        print(line)

def main():
    m, n, num_bombs = [int(x) for x in input("Please enter m,n,num_bombs\n").split(',')]
    board, bomb_locs = buildBoard(m, n, num_bombs)
    visited = [[False for x in range(n)] for y in range(m)]
    visible = [["#" for x in range(n)] for y in range(m)]
    flags = set()
    while True:
        printBoard(visible)
        i_str, j_str, flag_str = input("[i],[j],f to set a flag, [i],[j],s to select\n").split(',')
        setFlag = True if flag_str == "f" else False
        i, j = int(i_str), int(j_str)
        if reveal(i, j, board, visited, visible, flags, setFlag, m, n):
            print("You lost!!")
            break
        if bomb_locs == flags:
            print("You win!!")
            break

main()
