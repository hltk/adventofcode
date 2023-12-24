from aocd import data
from sympy import *
from sympy.solvers import solve
from itertools import combinations
import re

ints = lambda l: [*map(int, re.findall(r"-?\d+", l))]

lb, ub = 200000000000000, 400000000000000
l = [ints(x) for x in data.split("\n")]

a = 0

for (ix, iy, _, ixv, iyv, _), (jx, jy, _, jxv, jyv, _) in combinations(l, 2):
    t0, t1 = symbols("t0, t1")
    if (v := solve([ix + ixv * t0 - jx - jxv * t1, iy + iyv * t0 - jy - jyv * t1], t0, t1)):
        t0, t1 = v.values()
        if t0 >= 0 and t1 >= 0 and lb <= ix + ixv * t0 <= ub and lb <= iy + iyv * t0 <= ub:
            a += 1

print(a)

x, y, z, xv, yv, zv = symbols('x, y, z, xv, yv, zv', integer=True)
ss = [x, y, z, xv, yv, zv]
eqs = []

for i in range(3):
    ix, iy, iz, ixv, iyv, izv = l[i]
    t = symbols(f"{i}t", integer=True)
    eqs += [ix + ixv * t - x - xv * t]
    eqs += [iy + iyv * t - y - yv * t]
    eqs += [iz + izv * t - z - zv * t]
    ss += [t]

v ,= solve(eqs, ss)
print(sum(v[:3]))
