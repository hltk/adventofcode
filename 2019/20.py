from itertools import product, chain
from operator import itemgetter
from collections import defaultdict

import networkx as nx

def neighbours(p):
    yield (p[0] - 1, p[1])
    yield (p[0] + 1, p[1])
    yield (p[0], p[1] - 1)
    yield (p[0], p[1] + 1)

from aocd import data as grid
grid = grid.replace(" ", "#").split("\n")
n, m = len(grid), len(grid[0])
g = defaultdict(lambda: '#', {(i, j): grid[i][j] for i, j in product(range(n), range(m))})

apos = defaultdict(list)
for p in filter(lambda p: g[p] == '.', product(range(n), range(m))):
    for x in filter(lambda k: g[k].isalpha(), neighbours(p)):
        for y in filter(lambda k: g[k].isalpha(), neighbours(x)):
            s = ''.join(map(g.get, sorted([x, y])))
            apos[s].append(p)

lvls = len(apos) * 2

def solve_1():
    graph = nx.Graph()
    for i, j in filter(lambda p: g[p] == '.', product(range(n), range(m))):
        for ni, nj in filter(lambda p: g[p] == '.', neighbours((i, j))):
            graph.add_edge((i, j), (ni, nj))

    for l in apos.values():
        if len(l) == 2:
            graph.add_edge(*l)

    a, b = apos['AA'][0], apos['ZZ'][0]
    print(nx.shortest_path_length(graph, source=a, target=b))

solve_1()

def solve_2():
    graph = nx.Graph()
    for i, j in filter(lambda p: g[p] == '.', product(range(n), range(m))):
        for ni, nj in filter(lambda p: g[p] == '.', neighbours((i, j))):
            graph.add_edges_from((((i, j, l), (ni, nj, l)) for l in range(lvls)))

    minmax = lambda x: (min(x), max(x))
    xr = minmax(list(map(itemgetter(0), chain(*apos.values()))))
    yr = minmax(list(map(itemgetter(1), chain(*apos.values()))))

    for l in apos.values():
        if len(l) == 2:
            on_edge = lambda p: p[0] in xr or p[1] in yr
            a, b = sorted(l, key=on_edge)
            graph.add_edges_from((((*a, l), (*b, l + 1)) for l in range(lvls)))

    a, b = (*apos['AA'][0], 0), (*apos['ZZ'][0], 0)
    print(nx.shortest_path_length(graph, source=a, target=b))

solve_2()
