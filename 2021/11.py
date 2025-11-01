from aocd import data
from copy import deepcopy

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, 1, 0, -1]
*moves, = zip(di, dj)
grid = data.split("\n")
*grid, = map(lambda row: list(map(int, row)), grid)
N = len(grid)
assert len(grid[0]) == N
a = 0

for t in __import__('itertools').count(1):
    for i in range(N):
        for j in range(N):
            grid[i][j] += 1
    flashed = True
    oa = a
    while flashed:
        flashed = False
        for i in range(N):
            for j in range(N):
                if grid[i][j] > 9:
                    for di, dj in moves:
                        ni = i + di
                        nj = j + dj
                        if ni in range(N) and nj in range(N) and grid[ni][nj] != 0:
                            grid[ni][nj] += 1
                    grid[i][j] = 0
                    flashed = True
                    a += 1
    if a - oa == N * N:
        print(t)
        exit()
