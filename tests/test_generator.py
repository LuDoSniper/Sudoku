import unittest
import sys
import os
import timeit

# Ajoute le chemin du projet au PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Grid import Grid
from tools.generator import generate_full, calibrate
from tools.validator import verify

class TestGridGeneration(unittest.TestCase):

    def test_4x4_grid(self):
        grid = Grid(4)
        generate_full(grid)
        self.assertTrue(verify(grid), "La vérification de la grille 4x4 a échoué")
        calibrate(grid, "easy")  # Calibrage à des fins visuelles
        print(grid)

    def test_9x9_grid(self):
        grid = Grid(9)
        generate_full(grid)
        self.assertTrue(verify(grid), "La vérification de la grille 9x9 a échoué")
        calibrate(grid, "easy")  # Calibrage à des fins visuelles
        print(grid)

    def test_16x16_grid(self):
        grid = Grid(16)
        generate_full(grid)
        self.assertTrue(verify(grid), "La vérification de la grille 16x16 a échoué")
        calibrate(grid, "easy")  # Calibrage à des fins visuelles
        print(grid)
    
    # Prend plus de temps que l'âge de l'univers (c'est con)
    # def test_25x25_grid(self):
    #     grid = Grid(25)
    #     print("Grille créée")
    #     generate_full(grid)
    #     print("Grille générée")
    #     self.assertTrue(verify(grid), "La vérification de la grille 25x25 a échoué")
    #     print("Grille vérifiée")
    #     calibrate(grid, "easy")  # Calibrage à des fins visuelles
    #     print("Grille calibrée")
    #     print(grid)

if __name__ == '__main__':
    # unittest.main()
    time_elapsed = timeit.timeit(lambda: unittest.main(), number=1)
    print(f"Temps d'exécution: {time_elapsed:.2f} secondes")
