import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Grid import Grid
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

def generate_full(grid: Grid) -> bool:
    for line in range(grid.size):
        for col in range(grid.size):
            if grid.grid[line][col] == 0:
                
                nums = list(range(1, grid.size + 1))
                random.shuffle(nums)

                for num in nums:
                    if is_valid(grid.grid, grid.size, line, col, num):
                        grid.grid[line][col] = num
                        if generate_full(grid):
                            return True
                        grid.grid[line][col] = 0  # Backtracking
                return False  # Aucun chiffre ne fonctionne
    return True

def calibrate(grid: Grid, difficulty: str) -> None:
    difficulties = {
        "easy": (0.3, 0.4),
        "normal": (0.4, 0.5),
        "hard": (0.5, 0.6)
    }
    
    size = grid.size
    total_cells = size ** 2
    cells_to_remove = random.randint(int(total_cells * difficulties[difficulty][0]), int(total_cells * difficulties[difficulty][1]))
    
    removed = 0
    while removed < cells_to_remove:
        line = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if grid.grid[line][col] != 0:  # Vérifie que la case n'est pas déjà vide
            grid.grid[line][col] = 0
            removed += 1


def generate(grid: Grid, difficulty: str, alg: callable = None, **kwargs) -> None:
    if alg is None:
        generate_full(grid)
    else:
        alg(grid, **kwargs)

    calibrate(grid, difficulty)
