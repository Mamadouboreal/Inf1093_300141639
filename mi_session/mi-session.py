# Exercice 2
def build_list():
    liste_etudiants = [] 

    while True:
        nom = input("Entrez le nom de l'étudiant : ")
        prenom = input("Entrez le prénom de l'étudiant : ")

        # Ajout des données à la liste
        liste_etudiants.append((nom, prenom))

        # Demande à l'utilisateur s'il veut ajouter un nouvel étudiant
        continuer = input("Voulez-vous ajouter un nouvel étudiant ? (1 pour oui, 0 pour non) ")
        if continuer != '1':
            break 

    return liste_etudiants

# Exemple d'utilisation
if __name__ == "__main__":
    liste_etudiants = build_list()
    print("Liste des étudiants reunie :", liste_etudiants)


#Exercice 3 (N°1)

def permute(liste, i, j):
    
    if 0 <= i < len(liste) and 0 <= j < len(liste):
        liste[i], liste[j] = liste[j], liste[i]
        return liste
    else:
        print("Indices invalides. Assurez-vous que les indices sont dans la plage valide.")
        return liste

# Exemple d'utilisation
ma_liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27)]
i, j = 1, 3  # Indices des éléments à permuter
resultat = permute(ma_liste, i, j)
print(resultat)

#Exercice 3 (N°2)
def bubbleSort(liste):

    t = len(liste)
    for i in range(t):
        for j in range(0, t-i-1):
            if liste[j][0] > liste[j+1][0]:
                # Permuter les éléments
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# Exemple d'utilisation
liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27)]
ma_liste = bubbleSort(liste)
print(ma_liste)

#Exercice 3 (N°3)
def selectionSort(liste):
    
    t = len(liste)
    for i in range(t):
        min_index = i
        for j in range(i + 1, t):
            if liste[j][2] < liste[min_index][2]:
                min_index = j

        # Parmuter les éléments
        liste[i], liste[min_index] = liste[min_index], liste[i]

    return liste

# Exemple d'utilisation
liste = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27)]
ma_liste = selectionSort(liste)
print(ma_liste)