def estPont(graphe, sommet_depart, sommet_arrivee):
    graphe_temporaire = {sommet: voisins.copy() for sommet, voisins in graphe.items()}

    # Vérifie si les sommets spécifiés existent dans le graphe
    if sommet_depart not in graphe_temporaire or sommet_arrivee not in graphe_temporaire:
        return False  # Si l'un des sommets n'existe pas, l'arête n'est pas un pont

    # Supprime l'arête (sommet_depart, sommet_arrivee) du graphe temporaire
    if sommet_arrivee in graphe_temporaire[sommet_depart]:
        graphe_temporaire[sommet_depart].remove(sommet_arrivee)
        
    if sommet_depart in graphe_temporaire[sommet_arrivee]:
        graphe_temporaire[sommet_arrivee].remove(sommet_depart)

    # Vérifie la connectivité après la suppression de l'arête
    def dfs(graphe, sommet, visite):
        visite.add(sommet)
        for voisin in graphe[sommet]:
            if voisin not in visite:
                dfs(graphe, voisin, visite)

    visite = set()
    dfs(graphe_temporaire, sommet_depart, visite)

    # Vérifie si tous les sommets sont visités
    for sommet in graphe_temporaire:
        if sommet not in visite:
            return True  # Si un sommet n'est pas visité, l'arête est un pont

    return False  # Sinon, l'arête n'est pas un pont
