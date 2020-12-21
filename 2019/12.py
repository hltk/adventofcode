import operator
import re

from aocd import data
from functools import reduce
from itertools import count
from itertools import repeat
from math import lcm

ints = lambda line: tuple(map(int, re.findall(r"-?\d+", line)))

pos = list(map(ints, data.split("\n")))
vel = list(repeat(tuple(repeat(0, 3)), len(pos)))

vec_add = lambda *l: tuple(sum(p) for p in zip(*l))
norm = lambda x: 0 if x == 0 else x // abs(x)
diffs = lambda p, oth: tuple(norm(ov - v) for v, ov in zip(p, oth))
reduce_vec_add = lambda *l: [vec_add(*p) for p in zip(*l)]
gen_grav = lambda p, pos: tuple(reduce(vec_add, (diffs(p, oth) for oth in pos)))

def step(pos, vel):
    grav = list(map(gen_grav, pos, repeat(pos)))
    vel = reduce_vec_add(vel, grav)
    pos = reduce_vec_add(pos, vel)
    return pos, vel

def simulate(times, pos, vel):
    for _ in range(times):
        pos, vel = step(pos, vel)
    return pos, vel

total = lambda p, v: reduce(operator.mul, (sum(map(abs, x)) for x in [p, v]))
r = simulate(1000, pos, vel)
print(sum(total(*x) for x in zip(*r)))

def coord_cycle(i, pos, vel):
    seen = set()
    for time in count(0):
        state = tuple(map(operator.itemgetter(i), pos + vel))
        if state in seen:
            return time
        seen.add(state)
        pos, vel = step(pos, vel)

cycles = map(coord_cycle, range(len(pos[0])), repeat(pos), repeat(vel))
print(reduce(lcm, cycles))
