import random
from math import sqrt
from tools.find_next_empty import find_next_empty
from tools.is_valid import is_valid

def backtracking_recursif(grid, player: bool = False):
    """ Solveur de Sudoku utilisant le backtracking récursif avec choix aléatoire des valeurs. """
    size = grid.size
    
    cell = find_next_empty(grid, size)
    if cell is None:
        return True
    
    row, col = cell
    possible_values = list(range(1, size + 1))
    random.shuffle(possible_values)  # Mélange des valeurs pour varier la génération
    
    for num in possible_values:
        if is_valid(grid, num, row, col):
            grid.grid[row][col] = num
            if player and (row, col) not in grid.player_cells:
                grid.player_cells.append((row, col))
            if backtracking_recursif(grid, player):
                return True
            
            grid.grid[row][col] = 0
            if player:
                grid.player_cells.pop(grid.player_cells.index((row, col)))
    
    return False
