try:
    from src import graph
except ImportError:
    import graph

import sys


def main():

    cities = [
        "Paris", "Hambourg", "Londres", "Amsterdam",
        "Edimbourg", "Berlin", "Stockholm", "Rana", "Oslo"
    ]

    g = graph.Graph(cities)

    g.addArc("Paris", "Hambourg", 7)
    g.addArc("Paris", "Londres", 4)
    g.addArc("Paris", "Amsterdam", 3)
    g.addArc("Hambourg", "Stockholm", 1)
    g.addArc("Hambourg", "Berlin", 1)
    g.addArc("Londres", "Edimbourg", 2)
    g.addArc("Amsterdam", "Hambourg", 2)
    g.addArc("Amsterdam", "Oslo", 8)
    g.addArc("Stockholm", "Oslo", 2)
    g.addArc("Stockholm", "Rana", 5)
    g.addArc("Berlin", "Amsterdam", 2)
    g.addArc("Berlin", "Stockholm", 1)
    g.addArc("Berlin", "Oslo", 3)
    g.addArc("Edimbourg", "Oslo", 7)
    g.addArc("Edimbourg", "Amsterdam", 3)
    g.addArc("Edimbourg", "Rana", 6)
    g.addArc("Oslo", "Rana", 2)

    # Applique l'algorithme de Dijkstra pour obtenir une arborescence
    tree, distances = dijkstra(g, "Paris")

    print("Arbre des plus courts chemins :")
    print(tree)

    print("\nDistances depuis Paris :")
    for i, d in enumerate(distances):
        print(f"{g.nodes[i]} : {d}")


def dijkstra(g, origin):

    # 1. Initialisation

    # Récupération de l'indice du sommet d'origine
    r = g.indexOf(origin)

    # Ensemble des sommets déjà considérés comme pivot
    visited = set()
    
    # Les distances entre r et les autres sommets sont initialement infinies
    pi = [float("inf")] * g.n
    pi[r] = 0

    # Les prédécesseurs des sommets sont initialement inconnus
    pred = [-1] * g.n

    # 2. Boucle principale
    # L'algorithme continue tant que tous les sommets n'ont pas été visités
    while len(visited) < g.n:

        # Sélection du pivot :
        # sommet u non visité avec pi[u] minimal
        pivot = -1
        min_pi = float("inf")

        for i in range(g.n):
            if i not in visited and pi[i] < min_pi:
                min_pi = pi[i]
                pivot = i

        # Si aucun pivot n'est trouvé,
        # les sommets restants sont inaccessibles
        if pivot == -1:
            break

        # Ajouter le pivot à l'ensemble des sommets visités
        visited.add(pivot)

        # 3. Relâchement des arcs
        # On regarde tous les voisins j du pivot
        for j in range(g.n):

            poids = g.adjacency[pivot][j]

            # S'il existe un arc entre pivot et j
            # et que j n'a pas encore été visité
            if poids != 0 and j not in visited:

                # Nouvelle distance potentielle
                nouvelle_distance = pi[pivot] + poids

                # Si passer par le pivot est plus court
                if nouvelle_distance < pi[j]:
                    pi[j] = nouvelle_distance
                    pred[j] = pivot

    # 4. Construction de l'arborescence des plus courts chemins
    tree = graph.Graph(g.nodes)

    for i in range(g.n):
        if pred[i] != -1:
            poids = g.adjacency[pred[i]][i]
            tree.addArcByIndex(pred[i], i, poids)

    # Retourne l'arbre et les distances minimales
    return tree, pi


if __name__ == '__main__':
    main()
