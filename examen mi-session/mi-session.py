def build_list():
    student_list = [] 
    
    while True:
        name = input("Entrez le nom de l'étudiant : ")
        age = int(input("Entrez l'âge de l'étudiant : "))
        student_list.append((name, age))
        add_another = int(input("ajoute un autre étudiant ? (1 pour Oui, 0 pour Non) : "))
        if add_another == 0:
            break  
    return student_list
etudiants = build_list()
print("Liste des étudiants :")
for etudiant in etudiants:
    print(f"{etudiant[0]} ({etudiant[1]} ans)") 


def switch(liste i j): 
    if 0 <= i < len(liste) and 0 <= j < len(liste):
        liste[i], liste[j] = liste[j], liste[i]
        return liste
    else:
        print("Indices invalides. Veuillez fournir des indices valides dans les limites de la liste.")
        return liste
ma_liste = [("Viy34"),("Ryan" 43), ("Tity" 31), ("Antony" 27), ("Calvin" 39), ("Lilian" 27)] 
resultat = switch(ma_liste, i, j)
print(f"Liste après l'échange des éléments aux indices {i} et {j} : {resultat}") 


def selectionSort(age):
    n = len(age)
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if age[j] < age[minValueIndex] :
                minValueIndex = j
        if minValueIndex != i :
            temp = age[i]
            age[i] = age[minValueIndex]
            age[minValueIndex] = temp
    return ma_liste 
triplets = [("viny", 34), ("Ryan", 34), ("Tity",31), ("Antony", 27) ("Calvin", 39) ("lilian", 27)] 

print(selectionSort(age)) 



def tri_a_bulles_Sort(triplets):
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
triplets = [("Viny" 34), ("Ryan", 43), ("Tity" 31), ("Antony" 27), ("Calvin" 39), ("lilian"27)]
triplets_tries = tri_a_bulles_Sort(triplets)
for triplet in triplets_tries:
    print(triplet) 