from math import sqrt

def find_next_empty(grid, size):
    """ Trouve la prochaine cellule vide (0) dans la grille. """
    for row in range(size):
        for column in range(size):
            if grid.grid[row][column] == 0:
                return (row, column)
    return None

def is_valid(grid, num, row, col):
    """ Vérifie si un numéro peut être placé dans la cellule donnée. """
    if num in grid.get_row(row):
        return False
    if num in grid.get_col(col):
        return False
    if num in grid.get_square(row, col):
        return False
    return True

def backtracking_recursif(grid, player: bool = False):
    """ Solveur de Sudoku utilisant le backtracking récursif. """
    size = grid.size
    
    cell = find_next_empty(grid, size)
    if cell is None:
        return True
    
    row, col = cell

    for i in range(1,size+1):
        if is_valid(grid, i, row, col):
            grid.grid[row][col] = i
            if player:
                grid.player_cells.append((row, col))
            if backtracking_recursif(grid) is True:
                return True
            else:
                grid.grid[row][col] = 0


    return False