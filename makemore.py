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