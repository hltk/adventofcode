from utils import *
from aocd import data

grid = data.split("\n")

n, m = len(grid), len(grid[0])

def tree(i, j):
    return grid[i][j % m] == '#'

def check(di, dj):
    r = 0
    i, j = 0, 0
    while i < n:
        r += tree(i, j)
        i += di
        j += dj
    return r

print(check(1, 3))

R = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))

r = reduce(operator.mul, starmap(check, R))

print(r)
