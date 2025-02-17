import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from solvers.backtracking_recursif import backtracking_recursif
from solvers.heuristic_method import heuristic_method
from tools.get_time import get_time
from tools.generator import generate_full, calibrate
from models.Grid import Grid

grid = Grid(16)
generate_full(grid)
calibrate(grid, "hard")

print(get_time(backtracking_iteratif_pile, grid))
print(get_time(backtracking_recursif, grid))
print(get_time(heuristic_method, grid))