# Réduction et conversion d'images avec Python

Ce script Python permet de réduire le poids des images contenues dans un répertoire source en compressant leur qualité, tout en conservant leur résolution initiale. Les images compressées sont enregistrées dans un répertoire de destination. Il offre également une option pour convertir les images au format **WebP**, idéal pour les performances web. 

## Fonctionnalités

- Compression d'images pour les formats **JPEG**, **PNG**, **BMP**, **TIFF**, et **GIF**.
- Conversion optionnelle des images au format **WebP**.
- Qualité de compression personnalisable (par défaut : 85%).
- Création automatique du répertoire de destination s'il n'existe pas.
- Gestion des erreurs pour les fichiers non valides ou les problèmes de traitement.

## Prérequis

- Python 3.x
- La bibliothèque [Pillow](https://pillow.readthedocs.io/) (`pip install pillow`)

## Utilisation

1. Clone ou télécharge ce dépôt.
2. Modifie les variables `repertoire_source` et `repertoire_destination` pour spécifier le chemin du répertoire contenant les images à compresser et celui où enregistrer les images compressées.
3. Active ou désactive l'option de conversion en WebP en modifiant la variable `convertir_webp`.
4. Lance le script avec la commande suivante :

```bash
python script.py
