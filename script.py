from PIL import Image
import os

def reduire_poids_image(repertoire_source, repertoire_destination, qualite=85, convertir_webp=False):
    """
    Réduit le poids des images dans le répertoire source et les enregistre dans le répertoire destination.
    Offre également une option pour convertir les images au format WebP.
    
    :param repertoire_source: Chemin du répertoire contenant les images à compresser
    :param repertoire_destination: Chemin du répertoire où les images compressées seront enregistrées
    :param qualite: Qualité de l'image compressée (1-100), 85 par défaut
    :param convertir_webp: Si True, les images seront converties en format WebP
    """
    
    # Vérifie si le répertoire de destination existe, sinon le crée
    if not os.path.exists(repertoire_destination):
        os.makedirs(repertoire_destination)

    # Extensions prises en charge
    formats_acceptes = ('png', 'jpg', 'jpeg', 'bmp', 'tiff', 'gif')

    # Parcourt toutes les images dans le répertoire source
    for nom_fichier in os.listdir(repertoire_source):
        chemin_complet = os.path.join(repertoire_source, nom_fichier)

        # Vérifie si le fichier est une image
        if nom_fichier.lower().endswith(formats_acceptes):
            try:
                with Image.open(chemin_complet) as img:
                    # Conversion en WebP si demandé
                    if convertir_webp:
                        nouveau_nom = os.path.splitext(nom_fichier)[0] + ".webp"
                        img.save(os.path.join(repertoire_destination, nouveau_nom), format="WEBP", quality=qualite, optimize=True)
                        print(f"Image '{nom_fichier}' convertie et compressée en WebP avec succès.")
                    else:
                        # Compression sans conversion
                        img.save(os.path.join(repertoire_destination, nom_fichier), quality=qualite, optimize=True)
                        print(f"Image '{nom_fichier}' compressée avec succès.")
            except Exception as e:
                print(f"Erreur lors du traitement de '{nom_fichier}': {e}")

# Utilisation du script avec les chemins spécifiés et options
repertoire_source = r''  # Chemin du répertoire source
repertoire_destination = r''  # Chemin du répertoire de destination
qualite = 85  # Qualité de compression
convertir_webp = True  # Passer à True pour convertir les images en WebP

reduire_poids_image(repertoire_source, repertoire_destination, qualite=qualite, convertir_webp=convertir_webp)
