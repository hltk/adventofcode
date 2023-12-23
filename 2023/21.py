from aocd import data

T = 26501365

def f(c):
    return c.real % 131 + c.imag % 131 * 1j

g = {
    i + 1j * j: c
    for i, r in enumerate(data.split("\n"))
    for j, c in enumerate(r) if c != "#"
}

t = {p for p, x in g.items() if x == "S"}
x, y = [], []

for i in range(450):
    if i == 64:
        print(len(t))

    if not (i - T) % 131:
        x, y = x + [len(x)], y + [len(t)]

    t = {p + d for p in t for d in [1, -1, -1j, 1j] if f(p + d) in g}

from sympy.polys.polyfuncs import interpolate
from sympy.abc import a
print(interpolate([*zip(x, y)], a).subs({a: T // 131}))
