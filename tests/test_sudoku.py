from collections import defaultdict
import unittest

import sys
from pathlib import Path
two_up = Path(__file__).resolve().parents[1]
sys.path.append(str(two_up))

from src.sudoku import run

class TestSudoku(unittest.TestCase):
    board = [[0 for j in range(9)] for i in range(9)]
    board[0] = [3, 1, 6, 5, 7, 8, 4, 9, 2]
    board[1] = [5, 2, 9, 1, 3, 4, 7, 6, 8]
    board[2] = [4, 8, 7, 6, 2, 9, 5, 3, 1]
    board[3] = [2, 6, 3, 4, 1, 5, 9, 8, 7]
    board[4] = [9, 7, 4, 8, 6, 3, 1, 2, 5]
    board[5] = [8, 5, 1, 7, 9, 2, 6, 4, 3]
    board[6] = [1, 3, 8, 9, 4, 7, 2, 5, 6]
    board[7] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def test_empty_board(self):
        self.board = [[0 for j in range(9)] for i in range(9)]
        sudoku_board = run(self.board)
        is_valid = self.solution_valid(sudoku_board)
        self.assertTrue(is_valid, True)

    def test_completely_filled_valid_board(self):
        self.board[7] = [6, 9, 2, 3, 5, 1, 8, 7, 4]
        self.board[8] = [7, 4, 5, 2, 8, 6, 3, 1, 9]
        sudoku_board = run(self.board)
        is_valid = self.solution_valid(sudoku_board)
        self.assertTrue(is_valid, True)

    def test_half_filled_board(self):
        self.board[7] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        sudoku_board = run(self.board)
        is_valid = self.solution_valid(sudoku_board)
        self.assertTrue(is_valid, True)

    def test_incorrect_board(self):
        self.board[7] = [1, 9, 2, 3, 5, 1, 8, 7, 4]
        sudoku_board = run(self.board)
        is_valid = self.solution_valid(sudoku_board)
        self.assertFalse(is_valid, False)


    def solution_valid(self, board):
        # check row and column is distict no or not?!
        rows = defaultdict(int)
        columns = defaultdict(int)
        squares = defaultdict(int)
        
        for i in range(9):
            rows.clear()
            columns.clear()
            squares.clear()

            for j in range(9):
                if board[i][j] is not None:
                    columns[board[i][j]] += 1
                    if columns[board[i][j]] > 1:
                        return False

                if board[j][i] is not None:
                    rows[board[j][i]] += 1
                    if rows[board[j][i]] > 1:
                        return False

                new_j = (i*3 + j % 3) % 9
                new_i = (i//3)*3 + j//3
                if squares[board[new_i][new_j]] is not None:
                    squares[board[new_i][new_j]] += 1
                    if squares[board[new_i][new_j]] > 1:
                        return False
        return True


if __name__ == '__main__':
    unittest.main()


