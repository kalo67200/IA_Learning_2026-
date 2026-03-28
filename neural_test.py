import numpy as np 


X = np.array([[0],[1], [2], [3], [4]])
y = np.array([0, 0, 1, 1, 1])

poids = 0.0
biais = 0.0
learning_rate = 0.1 

for i in range(10):
    for j in range(len(X)):
        prediction = poids * X[j][0] + biais
        erreur = y[j] - prediction
        poids += learning_rate * erreur * X[j][0]
        biais += learning_rate * erreur

print(f"Poids final : {poids:.2f}")
print(f"Biais final : {biais:.2f}")
print(f"Prédiction pour X=5 : {poids * 5 + biais:.2f}")

