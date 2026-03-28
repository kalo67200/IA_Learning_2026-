from sklearn.datasets import load_iris 
import numpy as np 

iris = load_iris()
X= iris.data 
y = iris.target 

print(f"Taille du dataset : {X.shape}")
print(f"Exemple de données : {X[0]}")
print(f"Catégories : {iris.target_names}")

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.2)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

score= model.score(X_test, y_test )
print(f"Précision : {score*100:.1f}%")
