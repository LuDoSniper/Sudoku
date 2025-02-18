import math
from models.Graphe import Graphe

class SudokuGraphe(Graphe):
    def __init__(self, grid):
        """
        Initialise un graphe pour un Sudoku à partir d'une grille donnée.
        Chaque cellule est un sommet et est connectée à ses voisins selon les règles du Sudoku.
        """
        super().__init__()
        self.grid = grid.grid
        self.size = grid.size
        self.block_size = int(math.sqrt(self.size))
        self.valeurs = {}  # Dictionnaire pour stocker les valeurs des cellules
        
        self._ajouter_sommets()
        self._ajouter_aretes()

    def _ajouter_sommets(self):
        """Ajoute les sommets représentant les cellules de la grille avec leurs valeurs."""
        for i in range(self.size):
            for j in range(self.size):
                valeur = self.grid[i][j]
                self.ajouter_sommet((i, j), valeur)
                self.valeurs[(i, j)] = valeur  # Stocker la valeur associée à la cellule

    def _ajouter_aretes(self):
        """Ajoute les arêtes entre les sommets qui doivent avoir des valeurs différentes."""
        for i in range(self.size):
            for j in range(self.size):
                voisins = self._get_voisins(i, j)
                for voisin in voisins:
                    self.ajouter_arête((i, j), voisin)

    def _get_voisins(self, row, col):
        """Retourne tous les voisins d'une cellule (même ligne, même colonne, même bloc)."""
        voisins = set()
        
        # Ajouter voisins de la ligne et de la colonne
        for k in range(self.size):
            if k != col:
                voisins.add((row, k))  # Même ligne
            if k != row:
                voisins.add((k, col))  # Même colonne
        
        # Ajouter voisins du même bloc
        start_row, start_col = (row // self.block_size) * self.block_size, (col // self.block_size) * self.block_size
        for i in range(start_row, start_row + self.block_size):
            for j in range(start_col, start_col + self.block_size):
                if (i, j) != (row, col):
                    voisins.add((i, j))
        
        return voisins
