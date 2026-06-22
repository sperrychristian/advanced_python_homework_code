'''
Easy: (5 points)

Write a Python function that takes a NetworkX graph as input and returns the number of nodes in the graph.
'''

# importing networkx library
import networkx as nx

# building out a graph of 100 nodes based on the libraries documentation provided in the week 9/10 module
g = nx.complete_graph(100)

# based on networkx documentation, the number_of_nodes() function will return the number of nodes a networkx graph has
def nodeCount(g):
    count = nx.number_of_nodes(g)

    return count

# testing to confirm this works as intended
print(nodeCount(g))