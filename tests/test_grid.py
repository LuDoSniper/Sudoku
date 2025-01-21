import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Grid import Grid

grid = Grid(grid=[
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

print("Début des tests")
assert grid.get_row(0) == [1, 2, 3, 0, 0, 0, 0, 0, 0]
assert grid.get_row(1) == [4, 5, 6, 0, 0, 0, 0, 0, 0]
assert grid.get_row(2) == [7, 8, 9, 0, 0, 0, 0, 0, 0]

assert grid.get_col(0) == [1, 4, 7, 0, 0, 0, 0, 0, 0]
assert grid.get_col(1) == [2, 5, 8, 0, 0, 0, 0, 0, 0]
assert grid.get_col(2) == [3, 6, 9, 0, 0, 0, 0, 0, 0]

assert grid.get_square(0, 0) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert grid.get_square(0, 3) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Fin des tests")
