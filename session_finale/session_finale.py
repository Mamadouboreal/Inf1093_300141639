# Exercice 1: Tri-rapide
def partition(students, debut, fin):
    pivot = students[debut][1]
    gauche, droite = debut + 1, fin
    while True:
        while gauche <= droite and students[gauche][1] <= pivot:
            gauche += 1
        while students[droite][1] >= pivot and droite >= gauche:
            droite -= 1
        if droite < gauche:
            break
        students[gauche], students[droite] = students[droite], students[gauche]
    students[debut], students[droite] = students[droite], students[debut]
    return droite

def quickSortByAge(students, debut=0, fin=None):
    if fin is None:
        fin = len(students) - 1
    if debut < fin:
        pivot_index = partition(students, debut, fin)
        quickSortByAge(students, debut, pivot_index - 1)
        quickSortByAge(students, pivot_index + 1, fin)

# Exemple d'utilisation
my_students = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25)]
quickSortByAge(my_students)
print(my_students)

# Exercice 2: Recherche dichotomique 
def recherche_dichotomique(student, search_name):
    gauche = 0
    droite = len(student) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        nom_milieu, age_milieu = student[milieu]

        if nom_milieu == search_name:
            return age_milieu
        elif nom_milieu < search_name:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return None  # Le nom n'existe pas dans la liste

# Exemple d'utilisation
student = [("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25), ("Ryan", 43), ("Tity", 31), ("Viny", 34)]
search_name = "Calvin"
found_age = recherche_dichotomique(student, search_name)

if found_age is not None:
    print(f"L'âge de {search_name} est {found_age}.")
else:
    print(f"{search_name} n'existe pas dans la liste.")



# Exercice 3: La recursivité
def printNames(student):
    for name, _ in student:
        print(name)

# Exemple d'utilisation :
student = [("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25), ("Ryan", 43), ("Tity", 31), ("Viny", 34)]
printNames(student)    


def printRecNames(student, index=0):
    if index < len(student):
        name, _ = student[index]
        print(name)
        printRecNames(student, index + 1)

# Exemple d'utilisation
printRecNames(student)
