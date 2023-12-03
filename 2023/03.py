from aocd import data

from collections import defaultdict
from itertools import starmap, chain, product
from math import prod

def neighbours8(i, j):
    for di, dj in product([-1, 0, 1], repeat=2):
        if (di, dj) != (0, 0):
            yield (i + di, j + dj)

g = data.strip().split("\n")
n, m = len(g), len(g[0])

d = defaultdict(list)
ans = 0

for i in range(n):
    j, k = 0, 0
    while j < m:
        while k < m and g[i][j].isdigit() == g[i][k].isdigit(): k += 1
        if g[i][j].isdigit():
            x = int(g[i][j : k])
            p = {*chain(*starmap(neighbours8, ((i, jj) for jj in range(j, k))))}
            p = [(i, j) for i, j in p if i in range(n) and j in range(m)]
            ans += x * any(not c.isdigit() and c != "." for c in starmap(lambda i, j: g[i][j], p))
            [d[i, j].append(x) for i, j in p if g[i][j] == "*"]
        j = k

print(ans)
print(sum(prod(v) for v in d.values() if len(v) == 2))
