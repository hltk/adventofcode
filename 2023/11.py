from aocd import data
from functools import cache
from itertools import product

g = data.split("\n")
n, m = len(g), len(g[0])

def ec(j):
    return all(g[i][j] == "." for i in range(n))
def er(i):
    return all(g[i][j] == "." for j in range(m))
@cache
def ecs(x, y):
    return sum(ec(j) for j in range(min(x, y), max(x, y) + 1))
@cache
def ers(x, y):
    return sum(er(i) for i in range(x, y))

for t in [2, 10 ** 6]:
    ans = 0
    for i, j in product(range(n), range(m)):
        if g[i][j] == "#":
            for ni, nj in product(range(i, n), range(m)):
                if g[ni][nj] == "#" and (ni > i or nj > j):
                    ans += (ni - i) + abs(nj - j) + (ers(i, ni) + ecs(j, nj)) * (t - 1)
    print(ans)
