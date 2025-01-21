from math import sqrt
from colorama import init as colorama_init, Fore, Style

class Grid:
    
    STR_SEP_COL = " "
    STR_SEP_ROW = " "
    STR_SEP_SQUARE_COL = " "
    STR_SEP_SQUARE_ROW = " "

    def __init__(self, size: int = 9, grid = None) -> None:
        if size <= 0 or sqrt(size) % 1 != 0:
            raise ValueError("Size must be a positive integer and a perfect square")
        self.size = size

        if not grid:
            grid = [[0 for _ in range(size)] for _ in range(size)]
        elif len(grid) != size or any(len(row) != size for row in grid):
            raise ValueError("Grid must be a 2D list of size x size. This error can be caused by a wrong size parameter or a wrong grid parameter.")

        self.grid = grid
    
    def get_row(self, index: int) -> list:
        return list(self.grid[index])
    
    def get_col(self, index: int) -> list:
        return [row[index] for row in self.grid]

    def get_square(self, row: int, col: int) -> list:
        square_size = int(sqrt(self.size))

        # Trouver le coin supérieur gauche du sous-carré
        start_row = (row // square_size) * square_size
        start_col = (col // square_size) * square_size

        # Collecter toutes les cellules du sous-carré
        square = []
        for i in range(start_row, start_row + square_size):
            for j in range(start_col, start_col + square_size):
                square.append(self.grid[i][j])

        return square

    def get_max_width(self) -> int:
        max_width = 0
        for row in self.grid:
            for cell in row:
                cell_width = len(str(cell))
                if cell_width > max_width:
                    max_width = cell_width
        return max_width


    def __str__(self):
        square_size = int(sqrt(self.size))
        max_width = self.get_max_width()
        cell_width = max_width + 2  # Ajouter un espace de chaque côté pour l'esthétique

        # Définir les séparateurs spéciaux
        top_left, top_mid, top_right = "┌", "┬", "┐"
        mid_left, mid_mid, mid_right = "├", "┼", "┤"
        bot_left, bot_mid, bot_right = "└", "┴", "┘"
        horiz = "─" * cell_width

        # Construire les bordures
        top_border = Fore.BLUE + top_left + (top_mid.join([horiz] * self.size)) + top_right + Fore.RESET
        mid_border = Fore.BLUE + mid_left + Fore.GREEN + (mid_mid.join([horiz] * self.size)) + Fore.BLUE + mid_right + Fore.RESET
        mid_border_sep = Fore.BLUE + mid_left + (mid_mid.join([horiz] * self.size)) + mid_right + Fore.RESET
        bottom_border = Fore.BLUE + bot_left + (bot_mid.join([horiz] * self.size)) + bot_right + Fore.RESET

        lines = [top_border]
        for row_index, row in enumerate(self.grid):
            line = []
            for cell_idx, cell in enumerate(row):
                if cell != 0:
                    formatted_cell = Fore.RESET + str(cell).rjust(max_width)
                else:
                    formatted_cell = ' ' * max_width

                line.append(f" {formatted_cell} ")
            lines.append(Fore.BLUE + "│" + Fore.GREEN + "│".join(line) + Fore.BLUE + "│" + Fore.RESET)
            if row_index != self.size - 1:
                if (row_index + 1) % square_size == 0 and row_index + 1 != self.size:
                    lines.append(mid_border_sep) 
                else:
                    lines.append(mid_border)

        lines.append(bottom_border)  # Ajouter la bordure inférieure
        return "\n".join(lines)
