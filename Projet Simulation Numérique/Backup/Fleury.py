import PSN_matriceAdjacence
def fleury(graph, start_vertex=None):
    # Vérifier si le graphe est eulérien en vérifiant que chaque sommet a un degré pair
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:
            raise ValueError("Le graphe n'est pas eulérien")

    def is_bridge(u, v):
        # Temporairement retirer l'arête entre u et v
        graph[u].remove(v)
        graph[v].remove(u)

        # Vérifier si v est toujours accessible depuis u
        visited = {vertex: False for vertex in graph}
        dfs(u, visited)

        # Ajouter l'arête retirée pour restaurer le graphe
        graph[u].append(v)
        graph[v].append(u)

        # Si v est inaccessible depuis u, alors (u, v) est un pont
        return not visited[v]

    def dfs(u, visited):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v, visited)

    # Initialiser la chaîne C
    chain = [start_vertex]

    # Choisir le sommet de départ
    if start_vertex is None:
        # Si aucun sommet n'est spécifié, choisir arbitrairement un sommet
        start_vertex = next(iter(graph))

    # Parcourir le graphe
    current_vertex = start_vertex
    while any(graph.values()):
        # Trouver un successeur qui n'est pas un pont
        next_vertex = None
        for neighbor in graph[current_vertex]:
            if not is_bridge(current_vertex, neighbor):
                next_vertex = neighbor
                break
        
        # Si aucun successeur non-pont n'est trouvé, choisir arbitrairement un successeur
        if next_vertex is None:
            next_vertex = graph[current_vertex][0]

        # Ajouter le successeur à la fin de la chaîne C
        chain.append(next_vertex)

        # Supprimer l'arête (x, y) du graphe
        graph[current_vertex].remove(next_vertex)
        graph[next_vertex].remove(current_vertex)

        # Choisir le prochain sommet
        current_vertex = next_vertex
    
    return chain

nom_fichier = "facteur9.txt"
arretes, nombre_sommets = PSN_matriceAdjacence.lire_fichier_graphe(nom_fichier)
matrice_adjacence = PSN_matriceAdjacence.construire_matrice_adjacence(arretes, nombre_sommets)

graphe = PSN_matriceAdjacence.matrice_adjacence_vers_graphe(matrice_adjacence)

print(fleury(graphe,9))