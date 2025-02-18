from math import sqrt
from tools.find_next_empty import find_next_empty_mrv
from tools.is_valid import is_valid

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
            if backtracking_mrv(grid, player):
                return True
            grid.grid[row][col] = 0  # Backtrack
            if player:
                grid.player_cells.pop(grid.player_cells.index((row, col)))

    return False
