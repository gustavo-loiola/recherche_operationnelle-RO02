flot = ensemble de flux circulant sur les arcs du graph [$\phi_{ij}$]

flot réalisable = flot tel que $\phi_{ij} \le c_{ij}$ (capacité) et $\forall_j \sum_{i} \phi_{ij} = \sum_{k} \phi_{jk}$ (conservation)

flot complet = flot tel que chaque chemin de s à t un arc est saturé

arc saturé: $\phi_{ij} = c_{ij}$

coupe: partition des sommets en 2 ensembles S et T tq $s \epsilon S$ et $ t\epsilon T$

capacité de la coupe = $\sum_{i \epsilon S, j \epsilon T} c_{ij}$

Théorème de Ford-Fulkerson: valeur flot max = capacité coupe min