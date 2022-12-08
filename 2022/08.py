from aocd import data
from itertools import count, dropwhile, starmap
from functools import reduce
from operator import mul, sub, itemgetter

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

grid = data.split("\n")
n, m = len(grid), len(grid[0])

def is_outside(ci, cj):
    return not (ci in range(n) and cj in range(m))

visible = set()
values = []

for i in range(n):
    for j in range(m):
        def trees_visible(di, dj):
            def inside_and_lower(cnt):
                ci, cj = i + di * cnt, j + dj * cnt
                return not is_outside(ci, cj) and grid[ci][cj] < grid[i][j]
            steps = next(dropwhile(inside_and_lower, count(1)))
            return steps, is_outside(i + di * steps, j + dj * steps)
        if sum(map(itemgetter(1), starmap(trees_visible, directions))):
            visible.add((i, j))
        values.append(reduce(mul, starmap(sub, starmap(trees_visible, directions))))

print(len(visible))
print(max(values))
