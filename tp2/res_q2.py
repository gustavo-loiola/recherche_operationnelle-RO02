import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from graph import Graph
from fordFulkerson import fordFulkerson

def main():
    # Le poids des arcs de ce graphe correspondent aux capacités
    g1 = graph1_fig1()
    g2 = graph2_fig1()
    
    # Le poids des arcs de ce graphe correspondent au flot
    flow1, max_flow1 = fordFulkerson(g1, "s", "t")
    flow2, max_flow2 = fordFulkerson(g2, "s", "t")

    print("Graphe 1:")
    print(flow1)
    print(max_flow1)
    print("Graphe 2:")
    print(flow2)
    print(max_flow2)

def graph1_fig1():
        
    g = Graph(np.array(["s", "1", "2", "3", "4", "t"]))

    g.addArc("s", "1", 16)
    g.addArc("s", "2", 13)
    g.addArc("1", "2", 10)
    g.addArc("2", "1", 4)
    g.addArc("1", "3", 12)
    g.addArc("2", "4", 14)
    g.addArc("3", "2", 9)
    g.addArc("4", "3", 7)
    g.addArc("4", "t", 4)
    g.addArc("3", "t", 20)
    
    return g

def graph2_fig1():
    # Définition des sommets: s, A, B, C, D, E, F, t
    g = Graph(np.array(["s", "A", "B", "C", "D", "E", "F", "t"]))

    # Ajout des arcs avec leurs capacités
    # Départs de s
    g.addArc("s", "A", 10)
    g.addArc("s", "C", 12)
    g.addArc("s", "E", 15)
    
    # Depuis A
    g.addArc("A", "B", 9)
    g.addArc("A", "C", 4)
    g.addArc("A", "D", 15)
    
    # Depuis B
    g.addArc("B", "D", 15)
    g.addArc("B", "t", 10)
    
    # Depuis C
    g.addArc("C", "D", 8)
    g.addArc("C", "E", 4)
    
    # Depuis D
    g.addArc("D", "F", 15)
    g.addArc("D", "t", 10)
    
    # Depuis E
    g.addArc("E", "F", 16)
    
    # Depuis F
    g.addArc("F", "C", 6)
    g.addArc("F", "t", 10)

    return g


if __name__ == "__main__":
    main()