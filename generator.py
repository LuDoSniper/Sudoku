import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Grid import Grid
from math import sqrt
import random

def is_valid(grille, size, ligne, col, num):
    """
    Vérifie si le placement du chiffre 'num' dans la case (ligne, col) est valide.
    """
    # Vérifie la ligne
    if num in grille[ligne]:
        return False

    # Vérifie la colonne
    if num in [grille[i][col] for i in range(size)]:
        return False

    # Vérifie le carré
    square_size = int(sqrt(size))
    start_ligne, start_col = square_size * (ligne // square_size), square_size * (col // square_size)
    for i in range(square_size):
        for j in range(square_size):
            if grille[start_ligne + i][start_col + j] == num:
                return False

    return True

def generate(grid: Grid) -> bool:
    for line in range(grid.size):
        for col in range(grid.size):
            if grid.grid[line][col] == 0:
                
                nums = list(range(1, grid.size + 1))
                random.shuffle(nums)

                for num in nums:
                    if is_valid(grid.grid, grid.size, line, col, num):
                        grid.grid[line][col] = num
                        if generate(grid):
                            return True
                        grid.grid[line][col] = 0  # Backtracking
                return False  # Aucun chiffre ne fonctionne
    return True
