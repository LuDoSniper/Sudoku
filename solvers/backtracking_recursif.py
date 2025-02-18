from math import sqrt
from tools.find_next_empty import find_next_empty
from tools.is_valid import is_valid

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
            if player and (row, col) not in grid.player_cells:
                grid.player_cells.append((row, col))
            if backtracking_recursif(grid, player) is True:
                return True
            else:
                grid.grid[row][col] = 0
                if player:
                    grid.player_cells.pop(grid.player_cells.index((row, col)))


    return False