# Futoshiki Solver

[![Codecov Coverage](https://codecov.io/gh/bernaborrero/futoshiki/branch/master/graph/badge.svg)](https://codecov.io/gh/bernaborrero/futoshiki)
![Github action badge](https://github.com/bernaborrero/futoshiki/workflows/Build%20and%20test/badge.svg)

## Description

Ce programme est un solveur pour les puzzles Futoshiki, un jeu de logique similaire aux grilles de Sudoku mais avec des contraintes d'inégalités entre certaines cases. Il est entièrement réalisé en Python et utilise un algorithme de recherche pour trouver toutes les solutions possibles d'une grille de Futoshiki donnée.

## Fonctionnalités

- **Création de puzzles Futoshiki** : Génère des grilles de Futoshiki aléatoires avec des contraintes d'inégalités.
- **Choix du nombre de contraintes** : Permet de sélectionner le nombre de contraintes d'inégalités pour ajuster la complexité du puzzle.
- **Résolution automatique** : Trouve toutes les solutions possibles pour une grille de Futoshiki donnée, respectant les contraintes de ligne/colonne et les inégalités spécifiées.
- **Affichage des solutions** : Visualise facilement les solutions trouvées.

## Exécution

Pour exécuter le programme et résoudre un puzzle Futoshiki, assurez-vous d'avoir Python installé, puis lancez les commandes suivantes :

```bash
# Cloner le dépôt
git clone https://github.com/bernaborrero/futoshiki.git

# Naviguer dans le dossier
cd futoshiki

# Exécuter le solveur
python futoshiki_solver.py
