# Imports
import shutil
import textwrap
from colorama import Fore, Back

# Custom imports
# models
from models.Grid import Grid
from models.Char import Char
# tools
from tools.timer import time_all

def get_quit_commands_message() -> str:
    """
    Retourne le message pour quitter le programme
    """
    return f"{Fore.LIGHTBLACK_EX}'esc' pour quitter{Fore.RESET}"

def get_terminal_width() -> int:
    """
    Retourne la largeur du terminal
    """
    return shutil.get_terminal_size().columns

def message(message: str, type: str) -> None:
    """
    Affiche un message coloré en fonction du type
    """
    match type:
        case "error":
            print(f"[{Fore.RED}ERROR{Fore.RESET}] : {message}")
        case "info":
            print(f"[{Fore.CYAN}INFO{Fore.RESET}] : {message}")
        case "success":
            print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] : {message}")
        case "warning":
            print(f"[{Fore.YELLOW}WARNING{Fore.RESET}] : {message}")
        case "debug":
            print(f"[{Fore.LIGHTBLUE_EX}DEBUG{Fore.RESET}] : {message}")
        case _:
            raise ValueError("Type de message invalide")

def main_menu() -> None:
    """
    Affiche le menu principal
    """
    width = 40

    print(get_quit_commands_message())
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'SUDOKU'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'1. Jouer'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'2. Règles'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'3. Moyenne des temps d\'execution'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'4. Quitter'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def rules_menu() -> None:
    """
    Affiche les règles du Sudoku
    """
    width = 50
    
    rules = textwrap.fill('Le Sudoku se joue sur une grille n x n cases, divisée en racine(n) x racine(n) sous-grilles. Remplissez la grille avec les chiffres de 1 à n. Chaque ligne, colonne et sous-grille doivent contenir ces chiffres une seule fois.', width)
    formated_rules = ""
    for line in rules.split("\n"):
        formated_rules += f"{Fore.BLUE}│ {Fore.RESET}{line.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}\n"
    formated_rules = formated_rules[:-1]

    print(get_quit_commands_message())
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'RÈGLES'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(formated_rules)
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def mode_selection_menu() -> None:
    """
    Affiche le menu de sélection du mode de jeu
    """
    width = 30
    
    print(get_quit_commands_message())
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'SUDOKU'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'1. Mode classique'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'2. Importer sa grille'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def classique_menu() -> None:
    """
    Affiche le menu de sélection de la taille du Sudoku
    """
    width = 30

    print(get_quit_commands_message())
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'SUDOKU'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'1. 4x4'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'2. 9x9'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'3. 16x16'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'4. nxn'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def n_selection(n: int|None = None) -> None:
    """
    Affiche le menu de sélection de la taille du Sudoku (custom input)
    """
    width = 30
    n = n if n else ""

    print(get_quit_commands_message())
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'SUDOKU'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{('Choisir un entier : ' + str(n)).ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def difficulty_selection_menu(n: int|None = None) -> None:
    """
    Affiche le menu de sélection de la difficulté du Sudoku
    """
    width = 30
    n = n if n else ""

    print(get_quit_commands_message())
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{('SUDOKU ' + str(n) + 'x' + str(n)).center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'1. Facile'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'2. Normal'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'3. Difficile'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def algo_selection(message: str, graph: bool = True) -> None:
    """
    Affiche le menu de sélection de l'algorithme
    """
    width = 30

    print(get_quit_commands_message())
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{(f"SUDOKU - {message}").center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'1. Backtracking itératif'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'2. Backtracking récursif'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'3. Heuristique itératif'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'4. Heuristique récursif'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    if graph:
        print(f"{Fore.BLUE}│ {Fore.GREEN}{'5. Coloration de graphe'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def algo_times() -> None:
    """
    Affiche les moyennes des temps d'execution des algorithmes
    """
    width = 43

    message("Samples : 100 pour size < 16 ; Samples : 10 pour size >= 16", "info")
    message("Calcul des moyennes de temps d'execution...", "info")
    times = time_all()
    from tools.terminal import clear
    clear()

    print(get_quit_commands_message())
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{(f"SUDOKU - BENCHMARK").center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.LIGHTBLUE_EX}{(f"GENERATION").center(width, '─')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{(f"4x4").center(width, '─')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking itératif : {times[0][0][0]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking récursif : {times[0][0][1]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique itératif  : {times[0][0][2]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique récursif  : {times[0][0][3]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{(f"9x9").center(width, '─')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking itératif : {times[0][1][0]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking récursif : {times[0][1][1]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique itératif  : {times[0][1][2]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique récursif  : {times[0][1][3]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{(f"16x16").center(width, '─')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking itératif : {times[0][2][0]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking récursif : {times[0][2][1]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique itératif  : {times[0][2][2]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique récursif  : {times[0][2][3]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.LIGHTBLUE_EX}{(f"RESOLUTION").center(width, '─')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{(f"4x4").center(width, '─')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking itératif : {times[1][0][0]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking récursif : {times[1][0][1]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique itératif  : {times[1][0][2]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique récursif  : {times[1][0][3]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{(f"9x9").center(width, '─')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking itératif : {times[1][1][0]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking récursif : {times[1][1][1]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique itératif  : {times[1][1][2]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique récursif  : {times[1][1][3]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{(f"16x16").center(width, '─')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking itératif : {times[1][2][0]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Backtracking récursif : {times[1][2][1]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique itératif  : {times[1][2][2]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{f'Heuristique récursif  : {times[1][2][3]:.8f} secondes'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def decolor_string(string: str) -> str:
    """
    Retire les couleurs d'une chaîne de caractères
    """
    colors = (
        Fore.RESET,
        Fore.BLACK,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.YELLOW,
        Fore.LIGHTBLACK_EX,
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTRED_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.LIGHTYELLOW_EX,
    )
    formated_string = string
    for color in colors:
        formated_string = formated_string.replace(color, "")
    return formated_string

def get_first_color(string: str) -> str|None:
    """
    Renvois la première couleur trouvée dans une chaîne de caractères
    """
    colors = (
        Fore.RESET,
        Fore.BLACK,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.YELLOW,
        Fore.LIGHTBLACK_EX,
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTRED_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.LIGHTYELLOW_EX,
    )
    indexes = []
    for color in colors:
        if color in string:
            indexes.append((string.index(color), color))
    
    if indexes:
        return min(indexes)[1]
    return None


def decolor_string_v2(string: str) -> list[Char]:
    """
    Retire les couleurs d'une chaîne de caractères
    et renvois une liste de chaque charactère avec sa couleur
    et sa couleur de background associées
    """
    chars = []
    last_color = Fore.RESET
    color = get_first_color(string)
    while color and color in string:
        index = string.index(color)
        for char in string[:index]:
            chars.append(Char(char, last_color))
        string = string[index + len(color):]
        last_color = color
        color = get_first_color(string)
    if string:
        for char in string:
            chars.append(Char(char, last_color))
    return chars

def recolor_string(chars: list[Char]) -> str:
    """
    Recolorie une liste de caractères
    """
    string = ""
    for char in chars:
        string += char.__str__()
    return string

def grid_menu(grid: Grid, cursor_pos: tuple[int], imported: bool = False, input: bool = False) -> None:
    """
    Affiche la grille de Sudoku
    """
    lines = grid.__str__().split("\n")
    add = 1 if grid.size > 9 else 0
    index_y, index_x = cursor_pos[0] * 2 + 1, cursor_pos[1] * (4 + add) + 1 + 1

    selected_line = lines[index_y]
    
    decolored_line = decolor_string_v2(selected_line)
    left = decolored_line[:index_x]
    if grid.size > 9: 
        centers = decolored_line[index_x: index_x + grid.get_max_width()]
    else:
        centers = decolored_line[index_x]
    right = decolored_line[index_x + (grid.get_max_width() - 1 if grid.size > 9 else 0) + 1:]
    
    if isinstance(centers, list):
        for center in centers:
            center.back = Back.CYAN
    else:
        centers.back = Back.CYAN
    right[0].back = Back.RESET
    if isinstance(centers, list):
        center = centers
    else:
        center = [centers]
    selected_line = left + center + right
    
    lines[index_y] = recolor_string(selected_line)

    print(get_quit_commands_message())
    for line in lines:
        print(line)
    
    print()
    if not imported:
        print(f"Déplacements                   : {Fore.GREEN}flèches directionnelles{Fore.RESET}")
        if not input:
            print(f"Entrer un nombre               : {Fore.GREEN}1-9{Fore.RESET}")
        else:
            print(f"Entrer un nombre               : {Fore.GREEN}'e'{Fore.RESET}")
        print(f"Supprimer un nombre            : {Fore.GREEN}'backspace'{Fore.RESET}")
        print(f"Annuler                        : {Fore.GREEN}'b'{Fore.RESET}")
        print(f"Indice                         : {Fore.GREEN}'i'{Fore.RESET}")
        print(f"Vérifier la grille             : {Fore.GREEN}'v'{Fore.RESET}")
        print(f"Résoudre la grille             : {Fore.GREEN}'r'{Fore.RESET}")
        print(f"Afficher le graphe             : {Fore.GREEN}'g'{Fore.RESET}")
        print(f"Quitter vers le menu principal : {Fore.GREEN}'q'{Fore.RESET}")
    else:
        print(f"Déplacements                       : {Fore.GREEN}flèches directionnelles{Fore.RESET}")
        if not input:
            print(f"Entrer un nombre                   : {Fore.GREEN}1-9{Fore.RESET}")
        else:
            print(f"Entrer un nombre                   : {Fore.GREEN}'e'{Fore.RESET}")
        print(f"Supprimer un nombre                : {Fore.GREEN}'backspace'{Fore.RESET}")
        print(f"Annuler                            : {Fore.GREEN}'b'{Fore.RESET}")
        print(f"Vérifier la grille                 : {Fore.GREEN}'v'{Fore.RESET}")
        print(f"Résoudre la grille                 : {Fore.GREEN}'r'{Fore.RESET}")
        print(f"Afficher le graphe                 : {Fore.GREEN}'g'{Fore.RESET}")
        print(f"Vérifier si il existe une solution : {Fore.GREEN}'s'{Fore.RESET}")
        print(f"Jouer sur la grille                : {Fore.GREEN}'j'{Fore.RESET}")
        print(f"Quitter vers le menu principal     : {Fore.GREEN}'q'{Fore.RESET}")
    print()

def display(menu: str, n: int|None = None, grid: Grid|None = None, cursor_position: tuple[int]|None = None, imported: bool = False, input: bool = False) -> None:
    """
    Etablit la correspondance entre le menu et la fonction à appeler
    """
    match menu:
        case "main":
            main_menu()
        case "rules":
            rules_menu()
        case "mode_selection":
            mode_selection_menu()
        case "classique":
            classique_menu()
        case "n_selection" | "n_import_selection":
            n_selection(n)
        case "difficulty_selection":
            difficulty_selection_menu(n)
        case "solver_selection":
            algo_selection("SOLVER")
        case "generator_selection":
            algo_selection("GENERATOR", graph=False)
        case "indice_selection":
            algo_selection("INDICE", graph=False)
        case "algo_times":
            algo_times()
        case "grid":
            grid_menu(grid, cursor_position, imported=imported, input=input)
        case _:
            message("Menu invalide", "error")
