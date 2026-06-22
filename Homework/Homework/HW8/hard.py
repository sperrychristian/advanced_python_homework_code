'''
Hard: (10 points)

  2. Write a Python function that takes a NetworkX graph as input and returns the number of nodes in the graph that have a degree greater than 5
'''

# importing networkx library
import networkx as nx

# import random library so i can test graphs that randomly generate a node count between 20 - 100
import random as r

random_number = r.randint(20, 100)

# use the built in networkx function gnp_random_graph() to generate a graph with our previously determined random number
g = nx.gnp_random_graph(random_number, 0.3)  # random number of nodes, 30% chance of an edge between any pair

def nodeCountOver5(g):
    # using list comprehension to filter down to a list of results of nodes that have at least 6 degrees 
    count_over_5 = [node for node, degree in g.degree() if degree > 5]

    # simple as returning how many nodes are in the list
    return int(len(count_over_5))

# testing function
print(nodeCountOver5(g))


# AI Prompt: 'within the networkx library, how would I see which nodes have a degree of 5 or greater?'
# AI Prompt: 'i am testing a networkx function, how would i generate a graph where I can influence how likely the nodes are to be connected'