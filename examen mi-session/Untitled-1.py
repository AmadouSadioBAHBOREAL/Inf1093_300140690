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

def selectionSort(liste):
    
    t = len(liste)
    for i in range(t):
        min_index = i
        for j in range(i + 1, t):
            if liste[j][0] < liste[min_index][0]:
                min_index = j

        # Parmuter les éléments
        liste[i], liste[min_index] = liste[min_index], liste[i]

    return liste

# Exemple d'utilisation
liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27)]
ma_liste = selectionSort(liste)
print(ma_liste) 