import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Grid import Grid
from generator import generate
from validator import verify

print("Début des tests")
grid = Grid(4)
generate(grid)
print(grid)
print("Verification de la grille 4x4... ", end="")
assert verify(grid)
print("Fait")

grid = Grid(9)
generate(grid)
print(grid)
print("Verification de la grille 9x9... ", end="")
assert verify(grid)
print("Fait")

grid = Grid(16)
generate(grid)
print(grid)
print("Verification de la grille 16x16... ", end="")
assert verify(grid)
print("Fait")

print("Fin des tests")
