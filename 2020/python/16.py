from builtins import pow
from collections import *
from copy import deepcopy
from functools import *
from itertools import *
from math import *
from more_itertools import *
from parse import *
import networkx as nx
import operator
import re

def ints(line):
    return [int(r[0]) for r in findall("{:d}", line)]

def main(inp):
    inp = inp.strip()

    Requirement = namedtuple('Requirement', ['values', 'name'])

    fields = []
    for requirement in inp.split("your ticket:")[0].strip().split("\n"):
        ok = set()
        for l, r in ichunked(ints(requirement.replace("-", " ")), 2):
            ok |= set(range(l, r + 1))
        fields.append(Requirement(ok, requirement.split(":")[0]))
    all_values = set.union(*(x.values for x in fields))

    my_ticket, tickets = inp.split("your ticket:")[1].split("nearby tickets:")
    my_ticket = ints(my_ticket)

    print(sum(filter(lambda x: x not in all_values, ints(tickets))))

    tickets = tickets.strip().split("\n")
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
