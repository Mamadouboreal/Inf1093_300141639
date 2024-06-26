
#Collection de numbers
numbers = []
nb = int(input("Combien de nombres : "))
for i in range(nb):
    nb = int(input(f"Nombre1{i+1}:"))
    numbers.append(nb)

#Affichache des numbers
print(numbers)

# Lire la valeur a rechercher.
search_nb = int(input("Quel nombre a chercher?"))

# Recherche sequentielle

position = -1
for i in range(len(numbers)):
    if(search_nb==numbers[i]):
        position=i
        break
if(position>-1):
    print(f"{search_nb} est a la position {position}")
else:
    print(f"{search_nb} n'existe pas dans le tableau")

# Recherche dichotomique lorsque le tableau est trie
""" 
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

"""


#Question 1: Completer le code necessaire pour afficher la position de la valeur maximale dans numbers

numbers = [17, 76, 22, 13, 15, 45]
valeur_max = max(numbers)
position_max = numbers.index(valeur_max)

print(f"La valeur maximale est {valeur_max} à la position {position_max}.")


#Question 2: Completer le code necessaire pour afficher la position de la valeur minimale dans numbers


numbers = [17, 76, 22, 13, 15, 45]
valeur_minimale = min(numbers)
position = numbers.index(valeur_minimale)

print(f"La valeur minimale est {valeur_minimale} et sa position dans la liste est {position}.")


#Question 3: Ecrire le code necessaire pour verifier si le tableau numbers est trie en ordre croissant

def ordre_croissant(tableau):
    for i in range(len(tableau) - 1):
        if tableau[i] > tableau[i + 1]:
            return False
    return True

numbers = [17, 76, 22, 13, 15, 45]
if ordre_croissant(numbers):
    print("Le tableau est trié en ordre croissant.")
else:
    print("Le tableau n'est pas trié en ordre croissant.")


#Question 4: Considerons que le tableau est trie en ordre decroissant. Implementer une methode de recherche dichotomique dans ce cas.

def recherche_dichotomique(tableau, element):
    gauche, droite = 0, len(tableau) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        valeur_milieu = tableau[milieu]

        if valeur_milieu == element:
            return milieu 
        elif valeur_milieu < element:
            droite = milieu - 1 
        else:
            gauche = milieu + 1 

    return None  

tableau_trie = [17, 76, 22, 13, 15, 45]
element_recherche = 22
position = recherche_dichotomique(tableau_trie, element_recherche)

if position is not None:
    print(f"L'élément {element_recherche} se trouve à l'indice {position}.")
else:
    print(f"L'élément {element_recherche} n'est pas présent dans le tableau.")

