# graph data structure

# unlike a binary search tree, a graph can be connected to an infinate amount of nodes. There is no limit to the amount of connections. 
# vertices is another word for nodes
# a pysical example of a graph would be a bus route - each stop representing a node and the lines between the path it would take to get there. 
# In graphs, the successor and predecesor has much more to do with the way we traverse a graph. 
# In graphs, the 'degree' is the number of edges that each node or vertice has. 
# in-degree - the number of edges going in 
# out-degree - the number of edges going out

# directed vs un-directed
# in a directed graph, the flow may go from node a to node b, but not necessarily in reverse order. (think the edge being an arrow)
# an undirected is the oppposite, the flow can go back and forth.  (the direction doesn't matter)
# so a directed graph uses in-degree and out-degree because the rule that exists forcing a certain path through the nodes
# but an un directed graph uses 'degree' and 'neighbors' (since there is no concept of going in, then out)
# think of street traffic as undirected, you can travel either direction. But on a one way street, you can only travel one direction. The one way street would be directed.
# if the relationship of the nodes is directed, it's directed (a graph of people with edges pointing to those younger than them)

# loop
# in a graph, when one node comes back to itself, that is considered a loop!

# graphs are used to represent relationships in code. 
# 'x' likes 'y' (nodes are people and food)
# 'x' knows how to contact 'y' (nodes are people)
# 'x' is a friend of 'y' (note that this is not necessarily reciprocal)
# 'x' wants to work for 'y' (nodes are people)
# 'x' is a child of 'y' (nodes are people)
# there is a flight from 'x' to 'y' (nodes are cities)
# clubs 'x' and 'y' share common members (nodes are clubs)

# GRAPHS are used to CAPTURE BOTH THE DATA ITSELF AND IT'S RELATIONSHIP TO OTHER DATA

# GRAPHS IMPLIMENTATION (going from a graph mental model to building an application around a graph)

# 2 ways to represent graphs in code
# adjacency matrix
# adjacency list 

# adjacency matrix representation 
# they work really well for any graphs that store numeric information 
# think of a spreadsheet with rows and columns. Each row and column represents a node, but the row itself indicates the the relationship the node has with other nodes. So 011000 would indicate that this node points at node 1 and node 2, but not node 0, 3, 4, and 5
# adjacency matrix's are really easy to impliment, but no matter what it takes O(n^2) memory which is more taxing on the computer


# adjacency list
# alternatively, adjacency lists are more memory effective and in my opinion easier to understand. 
# L[2]: 0, 1, 4, 5 indicates that node 2 has a relationship to 0, 1,  4 and 5 (arrows pointing at 0, 1, 4, 5)

# directed vs. undirected will indicate which data structure should likely be used
# for undirected relationships, symmitery is expected in an adjacency matrix because if you can traverse from 1 to 2, you can traverse from 2 - 1

# GRAPH TRAVERSAL
# graph traversal and graph data structure go hand in hand - we need to consider the data structure first to identify what the most efficient way to retrieve data out of it 

# there are two standards for graph traversal

# breadth first search
# I'm at a current node, what are all the nodes I can go to next and analyze those nodes 
# I'm at node A, and can get to B, C and D. Breadth first search goes to nodes B, C and D in that order.
# keeps track of where you're at, where you've been, and keeps track of all available nodes next together

# depth first search
# depth first search says well I went from A --> B, instead of going back and checking C, check and see what B is connected to first and go deeper

# depth first searches vs breadth first
# breadth first is better, much more efficient, feels quite obvious

# both DFS and BFS
# in both DFS and BFS, we keep track of nodes that we visit so far in a way that is most efficient 
# when node x is visited, it is labeled as visited then added to the tree
# if the traversal got to node x from node y, x is considered the child of y and y is considered the parent of x

# DFS rules 
# 1 - select an unvisited node x, visit it, and treat it as the current node 
# 2 - find an unvisited neighbor of the current node, visit it, and make it the current node 
# 3 - if the current node has no unvisited neighbors, backtrack to the parent, and make the parent the new current node 
# 4 - repeat steps 3 and 4 until no more nodes can be visited
# 5 - if there are still unvisited nodes, repeat from step 1. Generates a forest.

# BFS rules 
# 1 - select an unvisited node x, visit it, have it be the root in a BFS tree being formed. Its level is called the current level
# 2 - try all one-step extensions of crrent paths before trying larger extensions
# 3 - repeat step 2 until no more nodes can be visited
# 4 - if there are still unvisited nodes, repeat from step 1

# all BFS can be turned into a tree! It's sometimes nice to have a visual of how to traverse the data structure. 

# there are multiple algorithims that can be used to traverse graphs, but Dijkstra's Algorithim is by far the fastest and most efficient! 

# edge weight - the distance between nodes. (the shortest distance to drive from Logan to St. George)
# the edge weight is the time it takes to traverse to the destination

# Dijkstra's Algorithm (will get us the shortest path much faster than any other algorithim!)
# add the edgewt from a node to its successor to the current distance 
# pull nodes from collection based on shortest distance - using a priority que
# Dijkstra's Algorithim will solve the shortest path from one starting point to every other node in the system. (we have to pick a starting point) (think shortest path from Logan to every other city in utah)
# the simple beauty of Dijkstra's Algorithim is that it evaluates the compute cost of moving from one node to another, and that will always stay the same 
# so if a node is connected to three other nodes, it will first visit the one that takes the least amount effort, then the second, then the third. Once we evaluate the first connecting nodes, it then moves to the next nodes outside of the nodes that node 0 is directly connected to. 

# there are many powerful libraries available for traversal algorithims!!! We won't need to memorize how to write them from scratch.

# GRAPH IMPLIMENTATION IN PYTHON
# networkx is the python libary used for implimenting graphs. It's well written and great! 



'''
this python pgraom takes the edges in a graph from a file, generates the graph,saves the graph visualization to a file,
and traverse the paths in a the graph and calculates path weights
'''

import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations

import os
import matplotlib
matplotlib.use('Agg') # puts matplotlib into server mode, no GUI

import matplotlib.pyplot as plt

import networkx as nx
from networkx.classes.function import path_weight

current_directory = os.path.dirname(__file__) # get the current directory of this file 
edges_file = current_directory + '/' + 'edges.txt' # asigning a variable to the filename
graph_visual_fill = current_directory + '/' + 'graph_visual.png'

file = open(edges_file)

graph = nx.DiGraph() # created a directed graph object (starts out as an empty graph then gets filled up with all nodes and edges)

######################################################
# step 1 - create a graph
# get all lines in txt file 

edges = []

for line in file.readlines():
    node1, node2, weight = line.split(',')
    weight = int(weight)
    edges.append((node1, node2, weight)) # add edge to a list of tupples

print(edges)

graph.add_weighted_edges_from(edges) # adds all edges to graph at once 

# print all nodes 
print(graph.nodes)

# saving graph as an image for review
pos = nx.circular_layout(graph)
nx.draw_networkx(graph, pos)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

plt.savefig(graph_visual_fill)

######################################################
# step 2 - traverse the graph
# for each node pair, find paths between them
# calculate the path weight 

for n1, n2 in permutations(graph.nodes, 2): # permutations returns all pairs
    print('All existing paths from ' + n1 + ' to ' + n2 +':')

    # all simple paths function below returns each path as a list
    # the graph can be accessed with nodes as keys, like a dictionary
    # graph['v0']['v1']['weight'] returns 2, the weight of the edge
    # iterating through the edges in a path, you can calculate the weight of that path 

    for path in nx.all_simple_paths(graph, source=n1, target=n2):
        print(path) # print each path
        path_weight = 0 

        # iterating through each edge in the path adding each edge weight to the total path weight 
        for i in range(len(path) -1):
            path_weight += graph[path[i]][path[i + 1]]['weight']
        print('Path weight:', path_weight)












