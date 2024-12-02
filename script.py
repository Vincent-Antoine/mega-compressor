from PIL import Image
import os

def reduire_poids_image(repertoire_source, repertoire_destination, qualite=85):
    """
    Réduit le poids des images dans le répertoire source et les enregistre dans le répertoire destination.
    
    :param repertoire_source: Chemin du répertoire contenant les images à compresser
    :param repertoire_destination: Chemin du répertoire où les images compressées seront enregistrées
    :param qualite: Qualité de l'image compressée (1-100), 85 par défaut
    """
    
    # Vérifie si le répertoire de destination existe, sinon le crée
    if not os.path.exists(repertoire_destination):
        os.makedirs(repertoire_destination)

    # Parcourt toutes les images dans le répertoire source
    for nom_fichier in os.listdir(repertoire_source):
        chemin_complet = os.path.join(repertoire_source, nom_fichier)

        # Vérifie si le fichier est une image (vous pouvez ajouter d'autres extensions si nécessaire)
        if nom_fichier.lower().endswith(('png', 'jpg', 'jpeg')):
            try:
                with Image.open(chemin_complet) as img:
                    # Redimensionne l'image (ici on garde la même taille, juste compresse)
                    img.save(os.path.join(repertoire_destination, nom_fichier), quality=qualite, optimize=True)
                    print(f"Image '{nom_fichier}' compressée avec succès.")
            except Exception as e:
                print(f"Erreur lors de la compression de '{nom_fichier}': {e}")

# Utilisation du script avec les chemins spécifiés
repertoire_source = r''  # Chemin du répertoire source
repertoire_destination = r''  # Chemin du répertoire de destination

reduire_poids_image(repertoire_source, repertoire_destination)
