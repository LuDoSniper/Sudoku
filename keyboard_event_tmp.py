import os
import sys
import termios
from pynput import keyboard

def clear() -> None:
    """
    Efface le terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")

def set_terminal_mode(raw: bool = True) -> None:
    """
    Active ou désactive le mode brut pour éviter les artefacts d'affichage. (^[[A par exemple)
    """
    fd = sys.stdin.fileno()
    settings = termios.tcgetattr(fd)
    if raw:
        tty_mode = termios.tcgetattr(fd)
        tty_mode[3] = tty_mode[3] & ~termios.ICANON & ~termios.ECHO  # Désactive l'écho et le mode canonique
        termios.tcsetattr(fd, termios.TCSADRAIN, tty_mode)
    else:
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)

def on_press(key) -> None:
    """
    Fonction appelée lorsqu'une touche est pressée.
    Pour le moment, les event sont des exemples,
    et seules les fleches sont prises en compte.
    """
    try:
        clear()
        if key == keyboard.Key.up:
            print("Haut")
        elif key == keyboard.Key.down:
            print("Bas")
        elif key == keyboard.Key.left:
            print("Gauche")
        elif key == keyboard.Key.right:
            print("Droite")
    except AttributeError:
        pass


# Lancement du programme et configuration du terminal
set_terminal_mode(True)
print("Appuyez sur les flèches pour afficher leur direction (Ctrl+C pour quitter).")

# Main
try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Quitter
except KeyboardInterrupt:
    pass

# Reset du terminal avant de fermer le programme
finally:
    set_terminal_mode(False)
