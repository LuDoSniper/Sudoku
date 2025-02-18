import sys
import os
import threading
import networkx as nx
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import matplotlib.pyplot as plt
from models.Grid import Grid
from models.SudokuGraphe import SudokuGraphe
from solvers.coloration_graphe import colorier_sudoku

def display(grid: Grid) -> None:
    """
    Afficher le graphe de la grille de sudoku
    """
    sudoku_graph = SudokuGraphe(grid)
    threading.Thread(target=colorier_sudoku, args=(sudoku_graph)).start()
    print("Le truc devrait se lancer normalement")

def dessiner_graphe_sudoku(sudoku_graphe):
    """Dessine le graphe du Sudoku avec un léger décalage pour éviter le chevauchement des arêtes."""
    G = nx.Graph()

    # Ajouter les sommets et arêtes
    for sommet, voisins in sudoku_graphe.adjacence.items():
        G.add_node(sommet)
        for voisin in voisins['liens']:
            G.add_edge(sommet, voisin)

    # Définition des positions avec un léger décalage
    size = sudoku_graphe.size
    spacing = 0.3  # Ajuste cet écart pour mieux espacer les lignes

    pos = {}
    for i in range(size):
        for j in range(size):
            x_offset = (i % 2) * spacing  # Décalage horizontal pour certaines lignes
            y_offset = (j % 2) * spacing  # Décalage vertical pour certaines colonnes
            pos[(i, j)] = (j + x_offset, (size - i - 1) + y_offset)

    # Dessiner le graphe
    plt.figure(figsize=(size, size))
    nx.draw(G, pos, with_labels=False, node_color='blue', edge_color='gray', node_size=700)

    # Ajouter les valeurs des nœuds
    labels = {n: sudoku_graphe.valeurs.get(n, "?") for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_color="white")

    plt.title("Graphe du Sudoku (Disposition avec léger écart)")
    plt.axis("off")  
    plt.show()