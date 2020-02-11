import networkx as nx

from sirg import generate as gg
from sirg import sir as sir


G = gg.random_connected_graph(20, 1)
sir.sis_simulation(G, 1, 0.5, 0.2, 10)


