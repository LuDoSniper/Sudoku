import unittest
import sys
import os

# Ajoute le chemin du projet au PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.ChainedList import ChainedList

class TestChainedList(unittest.TestCase):

    def setUp(self):
        self.head = ChainedList({"name": "Tanguy"})
        self.head.append({"name": "Romain"})
        self.head.append({"name": "Nathan"})
        self.head.append({"name": "Théo"})
        self.head.append({"name": "Léo"})
        self.head.append({"name": "Eliott"})
        self.head.append({"name": "Arthur"})
        self.head.append({"name": "Alexandre"})
        return super().setUp()
    
    def test_get_size(self):
        self.assertEqual(self.head.get_size(), 8)

    def test_get_data(self):
        self.assertEqual(self.head.get_data(), {"name": "Tanguy"})
    
    def test_pop(self):
        self.head, result = self.head.pop() # Output: {"name": "Alexandre"}
        self.assertEqual(result, {"name": "Alexandre"})
        self.head, result = self.head.pop(1) # Output: {'name': 'Romain'}
        self.assertEqual(result, {"name": "Romain"})
        self.head, result = self.head.pop(0) # Output: {'name': 'Tanguy'}
        self.assertEqual(result, {"name": "Tanguy"})
        self.head, result = self.head.pop(-1) # Output: {"name": "Arthur"}
        self.assertEqual(result, {"name": "Arthur"})

        self.head = ChainedList({"name": "Tanguy"})
        self.head, result = self.head.pop() # Output: {"name": "Tanguy"}
        self.assertEqual(result, {"name": "Tanguy"})
        self.assertEqual(self.head, None)

        self.head = ChainedList({"name": "Tanguy"})
        self.head, result = self.head.pop(0) # Output: {"name": "Tanguy"}
        self.assertEqual(result, {"name": "Tanguy"})
        self.assertEqual(self.head, None)

if __name__ == '__main__':
    unittest.main()
