class Board:
    def __init__(self, size):
        self.board = [[None for x in range(size)] for y in range(size)]
        self.fill_count = 0

def check_idxes(board, curr_char, idxes):
    for i, j in idxes:
        if board.board[i][j] != curr_char:
            return False
    return True

def check_diagonal(board, curr_char, isTopLeftToBottomRight):
    # TODO: consolidate
    idxes = [(i, i) for i in range(3)] if isTopLeftToBottomRight else [(2, 0), (1, 1), (0, 2)]
    return check_idxes(board, curr_char, idxes)

def check_line(board, curr_char, idx, isRow):
    idxes = [(idx, other_idx) for other_idx in range(3)] if isRow else [(other_idx, idx) for other_idx in range(3)]
    return check_idxes(board, curr_char, idxes)

def winning_position(board, curr_char, i, j):
    # in the middle, check both diagonals
    loc = (i, j)
    if i == j:
        if (check_diagonal(board, curr_char, True) or check_diagonal(board, curr_char, False)):
            return True
    # check left diagonal if necessary
    if loc in {(0, 0), (2, 2)}:
        if check_diagonal(board, curr_char, True):
            return True
    # check right diagonal if necessary
    if loc in {(2, 0), (0, 2)}:
        if check_diagonal(board, curr_char, False):
            return True
    # row
    if check_line(board, curr_char, i, True):
        return True

    # column
    if check_line(board, curr_char, j, False):
        return True

    return False

def move(board, isX):
    i, j = get_position_from_input("Please enter a valid position!\n")
    while board.board[i][j] is not None:
        i, j = get_position_from_input("Invalid position. Please enter a valid position!\n")

    curr_char = "x" if isX else "o"
    board.board[i][j] = curr_char
    board.fill_count += 1

    if winning_position(board, curr_char, i, j):
        print("Congratulations, {} won!".format(curr_char))
        return True
    if board.fill_count == 9:
        print("The game ended in a tie")
        return True

    return False

def get_position_from_input(input_prompt):
    # TODO: do error checking
    i, j = [int(val) for val in input("Please enter a valid position!\n").split(',')]
    return i, j

def print_board(board):
    for line in board.board:
        print(line)
    print('_______________')

if __name__ == "__main__":
    board = Board(3)
    print_board(board)
    isX = True
    while not move(board, isX):
        print_board(board)
        isX = not isX
    print_board(board)
