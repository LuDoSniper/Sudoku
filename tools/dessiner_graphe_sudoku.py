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

    from solvers.coloration_graphe import colorier_sudoku  # Import ici pour éviter la boucle

    global thread
    global stop_event

    stop_event = threading.Event()

    thread = threading.Thread(target=dessiner_graphe_sudoku, args=(SudokuGraphe(grid) if not graphe else grid, stop_event))
    thread.start()

def dessiner_graphe_sudoku(sudoku_graphe, stop_event: threading.Event, ax, fig):
    """Dessine le graphe du Sudoku avec un léger décalage pour éviter le chevauchement des arêtes."""
    while not stop_event.is_set():
        ax.clear()
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

        def on_close(event):
            if event is not None:
                stop_event.set()
                plt.close(fig)

        fig.canvas.mpl_connect('close_event', on_close)

        # Ajouter les valeurs des nœuds comme labels
        labels = {n: sudoku_graphe.valeurs.get(n, "?") for n in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=12, font_color="white")

        # Rafraîchir l'affichage
        plt.pause(0.9)  # Pause pour voir l'évolution

        return ax  # Retourne ax pour éviter qu'il devienne `None`
