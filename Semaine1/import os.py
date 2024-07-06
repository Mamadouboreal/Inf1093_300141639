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

#2. Algorithme de tri-sélection permettant de trier par tri bulle cette liste de triplet en fonction de la taille du fichier.

def tri_selection(file_triplets):
    
    t = len(file_triplets)
    for i in range(t):
        min_index = i
        for j in range(i + 1, t):
            if file_triplets[j][2] < file_triplets[min_index][2]:
                min_index = j

        # Parmuter les éléments
        file_triplets[i], file_triplets[min_index] = file_triplets[min_index], file_triplets[i]

    return file_triplets

# Exemple d'utilisation
file_triplets = [("fichier1", ".txt", 3), ("image_fati", ".png", 10), ("doc", ".pdf", 5)]
file_triplets_tri = tri_selection(file_triplets)
print(file_triplets_tri)

#3. Algorithmes de tri-bulle permettant de trier par tri sélection cette liste de triplet en fonction de du nom de fichier.

def tri_bulle_selection(file_triplets):

    t = len(file_triplets)
    for i in range(t):
        for j in range(0, t-i-1):
            if file_triplets[j][0] > file_triplets[j+1][0]:
                # Permuter les éléments
                file_triplets[j], file_triplets[j+1] = file_triplets[j+1], file_triplets[j]
    return file_triplets

# Exemple d'utilisation
file_triplets = [("fichier1", ".txt", 3), ("image_fati", ".png", 10), ("document", ".docx", 5)]
file_triplets_tri = tri_bulle_selection(file_triplets)
print(file_triplets_tri)
