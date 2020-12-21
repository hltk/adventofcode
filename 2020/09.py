from aocd import data
from itertools import combinations
from more_itertools import windowed, substrings

*l, = map(int, data.split())

p1 = next(x for *a, x in windowed(l, 26) if x not in map(sum, combinations(a, 2)))
print(p1)

s = next(l for l in substrings(l) if len(l) > 1 and sum(l) == p1)
print(min(s) + max(s))
