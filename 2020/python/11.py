from utils import *
from aocd import data

grid = data.split("\n")
n, m = len(grid), len(grid[0])

def find_first(i, j, vi, vj, p1):
    i += vi
    j += vj
    while i in range(n) and j in range(m):
        if grid[i][j] != '.':
            yield (i, j)
            break
        if p1:
            break
        i += vi
        j += vj


def neighbours(i, j, p1):
    yield from find_first(i, j, -1, 0, p1)
    yield from find_first(i, j, +1, 0, p1)
    yield from find_first(i, j, 0, -1, p1)
    yield from find_first(i, j, 0, +1, p1)
    yield from find_first(i, j, +1, +1, p1)
    yield from find_first(i, j, -1, +1, p1)
    yield from find_first(i, j, +1, -1, p1)
    yield from find_first(i, j, -1, -1, p1)

def step(seats, p1):
    def alive(i, j):
        if grid[i][j] == '.':
            return False
        ncnt = sum((ni, nj) in seats for ni, nj in neighbours(i, j, p1))
        if (i, j) not in seats and ncnt == 0:
            return True
        if (i, j) in seats and ncnt < (4 if p1 else 5):
            return True
        return False
    return {(i, j) for i, j in product(range(n), range(m)) if alive(i, j)}

def simulate(p1):
    seats = {(i, j) for i, j in product(range(n), range(m)) if grid[i][j] == '#'}
    while (nxt := step(seats, p1)) != seats:
        seats = nxt
    return len(seats)

print(simulate(True))

print(simulate(False))
