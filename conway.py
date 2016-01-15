'''
Conway's game of life
input is an nxn board of booleans
rules: if a cell is alive and it has two or three alive neighbors, it
remains alive. Otherwise, it dies.
If a cell is dead and it has exactly three alive neighbors, it comes back
to life. Otherwise, it stays dead.
'''

def conwayNextState(inputBoard):
    # true is alive, false is dead

    n = len(inputBoard)
    outputBoard = [[None for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            count = countAliveNeighbors(inputBoard, i, j, n)

            # current cell is alive
            if inputBoard[i][j]:
                outputBoard[i][j] = True if count is 2 or count is 3 else False

            # current cell is dead
            else:
                outputBoard[i][j] = True if count is 3 else False

    return outputBoard

def countAliveNeighbors(inputBoard, i, j, n):
    count = 0

    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if isValid(x, y, n) and not (i is x and j is y) and inputBoard[x][y]:
                count += 1
    return count

def isValid(x, y, n):
    return False if x < 0 or y < 0 or x > n - 1 or y > n - 1 else True

def main():
    board = [
            [1,0,1,0,1],
            [1,0,1,0,1],
            [1,0,1,0,1],
            [1,1,1,0,1],
            [1,0,1,0,1],
            ]
    for x in range(100):
        for line in board:
            print(line)
        print('\n')
        board = conwayNextState(board)

main()
