'''
This python program pulls live exchange rates for 13 crypto currencies from the
coingecko api, builds a directed graph where each currency is a node and each exchange
rate is a weighted edge, then traverses every path between every currency pair looking
for dis-equilibrium (arbitrage opportunities).

If I trade from one coin to another and back, multiplying all the exchange
rates along the way, the result should be exactly 1.0. If it's not exactly 1.0, the market is in dis-equilibrium and there is an arbitrage opportunity. the further from 1.0, the better.
'''

import os
import requests

# AI PROMPT: 'Give me a huge refresher about networkx and how i can use it working with graph data structures'
import networkx as nx
from itertools import permutations

import csv

from datetime import datetime

# AI PROMPT: 'what's the built in python library for reading and writing json files'
import json

# AI PROMPT: 'what's the alpaca python sdk and how do i submit a paper trading market order with it, give me details and examples. This is specifically for an assignment where I am using the alpaca api to make paper trades'
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# AI PROMPT: 'Remind me how to get the current directory of a file in python'
current_directory = os.path.dirname(__file__) # get the current directory of this file
coin_ids_file = current_directory + '/' + 'coin_ids.txt' # assigning a variable to the filename
vs_currencies_file = current_directory + '/' + 'vs_currencies.txt'
data_folder = current_directory + '/' + 'data' # folder where the currency pair csv snapshots get saved
results_file_path = current_directory + '/' + 'results.json' # where the analysis results get saved

# reading the coin ids and ticker symbols out of their txt files (one per line)
coin_ids = open(coin_ids_file).read().split()
ticker_symbols = open(vs_currencies_file).read().split()

# the two files line up line by line: line 1 of coin_ids.txt is 'ethereum' and line 1 of vs_currencies.txt is 'eth'. I'm looping through them together builds the mapping from id to ticker so the graph only has one node per coin!
coin_id_to_ticker = {}

for i in range(len(coin_ids)):
    coin_id_to_ticker[coin_ids[i]] = ticker_symbols[i]

# the coin full name and the ticker are both required in the url to get the price quote so I'm joining both lists to the url
url = 'https://api.coingecko.com/api/v3/simple/price?ids=' + ','.join(coin_ids) + '&vs_currencies=' + ','.join(ticker_symbols)


######################################################
# getting the exchange rates
# calling the api every run so the prices are always the most recent!

exchange_rates = requests.get(url).json() # parsing json into a python dictionary


######################################################
# saving the currency pair data to a csv
# the final project requirements want this saved as currency_pair_YYYY.MM.DD:HH.MM.txt with columns currency_from, currency_to, exchange_rate, so this happens before anything else touches exchange_rates, this way I have a raw snapshot saved no matter what

def saveCurrencyPairData(exchange_rates):

    # making the data folder if it doesn't exist yet 
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # building the filename with the current date and time
    #USED AU TO FIGURE OUT BEST WAY TO CAPTURE DATETIME IN THIS CIRCUMSTANCE
    file_timestamp = datetime.now().strftime('%Y.%m.%d:%H.%M')
    file_name = 'currency_pair_' + file_timestamp + '.txt'
    file_path = data_folder + '/' + file_name

    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['currency_from', 'currency_to', 'exchange_rate']) # header row

        # same nested json unpacking as the graph building step
        for coin_id, price_quotes in exchange_rates.items():
            from_ticker = coin_id_to_ticker[coin_id]

            for to_ticker, exchange_rate in price_quotes.items():

                # skipping a coin quoted against itself because their wieght will always be 1.0
                if from_ticker != to_ticker:
                    csv_writer.writerow([from_ticker, to_ticker, exchange_rate])

    return file_path


saved_file_path = saveCurrencyPairData(exchange_rates)
print('currency pair data saved to:', saved_file_path)


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

        # skipping a coin quoted against itself because their wieght will always be 1.0
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

# AI PROMPT: 'why would nx.all_simple_paths take forever to run and how do i speed it up'

# now that the graph has 13 coins instead of 7, letting all_simple_paths run with no length limit takes forever, capping how many hops a path can take keep it runnable.

path_length_cutoff = 4

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
    for path in nx.all_simple_paths(graph, source=n1, target=n2, cutoff=path_length_cutoff):

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


######################################################
# saving the smallest and greatest path weights to results.json
# final project requirements want the analysis results stored instead of just printed

def saveResultsToJson(smallest_factor, smallest_factor_paths, greatest_factor, greatest_factor_paths):

    results = {
        'smallest_factor': smallest_factor,
        'smallest_factor_forward_path': smallest_factor_paths[0],
        'smallest_factor_reverse_path': smallest_factor_paths[1],
        'greatest_factor': greatest_factor,
        'greatest_factor_forward_path': greatest_factor_paths[0],
        'greatest_factor_reverse_path': greatest_factor_paths[1]
    }

    with open(results_file_path, 'w') as results_file:
        json.dump(results, results_file, indent=4) # indent so the file is actually readable when I open it

    return results_file_path


saved_results_path = saveResultsToJson(smallest_factor, smallest_factor_paths, greatest_factor, greatest_factor_paths)
print('\nresults saved to:', saved_results_path)


######################################################
# paper trading the winning cycle on alpaca

# when the greatest path weights factor is far enough above 1.0 to be worth trading, this submits paper orders around that whole cycle (the forward path, then the reverse path, which together bring you back to the currency you started with)

# not every coin in my graph is tradable on alpaca so this set is what alpaca actually supports, anything outside this set gets skipped when submitting trades
ALPACA_TRADABLE_TICKERS = {'btc', 'eth', 'ltc', 'xrp', 'ada', 'bch', 'doge', 'dot', 'link', 'avax', 'uni', 'aave'}

# alpaca only lets me trade coins against usd, not coin to coin directly, so every leg of the cycle gets routed through usd instead of trying to trade the two coins against each other

trade_amount_usd = 10 # how many dollars worth of each coin to trade per leg


def getTradingClient():

    # reading the api key and secret out of environment variables instead of hardcoding them in the script
    api_key = os.environ.get('ALPACA_API_KEY')
    secret_key = os.environ.get('ALPACA_SECRET_KEY')

    if api_key is None or secret_key is None:
        print('alpaca api key and secret are not set as environment variables, skipping paper trading')
        return None

    # paper=True for paper trading, NOT LIVE TRADING
    return TradingClient(api_key, secret_key, paper=True)


def submitArbitrageTrades(trading_client, path, reverse_path):

    # stitching the forward path and reverse path together into one full loop of coins,skipping the first coin of reverse_path since it's the same coin path already ends on
    full_cycle = path + reverse_path[1:]

    # AI PROMPT: 'Give me the rundown on the alpaca trading libraries you showed me earlier, I need to know what arguments to use in each and understand the functions'

    # walking the cycle coin by coin and only trading when the coin I should be holding. If a coin in the cycle isn't tradable on alpaca, the target for that spot is usd instead! So I sell out of whatever I was holding and wait in cash until the cycle reaches a coin alpaca supports again

    # AI PROMPT: 'I need to keep track of what coin I'm currently holding as I loop through a list, and sometimes I'm not holding anything (just cash), whats a clean way to represent that in python instead of using a string like usd'

    current_holding = None  # None means I'm holding usd right now, since that's what a fresh paper account starts with

    # USED AI TO NAVIGATE ALPACA LIBRARY FUNCTIONS
    for coin in full_cycle:
        target_holding = coin if coin in ALPACA_TRADABLE_TICKERS else None

        if target_holding == current_holding:
            continue

        if current_holding is not None:
            try:
                sell_order = MarketOrderRequest(
                    symbol=current_holding.upper() + '/USD',
                    notional=trade_amount_usd,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC
                )
                trading_client.submit_order(sell_order)
                print('submitted paper sell order:', current_holding.upper() + '/USD')
            except Exception as order_error:
                print('sell order failed for ' + current_holding + ':', order_error)

        if target_holding is not None:
            try:
                buy_order = MarketOrderRequest(
                    symbol=target_holding.upper() + '/USD',
                    notional=trade_amount_usd,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.GTC
                )
                trading_client.submit_order(buy_order)
                print('submitted paper buy order:', target_holding.upper() + '/USD')
            except Exception as order_error:
                print('buy order failed for ' + target_holding + ':', order_error)

        current_holding = target_holding

# AI PROMPT: 'im about to compare a variable to a number but it might be None, how do i check for that safely so my program doesnt crash'
if greatest_factor is not None and greatest_factor > 1.0:

    trading_client = getTradingClient()

    if trading_client is not None:
        submitArbitrageTrades(trading_client, greatest_factor_paths[0], greatest_factor_paths[1])
else:
    print('\ngreatest factor was not above 1.0, no cycle to trade this run')

# USED AI TO GUIDE ME THROUGH DEPLOYING TO CRONTAB IN THE TERMINAL RATHER THAN READING THROUGH THE UBUNTU THREAD