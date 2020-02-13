"""
Feb 11, 2020
Christopher Fichtlscherer (fichtlscherer@mailbox.org)
GNU General Public License

Testing if the functions which are made for generating random graphs and 
analyzing them working correctly
""" 

import pytest
import networkx as nx

import sirg.generate


def test_random_connected_graph_1():
    """
    we test if the number of nodes and edges is correct.
    """

    n = 50
    p = 1
    
    g = sirg.generate.random_connected_graph(n, p)
    
    number_nodes = len(g.nodes())
    number_edges = len(g.edges())

    assert (number_nodes == 50) and (number_edges == (50 * (50-1)) / 2)


def test_density():

    G = nx.Graph()
    G.add_nodes_from(range(10))
    G.add_edges_from([(1,2), (1,5), (9,3), (4,5)])

    density = sirg.generate.density(G)

    assert density == 0.4


def test_random_connected_graph_1():
    """
    test the error message
    """

    n = 10
    p = 0
    
    g = sirg.generate.random_connected_graph(n, p)
   
    assert g == False


