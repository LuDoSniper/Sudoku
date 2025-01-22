from math import sqrt

def is_valid(grid, num, row, col, square_size):
    # Vérifier la ligne
    if num in grid.get_row(row):
        return False

    # Vérifier la colonne
    if num in grid.get_col(col):
        return False

    # Vérifier le carré
    if num in grid.get_square(row, col):
        return False

    return True

def find_mrv_cell(grid):
    """
    Trouve la cellule vide avec le moins de possibilités (Minimum Remaining Value).
    Renvoie une cellule (row, col) ou None si aucune cellule vide.
    """
    size = grid.size
    square_size = int(sqrt(size))
    min_possibilities = float('inf')
    mrv_cell = None

    for row in range(size):
        for col in range(size):
            if grid.grid[row][col] == 0:  # Cellule vide
                possibilities = [
                    num for num in range(1, size + 1)
                    if is_valid(grid, num, row, col, square_size)
                ]
                if len(possibilities) < min_possibilities:
                    min_possibilities = len(possibilities)
                    mrv_cell = (row, col)
                    # Si une cellule n'a qu'une seule possibilité, c'est optimal
                    if min_possibilities == 1:
                        return mrv_cell
    return mrv_cell

def heuristic_method(grid):
    """
    Résout le Sudoku en utilisant le backtracking avec heuristique MRV.
    """
    # Trouver la cellule avec le moins de valeurs possibles
    mrv_cell = find_mrv_cell(grid)

    # Si aucune cellule vide, la grille est résolue
    if not mrv_cell:
        return True

    row, col = mrv_cell
    square_size = int(sqrt(grid.size))

    # Tester chaque valeur possible pour la cellule
    for num in range(1, grid.size + 1):
        if is_valid(grid, num, row, col, square_size):
            grid.grid[row][col] = num  # Assigner une valeur
            if technique_heuristic(grid):  # Récursion
                return True
            grid.grid[row][col] = 0  # Backtrack si échec

    return False
