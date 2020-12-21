import re
import networkx as nx

def main(inp):
    allergens = {}
    for l in inp.splitlines():
        w, info = map(lambda x: re.findall('\w+', x), l.split("contains"))
        for u in info:
            if u not in allergens:
                allergens[u] = set(w)
            allergens[u] &= set(w)
    G = nx.Graph()
    for a, b in allergens.items():
        G.add_edges_from((x, a) for x in b)
    matching = nx.algorithms.bipartite.matching.maximum_matching(G)
    cover = nx.algorithms.bipartite.to_vertex_cover(G, matching)
    print(",".join(sorted(cover, key=matching.__getitem__)))

from aocd import data
main(data)
