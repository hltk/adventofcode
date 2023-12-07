from aocd import data
from itertools import count
import re

def i(x): return [*map(int, re.findall(r"\d+", x))]

seeds, *lines = data.split("\n\n")
seeds = i(seeds)
m = [sorted([(b, a, c) for a, b, c in map(i, l.split("\n")[1:])]) for l in lines]

def f(x, y=1):
    for mm in m[::y]:
        for a, b, c in mm:
            a, b = [a, b][::y]
            if 0 <= x - a < c:
                x = b + (x - a)
                break
    return x

def w(x): return any(0 <= x - a < b for a, b in zip(seeds[::2], seeds[1::2]))

p1 = min(map(f, seeds))
p2 = next(x for x in count(1) if w(f(x, -1)))

print(p1)
print(p2)
