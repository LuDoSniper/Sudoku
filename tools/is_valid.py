def is_valid(grid, num, row, col):
    """ Vérifie si un numéro peut être placé dans la cellule donnée. """
    if num in grid.get_row(row):
        return False
    if num in grid.get_col(col):
        return False
    if num in grid.get_square(row, col):
        return False
    return True