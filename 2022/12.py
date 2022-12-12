from aocd import data
from itertools import product, starmap
from utils import *

grid = list(map(list, data.split("\n")))
n, m = len(grid), len(grid[0])
indices = {(i, j) for i, j in product(range(n), range(m))}
grid = dict(zip(indices, starmap(lambda i, j: grid[i][j], indices)))

e ,= (p for p in indices if grid[p] == 'E')
s ,= (p for p in indices if grid[p] == 'S')

grid[e] = 'z'
grid[s] = 'a'

q, vis, dist = [e], {e}, {e: 0}

for cur in iter(q):
    for nxt in neighbours4(*cur):
        if nxt in indices - vis:
            if ord(grid[cur]) - ord(grid[nxt]) <= 1:
                vis.add(nxt)
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

print(dist[s])
print(min(v for p, v in dist.items() if grid[p] == 'a'))
