# produit.py — Programme principal · Radio Map
# Relie api.py (Internet), donnees.py (fichier JSON) et l'interface web
from flask import Flask, render_template, request, jsonify, Response
import api
import donnees

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/top")
def top():
    return jsonify(api.top_stations(24))


@app.route("/api/search")
def search():
    nom = request.args.get("q", "").strip()
    if not nom:
        return jsonify([])
    stations = api.chercher_stations(nom, 24)
    if stations:
        historique = donnees.charger()
        historique.append({"recherche": nom, "resultats": len(stations)})
        donnees.sauvegarder(historique[-20:])
    return jsonify(stations)


@app.route("/api/pays")
def pays():
    return jsonify(api.liste_pays())


@app.route("/api/pays/<nom>")
def par_pays(nom):
    return jsonify(api.stations_par_pays(nom, 24))


@app.route("/api/proxy")
def proxy():
    url = request.args.get("url", "")
    reponse = api.ouvrir_flux(url) if url else None
    if not reponse:
        return "Flux indisponible", 502
    type_audio = reponse.headers.get("content-type", "audio/mpeg")
    return Response(reponse.iter_content(chunk_size=4096), content_type=type_audio)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
