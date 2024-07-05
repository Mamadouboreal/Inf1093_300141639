#1. Ecriture d'une fonction listing_directory qui liste les  fichiers contenus a la racine d'un répertoire
import os

def listing_directory(directory_path):

    file_triplets = []
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):  # Vérifier si l'élément est un fichier
            file_name, file_extension = os.path.splitext(filename)
            file_size_Mo = os.path.getsize(filepath) / (1024 * 1024)  # Conversion en Mo
            file_triplets.append((file_name, file_extension, round(file_size_Mo, 2)))

    return file_triplets

repertoire_courant = os.getcwd()
liste_fichiers = listing_directory(repertoire_courant)

for triplet in liste_fichiers:
    print(triplet)

#2. Proposition d'une version de  nos algorithmes de tri2-sélection permettant de trier cette liste de triplet en fonction de la taille du fichier.
def sort_by_size(file_triplets):
    return sorted(file_triplets, key=lambda x: x[2])

# Exemple d'utilisation :
file_triplets = [("fichier1", ".txt", 3), ("image_fati", ".png", 10), ("fichier2", ".docx", 5)]
sorted_by_size = sort_by_size (file_triplets)
print(sorted_by_size)

#3. Proposition d'une version de  nos algorithmes de tri2-bulle permettant de trier cette liste de triplet en fonction de du nom de fichier.
def sorted_by_name(file_triplets):
    return sorted(file_triplets, key=lambda x: x[0])

# Exemple d'utilisation
file_triplets = [("fichier1", ".txt", 3), ("image_fati", ".png", 10), ("fichier2", ".docx", 5)]
sorted_file_triplets_by_name = sorted_by_name (file_triplets)

for file in sorted_file_triplets_by_name:
    print(f"Nom du fichier : {file[0]}{file[1]}, Taille: {file[2]} Mo")

