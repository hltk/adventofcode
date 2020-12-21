from functools import *
from itertools import *
from more_itertools import *
import networkx as nx
import operator
import re

def ints(s):
    return [int(k) for k in re.findall("\d+", s)]

def main(inp):
    fields = []
    tickets = []
    for l in inp.split("\n"):
        if k := ints(l):
            if len(k) == 4:
                l0, r0, l1, r1 = k
                fields.append([l, set(range(l0, r0 + 1)) | set(range(l1, r1 + 1))])
            else:
                tickets.append(k)

    all_values = set.union(*(x[1] for x in fields))
    print(sum(filterfalse(all_values.__contains__, flatten(tickets))))

    tickets = [v for v in tickets if all(map(all_values.__contains__, v))]
    field_values = [set(v) for v in zip(*tickets)]

    G = nx.Graph()
    for i, x in enumerate(field_values):
        G.add_edges_from((i, j + len(fields)) for j, y in enumerate(fields) if x <= y[1])
    matching = nx.algorithms.bipartite.matching.maximum_matching(G)
    pairs = [(a, b - len(fields)) for a, b in matching.items() if a < b]

    def in_ans(i):
        return fields[i][0].startswith("departure")
    print(reduce(operator.mul, (tickets[0][a] for a, b in pairs if in_ans(b))))

from aocd import data
main(data)
