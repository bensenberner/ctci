from collections import namedtuple
from copy import deepcopy

MAX_BOARD_VALUE = GRID_LENGTH = 9
UNASSIGNED = 0
Position = namedtuple("Position", ["row", "col"])


class GridSolver:
    def __init__(self, grid):
        self.grid = deepcopy(grid)

    def solve(self):
        """
        Finds an unassigned position on the board, attempts to assign a valid number to that
        position.
        :return: True if, given the state of the board at invocation time, we can find an
        assignment for the position that leads to the solution of the board.
        False if there is no valid assignment for this position.
        """
        position = self._find_unassigned_position()
        # no more open positions means the board is complete
        if not position:
            return True
        # attempt to assign numbers to the unassigned position
        for possible_number in range(1, MAX_BOARD_VALUE + 1):
            if self._is_valid_assignment(position, possible_number):
                # attempt an assignment
                self.grid[position.row][position.col] = possible_number
                if self.solve():
                    return True
                # wasn't able to solve the grid with this assignment, so undo it
                self.grid[position.row][position.col] = UNASSIGNED
        return False

    def _find_unassigned_position(self):
        for row in range(GRID_LENGTH):
            for col in range(GRID_LENGTH):
                if self.grid[row][col] is UNASSIGNED:
                    return Position(row=row, col=col)
        return None

    def _is_valid_assignment(self, position, number):
        square_top_left_corner_row = position.row - position.row % 3
        square_top_left_corner_col = position.col - position.col % 3
        return (
            self._is_valid_row_assignment(position.row, number)
            and self._is_valid_column_assignment(position.col, number)
            and self._is_valid_square_assignment(
                square_top_left_corner_row, square_top_left_corner_col, number
            )
        )

    def _is_valid_row_assignment(self, row, number):
        for col in range(GRID_LENGTH):
            if self.grid[row][col] == number:
                return False
        return True

    def _is_valid_column_assignment(self, col, number):
        for row in range(GRID_LENGTH):
            if self.grid[row][col] == number:
                return False
        return True

    def _is_valid_square_assignment(self, top_row, left_col, number):
        for row in range(top_row, top_row + 3):
            for col in range(left_col, left_col + 3):
                if self.grid[row][col] == number:
                    return False
        return True

    def print_board(self):
        for row in self.grid:
            print(row)


def main():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [5, 0, 1, 0, 3, 0, 4, 0, 8],
        [0, 9, 4, 0, 1, 0, 3, 0, 0],
        [0, 0, 7, 0, 0, 3, 0, 0, 0],
        [0, 2, 8, 9, 0, 5, 7, 3, 0],
        [0, 0, 0, 1, 0, 0, 6, 0, 0],
        [0, 0, 5, 0, 2, 0, 8, 7, 0],
        [9, 0, 2, 0, 6, 0, 5, 0, 4],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    solver = GridSolver(grid)
    print("Initial board:")
    solver.print_board()
    if solver.solve():
        print("Solution:")
        solver.print_board()
    else:
        print("No solution.")


if __name__ == "__main__":
    main()
