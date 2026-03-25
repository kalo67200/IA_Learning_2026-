import json
from flask import Flask, request, redirect
from datetime import datetime
import anthropic
import os 
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
FICHIER = "taches.json"

@app.route("/")
def accueil():
    try:
        with open(FICHIER, "r") as f:
            taches = json.load(f)
    except:
        taches = []


    html = """
    <html>
    <head>
    <style>
        body {font-family : Arial; max-width: 600px; margin: 50px auto; background: #0B0F19; color: white;}
        h1 { color: #00F0FF; }
        input{padding: 8px; width: 300px; border-radius: 5px; border: none}
        button { padding: 8px 16px; background: #00F0FF; border: none; border-radius: 5px; cursor: pointer;}
        li { list-style: none; padding: 10px; margin: 5px 0; background: #1a1f2e; border-radius: 5px; }
        a { color: #FF007F; text-decoration: none; margin-left: 10px; }
    </style>
    </head>
    <body>
    <h1>📝 Mes tâches du jour</h1>
    """

    html += "<form method='POST' action='/ajouter'>"
    html += "<input name='titre' placeholder='Nouvelle tâche...'>"
    html += "<button type='submit'>Ajouter</button>"
    html += "</form><ul>"
    html+= "<a href='/stats'>📊 Voir les stats</a><br><br>"
    html += "<a href='/brief'>🤖 Brief IA</a><br><br>"
    html += "<a href='/analyse'>📈 Analyse de productivité</a><br><br>"



    for t in taches:
        statut = "✅" if t["faite"] else "⬜"
        html += f"<li>{statut} {t['titre']} <a href='/marquer/{taches.index(t)}'>✔ </a></li>"

    html += "</body></html>"
    return html

@app.route("/ajouter", methods=["POST"])
def ajouter():
    titre = request.form["titre"]
    date = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(FICHIER, "r") as f:
            taches = json.load(f)
    except:
        taches = []
    taches.append({"titre": titre, "faite": False, "date": date})
    with open(FICHIER, "w") as f:
        json.dump(taches, f)
    return redirect("/")

@app.route("/marquer/<int:index>")
def marquer(index):
    try:
        with open(FICHIER,"r") as f: 
            taches= json.load(f)
        taches[index]["faite"]= True 
        with open(FICHIER, "w") as f:
            json.dump(taches,f)
    except : 
        pass
    return redirect("/")


@app.route("/stats")
def stats():
    try:
        with open(FICHIER,"r") as f:
            taches= json.load(f)
    except:
        taches = []

    total = len(taches)
    faites = len([t for t in taches if t["faite"]])
    restantes = total - faites 
    taux = round((faites / total)*100, 2) if total > 0 else 0

    html = f"""
    <html><head><style>
        body{{ font-family: Arial; max-width:600px; margin: 50px auto; background :#0B0F19; color: white;}}
        h1{{ color: #00F0FF; }}
        .stat {{ background: #1a1f2e; padding: 20px; margin: 10px 0; border-radius: 10px; font-size: 1.5em; }}
         a {{ color: #FF007F; }}
    </style></head><body>
     """
    html += "<h1>📊 Statistiques</h1>"
    html += f"<div class='stat'>Total : {total}</div>"
    html += f"<div class='stat'>✅ Faites : {faites}</div>"
    html += f"<div class='stat'>⬜ Restantes : {restantes}</div>"
    html += f"<div class='stat'>🎯 Taux : {taux}%</div>"
    html += "<br><a href='/'>← Retour</a>"
    html += "</body></html>"
    return html
    
@app.route("/analyse")
def analyse():
    try:
        with open(FICHIER,"r")as f :
            taches = json.load(f)
    except :
        taches = []

    dates_uniques = set([t["date"] for t in taches])
    resultats = {}
    for date in dates_uniques:
        taches_du_jour = [t for t in taches if t["date"] == date]
        total = len(taches_du_jour)
        faites = len([t for t in taches_du_jour if t["faite"]])
        resultats[date] = round((faites/total)*100,2) if total > 0 else 0
    
    meilleur_jour = max(resultats,key= resultats.get) if resultats else "Pas encore de données "

    html="""<html><head><style>
        body {font-family : Arial ; max-width: 600px ; margin: 50px auto; background: #0B0F19; color: white;}
        h1{ color: #00F0FF; }
        .jour { background: #1a1f2e; padding: 15px; margin: 8px 0; border-radius: 8px;}
        .meilleur { border : 2px solid #FF007F; }
        a { color: #FF007F; }
    </style></head><body>"""
    html += "<h1> Analyse de productivité </h1>"

    for date, taux in sorted(resultats.items()):
        classe  = "jour meilleur" if date == meilleur_jour else "jour"
        html += f"<div class ='{classe}'>{date} → {taux}%</div>"

    html += f"<br><div class='jour meilleur'>🏆 Meilleur jour : {meilleur_jour}</div>"
    html += "<br><a href='/'>← Retour</a>"
    html += "</body></html>"
    return html

    
    








@app.route("/brief")
def brief():
    try:
        with open(FICHIER,"r") as f:
            taches= json.load(f)
    except: 
        taches = []
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=150,
        messages=[
    {"role": "user", "content": f"tâches : {', '.join([t['titre'] + (' ✅' if t['faite'] else ' ⬜') for t in taches])}. Brief motivant en 2 lignes max."}
        ]
    )
    brief_text = message.content[0].text


    html = """<html><head><style>
        body { font-family: Arial; max-width:600px; margin: 50px auto; background :#0B0F19; color: white;}
        h1 { color: #00F0FF; }
        .brief { background: #1a1f2e; padding: 20px; margin: 10px 0; border-radius: 10px; font-size: 1.2em; }
         a { color: #FF007F; }
    </style></head><body>"""
    html += "<h1>🤖 Brief du jour</h1>"
    html += f"<div class='brief'>{brief_text}</div>"
    html += "<br><a href='/'>← Retour</a>"
    html += "</body></html>"
    return html






if __name__ == "__main__":
    app.run(debug=True)