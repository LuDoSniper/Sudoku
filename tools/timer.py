import timeit

from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from solvers.backtracking_recursif import backtracking_recursif
from models.Grid import Grid

def time(message_str: str, func: callable, *args: any, **kwargs: any) -> float:
    from tools.display_menu import message

    message(message_str, 'info')
    sum = 0
    for _ in range(5):
        sum += timeit.timeit(lambda: func(*args, **kwargs), number=1)
    return sum / 5

def time_all():
    times = []
    times.append([time("Calcul de backtracking_iteratif pour 4x4...", backtracking_iteratif_pile, Grid(4), use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 4x4...", backtracking_recursif, Grid(4), use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 4x4...", backtracking_iteratif_pile, Grid(4), use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 4x4...", backtracking_recursif, Grid(4), use_heuristic=True, use_random=False)])
    times.append([time("Calcul de backtracking_iteratif pour 9x9...", backtracking_iteratif_pile, Grid(9), use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 9x9...", backtracking_recursif, Grid(9), use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 9x9...", backtracking_iteratif_pile, Grid(9), use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 9x9...", backtracking_recursif, Grid(9), use_heuristic=True, use_random=False)])
    times.append([time("Calcul de backtracking_iteratif pour 16x16...", backtracking_iteratif_pile, Grid(16), use_heuristic=False, use_random=True), # A passer en False
                  time("Calcul de backtracking_recursif pour 16x16...", backtracking_recursif, Grid(16), use_heuristic=False, use_random=False),
                  time("Calcul de heuristique_iteratif pour 16x16...", backtracking_iteratif_pile, Grid(16), use_heuristic=True, use_random=True), # A passer en False
                  time("Calcul de heuristique_recursif pour 16x16...", backtracking_recursif, Grid(16), use_heuristic=True, use_random=False)])
    return times
