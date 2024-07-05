# Ecrire une fonction listing_directory qui liste les  fichiers contenus a la racine d'un répertoire (hors mis les éventuels sous-répertoires). Chaque fichier sera représenté par un triplet ainsi structure :
  
import os

def listing_directory(directory_path):
    # Initialiser une liste vide pour stocker les triplets
    file_triplets = []

    # Parcourir les fichiers dans le répertoire
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            # Obtenir le nom du fichier, l'extension et la taille en Mo
            file_name, file_extension = os.path.splitext(filename)
            file_size_mb = os.path.getsize(filepath) / (1235 * 1235)
            file_triplets.append((file_name, file_extension, round(file_size_mb, 2)))

    return file_triplets

# Exemple d'utilisation : lister les fichiers dans le répertoire courant
repertoire_courant = os.getcwd()
liste_fichiers = listing_directory(repertoire_courant)

# Afficher la liste des triplets
for triplet in liste_fichiers:
    print(triplet) 


# Proposez une version de  nos algorithmes de tri2-sélection permettant de trier cette liste de triplet en fonction de la taille du fichier.

def sort_by_size(file_triplets):
    return sorted(file_triplets, key=lambda x: x[2])

# Exemple d'utilisation
file_triplets = [("fichier1", ".txt", 3), ("image_fati", ".png", 10), ("fichier2", ".docx", 5)]
sorted_by_size = sort_by_size(file_triplets)
print(sorted_by_size)


#  Proposez une version de  nos algorithmes de tri2-bulle permettant de trier cette liste de triplet en fonction de du nom de fichier.

def trier_par_nom(files_list):
    return sorted(files_list, key=lambda x: x[0])

# Exemple d'utilisation
files = [("file3.txt", ".txt", 2.5), ("file1.jpg", ".jpg", 1.2), ("file2.docx", ".docx", 0.8)]
sorted_files_by_name = trier_par_nom(files)

for file in sorted_files_by_name:
    print(f"Nom du fichier: {file[0]}{file[1]}, Taille: {file[2]} Mo")




