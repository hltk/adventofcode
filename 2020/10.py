from aocd import data
from collections import Counter
from functools import cache

*l, = sorted([0, *map(int, data.split())])
l.append(max(l) + 3)

c = Counter(y - x for x, y in zip(l, l[1:]))

print(c[1] * c[3])

@cache
def calc(x):
    if x == 0:
        return 1
    return sum(map(calc, range(x-3, x))) if x in l else 0

print(calc(l[-1]))
