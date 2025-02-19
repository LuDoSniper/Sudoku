import sys
import os
import atexit

# Rendre le stderr muet pour empecher matplotlib de planter à la fermeture du programme
class NullIO:
    def write(self, s):
        pass

    def flush(self):
        pass

def disable_stderr():
    sys.stderr = NullIO()

atexit.register(disable_stderr)

import threading
import networkx as nx
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message="Starting a Matplotlib GUI outside of the main thread will likely fail."
)

from models.Grid import Grid
from models.SudokuGraphe import SudokuGraphe

thread: threading.Thread = None
stop_event: threading.Event = None

def stop_thread() -> None:
    global thread
    global stop_event

    if thread is not None and stop_event is not None:
        stop_event.set()
        thread.join()

def display(grid: Grid|SudokuGraphe, graphe: bool = False) -> None:
    """
    Afficher le graphe de la grille de sudoku
    le paramètre graphe est un booléen qui permet de savoir si le premier paramètre est un Grid ou un SudokuGraphe
    """

    global thread
    global stop_event

    # sudoku_graph = grid.grid
    stop_event = threading.Event()

    thread = threading.Thread(target=dessiner_graphe_sudoku, args=(SudokuGraphe(grid) if not graphe else grid, stop_event))
    thread.start()
    print("Le truc devrait se lancer normalement")

def dessiner_graphe_sudoku(sudoku_graphe, stop_event: threading.Event):
    """Dessine le graphe du Sudoku avec un léger décalage pour éviter le chevauchement des arêtes."""
    while not stop_event.is_set():
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
        fig = plt.figure(figsize=(size, size))
        nx.draw(G, pos, with_labels=False, node_color='blue', edge_color='gray', node_size=700)

        def on_close(event):
            if event is not None:
                stop_event.set()
                plt.close(fig)
        
        fig.canvas.mpl_connect('close_event', on_close)

        # Ajouter les valeurs des nœuds
        labels = {n: sudoku_graphe.valeurs.get(n, "?") for n in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_color="white")

        plt.title("Graphe du Sudoku (Disposition avec léger écart)")
        plt.axis("off")  
        plt.show()