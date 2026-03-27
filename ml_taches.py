import numpy as np 
import json
from sklearn.linear_model import LogisticRegression 

with open("taches.json", "r") as f: 
    taches =json.load(f)


X = np.array([[int(t["date"].split("-")[2])]for t in taches])
y = np.array([1 if t["faite"]else 0 for t in taches])

print("X (jours):", X.flatten())
print("y (faite):",y)


modele = LogisticRegression()
modele.fit(X,y)

prediction = modele.predict([[27]])
print(f"Jour 27 -> tache faite ? {'Oui' if prediction[0] == 1 else 'Non'}")

