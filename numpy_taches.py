import numpy as np 
import json 


with open("taches.json","r") as f: 
    taches = json.load(f)

print(taches)

donnees = []
for t in taches: 
    faite = 1 if t["faite"] else 0
    jour = int(t["date"].split("-")[2])
    donnees.append([faite,jour])

tableau = np.array(donnees)
print(tableau)
print(tableau.shape)
print(tableau.mean(axis=0))