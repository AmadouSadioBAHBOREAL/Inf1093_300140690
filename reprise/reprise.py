## Exercice 1
#### Question 1
listIdName = [(202401, "Anani"), (202402, "Simon"),(202403, "Pierre"),(202404, "Kylian"),(202405, "Alphonse"),(202406, "Joshua"),(202407, "Colince"),(202408, "Khristian"),(202409, "Zinedine"),(202410, "Didier") ]
listIdGrade = [(202401, 17), (202402, 59),(202403, 73),(202404, 90),(202405, ),(202406, 59),(202407, ),(202408, 74),(202409, 93),(202410, 93) ]
fulllist = [(202401, "Anani", 17), (202402, "Simon", 93),(202403, "Pierre", 59),(202404, "Kylian", ),(202405, "Alphonse", 77),(202406, "Joshua", ),(202407, "Colince", 90),(202408, "Khristian", 73),(202409, "Zinedine", 59),(202410, "Didier", 17) ]
fulllist =[]
print(listIdName)  
print(listIdGrade)
print(fulllist) 





## Exercice 2
#### Question 1
def searchNameById(name):
    milieu = (debut+fin)//2 :
    if (name == [milieu][0]):
        return [milieu][1]
    elif(name < [milieu][0]):
        fin = milieu-1
        return searchNameById(name, debut, fin)
    else:
        debut = milieu+1
        return searchNameById(name, debut, fin) 
listIdName[(202401, "Anani", 17), (202402, "Simon", 93),(202403, "Pierre", 59),(202404, "Kylian", ),(202405, "Alphonse", 77),(202406, "Joshua", ),(202407, "Colince", 90),(202408, "Khristian", 73),(202409, "Zinedine", 59),(202410, "Didier", 17) ]
searchNameById("Le matricule de Anani : ", searchNameById("Anani"))  
searchNameById("Le matricule de Peter : ", searchNameById("Peter")) 

print("Le matricule de Anani : ", searchNameById("Anani"))  ## Le matricule de Anani :  202401 
print("Le matricule de Peter : ", searchNameById("Peter"))  ## Le matricule de Peter :  0

#### Question 2
def searchGradeByIdSeq(id):
    n = len(id)
    for i in range(n = len(id)):
        range = 0    
    for i in range(0, n-i-1):
            if id[i][2] > id[i+1][2]:
                id [i] + [p+1] = id [i] + [i+2]
    if not 
       return = id 
listIdGrade = [(202401, 17), (202402, 59),(202403, 73),(202404, 90),(202405, ),(202406, 59),(202407, ),(202408, 74),(202409, 93),(202410, 93) ]

print("La note du matricule 202405 est de  : ", searchGradeByIdSeq(202405))  ## La note du matricule 202403 est de  :  0

#### Question 3
def buildListSeq(matricule):
 matricule = int(input("Quel nombre a chercher?"))
# Recherche dichotomique
found = False
begin=0
end=len(matricule)-1
while(not(found) and begin>end):
    mid = (begin+end)//2
    if( begin == matricule[mid]):
        found=True
       # print("nombre trouve a la position : ", mid)
    else:
        if(begin <= matricule[mid]):
            end = mid-1
        else:
            begin = mid+1

    if(not(found)):
listIdGrade = [(202401, 17), (202402, 59),(202403, 73),(202404, 90),(202405, ),(202406, 59),(202407, ),(202408, 74),(202409, 93),(202410, 93) ]
print("listIdGrande ")
    
    
    
buildListSeq()
#print(fullList)

## Exercice 3
## Question1  : implementons le tri de ton choix



    
#listIdGrade = tri(listIdGrade)
#print(listIdGrade)

####Question 2
def searchGradeByIdDicho(id):
 
    return 0

## Question 3
def buildListDicho()
    



# Recherche dichotomique
found = False
begin=0
end=len(numbers)-1
while(not(found) and begin>end):
    mid = (begin+end)//2
    if(search_nb == numbers[mid]):
        found=True
        print("nombre trouve a la position : ", mid)
    else:
        if(search_nb <= numbers[mid]):
            end = mid-1
        else:
            begin = mid+1

if(not(found)):
    print("Nombre inexistant ")

