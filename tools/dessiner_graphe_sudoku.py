import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Ajouter le dossier parent au PATH pour importer les modules custom

# Rendre le stderr muet pour empecher matplotlib de planter à la fermeture du programme
# ------stderr------
import atexit
class NullIO:
    def write(self, s):
        pass

    def flush(self):
        pass

def disable_stderr():
    sys.stderr = NullIO()

atexit.register(disable_stderr)
# ------------------

# Rendre muet les warnings de matplotlib
# ------warnings------
import warnings
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message="Starting a Matplotlib GUI outside of the main thread will likely fail."
)
# --------------------

# Imports
import threading
import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt

# Custom imports
# models
from models.Grid import Grid
from models.SudokuGraphe import SudokuGraphe

# Variables globales
thread: threading.Thread = None
stop_event: threading.Event = None

def stop_thread() -> None:
    """
    Stopper le thread courrant s'il existe
    """
    global thread
    global stop_event
    global current_figure

    if thread is not None and stop_event is not None:
        plt.close(current_figure)
        current_figure = None
        stop_event.set()
        thread.join()

def display(grid: Grid, solver: bool = False, pause: float = 0.5) -> None:
    """
    Afficher le graphe de la grille de sudoku
    """

    from solvers.coloration_graphe import colorier_sudoku  # Import ici pour éviter la boucle

    global thread
    global stop_event

    stop_event = threading.Event()

    thread = threading.Thread(target=dessiner_graphe_sudoku if not solver else colorier_sudoku, args=(SudokuGraphe(grid) if not solver else grid, stop_event, pause))
    thread.start()


def dessiner_graphe_sudoku(sudoku_graphe, stop_event: threading.Event = threading.Event(), pause: float = 0.5, ax: plt.Axes|None = None, fig: plt.Figure|None = None) -> plt.Axes:
    """
    Dessine le graphe du Sudoku et met à jour l'affichage si `ax` et `fig` sont fournis.
    """
    global current_figure
    current_figure = fig

    while stop_event is None or  not stop_event.is_set():
        if ax is not None:
            ax.clear()

        G = nx.Graph()

        # Ajouter les sommets et arêtes
        for sommet, voisins in sudoku_graphe.adjacence.items():
            G.add_node(sommet)
            for voisin in voisins['liens']:
                G.add_edge(sommet, voisin)

        # Définition des positions
        size = sudoku_graphe.size
        spacing = 0.3  

        pos = {(i, j): (j + (i % 2) * spacing, -i + (j % 2) * spacing) for i in range(size) for j in range(size)}

        # Définition des couleurs
        couleurs = {1: "green", 2: "blue", 3: "red", 4: "purple", 5: "orange",
                    6: "pink", 7: "yellow", 8: "cyan", 9: "brown"}

        node_colors = [couleurs.get(sudoku_graphe.valeurs.get(n, 0), "gray") for n in G.nodes()]

        if ax is not None and fig is not None:
            # Mode interactif : mise à jour directe du graphe
            nx.draw(G, pos, ax=ax, with_labels=False, node_color=node_colors, edge_color='gray', node_size=700)
            labels = {n: sudoku_graphe.valeurs.get(n, "?") for n in G.nodes()}
            nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=12, font_color="white")

            fig.canvas.draw()  # Force l'affichage
            fig.canvas.flush_events()  # Rafraîchit les événements
            plt.pause(pause)  # Pause pour voir l'évolution

            return ax

        else:
            # Mode statique
            fig, ax = plt.subplots(figsize=(6, 6))
            nx.draw(G, pos, ax=ax, with_labels=False, node_color=node_colors, edge_color='gray', node_size=700)
            labels = {n: sudoku_graphe.valeurs.get(n, "?") for n in G.nodes()}
            nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=12, font_color="white")
            current_figure = fig

            plt.show()
        
        if stop_event is not None:
            fig.canvas.mpl_connect('close_event', lambda event: stop_event.set() if event is not None else None)
