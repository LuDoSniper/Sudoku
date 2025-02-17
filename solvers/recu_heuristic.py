from math import sqrt

def find_next_empty_mrv(grid, size):
    """ Trouve la cellule vide avec le moins de choix possibles (MRV). """
    min_options = size + 1
    best_cell = None
    
    for row in range(size):
        for col in range(size):
            if grid.grid[row][col] == 0:
                possible_values = {num for num in range(1, size + 1) if is_valid(grid, num, row, col)}
                num_options = len(possible_values)
                
                if num_options < min_options:
                    min_options = num_options
                    best_cell = (row, col)

                if min_options == 1:  # On ne peut pas faire mieux
                    return best_cell

    return best_cell

def is_valid(grid, num, row, col):
    """ Vérifie si un numéro peut être placé dans la cellule donnée. """
    if num in grid.get_row(row):
        return False
    if num in grid.get_col(col):
        return False
    if num in grid.get_square(row, col):
        return False
    return True

def backtracking_mrv(grid, player: bool = False):
    """ Solveur de Sudoku utilisant le backtracking et l'heuristique MRV. """
    size = grid.size

    cell = find_next_empty_mrv(grid, size)
    if cell is None:
        return True  # Grille complète

    row, col = cell

    # Essayer chaque valeur possible pour cette cellule
    for num in range(1, size + 1):
        if is_valid(grid, num, row, col):
            grid.grid[row][col] = num
            if player and (row, col) not in grid.player_cells:
                grid.player_cells.append((row, col))
            if backtracking_mrv(grid):
                return True
            grid.grid[row][col] = 0  # Backtrack
            if player:
                grid.player_cells.pop(grid.player_cells.index((row, col)))

    return False
