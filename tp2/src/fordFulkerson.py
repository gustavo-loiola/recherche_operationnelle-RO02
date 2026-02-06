import numpy as np
import graph
import sys

def main():

    # Le poids des arcs de ce graphe correspondent aux capacités
    g = example()

    # Le poids des arcs de ce graphe correspondent au flot
    flow, max_flow = fordFulkerson(g, "s", "t")

    print(flow)
    print(max_flow)
    
# Fonction créant un graphe sur lequel sera appliqué l'algorithme de Ford-Fulkerson
def example():
        
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)
    
    return g

# Fonction appliquant l'algorithme de Ford-Fulkerson à un graphe
# Les noms des sommets sources est puits sont fournis en entrée
def fordFulkerson(g, sName, tName):

    """
    Marquage des sommets du graphe:
     - mark[i] est égal à +j si le sommet d'indice i peut être atteint en augmentant le flot sur l'arc ji
     - mark[i] est égal à  -j si le sommet d'indice i peut être atteint en diminuant le flot de l'arc ji
     - mark[i] est égal à sys.float_info.max si le sommet n'est pas marqué
    """
    mark = [0] * g.n
    
    # Récupérer l'indice de la source et du puits
    s = g.indexOf(sName)
    t = g.indexOf(tName)
    
    # Créer un nouveau graphe contenant les même sommets que g
    flow = graph.Graph(g.nodes)

    # Récupérer tous les arcs du graphe 
    arcs = g.getArcs()

    # Inicialiser le flot de tous les arcs à 0 dans le graphe flow
    for arc in arcs:
        flow.adjacency[arc.id1][arc.id2] = 0

    max_flow = 0

    while True:
        # Reinitialiser le marquage des sommets
        mark = [sys.float_info.max] * g.n

        # Queue pour le parcours en largeur du graphe (BFS)
        queue = [s]
        mark[s] = (s, 0) # Marquer la source avec un flot de 0
                         # Utilizar tupla resolve o problema de sinal para 0
        path_found = False

        # Parcours en largeur du graphe pour trouver un chemin augmentant
        while queue:
            u = queue.pop(0)

            if u == t: # Si on atteint le puits, on a trouvé un chemin augmentant
                path_found = True
                break

            # On vérifie les voisins de u
            for v in range(g.n):
                # Vérifier les arcs dans le sens normal (u -> v)
                if g.adjacency[u][v] != 0: # S'il y a un arc de u à v
                    capacity = g.adjacency[u][v]
                    flow_uv = flow.adjacency[u][v]
                    residual_capacity = capacity - flow_uv

                    if residual_capacity > 0 and mark[v] == sys.float_info.max:
                        mark[v] = (u, 1) # Marquer v avec u et indiquer que c'est un arc dans le sens normal
                        queue.append(v)

                # Vérifier les arcs dans le sens inverse (v -> u)
                if g.adjacency[v][u] != 0: # S'il y a un arc de v à u
                    flow_vu = flow.adjacency[v][u]
                    if flow_vu > 0 and mark[v] == sys.float_info.max:
                        mark[v] = (u, -1) # Marquer v avec u et indiquer que c'est un arc dans le sens inverse
                        queue.append(v)
        
        # Si on n'a pas trouvé de chemin augmentant, on peut arrêter l'algorithme
        if not path_found:
            break

        # Calculer le flot d'augmentation minimum le long du chemin trouvé
        delta = sys.float_info.max
        curr = t
        while curr != s:
            prev, direction = mark[curr]
            if direction == 1: # Arc dans le sens normal
                capacity = g.adjacency[prev][curr]
                flow_uv = flow.adjacency[prev][curr]
                residual_capacity = capacity - flow_uv
                delta = min(delta, residual_capacity)
            else: # Arc dans le sens inverse
                flow_vu = flow.adjacency[curr][prev]
                delta = min(delta, flow_vu)
            curr = prev

        # Mettre à jour le flot le long du chemin trouvé
        curr = t
        while curr != s:
            prev, direction = mark[curr]
            if direction == 1: # Arc dans le sens normal
                flow.adjacency[prev][curr] += delta
            else: # Arc dans le sens inverse
                flow.adjacency[curr][prev] -= delta
            curr = prev

        max_flow += delta

    return flow, max_flow
   
if __name__ == '__main__':
    main()
