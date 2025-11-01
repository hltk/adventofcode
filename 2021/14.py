from parse import findall, search
from aocd import data
from functools import reduce
import operator
from collections import Counter as C

s = search("{:l}", data)[0]
rules = {tuple(a): b for a, b in findall("{:l} -> {:l}", data)}

moves = [{x: C() for x in rules}]
for x in range(40):
    moves.append({})
    for a, b in rules:
        c = rules[a, b]
        moves[-1][a, b] = moves[-2][a, c] + moves[-2][c, b] + C(c)

u = C(s) + reduce(operator.add, map(moves[40].__getitem__, zip(s, s[1:])))
x = u.values()

print(max(x) - min(x))
