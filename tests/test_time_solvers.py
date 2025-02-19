import sys
import os
import timeit
import copy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Grid import Grid
from models.SudokuGraphe import SudokuGraphe
from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from solvers.backtracking_recursif import backtracking_recursif
from solvers.coloration_graphe import colorier_sudoku
from tools.generator import generate_full, calibrate
from tools.dessiner_graphe_sudoku import dessiner_graphe_sudoku

grid = Grid(16)
generate_full(grid)
calibrate(grid, "normal")  # Calibrage à des fins visuelles

print(grid)
grid1 = copy.deepcopy(grid)
grid2 = copy.deepcopy(grid)
grid3 = copy.deepcopy(grid)
grid4 = copy.deepcopy(grid)

recursif = timeit.timeit(lambda: backtracking_recursif(grid1, use_heuristic=False, use_random=False), number=1)
print(f"Temps d'exécution pour le recursif: {recursif:.2f} secondes")

recursif_heuristique = timeit.timeit(lambda: backtracking_recursif(grid2, use_heuristic=True, use_random=False), number=1)
print(f"Temps d'exécution pour le recursif heuristique: {recursif_heuristique:.2f} secondes")

iteratif = timeit.timeit(lambda: backtracking_iteratif_pile(grid3, use_heuristic=False, use_random=False), number=1)
print(f"Temps d'exécution pour l'iteratif: {iteratif:.2f} secondes")

iteratif_heurisique = timeit.timeit(lambda: backtracking_iteratif_pile(grid4, use_heuristic=True, use_random=False), number=1)
print(f"Temps d'exécution pour l'iteratif heuristique: {iteratif_heurisique:.2f} secondes")

# colorier_sudoku(grid)

# dessiner_graphe_sudoku(SudokuGraphe(grid))



