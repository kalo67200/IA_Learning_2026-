fruit = ["banane", "mangue", "fraise"]

for i, fruit in enumerate (fruit):
    print(f"{i+1}, {fruit}")

dictionnaire = {}
dictionnaire ['France'] =  'Paris '
dictionnaire ['Brésil'] = 'Brazilia'
dictionnaire ['US  '] = 'Washington'

for pays, capitale in dictionnaire.items(): 
    print( f" La capitale {pays} est {capitale}")


def saluer(prenom): 
    texte_cree =  f" Bonjour {prenom}"
    return texte_cree  

message = saluer("Thomas")
print(message)