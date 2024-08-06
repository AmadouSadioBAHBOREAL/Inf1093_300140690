def quickSortByAge(std):
    if (len(std)<=1):
        return std
    pivot = std.pop()
    petit =[]
    grand =[]
    for i in range (len(std)<=1):
        if (std[i][1] <= pivot[1]):
            petit.append(std[i])
        else:
            grand.append(std[i])

    return quickSortByAge(petit) + [pivot]  + quickSortByAge(grand) 
etudiants = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27),("Calvin", 39), ("Lilian", 27), ("Amadou", 33) ("Rachy", 25)]  
#print(quickSortByAge(etudiants)) 


def searchByName(name, fin, debut=0):
    milieu = (debut+fin)//2
    print(debut,fin)
    if(name == etudiants[milieu][0]):
        return etudiants[milieu][1]
    elif(name < etudiants[milieu][0]):
        fin = milieu-1
        return searchByName(name, debut, fin)
    else:
        debut = milieu + 1
        return searchByName(name, debut, fin)
#searchByName ("Rachy", 7, 0)



def printNames():
    for std in etudiants:
        print(std[0])

def printRacNames(debut,liste):
    if (len(liste)==1 or debut==len(liste)-1):
        print(liste[debut][0])
    elif(len(liste)>1):
        print(liste[debut][0])
        printRacNames(debut+1, liste)




#print(quickSortByAge(etudiants)) 
#searchByName ("Rachy", 7, 0)
printRacNames(0, etudiants)
