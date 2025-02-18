from tools.is_valid import is_valid

def find_next_empty(grid, size):
    """ Trouve la prochaine cellule vide (0) dans la grille. """
    for row in range(size):
        for column in range(size):
            if grid.grid[row][column] == 0:
                return (row, column)
    return None

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