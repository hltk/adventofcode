from itertools import product, count, takewhile
from aocd import data


grid = data.split("\n")
n, m = len(grid), len(grid[0])


def step(cells, neigh, p1):
    def alive(i, j):
        if grid[i][j] == '.':
            return False
        ncnt = sum(map(cells.__contains__, neigh[(i, j)]))
        if (i, j) not in cells and ncnt == 0:
            return True
        if (i, j) in cells and ncnt < (4 if p1 else 5):
            return True
        return False
    return {(i, j) for i, j in product(range(n), range(m)) if alive(i, j)}


def find_first(oi, oj, vi, vj, p1):
    def valid(p):
        return p[0] in range(n) and p[1] in range(m)
    for i, j in takewhile(valid, zip(count(oi + vi, vi), count(oj + vj, vj))):
        if grid[i][j] != '.':
            yield i, j
            break
        if p1:
            break


adj = set(product([-1, 0, 1], [-1, 0, 1])) - {(0, 0)}

def neighbours(i, j, p1):
    for vi, vj in adj:
        yield from find_first(i, j, vi, vj, p1)


def simulate(p1):
    cells = {(i, j) for i, j in product(range(n), range(m)) if grid[i][j] == '#'}
    neigh = {p: list(neighbours(*p, p1)) for p in product(range(n), range(m))}
    while (nxt := step(cells, neigh, p1)) != cells:
        cells = nxt
    return len(cells)


print(simulate(True))

print(simulate(False))
