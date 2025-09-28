
# 📘 Assignment: Hangman Game in Python

## 🎯 Objective

Créer le jeu du pendu en Python : l’élève va concevoir un jeu interactif où le joueur doit deviner un mot caché lettre par lettre avant d’épuiser ses essais. Ce projet développe la manipulation de chaînes, les boucles, les conditions et la gestion d’entrées utilisateur.

## 📝 Tasks

### 🛠️ Task 1: Word Selection & Setup

#### Description
Écrire une fonction qui sélectionne aléatoirement un mot dans une liste prédéfinie et initialise les variables du jeu (mot caché, essais restants, lettres déjà proposées).

#### Requirements
Completed program should:

- Sélectionner un mot au hasard dans une liste de mots
- Initialiser le nombre d’essais (ex : 6)
- Préparer l’affichage du mot sous forme de tirets (_ _ _)

### 🛠️ Task 2: Game Loop & User Interaction

#### Description
Implémenter la boucle principale du jeu : demander une lettre à l’utilisateur, mettre à jour l’affichage, gérer les essais et déterminer la victoire ou la défaite.

#### Requirements
Completed program should:

- Demander une lettre à chaque tour
- Afficher le mot avec les lettres trouvées et les tirets pour les lettres manquantes
- Afficher le nombre d’essais restants
- Terminer le jeu si le mot est trouvé ou si les essais sont épuisés
- Afficher un message de victoire ou de défaite

#### Exemple d’affichage
```python
Mot à deviner : _ _ _ _ _
Propose une lettre : a
Mot à deviner : a _ _ _ _
Essais restants : 5
```
