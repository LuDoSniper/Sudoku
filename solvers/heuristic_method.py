from math import sqrt

def find_next_empty_mrv(grid, size, square_size):
    min_options = size + 1  # Plus grand que le nombre maximal de choix possibles (1 à N)
    best_cell = None  

    for row in range(size):
        for col in range(size):
            if grid.grid[row][col] == 0:
                possible_values = {num for num in range(1, size + 1) if is_valid(grid, num, row, col, square_size)}
                num_options = len(possible_values)

                if num_options < min_options:
                    min_options = num_options
                    best_cell = (row, col)

                # Si une case n'a qu'une seule possibilité, on la choisit directement
                if min_options == 1:
                    break  
        if min_options == 1:
            break  

    return best_cell


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


def heuristic_method(grid):
    size = grid.size
    square_size = int(sqrt(size))
    stack = []

    current_cell = find_next_empty_mrv(grid, size, square_size)
    if not current_cell:
        return True  # Sudoku déjà résolu

    stack.append((current_cell, 1))  

    while stack:
        (row, col), attempt = stack.pop()
        solved = False

        while attempt <= size and not solved:
            if is_valid(grid, attempt, row, col, square_size):
                grid.grid[row][col] = attempt
                next_cell = find_next_empty_mrv(grid, size, square_size)

                if not next_cell:
                    return True  

                stack.append(((row, col), attempt + 1))
                stack.append((next_cell, 1))
                solved = True
            else:
                attempt += 1

        if not solved:
            grid.grid[row][col] = 0  

    return False  
