"""
Feb 03, 2020
Christopher Fichtlscherer (fichtlscherer@mailbox.org)
GNU General Public License

In this file we define functions to generate random graphs and to check
certain of their properties.
""" 

import networkx as nx
import numpy as np

def random_connected_graph(n, p):
    """generates a random connected graph with n nodes and every edges
    exists with probability"""

    for i in range(10**5):
        seed = int(np.random.random() * 10**9)
        G = nx.erdos_renyi_graph(n, p, seed=seed, directed=False)
        if nx.is_connected(G) == True:
            return G
    print("ERROR: Over 100 000 unsuccesfull iterations")
    return False

def density(G):
    """ returns the density of the graph"""
    nodes = G.number_of_nodes()
    edges = G.number_of_edges()

    density = edges / nodes

    return density

