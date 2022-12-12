from aocd import data
from itertools import product
from collections import defaultdict

def neighbours(i, j):
    yield i + 1, j
    yield i - 1, j
    yield i, j + 1
    yield i, j - 1

grid = list(map(list, data.split("\n")))
n, m = len(grid), len(grid[0])

vis = set()
dist = defaultdict(int)
q = []
it = 0

for i, j in product(range(n), range(m)):
    if grid[i][j] == 'S':
        e = i, j
        grid[i][j] = 'a'
    if grid[i][j] == 'E':
        grid[i][j] = 'z'
        q.append((i, j))
        vis.add((i, j))

while it < len(q):
    i, j = q[it]
    it += 1
    for ni, nj in neighbours(i, j):
        if ni in range(n) and nj in range(m) and (ni, nj) not in vis and ord(grid[i][j]) - ord(grid[ni][nj]) <= 1:
            vis.add((ni, nj))
            dist[ni, nj] = dist[i, j] + 1
            q.append((ni, nj))

print(dist[e])
print(min(dist[i, j] for i, j in product(range(n), range(m)) if grid[i][j] == 'a' and (i, j) in dist))
