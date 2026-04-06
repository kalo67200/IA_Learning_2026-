# Mes Notes IA — Kaloyan

## Python — Bases

### Classe
Un modèle. Comme un moule à gâteau.
Tu définis la forme une fois, tu crées autant d'objets que tu veux.

### __init__
S'exécute automatiquement quand tu crées un objet.
C'est les informations de base — comme remplir une fiche.

### __repr__
Dit à Python comment afficher ton objet proprement.
Sans ça → affichage bizarre. Avec ça → affichage lisible.

### self
Représente l'objet lui-même dans une classe.
Quand tu écris `self.data` → tu accèdes à la donnée de CET objet.

---

## Micrograd

### Gradient
La pente. Répond à : "si je change x de 1, y change de combien ?"
Utilisé pour ajuster les poids dans la bonne direction.

### _prev
Stocke les parents d'une valeur.
Permet de savoir où remonter pendant backprop.
Exemple : c = a + b → c._prev = {a, b}

### _backward
Fonction vide au départ (lambda: None).
Remplie quand on fait une opération (+, *).
Contient la règle pour calculer les gradients à cet endroit.

### backprop()
Remonte automatiquement toute la chaîne des gradients.
Comme le Petit Poucet qui suit les cailloux en sens inverse.

### Règle de la chaîne
Si A influence B et B influence C :
gradient total = gradient(A→B) × gradient(B→C)
On multiplie les gradients locaux en remontant.

---

## PyTorch

### tensor
Equivalent de np.array mais pour PyTorch.
Permet la backpropagation automatique.

### requires_grad=True
Dit à PyTorch de mémoriser les calculs pour calculer les gradients.

### backward()
Calcule automatiquement tous les gradients.
Équivalent de notre backprop() dans micrograd.

### loss
Mesure l'erreur du réseau.
Plus c'est petit → mieux le réseau prédit.

---

## Makemore

### Bigramme
Paire de deux lettres consécutives.
"emma" → (e,m), (m,m), (m,a)

### one_hot
Transforme un index en vecteur de 0 et 1.
'e' = index 5 → [0,0,0,0,0,1,0,...,0]

### Matrice W (27×27)
27 entrées × 27 sorties.
Contient les poids du réseau pour prédire la lettre suivante.