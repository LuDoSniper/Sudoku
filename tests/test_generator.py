import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Grid import Grid
from tools.generator import generate_full, calibrate
from tools.validator import verify

print("Début des tests")



# Test de la grille 4x4
grid = Grid(4)
generate_full(grid)
print(grid)
print("Verification de la grille 4x4... ", end="")
assert verify(grid)
print("Fait")

# Calibrage de la grille (mode facile) - ne fait pas partie du test, uniquement à des fins visuelles
calibrate(grid, "easy")
print(grid)



# Test de la grille 9x9
grid = Grid(9)
generate_full(grid)
print(grid)
print("Verification de la grille 9x9... ", end="")
assert verify(grid)
print("Fait")

# Calibrage de la grille (mode facile) - ne fait pas partie du test, uniquement à des fins visuelles
calibrate(grid, "easy")
print(grid)



# Test de la grille 16x16
grid = Grid(16)
generate_full(grid)
print(grid)
print("Verification de la grille 16x16... ", end="")
assert verify(grid)
print("Fait")

# Calibrage de la grille (mode facile) - ne fait pas partie du test, uniquement à des fins visuelles
calibrate(grid, "easy")
print(grid)



print("Fin des tests")
