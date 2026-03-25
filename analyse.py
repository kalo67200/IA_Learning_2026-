import json 

with open("taches.json","r") as f:
    taches = json.load(f)
    dates_uniques = set([t["date"] for t in taches])
    print(dates_uniques)
    
    resultats = {}
    for date in dates_uniques:
        taches_du_jour = [t for t in taches if t["date"] == date]
        total = len(taches_du_jour)
        faites = len([t for t in taches_du_jour if t["faite"]])
        taux  = round((faites/total)*100,2)
        resultats[date] = taux 

    print(resultats)
    meilleur_jour = max(resultats, key=resultats.get)
    print(f"🏆 Ton jour le plus productif : {meilleur_jour} ({resultats[meilleur_jour]}%)")
       