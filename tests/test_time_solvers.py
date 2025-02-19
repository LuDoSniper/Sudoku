import sys
import os
import timeit
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Grid import Grid
from models.SudokuGraphe import SudokuGraphe
from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from solvers.backtracking_recursif import backtracking_recursif
from solvers.ite_heuristic import ite_heuristic_method
from solvers.recu_heuristic import recu_heuristic_method
from solvers.coloration_graphe import colorier_sudoku
from tools.generator import generate_full, calibrate

grid = Grid(4)
generate_full(grid)
calibrate(grid, "easy")  # Calibrage à des fins visuelles

# recursif = timeit.timeit(lambda: backtracking_recursif(grid), number=1)
# print(f"Temps d'exécution pour le recursif: {recursif:.2f} secondes")

# iteratif = timeit.timeit(lambda: backtracking_iteratif_pile(grid), number=1)
# print(f"Temps d'exécution pour l'iteratif: {iteratif:.2f} secondes")

# heuristique_ite = timeit.timeit(lambda: ite_heuristic_method(grid), number=1)
# print(f"Temps d'exécution pour le heuristique: {heuristique_ite:.2f} secondes")

# heuristique_recu = timeit.timeit(lambda: recu_heuristic_method(grid), number=1)
# print(f"Temps d'exécution pour le heuristique: {heuristique_recu:.2f} secondes")


sudoku_graphe = SudokuGraphe(grid)
colorier_sudoku(sudoku_graphe)

