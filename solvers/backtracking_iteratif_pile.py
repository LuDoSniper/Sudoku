import random
from tools.find_next_empty import find_next_empty
from tools.is_valid import is_valid

def backtracking_iteratif_pile(grid, player: bool = False):
    size = grid.size

    # Initialiser la pile pour gérer les états
    stack = []

    # Trouver la première cellule vide
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

                # Trouver la prochaine cellule vide
                next_cell = find_next_empty(grid, size)

                if not next_cell:
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
            if player:
                grid.player_cells.pop(grid.player_cells.index((row, col)))

    return False  # Aucune solution trouvée
