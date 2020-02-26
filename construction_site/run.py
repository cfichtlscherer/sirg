import networkx as nx

from sirg import generate as gg

G = gg.random_connected_graph(20, 0.2)

p = nx.average_shortest_path_length(G)
print(p)

"""
for i in range(20):
    for j in range(20):
        print(i, j, p[i][j])
"""
