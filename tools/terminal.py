import sys
import os

# Ajoute le chemin du projet au PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if os.name == "posix":
    import termios
if os.name == "nt":
    import msvcrt
import keyboard
from tools.display_menu import display, message
from math import sqrt
from models.Grid import Grid
from tools.generator import generate
from models.ChainedList import ChainedList
from tools.validator import verify, is_complete
from solvers.backtracking_iteratif_pile import backtracking_iteratif_pile
from solvers.backtracking_recursif import backtracking_recursif
from solvers.heuristic_method import heuristic_method
from solvers.recu_heuristic import backtracking_mrv

# Variables globales
running = True
current_menu = "main"
selected_size = None
selected_difficulty = None
grid = None
cursor_position = None
logs: ChainedList = None

def logger(logs, coord, event):
    if logs is None:
        logs = ChainedList({"coord" : coord, "nb" : event})
    else:
        logs.append({"coord" : coord, "nb" : event})

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
    display(menu, n=n, grid=grid, cursor_position=cursor_position, imported=imported)

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

    # Cas spécial séparé pour une meilleure lisibilité (custom input)
    if event.name in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'backspace', 'enter'):
        match event.name:
            case "backspace":
                if current_menu in ("n_selection", "n_import_selection") and selected_size:
                    selected_size = int(str(selected_size)[:-1]) if len(str(selected_size)) > 1 else None
                    display_menu(current_menu, selected_size)
                elif current_menu == "grid":
                    if cursor_position:
                        if grid.grid[cursor_position[0]][cursor_position[1]] != 0 and (cursor_position in grid.player_cells or selected_difficulty is None):
                            grid.grid[cursor_position[0]][cursor_position[1]] = 0
                            grid.player_cells.remove(cursor_position)
                            display_menu("grid", grid=grid, cursor_position=cursor_position)
                    else:
                        message("Veuillez sélectionner une case", "error")
            case "enter":
                if current_menu in ("n_selection", "n_import_selection") and selected_size:
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
            case _:
                match current_menu:
                    case "n_selection" | "n_import_selection":
                        selected_size = int(str(selected_size) + event.name) if selected_size else int(event.name)
                        display_menu(current_menu, selected_size)
                    case "grid":
                        if cursor_position:
                            if grid.grid[cursor_position[0]][cursor_position[1]] == 0:
                                grid.grid[cursor_position[0]][cursor_position[1]] = int(event.name)
                                grid.player_cells.append(cursor_position)
                                display_menu("grid", grid=grid, cursor_position=cursor_position)
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
                    current_menu = "grid"
                    cursor_position = (0, 0)
                    grid = Grid(selected_size)
                    generate(grid, selected_difficulty)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "solver_selection":
                    current_menu = "grid"
                    backtracking_iteratif_pile(grid, player=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
        case "2":
            match current_menu:
                case "main":
                    current_menu = "rules"
                    display_menu(current_menu)
                case "mode_selection":
                    current_menu = "n_import_selection"
                    display_menu(current_menu)
                case "classique":
                    current_menu = "difficulty_selection"
                    selected_size = 9
                    display_menu(current_menu, selected_size)
                case "difficulty_selection":
                    selected_difficulty = "normal"
                    current_menu = "grid"
                    cursor_position = (0, 0)
                    grid = Grid(selected_size)
                    generate(grid, selected_difficulty)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
                case "solver_selection":
                    current_menu = "grid"
                    backtracking_recursif(grid, player=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
        case "3":
            match current_menu:
                case "main":
                    shutdown()
                case "classique":
                    current_menu = "difficulty_selection"
                    selected_size = 16
                    display_menu(current_menu, selected_size)
                case "difficulty_selection":
                    selected_difficulty = "hard"
                    current_menu = "grid"
                    cursor_position = (0, 0)
                    grid = Grid(selected_size)
                    generate(grid, selected_difficulty)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
        case "4":
            match current_menu:
                case "classique":
                    current_menu = "n_selection"
                    display_menu(current_menu, selected_size)
                case "solver_selection":
                    current_menu = "grid"
                    backtracking_mrv(grid, player=True)
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
        case "q":
            match current_menu:
                case "rules" | "mode_selection":
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
                    display_menu(current_menu)
                case "solver_selection":
                    current_menu = "grid"
                    display_menu(current_menu, grid=grid, cursor_position=cursor_position)
            selected_difficulty = None
        
        case "up"|"haut":
            if current_menu == "grid":
                if cursor_position:
                    if cursor_position[0] > 0:
                        cursor_position = (cursor_position[0] - 1, cursor_position[1])
                        display_menu("grid", grid=grid, cursor_position=cursor_position)
                else:
                    cursor_position = (0, 0)
                    display_menu("grid", grid=grid, cursor_position=cursor_position)
        case "down"|"bas":
            if current_menu == "grid":
                if cursor_position:
                    if cursor_position[0] < grid.size - 1:
                        cursor_position = (cursor_position[0] + 1, cursor_position[1])
                        display_menu("grid", grid=grid, cursor_position=cursor_position)
                else:
                    cursor_position = (0, 0)
                    display_menu("grid", grid=grid, cursor_position=cursor_position)
        case "left"|"gauche":
            if current_menu == "grid":
                if cursor_position:
                    if cursor_position[1] > 0:
                        cursor_position = (cursor_position[0], cursor_position[1] - 1)
                        display_menu("grid", grid=grid, cursor_position=cursor_position)
                else:
                    cursor_position = (0, 0)
                    display_menu("grid", grid=grid, cursor_position=cursor_position)
        case "right"|"droite":
            if current_menu == "grid":
                if cursor_position:
                    if cursor_position[1] < grid.size - 1:
                        cursor_position = (cursor_position[0], cursor_position[1] + 1)
                        display_menu("grid", grid=grid, cursor_position=cursor_position)
                else:
                    cursor_position = (0, 0)
                    display_menu("grid", grid=grid, cursor_position=cursor_position)

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
        case 'r':
            if current_menu == "grid":
                current_menu = "solver_selection"
                display_menu(current_menu)
        case 's':
            if current_menu == "grid":
                if selected_difficulty is None:
                    result = backtracking_mrv(grid)
                    message(f"Votre grille {"n'a pas de solution" if not result else "a une solution"}", "success" if result else "error")

        case _:
            message(f"Ceci est un message de debug : {event.name}", "info")
            message(logs, "info")

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
    clear_buffer()

    clear()
    message("Fermeture du programme", "info")
    
    global running
    running = False
