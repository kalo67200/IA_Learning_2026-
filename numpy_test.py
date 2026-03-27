import numpy as np 

tableau = np.array([1, 2, 3, 4, 5])
print(tableau.mean())
print(tableau.sum())
print(tableau.max())




taux = np.array([100.0, 50.0, 75.0, 33.0])
print(f"Moyenne des taux : {taux.mean()}%")
print(f"Meilleur taux : {taux.max()}%")
print(f"Pire : {taux.min()}%")