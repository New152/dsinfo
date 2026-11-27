# Radio Map

Application web et modulaire permettant de rechercher, localiser et écouter des stations de radio du monde entier en direct, avec sauvegarde des favoris en JSON.

## API utilisée
Radio Browser API (gratuite, sans clé) — https://api.radio-browser.info

## Architecture (3 modules)
- `api.py` : requêtes HTTP (`requests.get`) et gestion des erreurs réseau
- `donnees.py` : lecture et sauvegarde JSON dans `favoris.json` (`try/except FileNotFoundError`)
- `produit.py` : serveur Flask reliant les modules à l'interface web

## Installation
```bash
pip install -r requirements.txt
```

## Utilisation
```bash
python produit.py
```
Ouvrir ensuite `http://127.0.0.1:5000` dans le navigateur.
