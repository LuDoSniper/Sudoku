from math import sqrt

class Grid:
    
    STR_SEP_COL = "|"
    STR_SEP_ROW = "-"
    STR_SEP_SQUARE_COL = "|"
    STR_SEP_SQUARE_ROW = "-"

    def __init__(self, size: int = 9, grid = None) -> None:
        if size <= 0 or sqrt(size) % 1 != 0:
            raise ValueError("Size must be a positive integer and a perfect square")
        self.size = size

        if not grid:
            grid = [[0 for _ in range(size)] for _ in range(size)]
        elif len(grid) != size or any(len(row) != size for row in grid):
            raise ValueError("Grid must be a 2D list of size x size")

        self.grid = grid
    
    def get_row(self, index: int) -> list:
        return self.grid[index]
    
    def get_col(self, index: int) -> list:
        return [row[index] for row in self.grid]

    def get_square(self, row: int, col: int) -> list:
        square = []
        for y in range(int(sqrt(self.size))):
            for x in range(int(sqrt(self.size))):
                square.append(self.grid[row + y][col + x])
        return square
    
    def __str__(self):
        square_size = int(sqrt(self.size))
        lines = []

        for row_idx, row in enumerate(self.grid):
            line = []
            for col_idx, cell in enumerate(row):
                if col_idx % square_size == 0:
                    line.append(self.STR_SEP_SQUARE_COL)
                line.append(str(cell))
                line.append(self.STR_SEP_COL)
            lines.append("".join(line))
            
            if (row_idx + 1) % square_size == 0:
                lines.append(self.STR_SEP_SQUARE_ROW * len(line))

        string = "\n".join(lines)
        return self.STR_SEP_SQUARE_ROW * len(lines[0]) + "\n" + string