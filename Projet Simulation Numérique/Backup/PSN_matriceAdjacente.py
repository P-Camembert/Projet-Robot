"""def lire_fichier_graphe(nom_fichier):
    arretes = []
    with open(nom_fichier, 'r') as fichier:
        nombre_sommets = int(fichier.readline().strip())  # Lire le nombre de sommets depuis la première ligne
        for ligne in fichier:
            sommet_depart, sommet_arrivee = map(int, ligne.split())  
            arretes.append((sommet_depart, sommet_arrivee))
    return arretes, nombre_sommets

def construire_matrice_adjacence(arretes, nombre_sommets):
    matrice_adjacence = [[0] * nombre_sommets for _ in range(nombre_sommets)]  # Initialisation de la matrice

    for sommet_depart, sommet_arrivee in arretes:  # Attribution de la valeur 1 pour les arretes existantes dans la matrice
        if sommet_depart <= nombre_sommets and sommet_arrivee <= nombre_sommets:
            matrice_adjacence[sommet_depart-1][sommet_arrivee-1] = 1
            matrice_adjacence[sommet_arrivee-1][sommet_depart-1] = 1
    return matrice_adjacence


def afficher_matrice_adjacence(matrice_adjacence):  # fonction d'affichage de la matrice
    for ligne in matrice_adjacence:
        print(' '.join(map(str, ligne)))"""


# Nouveautés de la V2 : ajout de la fonction matrice_adjacence_vers_graphe

def lire_fichier_graphe(nom_fichier):
    arretes = []
    with open(nom_fichier, 'r') as fichier:
        nombre_sommets = int(fichier.readline().strip())  # Lire le nombre de sommets depuis la première ligne
        for ligne in fichier:
            sommet_depart, sommet_arrivee = map(int, ligne.split())  
            arretes.append((sommet_depart, sommet_arrivee))
    return arretes, nombre_sommets

def construire_matrice_adjacence(arretes, nombre_sommets):
    matrice_adjacence = [[0] * nombre_sommets for _ in range(nombre_sommets)]  # Initialisation de la matrice

    for sommet_depart, sommet_arrivee in arretes:  # Attribution de la valeur 1 pour les arretes existantes dans la matrice
        if sommet_depart <= nombre_sommets and sommet_arrivee <= nombre_sommets:
            matrice_adjacence[sommet_depart-1][sommet_arrivee-1] = 1
            matrice_adjacence[sommet_arrivee-1][sommet_depart-1] = 1
    return matrice_adjacence


def afficher_matrice_adjacence(matrice_adjacence):  # fonction d'affichage de la matrice
    for ligne in matrice_adjacence:
        print(' '.join(map(str, ligne)))


def matrice_adjacence_vers_graphe(matrice_adjacence):
    graphe = {}
    for sommet, voisins in enumerate(matrice_adjacence):
        sommet += 1  # Ajuster l'indice pour commencer à 1
        graphe[sommet] = [voisin + 1 for voisin, valeur in enumerate(voisins) if valeur == 1]
    return graphe



# Partie test :

""" nom_fichier = "facteur6.txt"
arretes, nombre_sommets = lire_fichier_graphe(nom_fichier)
print(nombre_sommets, arretes )
matrice_adjacence = construire_matrice_adjacence(arretes, nombre_sommets)
afficher_matrice_adjacence(matrice_adjacence) """



# Partie test
""" nom_fichier = input("Entrez le nom du fichier contenant les arêtes du graphe : ")
arretes, nombre_sommets = lire_fichier_graphe(nom_fichier)
print(nombre_sommets, arretes )
matrice_adjacence = construire_matrice_adjacence(arretes, nombre_sommets)

print(matrice_adjacence)
afficher_matrice_adjacence(matrice_adjacence) """