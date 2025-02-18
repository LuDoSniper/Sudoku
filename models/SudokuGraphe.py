from models.Graphe import Graphe
import math

class SudokuGraphe(Graphe):
    def __init__(self, grid):
        """Initialise un graphe pour un Sudoku de taille 'taille x taille'."""
        super().__init__()
        self.grid = grid.grid
        self.taille = grid.size
        self.taille_bloc = int(math.sqrt(grid.size))  # Taille des blocs
        self.valeurs = {}  # Dictionnaire pour stocker les valeurs des cases

        # Créer les sommets et ajouter les valeurs
        for i in range(self.taille):
            for j in range(self.taille):
                # Ajouter chaque sommet avec sa valeur
                valeur = self.grid[i][j]  # Valeur de la cellule
                self.ajouter_sommet((i, j), valeur)
                self.valeurs[(i, j)] = valeur  # Ajouter la valeur dans le dictionnaire

        # Ajouter les arêtes
        self._ajouter_aretes_sudoku()

    def _ajouter_aretes_sudoku(self):
        """Ajoute les arêtes pour respecter les règles du Sudoku."""
        for i in range(self.taille):
            for j in range(self.taille):
                for k in range(self.taille):
                    # Même ligne
                    if j != k:
                        self._ajouter_arête_unique((i, j), (i, k))
                    # Même colonne
                    if i != k:
                        self._ajouter_arête_unique((i, j), (k, j))

                # Même bloc
                debut_bloc_i = (i // self.taille_bloc) * self.taille_bloc
                debut_bloc_j = (j // self.taille_bloc) * self.taille_bloc
                for bi in range(debut_bloc_i, debut_bloc_i + self.taille_bloc):
                    for bj in range(debut_bloc_j, debut_bloc_j + self.taille_bloc):
                        if (bi, bj) != (i, j):
                            self._ajouter_arête_unique((i, j), (bi, bj))


    def _ajouter_arête_unique(self, sommet1, sommet2):
        """Ajoute une arête entre deux sommets seulement si elle n'existe pas déjà."""
        if sommet2 not in self.adjacence[sommet1]['liens']:
            self.ajouter_arête(sommet1, sommet2)
        if sommet1 not in self.adjacence[sommet2]['liens']:
            self.ajouter_arête(sommet2, sommet1)
