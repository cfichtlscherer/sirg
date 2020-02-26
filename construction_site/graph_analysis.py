"""
Feb 16, 2020
Christopher Fichtlscherer (fichtlscherer@mailbox.org)
GNU General Public License
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from tqdm import tqdm

from sirg import generate as gg

def get_average_shortest_paths(number_runs, number_nodes, pro_creation):
    """ a functionalized version of a simple plot of the average shortest path"""

    results = []

    for p in pro_creation:
        asp_tot = 0
        for i in tqdm(range(number_runs)):
            G = gg.random_connected_graph(number_nodes, p)
            asp = nx.average_shortest_path_length(G)
            asp_tot += asp
        av_asp = asp_tot / number_runs
        results += [av_asp]

    return results
    
# next step is to fit this
# compare numerical results with https://arxiv.org/abs/cond-mat/0407098
# see also here
# https://math.stackexchange.com/questions/501216/what-is-the-equation-for-the-average-path-length-in-a-random-graph
# Question: what is the connection between average degree and probability for edge creation?
# average_degree = (number_edges / number_nodes) * 2
# number_edges = prob * (number_nodes - 1) * (number_nodes - 2) / 2
# => average_degree = prob * (number_nodes - 1) * (number_nodes - 2) / number_nodes


def av_shortest_path(number_nodes, prob):
    """ the av shortest path implemented forumlar from 
    https://arxiv.org/abs/cond-mat/0407098"""

    number_edges = prob * (number_nodes - 1) * (number_nodes - 2) / 2
    av_degree = (number_edges / number_nodes) * 2
    avsp = ((np.log(number_nodes) - np.euler_gamma) / np.log(av_degree)) + 0.5

    return avsp


pro_creation = np.arange(0.1, 1, 0.1)
number_runs = 100
number_nodes = 100

results = get_average_shortest_paths(number_runs, number_nodes, pro_creation)
compare_results = [av_shortest_path(number_nodes, prob) for prob in pro_creation]

plt.plot(pro_creation, results, 'o', color = 'b')
plt.plot(pro_creation, compare_results, 'o', color = 'r')

plt.show()

# looks good but not perfectly... -> maybe simply raise the number of runs

