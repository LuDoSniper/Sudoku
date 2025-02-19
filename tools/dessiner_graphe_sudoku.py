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

def display(grid: Grid) -> None:
    """
    Afficher le graphe de la grille de sudoku
    """
    from solvers.coloration_graphe import colorier_sudoku  # Import ici pour éviter la boucle
    
    sudoku_graph = SudokuGraphe(grid)
    threading.Thread(target=colorier_sudoku, args=(sudoku_graph,)).start()
    print("Le truc devrait se lancer normalement")


def dessiner_graphe_sudoku(sudoku_graphe, ax):
    """Dessine le graphe du Sudoku en mettant à jour l'affichage."""
    ax.clear()  # Efface l'ancien graphe

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
            pos[(i, j)] = (j + x_offset, -i + y_offset)

    # Définition des couleurs
    couleurs = {
        1: "green", 2: "blue", 3: "red", 4: "purple", 5: "orange",
        6: "pink", 7: "yellow", 8: "cyan", 9: "brown"
    }

    # Attribution des couleurs aux nœuds
    node_colors = [couleurs.get(sudoku_graphe.valeurs.get(n, 0), "gray") for n in G.nodes()]

    # Dessiner le graphe
    nx.draw(G, pos, ax=ax, with_labels=False, node_color=node_colors, edge_color='gray', node_size=700)

    # Ajouter les valeurs des nœuds comme labels
    labels = {n: sudoku_graphe.valeurs.get(n, "?") for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=12, font_color="white")

    # Rafraîchir l'affichage
    plt.pause(0.9)  # Pause pour voir l'évolution

    return ax  # Retourne ax pour éviter qu'il devienne `None`

