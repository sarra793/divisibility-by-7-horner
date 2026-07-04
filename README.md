# divisibility-by-7-horner7

🧮 Description

Ce projet est une application graphique développée avec PyQt5 qui permet de vérifier si un nombre entier est divisible par 7 en utilisant une méthode algorithmique en 3 étapes :

Transformation des chiffres modulo 7
Regroupement des chiffres par tranches
Application de l’algorithme de Horner
⚙️ Fonctionnement de l’algorithme
🔹 Étape 1 : Transformation des chiffres

Chaque chiffre du nombre X est remplacé par son reste modulo 7.

Exemple :

X = 552757982
Y = 552050212
🔹 Étape 2 : Regroupement par tranches

Le nombre Y est découpé en blocs de 1 ou 2 chiffres à partir de la droite.
Chaque bloc est remplacé par son reste modulo 7.

Exemple :

Y = 552050212
Tranches : 12 | 02 | 05 | 52 | 5
Z = 53525
🔹 Étape 3 : Algorithme de Horner

Le nombre Z est évalué modulo 7 avec Horner :

M = 0
M = (M * 10 + chiffre) % 7
🖥️ Interface utilisateur

L’application contient :

un champ de saisie pour le nombre
un bouton de vérification
une zone de message affichant le résultat
▶️ Utilisation
Lancer le programme Python
Entrer un nombre entre 5 et 20 chiffres
Cliquer sur le bouton
Voir si le nombre est divisible par 7
📦 Technologies utilisées
Python 3
PyQt5
