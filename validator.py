import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Grid import Grid
from math import sqrt

def verify(grid: Grid) -> bool:
    """
    Vérifie si une grille est valide en respectant les règles du Sudoku.
    Une grille est valide si chaque ligne, chaque colonne et chaque sous-carré contient
    exactement les chiffres de 1 à n (taille de la grille).
    """
    size = grid.size
    expected_set = set(range(1, size + 1))

    # Vérifier les lignes
    for row_idx in range(size):
        if set(grid.get_row(row_idx)) != expected_set:
            return False

    # Vérifier les colonnes
    for col_idx in range(size):
        if set(grid.get_col(col_idx)) != expected_set:
            return False

    # Vérifier les sous-carrés
    square_size = int(sqrt(size))
    for row in range(0, size, square_size):
        for col in range(0, size, square_size):
            if set(grid.get_square(row, col)) != expected_set:
                return False

    return True