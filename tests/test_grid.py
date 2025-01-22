import unittest
import sys
import os

# Ajoute le chemin du projet au PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Grid import Grid

class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(grid=[
            [1, 2, 3, 0, 0, 0, 0, 0, 0],
            [4, 5, 6, 0, 0, 0, 0, 0, 0],
            [7, 8, 9, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])

    def test_get_row(self):
        self.assertEqual(self.grid.get_row(0), [1, 2, 3, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.grid.get_row(1), [4, 5, 6, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.grid.get_row(2), [7, 8, 9, 0, 0, 0, 0, 0, 0])

    def test_get_col(self):
        self.assertEqual(self.grid.get_col(0), [1, 4, 7, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.grid.get_col(1), [2, 5, 8, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.grid.get_col(2), [3, 6, 9, 0, 0, 0, 0, 0, 0])

    def test_get_square(self):
        self.assertEqual(self.grid.get_square(0, 0), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(self.grid.get_square(0, 3), [0, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
