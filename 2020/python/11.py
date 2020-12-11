from utils import *
from aocd import data

grid = data.split("\n")
n, m = len(grid), len(grid[0])

def find_first(i, j, vi, vj):
    i += vi
    j += vj
    while valid_coords(i, j) and grid[i][j] == '.':
        i += vi
        j += vj
    if valid_coords(i, j) and grid[i][j] != '.':
        return (i, j)
    return None


def neighbours(i, j):
    yield find_first(i, j, -1, 0)
    yield find_first(i, j, +1, 0)
    yield find_first(i, j, 0, -1)
    yield find_first(i, j, 0, +1)
    yield find_first(i, j, +1, +1)
    yield find_first(i, j, -1, +1)
    yield find_first(i, j, +1, -1)
    yield find_first(i, j, -1, -1)

def valid_coords(i, j):
    return 0 <= i < n and 0 <= j < m

seats = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            seats.add((i, j))

while True:
    new_seats = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                ncnt = 0
                for ni, nj in starfilter(valid_coords, filter(None, neighbours(i, j))):
                        if (ni, nj) in seats:
                            ncnt += 1
                if (i, j) not in seats and ncnt == 0:
                    new_seats.add((i, j))
                if (i, j) in seats and ncnt < 5:
                    new_seats.add((i, j))
    if new_seats == seats:
        break
    seats = new_seats
    print(len(seats))
