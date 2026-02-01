# Utiliser cette méthode pour résoudre le problème d’arbre couvrant de poids minimal sur les
# deux graphes représentés en Figure 1

import numpy as np 
from src import graph
from src.kruskal import kruskal

def solve_mst(nodes, edges):
    # Créer un graphe avec les noeuds donnés
    g = graph.Graph(np.array(nodes))

    # Ajouter les arêtes au graphe
    for edge in edges:
        g.addEdge(edge[0], edge[1], edge[2])

    # Obtenir un arbre couvrant de poids minimal du graphe
    tree = kruskal(g)

    if tree:
        print("Arbre couvrant de poids minimal trouvé :")
        print(tree)
    else:
        print("Pas d'arbre couvrant")

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
solve_mst(nodes1, edges1)