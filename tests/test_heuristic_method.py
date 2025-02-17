import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solvers.ite_heuristic import heuristic_method
from models.Grid import Grid

class TestTechniqueHeuristique(unittest.TestCase):

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

    def test_technique_heuristique_valid_grid(self):
        self.assertTrue(heuristic_method(self.sudoku_grid))

    def test_technique_heuristique_invalid_grid(self):
        self.assertFalse(heuristic_method(self.sudoku_grid_impossible))


if __name__ == '__main__':
    unittest.main()
