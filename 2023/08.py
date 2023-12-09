from itertools import cycle
from aocd import data
import re, math

sq, _, *m = data.split("\n")
sq = [int(c == "R") for c in sq]
m = [list(re.findall(r"[0-9A-Z]{3}", mm)) for mm in m]
m = {a: [b, c] for a, b, c in m}

def dist(x):
    for i, j in enumerate(cycle(sq)):
        if x.endswith("Z"):
            return i
        x = m[x][j]

print(dist("AAA"))
print(math.lcm(*map(dist, (u for u in m.keys() if u.endswith("A")))))
