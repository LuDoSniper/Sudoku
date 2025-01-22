import os
from tools import terminal

# Lancement du programme et configuration du terminal
if os.name == "posix":
    terminal.set_terminal_mode(True)

# Boucle principale
terminal.mainloop()

# Reset du terminal avant de fermer le programme
if os.name == "posix":
    terminal.set_terminal_mode(False)
