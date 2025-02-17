from math import sqrt
import random
from models.Grid import Grid

def find_next_empty_mrv(grid, size, square_size):
    """
    Trouve la prochaine case vide en utilisant la heuristique MRV (Minimum Remaining Values),
    c'est-à-dire la case avec le moins d'options possibles.
    """
    min_options = size + 1  # Initialise avec une valeur plus grande que le maximum possible (size)
    best_cell = None  # Variable pour stocker la meilleure case trouvée

    for row in range(size):
        for col in range(size):
            if grid.grid[row][col] == 0:  # Vérifie si la case est vide
                possible_values = {num for num in range(1, size + 1) if is_valid(grid, num, row, col, square_size)}
                num_options = len(possible_values)

                if num_options < min_options:
                    min_options = num_options  # Met à jour le minimum d'options possibles
                    best_cell = (row, col)  # Met à jour la meilleure case

                # Si une case n'a qu'une seule possibilité, on la choisit immédiatement
                if min_options == 1:
                    break  
        if min_options == 1:
            break  

    return best_cell  # Retourne la case la plus contrainte ou None si aucune case vide

def is_valid(grid, num, row, col, square_size):
    """
    Vérifie si un nombre peut être placé dans une cellule donnée.
    """
    # Vérifie si le nombre est déjà présent dans la ligne
    if num in grid.get_row(row):
        return False

    # Vérifie si le nombre est déjà présent dans la colonne
    if num in grid.get_col(col):
        return False

    # Vérifie si le nombre est déjà présent dans le carré correspondant
    square_row = (row // square_size) * square_size
    square_col = (col // square_size) * square_size
    if num in grid.get_square(square_row, square_col):
        return False

    return True  # Retourne True si le nombre peut être placé dans la cellule


def heuristic_method(grid: Grid, player: bool = False):
    """
    Génère un Sudoku valide en remplissant la grille avec des valeurs aléatoires.
    """
    size = grid.size  # Taille de la grille (ex: 4x4, 9x9)
    square_size = int(sqrt(size))  # Taille du sous-carré (ex: 2x2, 3x3)
    stack = []

    current_cell = find_next_empty_mrv(grid, size, square_size)
    if not current_cell:
        return True  # Grille déjà remplie

    stack.append((current_cell, list(range(1, size + 1))))  # Liste des valeurs possibles

    while stack:
        (row, col), possible_values = stack.pop()
        random.shuffle(possible_values)  # Mélange les valeurs pour générer une grille aléatoire

        while possible_values:
            attempt = possible_values.pop()  # Prend une valeur au hasard dans la liste mélangée

            if is_valid(grid, attempt, row, col, square_size):
                grid.grid[row][col] = attempt
                if player and (row, col) not in grid.player_cells:
                    grid.player_cells.append((row, col))
                next_cell = find_next_empty_mrv(grid, size, square_size)

                if not next_cell:
                    return True  # Grille complétée

                stack.append(((row, col), possible_values))  # Sauvegarde les tentatives restantes
                stack.append((next_cell, list(range(1, size + 1))))  # Ajoute la prochaine cellule
                break  # Passe à la cellule suivante

        if not possible_values:
            grid.grid[row][col] = 0  # Annule et revient en arrière si plus d'options
            if player:
                grid.player_cells.pop(grid.player_cells.index((row, col)))

    return False  # Retourne False si impossible

