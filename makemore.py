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
    mot_avec_tokens = '.' + mot + '.'
    for ch1 , ch2  in zip(mot_avec_tokens, mot_avec_tokens[1:]):
        paire  =(ch1, ch2 )
        compteur [paire] = compteur.get (paire, 0) + 1 
top5 = sorted (compteur.items(),key = lambda x : x[1], reverse = True )[:5]
for paire, count in top5 : 
    print(f"{paire[0]} -> {paire[1]} : {count} fois ")


total_a = sum(count for (ch1, ch2), count in compteur.items() if ch1 == 'a')

print(f"\nProbabilités après 'a' :")
probs_a = {}
for (ch1, ch2), count in compteur.items():
    if ch1 == 'a':
        probs_a[ch2] = count / total_a

top_a = sorted(probs_a.items(), key=lambda x: x[1], reverse=True)[:5]
for lettre, prob in top_a:
    print(f"  a → {lettre} : {prob:.3f}")




import random 

def generer_prenom():
    lettre = '.'
    prenom = ''
    
    while True:
        candidats = [(ch2, count) for (ch1, ch2), count in compteur.items() if ch1 == lettre]
        if not candidats:
            break
        total = sum(c for _, c in candidats)
        probs = [c/total for _, c in candidats]
        lettres_next = [c for c, _ in candidats]
        lettre = random.choices(lettres_next, weights=probs)[0]
        if lettre == '.':
            break
        prenom += lettre
    
    return prenom

for _ in range (5): 
    print (generer_prenom())
