import numpy as np
try:
    from src import graph 
except ImportError:
    import graph         
import sys

def main():
    
    # Créer un graphe contenant les sommets a, b, c, d, e, f, g 
    g = graph.Graph(np.array(["a", "b", "c", "d", "e", "f", "g"]))

    # Ajouter les arêtes
    g.addEdge("a", "b",  1.0)
    g.addEdge("a", "c",  3.0)
    g.addEdge("b", "c",  2.0)
    g.addEdge("b", "d",  5.0)
    g.addEdge("b", "e",  7.0)
    g.addEdge("b", "f",  9.0)
    g.addEdge("c", "d",  4.0)
    g.addEdge("d", "e",  6.0)
    g.addEdge("d", "g", 12.0)
    g.addEdge("e", "f",  8.0)
    g.addEdge("e", "g", 11.0)
    g.addEdge("f", "g", 10.0)
    
    # Obtenir un arbre couvrant de poids minimal du graphe
    print("Arbre couvrant de poids minimal :")
    tree_min = kruskal(g, computeMin=True)
    print(tree_min if tree_min else "Pas d'arbre couvrant")
    
    # Obtenir un arbre couvrant de poids maximal du graphe
    print("\nArbre couvrant de poids maximal :")
    tree_max = kruskal(g, computeMin=False)
    print(tree_max if tree_max else "Pas d'arbre couvrant")

# Applique l'algorithme de Kruskal pour trouver un arbre couvrant de poids minimal d'un graphe
# Retourne: Un arbre couvrant de poids minimal du graphe ou None s'il n'en existe pas
def kruskal(g, computeMin=True):
    # Créer un nouveau graphe contenant les mêmes sommets que g
    tree = graph.Graph(g.nodes)
    
    # Nombre d'arêtes dans l'arbre
    addedEdges = 0
    
    # Récupérer toutes les arêtes de g
    edges = g.getEdges()
    
    # Trier les arêtes par poids croissant ou décroissant selon computeMin
    edges.sort(reverse=not computeMin)

    # Parcourir les arêtes triées
    for edge in edges:
        if not tree.createACycle(edge):
            tree.addCopyOfEdge(edge)
            addedEdges += 1

        # Si l'arbre contient n-1 arêtes, il est complet
        if addedEdges == g.n - 1:
            break
    
    if addedEdges == g.n - 1:
        return tree
    else:
        return None

if __name__ == '__main__':
    main()
