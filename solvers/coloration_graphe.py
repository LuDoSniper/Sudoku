import sys
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.dessiner_graphe_sudoku import dessiner_graphe_sudoku

from models.Grid import Grid
from models.SudokuGraphe import SudokuGraphe

def valide(sudoku_graphe, cellule, valeur):
    """
    Vérifie si la valeur peut être placée dans la cellule sans violer les règles du Sudoku.
    """
    voisins = sudoku_graphe.adjacence[cellule]['liens']

    for voisin in voisins:
        if sudoku_graphe.valeurs[voisin] == valeur:  # Conflit avec un voisin
            return False
    
    return True  # Valeur valide


def resolve(sudoku_graphe, liste_cellules, index, ax):
    """
    Tente de résoudre le Sudoku en essayant différentes valeurs dans chaque cellule.
    """
    # Si toutes les cellules sont remplies, on a terminé
    if index == len(liste_cellules):
        return True

    # Récupérer la cellule actuelle
    cellule = liste_cellules[index]

    # Si la cellule a déjà une valeur, passer à la suivante
    if sudoku_graphe.valeurs[cellule] != 0:
        return resolve(sudoku_graphe, liste_cellules, index + 1, ax)

    # Essayer toutes les valeurs possibles (1 à taille)
    for valeur in range(1, sudoku_graphe.size + 1):
        if valide(sudoku_graphe, cellule, valeur):
            # Assigner la valeur
            sudoku_graphe.valeurs[cellule] = valeur
            sudoku_graphe.adjacence[cellule]['valeur'] = valeur

            dessiner_graphe_sudoku(sudoku_graphe, ax)

            # Continuer avec la cellule suivante
            if resolve(sudoku_graphe, liste_cellules, index + 1, ax):
                return True  # Succès, on arrête

            # Si la valeur ne fonctionne pas, annuler
            sudoku_graphe.valeurs[cellule] = 0
            sudoku_graphe.adjacence[cellule]['valeur'] = 0

            dessiner_graphe_sudoku(sudoku_graphe, ax)

    # Si aucune valeur ne fonctionne, retour arrière
    plt.ioff()  # Désactive le mode interactif après exécution
    plt.show()  # Garde la dernière figure ouverte
    return False


def colorier_sudoku(grid: Grid) -> SudokuGraphe:
    """
    Remplit le Sudoku en utilisant un algorithme de coloration de graphe.
    Modifie directement le SudokuGraphe donné en argument.
    """
    # Créer le graphe du Sudoku
    sudoku_graphe = SudokuGraphe(grid)

    # Récupérer la liste des cellules du graphe
    plt.ion()  # Active le mode interactif
    fig, ax = plt.subplots(figsize=(6, 6))

    # Dessiner l'état initial du graphe
    ax = dessiner_graphe_sudoku(sudoku_graphe, ax)

    # Lancer la résolution
    liste_cellules = list(sudoku_graphe.adjacence.keys())
    resolve(sudoku_graphe, liste_cellules, 0, ax)

    plt.ioff()  # Désactive le mode interactif après la résolution
    plt.show()  # Garde le dernier état affiché

    return sudoku_graphe
