# Réduction du poids des images avec Python

Ce script Python permet de réduire le poids des images contenues dans un répertoire source en compressant leur qualité, tout en conservant leur résolution initiale. Les images compressées sont enregistrées dans un répertoire de destination. Cela peut être utile pour optimiser les images avant de les télécharger sur un site web ou pour économiser de l'espace de stockage.

## Fonctionnalités

- Compression d'images au format **JPEG** et **PNG**.
- Qualité de compression personnalisable (par défaut : 85%).
- Création automatique du répertoire de destination s'il n'existe pas.
- Gestion des erreurs en cas de fichiers non valides ou d'autres problèmes.

## Prérequis

- Python 3.x
- La bibliothèque [Pillow](https://pillow.readthedocs.io/) (`pip install pillow`)

## Utilisation

1. Clone ou télécharge ce dépôt.
2. Modifie les variables `repertoire_source` et `repertoire_destination` pour spécifier le chemin du répertoire contenant les images à compresser et le répertoire où enregistrer les images compressées.
3. Lance le script avec la commande suivante :

```bash
python script.py
