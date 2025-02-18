from math import sqrt
from colorama import init as colorama_init, Fore, Style

class Grid:
    
    STR_SEP_COL = " "
    STR_SEP_ROW = " "
    STR_SEP_SQUARE_COL = " "
    STR_SEP_SQUARE_ROW = " "

    def __init__(self, size: int = 9, grid: list[list[int]] = None) -> None:
        if size <= 0 or sqrt(size) % 1 != 0:
            raise ValueError("Size must be a positive integer and a perfect square")
        self.size: int = size

        if not grid:
            grid = [[0 for _ in range(size)] for _ in range(size)]
        elif len(grid) != size or any(len(row) != size for row in grid):
            raise ValueError("Grid must be a 2D list of size x size. This error can be caused by a wrong size parameter or a wrong grid parameter.")

        self.grid: list[list[int]] = grid
        self.player_cells: list[tuple] = []
        self.indice_cells: list[tuple] = []
    
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

    def get_borders(self):
        top_left, top_mid, top_right = "┌", "┬", "┐"
        mid_left, mid_mid, mid_right = "├", "┼", "┤"
        bot_left, bot_mid, bot_right = "└", "┴", "┘"
        horiz = "─" * (self.get_max_width() + 2)

        # Initialisation de la bordure supérieure
        top_border = Fore.BLUE + top_left
        for _ in range(self.size):
            top_border += horiz
            if _ < self.size - 1:
                top_border += top_mid
        top_border += top_right + Fore.RESET

        # Initialisation de la bordure intermédiaire avec la condition pour les colonnes
        mid_border = Fore.BLUE + mid_left + Fore.RESET
        for col_index in range(self.size):
            mid_border += Fore.GREEN + horiz
            if col_index < self.size - 1:  # Ajouter un séparateur entre les colonnes sauf à la fin
                if (col_index + 1) % int(sqrt(self.size)) == 0:  # Vérifier si c'est une frontière de carré
                    mid_border += Fore.BLUE + mid_mid  # Bleu pour les séparateurs entre les carrés
                else:
                    mid_border += Fore.GREEN + mid_mid  # Vert pour les autres séparateurs
        mid_border += Fore.BLUE + mid_right + Fore.RESET

        # Initialisation de la bordure intermédiaire spéciale
        mid_border_sep = Fore.BLUE + mid_left
        for _ in range(self.size):
            mid_border_sep += horiz
            if _ < self.size - 1:
                mid_border_sep += mid_mid
        mid_border_sep += mid_right + Fore.RESET

        # Initialisation de la bordure inférieure
        bottom_border = Fore.BLUE + bot_left
        for _ in range(self.size):
            bottom_border += horiz
            if _ < self.size - 1:
                bottom_border += bot_mid
        bottom_border += bot_right + Fore.RESET

        return top_border, mid_border, mid_border_sep, bottom_border


    def __str__(self):
        square_size = int(sqrt(self.size))
        max_width = self.get_max_width()

        top_border, mid_border, mid_border_sep, bottom_border = self.get_borders()

        lines = [top_border]
        for row_index, row in enumerate(self.grid):
            line = []
            for col_index, cell in enumerate(row):
                if cell != 0:
                    if (row_index, col_index) in self.player_cells:
                        formatted_cell = (Fore.MAGENTA + str(cell) + Fore.RESET).center(max_width)
                    elif (row_index, col_index) in self.indice_cells:
                        formatted_cell = (Fore.LIGHTMAGENTA_EX + str(cell) + Fore.RESET).center(max_width)
                    else:
                        formatted_cell = Fore.RESET + str(cell).center(max_width)
                else:
                    formatted_cell = ' ' * max_width

                line.append(f" {formatted_cell} ")

            formatted_line = Fore.BLUE + "│" 
            for col_idx, cell in enumerate(line):
                formatted_line += cell
                # Vérifier si c'est une frontière de sous-carré ou le dernier séparateur de la ligne
                if (col_idx + 1) % square_size == 0 or col_idx + 1 == self.size:
                    formatted_line += Fore.BLUE + "│"  # Séparateur bleu
                else:
                    formatted_line += Fore.GREEN + "│"  # Séparateur vert
            formatted_line += Fore.RESET
            lines.append(formatted_line)


            if row_index != self.size - 1:
                if (row_index + 1) % square_size == 0 and row_index + 1 != self.size:
                    lines.append(mid_border_sep) 
                else:
                    lines.append(mid_border)

        lines.append(bottom_border)  # Ajouter la bordure inférieure
        return "\n".join(lines)
