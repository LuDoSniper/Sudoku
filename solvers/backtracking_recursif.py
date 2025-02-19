# Import
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Ajouter le dossier parent au PATH pour pouvoir importer les modules

# Custom import
# tools
from tools.find_next_empty import find_next_empty
from tools.find_next_empty import find_next_empty_mrv
from tools.is_valid import is_valid

def backtracking_recursif(grid, player: bool = False, indice: bool = False, use_heuristic: bool = False, use_random : bool = True) -> bool:
    """
    Solveur de Sudoku utilisant le backtracking récursif, renvoie True si la grille est résolue, False sinon.
    """
    
    size = grid.size
    # Trouver la prochaine case vide à remplir
    if use_heuristic:
        cell = find_next_empty_mrv(grid, size)
    else:
        cell = find_next_empty(grid, size)
    
    # Si aucune case vide n'est trouvée, la grille est complète et correcte
    if cell is None:
        return True
    row, col = cell  # Récupération des coordonnées de la case vide

    # Génération d'une liste des valeurs possibles + mélange
    possible_values = list(range(1, size + 1))
    if use_random:
        random.shuffle(possible_values)
    
    # Essai de chaque valeur dans la case vide
    for num in possible_values:
        if is_valid(grid, num, row, col):
            grid.grid[row][col] = num  # On place le nombre dans la case
            
            if player and (row, col) not in grid.player_cells:
                grid.player_cells.append((row, col))
            if indice and (row, col, num) not in grid.indice_cells:
                grid.indice_cells_buffer.append((row, col, num))

            if backtracking_recursif(grid, player=player, indice=indice, use_heuristic=use_heuristic):
                return True  # Si une solution a été trouvée, on arrête la recherche
            
            # Si la solution actuelle ne fonctionne pas, on annule l'affectation (backtracking)
            grid.grid[row][col] = 0  
            

            if player and (row, col) in grid.player_cells:
                grid.player_cells.pop(grid.player_cells.index((row, col)))
            if indice and (row, col, num) in grid.indice_cells_buffer:
                grid.indice_cells_buffer.pop(grid.indice_cells_buffer.index((row, col, num)))

    # Si aucune valeur ne fonctionne, la grille est dans un état non résoluble avec cette approche
    return False
