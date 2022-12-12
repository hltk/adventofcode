from aocd import lines
from utils import *

grid = {(i, j): v for i, row in enumerate(lines) for j, v in enumerate(row)}

goal ,= (p for p in grid if grid[p] == 'E')
start ,= (p for p in grid if grid[p] == 'S')

grid[start] = 'a'
grid[goal] = 'z'

queue, dist = [goal], {goal: 0}

for cur in iter(queue):
    for nxt in neighbours4(*cur):
        if nxt in set(grid) - set(dist):
            if ord(grid[cur]) - ord(grid[nxt]) <= 1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)

print(dist[start])
print(min(v for p, v in dist.items() if grid[p] == 'a'))
