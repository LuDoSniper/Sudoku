class Graphe:
    def __init__(self):
        """Initialise un graphe vide sous forme d'un dictionnaire d'adjacence."""
        self.adjacence = {}

    def ajouter_sommet(self, sommet, valeur):
        """Ajoute un sommet avec une valeur au graphe."""
        if sommet not in self.adjacence:
            self.adjacence[sommet] = {'valeur': valeur, 'liens': []}

    def ajouter_arête(self, sommet1, sommet2):
        """Ajoute une arête entre deux sommets (graphe non orienté)."""
        if sommet1 in self.adjacence and sommet2 in self.adjacence:
            self.adjacence[sommet1]['liens'].append(sommet2)
            self.adjacence[sommet2]['liens'].append(sommet1)

    def supprimer_sommet(self, sommet):
        """Supprime un sommet et toutes ses arêtes associées."""
        if sommet in self.adjacence:
            for voisin in self.adjacence[sommet]['liens']:
                self.adjacence[voisin]['liens'].remove(sommet)
            del self.adjacence[sommet]

    def supprimer_arête(self, sommet1, sommet2):
        """Supprime une arête entre deux sommets."""
        if sommet1 in self.adjacence and sommet2 in self.adjacence:
            if sommet2 in self.adjacence[sommet1]['liens']:
                self.adjacence[sommet1]['liens'].remove(sommet2)
            if sommet1 in self.adjacence[sommet2]['liens']:
                self.adjacence[sommet2]['liens'].remove(sommet1)

    def __str__(self):
        affichage = ""
        for sommet, data in self.adjacence.items():
            affichage += f"{sommet} (Valeur: {data['valeur']}) -> {data['liens']} \n"
        return affichage
    