import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from resolveurs.backtracking_iteratif_pile import backtracking_iteratif_pile
from models.Grid import Grid

test_grid_4x4 = [
    [3, 4, 2, 0],
    [1, 2, 0, 3],
    [4, 0, 0, 2],
    [0, 0, 3, 4]
]

sudoku_grid = Grid(4, grid=test_grid_4x4)

print("Grille initiale :")
print(sudoku_grid)

if backtracking_iteratif_pile(sudoku_grid):
    print("Grille résolue :")
    print(sudoku_grid)
else:
    print("Impossible de résoudre la grille.")
