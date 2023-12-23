from itertools import product
from aocd import data

g = {(i, j): c for i, r in enumerate(data.split("\n")) for j, c in enumerate(r) if c != "#"}
S, = {p for p in g if p[0] == 0}
E, = {p for p in g if p[0] == 140}

ed = {(i, j): {(ni, nj) for di, dj in product([-1, 0, 1], repeat=2)
            if abs(di) + abs(dj) == 1 and (ni := i + di, nj := j + dj) in g}
      for i, j in g}

it = {x for x, y in ed.items() if len(y) > 2} | {S, E}

def dfs(p, t, pt):
    return 0 if p == t else max(
            (dfs(x, t, pt | {x}) + 1 for x in ed[p] - (it - {t}) - pt),
            default=-10 ** 9
    )

dists = {(a, b): x for a, b in product(it, it) if (x := dfs(a, b, {a})) > 0}

def brute(c, left):
    return 0 if c[-1] == E else max(
        (brute(c + [x], left - {x}) + dists[c[-1], x] for x in left if (c[-1], x) in dists),
        default=-10 ** 9
    )

print(brute([S], it - {S}))
