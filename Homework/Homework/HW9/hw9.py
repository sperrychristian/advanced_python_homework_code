'''
this python program pulls live exchange rates for the top 7 crypto currencies from the
coingecko api, builds a directed graph where each currency is a node and each exchange
rate is a weighted edge, then traverses every path between every currency pair looking
for dis-equilibrium (arbitrage opportunities)

the big idea - if I trade from one coin to another and back, multiplying all the exchange
rates along the way, the result should be exactly 1.0. if it's not exactly 1.0, the market
is in dis-equilibrium and there is an arbitrage opportunity. the further from 1.0, the better.
'''

import os
import requests

# AI PROMPT: 'Give me a huge refresher about networkx and how i can use it working with graph data structures'
import networkx as nx
from itertools import permutations

current_directory = os.path.dirname(__file__) # get the current directory of this file
coin_ids_file = current_directory + '/' + 'coin_ids.txt' # asigning a variable to the filename
vs_currencies_file = current_directory + '/' + 'vs_currencies.txt'

# reading the coin ids and ticker symbols out of their txt files (one per line)
coin_ids = open(coin_ids_file).read().split()
ticker_symbols = open(vs_currencies_file).read().split()

# the two files line up line by line - line 1 of coin_ids.txt is 'ethereum' and line 1 of vs_currencies.txt is 'eth'. I'm looping through them together builds the mapping from id to ticker so the graph only has one node per coin!
coin_id_to_ticker = {}

for i in range(len(coin_ids)):
    coin_id_to_ticker[coin_ids[i]] = ticker_symbols[i]

# the coin full name and the ticker are both required in the url to get the price quote so I'm joing both lists to the url
url = 'https://api.coingecko.com/api/v3/simple/price?ids=' + ','.join(coin_ids) + '&vs_currencies=' + ','.join(ticker_symbols)


######################################################
# getting the exchange rates
# calling the api every run so the prices are always the most recent!

exchange_rates = requests.get(url).json() # parsing json into a python dictionary


######################################################
# create the graph
# each currency pair gets entered as (node_from, node_to, directed_edge_weight)

graph = nx.DiGraph() # creating a directed graph object

edges = []
# AI PROMPT: 'I need a reminder about how to unpack multiple items using a for loop in dictionary format'
# the json is nested, the outer key is the coin id, the inner dictionary is every coin it quotes against and the exchange rate
for coin_id, price_quotes in exchange_rates.items():
    from_ticker = coin_id_to_ticker[coin_id]

    for to_ticker, exchange_rate in price_quotes.items():

        # skipping a coin quoted against itself bedcause their wieght will always be 1.0
        if from_ticker != to_ticker:
            edges.append((from_ticker, to_ticker, exchange_rate)) # add edge to a list of tupples

# AI PROMPT: 'What is the built in networkx function to add graph edges'
graph.add_weighted_edges_from(edges) # adds all edges to graph at once


######################################################
# function to calculate the weight of a path
# multiply the weights of all the edges in the path together

def calculatePathWeight(graph, path):

    path_weight = 1.0

    # I'm iterating through each edge in the path multiplying each edge weight into the total path weight
    for i in range(len(path) - 1):
        path_weight = path_weight * graph[path[i]][path[i + 1]]['weight']

    return path_weight


######################################################
# traverse the graph
# for all currency pairs, find all paths, calculate the path weight and then reverse path weight, multiplying them together, and tracking the smallest and greatest path weights factor

smallest_factor = None
greatest_factor = None
smallest_factor_paths = None
greatest_factor_paths = None

# AI PROMPT: 'I'm working on an assignment where I need to iterate through all possible paths of a graph data structure, how can i do this most simply using python functionality?'

# AI PROMPT: 'Give me more examples of how permutations is used with detailed notes about functionality that I can reference while building in my assignment'

for n1, n2 in permutations(graph.nodes, 2): # permutations returns all possible ordering of nodes

    print('\npaths from ' + n1 + ' to ' + n2 + ' ----------------------------------')

    # AI PROMPT: 'what built in networkx functions allow me to pull all paths out if I wanted to iterate through them in a for loop?'
    # all simple paths function below returns each path as a list
    for path in nx.all_simple_paths(graph, source=n1, target=n2):

        # the reverse path is just the forward path flipped around
        reverse_path = list(reversed(path))

        # we  can trade into cardano but not from it, so the reverse path might use an edge that doesn't exist, using try/except to catch the missing edge and moves on to the next path
        try:
            forward_path_weight = calculatePathWeight(graph, path)
            reverse_path_weight = calculatePathWeight(graph, reverse_path)
        except KeyError:
            continue

        # if the two paths are in equilibrium this factor will be exactly 1.0
        path_weights_factor = forward_path_weight * reverse_path_weight

        print(path, forward_path_weight)
        print(reverse_path, reverse_path_weight)
        print(path_weights_factor)

        # keeping track of the best and worst arbitrage opportunities found so far
        if smallest_factor is None or path_weights_factor < smallest_factor:
            smallest_factor = path_weights_factor
            smallest_factor_paths = (path, reverse_path)

        if greatest_factor is None or path_weights_factor > greatest_factor:
            greatest_factor = path_weights_factor
            greatest_factor_paths = (path, reverse_path)


######################################################
# printing the smallest and greatest path weights

print('\n')
print('Smallest Paths weight factor: ', smallest_factor)
print('Paths: ', smallest_factor_paths[0], smallest_factor_paths[1])
print('Greatest Paths weight factor: ', greatest_factor)
print('Paths: ', greatest_factor_paths[0], greatest_factor_paths[1])