"""
Feb 03, 2020
Christopher Fichtlscherer (fichtlscherer@mailbox.org)
GNU General Public License

Run sir model on a networkx graph.
""" 

import networkx as nx
import numpy as np

def sis_infection_step(adjacency, ill_vector, beta):
    """ Perform one step of infection on the graph G. 
        every node which is connected by an edge with a node which is healthy
        will be infected with a probability of beta"""
        
    ad_ill = adjacency[ill_vector == 1]
    
    ad_ill_prob = np.random.random(np.shape(ad_ill))
    new_ill_matrix = (ad_ill_prob < beta).astype(int) * ad_ill
    new_ill_people = np.sum(new_ill_matrix, axis = 0)

    # hier ist ein problem muss noch gecheckt werden
    
    next_ill = ((ill_vector + new_ill_people) >= 1).astype(int)
    
    return ill_vector, next_ill



def sis_recover_step(ill_vector, next_ill, gamma):
    """every node which was ill in the step before has the chance to become 
    ill by probability gamma. Nodes which were just infected can't become
    directly health, nodes which have been ill and became infected again can
    recover
    """

    recover_prob = np.random.random(ill_vector.shape) 

    recovered = ill_vector * (recover_prob < gamma).astype(int)

    status_next = next_ill - recovered

    return status_next


def sis_simulation(G, ill_node, beta, gamma, steps):
    """performs a sis simulation on the graph G, starting from node ill_node
    for steps time steps."""

    adjacency = nx.to_numpy_matrix(G)
    
    ill_vector = np.zeros(G.number_of_nodes())
    ill_vector[ill_node] = 1
    
    for i in range(steps):
        ill_vector, next_ill = sis_infection_step(adjacency, ill_vector, beta)
        ill_vector = sis_recover_step(ill_vector, next_ill, gamma)
        print(ill_vector)




"""
def simultation(start, steps, beta, gamma):

    nx.set_node_attributes(G, 1, 'illness')
    nx.set_node_attributes(G, 'blue', 'color')

    G.node[start]['illness'] = 2 #welche Node wird krank (illness 2) 15 = Hamburg

    ill_vector = np.zeros(steps)

    for i in range(steps):
            #print(i)
            #attriplot()
            #simplebericht()
            #bericht = nx.get_node_attributes(G,'illness').values()
            #bericht = nx.get_node_attributes(G,'color').values()
            #print(bericht)
            data_array_maker(ill_vector, i) # same as simplebericht but stores in the array ill_vector
            for j in range(nodes):
                # gesunden
                if (G.node[j]['illness'] == 2) and (np.random.random() < gamma):
                    G.node[j]['illness'] = 1
                    for m in G.neighbors(j):
                        weightchance = np.random.random() * G.edges[m,j]['weight']
                        if weightchance < beta:G.node[m]['illness'] = 3

                for jj in range(nodes):
                    if G.node[jj]['illness']==3:G.node[jj]['illness'] = 2

    return ill_vector
"""
