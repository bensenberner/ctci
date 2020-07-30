"""
Design an algorithm to figure out if someone has won a game of tic-tac-toe
--------------------
If the tic-tac-toe board is an n x n board, then we would simply iterate through the board, row by row, col by col,
and each diag, counting the number of Xs and Os, seeing which one has n instances.

We'll a board and all we gotta do is check, when a piece is placed, that it isn't placed somewhere that's already occupied
or off the grid.
Then, instead of the naive search, we can instead keep track of the counts for X and O for each row, col, and diagonal. Adding
to a counter takes O(1) time, accessing it takes constant time, and so checking win condition takes constant time, at the cost of O(n) additional storage
"""
from collections import Counter, defaultdict
from enum import Enum


class Piece(Enum):
    X = "X"
    O = "O"


class Board:
    def __init__(self, n):
        self.n = n
        self._board = [[None for _ in range(n)] for __ in range(n)]
        self._row_counters = defaultdict(lambda: Counter())
        self._col_counters = defaultdict(lambda: Counter())
        self._diag_asc_counter = Counter()  # /
        self._diag_desc_counter = Counter()  # \

    def _is_within_board(self, row_idx, col_idx):
        return 0 <= row_idx < self.n and 0 <= col_idx < self.n

    def place_piece(self, row_idx: int, col_idx: int, piece: Piece) -> bool:
        """
        :return: True if placing this piece wins the game. False if it didn't win the game.
        :raises: AssertionError if the piece cannot be placed
        """
        if not self._is_within_board(row_idx, col_idx):
            raise AssertionError("Cannot place piece outside board area")
        if self._board[row_idx][col_idx] is not None:
            raise AssertionError("Cannot play on occupied space")
        self._board[row_idx][col_idx] = piece

        counters_to_modify = [
            self._row_counters[row_idx],
            self._col_counters[col_idx],
        ]
        if row_idx + col_idx + 1 == self.n:
            counters_to_modify.append(self._diag_asc_counter)
        if row_idx == col_idx:
            counters_to_modify.append(self._diag_desc_counter)

        for counter in counters_to_modify:
            counter[piece] += 1
            if counter[piece] == self.n:
                return True
        return False
