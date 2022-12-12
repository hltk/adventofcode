from aocd import data
from itertools import product
from collections import defaultdict
from utils import *

grid = list(map(list, data.split("\n")))
n, m = len(grid), len(grid[0])

q, vis, dist = [], set(), {}

for i, j in product(range(n), range(m)):
    if grid[i][j] == 'S':
        e = i, j
        grid[i][j] = 'a'
    if grid[i][j] == 'E':
        grid[i][j] = 'z'
        q.append((i, j))
        vis.add((i, j))
        dist[i, j] = 0

while q:
    i, j = q.pop(0)
    for ni, nj in neighbours4(i, j):
        if ni in range(n) and nj in range(m):
            if (ni, nj) not in vis and ord(grid[i][j]) - ord(grid[ni][nj]) <= 1:
                vis.add((ni, nj))
                dist[ni, nj] = dist[i, j] + 1
                q.append((ni, nj))

print(dist[e])
print(min(v for (i, j), v in dist.items() if grid[i][j] == 'a'))
