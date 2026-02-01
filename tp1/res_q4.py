# Utiliser cette méthode pour résoudre le problème d’arbre couvrant de poids minimal sur les
# deux graphes représentés en Figure 1

import numpy as np 
from src import graph
from src.dijkstra import dijkstra

def solve_plus_courts_chemins(nodes, edges, origin):
    # Créer un graphe avec les noeuds donnés
    g = graph.Graph(np.array(nodes))

    # Ajouter les arêtes au graphe
    for edge in edges:
        g.addEdge(edge[0], edge[1], edge[2])

    # Obtenir un arbre couvrant de poids minimal du graphe
    tree, distances = dijkstra(g, origin)

    print("Arbre des plus courts chemins :")
    print(tree)

    print(f"\nDistances depuis {origin} :")
    for i, d in enumerate(distances):
        print(f"{g.nodes[i]} : {d}")


# Figure 1 graph 1
nodes1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
edges1 = [
    ("a", "b",  9.0), ("a", "h",  9.0),
    ("a", "f",  6.0), ("b", "d", 8.0),
    ("b", "c",  5.0), ("b", "e",  5.0),
    ("e", "f",  1.0), ("e", "g",  3.0),
    ("c", "g",  5.0), ("c", "d", 2.0),
    ("d", "g",  8.0), ("d", "h",  7.0),
    ("g", "h",  5.0)
]
print("Résolution du graphe 1 min:")
solve_plus_courts_chemins(nodes1, edges1, "a")


# Figure 1 graph 2
nodes2 = ["a", "b", "c", "d", "e", "f"]
edges2 = [
    ("a", "b",  4.0), ("a", "c",  3.0),
    ("b", "c",  5.0), ("b", "f",  2.0),
    ("c", "f",  5.0), ("c", "d",  2.0),
    ("d", "f",  3.0), ("d", "e",  4.0),
    ("e", "f",  3.0)
]
print("\nRésolution du graphe 2 min:")
solve_plus_courts_chemins(nodes2, edges2, "a")
