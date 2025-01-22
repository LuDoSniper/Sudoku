import os
import sys
if os.name == "posix":
    import termios
import keyboard
from tools.display_menu import display, message
from math import sqrt

# Variables globales
running = True
current_menu = "main"
selected_size = None
selected_difficulty = None

def clear() -> None:
    """
    Efface le terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

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

def display_menu(menu: str, n: int|None = None) -> None:
    clear()
    display(menu, n)

def on_press(event: keyboard.KeyboardEvent) -> None:
    """
    Fonction appelée lorsqu'une touche est pressée.
    """
    global current_menu
    global selected_size
    global selected_difficulty

    # Cas spéciale séparé pour une meilleure lisibilité (custom input)
    if event.name in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'backspace', 'enter'):
        match event.name:
            case "backspace":
                if current_menu in ("n_selection", "n_import_selection") and selected_size:
                    selected_size = int(str(selected_size)[:-1]) if len(str(selected_size)) > 1 else None
                    display_menu(current_menu, selected_size)
            case "enter":
                if current_menu in ("n_selection", "n_import_selection") and selected_size:
                    if selected_size > 0 and sqrt(selected_size) % 1 == 0:
                        if current_menu == "n_selection":
                            current_menu = "difficulty_selection"
                            display_menu(current_menu, selected_size)
                        elif current_menu == "n_import_selection":
                            message("Valeur valide", "success")
                            message("Fonctionnalité non implémentée pour le moment", "info")
                    else:
                        selected_size = None
                        display_menu(current_menu, selected_size)
                        message("Veuillez entrer un entier valide", "error")
            case _:
                if current_menu in ("n_selection", "n_import_selection"):
                    selected_size = int(str(selected_size) + event.name) if selected_size else int(event.name)
                    display_menu(current_menu, selected_size)

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
        case "3":
            match current_menu:
                case "main":
                    shutdown()
                case "classique":
                    current_menu = "difficulty_selection"
                    selected_size = 16
                    display_menu(current_menu, selected_size)
        case "4":
            match current_menu:
                case "classique":
                    current_menu = "n_selection"
                    display_menu(current_menu, selected_size)
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
        case _:
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

    clear()
    message("Fermeture du programme", "info")
    
    global running
    running = False
