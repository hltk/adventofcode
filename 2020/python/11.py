from utils import *
from aocd import data


grid = data.split("\n")
n, m = len(grid), len(grid[0])


def step(seats, neigh, p1):
    def alive(i, j):
        if grid[i][j] == '.':
            return False
        ncnt = sum(map(seats.__contains__, neigh[(i, j)]))
        if (i, j) not in seats and ncnt == 0:
            return True
        if (i, j) in seats and ncnt < (4 if p1 else 5):
            return True
        return False
    return {(i, j) for i, j in product(range(n), range(m)) if alive(i, j)}


def find_first(i, j, vi, vj, p1):
    i, j = i + vi, j + vj
    while i in range(n) and j in range(m):
        if grid[i][j] != '.':
            yield i, j
            break
        if p1:
            break
        i, j = i + vi, j + vj


adj = set(product([-1, 0, 1], [-1, 0, 1])) - {(0, 0)}

def neighbours(i, j, p1):
    for vi, vj in adj:
        yield from find_first(i, j, vi, vj, p1)


def simulate(p1):
    seats = {(i, j) for i, j in product(range(n), range(m)) if grid[i][j] == '#'}
    neigh = {p: list(neighbours(*p, p1)) for p in product(range(n), range(m))}
    while (nxt := step(seats, neigh, p1)) != seats:
        seats = nxt
    return len(seats)


print(simulate(True))

print(simulate(False))
