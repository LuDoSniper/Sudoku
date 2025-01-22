import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from models.Grid import Grid

class TestBacktrackingIteratifPile(unittest.TestCase):

    def setUp(self):
        self.test_grid_4x4 = [
            [3, 4, 2, 0],
            [1, 2, 0, 3],
            [4, 0, 0, 2],
            [0, 0, 3, 4]
        ]

        self.test_grid_4x4_impossible = [
            [3, 4, 2, 0],
            [1, 0, 2, 3],
            [4, 0, 0, 2],
            [0, 0, 3, 4]
        ]

        # Initialisation des grilles avec le modèle Grid
        self.sudoku_grid = Grid(4, grid=self.test_grid_4x4)
        self.sudoku_grid_impossible = Grid(4, grid=self.test_grid_4x4_impossible)

    def test_backtracking_iteratif_pile_valid_grid(self):
        self.assertTrue(backtracking_iteratif_pile(self.sudoku_grid))

    def test_backtracking_iteratif_pile_invalid_grid(self):
        self.assertFalse(backtracking_iteratif_pile(self.sudoku_grid_impossible))


if __name__ == '__main__':
    unittest.main()
