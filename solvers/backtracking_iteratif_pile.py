from math import sqrt

def find_next_empty(grid, size):
    # Trouver la première cellule vide (valeur 0) à résoudre
    for row in range(size):
        for col in range(size):
            if grid.grid[row][col] == 0:
                return row, col
    return None
#Meilleur cas : O(1)
#Pire cas : O(n^2)

def is_valid(grid, num, row, col, square_size):
    # Vérifier si un numéro peut être placé dans une cellule
    # Vérifier la ligne
    if num in grid.get_row(row):
        return False

    # Vérifier la colonne
    if num in grid.get_col(col):
        return False

    # Vérifier le carré
    square_row = (row // square_size) * square_size
    square_col = (col // square_size) * square_size
    if num in grid.get_square(square_row, square_col):
        return False

    return True
#Meilleur cas : O(1)
#Pire cas : O(n)

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
                if player:
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

    return False  # Aucune solution trouvée
#Meilleur cas : O(1)
#Pire cas : O(n^4)