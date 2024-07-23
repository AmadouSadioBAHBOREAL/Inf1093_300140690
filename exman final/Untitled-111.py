
def quicksortbyage(student_list):
    def partition(arr, low, high):
        pivot = arr[high].age
        i = low - 1
        for j in range(low, high):
            if arr[j].age <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    quicksort(student_list, 0, len(student_list) - 1)

# Exemple d'utilisation :
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Viny", 34),
    Student("Ryan", 43),
    Student("Tity", 31),
    Student("Antony", 27),
    Student("Calvin", 39),
    Student("lilian", 27),
    Student("Merlin", 19),
    Student("Rachy", 25)
]


def recherche_dichotomique(records, nom_cible):
    
    gauche, droite = 0, len(records) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        nom, age = records[milieu]
        
        if nom == nom_cible:
            return age
        elif nom < nom_cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    return -1

# Exemple d'utilisation
records = [
    ("Viny", 34),
    ("Ryan", 43),
    ("Tity", 31),
    ("Antony", 27),
    ("Calvin", 39),
    ("Lilian", 27),
    ("Merlin", 19),
    ("Rachy", 25)
]

nom_cible = "Rachy"
age = recherche_dichotomique(records, nom_cible)

if age != -1:
    print(f"L'âge de {nom_cible} est de {age} ans.")
else:
    print(f"{nom_cible} n'a pas été trouvé dans les enregistrements.")

quicksortbyage(students)

for student in students:
    print(f"{student.name} ({student.age} ans)") 




# Liste d'exemple d'étudiants
students = [
    {"name": "Viny", "age": 34},
    {"name": "Ryan", "age": 43},
    {"name": "Tity", "age": 31},
    {"name": "Antony", "age": 27},
    {"name": "Calvin", "age": 39},
    {"name": "Lilian", "age": 27},
    {"name": "Merlin", "age": 19},
    {"name": "Rachy", "age": 25}
]

# Fonction pour afficher les noms en utilisant une boucle
def printnames():
    for student in students:
        print(student["name"])

# Appel de la fonction
print("Utilisation de printnames():")
printnames() 



# Fonction récursive pour afficher les noms
def printrecnames(index=0):
    if index < len(students):
        print(students[index]["name"])
        printrecnames(index + 1)

# Appel de la fonction récursive
print("\nUtilisation de printrecnames():")
printrecnames()