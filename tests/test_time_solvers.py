import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from solvers.backtracking_recursif import backtracking_recursif
from solvers.ite_heuristic import ite_heuristic_method
from solvers.recu_heuristic import recu_heuristic_method
from tools.get_time import get_time
from tools.generator import generate_full, calibrate
from models.Grid import Grid
import timeit

grid = Grid(16)
generate_full(grid)
calibrate(grid, "easy")  # Calibrage à des fins visuelles

# recursif = timeit.timeit(lambda: backtracking_recursif(grid), number=1)
# print(f"Temps d'exécution pour le recursif: {recursif:.2f} secondes")

# iteratif = timeit.timeit(lambda: backtracking_iteratif_pile(grid), number=1)
# print(f"Temps d'exécution pour l'iteratif: {iteratif:.2f} secondes")

heuristique = timeit.timeit(lambda: ite_heuristic_method(grid), number=1)
print(f"Temps d'exécution pour le heuristique: {heuristique:.2f} secondes")
# print(f"Validité de la grille: {heuristic_method(grid)}")