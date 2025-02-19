# Imports
import timeit

# Custom imports
# models
from models.Grid import Grid
# tools
from tools.generator import generate
# solvers
from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from solvers.backtracking_recursif import backtracking_recursif

def time(message_str: str, func: callable, *args: any, **kwargs: any) -> float:
    """
    Calcule le temps d'exécution moyen de la fonction `func` avec les arguments `args` et `kwargs`
    """
    from tools.display_menu import message # Import ici pour éviter la boucle

    message(message_str, 'info')
    sum = 0
    for _ in range(5):
        sum += timeit.timeit(lambda: func(*args, **kwargs), number=1)
    return sum / 5

def time_all():
    """
    Calcule le temps d'exécution moyen de chaque solveur pour les grilles de 4x4, 9x9 et 16x16
    """
    times = []

    # Génération
    gen = []
    gen.append([time("Calcul de backtracking_iteratif pour 4x4...", backtracking_iteratif_pile, Grid(4), use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 4x4...", backtracking_recursif, Grid(4), use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 4x4...", backtracking_iteratif_pile, Grid(4), use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 4x4...", backtracking_recursif, Grid(4), use_heuristic=True, use_random=False)])
    gen.append([time("Calcul de backtracking_iteratif pour 9x9...", backtracking_iteratif_pile, Grid(9), use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 9x9...", backtracking_recursif, Grid(9), use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 9x9...", backtracking_iteratif_pile, Grid(9), use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 9x9...", backtracking_recursif, Grid(9), use_heuristic=True, use_random=False)])
    gen.append([time("Calcul de backtracking_iteratif pour 16x16...", backtracking_iteratif_pile, Grid(16), use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 16x16...", backtracking_recursif, Grid(16), use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 16x16...", backtracking_iteratif_pile, Grid(16), use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 16x16...", backtracking_recursif, Grid(16), use_heuristic=True, use_random=False)])
    times.append(gen)

    # Résolution
    solv = []

    # Setup
    grid_4 = Grid(4)
    generate(grid_4, "normal", backtracking_iteratif_pile, use_heuristic=False, use_random=True) # A passer en False
    grid_9 = Grid(9)
    generate(grid_4, "normal", backtracking_iteratif_pile, use_heuristic=False, use_random=True) # A passer en False
    grid_16 = Grid(16)
    generate(grid_4, "normal", backtracking_iteratif_pile, use_heuristic=False, use_random=True) # A passer en False

    # Benchmark
    solv.append([time("Calcul de backtracking_iteratif pour 4x4...", backtracking_iteratif_pile, grid_4, use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 4x4...", backtracking_recursif, grid_4, use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 4x4...", backtracking_iteratif_pile, grid_4, use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 4x4...", backtracking_recursif, grid_4, use_heuristic=True, use_random=False)])
    solv.append([time("Calcul de backtracking_iteratif pour 9x9...", backtracking_iteratif_pile, grid_9, use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 9x9...", backtracking_recursif, grid_9, use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 9x9...", backtracking_iteratif_pile, grid_9, use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 9x9...", backtracking_recursif, grid_9, use_heuristic=True, use_random=False)])
    solv.append([time("Calcul de backtracking_iteratif pour 16x16...", backtracking_iteratif_pile, grid_16, use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 16x16...", backtracking_recursif, grid_16, use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 16x16...", backtracking_iteratif_pile, grid_16, use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 16x16...", backtracking_recursif, grid_16, use_heuristic=True, use_random=False)])
    times.append(solv)

    return times
