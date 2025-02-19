import random
from models.Grid import Grid
from tools.find_next_empty import find_next_empty
from tools.find_next_empty import find_next_empty_mrv
from tools.is_valid import is_valid

def backtracking_iteratif_pile(grid : Grid, player: bool = False, indice: bool = False, use_heuristic: bool = False) -> bool: 
    """
    Solveur de Sudoku utilisant le backtracking itératif avec pile, renvois True si la grille est résolue, False sinon.
    """
    size = grid.size

    # Initialiser les "logs" des actions effectuées pour l'indice
    if indice:
        logs = []

    # Initialiser la pile pour gérer les états
    stack = []

    # Trouver la première cellule vide
    if use_heuristic:
        current_cell = find_next_empty_mrv(grid, size)
    else:
        current_cell = find_next_empty(grid, size)

    if not current_cell:
        return True  # La grille est déjà complète

    # Ajouter le premier état à la pile
    possible_values = list(range(1, size + 1))
    random.shuffle(possible_values)
    stack.append((current_cell, possible_values))  # (position, valeurs possibles mélangées)

    while stack:
        # Récupérer la cellule actuelle et les valeurs possibles
        (row, col), possible_values = stack.pop()

        # Essayer les valeurs possibles pour la cellule actuelle
        while possible_values:
            attempt = possible_values.pop()
            if is_valid(grid, attempt, row, col):
                # Placer le numéro dans la cellule
                grid.grid[row][col] = attempt
                if player and (row, col) not in grid.player_cells:
                    grid.player_cells.append((row, col))
                if indice and (row, col) not in logs:
                    logs.append((row, col))

                # Trouver la prochaine cellule vide
                if use_heuristic:
                    next_cell = find_next_empty_mrv(grid, size)
                else:
                    next_cell = find_next_empty(grid, size)
                

                if not next_cell:
                    # Ne laisser qu'une seule case remplie pour l'indice
                    if indice:
                        if len(logs) > 1:
                            random.shuffle(logs)
                            for log in logs[1:]:
                                grid.grid[log[0]][log[1]] = 0
                        grid.indice_cells.append((logs[0][0], logs[0][1]))

                    return True  # Résolution terminée

                # Ajouter l'état suivant à la pile
                stack.append(((row, col), possible_values))  # Sauvegarde de l'état actuel
                new_possible_values = list(range(1, size + 1))
                random.shuffle(new_possible_values)
                stack.append((next_cell, new_possible_values))
                break

        # Si aucune tentative ne fonctionne, réinitialiser la cellule
        if not possible_values:
            grid.grid[row][col] = 0
            if player and (row, col) in grid.player_cells:
                grid.player_cells.pop(grid.player_cells.index((row, col)))
            if indice and (row, col) in logs:
                logs.pop(logs.index((row, col)))

    return False  # Aucune solution trouvée
