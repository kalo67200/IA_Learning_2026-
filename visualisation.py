import numpy as np 
import matplotlib.pyplot as plt

X = np.array([[0],[1],[2],[3],[4]])
y = np.array([0,0,1,1,1])

poids = 0.0
biais = 0.0
learning_rate = 0.1
historique_poids = []

for i in range (10):
    for j in range (len(X)):
        prediction = poids * X[j][0]+ biais
        erreur = y[j] - prediction
        poids += learning_rate * erreur * X[j][0]
        biais += learning_rate * erreur 
    historique_poids.append(poids)


plt.plot(historique_poids)
plt.title("Evolution du poids pendant l'entrainement !")
plt.xlabel("Epoque ")
plt.ylabel("Poids")
plt.savefig("apprentissage.png")
print("Graphique sauvegardé !")
