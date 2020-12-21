def main(inp):
    inp = inp.strip()
    inp = inp.split('\n')
    allergens = {}
    for line in inp:
        line, info = line.replace(")", "").split(" (contains ")
        line = line.split()
        for u in info.split(", "):
            if u in allergens:
                allergens[u] &= set(line)
            else:
                allergens[u] = set(line)
    import networkx as nx
    G = nx.Graph()
    for a, b in allergens.items():
        G.add_edges_from((x, a) for x in b)
    matching = nx.algorithms.bipartite.matching.maximum_matching(G)
    cover = nx.algorithms.bipartite.to_vertex_cover(G, matching)
    print(",".join(sorted(cover, key=matching.__getitem__)))


from aocd import data
main(data)
