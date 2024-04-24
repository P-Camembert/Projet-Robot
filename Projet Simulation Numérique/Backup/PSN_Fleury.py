import PSN_estPont

def fleury(graphe, sommet_depart):
    sommet_depart_choisi = sommet_depart
    chaine_fleury = [sommet_depart_choisi]
    
    while len(graphe[sommet_depart_choisi]) > 0:
        y = graphe[sommet_depart_choisi][0]

        # Vérifie si l'arête (sommet_depart_choisi, y) est un pont
        if PSN_estPont.estPont(graphe, sommet_depart_choisi, y) and len(graphe[sommet_depart_choisi]) > 1:
            # Trouve un autre voisin non pont
            for voisin in graphe[sommet_depart_choisi]:
                if not PSN_estPont.estPont(graphe, sommet_depart_choisi, voisin):
                    y = voisin
                    break

        chaine_fleury.append(y)
        graphe[sommet_depart_choisi].remove(y)
        if y in graphe and sommet_depart_choisi in graphe[y]:  # Vérifie si l'arête est bidirectionnelle
            graphe[y].remove(sommet_depart_choisi)
        sommet_depart_choisi = y
    
    return chaine_fleury

"""graphe2= {
    1:[2, 3],
    2:[1, 3, 4, 5],
    3:[1, 2, 5, 6],
    4:[2, 5],
    5:[2, 3, 4, 6],
    6:[3, 5]
}"""

# Affiche les chemins de tous les sommets (en cours)
"""def afficher_tous_chemins(graphe):
    tous_chemins = {}
    for sommet in graphe:
        tous_chemins[sommet] = fleury(graphe, sommet)
    return tous_chemins

# Appele la fonction pour afficher tous les chemins
chemins = afficher_tous_chemins(graphe2)

# Affiche les chemins
for sommet, chemin in chemins.items():
    print("Chemin à partir de", sommet, ":", chemin)"""


"""
sommet_depart_choisi = int(input("Entrez le sommet de départ : "))
print("Chaîne de Fleury:", fleury(graphe2, sommet_depart_choisi))
"""