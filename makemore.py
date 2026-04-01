lettres = 'abcdefghijklmnopqrstuvwxyz'
char_to_idx = {c: i for i, c in enumerate(lettres)}
idx_to_char = {i: c for i, c in enumerate(lettres)}


mots = open('names.txt').read().splitlines()
print(f"Nombre de prénoms  : {len(mots)}")
print(f"Exemples : {mots[:5]}")

for mot in mots [:3]: 
    print(f"\nMot : {mot}")
    for ch1, ch2 in zip(mot, mot[1:]): 
        print(f"{ch1} -> {ch2}")

compteur = {}
for mot in mots :
    for ch1 , ch2  in zip(mot, mot[1:]):
        paire  =(ch1, ch2 )
        compteur [paire] = compteur.get (paire, 0) + 1 
top5 = sorted (compteur.items(),key = lambda x : x[1], reverse = True )[:5]
for paire, count in top5 : 
    print(f"{paire[0]} -> {paire[1]} : {count} fois ")
    
