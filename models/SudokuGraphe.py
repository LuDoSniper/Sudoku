from Graphe import Graphe
import math

class SudokuGraphe(Graphe):
    def __init__(self, taille):
        """Initialise un graphe pour un Sudoku de taille 'taille x taille'."""
        super().__init__()
        self.taille = taille
        self.taille_bloc = int(math.sqrt(taille))  # Taille des blocs

        # Créer les sommets
        for i in range(taille):
            for j in range(taille):
                self.ajouter_sommet((i, j))

        # Ajouter les arêtes
        self._ajouter_aretes_sudoku()

    def _ajouter_aretes_sudoku(self):
        """Ajoute les arêtes pour respecter les règles du Sudoku."""
        for i in range(self.taille):
            for j in range(self.taille):
                for k in range(self.taille):
                    # Même ligne
                    if j != k:
                        self.ajouter_arête((i, j), (i, k))
                    # Même colonne
                    if i != k:
                        self.ajouter_arête((i, j), (k, j))

                # Même bloc
                debut_bloc_i = (i // self.taille_bloc) * self.taille_bloc
                debut_bloc_j = (j // self.taille_bloc) * self.taille_bloc
                for bi in range(debut_bloc_i, debut_bloc_i + self.taille_bloc):
                    for bj in range(debut_bloc_j, debut_bloc_j + self.taille_bloc):
                        if (bi, bj) != (i, j):
                            self.ajouter_arête((i, j), (bi, bj))

    def __str__(self):
        """Affiche la structure du graphe du Sudoku."""
        affichage = ""
        for sommet, voisins in self.adjacence.items():
            affichage += f"{sommet} -> {voisins} \n"
        return affichage


