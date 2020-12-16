from collections import *
from functools import *
from itertools import *
from more_itertools import *
from parse import *
import networkx as nx
import operator

def ints(line):
    return [int(r[0]) for r in findall("{:d}", line)]

def main(inp):
    Requirement = namedtuple('Requirement', ['values', 'name'])

    requirements, my_ticket, tickets = inp.split("\n\n")
    requirements = requirements.split("\n")
    my_ticket = ints(my_ticket)

    fields = []
    for requirement in requirements:
        ok = set()
        for l, r in ichunked(ints(requirement.replace("-", " ")), 2):
            ok |= set(range(l, r + 1))
        fields.append(Requirement(ok, requirement.split(":")[0]))
    all_values = set.union(*(x.values for x in fields))

    print(sum(filterfalse(all_values.__contains__, ints(tickets))))

    tickets = tickets.split("\n")[1:]

    def good(v):
        return all(map(all_values.__contains__, v))
    tickets = filter(good, map(ints, tickets))

    possible = [set(v) for v in zip(*tickets, my_ticket)]

    G = nx.Graph()
    for i, x in enumerate(possible):
        for j, y in enumerate(fields):
            if x.issubset(y.values):
                G.add_edge(i, j + len(fields))
    match = nx.algorithms.bipartite.matching.maximum_matching(G)
    match = [(a, b - len(fields)) for a, b in match.items() if a < b]

    def in_ans(i):
        return fields[i].name.startswith("departure")
    r = reduce(operator.mul, (my_ticket[a] for a, b in match if in_ans(b)))
    print(r)

from aocd import data
main(data)
