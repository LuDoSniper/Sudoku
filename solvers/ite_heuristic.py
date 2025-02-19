import random
from models.Grid import Grid
from tools.find_next_empty import find_next_empty_mrv
from tools.is_valid import is_valid


def ite_heuristic_method(grid: Grid, player: bool = False, indice: bool = False):
    """
    Génère un Sudoku valide en remplissant la grille avec des valeurs aléatoires.
    """
    size = grid.size  # Taille de la grille (ex: 4x4, 9x9)
    stack = []

    if indice:
        logs = []

    current_cell = find_next_empty_mrv(grid, size)
    if not current_cell:
        return True  # Grille déjà remplie

    stack.append((current_cell, list(range(1, size + 1))))  # Liste des valeurs possibles

    while stack:
        (row, col), possible_values = stack.pop()
        random.shuffle(possible_values)  # Mélange les valeurs pour générer une grille aléatoire

        while possible_values:
            attempt = possible_values.pop()  # Prend une valeur au hasard dans la liste mélangée

            if is_valid(grid, attempt, row, col):
                grid.grid[row][col] = attempt
                if player and (row, col) not in grid.player_cells:
                    grid.player_cells.append((row, col))
                if indice and (row, col) not in logs:
                    logs.append((row, col))
                next_cell = find_next_empty_mrv(grid, size)

                if not next_cell:
                    if indice:
                        if len(logs) > 1:
                            random.shuffle(logs)
                            for log in logs[1:]:
                                grid.grid[log[0]][log[1]] = 0
                        grid.indice_cells.append((logs[0][0], logs[0][1]))

                    return True  # Grille complétée

                stack.append(((row, col), possible_values))  # Sauvegarde les tentatives restantes
                stack.append((next_cell, list(range(1, size + 1))))  # Ajoute la prochaine cellule
                break  # Passe à la cellule suivante

        if not possible_values:
            grid.grid[row][col] = 0  # Annule et revient en arrière si plus d'options
            if player and (row, col) in grid.player_cells:
                grid.player_cells.pop(grid.player_cells.index((row, col)))
            if indice and (row, col) in logs:
                logs.pop(logs.index((row, col)))

    return False  # Retourne False si impossible  
