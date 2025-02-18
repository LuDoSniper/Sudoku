from math import sqrt
from tools.find_next_empty import find_next_empty
from tools.is_valid import is_valid

def backtracking_iteratif_pile(grid, player: bool = False):
    size = grid.size
    square_size = int(sqrt(size))

    # Initialiser la pile pour gérer les états
    stack = []

    # Trouver la première cellule vide
    current_cell = find_next_empty(grid, size)
    if not current_cell:
        return True  # La grille est déjà complète

    # Ajouter le premier état à la pile
    stack.append((current_cell, 1))  # (position, tentative actuelle)

    while stack:
        # Récupérer la cellule actuelle et la tentative
        (row, col), attempt = stack.pop()

        # Indicateur pour savoir si une tentative a réussi
        solved = False

        # Essayer les valeurs possibles pour la cellule actuelle
        while attempt <= size and not solved:
            if is_valid(grid, attempt, row, col, square_size):
                # Placer le numéro dans la cellule
                grid.grid[row][col] = attempt
                if player and (row, col) not in grid.player_cells:
                    grid.player_cells.append((row, col))

                # Trouver la prochaine cellule vide
                next_cell = find_next_empty(grid, size)

                if not next_cell:
                    return True  # Résolution terminée

                # Ajouter l'état suivant à la pile
                stack.append(((row, col), attempt + 1))
                stack.append((next_cell, 1))
                solved = True
            else:
                attempt += 1

        # Si aucune tentative ne fonctionne, réinitialiser la cellule
        if not solved:
            grid.grid[row][col] = 0
            if player:
                grid.player_cells.pop(grid.player_cells.index((row, col)))

    return False  # Aucune solution trouvée
