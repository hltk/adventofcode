import re
from itertools import product
from collections import defaultdict

from aocd import data

lines = data.split("\n")

def solve_1():
    g = defaultdict(int)

    for l in lines:
        a, b, c, d = map(int, re.findall(r'\d+', l))
        act = next(x for x in ["toggle", "on", "off"] if x in l)
        for i, j in product(range(a, c + 1), range(b, d + 1)):
            if act == "on": g[i, j] = 1
            if act == "off": g[i, j] = 0
            if act == "toggle": g[i, j] = 1 - g[i, j]

    print(sum(x == 1for x in g.values()))

solve_1()

def solve_2():
    g = defaultdict(int)

    for l in lines:
        a, b, c, d = map(int, re.findall(r'\d+', l))
        act = next(x for x in ["toggle", "on", "off"] if x in l)
        for i, j in product(range(a, c + 1), range(b, d + 1)):
            if act == "on": g[i, j] += 1
            if act == "off": g[i, j] = max(g[i, j] - 1, 0)
            if act == "toggle": g[i, j] += 2

    print(sum(g.values()))

solve_2()
