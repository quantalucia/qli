from indicator import *
import networkx as nx
import matplotlib.pyplot as plt

globalEconomy = []

#create any pods from base class
p1 = Indicator("GDP US")
p2 = Indicator("US Interest Rate")
p3 = Indicator("M2 CN")
pCryptoMarketCap = Indicator("total marketcap of crypto")

# append to global graph
globalEconomy.append(p1)
globalEconomy.append(p2)
globalEconomy.append(p3)
globalEconomy.append(pCryptoMarketCap)
# connect pods
p2.affectPod(p3,0.01)



graph = nx.DiGraph()
graph.add_edges_from([("root", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
print(graph.in_edges("e")) # => [('a', 'e'), ('d', 'e')]

G = nx.complete_graph(5)
nx.draw(G)