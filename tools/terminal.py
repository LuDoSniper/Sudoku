import os
import sys
if os.name == "posix":
    import termios
if os.name == "nt":
    import msvcrt
import keyboard
import copy
from tools.display_menu import display, message
from math import sqrt

# Custom
from models.Grid import Grid

from tools.generator import generate
from tools.validator import verify, is_complete
from tools.logger import log, unlog, init as init_logs, chained_list_to_string as get_str_logs, get_last_occurence
from tools.dessiner_graphe_sudoku import display as display_graph, stop_thread

from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from solvers.backtracking_recursif import backtracking_recursif
from solvers.ite_heuristic import ite_heuristic_method
from solvers.recu_heuristic import recu_heuristic_method
from solvers.coloration_graphe import colorier_sudoku

# Variables globales
running = True
current_menu = "main"
selected_size = None
selected_difficulty = None
grid = None
cursor_position = None
n = None
input_mode: str|None = None


def clear() -> None:
    """
    Efface le terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_buffer() -> None:
    """
    Vide le buffer du terminal.
    """
    sys.stdin.flush()
    sys.stdout.flush()
    sys.stderr.flush()

    # Vide le buffer du terminal
    if os.name == "posix":
        # Flush le tampon d'entrée (file descriptor de sys.stdin)
        termios.tcflush(sys.stdin.fileno(), termios.TCIFLUSH)
    if os.name == "nt":
        # Tant qu'il y a un caractère en attente, on le lit et l'ignore
        while msvcrt.kbhit():
            msvcrt.getch()

def set_terminal_mode(raw: bool = True) -> None:
    """
    Active ou désactive le mode brut pour éviter les artefacts d'affichage. (^[[A par exemple)
    /!\\ Ne fonctionne que sous Linux.
    """
    if os.name != "posix":
        raise Exception("Cette fonctionnalité n'est disponible que sous Linux.")
    fd = sys.stdin.fileno()
    settings = termios.tcgetattr(fd)
    if raw:
        tty_mode = termios.tcgetattr(fd)
        tty_mode[3] = tty_mode[3] & ~termios.ICANON & ~termios.ECHO  # Désactive l'écho et le mode canonique
        termios.tcsetattr(fd, termios.TCSADRAIN, tty_mode)
    else:
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)

def display_menu(menu: str, n: int|None = None, grid: Grid|None = None, cursor_position: tuple[int]|None = None, imported: bool = False) -> None:
    clear()
    display(menu, n=n, grid=grid, cursor_position=cursor_position, imported=imported, input=grid is not None and grid.size > 9)

def on_press(event: keyboard.KeyboardEvent) -> None:
    """
    Fonction appelée lorsqu'une touche est pressée.
    """
    global current_menu
    global selected_size
    global selected_difficulty
    global grid
    global cursor_position
    global logs
    global n
    global input_mode

    # Cas spécial séparé pour une meilleure lisibilité (custom input)
    if event.name in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'backspace', 'enter'):
        match event.name:
            case "backspace":
                if current_menu in ("n_selection", "n_import_selection") and (selected_size or n) and input_mode:
                    if input_mode == "size":
                        selected_size = int(str(selected_size)[:-1]) if len(str(selected_size)) > 1 else None
                    elif input_mode == "n":
                        n = int(str(n)[:-1]) if len(str(n)) > 1 else None
                    display_menu(current_menu, selected_size if input_mode == "size" else n)
                elif current_menu == "grid":
                    if cursor_position:
                        if grid.grid[cursor_position[0]][cursor_position[1]] != 0 and (cursor_position in grid.player_cells or selected_difficulty is None):
                            grid.grid[cursor_position[0]][cursor_position[1]] = 0
                            if cursor_position in grid.player_cells:
                                log({"coords" : cursor_position, "event" : event.name})
                            try:
                                grid.player_cells.remove(cursor_position)
                            except ValueError: # Lèvera une erreur si l'utilisateur est actuellement en importation
                                pass
                            imported = selected_difficulty is None
                            display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
                    else:
                        message("Veuillez sélectionner une case", "error")
            case "enter":
                if current_menu in ("n_selection", "n_import_selection"):
                    if selected_size and input_mode == "size":
                        if selected_size > 0 and sqrt(selected_size) % 1 == 0:
                            if current_menu == "n_selection":
                                current_menu = "difficulty_selection"
                                display_menu(current_menu, selected_size)
                            elif current_menu == "n_import_selection":
                                message("Valeur valide", "success")
                                grid = Grid(selected_size)
                                cursor_position = (0, 0)
                                current_menu = "grid"
                                display_menu(current_menu, grid=grid, cursor_position=cursor_position, imported=True)
                        else:
                            selected_size = None
                            display_menu(current_menu, selected_size)
                            message("Veuillez entrer un entier valide", "error")
                    elif n and input_mode == "n":
                        if 0 < n <= grid.size:
                            current_menu = "grid"
                            if cursor_position:
                                if grid.grid[cursor_position[0]][cursor_position[1]] == 0:
                                    grid.grid[cursor_position[0]][cursor_position[1]] = n
                                    log({"coords" : cursor_position, "event" : str(n)})
                                    imported = selected_difficulty is None
                                    if not imported:
                                        grid.player_cells.append(cursor_position)
                                    display_menu(current_menu, grid=grid, cursor_position=cursor_position, imported=imported)
                            else:
                                message("Veuillez sélectionner une case", "error")
                        else:
                            message('Valeur invalide', 'error')
                            message(f"Votre valeur doit être comprise entre 1 et {grid.size} incluts", 'info')
            case _:
                match current_menu:
                    case "n_selection" | "n_import_selection":
                        print(selected_size, n, input_mode)
                        if input_mode == "size":
                            selected_size = int(str(selected_size) + event.name) if selected_size else int(event.name)
                        elif input_mode == "n":
                            n = int(str(n) + event.name) if n else int(event.name)
                        display_menu(current_menu, selected_size if input_mode == "size" else n)
                    case "grid":
                        if event.name != '0' and grid.size <= 9:
                            if cursor_position:
                                if grid.grid[cursor_position[0]][cursor_position[1]] == 0:
                                    grid.grid[cursor_position[0]][cursor_position[1]] = int(event.name)
                                    log({"coords" : cursor_position, "event" : event.name})
                                    imported = selected_difficulty is None
                                    if not imported:
                                        grid.player_cells.append(cursor_position)
                                    display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
                            else:
                                message("Veuillez sélectionner une case", "error")

    match event.name:
        case "1":
            match current_menu:
                case "main":
                    current_menu = "mode_selection"
                    display_menu(current_menu)
                case "mode_selection":
                    current_menu = "classique"
                    display_menu(current_menu)
                case "classique":
                    current_menu = "difficulty_selection"
                    selected_size = 4
                    display_menu(current_menu, selected_size)
                case "difficulty_selection":
                    selected_difficulty = "easy"
                    current_menu = "generator_selection"
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "generator_selection":
                    current_menu = "grid"
                    cursor_position = (0, 0)
                    grid = Grid(selected_size)
                    generate(grid, selected_difficulty, alg=backtracking_iteratif_pile)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "solver_selection":
                    current_menu = "grid"
                    backtracking_iteratif_pile(grid, player=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "indice_selection":
                    current_menu = "grid"
                    backtracking_iteratif_pile(grid, indice=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
        case "2":
            match current_menu:
                case "main":
                    current_menu = "rules"
                    display_menu(current_menu)
                case "mode_selection":
                    current_menu = "n_import_selection"
                    input_mode = "size"
                    display_menu(current_menu)
                case "classique":
                    current_menu = "difficulty_selection"
                    selected_size = 9
                    display_menu(current_menu, selected_size)
                case "difficulty_selection":
                    selected_difficulty = "normal"
                    current_menu = "generator_selection"
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "generator_selection":
                    current_menu = "grid"
                    cursor_position = (0, 0)
                    grid = Grid(selected_size)
                    generate(grid, selected_difficulty, alg=backtracking_recursif)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "solver_selection":
                    current_menu = "grid"
                    backtracking_recursif(grid, player=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "indice_selection":
                    current_menu = "grid"
                    grid_list = copy.deepcopy(grid.grid)
                    backtracking_recursif(grid, indice=True)
                    grid.grid = grid_list
                    grid.activate_indice_buffer()
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
        case "3":
            match current_menu:
                case "main":
                    current_menu = "algo_times"
                    message("Sample : 10", "info")
                    message("Calcul des moyennes de temps d'execution...", "info")
                    display_menu(current_menu)
                case "classique":
                    current_menu = "difficulty_selection"
                    selected_size = 16
                    display_menu(current_menu, selected_size)
                case "difficulty_selection":
                    selected_difficulty = "hard"
                    current_menu = "generator_selection"
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "generator_selection":
                    current_menu = "grid"
                    cursor_position = (0, 0)
                    grid = Grid(selected_size)
                    generate(grid, selected_difficulty, alg=ite_heuristic_method)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "solver_selection":
                    current_menu = "grid"
                    ite_heuristic_method(grid, player=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "indice_selection":
                    current_menu = "grid"
                    ite_heuristic_method(grid, indice=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
        case "4":
            match current_menu:
                case "main":
                    shutdown()
                case "classique":
                    current_menu = "n_selection"
                    display_menu(current_menu, selected_size)
                case "generator_selection":
                    current_menu = "grid"
                    cursor_position = (0, 0)
                    grid = Grid(selected_size)
                    generate(grid, selected_difficulty, alg=recu_heuristic_method)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "solver_selection":
                    current_menu = "grid"
                    recu_heuristic_method(grid, player=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "indice_selection":
                    current_menu = "grid"
                    grid_list = copy.deepcopy(grid.grid)
                    recu_heuristic_method(grid, indice=True)
                    grid.grid = grid_list
                    grid.activate_indice_buffer()
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
        case '5':
            match current_menu:
                case "solver_selection":
                    current_menu = "grid"
                    stop_thread()
                    display_graph(grid, solver=True, pause=0.01)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                    # message('c\'est sensé marcher', 'debug')
        case "q":
            match current_menu:
                case "rules" | "mode_selection" | "algo_times":
                    current_menu = "main"
                    display_menu(current_menu)
                case "classique":
                    current_menu = "mode_selection"
                    display_menu(current_menu)
                case "difficulty_selection":
                    current_menu = "classique"
                    selected_size = None
                    display_menu(current_menu)
                case "grid":
                    current_menu = "main"
                    selected_size = None
                    grid = None
                    cursor_position = None
                    stop_thread()
                    display_menu(current_menu)
                case "solver_selection" | "generator_selection" | "indice_selection":
                    if cursor_position:
                        current_menu = "grid"
                    else:
                        current_menu = "difficulty_selection"
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
            selected_difficulty = None
        
        case "up"|"haut":
            if current_menu == "grid":
                imported = selected_difficulty is None
                if cursor_position:
                    if cursor_position[0] > 0:
                        cursor_position = (cursor_position[0] - 1, cursor_position[1])
                        display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
                else:
                    cursor_position = (0, 0)
                    display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
        case "down"|"bas":
            imported = selected_difficulty is None
            if current_menu == "grid":
                if cursor_position:
                    if cursor_position[0] < grid.size - 1:
                        cursor_position = (cursor_position[0] + 1, cursor_position[1])
                        display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
                else:
                    cursor_position = (0, 0)
                    display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
        case "left"|"gauche":
            imported = selected_difficulty is None
            if current_menu == "grid":
                if cursor_position:
                    if cursor_position[1] > 0:
                        cursor_position = (cursor_position[0], cursor_position[1] - 1)
                        display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
                else:
                    cursor_position = (0, 0)
                    display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
        case "right"|"droite":
            imported = selected_difficulty is None
            if current_menu == "grid":
                if cursor_position:
                    if cursor_position[1] < grid.size - 1:
                        cursor_position = (cursor_position[0], cursor_position[1] + 1)
                        display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)
                else:
                    cursor_position = (0, 0)
                    display_menu("grid", grid=grid, cursor_position=cursor_position, imported=imported)

        case 'e':
            if current_menu == "grid" and grid.size > 9:
                current_menu = "n_selection"
                n = None
                input_mode = "n"
                display_menu(current_menu)
        case 'b':
            if current_menu == "grid":
                result = unlog(data = False)

                if result is not None:
                    data = result.get_data()
                    coords = data.get("coords")
                    event = data.get("event")

                    if event == "backspace":
                        # Si le dernier log est un "backspace", on restaure la valeur précédente de la case concernée
                        prev = get_last_occurence(coords)
                        if prev is not None:
                            prev_data = prev.get_data()
                            prev_coords = prev_data.get("coords")
                            prev_event = prev_data.get("event")
                            grid.grid[prev_coords[0]][prev_coords[1]] = int(prev_event)
                            grid.player_cells.append(prev_coords)
                        
                    else:
                        # Sinon, on annule le dernier coup joué
                        grid.grid[coords[0]][coords[1]] = 0
                        grid.player_cells.append(coords)

                    display_menu("grid", grid=grid, cursor_position=cursor_position)
                    message("Dernier coup annulé", "info")
        case 'i':
            if current_menu == "grid" and selected_difficulty is not None:
                if not is_complete(grid):
                    current_menu = "indice_selection"
                    display_menu(current_menu)
                else:
                    message("Grille complète", "warning")
        case 'v':
            if current_menu == "grid":
                if is_complete(grid):
                    if verify(grid):
                        message("Grille valide", "success")
                    else:
                        message("Grille invalide", "error")
                else:
                    message("Grille incomplète", "warning")
        case 'j':
            if current_menu == "grid" and selected_difficulty is None:
                selected_difficulty = "easy"
                display_menu("grid", grid=grid, cursor_position=cursor_position)
                logs = init_logs()
        case 'r':
            if current_menu == "grid":
                current_menu = "solver_selection"
                display_menu(current_menu)
        case 's':
            if current_menu == "grid":
                if selected_difficulty is None:
                    grid_list = copy.deepcopy(grid.grid)
                    result = recu_heuristic_method(grid)
                    grid.grid = grid_list
                    message(f"Votre grille {"n'a pas de solution" if not result else "a une solution"}", "success" if result else "error")
        case 'g':
            if current_menu == "grid":
                if selected_difficulty is not None:
                    stop_thread()
                    display_graph(grid, pause=0.01)
                    message('Graphe en cours d\'affichage...', "info")
        case _:
            # message(f"Ceci est un message de debug : {event.name}", "info")
            # message(get_str_logs(), "info")
            pass

def mainloop() -> None:
    display_menu("main")
    keyboard.on_press(on_press)

    global running
    while running:
        if keyboard.is_pressed("esc"):
            shutdown()

def shutdown() -> None:
    """
    Réinitialisation des paramètres avant la fermeture du programme
    """
    keyboard.unhook_all()
    stop_thread()
    clear_buffer()

    clear()
    message("Fermeture du programme...", "info")
    message("Cela peut prendre quelques secondes", "info")
    
    global running
    running = False
