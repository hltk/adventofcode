from aocd import data
import re, networkx as nx
from math import prod

lines = [list(re.findall(r"\w+", l)) for l in data.split("\n")]
G = nx.from_dict_of_lists({a[0]: a[1:] for a in lines})
G.remove_edges_from(nx.minimum_edge_cut(G))

print(prod(map(len, nx.connected_components(G))))
