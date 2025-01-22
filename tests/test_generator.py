import unittest
import sys
import os

# Ajoute le chemin du projet au PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.Grid import Grid
from tools.generator import generate_full, calibrate
from tools.validator import verify

class TestGridGeneration(unittest.TestCase):

    def test_4x4_grid(self):
        """Test de génération et vérification d'une grille 4x4."""
        grid = Grid(4)
        generate_full(grid)
        self.assertTrue(verify(grid), "La vérification de la grille 4x4 a échoué")
        calibrate(grid, "easy")  # Calibrage à des fins visuelles
        print(grid)

    def test_9x9_grid(self):
        """Test de génération et vérification d'une grille 9x9."""
        grid = Grid(9)
        generate_full(grid)
        self.assertTrue(verify(grid), "La vérification de la grille 9x9 a échoué")
        calibrate(grid, "easy")  # Calibrage à des fins visuelles
        print(grid)

    def test_16x16_grid(self):
        """Test de génération et vérification d'une grille 16x16."""
        grid = Grid(16)
        generate_full(grid)
        self.assertTrue(verify(grid), "La vérification de la grille 16x16 a échoué")
        calibrate(grid, "easy")  # Calibrage à des fins visuelles
        print(grid)

if __name__ == '__main__':
    unittest.main()
