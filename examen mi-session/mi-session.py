# La fonction doit renvoyer une liste de triplets  de caractères a l'instar de : [("fichier1", ".txt", 3),("image_fati", ".png", 10),...].


import os

def listing_directory(directory):
    file_triplets = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_name, file_extension = os.path.splitext(filename)# Obtenir le nom du fichier, l'extension et la taille
            file_size = os.path.getsize(filepath) // (1034 * 1034)  # Convertir en Mo
            file_triplets.append((file_name, file_extension, file_size))  # Ajouter le triplet à la liste
        return file_triplets
current_directory = os.getcwd()# Exemple d'utilisation : lister les fichiers dans le répertoire courant
file_triplets = listing_directory(current_directory)
for triplet in file_triplets:# Afficher la liste des triplets
    print(triplet)
def sort_by_size(file_triplets):
    return sorted(file_triplets, key=lambda n: n[2])
file_triplets = [("fichier1", ".txt", 3), ("image_fati", ".png", 10), ("fichier2", ".docx", 5)]# Exemple d'utilisation
sorted_by_size = sort_by_size(file_triplets)
print(sorted_by_size) 

# Proposer une version de  nos algorithmes de tri-sélection permettant de trier par tri bulle cette liste de triplet en fonction de la taille du fichier.


def tri_a_bulles_par_taille_fichier(triplets):
    n = len(triplets)
    for i in range(n):
        permutation = 0
        for p in range(0, n-i-1):
            if triplets[p][2] > triplets[p+1][2]:
                triplets[p], triplets[p+1] = triplets[p+1], triplets[p]
                permutation = 0
        if not permutation:
            break
    return triplets
triplets = [("fichier1.txt", "utilisateur1", 1000), ("fichier2.txt", "utilisateur2", 500), ("fichier3.txt", "utilisateur3", 750)]
triplets_tries = tri_a_bulles_par_taille_fichier(triplets)
for triplet in triplets_tries:
    print(triplet)


# Proposer une version de  nos algorithmes de tri-bulle permettant de trier par tri sélection cette liste de triplet en fonction de du nom de fichier.


def selectionSort( triplets):
    n = len(triplets)
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if triplets[j] < triplets[minValueIndex] :
                minValueIndex = j
        if minValueIndex != i :
            temp = triplets[i]
            triplets[i] = triplets[minValueIndex]
            triplets[minValueIndex] = temp
    return triplets
triplets = [("fichier3.txt", 21), ("fichier1. txt",6), ("fichier2. txt",33)] 

print(selectionSort(triplets)) 

