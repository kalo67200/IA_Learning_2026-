import json
import difflib
import anthropic
import os
from dotenv import load_dotenv
from datetime import datetime
FICHIER = "taches.json"
def charger_taches():
    try:
        with open(FICHIER,"r") as f:
            toutes = json.load(f)
            aujourd_hui= datetime.now().strftime("%Y-%m-%d")
            taches_aujourd_hui = [t for t in toutes if aujourd_hui in t['date']]
            if taches_aujourd_hui:
                print(f"📝 Tes tâches d'aujourd'hui :")
                for t in taches_aujourd_hui:
                    print(f"- {t['titre']}{'✅'if t['faite'] else''}")
            else:   
                print("Aucune tâche pour aujourd'hui encore.")
        return taches_aujourd_hui
    except :
        print("⚠️ Aucun fichier trouvé. Démarrage à zéro.")
        taches_aujourd_hui = []
        return []


load_dotenv()
taches_aujourd_hui = charger_taches() 

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

taches = []
print("Entrez vos tâches une par une. Tapez 'fin' quand vous avez terminé.")

def collecter_taches():
    date = datetime.now().strftime("%Y-%m-%d")
    taches = []
    try: 
        with open(FICHIER,"r") as f:
            toutes = json.load(f)
            titres_existants = [t["titre"]for t in toutes ]
    except : 
        titres_existants = []
    while True:
        tache = input("Tâche : ")
        suggestions = difflib.get_close_matches(tache, titres_existants, n=1, cutoff=0.6)
        if suggestions:
            print(f"⚠️ Tu voulais dire '{suggestions[0]}' ? (oui/non)")
            reponse = input()
            if reponse == "oui":
                tache = suggestions[0]
        if tache.strip() == "fin":
            break
        taches.append({
            "titre": tache,
             "faite": False,
             "date": date
        })
    return taches

taches = collecter_taches()
print("\nQuelle tâche as-tu terminée ? (tape le numéro ou 'aucune')")




for i, t in enumerate(taches_aujourd_hui):
    print(f"{i+1}. {t['titre']}")

date = datetime.now().strftime("%Y-%m-%d")
def sauvegarder_taches(nouvelles_taches):
    try:
        with open(FICHIER,"r") as f:
            toutes = json.load(f)
    except :
        toutes = []
    toutes = toutes + nouvelles_taches
    with open(FICHIER,"w") as f:
        json.dump(toutes,f)
sauvegarder_taches(taches)

choix = input("Numéro : ")
def marquer_faite(taches_aujourd_hui):
    if choix.isdigit() and 0 < int (choix) <= len(taches_aujourd_hui):
        index =int(choix ) - 1 
        taches_aujourd_hui[index]["faite"] = True
        try:
            with open(FICHIER,"r") as f:
                toutes = json.load(f)
            for t in toutes:
                if t["titre"]== taches_aujourd_hui[index]["titre"]:
                    t["faite"] = True
            with open(FICHIER,"w") as f:
                json.dump(toutes,f)
            print(f"✅ Tâche marquée comme faite !")
        except:
            print("⚠️ Erreur fichier ")
    return taches_aujourd_hui
    
def afficher_stats():
    try:
        with open(FICHIER,"r") as f:
            toutes= json.load(f)
        total = len(toutes)
        faites = len([t for t in toutes if t["faite"]])
        restantes = total - faites
        taux = round((faites / total) * 100, 2) if total > 0 else 0
        print(f"Total : {total}")
        print(f"Faites : {faites} ✅")
        print(f"Restantes : {restantes}")
        print(f"Taux : {taux}%")
    except:
        print("⚠️ Aucune données!")

taches_aujourd_hui = marquer_faite(taches_aujourd_hui)
date = datetime.now().strftime("%Y-%m-%d")
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=150,
    messages=[
        {"role": "user", "content": f"Voici mes tâches : {taches_aujourd_hui}. Donne-moi un brief motivant en 2 lignes max."}
    ]
)
    
print(message.content[0].text)
print(f"\n✅ {date} {len(taches_aujourd_hui)} tâche(s) sauvegardée(s) dans {FICHIER}")

afficher_stats()