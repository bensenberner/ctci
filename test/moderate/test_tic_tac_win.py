from unittest import TestCase

from moderate.tic_tac_win import Board, Piece


class Test(TestCase):
    def test_horizontal(self):
        board = Board(3)
        self.assertFalse(board.place_piece(0, 0, Piece.X))
        self.assertFalse(board.place_piece(0, 1, Piece.X))
        self.assertTrue(board.place_piece(0, 2, Piece.X))

    def test_vertical(self):
        board = Board(3)
        self.assertFalse(board.place_piece(0, 0, Piece.X))
        self.assertFalse(board.place_piece(1, 0, Piece.X))
        self.assertTrue(board.place_piece(2, 0, Piece.X))

    def test_asc_diag(self):
        board = Board(3)
        self.assertFalse(board.place_piece(2, 0, Piece.X))
        self.assertFalse(board.place_piece(1, 1, Piece.X))
        self.assertTrue(board.place_piece(0, 2, Piece.X))

    def test_desc_diag(self):
        board = Board(3)
        self.assertFalse(board.place_piece(0, 0, Piece.X))
        self.assertFalse(board.place_piece(1, 1, Piece.X))
        self.assertTrue(board.place_piece(2, 2, Piece.X))

    def test_1x1(self):
        board = Board(1)
        self.assertTrue(board.place_piece(0, 0, Piece.O))

    def test_50(self):
        n = 50
        board = Board(n)
        for row_idx in range(n):
            for col_idx in range(n - row_idx - 1):
                self.assertFalse(board.place_piece(row_idx, col_idx, Piece.X))
        self.assertTrue(board.place_piece(0, n - 1, Piece.X))
