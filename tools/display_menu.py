import shutil
import textwrap
from colorama import Fore

def get_terminal_width() -> int:
    return shutil.get_terminal_size().columns

def message(message: str, type: str) -> None:
    match type:
        case "error":
            print(f"[{Fore.RED}ERROR{Fore.RESET}] : {message}")
        case "info":
            print(f"[{Fore.CYAN}INFO{Fore.RESET}] : {message}")
        case "success":
            print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] : {message}")
        case _:
            raise ValueError("Type de message invalide")

def main_menu() -> None:
    width = 30

    print(f"{Fore.LIGHTBLACK_EX}'esc' pour quitter{Fore.RESET}")
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'SUDOKU'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'1. Jouer'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'2. Règles'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'3. Quitter'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def rules_menu() -> None:
    width = 50
    
    rules = textwrap.fill('Le Sudoku se joue sur une grille n x n cases, divisée en racine(n) x racine(n) sous-grilles. Remplissez la grille avec les chiffres de 1 à n. Chaque ligne, colonne et sous-grille doivent contenir ces chiffres une seule fois.', width)
    formated_rules = ""
    for line in rules.split("\n"):
        formated_rules += f"{Fore.BLUE}│ {Fore.RESET}{line.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}\n"
    formated_rules = formated_rules[:-1]

    print(f"{Fore.LIGHTBLACK_EX}'esc' pour quitter{Fore.RESET}")
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'RÈGLES'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(formated_rules)
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def mode_selection_menu() -> None:
    width = 30
    
    print(f"{Fore.LIGHTBLACK_EX}'esc' pour quitter{Fore.RESET}")
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'SUDOKU'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'1. Mode classique'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'2. Importer sa grille'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def classique_menu() -> None:
    width = 30

    print(f"{Fore.LIGHTBLACK_EX}'esc' pour quitter{Fore.RESET}")
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
    width = 30
    n = n if n else ""

    print(f"{Fore.LIGHTBLACK_EX}'esc' pour quitter{Fore.RESET}")
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{'SUDOKU'.center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{('Choisir un entier : ' + str(n)).ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def difficulty_selection_menu(n: int|None = None) -> None:
    width = 30
    n = n if n else ""

    print(f"{Fore.LIGHTBLACK_EX}'esc' pour quitter{Fore.RESET}")
    print(f"{Fore.BLUE}┌{'─' * (width + 2)}┐{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.CYAN}{('SUDOKU ' + str(n) + 'x' + str(n)).center(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}├{'─' * (width + 2)}┤{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'1. Facile'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'2. Normal'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'3. Difficile'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {' ' * width} │{Fore.RESET}")
    print(f"{Fore.BLUE}│ {Fore.GREEN}{'q. Retour'.ljust(width, ' ')}{Fore.BLUE} │{Fore.RESET}")
    print(f"{Fore.BLUE}└{'─' * (width + 2)}┘{Fore.RESET}")

def display(menu: str, n: int|None = None) -> None:
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
        case _:
            message("Menu invalide", "error")
