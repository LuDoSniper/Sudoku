# Sudoku Terminal Interactif

Un jeu de **Sudoku** en mode terminal, développé en Python. Ce projet se distingue par une interface innovante qui capte les entrées directement, à l'image de *nudoku* sous Linux, sans utiliser la fonction classique `input()`.

## Fonctionnalités

- **Génération de grilles** : Créez des grilles de Sudoku de tailles variées (4x4, 9x9, 16x16, ou nxn).
- **Complétion interactive** : Complétez la grille en temps réel dans le terminal.
- **Indices intelligents** : Obtenez des indices grâce à **4 algorithmes différents**.
- **Vérification de solution** : Contrôlez la validité de votre solution à tout moment.
- **Choix du niveau de difficulté** : Sélectionnez le niveau qui correspond à votre expertise.
- **Résolution automatique** : Demandez la résolution complète du Sudoku ou même la génération automatique de grilles.
- **Visualisation graphique** : Affichez la grille sous forme de graphe.
- **Coloration de graphe progressive** : Observez la résolution par coloration de graphe, qui s'anime progressivement.
- **Importation de grilles** : Importez votre propre grille, vérifiez sa solvabilité et jouez avec les mêmes options qu'une grille générée.
- **Consultation des règles** : Accédez aux règles du Sudoku directement depuis le terminal.
- **Benchmarking des algorithmes** : Mesurez le temps d'exécution moyen de chaque algorithme (chaque algo est exécuté 5 fois pour obtenir une moyenne).

## Installation

Il est **préférable d'utiliser Windows** pour ce projet, car des problèmes mineurs peuvent survenir sous Linux. Bien que nous ayons fait de notre mieux pour assurer une compatibilité inter-OS, Linux n'est pas encore officiellement pris en charge. Le programme devrait normalement tourner sur Linux, mais nous n'avons pas encore effectué suffisamment de tests pour en garantir le fonctionnement optimal.

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/LuDoSniper/Sudoku.git
   ```

2. **Se placer dans le répertoire du projet :**

   ```bash
   cd Sudoku
   ```

3. **Installer les dépendances avec `requirements.txt` :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Exécuter le programme :**

   __Sous windows__ :

   ```bash
   python main.py
   ```

   __Sous Linux__ : *Le programme à besoin des privilèges administrateur*

   ```bash
   sudo python main.py
   ```

## Utilisation

Le projet est entièrement interactif via le terminal. Dès son lancement, suivez les instructions à l'écran pour :

- Générer une nouvelle grille.
- Compléter la grille existante.
- Obtenir des indices en sélectionnant l'algorithme de votre choix.
- Vérifier votre solution.
- Importer et tester la solvabilité d'une grille personnalisée.
- Visualiser la grille sous forme de graphe et observer la coloration progressive.
- Lancer des benchmarks pour comparer les performances des différents algorithmes.

## Contribuer

Les contributions sont les bienvenues !  
Si vous souhaitez améliorer le projet, ajouter des fonctionnalités ou corriger des bugs, n'hésitez pas à :
- Ouvrir une [issue](https://github.com/LuDoSniper/Sudoku/issues) pour discuter de vos idées.
- Soumettre une *pull request* avec vos modifications.

## Contact

Pour toute question ou suggestion, merci d'ouvrir une [issue](https://github.com/LuDoSniper/Sudoku/issues) sur le dépôt GitHub.

---

*Bon jeu et bonnes résolutions !*