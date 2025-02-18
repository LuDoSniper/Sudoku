import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.SudokuGraphe import SudokuGraphe
from models.Grid import Grid
from tools.generator import generate_full, calibrate
import networkx as nx
import matplotlib.pyplot as plt

def dessiner_graphe_sudoku(sudoku_graphe):
    """Dessine le graphe du Sudoku en affichant les valeurs des nœuds."""
    G = nx.Graph()

    # Ajouter les sommets et arêtes
    for sommet, voisins in sudoku_graphe.adjacence.items():
        G.add_node(sommet)
        for voisin in voisins['liens']:
            G.add_edge(sommet, voisin)

    # Positionnement des nœuds
    pos = nx.spring_layout(G, seed=42, k=0.5)

    # Dessiner le graphe
    nx.draw(G, pos, with_labels=False, node_color='blue', edge_color='gray', node_size=700)

    # Ajouter les valeurs des nœuds
    labels = {n: sudoku_graphe.valeurs.get(n, "?") for n in G.nodes()}  # Utilise la valeur si dispo, sinon '?'
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_color="white")

    plt.title("Graphe du Sudoku (Valeurs des nœuds)")
    plt.axis("off")  
    plt.show()


def sudoku_to_dict(grid_instance: Grid) -> dict:
    """
    Convertit une instance de Grid en un dictionnaire où chaque clé est un tuple (row, col)
    représentant les coordonnées de la cellule, et la valeur est le nombre correspondant dans la grille.
    """
    valeurs_noeuds = {}
    for row_index, row in enumerate(grid_instance.grid):
        for col_index, value in enumerate(row):
            valeurs_noeuds[(row_index, col_index)] = value
    
    return valeurs_noeuds

# Exemple d'utilisation :
grid = Grid(4)
generate_full(grid)
calibrate(grid, "easy")
print(grid)

valeurs_noeuds = sudoku_to_dict(grid)

sudoku_graphe = SudokuGraphe(grid)
print(sudoku_graphe)
dessiner_graphe_sudoku(sudoku_graphe)
